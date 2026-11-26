#!/usr/bin/env python3
"""Clips of one chapter in film order.  python3 tools/chclips.py <chapter>   (0 = hook + TITLE; 12 ends with END)"""
import json, sys
k = int(sys.argv[1]); ids = [c["id"] for c in json.load(open("script/clips.json")) if c["ch"] == k]
print(" ".join(ids + (["TITLE"] if k == 0 else ["END"] if k == 12 else [])))
