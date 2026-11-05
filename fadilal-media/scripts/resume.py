import json,os,sys,urllib.request,concurrent.futures as cf
sys.path.insert(0,os.path.dirname(__file__)); import kie
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
specs={s['name']:s for s in json.load(open(sys.argv[1]))}
pairs=[a.split('=') for a in sys.argv[2:]]
def go(p):
    name,tid=p; d=kie.wait(tid,timeout=3600); spec=specs[name]
    rec={"name":name,"model":spec["model"],"taskId":tid,"state":d.get("state"),"credits":d.get("creditsConsumed"),"costTime":d.get("costTime"),"failMsg":d.get("failMsg"),"input":spec["input"],"files":[]}
    if d.get("state")=="success":
        for u in json.loads(d["resultJson"]).get("resultUrls",[]):
            fn=os.path.join(S,"gen",name+os.path.splitext(u.split("?")[0])[1]); urllib.request.urlretrieve(u,fn); rec["files"].append({"path":fn,"url":u})
    open(os.path.join(S,"manifest.jsonl"),"a").write(json.dumps(rec)+"\n"); print("done",name,rec["state"],rec["credits"],rec["failMsg"] or "",flush=True)
with cf.ThreadPoolExecutor(8) as ex: list(ex.map(go,pairs))
