// Added picture language (EP17, 20 Nov 2026; EP18 set below). Nothing here changes the existing look: captions, tags, chapter card
// type and sound, subscribe pop-up and camera moves stay in gen.mjs as they were. This file adds one more layer ("gfx", between
// the pictures and the tags) that is filled only where a script line asks for it with its 4th field:
//   stat  [big, label, source, at?]      number card on the left (at = sentence of the line where it appears)
//   line  [[year, label, at], …]         small timeline on the left
//   big   [number, unit, label, at?]     one giant number over the dimmed picture
//   flash [words…] (+ strike)            one big word per sentence of the line
//   step  [k, of, label, jam?]           EP18: door counter, top right; jam = sentence at which the last door turns red
//   vaults {show, open, shut, at}        EP18: six doors A to F, full screen (two lines in a row share one graphic)
//   map "tvm"                            EP18: Thiruvananthapuram on the map, full screen
//   mock "report"                        EP18: a page of the 2014 audit report as a labelled mock-up, full screen
//   also kept from EP17: clock, vs, split, dots
// Full-screen graphics (map, vaults, report, dots) carry their own background and the line has no pictures of its own.
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { r, esc, sfx, rng, FONTS } from "../kit/gen/lib.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const GEO = JSON.parse(readFileSync(join(HERE, "geo.json"), "utf8"));
const C = { gold: "#f3d48a", cream: "#f6efdc", navy: "rgba(10,14,34,0.88)", ink: "#070a18", red: "#d8493f", paper: "#e9dfc4", inkp: "#2a2118" };
export const FULL = (fx) => !!fx && !!(fx.dots || fx.map || fx.vaults || fx.mock === "report");

