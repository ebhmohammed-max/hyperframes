// EP17 added picture language (20 Nov 2026). Nothing here changes the existing look: captions, tags, chapter card type and
// sound, subscribe pop-up and camera moves stay in gen.mjs as they were. This file adds one more layer ("gfx", between the
// pictures and the tags) that is filled only where a script line asks for it with its 4th field:
//   clock [h, m, label]                  small clock badge, top right, at the start of a chapter
//   stat  [big, label, source, at?]      number card on the left (at = sentence of the line where it appears)
//   vs    [title, [label, value, n], [label, value, n], at?]   two bars, then and now
//   line  [[year, label, at], …]         small timeline on the left
//   big   [number, unit, label, at?]     one giant number over the dimmed picture
//   flash [words…] (+ strike)            one big word per sentence of the line
//   split {L, R, a, b, at, until?}       two pictures side by side with a year on each (a, b = shot names)
//   coins 1 · dots [lit, title, sub, mode?, from?] · map "presidency" | "boat1…4" · mock "ticket" | "paper" | "postcard" | "telegram" | "intertitle"
// Full-screen graphics (coins, dots, map, paper, postcard, telegram) carry their own background; the pictures of that line,
// if any, are shown inside the graphic as photo cards.
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { r, esc, sfx, rng, FONTS } from "../kit/gen/lib.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const GEO = JSON.parse(readFileSync(join(HERE, "geo.json"), "utf8"));
const C = { gold: "#f3d48a", cream: "#f6efdc", navy: "rgba(10,14,34,0.88)", ink: "#070a18", red: "#d8493f", paper: "#e9dfc4", inkp: "#2a2118" };
export const FULL = (fx) => !!fx && (fx.coins || fx.dots || fx.map || ["paper", "postcard", "telegram"].includes(fx.mock));

// ── map geometry: plain equirectangular projection around 11°N, 100 px per degree before the camera zoom
const LON0 = 71.5, LAT1 = 23, KX = 100 * Math.cos((11 * Math.PI) / 180), KY = 100;
const P = (lon, lat) => [r((lon - LON0) * KX), r((LAT1 - lat) * KY)];
const dPath = (rings, close = true) => rings.map((g) => "M" + g.map(([a, b]) => P(a, b).join(",")).join("L") + (close ? "Z" : "")).join("");
const lineLen = (pts) => pts.reduce((s, p, i) => (i ? s + Math.hypot(p[0] - pts[i - 1][0], p[1] - pts[i - 1][1]) : 0), 0);
// Madras Presidency about 1926, drawn by hand from district lists and clipped to the coast: an approximate outline (shown with that label).
const PRES = [[86, 19.9], [84.75, 19.75], [84.3, 19.95], [83.4, 19.6], [82.6, 19.9], [81.9, 19.3], [81.4, 18.3], [81, 17.8], [80.6, 17.75], [80.4, 17.2], [80.3, 16.85], [79.9, 16.75], [79.5, 16.5], [79.2, 16.55], [78.9, 16.1], [78.2, 15.9], [77.4, 15.9], [76.6, 15.4], [76, 15], [75.85, 14.6], [76.3, 14.45], [76.85, 14.3], [77, 13.85], [77.6, 13.75], [78.25, 13.6], [78.35, 13.1], [78.3, 12.75], [78.05, 12.75], [77.8, 12.85], [77.6, 12.75], [77.35, 12.4], [77.15, 12.3], [76.95, 12.15], [76.9, 11.85], [76.6, 11.65], [76.35, 11.75], [76.1, 11.9], [75.85, 12.05], [75.65, 12.15], [75.45, 12.4], [75.45, 12.75], [75.6, 12.95], [75.3, 13.2], [75.1, 13.5], [74.95, 13.85], [74.75, 13.95], [74.55, 13.95], [73.8, 13.9], [75, 10.3], [76, 10.52], [76.25, 10.65], [76.45, 10.6], [76.7, 10.6], [76.9, 10.55], [77, 10.3], [77.2, 10.15], [77.25, 9.85], [77.2, 9.6], [77.25, 9.2], [77.2, 8.95], [77.35, 8.9], [77.4, 8.5], [77.55, 8.25], [77.6, 8.12], [77.7, 7.6], [82, 7.6], [86.5, 14], [86.5, 19.9]];
const RAIL_IN = [[80.26, 13.08], [79.97, 12.69], [79.49, 11.94], [79.69, 11.4], [79.65, 11.1], [79.14, 10.79], [78.69, 10.8], [78.12, 9.92], [78.48, 9.69], [78.83, 9.37], [79.12, 9.28], [79.21, 9.28], [79.42, 9.18]];
const FERRY = [[79.42, 9.18], [79.73, 9.1]];
const RAIL_LK = [[79.73, 9.1], [79.9, 8.98], [80.48, 8.54], [80.4, 8.33], [80.36, 7.48], [80.3, 7.33], [80.02, 7.08], [79.85, 6.93]];

/** Camera: put (lon, lat) at screen point (sx, sy) with zoom z. */
const cam = (lon, lat, z, sx = 960, sy = 540) => { const [x, y] = P(lon, lat); return { x: r(sx - z * x), y: r(sy - z * y), scale: z }; };
const camJs = (c) => `{ x: ${c.x}, y: ${c.y}, scale: ${c.scale}, transformOrigin: "0 0", force3D: false }`;

function mapBase(id) {
  const land = dPath([...GEO.c.IN, ...GEO.c.LK, ...(GEO.c.BD || [])]);
  let grid = "";
  for (let lo = 72; lo <= 89; lo += 1) grid += `M${P(lo, 23).join(",")}L${P(lo, 4.5).join(",")}`;
  for (let la = 5; la <= 23; la += 1) grid += `M${P(71.5, la).join(",")}L${P(89.5, la).join(",")}`;
  return { land, grid, css: `
    #${id} { position: absolute; inset: 0; }
    #${id}-in { position: absolute; inset: 0; opacity: 0; background: radial-gradient(ellipse at 40% 45%, #22343a 0%, #16242a 60%, #0f1a1f 100%); overflow: hidden; }
    #${id} svg { position: absolute; left: 0; top: 0; overflow: visible; }
    #${id}-cam { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 0 0; }
    #${id} .m-grid { fill: none; stroke: rgba(190,215,210,0.07); }
    #${id} .m-land { fill: #2b3d42; stroke: #a9bab6; stroke-linejoin: round; }
    #${id} .m-state { fill: none; stroke: rgba(169,186,182,0.28); stroke-dasharray: 3 3; }
    #${id} .m-t { font-family: "NK Serif Tamil", serif; fill: #d9e2dc; }
    #${id} .m-sea { font-family: "NK Serif Tamil", serif; fill: rgba(190,215,210,0.42); letter-spacing: 0.08em; }
    #${id} .m-vig { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 46%, rgba(0,0,0,0) 55%, rgba(4,8,12,0.55) 100%), linear-gradient(180deg, rgba(4,8,12,0) 66%, rgba(4,8,12,0.72) 100%); }
    #${id} .m-card { position: absolute; left: 1050px; top: 120px; width: 760px; height: 428px; padding: 12px; background: #efe8d6; box-shadow: 0 18px 50px rgba(0,0,0,0.6); opacity: 0; }
    #${id} .m-card img { width: 736px; height: 404px; object-fit: cover; display: block; }
    #${id} .m-note { position: absolute; right: 64px; top: 60px; font: 500 24px/1.3 "NK Sans Tamil", sans-serif; color: rgba(217,226,220,0.6); }
    #${id} .m-chip { position: absolute; padding: 10px 22px; border-radius: 10px; background: ${C.navy}; border: 1.5px solid rgba(243,212,138,0.55); font: 600 34px/1.35 "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; opacity: 0; }
    #${id} .m-chip b { color: ${C.gold}; font-weight: 700; }` };
}

