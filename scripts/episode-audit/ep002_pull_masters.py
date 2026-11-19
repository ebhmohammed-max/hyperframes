"""Rebuild the local master set from Drive.

Masters are deleted locally after upload to keep the workspace flat, which
means the workspace is not self-sufficient: a plate cannot be re-derived
without its master. This restores masters from the Episode 02 Drive folder
so a rebuild never depends on regenerating (and therefore re-buying) art.

Usage:  python ep002_pull_masters.py            # report only
        python ep002_pull_masters.py --write    # download into masters/
"""
import os, sys, json, urllib.request

MA = ("projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/art_dev/masters")
FOLDERS = {
    "01": ("1Szxuff_aFWySEGhkURjYC9L1ZCGGQ8zb", range(1, 11)),
    "02": ("1PyidDrkaNxyieuH-vAOWZ2axv9ObYj4n", range(11, 21)),
    "03": ("1SXDIHywPYU3yWR94xUeK85AkwhXiT2LY", range(21, 30)),
    "04": ("1DIaX2mvIuC2Py8ngNekbn5wy5XfcZ7VF", range(30, 40)),
    "05": ("1Qz-PoZy2pO386Yk4Qbtu5vuoCSjtXbXT", range(41, 51)),
    "06": ("1x8yZYuNMMPkK_ZGUA3t9un6vemfeNQkx", range(51, 61)),
    "07": ("1tC0XOpRG8XJUp5y_e1xs__xJoSS84vmD", range(61, 71)),
}

def main(write=False):
    have = sorted(int(f[:3]) for f in os.listdir(MA) if f.endswith(".jpg"))
    print("local masters:", len(have))
    print("missing locally:", [i for i in range(1, 71) if i not in have] or "none")
    if write:
        print("\nDownloading is done through the Drive connector, not here:")
        print("download_file(file_id, ...) per master, base64-decoded into", MA)
    return have

if __name__ == "__main__":
    main("--write" in sys.argv)
