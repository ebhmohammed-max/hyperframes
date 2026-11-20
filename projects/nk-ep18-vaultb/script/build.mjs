// node script/build.mjs → narration/text/Nxx.txt, script/lines.json, SCRIPT_TA.md
import { writeFileSync, mkdirSync } from "node:fs";
import { CLIPS, TAGS } from "./script.mjs";
mkdirSync("narration/text", { recursive: true });
const lines = [];
let md = "# EP18 — பத்மநாபசுவாமி கோயில்: திறக்காத கதவு (B நிலவறை)\n\nNarration script v2 (20 Nov 2026). Spoken Tamil. Labels in brackets are the on-screen source tags: " +
  Object.values(TAGS).join(" · ") + ". Captions show digits and the vault letters A to F; the voice reads numbers as words.\n";
let total = 0;
for (const c of CLIPS) {
  const txt = c.lines.map((l) => l[0]).join(" ");
  writeFileSync(`narration/text/${c.id}.txt`, txt + "\n");
  total += txt.length;
  console.log(c.id, c.slug.padEnd(9), String(c.lines.length).padStart(3), "lines", String(txt.length).padStart(5), "chars", txt.length > 1500 ? "  <<< OVER 1500" : "");
  md += `\n## ${c.sec === "HOOK" ? "HOOK — cold open and promise" : c.sec + " — " + c.title}  (${c.id})\n\n`;
  c.lines.forEach((l, q) => {
    lines.push({ clip: c.id, slug: c.slug, q, say: l[0], cap: l[2] || l[0], tag: l[1] || "", fx: l[3] || null });
    md += `- ${l[2] || l[0]}${l[1] ? "  [" + TAGS[l[1]] + "]" : ""}\n`;
  });
  if (c.id === "N01") md += "\n## TITLE — title sequence\n\n_No narration. Title: B நிலவறை · திறக்காத கதவு_\n";
}
md += "\n## End card (N08)\n\n_Same channel end card as EP10 to EP17 (like, comment, subscribe, bell)._\n";
writeFileSync("script/lines.json", JSON.stringify(lines, null, 1));
writeFileSync("SCRIPT_TA.md", md);
console.log("total", lines.length, "lines", total, "chars");