// ── map geometry: plain equirectangular projection around 11°N, 100 px per degree before the camera zoom
const LON0 = 71.5, LAT1 = 23, KX = 100 * Math.cos((11 * Math.PI) / 180), KY = 100;
const P = (lon, lat) => [r((lon - LON0) * KX), r((LAT1 - lat) * KY)];
const dPath = (rings, close = true) => rings.map((g) => "M" + g.map(([a, b]) => P(a, b).join(",")).join("L") + (close ? "Z" : "")).join("");
const lineLen = (pts) => pts.reduce((s, p, i) => (i ? s + Math.hypot(p[0] - pts[i - 1][0], p[1] - pts[i - 1][1]) : 0), 0);
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
      blk(cid2, a0, a1, `      <div id="${cid2}-c"><div id="${cid2}-f"><div id="${cid2}-h"></div><div id="${cid2}-m"></div><div id="${cid2}-d"></div></div><div id="${cid2}-t">${h}:${String(m).padStart(2, "0")}</div><div id="${cid2}-l">${esc(lab)}</div></div>`, 3);
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

    // ── a hundred dots
    if (fx.dots) {
      const [lit, title, sub, mode, from] = fx.dots, a0 = t0, a1 = tE, grow = from != null && from < lit, at = U(w, grow ? Math.min(2, w.a.un.length - 1) : mode === "lose" || from != null ? 1 : 1.35) - 0.05; // EP19: grow = from < lit, the added dots light up
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
      const cells = Array.from({ length: 100 }, (_, i) => `<div class="d${mode === "lose" || start.has(i) ? " d-on" : ""}${pick.has(i) ? " d-pk" : ""}${start.has(i) && !pick.has(i) ? " d-off" : ""}${grow && pick.has(i) && !start.has(i) ? " d-add" : ""}"></div>`).join("");
      blk(id, a0, a1, `      <div id="${id}-in" class="fx-full"><div id="${id}-g">${cells}</div><div id="${id}-t">${esc(title)}</div><div id="${id}-s">${esc(sub)}</div>${mode === "lose" ? `<div id="${id}-k">ஒரு புள்ளி = 10 குழந்தைகள்</div>` : ""}<div class="fx-sh"></div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.3, 0.3);
      if (from == null) js += `      tl.fromTo("#${id} .d", { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.25, ease: "back.out(2)", stagger: { each: 0.008, grid: [10, 10], from: "start" } }, ${r(a0 + 0.15)});\n`;
      if (mode === "lose") js += `      tl.to("#${id} .d-pk", { backgroundColor: "rgba(246,239,220,0.03)", borderColor: "rgba(246,239,220,0.3)", duration: 0.5, ease: "power2.out", stagger: 0.09 }, ${r(at)});\n`;
      else if (grow) js += `      tl.to("#${id} .d-add", { backgroundColor: "${C.gold}", borderColor: "${C.gold}", scale: 1.18, duration: 0.22, ease: "back.out(3)", stagger: 0.07 }, ${r(at)});\n      tl.to("#${id} .d-add", { scale: 1, duration: 0.2, stagger: 0.07 }, ${r(at + 0.3)});\n`;
      else if (from != null) js += `      tl.to("#${id} .d-off", { backgroundColor: "rgba(246,239,220,0.05)", borderColor: "rgba(246,239,220,0.34)", duration: 0.35, stagger: 0.07 }, ${r(at)});\n`;
      else js += `      tl.to("#${id} .d-pk", { backgroundColor: "${C.gold}", borderColor: "${C.gold}", scale: 1.18, duration: 0.22, ease: "back.out(3)", stagger: 0.09 }, ${r(at)});\n      tl.to("#${id} .d-pk", { scale: 1, duration: 0.2 }, ${r(at + 0.09 * lit + 0.25)});\n`;
      js += `      tl.fromTo("#${id}-t", { opacity: 0, x: 30 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, ${r(at + 0.3)});
      tl.fromTo("#${id}-s", { opacity: 0 }, { opacity: 1, duration: 0.35 }, ${r(at + 0.6)});\n`;
      if (from == null) snd("whoosh-short", a0 + 0.1, 0.14);
    }

    // ── EP18: door counter, top right ("door 2 of 3"); the last pip turns red when `jam` names a sentence
    if (fx.step) {
      const [k, of, lab, jam] = fx.step, a0 = t0 + 0.15, a1 = tE, sid = `${id}p`, first = !(win[wi - 1] && win[wi - 1].l.fx && win[wi - 1].l.fx.step);
      css += `
    #${sid}-c { position: absolute; right: 64px; top: 52px; width: 430px; height: 148px; border-radius: 26px; background: ${C.navy}; border: 1.5px solid rgba(243,212,138,0.55); box-shadow: 0 10px 40px rgba(0,0,0,0.5); opacity: 0; }
    #${sid}-k { position: absolute; left: 26px; top: 12px; font: 600 28px/1.4 "NK Sans Tamil", sans-serif; color: ${C.gold}; }
    #${sid}-n { position: absolute; left: 24px; top: 46px; font: 600 74px/1.15 "NK Oswald", sans-serif; color: ${C.cream}; white-space: nowrap; }
    #${sid}-n span { font-size: 44px; color: rgba(246,239,220,0.6); }
    #${sid}-c .pp { position: absolute; top: 28px; width: 44px; height: 62px; border-radius: 22px 22px 3px 3px; border: 3px solid rgba(243,212,138,0.6); }
    #${sid}-c .pp.on { background: ${C.gold}; border-color: ${C.gold}; }
    #${sid}-l { position: absolute; left: 180px; top: 100px; width: 236px; font: 600 26px/1.4 "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; }`;
      const pips = Array.from({ length: of }, (_, i) => `<div id="${sid}-p${i}" class="pp${i < k - 1 ? " on" : ""}" style="left: ${186 + i * 62}px"></div>`).join("");
      blk(sid, a0, a1, `      <div id="${sid}-c"><div id="${sid}-k">கதவு</div><div id="${sid}-n">${k}<span> / ${of}</span></div>${pips}<div id="${sid}-l">${esc(lab)}</div></div>`, 3);
      js += `      tl.fromTo("#${sid}-c", { opacity: 0, x: ${first ? 60 : 0} }, { opacity: 1, x: 0, duration: ${first ? 0.45 : 0.2}, ease: "power3.out" }, ${r(a0)});
      tl.fromTo("#${sid}-p${k - 1}", { backgroundColor: "rgba(243,212,138,0)", scale: 1 }, { backgroundColor: "${C.gold}", scale: 1.12, duration: 0.3, ease: "back.out(2)" }, ${r(a0 + 0.35)});\n`;
      if (jam != null) { const tj = U(w, jam);
        js += `      tl.to("#${sid}-p${k - 1}", { backgroundColor: "${C.red}", borderColor: "${C.red}", duration: 0.2 }, ${r(tj)});
      tl.fromTo("#${sid}-p${k - 1}", { x: -5 }, { x: 5, duration: 0.06, repeat: 7, yoyo: true, ease: "none" }, ${r(tj)});
      tl.to("#${sid}-p${k - 1}", { x: 0, duration: 0.05 }, ${r(tj + 0.5)});
      tl.to("#${sid}-n", { color: "${C.red}", duration: 0.2 }, ${r(tj)});\n`;
        snd("impact-bass-2", tj, 0.2); }
      js += `      tl.to("#${sid}-c", { opacity: 0, duration: 0.2, ease: "power2.in" }, ${r(a1 - 0.22)});\n`;
      snd("pop", a0 + 0.35, 0.1);
    }

    // ── EP18: six doors, A to F. A diagram of what the court record says, not a plan of the cellar.
    // Consecutive `vaults` lines share one block: the first line names the six, the next shows which are used and which stayed shut.
    if (fx.vaults) {
      if (win[wi - 1] && win[wi - 1].l.fx && win[wi - 1].l.fx.vaults) continue;
      const w2 = win[wi + 1] && win[wi + 1].l.fx && win[wi + 1].l.fx.vaults ? win[wi + 1] : null, v2 = w2 ? w2.l.fx.vaults : fx.vaults;
      const a0 = t0, a1 = r((w2 || w).end - 0.12), LET = ["A", "B", "C", "D", "E", "F"], X = (i) => 150 + i * 276;
      const ph = w.a.ph.slice(-6).map((p) => r(lead + p[0] - 0.08));
      const open = v2.open || [], shut = v2.shut || [];
      css += `
    #${id} .v-h { position: absolute; left: 0; width: 1920px; top: 112px; text-align: center; font: 700 54px/1.4 "NK Serif Tamil", serif; color: ${C.cream}; opacity: 0; }
    #${id} .v-h b { color: ${C.gold}; font: 600 66px/1 "NK Oswald", sans-serif; padding: 0 10px; }
    #${id} .v-note { position: absolute; right: 64px; top: 60px; font: 500 24px/1.3 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.6); }
    #${id} .v-floor { position: absolute; left: 110px; top: 650px; width: 1700px; height: 4px; background: linear-gradient(90deg, rgba(243,212,138,0) 0%, rgba(243,212,138,0.5) 12%, rgba(243,212,138,0.5) 88%, rgba(243,212,138,0) 100%); }
    #${id} .v-d { position: absolute; top: 256px; width: 240px; height: 394px; opacity: 0; }
    #${id} .v-a { position: absolute; inset: 0; border-radius: 120px 120px 4px 4px; border: 5px solid rgba(246,239,220,0.75); background: linear-gradient(180deg, #1a2246 0%, #0c1128 100%); box-shadow: inset 0 0 50px rgba(0,0,0,0.7); overflow: hidden; }
    #${id} .v-g { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 70%, rgba(243,212,138,0.75) 0%, rgba(243,212,138,0.12) 70%); opacity: 0; }
    #${id} .v-bar { position: absolute; left: -14px; top: 282px; width: 268px; height: 22px; border-radius: 4px; background: ${C.red}; box-shadow: 0 4px 16px rgba(0,0,0,0.6); transform-origin: 0% 50%; }
    #${id} .v-x { position: absolute; left: 0; width: 240px; top: 84px; text-align: center; font: 600 150px/1.1 "NK Cormorant", serif; color: ${C.cream}; }
    #${id} .v-st { position: absolute; top: 680px; text-align: center; font: 600 36px/1.4 "NK Sans Tamil", sans-serif; opacity: 0; white-space: nowrap; }
    #${id} .v-st i { display: block; height: 14px; border: 3px solid currentColor; border-top: 0; border-radius: 0 0 10px 10px; margin-bottom: 12px; }
    #${id} .v-st small { display: block; font: 500 27px/1.4 "NK Sans Tamil", sans-serif; opacity: 0.85; }`;
      const doors = LET.map((L, i) => `<div id="${id}-d${i}" class="v-d" style="left: ${X(i)}px"><div id="${id}-a${i}" class="v-a"><div id="${id}-g${i}" class="v-g"></div></div><div id="${id}-x${i}" class="v-x">${L}</div>${shut.includes(L) ? `<div id="${id}-b${i}" class="v-bar"></div>` : ""}</div>`).join("");
      const span = (arr) => { const ii = arr.map((L) => LET.indexOf(L)); return [X(Math.min(...ii)), X(Math.max(...ii)) + 240 - X(Math.min(...ii))]; };
      let st = "";
      if (open.length) { const [x, wd] = span(open); st += `<div id="${id}-so" class="v-st" style="left: ${x}px; width: ${wd}px; color: ${C.gold}"><i></i>அவ்வப்போது திறக்கற அறைகள்</div>`; }
      if (shut.length) { const [x, wd] = span(shut); st += `<div id="${id}-ss" class="v-st" style="left: ${x}px; width: ${wd}px; color: #ff8a80"><i></i>100+ வருஷம் திறக்கல<small>(அப்படி சொல்லப்பட்டது)</small></div>`; }
      blk(id, a0, a1, `      <div id="${id}-in" class="fx-full"><div id="${id}-h" class="v-h">கோயிலுக்கு அடியில <b>6</b> நிலவறைகள்</div><div class="v-floor"></div>${doors}${st}<div class="fx-sh"></div><div class="v-note">விளக்கப் படம் · அறைகளோட உண்மையான அமைப்பு இல்ல</div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.3, 0.3);
      js += `      tl.fromTo("#${id}-h", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, ${r(a0 + 0.25)});\n`;
      LET.forEach((L, i) => { const t = fx.vaults.show === "all" && ph.length === 6 ? ph[i] : a0 + 0.5 + i * 0.12;
        js += `      tl.fromTo("#${id}-d${i}", { opacity: 0, y: 40, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.32, ease: "back.out(1.6)" }, ${r(t)});\n`;
        snd("pop", t + 0.05, 0.08);
        if (shut.includes(L)) js += `      tl.fromTo("#${id}-b${i}", { scaleX: 0 }, { scaleX: 0.001, duration: 0.01 }, ${r(a0)});\n`; });
      if (w2) {
        const tO = U(w2, 0) + 0.25, tS = U(w2, v2.at ?? 1);
        open.forEach((L, k) => { const i = LET.indexOf(L);
          js += `      tl.to("#${id}-g${i}", { opacity: 1, duration: 0.45, ease: "power2.out" }, ${r(tO + k * 0.12)});
      tl.to("#${id}-a${i}", { borderColor: "${C.gold}", duration: 0.3 }, ${r(tO + k * 0.12)});
      tl.to("#${id}-x${i}", { color: "${C.ink}", duration: 0.3 }, ${r(tO + k * 0.12)});\n`; });
        if (open.length) js += `      tl.fromTo("#${id}-so", { opacity: 0, y: -10 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }, ${r(tO + 0.5)});\n`;
        shut.forEach((L, k) => { const i = LET.indexOf(L);
          js += `      tl.to("#${id}-b${i}", { scaleX: 1, duration: 0.28, ease: "power3.out" }, ${r(tS + k * 0.5)});
      tl.to("#${id}-a${i}", { borderColor: "${C.red}", duration: 0.25 }, ${r(tS + k * 0.5)});\n`;
          snd("impact-bass-2", tS + k * 0.5, 0.16); });
        if (shut.length) js += `      tl.fromTo("#${id}-ss", { opacity: 0, y: -10 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }, ${r(tS + 1.3)});
      tl.to([${open.map((L) => `"#${id}-d${LET.indexOf(L)}"`).join(", ")}, "#${id}-so"], { opacity: 0.35, duration: 0.5 }, ${r(tS + 1.3)});
      tl.to("#${id}-d${LET.indexOf("B")}", { scale: 1.08, transformOrigin: "50% 100%", duration: ${r(Math.max(0.4, a1 - tS - 2.2))}, ease: "power1.inOut" }, ${r(tS + 1.6)});\n`;
      }
      snd("whoosh-short", a0 + 0.1, 0.14);
    }

    // ── maps
    if (fx.map === "tvm") {
      const a0 = t0, a1 = tE, mb = mapBase(id), u1 = U(w, 1), u2 = U(w, 2), z = 2.3, c1 = cam(76.94, 8.49, z, 600, 640);
      const T = (lon, lat, px, txt, cls = "m-t", extra = "") => { const [x, y] = P(lon, lat); return `<text x="${x}" y="${y}" font-size="${r(px / z)}" class="${cls}" ${extra}>${esc(txt)}</text>`; };
      const [mx, my] = P(76.94, 8.49);
      css += mb.css + `
    #${id} .m-rt { position: absolute; right: 0; top: 0; width: 1100px; height: 1080px; background: linear-gradient(90deg, rgba(10,16,22,0) 0%, rgba(10,16,22,0.82) 46%, rgba(10,16,22,0.94) 100%); }
    #${id}-big { position: absolute; left: 1010px; top: 250px; width: 850px; }
    #${id}-big .b1 { font: 700 96px/1.35 "NK Serif Tamil", serif; color: ${C.cream}; white-space: nowrap; opacity: 0; }
    #${id}-big .b2 { margin-top: 6px; font: 600 44px/1.4 "NK Sans Tamil", sans-serif; color: ${C.gold}; opacity: 0; }
    #${id}-big .b3 { margin-top: 44px; font: 700 66px/1.4 "NK Serif Tamil", serif; color: ${C.cream}; white-space: nowrap; opacity: 0; }
    #${id}-big .b3 em { font-style: normal; color: ${C.gold}; } #${id}-big .b3 span { color: rgba(246,239,220,0.45); padding: 0 12px; }
    #${id}-big .b4 { margin-top: 8px; font: 500 36px/1.5 "NK Sans Tamil", sans-serif; color: rgba(217,226,220,0.85); opacity: 0; }`;
      blk(id, a0, a1, `      <div id="${id}-in"><div id="${id}-cam"><svg width="1920" height="1080" viewBox="0 0 1920 1080">
        <g><path class="m-grid" stroke-width="${r(1 / z)}" d="${mb.grid}"/><path class="m-land" stroke-width="${r(1.6 / z)}" d="${mb.land}"/>
        <path class="m-state" stroke-width="${r(1.4 / z)}" d="${dPath([...GEO.s["Tamil Nadu"], ...GEO.s.Karnataka])}"/>
        <path id="${id}-kl" d="${dPath(GEO.s.Kerala)}" fill="rgba(243,212,138,0.22)" stroke="${C.gold}" stroke-width="${r(3 / z)}" stroke-linejoin="round" opacity="0"/>
        ${T(76.35, 10.3, 34, "கேரளா", "m-t", `id="${id}-l0" opacity="0" font-weight="700"`)}${T(77.75, 10.75, 28, "தமிழ்நாடு", "m-t", `opacity="0.7"`)}
        ${T(74.75, 8.0, 26, "அரபிக் கடல்", "m-sea")}
        <circle cx="${mx}" cy="${my}" r="${r(9 / z)}" fill="${C.red}"/><circle id="${id}-ring" cx="${mx}" cy="${my}" r="${r(20 / z)}" fill="none" stroke="${C.red}" stroke-width="${r(3 / z)}"/></g></svg></div>
        <div class="m-vig"></div><div class="m-rt"></div><div id="${id}-big"><div id="${id}-b1" class="b1">திருவனந்தபுரம்</div><div id="${id}-b2" class="b2">கேரளாவோட தலைநகரம்</div><div id="${id}-b3" class="b3">திரு<span>·</span><em>அனந்த</em><span>·</span>புரம்</div><div id="${id}-b4" class="b4">அனந்தன் மேல பள்ளி கொண்டவரோட ஊர்</div></div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.35, 0.3);
      js += `      tl.fromTo("#${id}-cam", ${camJs(cam(78.6, 12.2, 0.95, 620, 470))}, { ...${camJs(c1)}, duration: ${r(Math.min(2.6, a1 - a0 - 0.4))}, ease: "power2.inOut" }, ${r(a0)});
      tl.fromTo("#${id}-ring", { scale: 0.4, opacity: 1, svgOrigin: "${mx} ${my}" }, { scale: 2.6, opacity: 0, duration: 1.1, repeat: ${Math.max(1, Math.floor((a1 - a0) / 1.1) - 1)}, ease: "power1.out" }, ${r(a0 + 0.3)});
      tl.fromTo("#${id}-b1", { opacity: 0, x: 30 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, ${r(a0 + 0.3)});
      tl.fromTo(["#${id}-kl", "#${id}-l0"], { opacity: 0 }, { opacity: 1, duration: 0.5 }, ${r(u1 - 0.05)});
      tl.fromTo("#${id}-b2", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.4, ease: "power3.out" }, ${r(u1)});
      tl.fromTo("#${id}-b3", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, ${r(u2 - 0.05)});
      tl.fromTo("#${id}-b4", { opacity: 0 }, { opacity: 1, duration: 0.4 }, ${r(u2 + 0.5)});\n`;
      snd("whoosh-short", a0 + 0.1, 0.14);
    }

    // ── mock-ups (set in the edit, never generated)
    if (fx.mock === "report") {
      const a0 = t0, a1 = tE, u1 = U(w, 1), u2 = U(w, 2);
      const bars = (k, wd) => Array.from({ length: k }, (_, i) => `<div class="ln" style="width: ${wd - ((i * 53) % 130)}px"></div>`).join("");
      css += `
    #${id}-p { position: absolute; left: 230px; top: 136px; width: 940px; height: 760px; padding: 32px 56px; background: ${C.paper}; color: ${C.inkp}; box-shadow: 0 24px 70px rgba(0,0,0,0.65); background-image: radial-gradient(ellipse at 30% 20%, rgba(255,255,255,0.25) 0%, rgba(120,90,40,0.12) 100%); opacity: 0; overflow: hidden; }
    #${id}-p .rh { white-space: nowrap; font: 700 50px/1.35 "NK Serif Tamil", serif; border-bottom: 4px solid ${C.inkp}; padding-bottom: 8px; }
    #${id}-p .rs { display: flex; justify-content: space-between; font: 500 26px/2 "NK Sans Tamil", sans-serif; border-bottom: 1.5px solid ${C.inkp}; }
    #${id}-p .rt { margin-top: 14px; font: 700 34px/1.4 "NK Sans Tamil", sans-serif; }
    #${id}-p .rr { display: flex; gap: 30px; margin-top: 6px; font: 600 32px/1.5 "NK Sans Tamil", sans-serif; } #${id}-p .rr b { font: 600 38px/1.3 "NK Oswald", sans-serif; }
    #${id} .ln { height: 9px; margin: 13px 0; background: rgba(42,33,24,0.38); border-radius: 2px; }
    #${id}-p .hl { position: relative; margin: 12px -14px 0; padding: 8px 14px; white-space: nowrap; font: 700 28px/1.5 "NK Serif Tamil", serif; }
    #${id}-p .hl i { position: absolute; left: 0; top: 0; width: 100%; height: 100%; background: rgba(243,190,60,0.55); transform-origin: 0% 50%; }
    #${id}-p .hl span { position: relative; }
    #${id}-q { position: absolute; left: 1250px; top: 560px; width: 600px; opacity: 0; }
    #${id}-7 { position: absolute; left: 1250px; top: 150px; width: 600px; opacity: 0; }
    #${id}-7 .n7 { font: 600 300px/1 "NK Cormorant", serif; font-variant-numeric: lining-nums; font-feature-settings: "lnum" 1; color: ${C.gold}; } #${id}-7 .n7 span { font: 700 72px/1 "NK Serif Tamil", serif; color: ${C.cream}; padding-left: 20px; }
    #${id}-7 .s7 { font: 600 34px/1.4 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.8); }
    #${id}-q .q1 { font: 600 30px/1.4 "NK Sans Tamil", sans-serif; color: ${C.gold}; } #${id}-q .q2 { margin-top: 6px; font: 700 50px/1.4 "NK Serif Tamil", serif; color: ${C.cream}; }
    #${id}-q .q3 { margin-top: 18px; font: 500 30px/1.5 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.75); }
    #${id}-n { position: absolute; right: 64px; top: 60px; font: 500 24px/1.3 "NK Sans Tamil", sans-serif; color: rgba(246,239,220,0.6); }`;
      blk(id, a0, a1, `      <div id="${id}-in" class="fx-full"><div id="${id}-p"><div class="rh">சிறப்பு தணிக்கை அறிக்கை</div><div class="rs"><span>சுப்ரீம் கோர்ட்டுக்கு</span><span>2014</span></div>
        <div class="rt">B நிலவறை · பதிவேட்டுக் குறிப்புகள்</div><div class="rr"><span><b>1990</b> · 2 தடவை</span><span><b>2002</b> · 5 தடவை</span></div>${bars(2, 800)}
        <div class="hl"><i id="${id}-h1"></i><span>வெள்ளிக் கட்டிகள்: வெளிய எடுக்கப்பட்டது</span></div>${bars(2, 760)}
        <div class="hl"><i id="${id}-h2"></i><span>தங்கப் பாத்திரங்கள்: உள்ள வச்சு, மறுபடி எடுத்தது</span></div>${bars(8, 800)}</div>
        <div id="${id}-7"><div class="n7">7<span>தடவை</span></div><div class="s7">1990ல 2 · 2002ல 5</div></div>
        <div id="${id}-q"><div class="q1">தணிக்கை அறிக்கை சொல்றது</div><div class="q2">பதிவேட்டுல இருக்கற குறிப்பு</div><div class="q3">அறிக்கை பத்தி 2014ல வந்த செய்திகள்படி</div></div>
        <div class="fx-sh"></div><div id="${id}-n">மாதிரி வடிவம் · அசல் பக்கம் இல்ல</div></div>`, 2);
      inOut(`#${id}-in`, a0, a1, 0.3, 0.3);
      js += `      tl.fromTo("#${id}-p", { opacity: 0, y: 160, rotation: 3 }, { opacity: 1, y: 0, rotation: -2, duration: 0.6, ease: "power3.out" }, ${r(a0 + 0.1)});
      tl.to("#${id}-p", { scale: 1.04, duration: ${r(a1 - a0 - 0.8)}, ease: "none" }, ${r(a0 + 0.7)});
      tl.fromTo("#${id}-7", { opacity: 0 }, { opacity: 1, duration: 0.35 }, ${r(a0 + 0.25)});
      tl.fromTo("#${id}-h1", { scaleX: 0 }, { scaleX: 1, duration: 0.7, ease: "power2.out" }, ${r(Math.max(a0 + 0.5, U(w, 0) + 0.2))});
      tl.fromTo("#${id}-h2", { scaleX: 0 }, { scaleX: 1, duration: 0.9, ease: "power2.out" }, ${r(u1 + 0.1)});
      tl.fromTo("#${id}-q", { opacity: 0, x: 30 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, ${r(u2 - 0.05)});\n`;
      snd("whoosh-short", a0 + 0.1, 0.14); snd("pop", u2, 0.1);
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
