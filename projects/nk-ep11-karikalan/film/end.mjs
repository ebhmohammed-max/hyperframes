// End card (17 s): channel banner, captions at the top, like / comment / SUBSCRIBE / bell row with a cursor
// that clicks in step with the N11 narration. Silent apart from the voice.   node film/end.mjs → film/END/
import { mkdirSync, writeFileSync, symlinkSync, rmSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { r, scene, index, esc, FONTS } from "../kit/gen/lib.mjs";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const C = { gold: "#f3d48a", cream: "#f6efdc", navy: "rgba(10,14,34,0.88)", red: "#e8201f", grey: "#30333b" };
const D = 17, L = 1.0; // film length, seconds before the voice
// N11 sentences (seconds in the audio), measured from the pauses
const S = [
  ["இந்த கதை உங்களுக்கு பிடிச்சிருந்தா, ஒரு லைக் பண்ணுங்க.", 0.25, 2.59],
  ["இது மாதிரி மறைஞ்சு போன உண்மைக் கதைகள் இன்னும் நிறைய இருக்கு.", 3.14, 5.64],
  ["மிஸ் பண்ணாம பாக்க, நிலவன் கதைகள் சேனலை சப்ஸ்கிரைப் பண்ணுங்க.", 6.19, 9.32],
  ["பெல் ஐகானையும் அழுத்துங்க.", 9.77, 11.16],
  ["அடுத்த கதையில சந்திப்போம்.", 11.51, 12.72],
].map(([text, a, b]) => ({ text, t0: r(L + a), t1: r(L + b) }));

const ICON = {
  like: "M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2z",
  comment: "M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z",
  bell: "M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z",
};
const svg = (d, fill, size = 46) => `<svg class="e-ic" width="${size}" height="${size}" viewBox="0 0 24 24"><path d="${d}" fill="${fill}"/></svg>`;

// layout: row centred on x = 960, y = 770
const Y = 722, H = 96, GAP = 40, WS = 330;
const X0 = 960 - (H * 3 + WS + GAP * 3) / 2;
const X = { like: X0, comment: X0 + H + GAP, sub: X0 + 2 * (H + GAP), bell: X0 + 2 * (H + GAP) + WS + GAP };
const cx = { like: X.like + H / 2, comment: X.comment + H / 2, sub: X.sub + WS * 0.62, bell: X.bell + H / 2 };
// beats
const T = { likeIn: S[0].t0 + 0.05, commentIn: S[0].t0 + 0.3, likeClick: S[0].t1 - 0.55, pill: S[1].t0 + 0.1, commentHover: S[1].t0 + 1.3,
  subIn: S[2].t0 - 0.45, subClick: S[2].t1 - 0.75, bellIn: S[3].t0 - 0.05, bellClick: S[3].t1 - 0.35 };

const circle = (k, label) => `    <div id="e-${k}" class="e-btn e-circ" style="left:${X[k]}px; top:${Y}px">
      <div id="e-${k}-off" class="e-face e-off">${svg(ICON[k], C.cream)}</div>
      <div id="e-${k}-on" class="e-face e-on">${svg(ICON[k], "#1a1408")}</div>
      <div class="e-lab">${label}</div>
    </div>\n`;

const css = `    ${FONTS.sansTa}
    ${FONTS.oswald}
    #e-bg { position: absolute; inset: 0; overflow: hidden; }
    #e-bg img { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; transform-origin: 50% 50%; }
    #e-shade { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(4,6,16,0.78) 0%, rgba(4,6,16,0.2) 30%, rgba(4,6,16,0.05) 52%, rgba(4,6,16,0.72) 74%, rgba(4,6,16,0.9) 100%); }
    .e-cap { position: absolute; left: 260px; width: 1400px; top: 92px; text-align: center; }
    .e-cap-in { opacity: 0; font: 560 56px/1.4 "NK Sans Tamil", sans-serif; color: #fff; text-wrap: balance; text-shadow: 0 0 5px rgba(0,0,0,0.95), 0 2px 12px rgba(0,0,0,0.9), 0 0 40px rgba(0,0,0,0.75); }
    #e-row { position: absolute; inset: 0; }
    .e-btn { position: absolute; height: ${H}px; opacity: 0; }
    .e-circ { width: ${H}px; }
    .e-face { position: absolute; left: 0; top: 0; width: 100%; height: ${H}px; border-radius: ${H / 2}px; display: flex; align-items: center; justify-content: center; }
    .e-off { background: rgba(10,14,34,0.86); border: 2.5px solid rgba(246,239,220,0.75); }
    .e-on { background: ${C.gold}; opacity: 0; box-shadow: 0 0 34px rgba(243,212,138,0.55); }
    .e-lab { position: absolute; left: -80px; width: ${H + 160}px; top: ${H + 14}px; text-align: center; font: 600 27px/1.3 "NK Sans Tamil", sans-serif; color: ${C.gold}; white-space: nowrap; text-shadow: 0 2px 8px rgba(0,0,0,0.9); }
    #e-sub { width: ${WS}px; }
    #e-sub .e-face { gap: 14px; }
    #e-sub-red { background: ${C.red}; box-shadow: 0 6px 30px rgba(232,32,31,0.45); }
    #e-sub-grey { background: ${C.grey}; opacity: 0; border: 2px solid rgba(255,255,255,0.14); }
    .e-st { font: 600 42px/1 "NK Oswald", sans-serif; letter-spacing: 0.04em; color: #fff; }
    #e-sub .e-lab { left: 0; width: ${WS}px; font: 500 27px/1.3 "NK Oswald", sans-serif; letter-spacing: 0.03em; color: ${C.cream}; }
    .e-play { width: 54px; height: 38px; border-radius: 10px; background: #fff; display: flex; align-items: center; justify-content: center; }
    .e-play i { display: block; width: 0; height: 0; border-left: 15px solid ${C.red}; border-top: 9px solid transparent; border-bottom: 9px solid transparent; margin-left: 4px; }
    #e-pill { position: absolute; left: 560px; width: 800px; top: 924px; height: 64px; text-align: center; }
    #e-pill-in { opacity: 0; display: inline-block; padding: 9px 34px; border-radius: 34px; border: 2px solid rgba(243,212,138,0.7); background: rgba(10,14,34,0.7); font: 600 31px/1.4 "NK Sans Tamil", sans-serif; color: ${C.cream}; white-space: nowrap; }
    #e-cur { position: absolute; left: 0; top: 0; width: 54px; height: 54px; opacity: 0; filter: drop-shadow(0 3px 6px rgba(0,0,0,0.7)); }
    #e-fade { position: absolute; inset: 0; background: #000; }`;

const html = `    <div id="e-bg" class="clip" data-start="0" data-duration="${D}" data-track-index="1"><img id="e-bg-img" src="assets/brand/banner_1920.jpg" alt="" /></div>
    <div id="e-shade" data-layout-ignore></div>
${S.map((s, i) => `    <div id="e-c${i}" class="e-cap clip" data-start="${r(s.t0 - 0.08)}" data-duration="${r((S[i + 1] ? S[i + 1].t0 - 0.2 : s.t1 + 1.6) - s.t0 + 0.08)}" data-track-index="2"><div id="e-c${i}-in" class="e-cap-in">${esc(s.text)}</div></div>`).join("\n")}
    <div id="e-row" class="clip" data-start="0" data-duration="${D}" data-track-index="3" data-layout-allow-overflow>
${circle("like", "லைக்")}${circle("comment", "கமெண்ட்")}    <div id="e-sub" class="e-btn" style="left:${X.sub}px; top:${Y}px">
      <div id="e-sub-red" class="e-face"><span class="e-play"><i></i></span><span class="e-st">SUBSCRIBE</span></div>
      <div id="e-sub-grey" class="e-face"><span class="e-st">SUBSCRIBED</span></div>
      <div class="e-lab">@NilavanKadhaigal</div>
    </div>
${circle("bell", "பெல்")}      <div id="e-pill"><div id="e-pill-in">புதிய கதைகள்: புதன் 7PM · சனி 8:30PM</div></div>
      <svg id="e-cur" viewBox="0 0 24 24"><path d="M4 2v17l4.6-4.3 3 6.8 2.7-1.2-3-6.7 6.3-.4z" fill="#fff" stroke="#111" stroke-width="1.3" stroke-linejoin="round"/></svg>
    </div>
    <div id="e-fade" class="clip" data-start="0" data-duration="${D}" data-track-index="4" data-layout-ignore></div>`;

const pop = (id, t) => `      tl.fromTo("#${id}", { opacity: 0, scale: 0.6, y: 16 }, { opacity: 1, scale: 1, y: 0, duration: 0.42, ease: "back.out(1.9)" }, ${r(t)});\n`;
// cursor: travel to (x, y) arriving at t, press, release
const click = (x, y, t, from) => `      tl.${from ? `fromTo("#e-cur", { x: ${from[0]}, y: ${from[1]}, opacity: 0 }, { x: ${x}, y: ${y}, opacity: 1` : `to("#e-cur", { x: ${x}, y: ${y}`}, duration: 0.6, ease: "power2.inOut" }, ${r(t - 0.72)});
      tl.to("#e-cur", { scale: 0.8, duration: 0.08, ease: "power2.in" }, ${r(t - 0.06)});
      tl.to("#e-cur", { scale: 1, duration: 0.16, ease: "power2.out" }, ${r(t + 0.04)});\n`;
const press = (id, t) => `      tl.to("#${id}", { scale: 0.9, duration: 0.08, ease: "power2.in" }, ${r(t - 0.04)});
      tl.to("#${id}", { scale: 1, duration: 0.3, ease: "back.out(2.4)" }, ${r(t + 0.05)});\n`;

let js = `      tl.fromTo("#e-bg-img", { scale: 1.3, x: 60, y: -40 }, { scale: 1.38, x: 66, y: -40, duration: ${D}, ease: "none" }, 0);
      tl.fromTo("#e-fade", { opacity: 1 }, { opacity: 0, duration: 0.7, ease: "power1.out" }, 0);
      tl.to("#e-fade", { opacity: 1, duration: 0.85, ease: "power2.in" }, ${D - 0.9});\n`;
S.forEach((s, i) => {
  const end = S[i + 1] ? S[i + 1].t0 - 0.2 : s.t1 + 1.6;
  js += `      tl.fromTo("#e-c${i}-in", { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.2, ease: "power2.out" }, ${r(s.t0 - 0.08)});
      tl.to("#e-c${i}-in", { opacity: 0, duration: 0.14, ease: "power2.in" }, ${r(end - 0.16)});\n`;
});
js += pop("e-like", T.likeIn) + pop("e-comment", T.commentIn) + pop("e-sub", T.subIn) + pop("e-bell", T.bellIn);
js += `      tl.fromTo("#e-pill-in", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, ${r(T.pill)});\n`;
const tip = (k) => [Math.round(cx[k] - 8), Y + 50];
js += click(...tip("like"), T.likeClick, [cx.like + 260, Y + 330]) + press("e-like", T.likeClick);
js += `      tl.to("#e-like-on", { opacity: 1, duration: 0.14 }, ${r(T.likeClick)});\n`;
js += `      tl.to("#e-cur", { x: ${tip("comment")[0]}, y: ${tip("comment")[1] + 6}, duration: 0.7, ease: "power2.inOut" }, ${r(T.commentHover - 0.7)});
      tl.to("#e-comment", { scale: 1.1, duration: 0.2, ease: "power2.out" }, ${r(T.commentHover)});
      tl.to("#e-comment", { scale: 1, duration: 0.3, ease: "power2.inOut" }, ${r(T.commentHover + 0.5)});\n`;
js += click(...tip("sub"), T.subClick) + press("e-sub", T.subClick);
js += `      tl.to("#e-sub-red", { opacity: 0, duration: 0.14 }, ${r(T.subClick)});
      tl.to("#e-sub-grey", { opacity: 1, duration: 0.14 }, ${r(T.subClick)});\n`;
js += click(...tip("bell"), T.bellClick) + press("e-bell", T.bellClick);
js += `      tl.to("#e-bell-on", { opacity: 1, duration: 0.14 }, ${r(T.bellClick)});
      tl.fromTo("#e-bell .e-ic", { rotation: 0 }, { rotation: 16, duration: 0.09, yoyo: true, repeat: 5, ease: "sine.inOut", transformOrigin: "50% 10%" }, ${r(T.bellClick + 0.08)});
      tl.to("#e-cur", { x: ${cx.bell + 130}, y: ${Y + 250}, opacity: 0, duration: 0.7, ease: "power2.in" }, ${r(T.bellClick + 0.9)});\n`;

const dir = join(ROOT, "film", "END");
mkdirSync(join(dir, "compositions"), { recursive: true });
writeFileSync(join(dir, "compositions/end.html"), scene({ id: "end", css, html, js }));
writeFileSync(join(dir, "index.html"), index({ title: "EP11 end card", dur: D, bg: "#000", hosts: [{ id: "end" }], audio: [{ id: "vo", src: "assets/vo/N11.mp3", start: L, dur: 13.1, vol: 1 }] }));
writeFileSync(join(dir, "hyperframes.json"), JSON.stringify({ $schema: "https://hyperframes.heygen.com/schema/hyperframes.json", registry: "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry", paths: { blocks: "compositions", components: "compositions/components", assets: "assets" }, media: { autoProxy: true } }, null, 2) + "\n");
writeFileSync(join(dir, "meta.json"), JSON.stringify({ id: "nk-ep11-end", name: "EP11 end card", createdAt: "2026-11-16T09:00:00.000Z" }, null, 2) + "\n");
rmSync(join(dir, "assets"), { recursive: true, force: true });
symlinkSync("../../shared", join(dir, "assets"));
console.log("END:", D, "s");
