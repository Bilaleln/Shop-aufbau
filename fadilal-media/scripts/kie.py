import json, os, sys, time, urllib.request
BASE = "https://api.kie.ai"
KEY = os.environ["KIE_API_KEY"]
H = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}

def req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(BASE + path, data=data, headers=H, method=method)
    with urllib.request.urlopen(r, timeout=120) as resp:
        return json.loads(resp.read())

def credits():
    return req("GET", "/api/v1/chat/credit")

def create(model, inp):
    res = req("POST", "/api/v1/jobs/createTask", {"model": model, "input": inp})
    if res.get("code") != 200:
        raise RuntimeError(json.dumps(res))
    return res["data"]["taskId"]

def info(tid):
    return req("GET", f"/api/v1/jobs/recordInfo?taskId={tid}")["data"]

def wait(tid, timeout=1800, every=10):
    t0 = time.time()
    while time.time() - t0 < timeout:
        d = info(tid)
        if d.get("state") in ("success", "fail"):
            return d
        time.sleep(every)
    raise TimeoutError(tid)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "credits":
        print(json.dumps(credits()))
    elif cmd == "info":
        print(json.dumps(info(sys.argv[2]), indent=1))
