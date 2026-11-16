// 07 — Kinetic typography: the narration is the picture. One phrase per screen, one word per
// line, each word slammed in on the frame it is spoken, the newest word in amber; the plates run
// behind as a dark, blurred, slowly drifting wash that hard-cuts with the phrase.
import { r, index, scene, writeStyle, buildShots, shotsFor, sentsFor, WIN, FONTS, groupsOf, esc, sfx } from "./lib.mjs";

const cps = (t) => [...t].filter((c) => !/[\u0BCD\u0BBF\u0BC0\u0BC1\u0BC2.,?!]/.test(c)).length + [...t].filter((c) => /[\u0BBF\u0BC0\u0BC1\u0BC2]/.test(c)).length * 0.35;

export default function build() {
  const w = "a", D = WIN[w].dur;
  const shots = shotsFor(w), sents = sentsFor(w);
  const P = buildShots(shots, { trans: () => ({ type: "cut", d: 0 }), kbScale: 1.4 });
  const pic = scene({
    id: "pic",
    css: `${P.css}
    .p-kb img { filter: blur(9px) saturate(0.55) brightness(0.46) contrast(1.1); }
    #p-wash { position: absolute; inset: 0; z-index: 40; background: linear-gradient(100deg, rgba(10,8,6,0.72) 0%, rgba(10,8,6,0.3) 60%, rgba(10,8,6,0.55) 100%); }`,
    html: `${P.html}    <div id="p-wash" data-layout-ignore></div>`,
    js: P.js,
  });

  const groups = sents.flatMap((s, si) => groupsOf(s, 3).map((g) => ({ g, si, n: s.n })));
  const layouts = ["L", "R", "L", "C"];
  let html = "", js = "", css = "";
  groups.forEach(({ g, si }, gi) => {
    const id = `k${gi + 1}`;
    const start = gi === 0 ? 0 : r(Math.max(0.1, g[0].t0 - 0.04));
    const next = groups[gi + 1] ? groups[gi + 1].g[0].t0 - 0.04 : D - 0.05;
    const end = r(Math.min(g.at(-1).t1 + 0.6, next - 0.02));
    const longest = Math.max(...g.map((x) => cps(x.text)));
    const size = Math.round(Math.min(g.length === 1 ? 300 : g.length === 2 ? 230 : 196, 1560 / (longest * 0.6)));
    const lay = g.length === 1 ? "C" : layouts[gi % layouts.length];
    const lh = Math.round(size * 1.3);
    const top = Math.round(520 - (lh * g.length) / 2);
    html += `    <div id="${id}" class="k-grp k-${lay} clip" data-start="${start}" data-duration="${r(end - start)}" data-track-index="1" style="top:${top}px;height:${lh * g.length}px"><div id="${id}-in" class="k-in" style="font-size:${size}px;line-height:${lh}px">${g
      .map((x, k) => `<div class="k-line" style="height:${lh}px"><span id="${id}-w${k}" class="k-w">${esc(x.text)}</span></div>`)
      .join("")}</div></div>\n`;
    g.forEach((x, k) => {
      const t = k === 0 ? start : r(x.t0 - 0.03);
      const from = lay === "R" ? `{ opacity: 0, x: 90 }` : lay === "C" ? `{ opacity: 0, scale: 1.5 }` : `{ opacity: 0, y: ${Math.round(size * 0.5)} }`;
      const to = lay === "R" ? `{ opacity: 1, x: 0, duration: 0.2, ease: "expo.out" }` : lay === "C" ? `{ opacity: 1, scale: 1, duration: 0.22, ease: "expo.out" }` : `{ opacity: 1, y: 0, duration: 0.2, ease: "expo.out" }`;
      if (gi > 0 || k > 0) js += `      tl.fromTo("#${id}-w${k}", ${from}, ${to}, ${t});\n`; // the opening word is on screen at frame 0
      js += `      tl.fromTo("#${id}-w${k}", { color: "#ffb347" }, { color: "#f7f1e2", duration: 0.25, ease: "power1.in" }, ${r(Math.max(x.t1, t + 0.25))});\n`;
    });
    js += `      tl.to("#${id}-in", { opacity: 0, duration: 0.08, ease: "power2.in" }, ${r(end - 0.09)});\n`;
  });
  const nS = sents.length;
  // sentence counter + rule that grows through each sentence
  sents.forEach((s, i) => {
    const t0 = i === 0 ? 0 : r(s.t0 - 0.04), t1 = sents[i + 1] ? r(sents[i + 1].t0 - 0.04) : D;
    html += `    <div id="kn${i}" class="k-num clip" data-start="${t0}" data-duration="${r(t1 - t0)}" data-track-index="3"><b>${String(i + 1).padStart(2, "0")}</b><span>/ ${String(nS).padStart(2, "0")}</span></div>\n`;
  });
  js += `      tl.fromTo("#k-bar-f", { scaleX: 0 }, { scaleX: 1, duration: ${D}, ease: "none" }, 0);\n`;

  const type = scene({
    id: "type",
    css: `    ${FONTS.anek}
    ${FONTS.oswald}
    .k-grp { position: absolute; left: 150px; width: 1620px; }
    .k-in { position: absolute; inset: 0; font-family: "NK Anek Tamil", sans-serif; font-weight: 800; font-stretch: 80%; color: #f7f1e2; white-space: nowrap; }
    .k-line { overflow: visible; }
    .k-w { display: inline-block; text-shadow: 0 6px 40px rgba(0,0,0,0.6); }
    .k-R .k-in { text-align: right; }
    .k-C .k-in { text-align: center; }
    .k-L .k-w { transform-origin: 0% 60%; } .k-R .k-w { transform-origin: 100% 60%; } .k-C .k-w { transform-origin: 50% 60%; }
    .k-num { position: absolute; left: 150px; top: 70px; width: 300px; height: 60px; font: 500 40px/60px "NK Oswald", sans-serif; letter-spacing: 0.1em; color: rgba(247,241,226,0.6); }
    .k-num b { font-weight: 600; color: #ffb347; margin-right: 10px; }
    #k-tag { position: absolute; right: 150px; top: 70px; height: 60px; font: 500 40px/60px "NK Oswald", sans-serif; letter-spacing: 0.1em; color: rgba(247,241,226,0.6); }
    #k-bar { position: absolute; left: 150px; top: 990px; width: 1620px; height: 4px; background: rgba(247,241,226,0.2); }
    #k-bar-f { position: absolute; inset: 0; background: #ffb347; transform-origin: 0% 50%; }`,
    html: `${html}    <div id="k-tag">NAGAPATTINAM 1856</div>
    <div id="k-bar" data-layout-ignore><div id="k-bar-f"></div></div>`,
    js,
  });

  writeStyle("07-kinetic-type", "NK 07 Kinetic typography", {
    "index.html": index({
      title: "NK style 07 — Kinetic typography", dur: D, bg: "#0a0806",
      hosts: [{ id: "pic" }, { id: "type", kind: "captions" }],
      audio: [
        { id: "vo", src: WIN[w].audio, start: 0, dur: WIN[w].adur, vol: 1 },
        ...shots.slice(1).map((s, i) => sfx(i % 2 ? "click-soft" : "key-press", s.t0, 0.22)),
      ],
    }),
    "compositions/pic.html": pic,
    "compositions/type.html": type,
  });
}
