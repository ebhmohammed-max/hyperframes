// 01 — Classic documentary: the EP06 house look. Full-bleed plates, slow camera, soft dissolves,
// cream serif subtitles, location title in the EP06 card language (copper kicker, teal rule).
import { r, index, scene, writeStyle, buildShots, shotsFor, sentsFor, WIN, FONTS, rng, tAt } from "./lib.mjs";
import { capSentences, grain } from "./caps.mjs";

export default function build() {
  const w = "full", D = WIN[w].dur;
  const shots = shotsFor(w), sents = sentsFor(w);
  const P = buildShots(shots, { trans: (i, s) => (s.cut ? { type: "cut", d: 0 } : { type: "fade", d: 0.9 }) });
  const G = grain("p-grain", D, rng(11), { opacity: 0.13 });
  const pic = scene({
    id: "pic",
    css: `${P.css}
${G.css}
    #p-vig { position: absolute; inset: 0; z-index: 50; pointer-events: none; background: linear-gradient(180deg, rgba(6,4,2,0) 62%, rgba(6,4,2,0.62) 100%), radial-gradient(ellipse at 50% 46%, rgba(0,0,0,0) 50%, rgba(6,4,2,0.5) 100%); }
    #p-out { position: absolute; inset: 0; z-index: 70; }
    #p-out-fill { position: absolute; inset: 0; background: #0b0a08; }`,
    html: `${P.html}    <div id="p-vig" data-layout-ignore></div>
${G.html}    <div id="p-out" class="clip" data-start="${r(D - 0.9)}" data-duration="0.9" data-track-index="3"><div id="p-out-fill"></div></div>`,
    js: `${P.js}${G.js}      tl.fromTo("#p-out-fill", { opacity: 0 }, { opacity: 1, duration: 0.85, ease: "power2.in" }, ${r(D - 0.9)});`,
  });

  const ttl = scene({
    id: "ttl",
    css: `    ${FONTS.serifTa}
    ${FONTS.corm}
    #t-loc { position: absolute; left: 200px; top: 520px; width: 1100px; height: 380px; }
    #t-scrim { position: absolute; left: -200px; top: -120px; width: 1500px; height: 640px; background: radial-gradient(ellipse at 30% 60%, rgba(8,6,4,0.86) 0%, rgba(8,6,4,0.6) 38%, rgba(8,6,4,0) 72%); }
    #t-kick { position: absolute; left: 4px; top: 0; font: 700 42px/1.3 "NK Serif Tamil", serif; color: #ffbb7a; text-shadow: 0 2px 6px rgba(0,0,0,0.95), 0 0 22px rgba(0,0,0,0.9); }
    #t-name { position: absolute; left: 0; top: 58px; font: 700 112px/1.35 "NK Serif Tamil", serif; color: #f4ecd8; white-space: nowrap; text-shadow: 0 3px 30px rgba(0,0,0,0.55); }
    #t-rule { position: absolute; left: 6px; top: 232px; width: 170px; height: 4px; background: #4aa39b; transform-origin: 0% 50%; }
    #t-year { position: absolute; left: 4px; top: 246px; font: 600 88px/1.2 "NK Cormorant", serif; letter-spacing: 0.14em; color: #e9dfc8; text-shadow: 0 2px 20px rgba(0,0,0,0.6); }`,
    html: `    <div id="t-loc" class="clip" data-start="0" data-duration="4.45" data-track-index="1" data-layout-allow-overflow>
      <div id="t-scrim" data-layout-ignore></div>
      <div id="t-kick">கால பயணம்</div>
      <div id="t-name">நாகப்பட்டினம்</div>
      <div id="t-rule"></div>
      <div id="t-year">1856</div>
    </div>`,
    js: `      tl.fromTo("#t-scrim", { opacity: 0 }, { opacity: 1, duration: 0.5, ease: "power1.out" }, 0);
      tl.fromTo("#t-name", { opacity: 0, filter: "blur(10px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.45, ease: "power3.out" }, 0.08);
      tl.fromTo("#t-kick", { opacity: 0 }, { opacity: 1, duration: 0.4, ease: "power2.out" }, 0.3);
      tl.fromTo("#t-rule", { scaleX: 0 }, { scaleX: 1, duration: 0.7, ease: "expo.out" }, 0.95);
      tl.fromTo("#t-year", { opacity: 0, filter: "blur(8px)" }, { opacity: 1, filter: "blur(0px)", duration: 0.4, ease: "power3.out" }, 1.5);
      tl.to(["#t-kick", "#t-name", "#t-rule", "#t-year", "#t-scrim"], { opacity: 0, duration: 0.3, ease: "power2.in" }, 4.1);`,
  });

  const C = capSentences(sents, { skip: [1, 2], merge: [] });
  const cap = scene({
    id: "cap",
    css: `    ${FONTS.serifTa}
    .c-cap { position: absolute; left: 210px; width: 1500px; bottom: 92px; text-align: center; }
    .c-in { font: 400 52px/1.42 "NK Serif Tamil", serif; color: #f6efdc; text-wrap: balance; text-shadow: 0 0 6px rgba(0,0,0,0.9), 0 2px 14px rgba(0,0,0,0.85), 0 0 44px rgba(0,0,0,0.7); }`,
    html: C.html,
    js: C.js,
  });

  writeStyle("01-classic-documentary", "NK 01 Classic documentary", {
    "index.html": index({
      title: "NK style 01 — Classic documentary",
      dur: D,
      bg: "#0b0a08",
      hosts: [{ id: "pic" }, { id: "ttl" }, { id: "cap", kind: "captions" }],
      audio: [{ id: "vo", src: WIN[w].audio, start: 0, dur: WIN[w].adur, vol: 1 }],
    }),
    "compositions/pic.html": pic,
    "compositions/ttl.html": ttl,
    "compositions/cap.html": cap,
  });
}
