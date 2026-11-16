#!/usr/bin/env python3
"""Print the next pictures still to be made (default 10): number and full prompt."""
import json, os, sys
n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
todo = [r for r in json.load(open("shots/prompts.json", encoding="utf8")) if not os.path.exists(f"out/raw/{r['n']:03d}.jpg")]
print(len(todo), "left")
for r in todo[:n]: print(f"{r['n']:03d} [{','.join(r.get('refs', []))}] {r['prompt']}\n")
