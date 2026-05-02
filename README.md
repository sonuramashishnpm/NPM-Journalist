<div align="center">

<img src="https://img.shields.io/badge/NPM%20Journalist-v2-red?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge" />
<img src="https://img.shields.io/badge/Made%20in-India%20🇮🇳-orange?style=for-the-badge" />

<br/>
<br/>

```
███╗   ██╗██████╗ ███╗   ███╗    ██╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗ █████╗ ██╗     ██╗███████╗████████╗
████╗  ██║██╔══██╗████╗ ████║    ██║██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔══██╗██║     ██║██╔════╝╚══██╔══╝
██╔██╗ ██║██████╔╝██╔████╔██║    ██║██║   ██║██║   ██║██████╔╝██╔██╗ ██║███████║██║     ██║███████╗   ██║   
██║╚██╗██║██╔═══╝ ██║╚██╔╝██║    ██║██║   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══██║██║     ██║╚════██║   ██║   
██║ ╚████║██║     ██║ ╚═╝ ██║    ██║╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║██║  ██║███████╗██║███████║   ██║   
╚═╝  ╚═══╝╚═╝     ╚═╝     ╚═╝    ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝
```

### *Promoting Individual Journalism to every nation village*
### *so that democratic values of a nation can be strengthened*

<br/>

