// node script/build.mjs → narration/text/Nxx.txt, script/lines.json, SCRIPT_TA.md
import { writeFileSync, mkdirSync } from "node:fs";
import { CLIPS, TAGS, TITLE } from "./script.mjs";
mkdirSync("narration/text", { recursive: true });
const lines = [];
let md = "# EP23 — " + TITLE.join(": ") + "\n\nNarration script (in progress, chapter by chapter). Spoken Tamil. Labels in brackets are the on-screen evidence tags: " +
  Object.values(TAGS).join(" · ") + ". Captions show digits; the voice reads numbers as words. \"அவரே எழுதியது\" marks his own version in Mein Kampf, which is often not confirmed. Sources and doubts: FACT_SHEET.md.\n";
let total = 0;
for (const c of CLIPS) {
  const txt = c.lines.map((l) => l[0]).join(" ");
  writeFileSync(`narration/text/${c.id}.txt`, txt + "\n");
  total += txt.length;
  console.log(c.id, c.slug.padEnd(7), String(c.lines.length).padStart(3), "lines", String(txt.length).padStart(5), "chars", "~" + Math.round(txt.length / 15.5) + "s", txt.length > 1500 ? "  <<< OVER 1500" : "");
  if (c.sec === "HOOK") md += c.id === "N01" ? "\n## HOOK — cold open\n" : "";
  else if (c.title) md += `\n## அத்தியாயம் ${c.sec} — ${c.title}\n`;
  md += `\n_${c.id}_\n\n`;
  c.lines.forEach((l, q) => {
    lines.push({ clip: c.id, slug: c.slug, q, say: l[0], cap: l[2] || l[0], tag: l[1] || "", fx: l[3] || null });
    md += `- ${l[2] || l[0]}${l[1] ? "  [" + TAGS[l[1]] + "]" : ""}\n`;
  });
  if (c.id === "N02") md += "\n## TITLE — title sequence\n\n_No narration. Title: " + TITLE.join(" · ") + "_\n";
}
writeFileSync("script/lines.json", JSON.stringify(lines, null, 1));
writeFileSync("SCRIPT_TA.md", md);
writeFileSync("script/clips.json", JSON.stringify(CLIPS.map((c) => ({ id: c.id, slug: c.slug, sec: c.sec, title: c.title, ch: c.sec === "HOOK" ? 0 : Number(c.sec.split(" ")[0]) })), null, 1));
console.log("total", CLIPS.length, "clips", lines.length, "lines", total, "chars", "~" + (total / 15.5 / 60).toFixed(1) + " min");
