// Caption builders shared by the styles. All captions are timed clips written into the HTML.
import { r, esc, wordsOf, groupsOf } from "./lib.mjs";

/** One caption per sentence (pairs in `merge` share a caption; the 2nd part arrives on its own word). */
export function capSentences(sents, { pfx = "c", merge = [[7, 8], [16, 17], [21, 22]], skip = [], lead = 0.08, tail = 0.3, cls = "" } = {}) {
  const groups = [];
  for (let i = 0; i < sents.length; i++) {
    const s = sents[i];
    if (skip.includes(s.n)) continue;
    const m = merge.find((p) => p[0] === s.n);
    if (m && sents[i + 1] && sents[i + 1].n === m[1]) groups.push([s, sents[++i]]);
    else groups.push([s]);
  }
  let html = "", js = "";
  groups.forEach((g, gi) => {
    const start = r(Math.max(0.1, g[0].t0 - lead));
    const nextStart = groups[gi + 1] ? groups[gi + 1][0].t0 - lead : Infinity;
    const end = r(Math.min(g.at(-1).t1 + tail, nextStart - 0.05));
    const id = `${pfx}${gi + 1}`;
    html += `    <div id="${id}" class="${pfx}-cap ${cls} clip" data-start="${start}" data-duration="${r(end - start)}" data-track-index="1"><div id="${id}-in" class="${pfx}-in">${g
      .map((s, k) => `<span id="${id}-s${k}" class="${pfx}-s">${esc(s.text)}</span>`)
      .join(" ")}</div></div>\n`;
    js += `      tl.fromTo("#${id}-in", { opacity: 0 }, { opacity: 1, duration: 0.16, ease: "power2.out" }, ${start});\n`;
    g.slice(1).forEach((s, k) => {
      js += `      tl.fromTo("#${id}-s${k + 1}", { opacity: 0 }, { opacity: 1, duration: 0.14, ease: "power2.out" }, ${r(s.t0 - 0.05)});\n`;
    });
    js += `      tl.to("#${id}-in", { opacity: 0, duration: 0.12, ease: "power2.in" }, ${r(end - 0.13)});\n`;
  });
  return { html, js, groups };
}

/** Word-timed caption groups (≤ max words). onWord(id, wordId, w, groupStart) returns the js for one word. */
export function capWords(sents, { pfx = "c", max = 3, skip = [], lead = 0.06, tail = 0.22, inAnim, onWord, exit = 0.1 } = {}) {
  const groups = sents.filter((s) => !skip.includes(s.n)).flatMap((s) => groupsOf(s, max));
  let html = "", js = "";
  groups.forEach((g, gi) => {
    const start = r(Math.max(0.1, g[0].t0 - lead));
    const nextStart = groups[gi + 1] ? groups[gi + 1][0].t0 - lead : Infinity;
    const end = r(Math.min(g.at(-1).t1 + tail, nextStart - 0.02));
    const id = `${pfx}${gi + 1}`;
    html += `    <div id="${id}" class="${pfx}-cap clip" data-start="${start}" data-duration="${r(end - start)}" data-track-index="1"><div id="${id}-in" class="${pfx}-in">${g
      .map((w, k) => `<span id="${id}-w${k}" class="${pfx}-w">${esc(w.text)}</span>`)
      .join(" ")}</div></div>\n`;
    js += inAnim ? inAnim(id, start, g) : `      tl.fromTo("#${id}-in", { opacity: 0 }, { opacity: 1, duration: 0.1, ease: "power2.out" }, ${start});\n`;
    g.forEach((w, k) => {
      if (onWord) js += onWord(id, `${id}-w${k}`, w, start, k, g);
    });
    if (exit) js += `      tl.to("#${id}-in", { opacity: 0, duration: ${exit}, ease: "power2.in" }, ${r(end - exit - 0.01)});\n`;
  });
  return { html, js, groups };
}

/** Film grain: an oversized noise layer stepped to a new offset 12× a second (seeded table). */
export function grain(id, dur, rand, { fps = 12, opacity = 0.16, z = 60, blend = "overlay" } = {}) {
  const N = 24;
  const tbl = Array.from({ length: N }, () => [Math.round(rand() * 240), Math.round(rand() * 240)]);
  return {
    css: `    #${id} { position: absolute; left: -256px; top: -256px; width: 2432px; height: 2432px; background: url("assets/tex/grain.png"); mix-blend-mode: ${blend}; opacity: ${opacity}; z-index: ${z}; pointer-events: none; }`,
    html: `    <div id="${id}" data-layout-ignore></div>\n`,
    js: `      { const G = ${JSON.stringify(tbl)}; for (let f = 0; f < ${Math.ceil(dur * fps)}; f++) tl.set("#${id}", { x: G[f % ${N}][0], y: G[f % ${N}][1] }, f / ${fps}); }\n`,
  };
}
