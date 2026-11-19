// 03 — OLA manuscript (NK "Direction A"): palm-leaf ground, manuscript double rule with vermilion
// corner ticks, running head, plate tipped in as a framed leaf, captions on a cream plate with the
// spoken word in vermilion. Separators are drawn diamonds; Tamil is never letter-spaced.
import { r, index, scene, writeStyle, buildShots, shotsFor, sentsFor, WIN, FONTS } from "./lib.mjs";
import { capWords } from "./caps.mjs";

const INK = "#1A1409", VER = "#A63A28", CREAM = "#FAF5E9", OLIVE = "#625C3A";
const tick = (id, x, y, rot) => `<div id="${id}" class="o-tick" style="left:${x}px;top:${y}px;transform:rotate(${rot}deg)" data-layout-ignore></div>`;
const kolam = `<svg id="o-kolam" viewBox="-34 -34 68 68" width="58" height="58" data-layout-ignore><g fill="none" stroke="${VER}" stroke-width="2.6"><ellipse cx="0" cy="-15" rx="8" ry="13"/><ellipse cx="0" cy="15" rx="8" ry="13"/><ellipse cx="-15" cy="0" rx="13" ry="8"/><ellipse cx="15" cy="0" rx="13" ry="8"/><path d="M0,-9 L9,0 L0,9 L-9,0 Z"/></g><g fill="${INK}"><circle cx="0" cy="-15" r="2.4"/><circle cx="0" cy="15" r="2.4"/><circle cx="-15" cy="0" r="2.4"/><circle cx="15" cy="0" r="2.4"/><circle cx="0" cy="0" r="2.4"/></g></svg>`;

