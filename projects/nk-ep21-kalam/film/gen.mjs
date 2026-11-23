// EP21 film generator: one HyperFrames project per narration clip.
//   node film/gen.mjs N01            → film/N01/ (index.html + compositions/pic|cap|ovl.html)
//   node film/gen.mjs N01 --to 5     → only lines q00..q05 (preview), fades out after the last one
// Inputs: script/lines.json, narration/align.json, shots/prompts.json, script/script.mjs.
// Pictures are read from assets/plates/NNN.jpg (shared/plates → out/img).
import { mkdirSync, writeFileSync, readFileSync, existsSync, symlinkSync, rmSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { r, scene, index, buildShots, rng, esc, sfx, FONTS } from "../kit/gen/lib.mjs";
import { grain } from "../kit/gen/caps.mjs";
import { TAGS, CLIPS } from "../script/script.mjs";
import { buildFx, cardBg, FULL } from "./fx.mjs"; // EP17 additions: graphics layer and chapter card picture

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const J = (p) => JSON.parse(readFileSync(join(ROOT, p), "utf8"));
const LINES = J("script/lines.json"), ALIGN = J("narration/align.json"), SHOTS = J("shots/prompts.json");

const C = { gold: "#f3d48a", cream: "#f6efdc", navy: "rgba(10,14,34,0.88)", ink: "#070a18" };
const CARD = 2.3; // chapter card, silent

// spoken weight of a piece of Tamil text (syllables)
function syl(t) {
  let n = 0; const cp = [...t];
  for (let i = 0; i < cp.length; i++) {
    const c = cp[i].codePointAt(0);
    if (c >= 0x0b85 && c <= 0x0b94) n += 1;
    else if (c >= 0x0b95 && c <= 0x0bb9) n += cp[i + 1] === "\u0bcd" ? 0.3 : 1;
    else if (/[0-9]/.test(cp[i])) n += 2.2;
  }
  return Math.max(n, 0.6);
}
const units = (t) => t.split(/(?<=[.?!…])\s+/).map((s) => s.trim()).filter(Boolean);
/** Break one sentence into caption chunks of at most `max` characters, at commas first, then evenly by words. */
function chunks(t, max = 76) {
  if ([...t].length <= max) return [t];
  const parts = t.split(/(?<=,)\s+/);
  const out = [];
  for (const p of parts) {
    if ([...p].length <= max) { out.push(p); continue; }
    const ws = p.split(/\s+/), k = Math.ceil([...p].length / max), per = Math.ceil(ws.length / k);
    for (let i = 0; i < ws.length; i += per) out.push(ws.slice(i, i + per).join(" "));
  }
  // glue very short pieces to a neighbour
  for (let i = out.length - 1; i > 0; i--) if ([...out[i]].length < 12 && [...(out[i - 1] + out[i])].length <= max + 8) { out[i - 1] += " " + out[i]; out.splice(i, 1); }
  return out;
}

// Camera moves [scale, x, y] → [scale, x, y]; cycled with a seeded shuffle so neighbours differ.
const MOVES = [
  { o: "50% 50%", a: [1.06, 0, 0], b: [1.14, 0, 0] },
  { o: "50% 45%", a: [1.15, 0, 0], b: [1.07, 0, 0] },
  { o: "40% 50%", a: [1.12, 34, 0], b: [1.12, -34, 0] },
  { o: "60% 50%", a: [1.12, -34, 0], b: [1.12, 34, 0] },
  { o: "50% 60%", a: [1.1, 0, 18], b: [1.15, 0, -14] },
  { o: "35% 40%", a: [1.07, 0, 0], b: [1.17, 0, 0] },
  { o: "65% 55%", a: [1.17, 0, 0], b: [1.08, 0, 0] },
];

// Hook effects (N01 only): [line q, effect, volume, where: "start" | "last" (last sentence of the line) | sentence number]
const HOOK_FX = [
  // date, time, place (three hits) → "he is Abdul Kalam" → the question → minister? scientist? a guard → three words → the promise → "come"
  [0, "impact-bass-1", 0.3, "start"], [2, "impact-bass-2", 0.3, "start"], [3, "whoosh", 0.16, "start"],
  [4, "impact-bass-1", 0.3, "last"], [6, "whoosh-cinematic", 0.16, "start"], [7, "riser", 0.18, "start"], [7, "impact-bass-2", 0.32, "last"],
];
// Chapter card backgrounds: one picture of the chapter behind the unchanged card (shot names from shots/shots.txt)
const CARD_BG = { N02: "airliner_monsoon_climb", N03: "young_man_selection_gate", N04: "control_room_1979", N05: "jeep_three_soldiers", N06: "stage_podium_wide", N07: "modest_room_door_open" };
const pad3 = (n) => String(n).padStart(3, "0");
const plateOf = (name) => { const s_ = SHOTS.find((x) => x.name === name); if (!s_) throw new Error("no shot named " + name); return pad3(s_.n); };

export function build(cid, opt = {}) {
  const clip = CLIPS.find((c) => c.id === cid), ci = CLIPS.indexOf(clip);
  const AL = ALIGN[cid];
  let L = LINES.filter((l) => l.clip === cid);
  const partial = opt.to != null && opt.to < L.length - 1;
  if (partial) L = L.filter((l) => l.q <= opt.to);
  const lead = ci === 0 ? 0.4 : CARD + 0.25;
  const aEnd = partial ? AL.lines[opt.to + 1].a0 - 0.12 : AL.dur;
  const D = r(lead + aEnd + (partial ? 0.9 : 0.6));
  const rand = rng(1100 + ci * 17);

  // ── line windows on the film clock
  const win = L.map((l, i) => {
    const a = AL.lines[l.q];
    return { q: l.q, t0: r(lead + a.a0), t1: r(lead + a.a1), end: r(i + 1 < L.length ? lead + AL.lines[l.q + 1].a0 : D), a, l };
  });

  // ── pictures
  const shots = [];
  let mv = Math.floor(rand() * MOVES.length);
  for (const w of win) {
    const fx = w.l.fx || {}, only = new Set(fx.only || []);
    // EP17: a line under a full-screen graphic has no pictures of its own (the last picture runs on underneath); pictures named in `only` belong to the graphic
    const S = FULL(fx) ? [] : fx.reuse ? fx.reuse.map((nm) => SHOTS.find((s) => s.name === nm)) : SHOTS.filter((s) => s.clip === cid && s.q === w.q && !only.has(s.name));
    const from = shots.length || w === win[0] ? (shots.length ? w.t0 - 0.14 : 0) : w.t0 - 0.14, to = w.end - 0.14, k = S.length;
    if (!k) { if (shots.length) shots.at(-1).t1 = r(to); continue; }
    // cut points: prefer pauses inside the line, at least 1.3 s apart; otherwise spread evenly
    const pauses = w.a.ph.slice(1).map((p) => lead + p[0] - 0.08);
    const cuts = [];
    for (let j = 1; j < k; j++) {
      const target = from + ((to - from) * j) / k;
      const near = pauses.filter((p) => Math.abs(p - target) < (to - from) / k / 2.6).sort((x, y) => Math.abs(x - target) - Math.abs(y - target))[0];
      cuts.push(near ?? target);
    }
    const edges = [from, ...cuts, to];
    const ok = edges.every((e, i) => i === 0 || e - edges[i - 1] >= 1.3);
    let E = ok ? edges : Array.from({ length: k + 1 }, (_, j) => from + ((to - from) * j) / k);
    if (fx.flash && k === fx.flash.length && w.a.un.length === k) E = [from, ...w.a.un.slice(1).map((u) => lead + u[0] - 0.1), to]; // one picture per flashed word
    if (fx.cuts && fx.cuts.length === k - 1) E = [from, ...fx.cuts.map((u) => lead + w.a.un[u][0] - 0.1), to]; // EP20: picture changes at the named sentences
    S.forEach((s, j) => {
      mv = (mv + 1 + Math.floor(rand() * 3)) % MOVES.length;
      shots.push({ plate: String(s.n).padStart(3, "0"), t0: r(E[j]), t1: r(E[j + 1]), cut: j > 0 ? 1 : 0, q: w.q, ...MOVES[mv] });
    });
  }
  shots[0].t0 = 0; shots.at(-1).t1 = D;
  const missing = SHOTS.filter((s) => s.clip === cid && !existsSync(join(ROOT, "out/img", pad3(s.n) + ".jpg"))).map((s) => pad3(s.n));
  // EP17: the hook cuts harder (short zoom-ins inside a line); the chapters keep the soft fades
  const P = buildShots(shots, { trans: (i, s) => (ci === 0 ? (s.cut ? { type: i % 2 ? "zoom" : "fade", d: 0.2 } : { type: "fade", d: 0.32 }) : s.cut ? { type: "fade", d: 0.24 } : { type: "fade", d: 0.5 }) });
  const G = grain("p-grain", D, rng(11 + ci), { opacity: 0.1 });

  // chapter card
  let cardCss = "", cardHtml = "", cardJs = "";
  if (ci > 0) {
    const bgName = CARD_BG[cid], bgOk = bgName && existsSync(join(ROOT, "out/img", plateOf(bgName) + ".jpg"));
    const KB = bgOk ? cardBg(plateOf(bgName), CARD) : { css: "", html: "", js: "" };
    cardCss = KB.css + `    ${FONTS.serifTa}
    ${FONTS.corm}
    #k-card { position: absolute; inset: 0; z-index: 80; }
    #k-bg { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 46%, #121a3c 0%, ${C.ink} 72%); }
    #k-num { position: absolute; left: 0; width: 1920px; top: 318px; text-align: center; font: 600 150px/1 "NK Cormorant", serif; letter-spacing: 0.08em; color: ${C.gold}; opacity: 0; }
    #k-rule { position: absolute; left: 860px; top: 500px; width: 200px; height: 3px; background: ${C.gold}; transform-origin: 50% 50%; opacity: 0; }
    #k-title { position: absolute; left: 0; width: 1920px; top: 536px; text-align: center; font: 700 104px/1.4 "NK Serif Tamil", serif; color: ${C.cream}; opacity: 0; }`;
    cardHtml = `    <div id="k-card" class="clip" data-start="0" data-duration="${r(CARD + 0.5)}" data-track-index="4">
      <div id="k-bg"></div>
${KB.html}      <div id="k-num">${clip.sec.split(" ")[0]}</div>
      <div id="k-rule"></div>
      <div id="k-title">${esc(clip.title)}</div>
    </div>\n`;
    cardJs = KB.js + `      tl.fromTo("#k-num", { opacity: 0, y: 18 }, { opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }, 0.12);
      tl.fromTo("#k-rule", { opacity: 0, scaleX: 0 }, { opacity: 1, scaleX: 1, duration: 0.5, ease: "expo.out" }, 0.34);
      tl.fromTo("#k-title", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.5, ease: "power3.out" }, 0.5);
      tl.to(["#k-num", "#k-rule", "#k-title"], { opacity: 0, duration: 0.3, ease: "power2.in" }, ${r(CARD - 0.35)});
      tl.to("#k-card", { opacity: 0, duration: 0.5, ease: "power1.inOut" }, ${CARD});\n`;
  }
  const fadeOut = partial || ci === CLIPS.length - 1;
  const outD = partial ? 0.7 : 1.4;
  const pic = scene({
    id: "pic",
    css: `${P.css}
${G.css}
${cardCss}
    #p-vig { position: absolute; inset: 0; z-index: 50; pointer-events: none; background: linear-gradient(180deg, rgba(4,6,14,0) 58%, rgba(4,6,14,0.7) 100%), radial-gradient(ellipse at 50% 46%, rgba(0,0,0,0) 52%, rgba(4,6,14,0.46) 100%); }
    #p-out { position: absolute; inset: 0; z-index: 90; }
    #p-out-fill { position: absolute; inset: 0; background: #000; opacity: 0; }`,
    html: `${P.html}    <div id="p-vig" data-layout-ignore></div>
${G.html}${cardHtml}${fadeOut ? `    <div id="p-out" class="clip" data-start="${r(D - outD)}" data-duration="${outD}" data-track-index="3"><div id="p-out-fill"></div></div>` : ""}`,
    js: `${P.js}${G.js}${cardJs}${fadeOut ? `      tl.fromTo("#p-out-fill", { opacity: 0 }, { opacity: 1, duration: ${r(outD - 0.05)}, ease: "power2.in" }, ${r(D - outD)});` : ""}`,
  });

  // ── captions: one chunk on screen at a time, timed inside each sentence by syllable weight
  let cHtml = "", cJs = "", n = 0;
  const caps = [];
  for (const w of win) {
    const U = units(w.l.cap);
    const un = w.a.un.length === U.length ? w.a.un : null;
    const totW = U.reduce((s, u) => s + syl(u), 0);
    let acc = 0;
    U.forEach((u, ui) => {
      const u0 = un ? lead + un[ui][0] : w.t0 + ((w.t1 - w.t0) * acc) / totW;
      const u1 = un ? lead + un[ui][1] : w.t0 + ((w.t1 - w.t0) * (acc + syl(u))) / totW;
      acc += syl(u);
      const ch = chunks(u), cw = ch.reduce((s, c) => s + syl(c), 0);
      let a2 = 0;
      for (const c of ch) { caps.push({ text: c, t0: u0 + ((u1 - u0) * a2) / cw, vEnd: u0 + ((u1 - u0) * (a2 + syl(c))) / cw, q: w.q }); a2 += syl(c); }
    });
  }
  // short neighbours inside one line share a caption (two lines on screen)
  const merged = [];
  for (const c of caps) {
    const p = merged.at(-1);
    if (p && p.q === c.q && [...(p.text + c.text)].length <= 40 && !/…$/.test(p.text)) { p.text += " " + c.text; p.vEnd = c.vEnd; }
    else merged.push({ ...c });
  }
  merged.forEach((c, i) => {
    const start = r(Math.max(0.05, c.t0 - 0.07));
    const nx = merged[i + 1];
    const end = r(Math.min(nx ? nx.t0 - 0.09 : D - 0.1, c.vEnd + 0.5));
    const id = `c${++n}`;
    cHtml += `    <div id="${id}" class="c-cap clip" data-start="${start}" data-duration="${r(end - start)}" data-track-index="1"><div id="${id}-in" class="c-in">${esc(c.text).replace(/(\S+-\S+)/g, '<span style="white-space:nowrap">$1</span>')}</div></div>\n`; // a token like 10-ல must not break at its hyphen
    cJs += `      tl.fromTo("#${id}-in", { opacity: 0, y: 6 }, { opacity: 1, y: 0, duration: 0.16, ease: "power2.out" }, ${start});
      tl.to("#${id}-in", { opacity: 0, duration: 0.1, ease: "power2.in" }, ${r(end - 0.11)});\n`;
  });
  const cap = scene({
    id: "cap",
    css: `    ${FONTS.sansTa}
    .c-cap { position: absolute; left: 190px; width: 1540px; bottom: 84px; text-align: center; }
    .c-in { opacity: 0; font: 560 52px/1.4 "NK Sans Tamil", sans-serif; color: #ffffff; text-wrap: balance; text-shadow: 0 0 5px rgba(0,0,0,0.95), 0 2px 12px rgba(0,0,0,0.9), 0 0 40px rgba(0,0,0,0.75); }`,
    html: cHtml, js: cJs,
  });

  // ── evidence tags (small, top left) — consecutive lines with the same tag share one pill
  let oHtml = "", oJs = "", tn = 0;
  for (let i = 0; i < win.length; i++) {
    const tag = win[i].l.tag; if (!tag) continue;
    let j = i; while (j + 1 < win.length && win[j + 1].l.tag === tag) j++;
    const start = r(win[i].t0 - 0.05), end = r(Math.min(win[j].t1 + 0.45, win[j].end - 0.05));
    const id = `g${++tn}`;
    oHtml += `    <div id="${id}" class="o-tag clip" data-start="${start}" data-duration="${r(end - start)}" data-track-index="1"><div id="${id}-in" class="o-in"><span class="o-dot"></span><span class="o-tx">${esc(TAGS[tag])}</span></div></div>\n`;
    oJs += `      tl.fromTo("#${id}-in", { opacity: 0, x: -14 }, { opacity: 1, x: 0, duration: 0.28, ease: "power3.out" }, ${start});
      tl.to("#${id}-in", { opacity: 0, duration: 0.2, ease: "power2.in" }, ${r(end - 0.22)});\n`;
    i = j;
  }
  // ── subscribe pop-up (chapter 1 only): silent, 5 s, top right
  let sCss = "", sHtml = "", sJs = "";
  if (ci === 1 && !partial) {
    const w5 = win.find((x) => x.q === 2) ?? win[Math.min(2, win.length - 1)]; // EP21: the turbulence line (7.5 s, no graphic on screen)
    const T0 = r(w5.t0), BX = 648, BY = 76;
    const BELL = "M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z";
    sCss = `
    ${FONTS.oswald}
    #s-pop { position: absolute; left: 1036px; top: 52px; width: 820px; height: 400px; }
    #s-card { position: absolute; left: 0; top: 0; width: 820px; height: 148px; border-radius: 26px; background: ${C.navy}; border: 1.5px solid rgba(243,212,138,0.55); box-shadow: 0 10px 40px rgba(0,0,0,0.55); opacity: 0; }
    #s-logo { position: absolute; left: 20px; top: 20px; width: 108px; height: 108px; border-radius: 54px; border: 2.5px solid ${C.gold}; object-fit: cover; }
    #s-name { position: absolute; left: 150px; top: 28px; width: 360px; font: 650 35px/1.4 "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; }
    #s-at { position: absolute; left: 152px; top: 88px; width: 360px; font: 500 26px/1.3 "NK Oswald", sans-serif; letter-spacing: 0.03em; color: ${C.gold}; white-space: nowrap; }
    #s-btn { position: absolute; left: 528px; top: 34px; width: 270px; height: 80px; }
    .s-face { position: absolute; inset: 0; border-radius: 40px; display: flex; align-items: center; justify-content: center; gap: 10px; font: 600 35px/1 "NK Oswald", sans-serif; letter-spacing: 0.04em; color: #fff; }
    #s-red { background: #e8201f; box-shadow: 0 6px 26px rgba(232,32,31,0.45); }
    #s-grey { background: #30333b; border: 2px solid rgba(255,255,255,0.14); opacity: 0; font-size: 31px; }
    #s-cur { position: absolute; left: 0; top: 0; width: 50px; height: 50px; opacity: 0; filter: drop-shadow(0 3px 6px rgba(0,0,0,0.7)); }`;
    sHtml = `    <div id="s-pop" class="clip" data-start="${T0}" data-duration="5" data-track-index="2" data-layout-allow-overflow>
      <div id="s-card">
        <img id="s-logo" src="assets/brand/logo_512.jpg" alt="" />
        <div id="s-name">நிலவன் கதைகள்</div>
        <div id="s-at">@NilavanKadhaigal</div>
        <div id="s-btn">
          <div id="s-red" class="s-face">SUBSCRIBE</div>
          <div id="s-grey" class="s-face"><svg id="s-bell" width="32" height="32" viewBox="0 0 24 24"><path d="${BELL}" fill="${C.gold}"/></svg><span>SUBSCRIBED</span></div>
        </div>
      </div>
      <svg id="s-cur" viewBox="0 0 24 24"><path d="M4 2v17l4.6-4.3 3 6.8 2.7-1.2-3-6.7 6.3-.4z" fill="#fff" stroke="#111" stroke-width="1.3" stroke-linejoin="round"/></svg>
    </div>\n`;
    const K = r(T0 + 2.1); // the click
    sJs = `      tl.fromTo("#s-card", { opacity: 0, x: 70 }, { opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }, ${r(T0 + 0.05)});
      tl.fromTo("#s-cur", { x: 760, y: 300, opacity: 0 }, { x: ${BX}, y: ${BY}, opacity: 1, duration: 0.75, ease: "power2.inOut" }, ${r(K - 0.9)});
      tl.to("#s-cur", { scale: 0.8, duration: 0.08, ease: "power2.in" }, ${r(K - 0.06)});
      tl.to("#s-cur", { scale: 1, duration: 0.16, ease: "power2.out" }, ${r(K + 0.04)});
      tl.to("#s-btn", { scale: 0.92, duration: 0.08, ease: "power2.in" }, ${r(K - 0.04)});
      tl.to("#s-btn", { scale: 1, duration: 0.3, ease: "back.out(2.4)" }, ${r(K + 0.05)});
      tl.to("#s-red", { opacity: 0, duration: 0.14 }, ${K});
      tl.to("#s-grey", { opacity: 1, duration: 0.14 }, ${K});
      tl.fromTo("#s-bell", { rotation: 0 }, { rotation: 16, duration: 0.09, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 10%" }, ${r(K + 0.12)});
      tl.to("#s-cur", { x: 800, y: 290, opacity: 0, duration: 0.6, ease: "power2.in" }, ${r(K + 0.8)});
      tl.to("#s-card", { opacity: 0, x: 50, duration: 0.4, ease: "power2.in" }, ${r(T0 + 4.5)});\n`;
  }
  const ovl = scene({
    id: "ovl",
    css: `    ${FONTS.sansTa}${sCss}
    .o-tag { position: absolute; left: 64px; top: 56px; width: 680px; height: 64px; }
    .o-in { opacity: 0; display: inline-flex; align-items: center; gap: 14px; padding: 9px 24px 9px 18px; border-radius: 34px; background: ${C.navy}; border: 1.5px solid rgba(243,212,138,0.55); }
    .o-dot { width: 12px; height: 12px; border-radius: 50%; background: ${C.gold}; }
    .o-tx { font: 600 30px/1.4 "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; }`,
    html: (oHtml || `    <div id="g0" class="o-tag clip" data-start="0" data-duration="0.1" data-track-index="1"></div>\n`) + sHtml, js: oJs + sJs,
  });

  // ── sound: narration, plus effects in the hook only
  const audio = [{ id: "vo", src: `assets/vo/${cid}.mp3`, start: lead, dur: r(Math.min(AL.dur, aEnd)), vol: 1 }];
  if (ci === 0)
    for (const [q, name, vol, where] of HOOK_FX) {
      const w = win.find((x) => x.q === q); if (!w) continue;
      const t = where === "last" ? lead + w.a.un.at(-1)[0] : typeof where === "number" ? lead + w.a.un[where][0] - 0.05 : q === 0 ? 0.1 : w.t0 - 0.14;
      audio.push(sfx(name, t, vol, D));
    }

  // ── EP17 graphics layer (film/fx.mjs)
  const FXR = buildFx({ cid, win, lead, D, plateOf, shotsOf: (q) => SHOTS.filter((s) => s.clip === cid && s.q === q).map((s) => ({ plate: pad3(s.n), name: s.name })) });
  const gfx = scene({ id: "gfx", css: FXR.css, html: FXR.html, js: FXR.js });
  audio.push(...FXR.audio);

  // ── write
  const dir = join(ROOT, "film", cid);
  mkdirSync(join(dir, "compositions"), { recursive: true });
  writeFileSync(join(dir, "index.html"), index({ title: `EP21 ${cid} ${clip.slug}`, dur: D, bg: "#000", hosts: [{ id: "pic" }, { id: "gfx" }, { id: "ovl" }, { id: "cap", kind: "captions" }], audio }));
  writeFileSync(join(dir, "compositions/pic.html"), pic);
  writeFileSync(join(dir, "compositions/gfx.html"), gfx);
  writeFileSync(join(dir, "compositions/cap.html"), cap);
  writeFileSync(join(dir, "compositions/ovl.html"), ovl);
  writeFileSync(join(dir, "hyperframes.json"), JSON.stringify({ $schema: "https://hyperframes.heygen.com/schema/hyperframes.json", registry: "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry", paths: { blocks: "compositions", components: "compositions/components", assets: "assets" }, media: { autoProxy: true } }, null, 2) + "\n");
  writeFileSync(join(dir, "meta.json"), JSON.stringify({ id: `nk-ep21-${cid}`, name: `EP21 ${cid}`, createdAt: "2026-11-21T09:00:00.000Z" }, null, 2) + "\n");
  const link = join(dir, "assets");
  rmSync(link, { recursive: true, force: true });
  symlinkSync("../../shared", link);
  console.log(`${cid}: ${D}s, ${shots.length} pictures, ${merged.length} captions, ${tn} tags, ${audio.length - 1} effects${missing.length ? `, MISSING ${missing.length}: ${missing[0]}…${missing.at(-1)}` : ""}`);
  return { D, shots, caps: merged };
}

const args = process.argv.slice(2);
if (args.length) {
  const to = args.includes("--to") ? Number(args[args.indexOf("--to") + 1]) : null;
  for (const a of args.filter((x) => /^N\d\d$/.test(x))) build(a, { to });
}
