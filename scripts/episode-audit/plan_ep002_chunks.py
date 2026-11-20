"""Choose render-chunk boundaries that never land on a chapter change.

The last film hitched at three chapter changes because the chunk boundaries
were 300, 600, 900, 1200, 1500, 1800 and chapters II, III and IV begin at
exactly 300, 600 and 900. The join cut through a transition that was still
running, so the outgoing chunk's last frames were captured half-faded and the
incoming chunk snapped back.

Boundaries are now chosen to satisfy two rules:

  1. never within GUARD seconds of a chapter start
  2. never within GUARD seconds of a chapter card's reveal or exit

and otherwise land as close to the nominal spacing as possible, inside the
quiet part of an ordinary plate.
"""
import json, sys

BLOCK = 30.0
GUARD = 3.0

# chapter start blocks, from the build
CH_START_BLOCK = {1: 1, 2: 11, 3: 21, 4: 31, 5: 42, 6: 52, 7: 62}
# the opening chapter card was re-sequenced to 5.40; every other reveals at 0.35
CH_REVEAL = {1: 5.40}
EXIT_AFTER = 4.05          # card exits this long after its reveal

def forbidden(film_seconds, chapters):
    """Every second that must not contain a seam."""
    bad = []
    for (num, start_block) in chapters:
        t0 = (start_block - 1) * BLOCK
        rev = CH_REVEAL.get(num, 0.35)
        for x in (t0, t0 + rev, t0 + rev + EXIT_AFTER):
            if 0 < x < film_seconds:
                bad.append((x, num, "start" if x == t0 else
                            ("reveal" if x == t0 + rev else "exit")))
    return bad

def plan(film, n_chunks, preroll=3.0):
    chapters = sorted(CH_START_BLOCK.items())
    bad = forbidden(film, chapters)
    nominal = film / n_chunks
    bounds = [0.0]
    for i in range(1, n_chunks):
        target = film * i / n_chunks
        # search outward from the nominal point for a legal second
        chosen = None
        step = 0.5
        for k in range(0, 200):
            for cand in (target - k * step, target + k * step):
                if not (bounds[-1] + 60 < cand < film - 30):
                    continue
                if all(abs(cand - x) > GUARD for x, _, _ in bad):
                    chosen = cand; break
            if chosen is not None:
                break
        bounds.append(chosen if chosen is not None else target)
    bounds.append(film)
    chunks = []
    for i in range(n_chunks):
        a, b = bounds[i], bounds[i + 1]
        chunks.append(dict(name=f"ch{i+1:02d}", start=round(a, 3),
                           end=round(b, 3), preroll=(preroll if i else 0.0)))
    return chunks, bad

if __name__ == "__main__":
    film = 2100.0
    chunks, bad = plan(film, 7)
    print("forbidden seconds (never a seam here):")
    for x, num, why in bad:
        print(f"   {x:7.2f}s  chapter {num} {why}")
    print("\nchunk plan:")
    for c in chunks:
        seg = c["end"] - c["start"]
        print(f"   {c['name']}  {c['start']:7.1f} -> {c['end']:7.1f}  "
              f"{seg:6.1f}s  preroll {c['preroll']:.1f}")
    print("\nseam check:")
    ok = True
    for c in chunks[1:]:
        gap = min(abs(c["start"] - x) for x, _, _ in bad)
        flag = "OK" if gap > GUARD else "*** TOO CLOSE ***"
        if gap <= GUARD: ok = False
        print(f"   seam {c['start']:7.1f}  nearest forbidden {gap:5.1f}s  {flag}")
    json.dump(chunks, open(".cache/ep002_chunk_plan.json", "w"), indent=1)
    sys.exit(0 if ok else 1)
