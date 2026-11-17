// 06 — Archive board (case file): the plates are photo prints pinned on a dark board. One camera
// travels print to print on the narration, new evidence drops in as it is named, a red thread
// links the finds, a rubber stamp lands on "உலோகம்", captions sit on a typed label strip.
import { r, index, scene, writeStyle, shotsFor, sentsFor, WIN, FONTS, HIT, sfx, tAt, rng } from "./lib.mjs";
import { capSentences } from "./caps.mjs";

export default function build() {
  const w = "b", D = WIN[w].dur;
  const shots = shotsFor(w), sents = sentsFor(w);
  const hit = tAt(w, HIT);
  const PW = 1120, PH = 630, B = 26, LBL = 118; // print size, border, label strip
  // world layout (px); rot in degrees
  const prints = {
    sh005: { x: 300, y: 260, rot: -2.2, no: "01", la: "THE DIG", ta: "தோண்டும் இடம்" },
    sh001: { x: 1760, y: 180, rot: 1.6, no: "02", la: "BLACK SOIL", ta: "மண்" },
    sh002: { x: 3180, y: 300, rot: -1.2, no: "03", la: "THE TOOL", ta: "கருவி" },
    sh008: { x: 2900, y: 1420, rot: 2.4, no: "04", la: "METAL", ta: "உலோகம்" },
    sh007: { x: 1480, y: 1500, rot: -1.8, no: "05", la: "THE FINDS", ta: "புதையல்?" },
    sh004: { x: 120, y: 1380, rot: 1.4, no: "06", la: "THE FACE", ta: "தெய்வம்?" },
  };
  const WW = 4600, WH = 2500;
  const order = ["sh005", "sh001", "sh002", "sh008", "sh007", "sh004"];
  const cx = (p) => p.x + (PW + 2 * B) / 2, cy = (p) => p.y + (PH + 2 * B + LBL) / 2 - 30;
  // first shot on each print = wide; later shots on the same print punch in on the picture
  const seen = {};
  const cams = shots.map((s) => {
    const p = prints[s.plate];
    const n = (seen[s.plate] = (seen[s.plate] ?? 0) + 1);
    const tight = s.a[0] > 1.3;
    const sc = tight ? 1.5 + (s.a[0] - 1.3) * 0.9 : n > 1 ? 0.96 : 0.9;
    const [ox, oy] = s.o.split(" ").map((v) => parseFloat(v) / 100);
    const fx = tight ? p.x + B + PW * (0.5 + (ox - 0.5) * 0.55) : cx(p);
    const fy = tight ? Math.min(p.y + B + PH * (0.5 + (oy - 0.5) * 0.55), p.y + B + PH + 14 - 610 / sc) : cy(p);
    return { s, p, sc, fx, fy, sy: tight ? 520 : 462, rot: tight ? -p.rot * 0.6 : -p.rot * 0.35 };
  });
  const st = (c, k = 1) => `{ x: ${r(960 - c.fx * c.sc * k)}, y: ${r(c.sy - c.fy * c.sc * k)}, scale: ${r(c.sc * k)}, rotation: ${r(c.rot)} }`;
  let js = `      tl.set("#b-world", ${st(cams[0], 0.94)}, 0);\n`;
  let prevEnd = 0;
  cams.forEach((c, i) => {
    const same = i > 0 && cams[i - 1].s.plate === c.s.plate;
    const d = i === 0 ? 0 : same ? 0.34 : 0.9;
    const arrive = i === 0 ? 0 : r(c.s.t0 + (same ? 0.1 : 0.2));
    const leave = i + 1 < cams.length ? r(cams[i + 1].s.t0 + (cams[i + 1].s.plate === c.s.plate ? 0.1 : 0.2) - (cams[i + 1].s.plate === c.s.plate ? 0.34 : 0.9)) : D;
    if (i > 0) js += `      tl.to("#b-world", { ...${st(c)}, duration: ${d}, ease: "${same ? "power3.out" : "power3.inOut"}" }, ${r(arrive - d)});\n`;
    const hold = r(leave - arrive);
    if (hold > 0.15) js += `      tl.to("#b-world", { ...${st(c, 1.035)}, duration: ${hold}, ease: "none" }, ${arrive});\n`;
    prevEnd = leave;
  });
  // prints drop in the first time the camera heads for them
  const first = {};
  cams.forEach((c) => { if (first[c.s.plate] === undefined) first[c.s.plate] = c.s.t0; });
  let html = "";
  order.forEach((k, i) => {
    const p = prints[k];
    html += `      <div id="b-pr${i}" class="b-print" style="left:${p.x}px;top:${p.y}px;transform:rotate(${p.rot}deg)">
        <div id="b-pr${i}-in" class="b-print-in">
          <img class="b-ph" src="assets/plates/${k}.jpg" alt="" />
          <div class="b-lbl"><span class="b-no">No. ${p.no}</span><span class="b-la">${p.la}</span><span class="b-ta">${p.ta}</span></div>
          <div class="b-pin" data-layout-ignore></div>
        </div>
      </div>\n`;
    if (i > 0) {
      const t = r(first[k] - 0.62);
      js += `      tl.fromTo("#b-pr${i}-in", { opacity: 0, scale: 1.22, rotation: ${i % 2 ? 5 : -5} }, { opacity: 1, scale: 1, rotation: 0, duration: 0.42, ease: "power3.in" }, ${t});\n`;
    }
  });
  // red thread from pin to pin
  const pin = (p) => { const a = (p.rot * Math.PI) / 180, hx = (PW + 2 * B) / 2, hy = (PH + 2 * B + LBL) / 2, dy = 14 - hy; return [r(p.x + hx - dy * Math.sin(a)), r(p.y + hy + dy * Math.cos(a))]; };
  let threads = "";
  order.slice(1).forEach((k, i) => {
    const [x1, y1] = pin(prints[order[i]]), [x2, y2] = pin(prints[k]);
    const len = Math.ceil(Math.hypot(x2 - x1, y2 - y1));
    const sag = 60;
    threads += `<path id="b-th${i}" d="M${x1},${y1} Q${r((x1 + x2) / 2)},${r((y1 + y2) / 2 + sag)} ${x2},${y2}" fill="none" stroke="#b3261a" stroke-width="5" stroke-linecap="round" stroke-dasharray="${len + 80}" stroke-dashoffset="${len + 80}" />`;
    js += `      tl.fromTo("#b-th${i}", { strokeDashoffset: ${len + 80} }, { strokeDashoffset: 0, duration: 0.8, ease: "power2.inOut" }, ${r(first[k] - 0.6)});\n`;
  });
  const sMetal = sents.find((s) => s.text.startsWith("உலோகம்"));
  const p8 = prints.sh008;
  js += `      tl.fromTo("#b-stamp", { opacity: 0, scale: 2.6 }, { opacity: 0.92, scale: 1, duration: 0.16, ease: "power4.in" }, ${r(sMetal.t0 - 0.02)});\n`;
  js += `      tl.fromTo("#b-ring", { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }, ${r(hit)});\n`;
  const p2 = prints.sh002;

  const C = capSentences(sents, { merge: [] });
  const board = scene({
    id: "board",
    css: `    ${FONTS.elite}
    ${FONTS.kavi}
    ${FONTS.hind}
    #b-bg { position: absolute; left: 0; top: 0; width: 1920px; height: 1080px; }
    #b-world { position: absolute; left: 0; top: 0; width: ${WW}px; height: ${WH}px; transform-origin: 0 0; }
    #b-felt { position: absolute; left: -1400px; top: -1000px; width: ${WW + 2800}px; height: ${WH + 2000}px; background: url("assets/tex/board.jpg"); background-size: 1920px 1080px; }
    .b-print { position: absolute; width: ${PW + 2 * B}px; height: ${PH + 2 * B + LBL}px; }
    .b-print-in { position: absolute; inset: 0; background: #f1ead8; box-shadow: 0 2px 3px rgba(0,0,0,0.5), 0 22px 44px rgba(0,0,0,0.55); }
    .b-ph { position: absolute; left: ${B}px; top: ${B}px; width: ${PW}px; height: ${PH}px; object-fit: cover; }
    .b-lbl { position: absolute; left: ${B}px; top: ${PH + B + 14}px; width: ${PW}px; height: ${LBL - 4}px; display: flex; align-items: center; gap: 26px; white-space: nowrap; }
    .b-no { font: 400 40px/1 "NK Special Elite", monospace; color: #8f2a1b; padding-top: 8px; }
    .b-la { font: 400 40px/1 "NK Special Elite", monospace; letter-spacing: 0.06em; color: #2b241a; padding-top: 8px; }
    .b-ta { margin-left: auto; font: 400 62px/1.4 "NK Kavivanar", cursive; color: #1d2c5a; }
    .b-pin { position: absolute; left: ${(PW + 2 * B) / 2 - 15}px; top: -1px; width: 30px; height: 30px; border-radius: 50%; background: radial-gradient(circle at 36% 32%, #ff8a7a 0%, #c0271a 46%, #6d120b 100%); box-shadow: 0 6px 8px rgba(0,0,0,0.5); }
    #b-threads { position: absolute; left: 0; top: 0; width: ${WW}px; height: ${WH}px; overflow: visible; filter: drop-shadow(0 6px 5px rgba(0,0,0,0.5)); }
    #b-stamp { position: absolute; left: ${p8.x + 250}px; top: ${p8.y + 220}px; width: 680px; height: 230px; transform: rotate(-9deg); display: flex; align-items: center; justify-content: center; border: 12px solid #b3261a; border-radius: 18px; font: 700 150px/1.3 "NK Hind Madurai", sans-serif; color: #b3261a; mix-blend-mode: normal; background: rgba(241,234,216,0.12); }
    #b-ring { position: absolute; left: ${p2.x + B + PW * 0.48 - 170}px; top: ${p2.y + B + PH * 0.6 - 150}px; width: 340px; height: 300px; border: 8px solid #b3261a; border-radius: 50%; transform: rotate(-12deg); }
    #b-vig { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 46%, rgba(0,0,0,0) 46%, rgba(0,0,0,0.62) 100%); }
    #b-file { position: absolute; left: 70px; top: 56px; display: flex; align-items: center; gap: 20px; padding: 12px 24px 6px; background: #e9dfc6; box-shadow: 0 6px 16px rgba(0,0,0,0.5); font: 400 34px/1.3 "NK Special Elite", monospace; letter-spacing: 0.05em; color: #2b241a; white-space: nowrap; }
    #b-file b { font-weight: 400; color: #a63a28; }
    .c-cap { position: absolute; left: 160px; width: 1600px; bottom: 76px; text-align: center; }
    .c-in { display: inline-block; max-width: 1500px; padding: 12px 34px 12px; background: #ece3cc; box-shadow: 0 8px 20px rgba(0,0,0,0.55); font: 500 46px/1.42 "NK Hind Madurai", sans-serif; color: #1c1710; }`,
    html: `    <div id="b-world">
      <div id="b-felt" data-layout-ignore></div>
      <svg id="b-threads" viewBox="0 0 ${WW} ${WH}" data-layout-ignore>${threads}</svg>
${html}      <div id="b-ring" data-layout-ignore></div>
      <div id="b-stamp" data-layout-ignore>உலோகம்</div>
    </div>
    <div id="b-vig" data-layout-ignore></div>
    <div id="b-file"><b>FILE 06</b><span>NAGAPATTINAM · 1856</span></div>
${C.html}`,
    js: js + C.js,
  });

  writeStyle("06-archive-board", "NK 06 Archive board", {
    "index.html": index({
      title: "NK style 06 — Archive board", dur: D, bg: "#14110d",
      hosts: [{ id: "board", kind: "captions" }],
      audio: [
        { id: "vo", src: WIN[w].audio, start: 0, dur: WIN[w].adur, vol: 1 },
        ...order.slice(1).map((k, i) => sfx(i % 2 ? "pop" : "click-soft", first[k] - 0.2, 0.34)),
        sfx("whoosh", first.sh001 - 0.45, 0.18),
        sfx("whoosh", first.sh008 - 0.45, 0.18),
        sfx("impact-bass-1", sMetal.t0 + 0.14, 0.42),
        sfx("key-press", hit + 0.02, 0.4),
      ],
    }),
    "compositions/board.html": board,
  });
}
