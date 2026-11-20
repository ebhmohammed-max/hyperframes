// 04 — Vertical short (9:16, 1080×1920): hook on frame 0, full-bleed crops that pan, punch-ins,
// flash cuts, a jolt on the strike, word-by-word captions with the spoken word boxed, progress bar.
// Text stays inside the 168–1330 px band the apps leave clear.
import { r, index, scene, writeStyle, buildShots, shotsFor, sentsFor, WIN, FONTS, rng, HIT, sfx, tAt } from "./lib.mjs";
import { capWords } from "./caps.mjs";

export default function build() {
  const w = "b", D = WIN[w].dur, W = 1080, H = 1920;
  const pos = { sh005: "36% 50%", sh001: "34% 50%", sh002: "50% 50%", sh008: "56% 50%", sh007: "42% 50%", sh004: "50% 50%" };
  const shots = shotsFor(w).map((s, i) => ({
    ...s,
    o: "50% 55%",
    // vertical crops are already tight: keep the punch-ins small and pan across the plate instead
    a: [1 + (s.a[0] - 1) * 0.3, i % 2 ? 110 : -110, 0],
    b: [1 + (s.b[0] - 1) * 0.3 + 0.05, i % 2 ? -110 : 110, 0],
  }));
  const sents = sentsFor(w);
  const hit = tAt(w, HIT);
  const P = buildShots(shots, { W, H, trans: () => ({ type: "cut", d: 0 }), kbEase: "sine.inOut" });
  const css = P.css.replace("object-fit: cover; }", "object-fit: cover; }\n" + shots.map((s, i) => `    #p${i + 1}-kb img { object-position: ${pos[s.plate]}; }`).join("\n"));
  let fxHtml = "", fxJs = "";
  shots.slice(1).forEach((s, i) => {
    fxHtml += `    <div id="p-fl${i}" class="p-fx clip" data-start="${s.t0}" data-duration="0.3" data-track-index="4"><div id="p-fl${i}-f" class="p-flash"></div></div>\n`;
    fxJs += `      tl.fromTo("#p-fl${i}-f", { opacity: ${["b7", "b11"].includes(s.k) ? 0.9 : 0.4} }, { opacity: 0, duration: 0.28, ease: "power2.out" }, ${s.t0});\n`;
  });
  const b5 = shots.findIndex((s) => s.k === "b5") + 1;
  const J = rng(9);
  let jolt = `      tl.fromTo("#p${b5}-tr", { scale: 1 }, { scale: 1.16, duration: 0.14, ease: "power4.out" }, ${hit});\n`;
  for (let k = 0; k < 7; k++) jolt += `      tl.to("#p${b5}-tr", { x: ${r((J() - 0.5) * 60 * (1 - k / 7))}, y: ${r((J() - 0.5) * 60 * (1 - k / 7))}, duration: 0.05, ease: "none" }, ${r(hit + k * 0.05)});\n`;
  jolt += `      tl.to("#p${b5}-tr", { x: 0, y: 0, duration: 0.08, ease: "power2.out" }, ${r(hit + 0.35)});\n`;

  const pic = scene({
    id: "pic", W, H,
    css: `${css}
    .p-fx { position: absolute; inset: 0; z-index: 40; }
    .p-flash { position: absolute; inset: 0; background: #fff6e6; }
    #p-shade { position: absolute; inset: 0; z-index: 45; background: linear-gradient(180deg, rgba(8,6,4,0.86) 0%, rgba(8,6,4,0.5) 26%, rgba(8,6,4,0) 44%, rgba(8,6,4,0.55) 66%, rgba(8,6,4,0.82) 100%); }`,
    html: `${P.html}${fxHtml}    <div id="p-shade" data-layout-ignore></div>`,
    js: `${P.js}${fxJs}${jolt}`,
  });

  const s9 = sents[0];
  const ui = scene({
    id: "ui", W, H,
    css: `    ${FONTS.anek}
    ${FONTS.oswald}
    #u-bar { position: absolute; left: 60px; top: 178px; width: 960px; height: 8px; border-radius: 4px; background: rgba(250,245,233,0.28); overflow: hidden; }
    #u-fill { position: absolute; inset: 0; background: #d5462f; transform-origin: 0% 50%; }
    #u-tag { position: absolute; left: 60px; top: 214px; width: 960px; height: 76px; }
    #u-tag-in { display: inline-flex; align-items: center; gap: 16px; padding: 8px 26px 8px; border-radius: 40px; background: #faf5e9; font: 700 40px/1.4 "NK Anek Tamil", sans-serif; color: #1a1409; }
    #u-tag-in b { font: 600 40px/1 "NK Oswald", sans-serif; letter-spacing: 0.06em; }
    .u-dia { width: 13px; height: 13px; background: #a63a28; transform: rotate(45deg); }
    #u-hook { position: absolute; left: 60px; top: 320px; width: 960px; height: 300px; }
    #u-hook-in { font: 800 92px/1.24 "NK Anek Tamil", sans-serif; font-stretch: 88%; color: #faf5e9; text-shadow: 0 4px 30px rgba(0,0,0,0.75); }
    #u-hook-in em { font-style: normal; color: #ffd591; }`,
    html: `    <div id="u-bar" data-layout-ignore><div id="u-fill"></div></div>
    <div id="u-tag" class="clip" data-start="0" data-duration="${D}" data-track-index="1"><div id="u-tag-in"><span>நாகப்பட்டினம்</span><span class="u-dia"></span><b>1856</b></div></div>
    <div id="u-hook" class="clip" data-start="0" data-duration="${r(sents[1].t0 - 0.1)}" data-track-index="2"><div id="u-hook-in">மண்ணுக்கு அடியில<br /><em>என்ன இருந்தது?</em></div></div>`,
    js: `      tl.fromTo("#u-fill", { scaleX: 0 }, { scaleX: 1, duration: ${D}, ease: "none" }, 0);
      tl.to("#u-hook-in", { opacity: 0, filter: "blur(10px)", duration: 0.22, ease: "power2.in" }, ${r(sents[1].t0 - 0.36)});`,
  });

  const C = capWords(sents, {
    max: 3, lead: 0.05, tail: 0.25, exit: 0.08,
    inAnim: (id, start, g) => `      tl.fromTo("#${id}-in", { opacity: 0, scale: 0.9 }, { opacity: 1, scale: 1, duration: 0.16, ease: "back.out(1.6)" }, ${start});\n`,
    onWord: (id, wid, wd) => `      tl.set("#${wid}", { backgroundColor: "#d5462f" }, ${wd.t0}); tl.set("#${wid}", { backgroundColor: "rgba(213,70,47,0)" }, ${wd.t1});\n`,
  });
  // the one-word sentence gets the frame to itself
  const capHtml = C.html.replace(/class="c-cap clip"([^>]*)>(<div id="c\d+-in" class="c-in"><span id="c\d+-w0" class="c-w">உலோகம்\.)/, 'class="c-cap c-big clip"$1>$2');
  const cap = scene({
    id: "cap", W, H,
    css: `    ${FONTS.anek}
    .c-cap { position: absolute; left: 60px; width: 960px; top: 1010px; height: 300px; display: flex; align-items: center; justify-content: center; text-align: center; }
    .c-in { font: 800 86px/1.36 "NK Anek Tamil", sans-serif; font-stretch: 86%; color: #fffaf0; -webkit-text-stroke: 12px #15110b; paint-order: stroke fill; }
    .c-w { display: inline-block; padding: 0 14px; border-radius: 16px; background-color: rgba(213,70,47,0); }
    .c-big { top: 760px; height: 420px; }
    .c-big .c-in { font-size: 230px; }`,
    html: capHtml,
    js: C.js,
  });

  const cutsFx = shots.slice(1).filter((s) => !["b7", "b11", "b5"].includes(s.k)).map((s, i) => sfx(i % 2 ? "whoosh-short" : "whoosh", s.t0, i % 2 ? 0.2 : 0.26));
  writeStyle("04-vertical-short", "NK 04 Vertical short", {
    "index.html": index({
      title: "NK style 04 — Vertical short", W, H, dur: D,
      hosts: [{ id: "pic" }, { id: "ui" }, { id: "cap", kind: "captions" }],
      audio: [
        { id: "vo", src: WIN[w].audio, start: 0, dur: WIN[w].adur, vol: 1 },
        ...cutsFx,
        sfx("impact-bass-1", hit, 0.5),
        sfx("riser", sents[9].t0 - 0.05, 0.24),
        sfx("impact-bass-2", sents[9].t0 - 0.05, 0.5),
        sfx("impact-bass-1", sents[13].t0 - 0.04, 0.4),
      ],
    }),
    "compositions/pic.html": pic,
    "compositions/ui.html": ui,
    "compositions/cap.html": cap,
  });
}
