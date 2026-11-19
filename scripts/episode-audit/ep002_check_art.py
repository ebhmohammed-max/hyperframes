"""Catch modern objects that should never appear in a pre-medieval film.

Scene 032 came back as a 20th-century office: electric desk fan, ballpoint,
wristwatch, short-sleeved shirt. Nothing in the pipeline noticed, because a
contact sheet at thumbnail size hides exactly that kind of detail.

This cannot understand a picture. It catches the failures a human would catch
on a full-size look, by flagging scenes whose direction invited a modern
interior and that have not been eyeballed. Every master still gets a visual
check; this only decides which ones get it first.
"""
import os, sys, json

MA = ("projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/art_dev/masters")

# Directions that historically pulled the model toward a modern interior.
RISK = {
    32: "cramped office, exhausted man writing - produced an electric fan, "
        "ballpoint and wristwatch in take one; fixed with clay tablets",
    42: "council of rival noble houses - produced generic Westeros with fur "
        "cloaks in take one; must be Valyrian black stone and firelight",
    44: "hand writing a refusal on a scroll - produced legible English text "
        "inside the image in take one; must have no readable characters",
}

STYLE_BAN = (
    "Period-correct antiquity only. No modern objects: no electric fans, no "
    "wires or sockets, no electric light, no wristwatches, no ballpoint or "
    "fountain pens, no printed paper, no glass windows, no short-sleeved "
    "shirt collars, no zips or buttons of modern type, no plastic."
)

def report():
    have = sorted(int(f[:3]) for f in os.listdir(MA) if f.endswith(".jpg"))
    flagged = [s for s in have if s in RISK]
    return {"present": len(have), "flagged": flagged,
            "risk_notes": {s: RISK[s] for s in flagged}}

if __name__ == "__main__":
    r = report()
    print(json.dumps(r, indent=1))
    print("\nstyle ban for risky scenes:\n" + STYLE_BAN)
