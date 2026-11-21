// Shared story data + HTML helpers for the NK style samples.
// Every style is generated as a normal HyperFrames project (index.html + compositions/*.html):
// the generator only writes static, hand-editable HTML — nothing is created at render time.
import { mkdirSync, writeFileSync, existsSync, symlinkSync, rmSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

export const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
export const r = (x) => Math.round(x * 1000) / 1000;

// ── Narration: EP06 Act 1 cold open (voice19). Times are seconds in the Act 1 master,
// measured from the waveform (silence gaps), one entry per spoken sentence.
export const SENT = [
  ["நாகப்பட்டினம்.", 0.05, 0.87],
  ["ஆயிரத்து எண்ணூற்று ஐம்பத்தாறாம் வருஷம்.", 1.44, 4.1],
  ["கடற்கரையிலிருந்து கொஞ்ச தூரத்துல ஒரு பழைய மண் மேடு.", 4.49, 8.73],
  ["ஊரு மக்கள் அதை எப்பவோ இருந்து பார்த்துக்கிட்டு தான் இருக்காங்க.", 9.16, 12.27],
  ["அதுக்கு பெரிய மதிப்பு எதுவும் கிடையாது.", 12.33, 14.67],
  ["மழை பெஞ்சா அதோட ஓரம் கொஞ்சம் சரியும்.", 14.93, 17.58],
  ["வெயில் அடிச்சா அது வெடிக்கும்.", 17.94, 19.54],
  ["அவ்வளவு தான்.", 19.87, 20.39],
  ["அன்னிக்கு அங்க சில பேரு மண்ணைத் தோண்டிக்கிட்டு இருந்தாங்க.", 20.78, 23.97],
  ["தொல்பொருள் ஆராய்ச்சி இல்ல.", 24.53, 25.68],
  ["பெரிய நோக்கம் எதுவும் இல்ல.", 26.16, 27.41],
  ["சாதாரண வேலை தான்.", 27.73, 28.84],
  ["மண் கொஞ்சம் கொஞ்சமா விலகுது.", 29.23, 31.14],
  ["கருவி மண்ணுக்குள்ள இறங்குது.", 31.67, 33.35],
  ["திடீர்னு அது எதோ ஒண்ணுல மோதுது.", 33.66, 35.88],
  ["அந்த சத்தம் கல்லோட சத்தம் இல்ல.", 36.45, 38.47],
  ["வேரோட சத்தம் இல்ல.", 38.87, 40.04],
  ["உலோகம்.", 40.56, 41.11],
  ["தோண்டினவங்க நின்னுட்டாங்க.", 41.6, 43.22],
  ["அந்தக் காலத்துல, மண்ணுக்கு அடியில உலோகம்னா, அது பொதுவா ரெண்டுல ஒண்ணு.", 43.64, 48.28],
  ["புதையல்,", 48.82, 49.26],
  ["இல்லன்னா தெய்வம்.", 49.59, 50.37],
].map(([text, t0, t1], i) => ({ n: i + 1, text, t0, t1 }));

// Spoken weight of a Tamil word ≈ its syllable count (vowel-bearing letters; a consonant
// with a pulli closes the previous syllable and costs a little time).
function weight(w) {
  let n = 0.3;
  const cp = [...w];
  for (let i = 0; i < cp.length; i++) {
    const c = cp[i].codePointAt(0);
    if (c >= 0x0b85 && c <= 0x0b94) n += 1;
    else if (c >= 0x0b95 && c <= 0x0bb9) n += cp[i + 1] === "\u0bcd" ? 0.35 : 1;
  }
  return n;
}
/** Word timings inside one sentence, spread by spoken weight. */
export function wordsOf(s) {
  const ws = s.text.split(/\s+/);
  const wt = ws.map(weight);
  const tot = wt.reduce((a, b) => a + b, 0);
  let t = s.t0;
  return ws.map((text, i) => {
    const d = ((s.t1 - s.t0) * wt[i]) / tot;
    const o = { text, t0: r(t), t1: r(t + d), sn: s.n, i };
    t += d;
    return o;
  });
}
export const HIT = wordsOf(SENT[14]).at(-1).t0 + 0.12; // "மோதுது" — the tool strikes

// ── Picture: the shot plan on the same clock. s = scale, x/y = px drift, o = transform origin.
export const SHOTS = [
  { k: "a1", plate: "sh010", t0: 0, t1: 6.6, o: "40% 62%", a: [1.1, 50, 0], b: [1.19, -50, 0] },
  { k: "a2", plate: "sh005a", t0: 6.6, t1: 9.05, o: "50% 50%", a: [1.22, 0, 0], b: [1.1, 0, 0] },
  { k: "a3", plate: "sh011", t0: 9.05, t1: 12.25, o: "50% 56%", a: [1.05, 0, 0], b: [1.16, 0, 0] },
  { k: "a4", plate: "sh001", t0: 12.25, t1: 14.85, o: "35% 40%", a: [1.14, 45, 0], b: [1.14, -45, 0] },
  { k: "a5", plate: "sh014", t0: 14.85, t1: 17.85, o: "45% 45%", a: [1.17, 0, -24], b: [1.07, 0, 10] },
  { k: "a6", plate: "sh005a", t0: 17.85, t1: 20.65, o: "30% 60%", a: [1.52, 30, 0], b: [1.62, -30, 0] },
  { k: "b1", plate: "sh005", t0: 20.65, t1: 24.45, o: "40% 60%", a: [1.04, 0, 0], b: [1.11, 0, 0] },
  { k: "b2", plate: "sh005", t0: 24.45, t1: 29.05, o: "34% 64%", a: [1.46, 0, 0], b: [1.56, 0, 0], cut: 1 },
  { k: "b3", plate: "sh001", t0: 29.05, t1: 31.55, o: "30% 35%", a: [1.5, -30, 0], b: [1.36, 20, 0] },
  { k: "b4", plate: "sh002", t0: 31.55, t1: 33.55, o: "50% 55%", a: [1.05, 0, -16], b: [1.12, 0, 0] },
  { k: "b5", plate: "sh002", t0: 33.55, t1: 36.3, o: "48% 60%", a: [1.36, 0, 0], b: [1.5, 0, 0], cut: 1 },
  { k: "b6", plate: "sh002", t0: 36.3, t1: 40.45, o: "48% 60%", a: [1.72, 0, 0], b: [1.84, 0, 0], cut: 1 },
  { k: "b7", plate: "sh008", t0: 40.45, t1: 41.5, o: "55% 50%", a: [1.3, 0, 0], b: [1.2, 0, 0], cut: 1 },
  { k: "b8", plate: "sh005", t0: 41.5, t1: 43.5, o: "40% 60%", a: [1.09, 0, 0], b: [1.1, 0, 0], cut: 1 },
  { k: "b9", plate: "sh008", t0: 43.5, t1: 48.6, o: "55% 50%", a: [1.1, 0, 0], b: [1.3, 0, 0] },
  { k: "b10", plate: "sh007", t0: 48.6, t1: 49.45, o: "50% 55%", a: [1.12, 20, 0], b: [1.16, -10, 0], cut: 1 },
  { k: "b11", plate: "sh004", t0: 49.45, t1: 52, o: "62% 45%", a: [1.24, 0, 0], b: [1.08, 0, 0], cut: 1 },
];

// ── Excerpts. off = where the excerpt starts in the master; dur = film length.
export const WIN = {
  full: { off: 0, dur: 52, audio: "assets/audio/vo_full.mp3", adur: 51.6 },
  a: { off: 0, dur: 21.6, audio: "assets/audio/vo_a.mp3", adur: 20.62 },
  b: { off: 20.5, dur: 31.6, audio: "assets/audio/vo_b.mp3", adur: 31.1 },
};
/** Sentences / shots of an excerpt, re-clocked to film time (lead = seconds before the voice). */
export function sentsFor(w, lead = 0) {
  const W = WIN[w];
  return SENT.filter((s) => s.t0 >= W.off - 0.01 && s.t1 <= W.off + W.adur + 0.5).map((s) => ({
    ...s,
    t0: r(s.t0 - W.off + lead),
    t1: r(s.t1 - W.off + lead),
  }));
}
export function shotsFor(w, lead = 0) {
  const W = WIN[w];
  const total = W.dur + lead;
  const out = SHOTS.filter((s) => s.t1 > W.off + 0.2 && s.t0 < W.off + W.dur - 0.3).map((s) => ({
    ...s,
    t0: r(Math.max(0, s.t0 - W.off + lead)),
    t1: r(Math.min(total, s.t1 - W.off + lead)),
  }));
  out[0].t0 = 0;
  out.at(-1).t1 = total;
  return out;
}
export const tAt = (w, t, lead = 0) => r(t - WIN[w].off + lead);

// ── Fonts
const FF = (family, file, weight = "400", style = "normal") =>
  `@font-face{font-family:"${family}";src:url("assets/fonts/${file}");font-weight:${weight};font-style:${style};font-display:block;}`;
export const FONTS = {
  serifTa: FF("NK Serif Tamil", "NotoSerifTamil-Regular.ttf", "400") + FF("NK Serif Tamil", "NotoSerifTamil-Bold.ttf", "700"),
  sansTa: FF("NK Sans Tamil", "NotoSansTamil-VF.ttf", "100 900"),
  anek: `@font-face{font-family:"NK Anek Tamil";src:url("assets/fonts/AnekTamil-VF.ttf");font-weight:100 800;font-stretch:75% 125%;font-display:block;}`,
  hind: FF("NK Hind Madurai", "HindMadurai-Medium.ttf", "500") + FF("NK Hind Madurai", "HindMadurai-Bold.ttf", "700"),
  tiro: FF("NK Tiro Tamil", "TiroTamil-Regular.ttf", "400") + FF("NK Tiro Tamil", "TiroTamil-Italic.ttf", "400", "italic"),
  kavi: FF("NK Kavivanar", "Kavivanar-Regular.ttf", "400"),
  corm: FF("NK Cormorant", "CormorantGaramond-VF.ttf", "300 700") + FF("NK Cormorant", "CormorantGaramond-Italic-VF.ttf", "300 700", "italic"),
  oswald: FF("NK Oswald", "Oswald-VF.ttf", "200 700"),
  elite: FF("NK Special Elite", "SpecialElite-Regular2.ttf", "400"),
  plex: FF("NK Plex Mono", "IBMPlexMono-Medium.ttf", "500"),
};

// ── File writers
/** A scene file: everything inside <template>, root styled as #root. */
export function scene({ id, W = 1920, H = 1080, css = "", html = "", js = "" }) {
  return `<template>
  <style>
    #root { position: absolute; inset: 0; overflow: hidden; }
${css}
  </style>
  <div id="root" data-composition-id="${id}" data-width="${W}" data-height="${H}">
${html}
  </div>
  <script>
    (function () {
      const tl = gsap.timeline({ paused: true });
${js}
      window.__timelines["${id}"] = tl;
    })();
  </script>
</template>
`;
}
/** index.html: scene hosts + audio only. hosts: [{id, kind, z, start?, dur?}], audio: [{id, src, start, dur, vol, mstart?}] */
export function index({ title, W = 1920, H = 1080, dur, bg = "#000", hosts, audio = [], lang = "ta" }) {
  const hostTags = hosts
    .map(
      (h, i) => `      <div
        id="${h.id}"
        data-composition-id="${h.id}"
        data-composition-src="compositions/${h.id}.html"
        data-start="${h.start ?? 0}"
        data-duration="${h.dur ?? dur}"
        data-track-index="${i + 1}"
        data-track-kind="${h.kind ?? "graphics"}"
        data-width="${W}"
        data-height="${H}"
        style="z-index: ${h.z ?? i + 1}"
      ></div>`,
    )
    .join("\n");
  const audioTags = audio
    .map(
      (a, i) =>
        `      <audio id="${a.id}" class="clip" src="${a.src}" data-start="${r(a.start)}" data-duration="${r(a.dur)}"${
          a.mstart ? ` data-media-start="${r(a.mstart)}"` : ""
        } data-track-index="${hosts.length + i + 1}" data-volume="${a.vol ?? 1}"></audio>`,
    )
    .join("\n");
  return `<!doctype html>
<html lang="${lang}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=${W}, height=${H}" />
    <title>${title}</title>
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { margin: 0; width: ${W}px; height: ${H}px; overflow: hidden; background: ${bg}; }
      #root { position: relative; width: ${W}px; height: ${H}px; overflow: hidden; background: ${bg}; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="${dur}" data-width="${W}" data-height="${H}">
${hostTags}
${audioTags}
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = gsap.timeline({ paused: true });
    </script>
  </body>
</html>
`;
}
export function writeStyle(slug, name, files) {
  const dir = join(ROOT, "styles", slug);
  mkdirSync(join(dir, "compositions"), { recursive: true });
  for (const f of ["index.html", ...Object.keys(files).filter((k) => k !== "index.html")]) {
    const p = join(dir, f);
    mkdirSync(dirname(p), { recursive: true });
    writeFileSync(p, files[f]);
  }
  writeFileSync(
    join(dir, "hyperframes.json"),
    JSON.stringify(
      {
        $schema: "https://hyperframes.heygen.com/schema/hyperframes.json",
        registry: "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry",
        paths: { blocks: "compositions", components: "compositions/components", assets: "assets" },
        media: { autoProxy: true },
      },
      null,
      2,
    ) + "\n",
  );
  writeFileSync(join(dir, "meta.json"), JSON.stringify({ id: slug, name, createdAt: "2026-11-15T09:00:00.000Z" }, null, 2) + "\n");
  const link = join(dir, "assets");
  if (existsSync(link)) rmSync(link, { recursive: true, force: true });
  symlinkSync("../../shared", link);
  console.log("wrote", slug);
}

// ── Picture builder ─────────────────────────────────────────────────────────
// Each shot is one timed clip: .tr carries the transition, .kb the camera move, img the plate.
// trans(i, shot, prev) → { type: "cut"|"fade"|"wipe"|"iris"|"push"|"zoom", d }
export function buildShots(shots, opt = {}) {
  const {
    pfx = "p",
    W = 1920,
    H = 1080,
    trans = (i, s) => (s.cut ? { type: "cut", d: 0 } : { type: "fade", d: 0.8 }),
    src = (s) => `assets/plates/${s.plate}.jpg`,
    kbEase = "none",
    kbScale = 1, // multiply drift amounts
    z0 = 1,
    track = 1,
  } = opt;
  const tr = shots.map((s, i) => (i === 0 ? { type: "cut", d: 0 } : trans(i, s, shots[i - 1])));
  let html = "";
  let js = "";
  shots.forEach((s, i) => {
    const d = tr[i].d;
    const dn = i + 1 < shots.length ? tr[i + 1].d : 0;
    const start = r(Math.max(0, s.t0 - d / 2));
    const end = r(i + 1 < shots.length ? shots[i + 1].t0 + dn / 2 : s.t1);
    const dur = r(end - start);
    const id = `${pfx}${i + 1}`;
    html += `    <div id="${id}" class="${pfx}-shot clip" data-start="${start}" data-duration="${dur}" data-track-index="${track + (i % 2)}" style="z-index: ${z0 + i}">
      <div id="${id}-tr" class="${pfx}-tr"><div id="${id}-kb" class="${pfx}-kb" style="transform-origin: ${s.o}"><img src="${src(s)}" alt="" /></div></div>
    </div>\n`;
    const A = s.a,
      B = s.b;
    const sc = (v) => r(1 + (v - 1) * (v > 1.3 ? 1 : kbScale));
    js += `      tl.fromTo("#${id}-kb", { scale: ${sc(A[0])}, x: ${r(A[1] * kbScale)}, y: ${r(A[2] * kbScale)} }, { scale: ${sc(B[0])}, x: ${r(B[1] * kbScale)}, y: ${r(B[2] * kbScale)}, duration: ${dur}, ease: "${s.ease ?? kbEase}" }, ${start});\n`;
    const T = tr[i];
    if (T.type === "fade") js += `      tl.fromTo("#${id}-tr", { opacity: 0 }, { opacity: 1, duration: ${d}, ease: "power1.inOut" }, ${start});\n`;
    if (T.type === "wipe") js += `      tl.fromTo("#${id}-tr", { clipPath: "inset(0% 0% 0% 100%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: ${d}, ease: "power3.inOut" }, ${start});\n`;
    if (T.type === "wipeUp") js += `      tl.fromTo("#${id}-tr", { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: ${d}, ease: "power3.inOut" }, ${start});\n`;
    if (T.type === "iris") js += `      tl.fromTo("#${id}-tr", { clipPath: "circle(0% at ${T.at ?? "50% 50%"})" }, { clipPath: "circle(75% at ${T.at ?? "50% 50%"})", duration: ${d}, ease: "power2.inOut" }, ${start});\n`;
    if (T.type === "push") {
      js += `      tl.fromTo("#${id}-tr", { x: ${W} }, { x: 0, duration: ${d}, ease: "power3.inOut" }, ${start});\n`;
      js += `      tl.fromTo("#${pfx}${i}-tr", { x: 0 }, { x: ${-W}, duration: ${d}, ease: "power3.inOut", immediateRender: false }, ${start});\n`;
    }
    if (T.type === "zoomThrough") {
      js += `      tl.fromTo("#${id}-tr", { opacity: 0, scale: 0.72 }, { opacity: 1, scale: 1, duration: ${d}, ease: "power3.out" }, ${start});\n`;
      js += `      tl.to("#${pfx}${i}-tr", { scale: 1.9, filter: "blur(14px)", duration: ${d}, ease: "power3.in" }, ${start});\n`;
    }
    if (T.type === "whip") {
      js += `      tl.fromTo("#${id}-tr", { x: ${W}, filter: "blur(22px)" }, { x: 0, filter: "blur(0px)", duration: ${d}, ease: "power4.inOut" }, ${start});\n`;
      js += `      tl.to("#${pfx}${i}-tr", { x: ${-W}, filter: "blur(22px)", duration: ${d}, ease: "power4.inOut" }, ${start});\n`;
    }
    if (T.type === "blur") {
      js += `      tl.fromTo("#${id}-tr", { opacity: 0, filter: "blur(30px)" }, { opacity: 1, filter: "blur(0px)", duration: ${d}, ease: "power2.inOut" }, ${start});\n`;
      js += `      tl.to("#${pfx}${i}-tr", { filter: "blur(30px)", duration: ${d}, ease: "power2.inOut" }, ${start});\n`;
    }
    if (T.type === "slideUp") js += `      tl.fromTo("#${id}-tr", { yPercent: 100 }, { yPercent: 0, duration: ${d}, ease: "expo.out" }, ${start});\n`;
    if (T.type === "diag") js += `      tl.fromTo("#${id}-tr", { clipPath: "polygon(100% 0%, 100% 0%, 100% 0%, 100% 0%)" }, { clipPath: "polygon(-60% 0%, 100% 0%, 100% 100%, 0% 100%)", duration: ${d}, ease: "power2.inOut" }, ${start});\n`;
    if (T.type === "zoom") {
      js += `      tl.fromTo("#${id}-tr", { opacity: 0, scale: 1.25 }, { opacity: 1, scale: 1, duration: ${d}, ease: "power3.out" }, ${start});\n`;
    }
  });
  const css = `    .${pfx}-shot { position: absolute; left: 0; top: 0; width: ${W}px; height: ${H}px; overflow: hidden; }
    .${pfx}-tr, .${pfx}-kb { position: absolute; inset: 0; }
    .${pfx}-kb img { position: absolute; left: 0; top: 0; width: ${W}px; height: ${H}px; object-fit: cover; }`;
  return { html, js, css, tr };
}

/** Deterministic PRNG for jitter tables written into the files. */
export function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** Split a sentence's words into caption groups of at most `max` words: break at commas first,
 * then into evenly sized groups (7 words at max 5 → 4 + 3, never 5 + 2). */
export function groupsOf(s, max) {
  const ws = wordsOf(s);
  const segs = [];
  let cur = [];
  for (const w of ws) {
    cur.push(w);
    if (/[,]$/.test(w.text)) { segs.push(cur); cur = []; }
  }
  if (cur.length) segs.push(cur);
  const out = [];
  for (const seg of segs) {
    const k = Math.ceil(seg.length / max);
    const size = Math.ceil(seg.length / k);
    for (let i = 0; i < seg.length; i += size) out.push(seg.slice(i, i + size));
  }
  return out;
}
export const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");

// ── Bundled sound effects (skills/media-use, Pixabay licence). peak = seconds into the file where it hits.
const SFX = {
  riser: { dur: 4.3, peak: 3.47 },
  "impact-bass-1": { dur: 2.1, peak: 0.073 },
  "impact-bass-2": { dur: 2.59, peak: 0.03 },
  whoosh: { dur: 0.57, peak: 0.162 },
  "whoosh-short": { dur: 0.57, peak: 0.162 },
  "whoosh-cinematic": { dur: 4.4, peak: 2.5 },
  pop: { dur: 0.7, peak: 0.12 },
  "key-press": { dur: 0.4, peak: 0.076 },
  "click-soft": { dur: 0.36, peak: 0.073 },
};
let sfxN = 0;
/** Place an effect so its peak lands one frame after the picture event at time t. */
export function sfx(name, t, vol = 0.3, total = Infinity) {
  const m = SFX[name];
  let start = t + 1 / 30 - m.peak, mstart = 0;
  if (start < 0) { mstart = -start; start = 0; }
  const dur = Math.min(m.dur - mstart, total - start - 0.02);
  return { id: `fx${++sfxN}-${name}`, src: `assets/sfx/${name}.mp3`, start: r(start), dur: r(dur), vol, mstart: r(mstart) };
}
