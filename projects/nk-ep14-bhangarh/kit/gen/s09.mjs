// 09 — Split-screen triptych: three tall panels hold the last three shots. Each new shot rises
// into the oldest panel and takes the light; the other two fall back to a dim duotone. A marker
// rides above the live panel; captions sit centred underneath.
import { r, index, scene, writeStyle, buildShots, shotsFor, sentsFor, WIN, FONTS, sfx, HIT, tAt } from "./lib.mjs";
import { capSentences } from "./caps.mjs";

export default function build() {
  const w = "b", D = WIN[w].dur;
  const shots = shotsFor(w), sents = sentsFor(w);
  const PW = 592, PH = 760, GAP = 18, X0 = (1920 - 3 * PW - 2 * GAP) / 2, Y0 = 84;
  const pos = { sh005: "36% 50%", sh001: "34% 50%", sh002: "50% 50%", sh008: "56% 50%", sh007: "42% 50%", sh004: "50% 50%" };
  let css = "", html = "", js = "";
  for (let c = 0; c < 3; c++) {
    const mine = shots.map((s, i) => ({ ...s, i })).filter((s) => s.i % 3 === c).map((s) => ({ ...s, a: [1 + (s.a[0] - 1) * 0.35, s.a[1], 0], b: [1 + (s.b[0] - 1) * 0.35 + 0.06, s.b[1], 0], o: "50% 55%" }));
    mine.at(-1).t1 = D;
    const P = buildShots(mine, { pfx: `q${c}`, W: PW, H: PH, kbScale: 0.5, kbEase: "sine.inOut", trans: () => ({ type: "slideUp", d: 0.5 }), track: 1 + c * 2 });
    css += P.css + "\n" + mine.map((s, k) => `    #q${c}${k + 1}-kb img { object-position: ${pos[s.plate]}; }`).join("\n") + "\n";
    html += `    <div id="q-col${c}" class="q-col" style="left:${X0 + c * (PW + GAP)}px">\n${P.html}      <div id="q-dim${c}" class="q-dim" data-layout-ignore></div>\n    </div>\n`;
    js += P.js;
    // the first shot of a panel also rises in
    if (c > 0) js += `      tl.fromTo("#q${c}1-tr", { yPercent: 100 }, { yPercent: 0, duration: 0.5, ease: "expo.out" }, ${mine[0].t0});\n`;
  }
  js += `      tl.set(["#q-dim0", "#q-dim1", "#q-dim2"], { opacity: 0 }, 0);\n`;
  shots.forEach((s, i) => {
    const c = i % 3;
    if (i > 0) {
      js += `      tl.to("#q-dim${c}", { opacity: 0, duration: 0.25, ease: "power2.out" }, ${s.t0});\n`;
      js += `      tl.to("#q-dim${(i - 1) % 3}", { opacity: 1, duration: 0.4, ease: "power2.out" }, ${s.t0});\n`;
      js += `      tl.to("#q-mark", { x: ${c * (PW + GAP)}, duration: 0.4, ease: "expo.out" }, ${s.t0});\n`;
    }
  });
  const hit = tAt(w, HIT);
  const hc = shots.findIndex((s) => s.k === "b5") % 3;
  js += `      tl.fromTo("#q-col${hc}", { y: 0 }, { y: -16, duration: 0.06, ease: "power2.out" }, ${hit});\n      tl.to("#q-col${hc}", { y: 0, duration: 0.5, ease: "elastic.out(1.2, 0.3)" }, ${r(hit + 0.06)});\n`;
  js += `      tl.fromTo("#q-bar-f", { scaleX: 0 }, { scaleX: 1, duration: ${D}, ease: "none" }, 0);\n`;
  const C = capSentences(sents, { merge: [] });
  const tri = scene({
    id: "tri",
    css: `    ${FONTS.hind}
    ${FONTS.oswald}
    .q-col { position: absolute; top: ${Y0}px; width: ${PW}px; height: ${PH}px; overflow: hidden; background: #17130f; border-radius: 6px; }
${css}    .q-dim { position: absolute; inset: 0; z-index: 90; background: rgba(16,13,10,0.66); backdrop-filter: saturate(0.25); }
    #q-mark { position: absolute; left: ${X0}px; top: ${Y0 - 22}px; width: ${PW}px; height: 6px; background: #e0a458; border-radius: 3px; }
    #q-tag { position: absolute; left: ${X0}px; top: 16px; height: 40px; font: 500 30px/40px "NK Oswald", sans-serif; letter-spacing: 0.12em; color: rgba(240,232,214,0.62); }
    #q-bar { position: absolute; left: ${X0}px; top: ${Y0 + PH + 16}px; width: ${1920 - 2 * X0}px; height: 3px; background: rgba(240,232,214,0.16); }
    #q-bar-f { position: absolute; inset: 0; background: rgba(224,164,88,0.8); transform-origin: 0% 50%; }
    .c-cap { position: absolute; left: 160px; width: 1600px; top: ${Y0 + PH + 40}px; height: 150px; display: flex; align-items: center; justify-content: center; text-align: center; }
    .c-in { font: 500 50px/1.4 "NK Hind Madurai", sans-serif; color: #f4ecd9; max-width: 1500px; }`,
    html: `${html}    <div id="q-mark" data-layout-ignore></div>
    <div id="q-tag">NAGAPATTINAM · 1856</div>
    <div id="q-bar" data-layout-ignore><div id="q-bar-f"></div></div>
${C.html}`,
    js: js + C.js,
  });
  const sMetal = sents.find((s) => s.text.startsWith("உலோகம்"));
  writeStyle("09-split-triptych", "NK 09 Split-screen triptych", {
    "index.html": index({
      title: "NK style 09 — Split-screen triptych", dur: D, bg: "#0d0b09",
      hosts: [{ id: "tri", kind: "captions" }],
      audio: [
        { id: "vo", src: WIN[w].audio, start: 0, dur: WIN[w].adur, vol: 1 },
        ...shots.slice(1).map((s, i) => sfx("whoosh-short", s.t0 + 0.1, 0.16)),
        sfx("impact-bass-1", hit, 0.4),
        sfx("impact-bass-2", sMetal.t0, 0.4),
      ],
    }),
    "compositions/tri.html": tri,
  });
}