export default function build() {
  const w = "a", D = WIN[w].dur;
  const shots = shotsFor(w), sents = sentsFor(w);
  const PW = 1400, PH = 700, PX = 260, PY = 132;
  const P = buildShots(shots, { W: PW, H: PH, kbScale: 0.8, trans: (i) => (i % 2 ? { type: "wipe", d: 0.8 } : { type: "fade", d: 0.8 }) });
  const page = scene({
    id: "page",
    css: `    ${FONTS.serifTa}
    ${FONTS.corm}
    #o-paper { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }
    #o-rule-a { position: absolute; left: 40px; top: 40px; width: 1840px; height: 1000px; border: 2.5px solid ${INK}; }
    #o-rule-b { position: absolute; left: 52px; top: 52px; width: 1816px; height: 976px; border: 1px solid rgba(26,20,9,0.7); }
    .o-tick { position: absolute; width: 34px; height: 34px; border-left: 5px solid ${VER}; border-top: 5px solid ${VER}; }
    #o-head { position: absolute; left: 0; width: 1920px; top: 62px; height: 56px; display: flex; align-items: center; justify-content: center; gap: 22px; font: 700 34px/1.4 "NK Serif Tamil", serif; color: ${INK}; }
    .o-dia { width: 12px; height: 12px; background: ${VER}; transform: rotate(45deg); flex: none; }
    .o-hr { width: 190px; height: 1.5px; background: rgba(26,20,9,0.55); flex: none; }
    #o-foot { position: absolute; left: 0; width: 1920px; top: 986px; height: 40px; display: flex; align-items: center; justify-content: center; gap: 18px; font: 400 28px/1.4 "NK Serif Tamil", serif; color: ${OLIVE}; }
    #o-foot b { font: 600 31px/1 "NK Cormorant", serif; letter-spacing: 0.08em; color: ${INK}; }
    #o-kolam { position: absolute; left: 96px; top: 62px; }
    #o-leafno { position: absolute; right: 100px; top: 70px; font: 600 30px/1.3 "NK Cormorant", serif; letter-spacing: 0.1em; color: ${INK}; }
    #o-frame { position: absolute; left: ${PX}px; top: ${PY}px; width: ${PW}px; height: ${PH}px; overflow: hidden; background: #2a2418; box-shadow: 0 0 0 2px ${INK}, 0 0 0 10px ${CREAM}, 0 0 0 11.5px rgba(26,20,9,0.75), 0 18px 40px rgba(60,40,10,0.28); }
    #o-inner { position: absolute; inset: 0; box-shadow: inset 0 0 90px rgba(20,12,0,0.45); z-index: 40; pointer-events: none; }
${P.css}
    #o-tab { position: absolute; left: ${PX + 26}px; top: ${PY + 26}px; z-index: 60; }
    #o-tab-in { display: flex; align-items: center; gap: 14px; padding: 8px 20px 9px; background: ${CREAM}; border: 1.5px solid ${INK}; font: 700 30px/1.4 "NK Serif Tamil", serif; color: ${INK}; }
    #o-tab-in b { font: 700 32px/1 "NK Cormorant", serif; letter-spacing: 0.06em; }`,
    html: `    <img id="o-paper" src="assets/tex/ola_paper.jpg" alt="" data-layout-ignore />
    <div id="o-rule-a" data-layout-ignore></div>
    <div id="o-rule-b" data-layout-ignore></div>
    ${tick("o-t1", 40, 40, 0)}${tick("o-t2", 1846, 40, 90)}${tick("o-t3", 1846, 1006, 180)}${tick("o-t4", 40, 1006, 270)}
    ${kolam}
    <div id="o-head"><span class="o-hr"></span><span class="o-dia"></span><span id="o-head-t">நிலவன் கதைகள்</span><span class="o-dia"></span><span class="o-hr"></span></div>
    <div id="o-leafno">EP 06</div>
    <div id="o-frame">
${P.html}      <div id="o-inner" data-layout-ignore></div>
    </div>
    <div id="o-tab" class="clip" data-start="0.05" data-duration="${r(D - 0.05)}" data-track-index="3"><div id="o-tab-in"><span id="o-tab-a">நாகப்பட்டினம்</span><span class="o-dia" id="o-tab-d"></span><b id="o-tab-b">1856</b></div></div>
    <div id="o-foot"><span>ஏடு</span><b>06</b><span class="o-dia"></span><span>ராஜேந்திர சோழனும் ஸ்ரீவிஜயமும்</span></div>`,
    js: `${P.js}      tl.fromTo("#o-tab-in", { opacity: 0, x: -24 }, { opacity: 1, x: 0, duration: 0.5, ease: "expo.out" }, 0.08);
      tl.fromTo(["#o-tab-d", "#o-tab-b"], { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power2.out" }, 1.45);`,
  });

  const C = capWords(sents, {
    max: 5,
    lead: 0.1,
    tail: 0.35,
    exit: 0.1,
    inAnim: (id, start) => `      tl.fromTo("#${id}-in", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.2, ease: "power3.out" }, ${start});\n`,
    onWord: (id, wid, wd) => `      tl.set("#${wid}", { color: "${VER}" }, ${wd.t0}); tl.set("#${wid}", { color: "${INK}" }, ${wd.t1});\n`,
  });
  const cap = scene({
    id: "cap",
    css: `    ${FONTS.serifTa}
    .c-cap { position: absolute; left: 160px; width: 1600px; top: 868px; height: 100px; text-align: center; }
    .c-in { display: inline-block; white-space: nowrap; padding: 12px 40px 14px; background: ${CREAM}; border: 1.5px solid ${INK}; box-shadow: 0 6px 18px rgba(60,40,10,0.18); font: 700 46px/1.45 "NK Serif Tamil", serif; color: #746c54; }
    .c-w { color: #746c54; }`,
    html: C.html,
    js: C.js,
  });

  writeStyle("03-ola-manuscript", "NK 03 OLA manuscript", {
    "index.html": index({
      title: "NK style 03 — OLA manuscript",
      dur: D,
      bg: "#E8DBBB",
      hosts: [{ id: "page" }, { id: "cap", kind: "captions" }],
      audio: [{ id: "vo", src: WIN[w].audio, start: 0, dur: WIN[w].adur, vol: 1 }],
    }),
    "compositions/page.html": page,
    "compositions/cap.html": cap,
  });
}
