"""Regenerates every pixel SVG in assets/. Run from anywhere: python tools/generate_assets.py
(assets/px-telemetry.svg is produced by update_stats.py)"""
import os,sys,random
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
os.chdir(os.path.dirname(HERE))
from pixel import *
W=840
def out(name,s): open(f"assets/{name}.svg","w").write(s)

# ---- header-only strips (sections whose body is plain markdown)
for slug,title in [("status","STATUS BOARD"),("runbook","RUNBOOK"),("channels","OPEN CHANNELS")]:
    out(f"px-{slug}",svg(W,45,header(title,slug),title.title()))

# ---- player card
H=216; b=frame(W,H)
mon=["################","#..............#","#.############.#","#.#..........#.#","#.#.#........#.#","#.#..#.......#.#",
     "#.#...#......#.#","#.#..#..####.#.#","#.#.#........#.#","#.#..........#.#","#.############.#","#..............#",
     "################",".....######.....","...##########..."]
b+=bitmap(mon,36,42,9,"#fff"); b.append(brect(36+7*9,42+7*9,36,9,"#000","1.2s"))
x=212; s=2
b+=text("PLAYER 1",x,30,s,"#888")
st="OPERATIONAL"; b.append(brect(W-34-tw(st,s)-20,30,10,12,"#fff","1.2s")); b+=text(st,W-34-tw(st,s),30,s,"#888")
b+=text("PITOU911",x,50,4); b+=text("LV",x+tw("PITOU911",4)+24,64,s,"#888"); b+=text("B.SC",x+tw("PITOU911",4)+66,64,s)
for i,(k,v) in enumerate([("CLASS","SOLO IT UNIT + CO-FOUNDER / CTO"),("GUILD","KHMERROOMS * MEF GOV SECURITIES"),
                          ("BASE","PHNOM PENH, CAMBODIA"),("TONGUES","KM * EN * HU * FR")]):
    y=94+i*22; b+=text(k,x,y,s,"#888"); b+=text(v,x+102,y,s)
y=186; b+=text("HP",x,y,s,"#888")
for i in range(5):
    h=bitmap(F['$'].split('|'),x+36+i*16,y,2,"#fff")
    if i==4: h=[r[:-2]+blink("1.6s") for r in h]
    b+=h
bx=x+150; b+=text("BOSS",bx,y,s,"#888"); b+=text("ABA PAYWAY",bx+60,y,s)
px=bx+60+tw("ABA PAYWAY",s)+14; b+=[R(px,y,146,14,"#fff"),R(px+2,y+2,142,10,"#000")]
for i in range(10):
    if i<7: b.append(R(px+4+i*14,y+4,12,6,"#fff"))
    elif i==7: b.append(brect(px+4+i*14,y+4,12,6,"#888","0.8s"))
b+=text("70",px+154,y,s,"#888")
out("px-player-card",svg(W,H,b,"Player 1: Pitou911. Solo IT unit and co-founder/CTO. Base: Phnom Penh. Boss fight: ABA PayWay, in progress."))

