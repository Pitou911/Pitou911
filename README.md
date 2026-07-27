<div align="center">

<img src="https://raw.githubusercontent.com/Pitou911/Pitou911/main/assets/pixel-banner.svg" width="100%" alt="Phnom Penh at dusk, in pixels"/>

<a href="https://git.io/typing-svg">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=17&duration=2800&pause=900&color=FFFFFF&center=true&vCenter=true&width=780&lines=root%40pitou911%3A~%24+whoami;Solo+IT+unit+%E2%80%94+Dept.+of+Government+Securities%2C+MEF;Co-Founder+%26+CTO+%E2%80%94+KhmerRooms;Laravel+%C2%B7+Next.js+%C2%B7+React+Native+%C2%B7+Spring+Boot;I+ship+the+systems+a+country+runs+on.;Built+in+the+dark+%E2%80%94+ships+in+silence." alt="Typing SVG" />
</a>

<br/>

<img src="https://komarev.com/ghpvc/?username=Pitou911&style=flat-square&color=ffffff&label=OBSERVED&labelColor=000000"/>
<img src="https://img.shields.io/badge/STATUS-OPERATIONAL-ffffff?style=flat-square&labelColor=000000"/>
<img src="https://img.shields.io/badge/LOCATION-CAMBODIA%20%F0%9F%87%B0%F0%9F%87%AD-ffffff?style=flat-square&labelColor=000000"/>
<img src="https://img.shields.io/badge/LANGUAGES-KM%20%C2%B7%20EN%20%C2%B7%20HU%20%C2%B7%20FR-ffffff?style=flat-square&labelColor=000000"/>

<br/><br/>

<img src="https://raw.githubusercontent.com/Pitou911/Pitou911/main/assets/pixel-divider.svg" width="100%" alt=""/>

</div>

## `▸ STATUS BOARD`

> Not a skills list. These are systems that are running right now, and I'm the one who gets called when they stop.