[![Visit NPM Journalist](https://img.shields.io/badge/🌐%20Live%20Platform-npmjournalist.onrender.com-red?style=for-the-badge)](https://npmjournalist.onrender.com)
[![FastAPI Docs](https://img.shields.io/badge/⚡%20API%20Docs-HuggingFace-yellow?style=for-the-badge)](https://sonuramashishnpm-npm-journalist.hf.space/docs)
[![DeepWiki](https://img.shields.io/badge/📖%20DeepWiki-Full%20Docs-blue?style=for-the-badge)](https://deepwiki.com/sonuramashishnpm/NPM-Journalist)
[![npmai](https://img.shields.io/badge/npmai-912K%2B%20Downloads-purple?style=for-the-badge)](https://pypi.org/project/npmai)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## ⚡ What is NPM Journalist v2?

NPM Journalist started as a simple anonymous complaint sender to government officers.

**Version 2 is a full civic-tech platform** — now with a volunteer dispatch network, geo-location based complaint routing, GitHub-style volunteer profiles, photo evidence upload, and Supabase-powered real backend.

> Built entirely on free infrastructure. Zero monthly cost. Serving real citizens.

---

## 🔄 What Changed in v2

| Feature | v1 | v2 |
|---|:---:|:---:|
| Anonymous complaints to officers | ✅ | ✅ |
| AI safety layer | ✅ | ✅ |
| Volunteer network | ❌ | ✅ |
| Geo-based complaint dispatch | ❌ | ✅ |
| Photo evidence upload | ❌ | ✅ |
| GitHub-style volunteer profiles | ❌ | ✅ |
| My Reports dashboard | ❌ | ✅ |
| FastAPI core backend | ❌ | ✅ |
| Supabase DB + Auth + Storage | ❌ | ✅ |
| OLA Maps distance matrix | ❌ | ✅ |
| Flask proxy layer | ❌ | ✅ |

---

## 🚀 How v2 Works — Full Pipeline

    CITIZEN
       |
       |  uploads photo + marks location on map + writes description
       ↓
    FLASK — npmjournalist.onrender.com
       |
       |  forwards as multipart/form-data
       ↓
    FASTAPI CORE — sonuramashishnpm-npm-journalist.hf.space
       |
       |  queries all volunteer locations from Supabase
       ↓
    OLA MAPS DISTANCE MATRIX API
       |
       |  calculates driving distance to every volunteer
       |  picks the closest one
       ↓
    SUPABASE STORAGE
       |
       |  uploads complaint photo
       |  generates public URL
       ↓
    SUPABASE DATABASE
       |
       |  inserts complaint linked to nearest volunteer email
       ↓
    VOLUNTEER DASHBOARD
       |
       |  volunteer logs in → sees complaint in My Reports tab
       ↓
    PROBLEM GETS SOLVED

---

## 🎯 Three Ways to Use NPM Journalist v2

### 📸 1 — Report a Local Problem
Citizen uploads a photo, marks location on map, describes the issue.
System finds the nearest registered volunteer and dispatches the complaint to them directly.
No login needed from citizen side.

### 📨 2 — Send Anonymous Complaint to Government Officer

Select officer, write subject and complaint.
AI safety layer reviews the message.
If safe — email sent anonymously. Identity never revealed.

Supported officers:

    DM Kota          DM Patna         DM Nalanda
    Rajasthan CM     Bihar CM         Delhi CM
    SP Kota City     SP Nalanda       SP Patna City

### 👷 3 — Join as Volunteer
Register with name, location, profession and photo.
Get assigned nearby complaints automatically.
View your GitHub-style profile and all assigned reports in the dashboard.

---

## 🏗️ Architecture

    npmjournalist.onrender.com
    Flask — Frontend + Proxy Layer (Render)
            |
            |  HTTP POST — params + files
            ↓
    sonuramashishnpm-npm-journalist.hf.space
    FastAPI — Core Backend (HuggingFace Spaces)
            |
            |── Supabase Auth     →  volunteer signup / signin
            |── Supabase Storage  →  profile photos + complaint photos
            |── Supabase DB       →  profiles table + complaints table
            └── OLA Maps API      →  driving distance matrix

---

## 🛠️ Tech Stack

| Layer | Technology | Hosting |
|---|---|---|
| Frontend | HTML, CSS, JavaScript, Leaflet.js | Render |
| Proxy Backend | Flask (Python) | Render |
| Core Backend | FastAPI (Python) | HuggingFace Spaces |
| Database | Supabase (PostgreSQL) | Supabase |
| File Storage | Supabase Storage | Supabase |
| Auth | Supabase Auth | Supabase |
| Maps | Leaflet.js + OLA Maps | OLA Krutrim |
| AI Safety Layer | npmai Ecosystem | HuggingFace |
| Anonymous Email | npmjournalist code | self |

---

## 👤 Volunteer Profile — GitHub Style

After signup or login volunteers see a full profile card:

    LEFT SIDEBAR                    RIGHT CONTENT
    ─────────────────               ─────────────────────────────────
    Profile avatar                  [ Overview ] [ My Reports ]
    Active / Passive badge
    Name + @handle                  Overview:
    Bio                               Complaints Handled | Type | Org
    Profession                        Recent Activity Feed
    Email
    Phone                           My Reports:
    Location coords                   Complaint cards with photos
    Organisation                      Text description
    Tags — Active / Org Member        Assigned timestamp

---

## 🗄️ Database Schema

    profiles table
    ──────────────────────────────────────────
    id           uuid    auto generated (primary key)
    name         text
    email        text
    password     text
    phone        text
    profession   text
    lat          text
    longt        text
    active       text
    passive      text
    jno          text
    jyes         text
    photo_url    text
    organisation text
    description  text
    updated_at   timestamp with time zone

    complaints table
    ──────────────────────────────────────────
    id           uuid    auto generated (primary key)
    email        text    (linked to volunteer)
    complaints   text
    photo_url    text

---

## 📦 npmai Ecosystem

This project is part of the **NPMAI Ecosystem** — all open source, all on free infra.

[![npmai PyPI](https://img.shields.io/pypi/v/npmai?style=flat-square)](https://pypi.org/project/npmai)
[![Downloads](https://pepy.tech/badge/npmai)](https://pepy.tech/projects/npmai)

    912,000+ total PyPI downloads
    10+ live projects under NPMAI Ecosystem
    Research paper — LARA: Latency-Aware Rerank-then-Allocate Architecture for RAG
    npmai — connects Ollama + 12 open source LLMs, no API key, no login, free

---

## 🚀 Self Host

    Step 1 — Clone
        git clone https://github.com/sonuramashishnpm/NPM-Journalist

    Step 2 — Install dependencies
        pip install flask requests

    Step 3 — Set environment variables
        SUPABASE_URL   =  your project url from supabase dashboard
        SUPABASE_KEY   =  your service role key
        OLA_MAPS_KEY   =  your ola maps api key from cloud.olakrutrim.com
        PORT           =  5000

    Step 4 — Run Flask
        python app.py

    FastAPI core — deploy separately on HuggingFace Spaces
    with same SUPABASE_URL and SUPABASE_KEY secrets

---

## 🤝 Contributing

    - Add more government officers
    - Improve AI safety prompt
    - Add support for more Indian languages
    - Improve volunteer matching algorithm
    - Add real-time complaint status tracking
    - Add notification system for volunteers

---

## 👨‍💻 Developer

<div align="center">

**Sonu Kumar**

*14 years old · From Nalanda, Bihar · Self-taught*

    Software Developer  |  AI Developer  |  Web Developer
    Cloud Developer     |  DevOps        |  TEDx Speaker
    Founder — NPMAI Ecosystem

    Self-taught with zero CS background in family
    TEDx Speaker at age 13
    Challenged state Chief Minister at age 11
    100% scholarship at Allen Career Institute Kota
    433K+ Facebook · 10k+ requests handled daily 

[![GitHub](https://img.shields.io/badge/GitHub-sonuramashishnpm-black?style=for-the-badge&logo=github)](https://github.com/sonuramashishnpm)
[![Email](https://img.shields.io/badge/Email-sonuramashishnpm@gmail.com-red?style=for-the-badge&logo=gmail)](mailto:sonuramashishnpm@gmail.com)
[![TEDx](https://img.shields.io/badge/TEDx-Watch%20Talk-red?style=for-the-badge)](https://youtu.be/qWTkKsegx9c)
[![Facebook](https://img.shields.io/badge/Facebook-433K%2B-blue?style=for-the-badge&logo=facebook)](https://facebook.com/share/19dvhX1mH7/)

</div>

---

## ⚠️ Disclaimer

This tool is only for responsible and respectful civic communication.
Misuse is not allowed. Developer is not responsible for any message content sent through the platform.

---

<div align="center">

*Made with ❤️ by Sonu Kumar · NPMAI Ecosystem · 2026*

*Empowering every citizen to raise their voice — safely, anonymously, effectively.*

**⭐ Star this repo if NPM Journalist helped you or inspired you**

</div>
