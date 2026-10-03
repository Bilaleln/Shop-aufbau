"""Download first image / video preview for given ad ids from raw/*.jsonl. Usage: python3 thumbs.py id1 id2 ..."""
import json, glob, os, sys, subprocess
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
idx = {}
for f in glob.glob(D + "/raw/*.jsonl") + glob.glob(D + "/scrapers/samples/meta*.jsonl"):
    for l in open(f):
        r = json.loads(l)
        if r.get("ad_archive_id"): idx.setdefault(r["ad_archive_id"], r)
for i in sys.argv[1:]:
    r = idx.get(i)
    if not r: print(i, "not found"); continue
    u = ((r.get("image_urls") or []) + (r.get("video_preview_urls") or []) or [None])[0]
    if not u: print(i, "no thumb url"); continue
    out = f"{D}/thumbs/{i}.jpg"
    rc = subprocess.run(["curl", "-sS", "-L", "-o", out, u], capture_output=True)
    print(i, rc.returncode, os.path.getsize(out) if os.path.exists(out) else 0)
