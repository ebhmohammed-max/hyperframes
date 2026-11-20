// 02 — Cinematic trailer: 2.39:1 letterbox, bigger camera moves, dips to black, flash cuts,
// a camera jolt on the strike, type supers on the key words, and sound effects on the hits.
import { r, index, scene, writeStyle, buildShots, shotsFor, sentsFor, WIN, FONTS, rng, HIT, SENT, sfx } from "./lib.mjs";
import { capSentences, grain } from "./caps.mjs";

export default function build() {
  const w = "full", D = WIN[w].dur;
  const shots = shotsFor(w), sents = sentsFor(w);
  const dipAt = ["a3", "b1"], flashAt = ["b7", "b10", "b11"], leakAt = ["a5", "b9"];
  const P = buildShots(shots, {
    kbScale: 1.5,
    kbEase: "sine.inOut",
    trans: (i, s) => (s.cut || dipAt.includes(s.k) ? { type: "cut", d: 0 } : { type: "fade", d: 0.7 }),
  });
  const G = grain("p-grain", D, rng(22), { opacity: 0.17 });
  let fxHtml = "", fxJs = "";
  shots.forEach((s) => {
    if (dipAt.includes(s.k)) {
      fxHtml += `    <div id="p-dip-${s.k}" class="p-fx clip" data-start="${r(s.t0 - 0.4)}" data-duration="0.9" data-track-index="4"><div id="p-dip-${s.k}-f" class="p-black" style="opacity: 0"></div></div>\n`;
      fxJs += `      tl.fromTo("#p-dip-${s.k}-f", { opacity: 0 }, { opacity: 1, duration: 0.38, ease: "power2.in" }, ${r(s.t0 - 0.4)});
      tl.to("#p-dip-${s.k}-f", { opacity: 0, duration: 0.48, ease: "power2.out" }, ${r(s.t0 + 0.02)});\n`;
    }
    if (flashAt.includes(s.k)) {
      fxHtml += `    <div id="p-fl-${s.k}" class="p-fx clip" data-start="${s.t0}" data-duration="0.45" data-track-index="4"><div id="p-fl-${s.k}-f" class="p-flash"></div></div>\n`;
      fxJs += `      tl.fromTo("#p-fl-${s.k}-f", { opacity: 0.9 }, { opacity: 0, duration: 0.42, ease: "power2.out" }, ${s.t0});\n`;
    }
    if (leakAt.includes(s.k)) {
      fxHtml += `    <div id="p-lk-${s.k}" class="p-fx clip" data-start="${r(s.t0 - 0.6)}" data-duration="1.4" data-track-index="4" data-layout-allow-overflow><div id="p-lk-${s.k}-f" class="p-leak"></div></div>\n`;
      fxJs += `      tl.fromTo("#p-lk-${s.k}-f", { x: -1500, opacity: 0 }, { x: 300, opacity: 0.85, duration: 0.7, ease: "sine.in" }, ${r(s.t0 - 0.6)});
      tl.to("#p-lk-${s.k}-f", { x: 2100, opacity: 0, duration: 0.7, ease: "sine.out" }, ${r(s.t0 + 0.1)});\n`;
    }
  });
  // the strike: a snap push and a decaying jolt on the trowel shot
  const b5 = shots.findIndex((s) => s.k === "b5") + 1;
  const J = rng(5);
  let jolt = `      tl.fromTo("#p${b5}-tr", { scale: 1 }, { scale: 1.1, duration: 0.14, ease: "power4.out" }, ${r(HIT)});\n`;
  for (let k = 0; k < 7; k++) {
    const amp = 26 * (1 - k / 7);
    jolt += `      tl.to("#p${b5}-tr", { x: ${r((J() - 0.5) * 2 * amp)}, y: ${r((J() - 0.5) * 2 * amp)}, duration: 0.05, ease: "none" }, ${r(HIT + k * 0.05)});\n`;
  }
  jolt += `      tl.to("#p${b5}-tr", { x: 0, y: 0, duration: 0.08, ease: "power2.out" }, ${r(HIT + 0.35)});\n`;

  const pic = scene({
    id: "pic",
    css: `${P.css}
${G.css}
    .p-fx { position: absolute; inset: 0; z-index: 40; pointer-events: none; }
    .p-black { position: absolute; inset: 0; background: #000; }
    .p-flash { position: absolute; inset: 0; background: #fff3dc; }
    .p-leak { position: absolute; left: 0; top: -200px; width: 1300px; height: 1500px; mix-blend-mode: screen; background: radial-gradient(ellipse at 50% 50%, rgba(255,170,80,0.9) 0%, rgba(255,90,30,0.45) 35%, rgba(255,60,20,0) 70%); }
    #p-tint { position: absolute; inset: 0; z-index: 45; mix-blend-mode: soft-light; background: linear-gradient(180deg, rgba(40,110,120,0.5) 0%, rgba(0,0,0,0) 45%, rgba(190,90,20,0.35) 100%); }
    #p-vig { position: absolute; inset: 0; z-index: 46; background: radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 45%, rgba(0,0,0,0.62) 100%); }
    .p-bar { position: absolute; left: 0; width: 1920px; height: 139px; background: #000; z-index: 80; }
    #p-bar-t { top: 0; transform-origin: 50% 0%; } #p-bar-b { bottom: 0; transform-origin: 50% 100%; }
    #p-out { position: absolute; inset: 0; z-index: 70; }`,
    html: `${P.html}${fxHtml}    <div id="p-tint" data-layout-ignore></div>
    <div id="p-vig" data-layout-ignore></div>
${G.html}    <div id="p-out" class="clip" data-start="${r(D - 0.8)}" data-duration="0.8" data-track-index="5"><div id="p-out-f" class="p-black"></div></div>
    <div id="p-bar-t" class="p-bar" data-layout-ignore></div>
    <div id="p-bar-b" class="p-bar" data-layout-ignore></div>`,
    js: `${P.js}${fxJs}${jolt}${G.js}      tl.fromTo(".p-bar", { scaleY: 0 }, { scaleY: 1, duration: 1.1, ease: "power3.inOut" }, 0);
      tl.fromTo("#p-out-f", { opacity: 0 }, { opacity: 1, duration: 0.75, ease: "power2.in" }, ${r(D - 0.8)});`,
  });

  const s18 = sents[17], s21 = sents[20], s22 = sents[21];
  const ttl = scene({
    id: "ttl",
    css: `    ${FONTS.anek}
    ${FONTS.oswald}
    .t-full { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }
    #t-lat { position: absolute; left: 0; width: 1920px; top: 296px; text-align: center; font: 500 34px/1 "NK Oswald", sans-serif; letter-spacing: 0.62em; color: #e9e2d0; text-indent: 0.62em; }
    #t-big { position: absolute; left: 0; width: 1920px; top: 340px; text-align: center; font: 700 210px/1.3 "NK Anek Tamil", sans-serif; font-stretch: 88%; color: #f5efe0; text-shadow: 0 6px 60px rgba(0,0,0,0.55); white-space: nowrap; }
    #t-yr { position: absolute; left: 0; width: 1920px; top: 610px; text-align: center; font: 400 104px/1 "NK Oswald", sans-serif; letter-spacing: 0.5em; text-indent: 0.5em; color: #f5efe0; text-shadow: 0 4px 40px rgba(0,0,0,0.6); }
    #t-metal-w { position: absolute; left: 0; width: 1920px; top: 310px; text-align: center; font: 800 360px/1.25 "NK Anek Tamil", sans-serif; font-stretch: 80%; color: #f7f1e2; text-shadow: 0 10px 90px rgba(0,0,0,0.7); white-space: nowrap; }
    #t-end-a { position: absolute; left: 204px; top: 300px; font: 500 84px/1.3 "NK Anek Tamil", sans-serif; color: #e9e2d0; text-shadow: 0 4px 40px rgba(0,0,0,0.8); }
    #t-end-b { position: absolute; left: 200px; top: 410px; width: 720px; font: 800 128px/1.24 "NK Anek Tamil", sans-serif; font-stretch: 84%; color: #f7f1e2; text-shadow: 0 6px 60px rgba(0,0,0,0.8); }
    #t-scrim { position: absolute; inset: 0; background: rgba(0,0,0,0.34); }`,
    html: `    <div id="t-open" class="t-full clip" data-start="0" data-duration="4.4" data-track-index="1">
      <div id="t-scrim" data-layout-ignore></div>
      <div id="t-lat">TAMIL NADU COAST</div>
      <div id="t-big">நாகப்பட்டினம்</div>
      <div id="t-yr">1856</div>
    </div>
    <div id="t-metal" class="t-full clip" data-start="${r(s18.t0 - 0.06)}" data-duration="${r(41.5 - s18.t0 + 0.06)}" data-track-index="1"><div id="t-metal-w">உலோகம்.</div></div>
    <div id="t-end" class="t-full clip" data-start="${r(s21.t0 - 0.05)}" data-duration="${r(D - s21.t0 + 0.05)}" data-track-index="1">
      <div id="t-end-a">புதையல்,</div>
      <div id="t-end-b">இல்லன்னா<br />தெய்வம்.</div>
    </div>`,
    js: `      tl.fromTo("#t-big", { opacity: 0, filter: "blur(18px)", scale: 1.06 }, { opacity: 1, filter: "blur(0px)", scale: 1, duration: 0.6, ease: "expo.out" }, 0.05);
      tl.fromTo("#t-lat", { opacity: 0 }, { opacity: 0.9, duration: 0.5, ease: "power2.out" }, 0.45);
      tl.fromTo("#t-yr", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.45, ease: "power3.out" }, 1.48);
      tl.fromTo("#t-scrim", { opacity: 0 }, { opacity: 1, duration: 0.5, ease: "power1.out" }, 0);
      tl.to(["#t-big", "#t-lat", "#t-yr"], { opacity: 0, filter: "blur(12px)", duration: 0.28, ease: "power2.in" }, 4.08);
      tl.to("#t-scrim", { opacity: 0, duration: 0.3, ease: "power1.in" }, 4.08);
      tl.fromTo("#t-metal-w", { opacity: 0, scale: 1.18 }, { opacity: 1, scale: 1, duration: 0.14, ease: "power4.out" }, ${r(s18.t0 - 0.05)});
      tl.fromTo("#t-end-a", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.2, ease: "power3.out" }, ${r(s21.t0 - 0.04)});
      tl.fromTo("#t-end-b", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.25, ease: "power3.out" }, ${r(s22.t0 - 0.04)});
      tl.to(["#t-end-a", "#t-end-b"], { opacity: 0, duration: 0.6, ease: "power2.in" }, ${r(D - 0.75)});`,
  });

  const C = capSentences(sents, { skip: [1, 2, 18, 21, 22], merge: [] });
  const cap = scene({
    id: "cap",
    css: `    ${FONTS.sansTa}
    .c-cap { position: absolute; left: 260px; width: 1400px; bottom: 168px; text-align: center; }
    .c-in { font: 500 40px/1.4 "NK Sans Tamil", sans-serif; color: #f1ecdf; text-wrap: balance; text-shadow: 0 0 5px rgba(0,0,0,0.95), 0 2px 12px rgba(0,0,0,0.9), 0 0 36px rgba(0,0,0,0.7); }`,
    html: C.html,
    js: C.js,
  });

  writeStyle("02-cinematic-trailer", "NK 02 Cinematic trailer", {
    "index.html": index({
      title: "NK style 02 — Cinematic trailer",
      dur: D,
      hosts: [{ id: "pic" }, { id: "ttl" }, { id: "cap", kind: "captions" }],
      audio: [
        { id: "vo", src: WIN[w].audio, start: 0, dur: WIN[w].adur, vol: 1 },
        sfx("whoosh-cinematic", 9.05, 0.22),
        sfx("whoosh-cinematic", 20.65, 0.22),
        sfx("impact-bass-1", HIT, 0.5),
        sfx("riser", s18.t0 - 0.05, 0.26),
        sfx("impact-bass-2", s18.t0 - 0.05, 0.55),
        sfx("impact-bass-1", s22.t0 - 0.04, 0.42),
      ],
    }),
    "compositions/pic.html": pic,
    "compositions/ttl.html": ttl,
    "compositions/cap.html": cap,
  });
}