export function buildFx({ cid, win, lead, D, shotsOf, plateOf }) {
  let css = `    ${FONTS.sansTa}\n    ${FONTS.serifTa}\n    ${FONTS.corm}\n    ${FONTS.oswald}\n    ${FONTS.kavi}\n    ${FONTS.elite}
    .fxb { position: absolute; inset: 0; }
    .fx-full { position: absolute; inset: 0; opacity: 0; background: radial-gradient(ellipse at 50% 44%, #141d40 0%, ${C.ink} 74%); overflow: hidden; }
    .fx-sh { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(4,6,14,0) 62%, rgba(4,6,14,0.78) 100%); }`;
  let html = "", js = "", n = 0;
  const audio = [];
  const U = (w, i) => { const un = w.a.un; if (!un.length) return w.t0; const k = Math.min(Math.floor(i), un.length - 1), f = i - Math.floor(i); return r(lead + un[k][0] + (un[k][1] - un[k][0]) * f); };
  const Ue = (w, i) => r(lead + w.a.un[Math.min(i, w.a.un.length - 1)][1]);
  const blk = (id, t0, t1, inner, track = 1) => { html += `    <div id="${id}" class="fxb clip" data-start="${r(t0)}" data-duration="${r(t1 - t0)}" data-track-index="${track}" data-layout-allow-overflow>\n${inner}\n    </div>\n`; };
  const inOut = (sel, t0, t1, fi = 0.3, fo = 0.3) => { js += `      tl.fromTo("${sel}", { opacity: 0 }, { opacity: 1, duration: ${fi}, ease: "power2.out" }, ${r(t0)});\n      tl.to("${sel}", { opacity: 0, duration: ${fo}, ease: "power2.in" }, ${r(t1 - fo - 0.02)});\n`; };
  const snd = (name, t, vol) => audio.push(sfx(name, t, vol, D));

  for (let wi = 0; wi < win.length; wi++) {
    const w = win[wi], fx = w.l.fx; if (!fx) continue;
    const id = `x${++n}`, t0 = r(Math.max(0.05, w.t0 - 0.1)), tE = r(w.end - 0.12);

    // ── clock badge
    if (fx.clock) {
      const [h, m, lab] = fx.clock, a0 = t0 + 0.15, a1 = Math.min(tE, a0 + 3.6), cid2 = `${id}k`;
      const hDeg = ((h % 12) + m / 60) * 30, mDeg = m * 6;
      css += `
    #${cid2}-c { position: absolute; right: 64px; top: 52px; width: 372px; height: 148px; border-radius: 26px; background: ${C.navy}; border: 1.5px solid rgba(243,212,138,0.55); box-shadow: 0 10px 40px rgba(0,0,0,0.5); opacity: 0; }
    #${cid2}-f { position: absolute; left: 20px; top: 18px; width: 112px; height: 112px; border-radius: 50%; border: 3px solid ${C.gold}; background: radial-gradient(circle, #1b2550 0%, #0b1026 100%); }
    #${cid2}-h, #${cid2}-m { position: absolute; left: 53px; bottom: 53px; width: 6px; border-radius: 3px; background: ${C.cream}; transform-origin: 50% 100%; }
    #${cid2}-h { height: 30px; } #${cid2}-m { height: 44px; width: 4px; left: 54px; background: ${C.gold}; }
    #${cid2}-d { position: absolute; left: 51px; top: 51px; width: 10px; height: 10px; border-radius: 50%; background: ${C.gold}; }
    #${cid2}-t { position: absolute; left: 154px; top: 16px; width: 210px; font: 600 62px/1.1 "NK Oswald", sans-serif; letter-spacing: 0.02em; color: ${C.cream}; white-space: nowrap; }
    #${cid2}-l { position: absolute; left: 156px; top: 90px; width: 210px; font: 600 30px/1.3 "NK Sans Tamil", sans-serif; color: ${C.gold}; white-space: nowrap; }`;
      blk(cid2, a0, a1, `      <div id="${cid2}-c"><div id="${cid2}-f"><div id="${cid2}-h"></div><div id="${cid2}-m"></div><div id="${cid2}-d"></div></div><div id="${cid2}-t">${h}:${String(m).padStart(2, "0")}</div><div id="${cid2}-l">${esc(lab)} · 1926</div></div>`, 3);
      js += `      tl.fromTo("#${cid2}-c", { opacity: 0, x: 60 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, ${r(a0)});
      tl.fromTo("#${cid2}-h", { rotation: ${r(hDeg - 60)} }, { rotation: ${r(hDeg)}, duration: 1.1, ease: "power3.out" }, ${r(a0 + 0.1)});
      tl.fromTo("#${cid2}-m", { rotation: ${r(mDeg - 720)} }, { rotation: ${r(mDeg)}, duration: 1.1, ease: "power3.out" }, ${r(a0 + 0.1)});
      tl.to("#${cid2}-c", { opacity: 0, x: 40, duration: 0.35, ease: "power2.in" }, ${r(a1 - 0.4)});\n`;
    }

    // ── number card
    if (fx.stat) {
      const [big, lab, src, at] = fx.stat, a0 = Math.max(t0, U(w, at ?? w.a.un.length - 1) - 0.05), a1 = tE;
      css += `
    #${id}-c { position: absolute; left: 64px; top: 150px; padding: 18px 34px 20px 30px; background: ${C.navy}; border-left: 6px solid ${C.gold}; border-radius: 4px 14px 14px 4px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); opacity: 0; }
    #${id}-b { font: 600 104px/1.15 "NK Oswald", "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; }
    #${id}-l { font: 600 34px/1.4 "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; }
    #${id}-s { margin-top: 4px; font: 500 25px/1.4 "NK Sans Tamil", sans-serif; color: ${C.gold}; white-space: nowrap; }`;
      blk(id, a0, a1, `      <div id="${id}-c"><div id="${id}-b">${esc(big)}</div><div id="${id}-l">${esc(lab)}</div><div id="${id}-s">${esc(src)}</div></div>`, 1);
      js += `      tl.fromTo("#${id}-c", { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, ${r(a0)});
      tl.fromTo("#${id}-b", { scale: 0.7, transformOrigin: "0% 60%" }, { scale: 1, duration: 0.5, ease: "back.out(2)" }, ${r(a0 + 0.05)});
      tl.to("#${id}-c", { opacity: 0, duration: 0.25, ease: "power2.in" }, ${r(a1 - 0.28)});\n`;
      snd("pop", a0 + 0.1, 0.1);
    }

    // ── then and now bars
    if (fx.vs) {
      const [title, A, B, at] = fx.vs, a0 = Math.max(t0, U(w, at ?? 2) - 0.05), aB = U(w, (at ?? 2) + 1), a1 = tE;
      const wA = Math.max(4, Math.round((A[2] / B[2]) * 100));
      css += `
    #${id}-c { position: absolute; left: 64px; top: 150px; width: 800px; padding: 22px 30px 26px; background: ${C.navy}; border-left: 6px solid ${C.gold}; border-radius: 4px 14px 14px 4px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); opacity: 0; }
    #${id}-c .v-t { font: 600 30px/1.4 "NK Sans Tamil", sans-serif; color: ${C.gold}; margin-bottom: 8px; }
    #${id}-c .v-l { font: 500 26px/1.4 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.8); margin-top: 10px; }
    #${id}-c .v-r { display: flex; align-items: center; gap: 18px; height: 62px; }
    #${id}-c .v-bar { height: 34px; border-radius: 4px; transform-origin: 0% 50%; }
    #${id}-a { width: ${r(wA * 4.6)}px; background: ${C.cream}; } #${id}-b { width: 460px; background: ${C.gold}; }
    #${id}-c .v-v { font: 600 46px/1.2 "NK Oswald", "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; }`;
      blk(id, a0, a1, `      <div id="${id}-c"><div class="v-t">${esc(title)}</div><div class="v-l">${esc(A[0])}</div><div class="v-r"><div id="${id}-a" class="v-bar"></div><div id="${id}-av" class="v-v">${esc(A[1])}</div></div><div id="${id}-bl" class="v-l">${esc(B[0])}</div><div id="${id}-br" class="v-r"><div id="${id}-b" class="v-bar"></div><div id="${id}-bv" class="v-v">${esc(B[1])}</div></div></div>`, 1);
      js += `      tl.fromTo("#${id}-c", { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, ${r(a0)});
      tl.fromTo("#${id}-a", { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "power3.out" }, ${r(a0 + 0.2)});
      tl.fromTo("#${id}-av", { opacity: 0 }, { opacity: 1, duration: 0.3 }, ${r(a0 + 0.35)});
      tl.fromTo(["#${id}-bl", "#${id}-br"], { opacity: 0 }, { opacity: 1, duration: 0.3 }, ${r(aB)});
      tl.fromTo("#${id}-b", { scaleX: 0 }, { scaleX: 1, duration: 1.1, ease: "power2.out" }, ${r(aB + 0.05)});
      tl.to("#${id}-c", { opacity: 0, duration: 0.25, ease: "power2.in" }, ${r(a1 - 0.28)});\n`;
      snd("pop", a0 + 0.1, 0.1);
    }

    // ── small timeline
    if (fx.line) {
      const N = fx.line, a0 = Math.max(t0, U(w, N[0][2]) - 0.05), a1 = tE, Wd = 400, tot = Wd * (N.length - 1);
      css += `
    #${id}-c { position: absolute; left: 64px; top: 150px; width: ${tot + 400}px; height: 178px; background: ${C.navy}; border-left: 6px solid ${C.gold}; border-radius: 4px 14px 14px 4px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); opacity: 0; }
    #${id}-r { position: absolute; left: 200px; top: 82px; width: ${tot}px; height: 3px; background: ${C.gold}; transform-origin: 0% 50%; }
    #${id}-c .t-n { position: absolute; top: 14px; width: 390px; margin-left: -195px; text-align: center; }
    #${id}-c .t-y { font: 600 50px/1.15 "NK Oswald", "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; }
    #${id}-c .t-d { width: 16px; height: 16px; border-radius: 50%; background: ${C.gold}; margin: 4px auto 12px; }
    #${id}-c .t-l { font: 500 27px/1.3 "NK Sans Tamil", sans-serif; color: ${C.gold}; white-space: nowrap; }`;
      blk(id, a0, a1, `      <div id="${id}-c"><div id="${id}-r"></div>${N.map((p, i) => `<div id="${id}-n${i}" class="t-n" style="left: ${200 + i * Wd}px"><div class="t-y">${esc(p[0])}</div><div class="t-d"></div><div class="t-l">${esc(p[1])}</div></div>`).join("")}</div>`, 1);
      js += `      tl.fromTo("#${id}-c", { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, ${r(a0)});\n      tl.fromTo("#${id}-r", { scaleX: 0 }, { scaleX: 0.001, duration: 0.01 }, ${r(a0)});\n`;
      N.forEach((p, i) => {
        const t = i ? Math.max(a0 + 0.3, U(w, p[2]) - 0.05) : a0 + 0.1;
        js += `      tl.fromTo("#${id}-n${i}", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }, ${r(t + (i ? 0.25 : 0))});\n`;
        if (i) js += `      tl.to("#${id}-r", { scaleX: ${r(i / (N.length - 1))}, duration: 0.5, ease: "power2.inOut" }, ${r(t - 0.2)});\n`;
      });
      js += `      tl.to("#${id}-c", { opacity: 0, duration: 0.25, ease: "power2.in" }, ${r(a1 - 0.28)});\n`;
    }

    // ── one giant number over the dimmed picture
    if (fx.big) {
      const [num, unit, lab, at] = fx.big, a0 = Math.max(t0, U(w, at ?? 1) - 0.12), a1 = tE;
      css += `
    #${id}-d { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 42%, rgba(7,10,24,0.74) 0%, rgba(7,10,24,0.9) 80%); opacity: 0; }
    #${id}-n { position: absolute; left: 0; width: 1920px; top: 150px; text-align: center; font: 600 440px/1 "NK Cormorant", serif; font-variant-numeric: lining-nums; font-feature-settings: "lnum" 1; color: ${C.gold}; opacity: 0; text-shadow: 0 10px 60px rgba(0,0,0,0.6); }
    #${id}-u { position: absolute; left: 0; width: 1920px; top: 600px; text-align: center; font: 700 84px/1.4 "NK Serif Tamil", serif; color: ${C.cream}; opacity: 0; }
    #${id}-l { position: absolute; left: 0; width: 1920px; top: 726px; text-align: center; font: 500 32px/1.4 "NK Sans Tamil", sans-serif; color: rgba(243,212,138,0.85); opacity: 0; }`;
      blk(id, a0, a1, `      <div id="${id}-d"></div><div id="${id}-n">${esc(num)}</div><div id="${id}-u">${esc(unit)}</div><div id="${id}-l">${esc(lab)}</div>`, 1);
      js += `      tl.fromTo("#${id}-d", { opacity: 0 }, { opacity: 1, duration: 0.35, ease: "power2.out" }, ${r(a0)});
      tl.fromTo("#${id}-n", { opacity: 0, scale: 1.5, filter: "blur(14px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.45, ease: "power4.out" }, ${r(a0 + 0.1)});
      tl.fromTo("#${id}-u", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }, ${r(a0 + 0.45)});
      tl.fromTo("#${id}-l", { opacity: 0 }, { opacity: 1, duration: 0.35 }, ${r(a0 + 0.7)});
      tl.to("#${id}-n", { scale: 1.04, duration: ${r(Math.max(0.3, a1 - a0 - 0.9))}, ease: "none" }, ${r(a0 + 0.55)});
      tl.to(["#${id}-d", "#${id}-n", "#${id}-u", "#${id}-l"], { opacity: 0, duration: 0.25, ease: "power2.in" }, ${r(a1 - 0.28)});\n`;
    }

    // ── one big word per sentence
    if (fx.flash) {
      const Wd = fx.flash;
      css += `
    #${id} .f-w { position: absolute; left: 0; width: 1920px; top: 330px; text-align: center; opacity: 0; }
    #${id} .f-n { font: 600 70px/1 "NK Cormorant", serif; letter-spacing: 0.1em; color: ${C.gold}; margin-bottom: 6px; }
    #${id} .f-t { display: inline-block; position: relative; font: 700 190px/1.3 "NK Serif Tamil", serif; color: ${C.cream}; text-shadow: 0 0 30px rgba(0,0,0,0.9), 0 6px 40px rgba(0,0,0,0.85); white-space: nowrap; }
    #${id} .f-x { position: absolute; left: -3%; top: 54%; width: 106%; height: 12px; border-radius: 6px; background: ${C.red}; transform-origin: 0% 50%; box-shadow: 0 2px 14px rgba(0,0,0,0.6); }
    #${id}-d { position: absolute; inset: 0; background: rgba(7,10,24,0.38); }`;
      let inner = `      <div id="${id}-d"></div>`;
      Wd.forEach((word, i) => {
        const a = Math.max(t0, U(w, i) - 0.08), b = i + 1 < Wd.length ? U(w, i + 1) - 0.1 : fx.strike || Wd.length > 4 ? tE : Math.min(tE, Ue(w, i) + 0.5);
        inner += `<div id="${id}-w${i}" class="f-w">${fx.strike ? "" : Wd.length > 4 ? `<div class="f-n">${String(i + 1).padStart(2, "0")}</div>` : ""}<div class="f-t">${esc(word)}${fx.strike ? `<div id="${id}-s${i}" class="f-x"></div>` : ""}</div></div>`;
        js += `      tl.fromTo("#${id}-w${i}", { opacity: 0, scale: 1.25 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out" }, ${r(a)});
      tl.to("#${id}-w${i}", { opacity: 0, duration: 0.1, ease: "power2.in" }, ${r(b - 0.1)});\n`;
        if (fx.strike) { const ts = a + (Ue(w, i) - a) * 0.52; js += `      tl.fromTo("#${id}-s${i}", { scaleX: 0 }, { scaleX: 1, duration: 0.16, ease: "power3.out" }, ${r(ts)});\n`; snd("whoosh-short", ts, 0.16); }
        else if (Wd.length > 4) snd("whoosh-short", a + 0.05, 0.14);
      });
      const fe = fx.strike || Wd.length > 4 ? tE : Math.min(tE, Ue(w, Wd.length - 1) + 0.55);
      blk(id, t0, fe, inner, 1);
      js += `      tl.fromTo("#${id}-d", { opacity: 0 }, { opacity: 1, duration: 0.2 }, ${t0});\n      tl.to("#${id}-d", { opacity: 0, duration: 0.2 }, ${r(fe - 0.22)});\n`;
    }

    // ── two pictures side by side with a year on each
    if (fx.split) {
      const s = fx.split, a0 = Math.max(t0, U(w, s.at ?? 0) - 0.1), a1 = s.until != null ? U(w, s.until) - 0.05 : tE;
      css += `
    #${id}-in { position: absolute; inset: 0; opacity: 0; background: #000; }
    #${id} .s-h { position: absolute; top: 0; width: 960px; height: 1080px; overflow: hidden; }
    #${id} .s-h img { position: absolute; left: -160px; top: 0; width: 1280px; height: 1080px; object-fit: cover; }
    #${id}-a { left: 0; } #${id}-b { left: 960px; }
    #${id} .s-y { position: absolute; top: 96px; width: 960px; text-align: center; font: 600 190px/1 "NK Cormorant", serif; color: ${C.cream}; text-shadow: 0 4px 40px rgba(0,0,0,0.9), 0 0 16px rgba(0,0,0,0.8); }
    #${id}-yb { left: 960px; color: ${C.gold} !important; } #${id}-ya { left: 0; }
    #${id}-v { position: absolute; left: 957px; top: 0; width: 6px; height: 1080px; background: ${C.gold}; transform-origin: 50% 0%; box-shadow: 0 0 30px rgba(0,0,0,0.8); }`;
      blk(id, a0, a1, `      <div id="${id}-in"><div id="${id}-a" class="s-h"><img id="${id}-ia" src="assets/plates/${plateOf(s.a)}.jpg" alt="" /></div><div id="${id}-b" class="s-h"><img id="${id}-ib" src="assets/plates/${plateOf(s.b)}.jpg" alt="" /></div><div class="fx-sh"></div><div id="${id}-ya" class="s-y">${esc(s.L)}</div><div id="${id}-yb" class="s-y">${esc(s.R)}</div><div id="${id}-v"></div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.22, 0.25);
      js += `      tl.fromTo("#${id}-a", { x: -960 }, { x: 0, duration: 0.5, ease: "power4.out" }, ${r(a0)});
      tl.fromTo("#${id}-b", { x: 960 }, { x: 0, duration: 0.5, ease: "power4.out" }, ${r(a0)});
      tl.fromTo("#${id}-ia", { x: -30, scale: 1.04 }, { x: 30, scale: 1.1, duration: ${r(a1 - a0)}, ease: "none" }, ${r(a0)});
      tl.fromTo("#${id}-ib", { x: 30, scale: 1.1 }, { x: -30, scale: 1.04, duration: ${r(a1 - a0)}, ease: "none" }, ${r(a0)});
      tl.fromTo("#${id}-v", { scaleY: 0 }, { scaleY: 1, duration: 0.45, ease: "power3.out" }, ${r(a0 + 0.25)});
      tl.fromTo(["#${id}-ya", "#${id}-yb"], { opacity: 0, y: -30 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out", stagger: 0.12 }, ${r(a0 + 0.35)});\n`;
      snd("whoosh-cinematic", a0 + 0.1, 0.2);
    }

    // ── rupee, anna, pie
    if (fx.coins) {
      const a0 = t0, a1 = tE, u1 = U(w, 1), u2 = U(w, 2), u3 = U(w, 3);
      const coin = (k, d, bg, bd) => `#${id} .c-${k} { width: ${d}px; height: ${d}px; border-radius: 50%; background: ${bg}; border: ${bd}; box-shadow: inset 0 -${Math.round(d / 14)}px ${Math.round(d / 7)}px rgba(0,0,0,0.4), 0 ${Math.round(d / 16)}px ${Math.round(d / 6)}px rgba(0,0,0,0.5); }`;
      css += `
    ${coin("r", 300, "radial-gradient(circle at 35% 30%, #f1f1ee 0%, #b9bcc0 45%, #7d8187 100%)", "8px double rgba(60,64,70,0.55)")}
    ${coin("a", 92, "radial-gradient(circle at 35% 30%, #e9e3cf 0%, #b4ab8e 55%, #7b7460 100%)", "4px dotted rgba(70,62,44,0.6)")}
    ${coin("p", 21, "radial-gradient(circle at 35% 30%, #e7a878 0%, #a8643a 60%, #6b3b20 100%)", "0")}
    #${id}-r { position: absolute; left: 130px; top: 250px; display: flex; align-items: center; justify-content: center; font: 700 150px/1 "NK Cormorant", serif; color: rgba(40,44,50,0.82); }
    #${id}-ag { position: absolute; left: 640px; top: 196px; width: 452px; display: grid; grid-template-columns: repeat(4, 92px); gap: 28px; }
    #${id}-pg { position: absolute; left: 1300px; top: 214px; width: 500px; display: grid; grid-template-columns: repeat(16, 21px); gap: 10px; }
    #${id} .c-a { display: flex; align-items: center; justify-content: center; font: 700 44px/1 "NK Cormorant", serif; color: rgba(60,52,36,0.8); }
    #${id} .c-eq { position: absolute; top: 330px; width: 80px; text-align: center; font: 500 120px/1 "NK Cormorant", serif; color: ${C.gold}; opacity: 0; }
    #${id} .c-lb { position: absolute; top: 700px; text-align: center; font: 700 62px/1.4 "NK Serif Tamil", serif; color: ${C.cream}; opacity: 0; white-space: nowrap; }
    #${id}-hl { position: absolute; left: 626px; top: 182px; width: 120px; height: 120px; border-radius: 50%; border: 4px solid ${C.gold}; opacity: 0; }
    #${id}-x { position: absolute; left: 1300px; top: 150px; width: 500px; text-align: center; font: 600 34px/1.3 "NK Sans Tamil", sans-serif; color: ${C.gold}; opacity: 0; }`;
      const annas = Array.from({ length: 16 }, (_, i) => `<div class="c-a c-an">1</div>`).join("");
      const pies = Array.from({ length: 192 }, (_, i) => `<div class="c-p c-pi${i < 12 ? " c-p12" : ""}"></div>`).join("");
      blk(id, a0, a1, `      <div id="${id}-in" class="fx-full"><div id="${id}-r" class="c-r">1</div><div id="${id}-e1" class="c-eq" style="left: 496px">=</div><div id="${id}-ag">${annas}</div><div id="${id}-hl"></div><div id="${id}-e2" class="c-eq" style="left: 1158px">=</div><div id="${id}-x">1 அணா = 12 பை</div><div id="${id}-pg">${pies}</div>
        <div id="${id}-l1" class="c-lb" style="left: 80px; width: 400px">1 ரூபாய்</div><div id="${id}-l2" class="c-lb" style="left: 640px; width: 452px">16 அணா</div><div id="${id}-l3" class="c-lb" style="left: 1300px; width: 500px">192 பை</div><div class="fx-sh"></div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.3, 0.3);
      js += `      tl.fromTo("#${id}-r", { opacity: 0, scale: 0.4, rotation: -90 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.6, ease: "back.out(1.6)" }, ${r(a0 + 0.2)});
      tl.fromTo("#${id}-l1", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.3 }, ${r(a0 + 0.55)});
      tl.fromTo("#${id}-e1", { opacity: 0 }, { opacity: 1, duration: 0.25 }, ${r(u1 + 0.1)});
      tl.fromTo("#${id} .c-an", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.2)", stagger: 0.06 }, ${r(u1 + 0.25)});
      tl.fromTo("#${id}-l2", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.3 }, ${r(u1 + 1.1)});
      tl.fromTo("#${id}-hl", { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power3.out" }, ${r(u2)});
      tl.fromTo("#${id}-x", { opacity: 0 }, { opacity: 1, duration: 0.3 }, ${r(u2 + 0.15)});
      tl.fromTo("#${id} .c-p12", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(2)", stagger: 0.05 }, ${r(u2 + 0.3)});
      tl.fromTo("#${id}-e2", { opacity: 0 }, { opacity: 1, duration: 0.25 }, ${r(u3)});
      tl.to("#${id}-hl", { opacity: 0, duration: 0.2 }, ${r(u3)});
      tl.fromTo("#${id} .c-pi:not(.c-p12)", { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(2)", stagger: { each: 0.006, from: "start" } }, ${r(u3 + 0.1)});
      tl.fromTo("#${id}-l3", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.3 }, ${r(u3 + 1.0)});\n`;
      snd("whoosh-short", a0 + 0.1, 0.14); snd("pop", u1 + 0.3, 0.1); snd("pop", u3 + 0.15, 0.1);
    }

    // ── a hundred dots
    if (fx.dots) {
      const [lit, title, sub, mode, from] = fx.dots, a0 = t0, a1 = tE, at = U(w, mode === "lose" || from != null ? 1 : 1.35) - 0.05;
      const rnd = rng(77 + n), order = Array.from({ length: 100 }, (_, i) => i);
      if (mode === "lose") for (let i = 99; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [order[i], order[j]] = [order[j], order[i]]; }
      const pick = new Set(order.slice(0, lit)), start = new Set(order.slice(0, from ?? 0));
      css += `
    #${id}-g { position: absolute; left: 190px; top: 150px; width: 640px; display: grid; grid-template-columns: repeat(10, 46px); gap: 20px; }
    #${id} .d { width: 46px; height: 46px; border-radius: 50%; border: 3px solid rgba(246,239,220,0.34); background: rgba(246,239,220,0.05); }
    #${id} .d-on { background: ${C.gold}; border-color: ${C.gold}; }
    #${id}-t { position: absolute; left: 960px; top: ${title.length > 14 ? 326 : 300}px; width: 900px; white-space: nowrap; font: 700 ${title.length > 18 ? 60 : title.length > 14 ? 72 : 96}px/1.35 "NK Serif Tamil", serif; color: ${C.cream}; opacity: 0; }
    #${id}-s { position: absolute; left: 964px; top: 470px; width: 860px; font: 500 36px/1.5 "NK Sans Tamil", sans-serif; color: ${C.gold}; opacity: 0; }
    #${id}-k { position: absolute; left: 964px; top: 620px; font: 500 28px/1.3 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.6); }`;
      const cells = Array.from({ length: 100 }, (_, i) => `<div class="d${mode === "lose" || start.has(i) ? " d-on" : ""}${pick.has(i) ? " d-pk" : ""}${start.has(i) && !pick.has(i) ? " d-off" : ""}"></div>`).join("");
      blk(id, a0, a1, `      <div id="${id}-in" class="fx-full"><div id="${id}-g">${cells}</div><div id="${id}-t">${esc(title)}</div><div id="${id}-s">${esc(sub)}</div>${mode === "lose" ? `<div id="${id}-k">ஒரு புள்ளி = 10 குழந்தைகள்</div>` : ""}<div class="fx-sh"></div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.3, 0.3);
      if (from == null) js += `      tl.fromTo("#${id} .d", { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)", stagger: { each: 0.008, grid: [10, 10], from: "start" } }, ${r(a0 + 0.15)});\n`;
      if (mode === "lose") js += `      tl.to("#${id} .d-pk", { backgroundColor: "rgba(246,239,220,0.03)", borderColor: "rgba(246,239,220,0.3)", duration: 0.5, ease: "power2.out", stagger: 0.09 }, ${r(at)});\n`;
      else if (from != null) js += `      tl.to("#${id} .d-off", { backgroundColor: "rgba(246,239,220,0.05)", borderColor: "rgba(246,239,220,0.34)", duration: 0.35, stagger: 0.07 }, ${r(at)});\n`;
      else js += `      tl.to("#${id} .d-pk", { backgroundColor: "${C.gold}", borderColor: "${C.gold}", scale: 1.18, duration: 0.22, ease: "back.out(3)", stagger: 0.09 }, ${r(at)});\n      tl.to("#${id} .d-pk", { scale: 1, duration: 0.2 }, ${r(at + 0.09 * lit + 0.25)});\n`;
      js += `      tl.fromTo("#${id}-t", { opacity: 0, x: 30 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, ${r(at + 0.3)});
      tl.fromTo("#${id}-s", { opacity: 0 }, { opacity: 1, duration: 0.35 }, ${r(at + 0.6)});\n`;
      if (from == null) snd("whoosh-short", a0 + 0.1, 0.14);
    }

    // ── maps
    if (fx.map === "presidency") {
      const a0 = t0, a1 = tE, mb = mapBase(id), u1 = U(w, 1), u1e = Ue(w, 1), u2 = U(w, 2), z = 0.68, c0 = cam(79.6, 14.2, z, 700, 425);
      const T = (lon, lat, px, txt, cls = "m-t", extra = "") => { const [x, y] = P(lon, lat); return `<text x="${x}" y="${y}" font-size="${r(px / z)}" class="${cls}" ${extra}>${esc(txt)}</text>`; };
      const [mx, my] = P(80.27, 13.08);
      css += mb.css + `
    #${id}-big { position: absolute; left: 1160px; top: 320px; width: 700px; opacity: 0; }
    #${id}-big .b1 { font: 700 84px/1.35 "NK Serif Tamil", serif; color: ${C.cream}; } #${id}-big .b2 { font: 600 60px/1.2 "NK Cormorant", serif; letter-spacing: 0.08em; color: ${C.gold}; }
    #${id}-big .b3 { margin-top: 14px; font: 500 30px/1.5 "NK Sans Tamil", sans-serif; color: rgba(217,226,220,0.8); }`;
      blk(id, a0, a1, `      <div id="${id}-in"><div id="${id}-cam"><svg width="1920" height="1080" viewBox="0 0 1920 1080"><defs><clipPath id="${id}-cp"><path d="${dPath(GEO.c.IN)}"/></clipPath></defs>
        <g><path class="m-grid" stroke-width="${r(1 / z)}" d="${mb.grid}"/><path class="m-land" stroke-width="${r(1.6 / z)}" d="${mb.land}"/>
        <path class="m-state" stroke-width="${r(1.4 / z)}" d="${dPath([...GEO.s["Andhra Pradesh"], ...GEO.s.Kerala, ...GEO.s.Karnataka, ...GEO.s.Telangana, ...GEO.s.Odisha])}"/>
        <path id="${id}-pr" d="${dPath([PRES])}" clip-path="url(#${id}-cp)" fill="rgba(216,73,63,0.4)" stroke="none" opacity="0"/>
        <path id="${id}-tn" d="${dPath(GEO.s["Tamil Nadu"])}" fill="rgba(243,212,138,0.2)" stroke="${C.gold}" stroke-width="${r(3 / z)}" stroke-linejoin="round" opacity="0"/>
        ${T(77.75, 10.9, 34, "தமிழ்நாடு", "m-t", `id="${id}-l0" opacity="0" font-weight="700"`)}${T(79.0, 15.0, 30, "ஆந்திரா", "m-t", `id="${id}-l1" opacity="0"`)}${T(72.55, 11.55, 30, "மலபார்", "m-t", `id="${id}-l2" opacity="0"`)}${T(71.7, 14.9, 28, "கர்நாடகா பகுதிகள்", "m-t", `id="${id}-l3" opacity="0"`)}
        ${T(83.3, 9.2, 26, "வங்கக் கடல்", "m-sea")}${T(80.9, 7.25, 24, "இலங்கை", "m-sea")}
        <circle cx="${mx}" cy="${my}" r="${r(8 / z)}" fill="${C.red}"/><circle id="${id}-ring" cx="${mx}" cy="${my}" r="${r(18 / z)}" fill="none" stroke="${C.red}" stroke-width="${r(2.5 / z)}"/>${T(80.6, 13.0, 30, "மெட்ராஸ்", "m-t", `font-weight="700"`)}</g></svg></div>
        <div class="m-vig"></div><div id="${id}-big"><div class="b1">மெட்ராஸ் மாகாணம்</div><div class="b2">1926</div><div class="b3">இன்னிக்கு இருக்கற நாலு மாநிலங்களோட பகுதிகள்</div></div><div class="m-note">சிவப்பு பகுதி: மாகாணத்தோட தோராயமான எல்லை</div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.35, 0.3);
      js += `      tl.fromTo("#${id}-cam", ${camJs(cam(79.3, 11.5, 1.0, 700, 440))}, { ...${camJs(c0)}, duration: ${r(a1 - a0)}, ease: "power1.out" }, ${r(a0)});
      tl.fromTo("#${id}-ring", { scale: 0.4, opacity: 1, svgOrigin: "${mx} ${my}" }, { scale: 2.4, opacity: 0, duration: 1.2, repeat: ${Math.max(1, Math.floor((a1 - a0) / 1.2) - 1)}, ease: "power1.out" }, ${r(a0 + 0.3)});
      tl.fromTo(["#${id}-tn", "#${id}-l0"], { opacity: 0 }, { opacity: 1, duration: 0.5 }, ${r(a0 + 0.9)});
      tl.fromTo("#${id}-pr", { opacity: 0 }, { opacity: 1, duration: 1.2, ease: "power2.out" }, ${r(u1 - 0.1)});
      tl.fromTo("#${id}-l1", { opacity: 0 }, { opacity: 1, duration: 0.3 }, ${r(u1 + 0.15)});
      tl.fromTo("#${id}-l2", { opacity: 0 }, { opacity: 1, duration: 0.3 }, ${r(u1 + (u1e - u1) * 0.3)});
      tl.fromTo("#${id}-l3", { opacity: 0 }, { opacity: 1, duration: 0.3 }, ${r(u1 + (u1e - u1) * 0.52)});
      tl.fromTo("#${id}-big", { opacity: 0, x: 30 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, ${r(u1 + (u1e - u1) * 0.76)});
      tl.to("#${id}-tn", { opacity: 0.35, duration: 0.5 }, ${r(u2 + 0.3)});\n`;
      snd("whoosh-short", a0 + 0.1, 0.14);
    }
    if (fx.map === "boat1") {
      // one map over four lines: boat1 the two cities, boat2 the route, boat3 the time, boat4 Dhanushkodi
      const W4 = [w, win[wi + 1], win[wi + 2], win[wi + 3]], a0 = t0, a1 = r(W4[3].end - 0.12), mb = mapBase(id);
      const zW = 1.07, zS = 3.4, zD = 6.5, cW = cam(79.9, 10.0, zW, 620, 440), cS = cam(79.45, 9.2, zS, 560, 470), cD = cam(79.38, 9.2, zD, 700, 470);
      const pts = (a) => a.map(([x, y]) => P(x, y)), d = (a) => "M" + pts(a).map((p) => p.join(",")).join("L");
      const L1 = lineLen(pts(RAIL_IN)), L3 = lineLen(pts(RAIL_LK));
      const T = (lon, lat, px, zz, txt, idx, cls = "m-t", extra = "") => { const [x, y] = P(lon, lat); return `<text ${idx ? `id="${id}-${idx}" opacity="0"` : ""} x="${x}" y="${y}" font-size="${r(px / zz)}" class="${cls}" ${extra}>${esc(txt)}</text>`; };
      const pin = (lon, lat, zz, idx, rr = 7) => { const [x, y] = P(lon, lat); return `<circle id="${id}-${idx}" cx="${x}" cy="${y}" r="${r(rr / zz)}" fill="${C.red}" stroke="#f4e9e2" stroke-width="${r(2 / zz)}" opacity="0"/>`; };
      const [dx, dy] = P(79.42, 9.18), [m0x, m0y] = P(80.26, 13.08), [c0x, c0y] = P(79.85, 6.93);
      const cards = W4.flatMap((x, k) => shotsOf(x.q).map((s, j, arr) => ({ plate: s.plate, k, j, m: arr.length, x })));
      css += mb.css;
      blk(id, a0, a1, `      <div id="${id}-in"><div id="${id}-cam"><svg width="1920" height="1080" viewBox="0 0 1920 1080"><g><path class="m-grid" stroke-width="${r(1 / zW)}" d="${mb.grid}"/><path id="${id}-land" class="m-land" stroke-width="${r(1.5 / zW)}" d="${mb.land}"/>
        <path id="${id}-air" d="M${m0x},${m0y}Q${r(m0x + 150)},${r((m0y + c0y) / 2)} ${c0x},${c0y}" fill="none" stroke="${C.gold}" stroke-width="${r(3 / zW)}" stroke-dasharray="${r(10 / zW)} ${r(8 / zW)}" opacity="0"/>
        <path id="${id}-r1" d="${d(RAIL_IN)}" fill="none" stroke="${C.red}" stroke-width="${r(5 / zW)}" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="${r(L1)}" stroke-dashoffset="${r(L1)}"/>
        <path id="${id}-r2" d="${d(FERRY)}" fill="none" stroke="#f4e9e2" stroke-width="${r(3.5 / zS)}" stroke-dasharray="${r(7 / zS)} ${r(6 / zS)}" opacity="0"/>
        <path id="${id}-r3" d="${d(RAIL_LK)}" fill="none" stroke="${C.red}" stroke-width="${r(5 / zW)}" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="${r(L3)}" stroke-dashoffset="${r(L3)}"/>
        ${pin(80.26, 13.08, zW, "p0")}${pin(79.85, 6.93, zW, "p1")}${pin(79.42, 9.18, zS, "p2", 6)}${pin(79.73, 9.1, zS, "p3", 6)}
        <circle id="${id}-ring" cx="${dx}" cy="${dy}" r="${r(26 / zD)}" fill="none" stroke="${C.red}" stroke-width="${r(3 / zD)}" opacity="0"/>
        ${T(80.5, 13.02, 34, zW, "மெட்ராஸ்", "t0", "m-t", `font-weight="700"`)}${T(80.1, 6.88, 34, zW, "கொழும்பு", "t1", "m-t", `font-weight="700"`)}
        ${T(79.2, 9.07, 30, zS, "தனுஷ்கோடி", "t2", "m-t", `font-weight="700" text-anchor="end"`)}${T(79.78, 9.03, 28, zS, "தலைமன்னார்", "t3")}
        ${T(75.9, 11.6, 26, zW, "மெட்ராஸ் மாகாணம்", "", "m-sea zz")}${T(80.35, 7.9, 26, zW, "சிலோன்", "", "m-sea zz")}${T(81.6, 11.2, 26, zW, "வங்கக் கடல்", "", "m-sea zz")}</g></svg></div>
        <div class="m-vig"></div>
        <div id="${id}-c1" class="m-chip" style="left: 64px; top: 150px"><b>ரயில்</b> · போட் மெயில் · சுமார் 20 மணி நேரம்</div>
        <div id="${id}-c2" class="m-chip" style="left: 64px; top: 150px"><b>கப்பல்</b> · தனுஷ்கோடி → தலைமன்னார்</div>
        <div id="${id}-c3" class="m-chip" style="left: 64px; top: 150px"><b>ரயில்</b> · தலைமன்னார் → கொழும்பு</div>
        <div id="${id}-c4" class="m-chip" style="left: 64px; top: 150px"><b>1926</b> · ஒன்றரை நாளுக்கும் மேல</div>
        <div id="${id}-c5" class="m-chip" style="left: 64px; top: 232px"><b>இன்னிக்கு</b> · விமானத்துல ஒன்றரை மணி நேரம்</div>
        <div id="${id}-c6" class="m-chip" style="left: 64px; top: 150px"><b>1964</b> · 38 வருஷம் கழிச்சு ஒரு புயல்</div>
        <div class="m-note" style="right: 110px; top: 590px">ரயில் பாதை: தோராயமான வரைவு</div>
        ${cards.map((c, i) => `<div id="${id}-k${i}" class="m-card" style="transform: rotate(${i % 2 ? -2 : 2}deg)"><img src="assets/plates/${c.plate}.jpg" alt="" /></div>`).join("")}</div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.35, 0.35);
      const [B1, B2, B3, B4] = W4, b2 = [0, 1, 2, 3].map((i) => U(B2, i)), tB3 = r(B3.t0 - 0.1), tB4 = r(B4.t0 - 0.1);
      const show = (sel, t, dur = 0.3) => (js += `      tl.fromTo("${sel}", { opacity: 0 }, { opacity: 1, duration: ${dur} }, ${r(t)});\n`);
      const hide = (sel, t) => (js += `      tl.to("${sel}", { opacity: 0, duration: 0.25 }, ${r(t)});\n`);
      js += `      tl.fromTo("#${id}-cam", ${camJs(cam(79.9, 10.0, 0.94, 620, 440))}, { ...${camJs(cW)}, duration: ${r(b2[0] - a0)}, ease: "power2.out" }, ${r(a0)});\n`;
      show(`#${id}-p0`, a0 + 0.5); show(`#${id}-t0`, a0 + 0.6); show(`#${id}-p1`, U(B1, 1) + 0.9); show(`#${id}-t1`, U(B1, 1) + 1.0);
      // route: rail to Dhanushkodi, ferry, rail to Colombo
      js += `      tl.to("#${id}-r1", { attr: { "stroke-dashoffset": 0 }, duration: ${r(Ue(B2, 1) - b2[0] - 0.3)}, ease: "power1.inOut" }, ${r(b2[0] + 0.1)});
      tl.to("#${id}-cam", { ...${camJs(cS)}, duration: ${r(Math.max(1.2, b2[2] - b2[1] - 0.2))}, ease: "power2.inOut" }, ${r(b2[1] + 0.2)});\n`;
      const sw = (zz, t, dur) => (js += `      tl.to(["#${id}-r1", "#${id}-r3"], { attr: { "stroke-width": ${r(5 / zz)} }, duration: ${dur}, ease: "power2.inOut" }, ${r(t)});\n      tl.to("#${id}-land", { attr: { "stroke-width": ${r(1.6 / zz)} }, duration: ${dur}, ease: "power2.inOut" }, ${r(t)});\n`);
      sw(zS, b2[1] + 0.2, r(Math.max(1.2, b2[2] - b2[1] - 0.2)));
      js += `      tl.to("#${id} .zz", { opacity: 0, duration: 0.5 }, ${r(b2[1] + 0.2)});\n      tl.to("#${id} .zz", { opacity: 1, duration: 0.5 }, ${r(b2[3] + 0.7)});\n      tl.to("#${id} .zz", { opacity: 0, duration: 0.5 }, ${r(tB4)});\n`;
      show(`#${id}-c1`, b2[0] + 0.3); hide(`#${id}-c1`, b2[2] - 0.3);
      show(`#${id}-p2`, Ue(B2, 1) - 0.5); show(`#${id}-t2`, Ue(B2, 1) - 0.4);
      show(`#${id}-r2`, b2[2] + 0.2, 0.6); show(`#${id}-c2`, b2[2] + 0.05); hide(`#${id}-c2`, b2[3] - 0.3);
      show(`#${id}-p3`, b2[2] + 0.9); show(`#${id}-t3`, b2[2] + 1.0);
      js += `      tl.to("#${id}-cam", { ...${camJs(cW)}, duration: 1.3, ease: "power2.inOut" }, ${r(b2[3] - 0.1)});\n`; sw(zW, b2[3] - 0.1, 1.3); js += `
      tl.to("#${id}-r3", { attr: { "stroke-dashoffset": 0 }, duration: ${r(Math.max(1, Ue(B2, 3) - b2[3] - 0.5))}, ease: "power1.inOut" }, ${r(b2[3] + 0.5)});\n`;
      show(`#${id}-c3`, b2[3] + 0.05); hide(`#${id}-c3`, tB3 - 0.2);
      hide(`#${id}-t2`, b2[3]); hide(`#${id}-t3`, b2[3]);
      // time: then and now
      show(`#${id}-c4`, tB3 + 0.1); show(`#${id}-c5`, U(B3, 1)); show(`#${id}-air`, U(B3, 1) - 0.1, 0.5);
      hide(`#${id}-c4`, tB4 - 0.15); hide(`#${id}-c5`, tB4 - 0.15); hide(`#${id}-air`, tB4);
      // Dhanushkodi
      js += `      tl.to("#${id}-cam", { ...${camJs(cD)}, duration: 1.8, ease: "power2.inOut" }, ${r(tB4)});\n`; sw(zD, tB4, 1.8); js += `
      tl.to("#${id}-t2", { opacity: 1, duration: 0.3 }, ${r(tB4 + 1.2)});
      tl.fromTo("#${id}-ring", { opacity: 1, scale: 0.5, svgOrigin: "${dx} ${dy}" }, { opacity: 0, scale: 2.6, duration: 1.3, repeat: ${Math.max(1, Math.floor((a1 - tB4 - 1.5) / 1.3))}, ease: "power1.out" }, ${r(tB4 + 1.3)});\n`;
      show(`#${id}-c6`, U(B4, 1));
      cards.forEach((c, i) => {
        const x = c.x, k0 = c.m > 1 ? [0, 2, 3][c.j] ?? c.j : 0;
        const s0 = c.m > 1 ? U(x, k0) + (c.j ? 0.1 : 0.5) : r(x.t0 + 0.45);
        const nx = cards[i + 1], e0 = nx ? (nx.x === x ? U(x, [0, 2, 3][nx.j] ?? nx.j) - 0.1 : r(x.end - 0.3)) : a1 - 0.4;
        js += `      tl.fromTo("#${id}-k${i}", { opacity: 0, y: 40, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "power3.out" }, ${r(s0)});
      tl.to("#${id}-k${i}", { opacity: 0, y: -20, duration: 0.3, ease: "power2.in" }, ${r(e0)});\n`;
      });
      snd("whoosh-short", a0 + 0.1, 0.14);
    }

    // ── mock-ups (set in the edit, never generated)
    if (fx.mock === "ticket") {
      const a0 = t0, a1 = tE;
      css += `
    #${id}-c { position: absolute; left: 1250px; top: 170px; width: 520px; height: 250px; background: #e6d7b0; border-radius: 6px; box-shadow: 0 16px 44px rgba(0,0,0,0.6); padding: 20px 28px; opacity: 0; color: ${C.inkp}; background-image: repeating-linear-gradient(0deg, rgba(60,40,10,0.05) 0 2px, transparent 2px 5px); }
    #${id}-c .k1 { font: 700 27px/1.3 "NK Serif Tamil", serif; white-space: nowrap; border-bottom: 2px solid rgba(42,33,24,0.6); padding-bottom: 6px; }
    #${id}-c .k2 { margin-top: 12px; font: 700 62px/1.2 "NK Serif Tamil", serif; } #${id}-c .k3 { margin-top: 6px; font: 500 22px/1.3 "NK Special Elite", monospace; letter-spacing: 0.1em; color: rgba(140,40,30,0.9); }
    #${id}-c .k4 { position: absolute; right: 22px; bottom: 16px; font: 500 20px/1.3 "NK Sans Tamil", sans-serif; opacity: 0.6; }`;
      blk(id, a0, a1, `      <div id="${id}-c"><div class="k1">மெட்ராஸ் டிராம் · பயணச் சீட்டு</div><div class="k2">1 அணா</div><div class="k3">No. 04127</div><div class="k4">மாதிரி வடிவம்</div></div>`, 2);
      js += `      tl.fromTo("#${id}-c", { opacity: 0, y: -60, rotation: -14 }, { opacity: 1, y: 0, rotation: -5, duration: 0.4, ease: "back.out(1.5)" }, ${r(a0)});
      tl.to("#${id}-c", { opacity: 0, duration: 0.2 }, ${r(a1 - 0.22)});\n`;
      snd("pop", a0 + 0.1, 0.1);
    }
    if (fx.mock === "paper") {
      const a0 = t0, a1 = tE, u1 = U(w, 1), u2 = U(w, 2);
      const bars = (k, wd) => Array.from({ length: k }, (_, i) => `<div class="ln" style="width: ${wd - ((i * 37) % 60)}px"></div>`).join("");
      css += `
    #${id} .ppr { position: absolute; background: ${C.paper}; color: ${C.inkp}; box-shadow: 0 24px 70px rgba(0,0,0,0.65); background-image: radial-gradient(ellipse at 30% 20%, rgba(255,255,255,0.25) 0%, rgba(120,90,40,0.12) 100%); opacity: 0; }
    #${id}-p { left: 190px; top: 150px; width: 860px; height: 640px; padding: 26px 40px; overflow: hidden; }
    #${id}-p .mh { text-align: center; font: 700 82px/1.3 "NK Serif Tamil", serif; white-space: nowrap; border-bottom: 5px double ${C.inkp}; } #${id}-p .dt { display: flex; justify-content: space-between; font: 500 24px/2 "NK Sans Tamil", sans-serif; border-bottom: 2px solid ${C.inkp}; }
    #${id}-p .hd { margin-top: 12px; font: 700 44px/1.35 "NK Serif Tamil", serif; } #${id}-p .cols { display: flex; gap: 26px; margin-top: 16px; }
    #${id} .ln { height: 9px; margin-bottom: 11px; background: rgba(42,33,24,0.42); border-radius: 2px; }
    #${id}-m { left: 1190px; top: 130px; width: 520px; height: 650px; padding: 30px; border: 10px double #7b2a1c; text-align: center; }
    #${id}-m .mt { font: 700 78px/1.3 "NK Serif Tamil", serif; color: #7b2a1c; } #${id}-m .ms { margin-top: 8px; font: 600 34px/1.5 "NK Sans Tamil", sans-serif; }
    #${id}-m .mo { margin: 24px auto 0; width: 220px; height: 220px; border-radius: 50%; border: 6px solid #7b2a1c; display: flex; align-items: center; justify-content: center; font: 600 110px/1 "NK Cormorant", serif; color: #7b2a1c; }
    #${id}-n { position: absolute; right: 64px; top: 60px; font: 500 24px/1.3 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.6); }`;
      blk(id, a0, a1, `      <div id="${id}-in" class="fx-full"><div id="${id}-p" class="ppr"><div class="mh">சுதேசமித்திரன்</div><div class="dt"><span>மெட்ராஸ்</span><span>1926</span><span>தினசரி</span></div><div class="hd">இன்றைய செய்திகள்</div><div class="cols"><div>${bars(16, 240)}</div><div>${bars(16, 240)}</div><div>${bars(16, 240)}</div></div></div>
        <div id="${id}-m" class="ppr"><div class="mt">ஆனந்த விகடன்</div><div class="ms">மாத இதழ் · பிப்ரவரி 1926</div><div class="mo">1</div></div><div class="fx-sh"></div><div id="${id}-n">மாதிரி வடிவம் · அசல் பக்கம் இல்ல</div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.3, 0.3);
      js += `      tl.fromTo("#${id}-p", { opacity: 0, y: 160, rotation: 4 }, { opacity: 1, y: 0, rotation: -3, duration: 0.6, ease: "power3.out" }, ${r(a0 + 0.15)});
      tl.to("#${id}-p", { scale: 1.04, duration: ${r(a1 - a0 - 0.8)}, ease: "none" }, ${r(a0 + 0.75)});
      tl.fromTo("#${id}-m", { opacity: 0, x: 200, rotation: 12 }, { opacity: 1, x: 0, rotation: 4, duration: 0.55, ease: "back.out(1.3)" }, ${r(u1 + 0.4)});
      tl.fromTo("#${id}-m .mt", { scale: 0.85 }, { scale: 1, duration: 0.4, ease: "back.out(2)" }, ${r(u2)});\n`;
      snd("whoosh-short", a0 + 0.1, 0.14); snd("pop", u1 + 0.5, 0.1);
    }
    if (fx.mock === "postcard") {
      const a0 = t0, a1 = tE, u1 = U(w, 1), u2 = U(w, 2);
      const hand = ["அன்புள்ள அண்ணாவுக்கு,", "இங்கு யாவரும் நலம்.", "அங்கு உங்கள் நலம் அறிய ஆவல்.", "உடனே பதில் எழுதவும்."];
      css += `
    #${id}-p { position: absolute; left: 170px; top: 160px; width: 940px; height: 590px; background: #e4d6b4; box-shadow: 0 24px 70px rgba(0,0,0,0.65); opacity: 0; background-image: radial-gradient(ellipse at 30% 20%, rgba(255,255,255,0.22) 0%, rgba(120,90,40,0.14) 100%); }
    #${id}-p .st { position: absolute; right: 36px; top: 34px; width: 120px; height: 146px; border: 3px solid rgba(110,40,30,0.7); display: flex; align-items: center; justify-content: center; } #${id}-p .st i { width: 66px; height: 88px; border-radius: 50%; border: 3px solid rgba(110,40,30,0.6); display: block; }
    #${id}-p .pm { position: absolute; right: 120px; top: 60px; width: 130px; height: 130px; border-radius: 50%; border: 4px solid rgba(30,30,30,0.5); display: flex; align-items: center; justify-content: center; font: 500 22px/1.2 "NK Special Elite", monospace; color: rgba(30,30,30,0.6); transform: rotate(-16deg); text-align: center; }
    #${id}-p .hw { position: absolute; left: 56px; width: 800px; font: 400 50px/1.3 "NK Kavivanar", "NK Sans Tamil", cursive; color: #1d2a55; white-space: nowrap; }
    #${id}-d { position: absolute; left: 1220px; top: 250px; width: 600px; opacity: 0; } #${id}-d .dh { font: 600 34px/1.4 "NK Sans Tamil", sans-serif; color: ${C.gold}; margin-bottom: 18px; }
    #${id}-d .dr { display: grid; grid-template-columns: repeat(7, 70px); gap: 12px; } #${id}-d .dd { height: 86px; border-radius: 10px; border: 2px solid rgba(246,239,220,0.4); display: flex; align-items: center; justify-content: center; font: 600 44px/1 "NK Oswald", sans-serif; color: ${C.cream}; }
    #${id}-d .dn { margin-top: 22px; font: 700 64px/1.3 "NK Serif Tamil", serif; color: ${C.cream}; opacity: 0; }
    #${id}-n { position: absolute; right: 64px; top: 60px; font: 500 24px/1.3 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.6); }`;
      blk(id, a0, a1, `      <div id="${id}-in" class="fx-full"><div id="${id}-p"><div class="st"><i></i></div><div class="pm">MADRAS<br/>1926</div>${hand.map((h, i) => `<div id="${id}-h${i}" class="hw" style="top: ${218 + i * 84}px">${esc(h)}</div>`).join("")}</div>
        <div id="${id}-d"><div class="dh">பதில் வர…</div><div class="dr">${[1, 2, 3, 4, 5, 6, 7].map((k) => `<div class="dd">${k}</div>`).join("")}</div><div id="${id}-dn" class="dn">ஒரு வாரம்</div></div><div class="fx-sh"></div><div id="${id}-n">மாதிரி வடிவம்</div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.3, 0.3);
      js += `      tl.fromTo("#${id}-p", { opacity: 0, y: 120, rotation: -9 }, { opacity: 1, y: 0, rotation: -3, duration: 0.55, ease: "power3.out" }, ${r(a0 + 0.15)});\n`;
      hand.forEach((h, i) => (js += `      tl.fromTo("#${id}-h${i}", { clipPath: "inset(0% 100% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.55, ease: "power1.inOut" }, ${r(u1 + 0.15 + i * 0.5)});\n`));
      js += `      tl.fromTo("#${id}-d", { opacity: 0 }, { opacity: 1, duration: 0.3 }, ${r(u2 - 0.05)});
      tl.fromTo("#${id}-d .dd", { opacity: 0.25, backgroundColor: "rgba(243,212,138,0)" }, { opacity: 1, backgroundColor: "rgba(243,212,138,0.28)", duration: 0.16, stagger: 0.2 }, ${r(u2 + 0.1)});
      tl.fromTo("#${id}-dn", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.3 }, ${r(u2 + 1.5)});\n`;
      snd("whoosh-short", a0 + 0.1, 0.14);
    }
    if (fx.mock === "telegram") {
      const a0 = t0, a1 = tE, u1 = U(w, 1), u2 = U(w, 2), words = ["FATHER", "SERIOUS", "START", "IMMEDIATELY"];
      css += `
    #${id}-p { position: absolute; left: 330px; top: 150px; width: 1260px; height: 610px; background: #e9d9c6; box-shadow: 0 24px 70px rgba(0,0,0,0.65); opacity: 0; padding: 30px 50px; color: ${C.inkp}; background-image: radial-gradient(ellipse at 30% 20%, rgba(255,255,255,0.22) 0%, rgba(150,80,60,0.12) 100%); }
    #${id}-p .th { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 4px solid ${C.inkp}; padding-bottom: 8px; } #${id}-p .th b { font: 700 64px/1.3 "NK Serif Tamil", serif; } #${id}-p .th span { font: 500 30px/1.2 "NK Special Elite", monospace; letter-spacing: 0.14em; }
    #${id}-p .tr { margin-top: 18px; display: flex; gap: 30px; align-items: baseline; font: 500 24px/1.3 "NK Special Elite", monospace; color: rgba(42,33,24,0.7); }
    #${id}-p .ts { margin-top: 34px; display: flex; gap: 20px; flex-wrap: wrap; } #${id}-p .tw { background: #f6efe2; padding: 10px 20px 4px; font: 500 62px/1.2 "NK Special Elite", monospace; letter-spacing: 0.04em; box-shadow: 0 2px 6px rgba(0,0,0,0.25); opacity: 0; }
    #${id}-p .tg { margin-top: 40px; font: 600 44px/1.5 "NK Sans Tamil", sans-serif; color: #7b2a1c; opacity: 0; }
    #${id}-p .tc { margin-left: auto; display: flex; align-items: baseline; gap: 14px; font: 600 34px/1.3 "NK Sans Tamil", sans-serif; color: ${C.inkp}; } #${id}-p .cw { position: relative; width: 40px; height: 56px; }
    #${id}-p .cn { position: absolute; right: 0; bottom: 0; font: 600 56px/1 "NK Oswald", sans-serif; color: #7b2a1c; opacity: 0; }
    #${id}-n { position: absolute; right: 64px; top: 60px; font: 500 24px/1.3 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.6); }`;
      blk(id, a0, a1, `      <div id="${id}-in" class="fx-full"><div id="${id}-p"><div class="th"><b>தந்தி</b><span>INDIAN POSTS AND TELEGRAPHS</span></div><div class="tr"><span>MADRAS</span><span>1926</span><span>URGENT</span><div class="tc"><div class="cw">${words.map((x, i) => `<b id="${id}-c${i}" class="cn">${i + 1}</b>`).join("")}</div><span>வார்த்தை</span></div></div>
        <div class="ts">${words.map((x, i) => `<div id="${id}-w${i}" class="tw">${x}</div>`).join("")}</div><div id="${id}-g" class="tg">“அப்பாவுக்கு உடம்பு சரியில்ல. உடனே கிளம்பு.”</div></div><div class="fx-sh"></div><div id="${id}-n">மாதிரி வடிவம்</div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.3, 0.3);
      js += `      tl.fromTo("#${id}-p", { opacity: 0, y: 100, rotation: 5 }, { opacity: 1, y: 0, rotation: -1.5, duration: 0.5, ease: "power3.out" }, ${r(a0 + 0.15)});\n`;
      const step = Math.min(0.55, Math.max(0.3, (u2 - u1 - 0.2) / 4));
      words.forEach((x, i) => {
        const t = u1 + 0.05 + i * step;
        js += `      tl.fromTo("#${id}-w${i}", { opacity: 0, y: -14 }, { opacity: 1, y: 0, duration: 0.12, ease: "power2.out" }, ${r(t)});\n      tl.fromTo("#${id}-c${i}", { opacity: 0 }, { opacity: 1, duration: 0.05 }, ${r(t)});\n`;
        if (i < 3) js += `      tl.to("#${id}-c${i}", { opacity: 0, duration: 0.05 }, ${r(t + step)});\n`;
        snd("key-press", t, 0.16);
      });
      js += `      tl.fromTo("#${id}-g", { opacity: 0 }, { opacity: 1, duration: 0.4 }, ${r(u2 + 0.1)});\n`;
      snd("whoosh-short", a0 + 0.1, 0.14);
    }
    if (fx.mock === "intertitle") {
      const a0 = Math.max(t0, U(w, fx.at ?? 3) - 0.1), a1 = tE, rnd = rng(31);
      css += `
    #${id}-in { position: absolute; inset: 0; background: #0b0b0b; opacity: 0; }
    #${id}-f { position: absolute; left: 230px; top: 140px; width: 1460px; height: 640px; border: 5px solid #d8d2c2; outline: 2px solid #d8d2c2; outline-offset: 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; }
    #${id}-f .i1 { font: 700 84px/1.5 "NK Serif Tamil", serif; color: #e9e4d6; text-align: center; } #${id}-f .i2 { margin-top: 30px; width: 180px; height: 3px; background: #a9a391; }
    #${id}-s { position: absolute; top: 0; width: 3px; height: 1080px; background: rgba(255,255,255,0.22); }
    #${id}-n { position: absolute; right: 64px; top: 60px; font: 500 24px/1.3 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.5); }`;
      blk(id, a0, a1, `      <div id="${id}-in"><div id="${id}-f"><div class="i1">“அரசே! எதிரிப் படை<br/>கோட்டையை நெருங்கிவிட்டது!”</div><div class="i2"></div></div><div id="${id}-s"></div><div id="${id}-n">மாதிரி வடிவம்</div></div>`, 2);
      js += `      tl.fromTo("#${id}-in", { opacity: 0 }, { opacity: 1, duration: 0.08 }, ${r(a0)});\n      tl.to("#${id}-in", { opacity: 0, duration: 0.12 }, ${r(a1 - 0.14)});\n`;
      for (let t = a0 + 0.1; t < a1 - 0.2; t += 0.09) js += `      tl.set("#${id}-f", { opacity: ${r(0.82 + rnd() * 0.18)}, x: ${r((rnd() - 0.5) * 5)}, y: ${r((rnd() - 0.5) * 4)} }, ${r(t)});\n      tl.set("#${id}-s", { x: ${Math.round(100 + rnd() * 1700)}, opacity: ${rnd() > 0.5 ? 1 : 0} }, ${r(t)});\n`;
    }
  }
  if (!html) html = `    <div id="x0" class="fxb clip" data-start="0" data-duration="0.1" data-track-index="1"></div>\n`;
  return { css, html, js, audio };
}

/** Chapter card background: one picture of the chapter, dark and slowly moving, under the unchanged card type. */
export function cardBg(plate, CARD) {
  return {
    css: `
    #k-pic { position: absolute; inset: 0; overflow: hidden; }
    #k-pic img { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; object-fit: cover; filter: saturate(0.7) brightness(0.62); }
    #k-shade { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 46%, rgba(18,26,60,0.62) 0%, rgba(7,10,24,0.9) 78%); }`,
    html: `      <div id="k-pic"><img id="k-img" src="assets/plates/${plate}.jpg" alt="" /></div>\n      <div id="k-shade"></div>\n`,
    js: `      tl.fromTo("#k-img", { scale: 1.06 }, { scale: 1.14, duration: ${r(CARD + 0.5)}, ease: "none" }, 0);\n`,
  };
}
