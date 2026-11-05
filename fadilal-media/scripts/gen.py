import json, os, sys, time, urllib.request, concurrent.futures as cf
sys.path.insert(0, os.path.dirname(__file__))
import kie
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(S, "gen"); os.makedirs(OUT, exist_ok=True)
MAN = os.path.join(S, "manifest.jsonl")

def run(spec):
    tid = kie.create(spec["model"], spec["input"])
    print("submitted", spec["name"], tid, flush=True)
    d = kie.wait(tid, timeout=spec.get("timeout", 1800))
    rec = {"name": spec["name"], "model": spec["model"], "taskId": tid, "state": d.get("state"),
           "credits": d.get("creditsConsumed"), "costTime": d.get("costTime"),
           "failMsg": d.get("failMsg"), "input": spec["input"], "files": []}
    if d.get("state") == "success":
        urls = json.loads(d["resultJson"]).get("resultUrls", [])
        for i, u in enumerate(urls):
            ext = os.path.splitext(u.split("?")[0])[1] or ".bin"
            fn = os.path.join(OUT, spec["name"] + (f"_{i}" if i else "") + ext)
            urllib.request.urlretrieve(u, fn)
            rec["files"].append({"path": fn, "url": u})
    with open(MAN, "a") as f: f.write(json.dumps(rec) + "\n")
    print("done", spec["name"], rec["state"], rec["credits"], rec["failMsg"] or "", flush=True)
    return rec

if __name__ == "__main__":
    specs = json.load(open(sys.argv[1]))
    with cf.ThreadPoolExecutor(int(sys.argv[2]) if len(sys.argv) > 2 else 6) as ex:
        list(ex.map(run, specs))
