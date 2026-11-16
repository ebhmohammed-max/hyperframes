// Title sequence (12 s, no voice, no numbers): crown → the prince → the empty throne with the title.
//   node film/title.mjs → film/TITLE/
import { mkdirSync, writeFileSync, symlinkSync, rmSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { r, scene, index, rng, sfx, FONTS } from "../kit/gen/lib.mjs";
import { grain } from "../kit/gen/caps.mjs";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const C = { gold: "#f3d48a", cream: "#f6efdc", ink: "#070a18" };
const D = 12, T = 6.2; // length, title reveal
// [plate, in, out, transform-origin, from [scale,x,y], to [scale,x,y]]
const P = [
  ["002", 0, 3.5, "42% 70%", [1.08, 0, 0], [1.2, 0, 0]],
  ["298", 2.9, 6.3, "50% 35%", [1.2, 0, 10], [1.08, 0, 0]],
  ["026", 5.7, D, "38% 52%", [1.05, 0, 0], [1.16, 0, 0]],
];
const G = grain("t-grain", D, rng(77), { opacity: 0.11 });

const css = `    ${FONTS.serifTa}
    ${FONTS.sansTa}
    ${FONTS.oswald}
    .t-pl { position: absolute; inset: 0; overflow: hidden; }
    .t-pl img { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; opacity: 0; }
    #t-vig { position: absolute; inset: 0; z-index: 20; background: radial-gradient(ellipse at 50% 46%, rgba(0,0,0,0) 40%, rgba(4,6,14,0.62) 100%); }
    #t-shade { position: absolute; inset: 0; z-index: 21; background: linear-gradient(180deg, rgba(5,7,18,0.5) 0%, rgba(5,7,18,0.7) 45%, rgba(5,7,18,0.8) 100%); opacity: 0; }
${G.css}
    #t-pre { position: absolute; left: 0; width: 1920px; top: 942px; height: 80px; z-index: 70; text-align: center; }
    #t-pre-in { opacity: 0; font: 560 40px/1.5 "NK Sans Tamil", sans-serif; letter-spacing: 0.06em; color: ${C.cream}; text-shadow: 0 2px 14px rgba(0,0,0,0.9); }
    #t-pre-in b { font-weight: 700; color: ${C.gold}; }
    #t-ttl { position: absolute; inset: 0; z-index: 72; }
    #t-r1 { position: absolute; left: 760px; top: 318px; width: 400px; height: 2px; background: ${C.gold}; opacity: 0; transform-origin: 50% 50%; }
    #t-name { position: absolute; left: 0; width: 1920px; top: 352px; text-align: center; font: 700 158px/1.42 "NK Serif Tamil", serif; color: ${C.gold}; opacity: 0; text-shadow: 0 6px 40px rgba(0,0,0,0.85), 0 0 90px rgba(243,212,138,0.18); white-space: nowrap; }
    #t-r2 { position: absolute; left: 860px; top: 604px; width: 200px; height: 3px; background: ${C.gold}; opacity: 0; transform-origin: 50% 50%; }
    #t-sub { position: absolute; left: 0; width: 1920px; top: 640px; text-align: center; font: 600 74px/1.45 "NK Sans Tamil", sans-serif; color: ${C.cream}; opacity: 0; text-shadow: 0 3px 22px rgba(0,0,0,0.9); white-space: nowrap; }
    #t-nk { position: absolute; left: 0; width: 1920px; top: 936px; text-align: center; font: 500 30px/1.3 "NK Oswald", sans-serif; letter-spacing: 0.42em; color: rgba(246,239,220,0.82); opacity: 0; white-space: nowrap; }
    #t-fade { position: absolute; inset: 0; z-index: 95; background: #000; }`;

const html = `${P.map(([n, a, b], i) => `    <div id="t-p${i}" class="t-pl clip" data-start="${a}" data-duration="${r(b - a)}" data-track-index="${i + 1}" style="z-index:${i + 1}"><img id="t-p${i}-img" src="assets/plates/${n}.jpg" alt="" /></div>`).join("\n")}
    <div id="t-vig" data-layout-ignore></div>
    <div id="t-shade" data-layout-ignore></div>
${G.html}    <div id="t-pre" class="clip" data-start="0.7" data-duration="2.6" data-track-index="5"><div id="t-pre-in"><b>நிலவன் கதைகள்</b> வழங்கும்</div></div>
    <div id="t-ttl" class="clip" data-start="${r(T - 0.3)}" data-duration="${r(D - T + 0.3)}" data-track-index="6">
      <div id="t-r1"></div>
      <div id="t-name">பூம்புகார்</div>
      <div id="t-r2"></div>
      <div id="t-sub">கடலுக்கு அடியில நிஜமா என்ன இருக்கு?</div>
      <div id="t-nk">NK DOCUMENTARIES</div>
    </div>
    <div id="t-fade" class="clip" data-start="0" data-duration="${D}" data-track-index="7" data-layout-ignore></div>`;

let js = `      tl.fromTo("#t-fade", { opacity: 1 }, { opacity: 0, duration: 0.9, ease: "power1.out" }, 0);
      tl.to("#t-fade", { opacity: 1, duration: 0.85, ease: "power2.in" }, ${D - 0.9});\n`;
P.forEach(([n, a, b, o, f, t], i) => {
  js += `      tl.fromTo("#t-p${i}-img", { scale: ${f[0]}, x: ${f[1]}, y: ${f[2]}, transformOrigin: "${o}" }, { scale: ${t[0]}, x: ${t[1]}, y: ${t[2]}, duration: ${r(b - a)}, ease: "none" }, ${a});
      tl.fromTo("#t-p${i}-img", { opacity: 0 }, { opacity: 1, duration: ${i ? 0.6 : 0.05}, ease: "power1.inOut" }, ${a});\n`;
});
js += `${G.js}      tl.fromTo("#t-pre-in", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.5, ease: "power2.out" }, 0.8);
      tl.to("#t-pre-in", { opacity: 0, duration: 0.4, ease: "power2.in" }, 2.8);
      tl.to("#t-shade", { opacity: 1, duration: 0.7, ease: "power2.out" }, ${r(T - 0.25)});
      tl.fromTo("#t-name", { opacity: 0, scale: 1.12, filter: "blur(14px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.7, ease: "expo.out" }, ${T});
      tl.to("#t-name", { scale: 1.035, duration: ${r(D - T - 0.7)}, ease: "none" }, ${r(T + 0.7)});
      tl.fromTo("#t-r1", { opacity: 0, scaleX: 0 }, { opacity: 0.85, scaleX: 1, duration: 0.7, ease: "expo.out" }, ${r(T + 0.15)});
      tl.fromTo("#t-r2", { opacity: 0, scaleX: 0 }, { opacity: 1, scaleX: 1, duration: 0.6, ease: "expo.out" }, ${r(T + 0.9)});
      tl.fromTo("#t-sub", { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.55, ease: "power3.out" }, ${r(T + 1.1)});
      tl.fromTo("#t-nk", { opacity: 0 }, { opacity: 1, duration: 0.8, ease: "power1.out" }, ${r(T + 2.0)});\n`;

const audio = [sfx("impact-bass-1", 0.15, 0.22, D), sfx("whoosh", 2.95, 0.14, D), sfx("whoosh-cinematic", T, 0.2, D), sfx("impact-bass-2", T, 0.36, D), sfx("whoosh-short", T + 1.1, 0.1, D)];

const dir = join(ROOT, "film", "TITLE");
mkdirSync(join(dir, "compositions"), { recursive: true });
writeFileSync(join(dir, "compositions/ttl.html"), scene({ id: "ttl", css, html, js }));
writeFileSync(join(dir, "index.html"), index({ title: "EP12 title", dur: D, bg: "#000", hosts: [{ id: "ttl" }], audio }));
writeFileSync(join(dir, "hyperframes.json"), JSON.stringify({ $schema: "https://hyperframes.heygen.com/schema/hyperframes.json", registry: "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry", paths: { blocks: "compositions", components: "compositions/components", assets: "assets" }, media: { autoProxy: true } }, null, 2) + "\n");
writeFileSync(join(dir, "meta.json"), JSON.stringify({ id: "nk-ep12-title", name: "EP12 title", createdAt: "2026-11-16T09:00:00.000Z" }, null, 2) + "\n");
rmSync(join(dir, "assets"), { recursive: true, force: true });
symlinkSync("../../shared", join(dir, "assets"));
console.log("TITLE:", D, "s");
