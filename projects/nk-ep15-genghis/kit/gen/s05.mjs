// 05 — Vintage film (silent-era 4:3): sepia orthochromatic plates in a rounded gate, gate weave,
// exposure flicker, running scratches, dust, heavy grain, iris in/out, an intertitle card and
// serif italic titles. Everything "random" is a seeded table baked at build time.
import { r, index, scene, writeStyle, buildShots, shotsFor, sentsFor, WIN, FONTS, rng } from "./lib.mjs";
import { capSentences, grain } from "./caps.mjs";

export default function build() {
  const w = "a", D = WIN[w].dur, GW = 1440, GH = 1080, GX = 240, FPS = 15;
  const CARD = 3.8; // intertitle holds while the place and year are spoken
  const shots = shotsFor(w), sents = sentsFor(w);
  const P = buildShots(shots, {
    W: GW, H: GH, kbScale: 0.7,
    src: (s) => `assets/plates_sepia/${s.plate}.jpg`,
    trans: (i) => ({ type: "fade", d: 1.0 }),
  });
  const R = rng(1856), N = Math.ceil(D * FPS);
  const weave = Array.from({ length: N }, () => [r((R() - 0.5) * 5), r((R() - 0.5) * 7), r((R() - 0.5) * 0.12)]);
  const flick = Array.from({ length: N }, () => r(R() < 0.12 ? 0.1 + R() * 0.1 : R() * 0.05));
  const scr = [0, 1, 2].map(() => { let x = 100 + R() * 1200, on = false; return Array.from({ length: N }, () => { if (R() < (on ? 0.14 : 0.035)) { on = !on; x = 100 + R() * 1200; } x += (R() - 0.5) * 6; return [Math.round(x), on ? r(0.12 + R() * 0.25) : 0]; }); });
  const dust = [0, 1, 2, 3, 4].map(() => Array.from({ length: N }, () => (R() < 0.16 ? [Math.round(R() * 1400), Math.round(R() * 1040), r(0.5 + R() * 1.6), r(0.5 + R() * 0.4)] : [0, 0, 1, 0])));
  const G = grain("f-grain", D, rng(5), { opacity: 0.34, fps: FPS, z: 70 });
  const C = capSentences(sents, { skip: [1, 2], merge: [] });

  const film = scene({
    id: "film",
    css: `    ${FONTS.tiro}
    ${FONTS.corm}
    #f-gate { position: absolute; left: ${GX}px; top: 0; width: ${GW}px; height: ${GH}px; }
    #f-win { position: absolute; left: 22px; top: 18px; width: ${GW - 44}px; height: ${GH - 36}px; overflow: hidden; border-radius: 38px; background: #0b0906; }
    #f-pic { position: absolute; left: -22px; top: -18px; width: ${GW}px; height: ${GH}px; }
${P.css}
    #f-card { position: absolute; left: 0; top: 0; width: ${GW}px; height: ${GH}px; z-index: 50; }
    #f-card-bg { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 50%, #241c12 0%, #0d0a06 78%); }
    #f-card-b1 { position: absolute; left: 130px; top: 130px; width: ${GW - 260}px; height: ${GH - 260}px; border: 3px solid #cdbb94; border-radius: 6px; }
    #f-card-b2 { position: absolute; left: 146px; top: 146px; width: ${GW - 292}px; height: ${GH - 292}px; border: 1px solid #cdbb94; }
    #f-card-k { position: absolute; left: 0; width: ${GW}px; top: 286px; text-align: center; font: italic 500 46px/1.3 "NK Cormorant", serif; letter-spacing: 0.14em; color: #cdbb94; }
    #f-card-t { position: absolute; left: 0; width: ${GW}px; top: 372px; text-align: center; font: 400 128px/1.4 "NK Tiro Tamil", serif; color: #efe3c4; }
    #f-card-r { position: absolute; left: ${GW / 2 - 120}px; top: 590px; width: 240px; height: 2px; background: #cdbb94; }
    #f-card-y { position: absolute; left: 0; width: ${GW}px; top: 622px; text-align: center; font: 500 120px/1.2 "NK Cormorant", serif; letter-spacing: 0.12em; color: #efe3c4; }
    #f-vig { position: absolute; inset: 0; z-index: 55; background: radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 42%, rgba(0,0,0,0.5) 82%, rgba(0,0,0,0.86) 100%); }
    #f-flick { position: absolute; inset: 0; z-index: 56; background: #fff3d6; opacity: 0; }
    .f-scr { position: absolute; top: 0; width: 2px; height: ${GH}px; z-index: 57; background: rgba(255,246,220,0.9); opacity: 0; }
    .f-dust { position: absolute; left: 0; top: 0; width: 9px; height: 7px; z-index: 58; border-radius: 50%; background: #0a0805; opacity: 0; }
    #f-iris { position: absolute; inset: 0; z-index: 60; background: #050403; }
    #f-capz { position: absolute; left: 0; top: 0; width: ${GW}px; height: ${GH}px; z-index: 59; }
    .c-cap { position: absolute; left: 110px; width: ${GW - 220}px; bottom: 96px; text-align: center; }
    .c-in { display: inline-block; font: italic 400 50px/1.5 "NK Tiro Tamil", serif; color: #f3e8cc; text-shadow: 0 2px 4px rgba(0,0,0,0.95), 0 0 18px rgba(0,0,0,0.9), 0 0 40px rgba(0,0,0,0.7); }
${G.css}`,
    html: `    <div id="f-gate"><div id="f-win"><div id="f-pic">
${P.html}      <div id="f-card" class="clip" data-start="0" data-duration="${CARD + 0.45}" data-track-index="3"><div id="f-card-in" style="position:absolute;inset:0">
        <div id="f-card-bg" data-layout-ignore></div><div id="f-card-b1" data-layout-ignore></div><div id="f-card-b2" data-layout-ignore></div>
        <div id="f-card-k">Tamil Coast</div>
        <div id="f-card-t">நாகப்பட்டினம்</div>
        <div id="f-card-r"></div>
        <div id="f-card-y">1856</div>
      </div></div>
      <div id="f-vig" data-layout-ignore></div>
      <div id="f-capz">
${C.html}      </div>
      <div id="f-flick" data-layout-ignore></div>
      ${[0, 1, 2].map((k) => `<div id="f-scr${k}" class="f-scr" data-layout-ignore></div>`).join("")}
      ${[0, 1, 2, 3, 4].map((k) => `<div id="f-dust${k}" class="f-dust" data-layout-ignore></div>`).join("")}
      <div id="f-iris" data-layout-ignore></div>
${G.html}    </div></div></div>`,
    js: `${P.js}${C.js}${G.js}      tl.fromTo("#f-iris", { clipPath: "circle(0% at 50% 50%)" }, { clipPath: "circle(0% at 50% 50%)", duration: 0.01 }, 0);
      tl.fromTo("#f-iris", { opacity: 1 }, { opacity: 0, duration: 0.9, ease: "power2.out" }, 0);
      tl.fromTo("#f-card-y", { opacity: 0 }, { opacity: 1, duration: 0.5, ease: "power1.out" }, 1.5);
      tl.fromTo("#f-card-r", { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power2.out" }, 1.35);
      tl.to("#f-card-in", { opacity: 0, duration: 0.4, ease: "power1.inOut" }, ${CARD});
      tl.set("#f-iris", { opacity: 1, clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)", WebkitMaskImage: "radial-gradient(circle at 50% 50%, rgba(0,0,0,0) 99%, #000 100%)" }, ${r(D - 1.3)});
      { const o = { v: 99 }; tl.to(o, { v: 0, duration: 1.1, ease: "power2.in", onUpdate: () => { document.getElementById("f-iris").style.webkitMaskImage = "radial-gradient(circle at 50% 50%, rgba(0,0,0,0) " + o.v.toFixed(2) + "%, #000 " + (o.v + 1).toFixed(2) + "%)"; } }, ${r(D - 1.3)}); }
      { const WV = ${JSON.stringify(weave)}, FL = ${JSON.stringify(flick)}, SC = ${JSON.stringify(scr)}, DU = ${JSON.stringify(dust)};
        for (let f = 0; f < ${N}; f++) { const t = f / ${FPS};
          tl.set("#f-pic", { x: WV[f][0], y: WV[f][1], rotation: WV[f][2] }, t);
          tl.set("#f-flick", { opacity: FL[f] }, t);
          for (let k = 0; k < 3; k++) tl.set("#f-scr" + k, { x: SC[k][f][0], opacity: SC[k][f][1] }, t);
          for (let k = 0; k < 5; k++) tl.set("#f-dust" + k, { x: DU[k][f][0], y: DU[k][f][1], scale: DU[k][f][2], opacity: DU[k][f][3] }, t);
        } }
`,
  });

  writeStyle("05-vintage-film", "NK 05 Vintage film", {
    "index.html": index({
      title: "NK style 05 — Vintage film", dur: D, bg: "#050403",
      hosts: [{ id: "film", kind: "captions" }],
      audio: [{ id: "vo", src: WIN[w].audio, start: 0, dur: WIN[w].adur, vol: 1 }],
    }),
    "compositions/film.html": film,
  });
}
