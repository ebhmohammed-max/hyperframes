#!/usr/bin/env python3
"""Print the next pictures still to be made (default 10): number and full prompt."""
import json, os, sys
n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
later = {int(l.split("|")[0]) for l in open("shots/redo.txt", encoding="utf8") if l[:1].isdigit()} if os.path.exists("shots/redo.txt") else set()
todo = [r for r in json.load(open("shots/prompts.json", encoding="utf8")) if not os.path.exists(f"out/raw/{r['n']:03d}.jpg") and r["n"] not in later]
print("held for the redo pass:", sorted(later))
print(len(todo), "left")
for r in todo[:n]: print(f"{r['n']:03d} [{','.join(r.get('refs', []))}] images={r.get('images', [])}\n{r['prompt']}\n")
