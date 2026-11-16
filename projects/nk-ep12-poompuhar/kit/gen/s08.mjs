// 08 — Title sequence / teaser (no narration): the question card, a riser, all 17 plates in an
// accelerating cut (whips, zoom-throughs, then hard cuts on impacts), a flash, and the episode
// title card. Card wording is taken from the EP06 cards.
import { r, index, scene, writeStyle, buildShots, FONTS, sfx, rng } from "./lib.mjs";
import { grain } from "./caps.mjs";

export default function build() {
  const D = 15.5, T0 = 3.6;
  const plates = ["sh010", "sh014", "sh015", "sh023", "sh011", "sh017", "sh018", "sh012", "sh005", "sh005a", "sh001", "sh002", "sh003", "sh008", "sh006", "sh007", "sh004"];
  const lens = [0.86, 0.8, 0.74, 0.66, 0.58, 0.52, 0.46, 0.4, 0.36, 0.32, 0.28, 0.24, 0.21, 0.18, 0.16, 0.14, 0.34];
  let t = T0;
  const R = rng(25);
  const shots = plates.map((p, i) => {
    const s = { k: `m${i}`, plate: p, t0: r(t), t1: r(t + lens[i]), o: `${40 + Math.round(R() * 20)}% ${45 + Math.round(R() * 12)}%`, a: i % 2 ? [1.3, 0, 0] : [1.08, 0, 0], b: i % 2 ? [1.12, 0, 0] : [1.26, 0, 0], ease: "power2.out" };
    t += lens[i];
    return s;
  });
  const TT = r(t); // title card time
  shots[0].t0 = T0;
  const P = buildShots(shots, {
    trans: (i) => (i < 5 ? { type: i % 2 ? "whip" : "zoomThrough", d: 0.26 } : { type: "cut", d: 0 }),
  });
  // buildShots starts the first shot where it is told; shift every clip so nothing shows before T0
  const G = grain("m-grain", D, rng(8), { opacity: 0.14 });
  const pic = scene({
    id: "pic",
    css: `    ${FONTS.serifTa}
${P.css}
    #m-bars { position: absolute; inset: 0; z-index: 50; box-shadow: inset 0 132px 0 #000, inset 0 -132px 0 #000; }
    #m-flash { position: absolute; inset: 0; z-index: 45; background: #fff4e0; opacity: 0; }
    #m-flash2 { position: absolute; inset: 0; z-index: 70; background: #fff4e0; opacity: 0; }
    #m-q { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; z-index: 60; background: #0c0a08; }
    #m-q-in { position: absolute; left: 160px; top: 360px; width: 1600px; text-align: center; font: 700 96px/1.5 "NK Serif Tamil", serif; color: #f1e9d6; }
    .m-qw { display: inline-block; }
    #m-q-em { color: #f0a868; }
    #m-card { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; z-index: 61; background: #0c0a08; }
    #m-card-bg { position: absolute; inset: 0; background: url("assets/plates/sh015.jpg") center / cover; opacity: 0.2; filter: saturate(0.5); }
    #m-card-in { position: absolute; inset: 0; }
    #m-k { position: absolute; left: 0; width: 1920px; top: 318px; text-align: center; font: 700 46px/1.4 "NK Serif Tamil", serif; color: #f0a868; }
    #m-t { position: absolute; left: 0; width: 1920px; top: 420px; text-align: center; font: 700 92px/1.45 "NK Serif Tamil", serif; color: #f4ecd9; white-space: nowrap; }
    #m-rule { position: absolute; left: 860px; top: 604px; width: 200px; height: 4px; background: #3f9c8f; }
    #m-s { position: absolute; left: 0; width: 1920px; top: 640px; text-align: center; font: 400 52px/1.5 "NK Serif Tamil", serif; color: #d9cfb8; }
${G.css}`,
    html: `${P.html}    <div id="m-bars" data-layout-ignore></div>
    <div id="m-flash" data-layout-ignore></div>
    <div id="m-flash2" data-layout-ignore></div>
    <div id="m-q" class="clip" data-start="0" data-duration="${T0}" data-track-index="4"><div id="m-q-in">${["ஒரு", "நட்பு", "எப்படி"].map((x, i) => `<span id="m-qw${i}" class="m-qw">${x}</span>`).join(" ")}<br /><span id="m-q-em">${["ஒரு", "போராக", "மாறியது?"].map((x, i) => `<span id="m-qw${i + 3}" class="m-qw">${x}</span>`).join(" ")}</span></div></div>
    <div id="m-card" class="clip" data-start="${TT}" data-duration="${r(D - TT)}" data-track-index="5"><div id="m-card-bg" data-layout-ignore></div><div id="m-card-in">
      <div id="m-k">கால பயணம்</div>
      <div id="m-t">ராஜேந்திர சோழனும் ஸ்ரீவிஜயமும்</div>
      <div id="m-rule"></div>
      <div id="m-s">ஆயிரத்து இருபத்தைந்தாம் ஆண்டு</div>
    </div></div>
${G.html}`,
    js: `${P.js}${G.js}${[3, 4, 5].map((i) => `      tl.fromTo("#m-qw${i}", { opacity: 0, y: 26, filter: "blur(8px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.45, ease: "power3.out" }, ${r(0.9 + (i - 3) * 0.34)});`).join("\n")}
      tl.fromTo("#m-q-in", { scale: 1 }, { scale: 1.06, duration: ${T0}, ease: "none" }, 0);
      tl.to("#m-q-in", { opacity: 0, filter: "blur(14px)", duration: 0.22, ease: "power2.in" }, ${r(T0 - 0.24)});
      tl.fromTo("#m-flash", { opacity: 0.85 }, { opacity: 0, duration: 0.3, ease: "power2.out", immediateRender: false }, ${T0});
      tl.fromTo("#m-flash2", { opacity: 1 }, { opacity: 0, duration: 0.7, ease: "power2.out", immediateRender: false }, ${TT});
      tl.fromTo("#m-card-bg", { scale: 1.12 }, { scale: 1, duration: ${r(D - TT)}, ease: "power1.out" }, ${TT});
      tl.fromTo("#m-k", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, ${r(TT + 0.25)});
      tl.fromTo("#m-t", { opacity: 0, scale: 1.08, filter: "blur(10px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.8, ease: "power3.out" }, ${r(TT + 0.4)});
      tl.fromTo("#m-rule", { scaleX: 0 }, { scaleX: 1, duration: 0.6, ease: "power3.inOut" }, ${r(TT + 0.95)});
      tl.fromTo("#m-s", { opacity: 0 }, { opacity: 1, duration: 0.6, ease: "power2.out" }, ${r(TT + 1.3)});
      tl.to("#m-card-in", { opacity: 0, duration: 0.5, ease: "power2.in" }, ${r(D - 0.6)});
`,
  });
  const fx = [sfx("riser", T0, 0.5, D), sfx("impact-bass-2", T0, 0.7, D)];
  shots.slice(1).forEach((s, i) => {
    if (i < 4) fx.push(sfx(i % 2 ? "whoosh-short" : "whoosh", s.t0, 0.3, D));
    else if (i < 9) fx.push(sfx("impact-bass-1", s.t0, 0.32 + i * 0.02, D));
    else fx.push(sfx(i % 2 ? "click-soft" : "key-press", s.t0, 0.4, D));
  });
  fx.push(sfx("whoosh-cinematic", TT, 0.45, D), sfx("impact-bass-2", TT, 0.85, D), sfx("impact-bass-1", TT + 0.02, 0.6, D));
  writeStyle("08-title-sequence", "NK 08 Title sequence", {
    "index.html": index({ title: "NK style 08 — Title sequence", dur: D, bg: "#0c0a08", hosts: [{ id: "pic" }], audio: fx }),
    "compositions/pic.html": pic,
  });
}