# ---- architecture (header + diagram in one svg)
H=472; b=frame(W,H); d=[]
def box(x,y,w,h,lines,big=False):
    o=[R(x,y,w,h,"#fff"),R(x+3,y+3,w-6,h-6,"#000")]
    hs=[(21 if (big and i==0) else 14) for i in range(len(lines))]; gap=6 if big else 4
    cy=y+(h-(sum(hs)+gap*(len(lines)-1)))//2
    for i,l in enumerate(lines):
        o+=ctext(l,x+w//2,cy,3 if (big and i==0) else 2,"#fff" if i==0 else "#888"); cy+=hs[i]+gap
    return o
vl=lambda x,y1,y2: R(x-2,y1,4,y2-y1,"#888"); hl=lambda y,x1,x2: R(x1,y-2,x2-x1,4,"#888")
d+=box(120,16,250,64,["IOS / ANDROID","REACT NATIVE"])+box(470,16,250,64,["WEB","NEXT.JS"])
d+=[vl(245,80,112),vl(595,80,112),hl(112,243,597),vl(420,112,150)]+text("HTTPS - SANCTUM",434,124,2,"#888")
d+=box(260,150,320,96,["LARAVEL 12","BOOKINGS - ROOMS","RATES - AVAILABILITY"],big=True)
cxs=[110,316,522,728]; d+=[vl(420,246,272),hl(272,cxs[0]-2,cxs[-1]+2)]
for cx,l in zip(cxs,[["MYSQL","DATABASE"],["ABA PAYWAY","KHQR - HMAC"],["TELEGRAM","OPS BOT"],["CHANNEL","MANAGER"]]):
    d+=[vl(cx,272,300)]+box(cx-88,300,176,62,l)
d+=[vl(316,362,388),R(186,388,260,56,"#fff"),R(189,391,254,50,"#000")]+text("BOSS FIGHT",202,396,2)
for i in range(10):
    xx=202+i*22
    d.append(R(xx,418,18,12,"#fff") if i<7 else (brect(xx,418,18,12,"#888","0.8s") if i==7 else R(xx,418,18,12,"#222")))
d+=text("IN PROGRESS",462,408,2,"#888")
b+=['<g transform="translate(0,8)">']+d+['</g>']
out("px-architecture",page("ARCHITECTURE - KHMERROOMS","architecture",b,H,
 "KhmerRooms architecture: iOS/Android (React Native) and Web (Next.js) call a Laravel 12 API over HTTPS with Sanctum. Laravel talks to MySQL, ABA PayWay (KHQR, HMAC), a Telegram ops bot and a channel manager. ABA PayWay is the current boss fight, in progress."))

# ---- arsenal (header + pixel tech chips in one svg)
groups=[("BACKEND",["LARAVEL","PHP","SPRING BOOT","JAVA","NODE.JS"]),
        ("FRONTEND",["NEXT.JS","REACT","REACT NATIVE","TAILWIND","JAVASCRIPT","TYPESCRIPT"]),
        ("DATA",["MYSQL","POSTGRES","MONGODB"]),("TOOLS",["GIT","GITHUB","DOCKER","FIGMA","VS CODE"])]
hot={"LARAVEL","NEXT.JS","REACT NATIVE","MYSQL"}; d=[]; y=30; X0=150
for g,items in groups:
    d+=text(g,32,y+7,2,"#888"); x=X0
    for it in items:
        w=tw(it,2)+24
        if x+w>W-30: x=X0; y+=38
        if it in hot: d+=[R(x,y,w,28,"#fff")]+text(it,x+12,y+7,2,"#000")
        else: d+=[R(x,y,w,28,"#555"),R(x+2,y+2,w-4,24,"#000")]+text(it,x+12,y+7,2,"#fff")
        x+=w+10
    y+=38+14
d+=[R(32,y+2,28,16,"#fff")]+text("DAILY DRIVER",72,y+4,2,"#888")
H=y+44; b=frame(W,H)+['<g transform="translate(0,0)">']+d+['</g>']
out("px-arsenal",page("ARSENAL","arsenal",b,H,"Tech stack: Laravel, PHP, Spring Boot, Java, Node.js; Next.js, React, React Native, Tailwind, JavaScript, TypeScript; MySQL, PostgreSQL, MongoDB; Git, GitHub, Docker, Figma, VS Code."))

# ---- footer skyline
random.seed(911); H=300; b=[]
for i in range(90):
    sx=random.randrange(0,W//3)*3; sy=random.randrange(0,70)*3; sz=random.choice([3,3,3,6]); g=random.choice(["#fff","#888","#555","#555"])
    if random.random()<.45:
        dd=round(random.uniform(1.8,5),1); bg=round(random.uniform(0,4),1)
        b.append(R(sx,sy,sz,sz,g)[:-2]+f'><animate attributeName="opacity" values="1;0.15;1" dur="{dd}s" begin="{bg}s" repeatCount="indefinite"/></rect>')
    else: b.append(R(sx,sy,sz,sz,g))
b+=bitmap(["..####..",".######.","########","########","########","########",".######.","..####.."],700,28,6,"#fff")
b+=bitmap(["##.",".##","##."],718,40,6,"#bbb")+[R(730,64,6,6,"#bbb")]
b.append('<g opacity="0">'+R(0,0,18,3,"#fff")+R(-12,0,12,3,"#888")+R(-24,0,12,3,"#444")+
 '<animateTransform attributeName="transform" type="translate" values="60,20;420,140" dur="9s" keyTimes="0;1" repeatCount="indefinite"/>'
 '<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.82;0.84;0.94;0.97;1" dur="9s" repeatCount="indefinite"/></g>')
for i,l in enumerate(["SYSTEMS FIRST","CODE SECOND","SHIP ALWAYS"]): b+=text(l,(W-tw(l,4))//2,34+i*40,4,["#fff","#bbb","#fff"][i])
base=250; x=0
while x<W:
    w=random.choice([24,30,36,42,54]); h=random.choice([18,24,36,42,54,66,78]) if not (300<x<540) else random.choice([12,18,24,30])
    b+=[R(x,base-h,w,h,"#1c1c1c"),R(x,base-h,w,3,"#333")]
    if h>40 and random.random()<.35: b+=[R(x+w//2-1,base-h-12,3,12,"#333"),brect(x+w//2-1,base-h-15,3,3,"#fff","2s")]
    for wy in range(base-h+9,base-6,9):
        for wx in range(x+6,x+w-6,9):
            r=random.random()
            if r<.16: b.append(R(wx,wy,3,3,"#fff"))
            elif r<.22:
                dd=round(random.uniform(3,8),1)
                b.append(R(wx,wy,3,3,"#fff")[:-2]+f'><animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;0.45;0.5;0.95;1" dur="{dd}s" repeatCount="indefinite"/></rect>')
    x+=w
b.append(R(0,base,W,3,"#fff"))
for i in range(60): b.append(R(random.randrange(0,W//6)*6,base+6+random.randrange(0,3)*4,random.choice([6,12,18]),2,random.choice(["#333","#555","#222"])))
t="[ PITOU911 ] * BUILT IN THE DARK * SHIPS IN SILENCE * KH"; b+=text(t,(W-tw(t,2))//2,274,2,"#888")
out("px-footer",svg(W,H,b,"Systems first. Code second. Ship always. Pitou911, built in the dark, ships in silence."))
