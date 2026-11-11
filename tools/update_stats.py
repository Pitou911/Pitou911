"""Builds assets/px-telemetry.svg from the GitHub GraphQL API.
Usage:  GH_TOKEN=... GH_USER=Pitou911 python tools/update_stats.py   (or --demo for a pending placeholder)"""
import os,sys,json,datetime as dt,urllib.request
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
ROOT=os.path.dirname(HERE)
from pixel import *
USER=os.environ.get("GH_USER","Pitou911")
def gql(q,v):
    req=urllib.request.Request("https://api.github.com/graphql",json.dumps({"query":q,"variables":v}).encode(),
        {"Authorization":"bearer "+os.environ["GH_TOKEN"],"Content-Type":"application/json","User-Agent":"pixel-telemetry"})
    with urllib.request.urlopen(req,timeout=60) as r: d=json.load(r)
    if "errors" in d: raise SystemExit(json.dumps(d["errors"]))
    return d["data"]
def fetch():
    now=dt.datetime.now(dt.timezone.utc)
    u=gql('''query($u:String!){user(login:$u){createdAt followers{totalCount}
      repositories(ownerAffiliations:OWNER,isFork:false,privacy:PUBLIC,first:100){totalCount nodes{stargazerCount
      languages(first:8,orderBy:{field:SIZE,direction:DESC}){edges{size node{name}}}}}}}''',{"u":USER})["user"]
    days={}
    for y in range(int(u["createdAt"][:4]),now.year+1):
        f=f"{y}-01-01T00:00:00Z"
        t=min(now,dt.datetime(y,12,31,23,59,59,tzinfo=dt.timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ")
        d=gql('''query($u:String!,$f:DateTime!,$t:DateTime!){user(login:$u){contributionsCollection(from:$f,to:$t){
          contributionCalendar{weeks{contributionDays{date contributionCount}}}}}}''',{"u":USER,"f":f,"t":t})
        for w in d["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]:
            for x in w["contributionDays"]:
                days[x["date"]]=max(days.get(x["date"],0),x["contributionCount"])
    langs={}
    for r in u["repositories"]["nodes"]:
        for e in r["languages"]["edges"]: langs[e["node"]["name"]]=langs.get(e["node"]["name"],0)+e["size"]
    tot=sum(langs.values()) or 1
    top=sorted(langs.items(),key=lambda kv:-kv[1])[:5]
    return dict(days=days,langs=[(n,round(100*s/tot)) for n,s in top],repos=u["repositories"]["totalCount"],
        stars=sum(r["stargazerCount"] for r in u["repositories"]["nodes"]),followers=u["followers"]["totalCount"],
        since=u["createdAt"][:4])
def streaks(days,today):
    ds=sorted(d for d in days if d<=today.isoformat()); best=run=0; prev=None
    for d in ds:
        dd=dt.date.fromisoformat(d)
        run=run+1 if days[d]>0 and prev and (dd-prev).days==1 and run>0 else (1 if days[d]>0 else 0)
        best=max(best,run); prev=dd
    cur=0; d=today
    if days.get(d.isoformat(),0)==0: d-=dt.timedelta(days=1)
    while days.get(d.isoformat(),0)>0: cur+=1; d-=dt.timedelta(days=1)
    return cur,best
def render(m,pending=False):
    W,H=840,300; today=dt.date.today(); b=[]
    b+=frame(W,H)
    days=m["days"]; total=m.get("total",sum(days.values())); cur,best=m["streak"] if "streak" in m else streaks(days,today)
    tiles=[("CONTRIBUTIONS",f"{total:,}",f"SINCE {m['since']}"),("CURRENT STREAK",str(cur),"DAYS"),
           ("LONGEST STREAK",str(best),"DAYS"),("PUBLIC REPOS",str(m["repos"]),f"{m['stars']} STARS")]
    for i,(k,v,u) in enumerate(tiles):
        x=28+i*198; y=26
        b+=[R(x,y,190,84,"#555"),R(x+2,y+2,186,80,"#000")]
        b+=text(k,x+12,y+10,2,"#888"); b+=text(safe(v),x+12,y+28,4,"#fff"); b+=text(safe(u),x+12,y+64,2,"#555")
    b+=text("LAST 30 WEEKS",28,128,2,"#888"); b+=text("TOP LANGUAGES",510,128,2,"#888")
    wk0=today-dt.timedelta(days=(today.weekday()+1)%7)-dt.timedelta(weeks=29)
    nz=sorted(v for v in days.values() if v>0)
    q=[nz[len(nz)*k//4] for k in (1,2,3)] if nz else [1,2,3]
    for c in range(30):
        for r in range(7):
            d=wk0+dt.timedelta(days=7*c+r)
            if d>today: continue
            v=days.get(d.isoformat(),0)
            lvl=0 if v==0 else 1+sum(v>=t for t in q)
            b.append(R(28+c*15,152+r*15,12,12,["#1c1c1c","#444","#888","#ccc","#fff"][min(lvl,4)]))
    if pending or not m.get("langs"):
        b+=ctext("AWAITING FIRST SYNC",660,176,2,"#888"); b+=ctext("RUN THE WORKFLOW",660,200,2,"#555")
    else:
        for i,(n,p) in enumerate(m["langs"]):
            y=156+i*22; b+=text(safe(n)[:10],510,y,2,"#fff")
            fill=max(1,round(p/10)) if p>0 else 0
            for s in range(10): b.append(R(640+s*12,y,10,12,"#fff" if s<fill else "#222"))
            b+=text(f"{p}%",766,y,2,"#888")
    b+=text(f"FOLLOWERS {m['followers']}" if not pending else "STATS FROM GITHUB",28,272,2,"#888")
    stamp="SYNC PENDING" if pending else f"UPDATED {today.isoformat()}"
    b+=text(stamp,W-28-tw(stamp,2)-20,272,2,"#555"); b.append(brect(W-28-10,272,10,12,"#fff","1.2s"))
    return page("TELEMETRY","telemetry",b,H,"GitHub telemetry: contributions, streaks, repositories, last 30 weeks of activity and top languages.")
if __name__=="__main__":
    out=os.path.join(ROOT,"assets","px-telemetry.svg")
    if "--demo" in sys.argv:
        m=dict(days={},langs=[],repos=0,stars=0,followers=0,since="2020",total=2924,streak=(2,21))
        m["repos"]="-"; m["stars"]="-"; open(out,"w").write(render(m,pending=True))
    else: open(out,"w").write(render(fetch()))
    print("wrote",out)
