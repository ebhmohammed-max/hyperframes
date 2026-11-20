// node build.mjs [nn ...]   → regenerates styles/<nn-…>/ from gen/sNN.mjs
import { readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
const here = dirname(fileURLToPath(import.meta.url));
const want = process.argv.slice(2);
for (const f of readdirSync(join(here, "gen")).filter((f) => /^s\d\d\.mjs$/.test(f)).sort()) {
  if (want.length && !want.includes(f.slice(1, 3))) continue;
  (await import(join(here, "gen", f))).default();
}