| | SYSTEM | ROLE | STACK | STATE |
|:--|:--|:--|:--|:--|
| `◉` | **KhmerRooms** — Cambodia-first hotel OTA | Co-Founder / CTO | `Next.js` `React Native` `Laravel 12` | **BUILDING** |
| `◉` | **MEF Investor Portal** — [investor.mef.gov.kh](https://investor.mef.gov.kh) | Sole engineer | `React` `Vite` `Tailwind v4` `Laravel 11` | **LIVE** |
| `◉` | **Government Securities Platform** — internal, MEF | Sole engineer | `Laravel 12` `MySQL` | **LIVE · INTERNAL** |
| `◉` | **Saravoan Medical Laboratory** | Freelance build | `React 18` `Laravel 11` `FrankenPHP` | **SHIPPED** |
| `○` | **SwiftPOS** — retail point-of-sale | Solo | `Laravel 12` `Alpine.js` `Tailwind` | [`repo →`](https://github.com/Pitou911/POS-Laravel) |
| `○` | **Immutable Audit Trail** — SHA-256 hash chain | Solo | `Laravel` `MySQL` | [`repo →`](https://github.com/Pitou911) |
| `○` | **CareNest** — symptom → disease prediction | AI engineer, team of 4 | `Spring Boot` `Flask` `scikit-learn` | [`repo →`](https://github.com/Pitou911/CareNest-AI-Disease-Prediction-App) |

<sub>`◉` in production · `○` archived or open source</sub>

---

## `▸ ARCHITECTURE — khmerrooms`

```
        ┌──────────────────┐          ┌──────────────────┐
        │   iOS / Android  │          │       Web        │
        │   React Native   │          │     Next.js      │
        └────────┬─────────┘          └─────────┬────────┘
                 └─────────────┬────────────────┘
                               │  HTTPS · Sanctum
                    ┌──────────▼───────────┐
                    │      LARAVEL 12      │
                    │  bookings · rooms ·  │
                    │  rates · availability│
                    └──────────┬───────────┘
        ┌──────────────┬───────┴───────┬──────────────┐
   ┌────▼────┐   ┌─────▼──────┐  ┌─────▼─────┐  ┌─────▼─────┐
   │  MySQL  │   │ ABA PayWay │  │  Telegram │  │  Channel  │
   │         │   │ KHQR·HMAC  │  │  ops bot  │  │  manager  │
   └─────────┘   └────────────┘  └───────────┘  └───────────┘
                        ▲
                 ┌──────┴──────┐
                 │ BOSS FIGHT  │  ███████░░░  in progress
                 └─────────────┘
```

---

## `▸ ARSENAL`

<div align="center">

<img src="https://skillicons.dev/icons?i=laravel,php,nextjs,react,tailwind,js,ts,mysql,postgres&theme=dark&perline=9"/>
<br/>
<img src="https://skillicons.dev/icons?i=spring,java,nodejs,mongodb,git,github,docker,figma,vscode&theme=dark&perline=9"/>

</div>

---

## `▸ RUNBOOK`

<details>
<summary><code>$ cat /etc/identity</code></summary>

<br/>

```yaml
name:      Song Pitou
alias:     Pitou911  ·  "twin"
base:      Phnom Penh, Cambodia
degree:    B.Sc. Computer Engineering
           University of Debrecen, Hungary  (2022–2026)
           Stipendium Hungaricum scholarship
day_job:   the entire IT department of one government department
night_job: co-founding an OTA that speaks Khmer first
creed:     Systems first. Code second. Ship always.
```

</details>

<details>
<summary><code>$ locale -a</code></summary>

<br/>

```
km_KH   ភាសាខ្មែរ     native
en_US   English      fluent
hu_HU   Magyar       four years in Debrecen will do that
fr_FR   Français     school, and it stuck
```

Four languages, one keyboard layout that still fights me.

</details>

<details>
<summary><code>$ tail -f /var/log/current.log</code></summary>

<br/>

```log
[NOW]  ABA PayWay + KHQR integration — HMAC-SHA512 verification
[NOW]  Hotel onboarding flow for KhmerRooms partners
[NOW]  Central Data Hub feasibility work for MEF
[NEXT] Getting better at system design under real load
[IDLE] A roguelite in Unity that I swear I will finish
```

</details>

<details>
<summary><code>$ uptime --offline</code></summary>

<br/>

Away from the terminal I'm on a trail somewhere, reading science fiction, or drawing things one pixel at a time. I build small, useless, beautiful software as gifts. It's the best debugging there is.

</details>

---

## `▸ TELEMETRY`

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Pitou911&show_icons=true&hide_border=true&bg_color=00000000&title_color=ffffff&text_color=888888&icon_color=ffffff&ring_color=ffffff&rank_icon=github" height="165"/>
<img src="https://streak-stats.demolab.com?user=Pitou911&hide_border=true&background=00000000&ring=ffffff&fire=ffffff&currStreakLabel=ffffff&sideLabels=888888&dates=555555&currStreakNum=ffffff&sideNums=ffffff" height="165"/>

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Pitou911&bg_color=00000000&color=ffffff&line=ffffff&point=888888&area=true&area_color=333333&hide_border=true&custom_title=COMMIT%20TELEMETRY" width="98%"/>

<br/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Pitou911&layout=compact&hide_border=true&bg_color=00000000&title_color=ffffff&text_color=888888&langs_count=8" height="150"/>

</div>

---

## `▸ OPEN CHANNELS`

<div align="center">

<a href="https://khmerrooms.com">
<img src="https://img.shields.io/badge/KHMERROOMS-000000?style=for-the-badge&logo=googlechrome&logoColor=ffffff&labelColor=000000"/>
</a>
<a href="https://www.linkedin.com/in/song-pitou-414834216/">
<img src="https://img.shields.io/badge/LINKEDIN-000000?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=000000"/>
</a>
<a href="mailto:songpitou723@gmail.com">
<img src="https://img.shields.io/badge/EMAIL-000000?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=000000"/>
</a>

</div>

---

<div align="center">

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

              ▄▄
             ████            SYSTEMS FIRST
            ██████           CODE SECOND
           ████████          SHIP ALWAYS
          ██████████
         ▀▀▀▀████▀▀▀▀
             ████
      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   [ PITOU911 ]  ·  built in the dark  ·  ships in silence  ·  ᴋʜ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

<img src="https://raw.githubusercontent.com/Pitou911/Pitou911/main/assets/pixel-divider.svg" width="100%" alt=""/>

</div>