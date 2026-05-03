---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-03
Periode: 2026-04-01 / 2026-04-30
Status: Afgerond
tags:
  - maandoverzicht
  - april-2026
---

# AI Maandbriefing – April 2026

> Synthese van alle dagbriefings en weekoverzichten voor april 2026 (W15–W18).
> Gebaseerd op ~20 dagbriefings en 3 weekoverzichten.

---

## 🔑 Maand in één oogopslag

April 2026 is de maand waarin agentic AI ophield een belofte te zijn en een productie-realiteit werd. Drie hyperschalers — Microsoft, Google en OpenAI — brachten elk volwassen agentic platforms op de markt. Tegelijkertijd liet Anthropic's Claude Mythos zien dat dezelfde AI-capaciteiten dual-use zijn geworden: krachtig genoeg om duizenden zero-day kwetsbaarheden te vinden, en daarmee te riskant om breed te distribueren. De EU AI Act-deadline van 2 augustus nadert onvermijdelijk na de mislukking van de Omnibus-triloog. En DeepSeek V4 herdefinieerde in één week de prijs-prestatieverhouding van frontier AI.

**De vijf structurele verschuivingen van april:**
1. Agentic AI = standaard product (geen experiment meer)
2. Dual-use AI = bewezen schaalbaar dreigingsniveau
3. Open-source = frontier-kwaliteit voor 1/20e van de prijs
4. MCP = standaard én kwetsbaarheidsoppervlak
5. EU AI Act = harde deadline, geen uitstel meer

---

## 📅 Tijdlijn april 2026

### Week 14 – vroeg april (1–6 april)

| Datum | Gebeurtenis | Domein |
|-------|-------------|--------|
| 2 apr | Microsoft lanceert drie in-house foundation models: MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2 — een directe aanval op OpenAI's monopolie bij Microsoft | Technologie |
| 3 apr | A2A-protocol (Agent-to-Agent, Google) krijgt brede industrie-endorsement; Microsoft committeert aan A2A voor multi-agent interoperabiliteit | Technologie |
| ~5 apr | MCP overgedragen door Anthropic aan de nieuw opgerichte Agentic AI Foundation (Anthropic, Block, OpenAI); >10.000 actieve publieke servers | Technologie |

---

### Week 15 – Mythos en Glasswing (7–12 april)

| Datum | Gebeurtenis | Domein |
|-------|-------------|--------|
| 7 apr | **Anthropic onthult Claude Mythos Preview** — het krachtigste model ooit, bewust niet publiek uitgebracht vanwege extreme cybersecurity-capabilities (83,1% CyberGym; 181 werkende exploits voor Firefox 147) | Security / Tech |
| 7 apr | **Project Glasswing gelanceerd** — $100M initiatief met 12 partners (Amazon, Apple, Cisco, CrowdStrike, Google, Linux Foundation, Microsoft, Nvidia, Palo Alto Networks) om zero-days defensief te patchen | Security |
| 8 apr | EC publiceert praktische richtlijnen voor AI-systeemclassificatie (definitie AI-systeem, Art. 3) — eerste concrete implementatiedocumenten | Governance |
| 9 apr | Meta lanceert Muse Spark — nieuw multi-agent reasoning model met "Contemplating"-modus voor complexe vraagstukken | Technologie |
| ~10 apr | Google Gemma 4 beschikbaar (Apache 2, 31B dense, #3 wereldwijd op Arena-leaderboard) | Technologie |
| ~10 apr | China's GLM-5 (#1 open-weight op LMArena, MIT, volledig op Huawei Ascend-chips) — bewijst soevereine AI-stack | Technologie |
| 12 apr | Trump-officials zouden banken aanmoedigen Mythos te testen; relatie Anthropic–Trump-administratie lijkt te verbeteren | Governance |

---

### Week 16 – Stanford AI Index en open-source inhaalslag (13–19 april)

| Datum | Gebeurtenis | Domein |
|-------|-------------|--------|
| 13 apr | **Stanford AI Index 2026 gepubliceerd**: SWE-bench van 60% → ~100% in 1 jaar; 88% van organisaties gebruikt AI; VS–China-gap gedaald naar 2,7%; transparantiescore frontier labs daalt van 58 → 40 | Technologie / Markt |
| 14 apr | Anthropic bevestigt briefing aan Trump-administratie over Mythos | Governance |
| 16 apr | Arcee AI Trinity gelanceerd (400B, Apache 2) — grootste open-weight release buiten China ooit | Technologie |
| 16 apr | Zhipu GLM-4.6V (106B, native tool-calling, 128K context, SOTA op 20+ benchmarks) | Technologie |
| 17 apr | LangChain/LangGraph-kwetsbaarheden: 3 CVE's blootstelling van bestanden, env secrets en databaseinhoud in populaire RAG-frameworks | Security |
| ~18 apr | NSA begint gebruik van Mythos, ondanks beperkte toegang (Pentagon-vetes) — lek van restricted model | Security |
| 18 apr | Anthropic–Trump-relatie "aan het ontdooien" — geopolitiek relevant voor frontier AI-toegang | Governance |
| ~18 apr | Recruteringstools per 17 maart formeel high-risk onder EU AI Act (AI voor kandidaatscreening = high-risk) | Governance |

---

### Week 17 – Google Cloud Next en MCP-kwetsbaarheid (20–26 april)

| Datum | Gebeurtenis | Domein |
|-------|-------------|--------|
| 20 apr | Enterprise AI Adoption Curve: 88% gebruikt AI, 97% executives deployt agents — maar slechts 29% rapporteert significante ROI | Markt |
| 20 apr | NSA-gebruik Mythos officieel bevestigd via TechCrunch | Security |
| 21 apr | EC laat €63,2M vrij voor AI-innovatie in gezondheid en online veiligheid | Governance |
| 21 apr | **Ongeautoriseerde groep krijgt toegang tot Mythos** — bewust beperkte release blijkt niet waterdicht | Security |
| 22 apr | **Google Cloud Next 2026**: Gemini Enterprise Agent Platform (Agent Designer, Skills, Inbox, long-running agents), TPU 8i (1.152 per pod, 3× SRAM), Agentic Data Cloud, Agentic Defense, $750M partnercommitment | Technologie / Markt |
| 22 apr | Microsoft Copilot Agent Mode voor Word, Excel en PowerPoint **GA** — agentic capabilities voor alle M365-gebruikers | Technologie |
| 22 apr | Claude Opus 4.7 op Amazon Bedrock (task budgets, xhigh-effort, 2576px vision, SWE-bench Pro 64,3%) | Technologie |
| 23 apr | **OpenAI lanceert GPT-5.5** — best model tot nu toe, sterk in computer use, web search, code; 6 weken na GPT-5.4; $5/M input-tokens | Technologie |
| ~23 apr | MCP-kwetsbaarheid gepubliceerd (OX Security): RCE via unsafe STDIO-standaardinstellingen in officiële SDK; 200.000 instanties kwetsbaar, 10 CVE's in LangChain/LangFlow/LiteLLM/Flowise; Anthropic weigert te patchen ("by design") | Security |
| 24 apr | **DeepSeek V4 Pro + Flash gelanceerd** (MIT, 1M context, frontier-prestaties voor 1/20e prijs Opus 4.7 en GPT-5.5) | Technologie |
| 24 apr | Deloitte lanceert Google Cloud Agentic Transformation Practice: 1.000+ industry agents, 25.000 Gemini Enterprise-licenties | Markt |

---

### Week 18 – Omnibus mislukt, Microsoft GA, eindejaar april (27 april – 1 mei)

| Datum | Gebeurtenis | Domein |
|-------|-------------|--------|
| 27 apr | Microsoft Copilot Frontier-update: Outlook agentisch (e-mailtriage, follow-ups, kalenderconflicten) | Technologie |
| 27 apr | **Avoca haalt $125M op bij $1B-valuation** — AI-voice-agent voor loodgieters boekt, plant en volgt op volledig autonoom | Markt |
| 28 apr | **EU Digital Omnibus-triloog mislukt** na 12 uur onderhandelen — voorstel voor uitstel high-risk deadline (→ dec 2027) haalde geen akkoord; augustus-deadline staat | Governance |
| 29 apr | Onderzoekers documenteren 10 concrete in-the-wild indirect prompt injection-payloads: financiële fraude, bestandsverwijdering, API-key-diefstal | Security |
| 30 apr | OpenAI beperkt toegang tot eigen "Cyber"-model — na kritiek op Anthropic's aanpak met Mythos | Security |
| 1 mei | **Microsoft 365 E7 "The Frontier Suite" + Agent 365 GA** — bundelt M365 E5, Entra Suite, Copilot en agent-governance | Technologie / Markt |

---

## 🧠 Thematische analyse

### Technologie & Modellen: het agentic tijdperk is begonnen

April 2026 markeerde de overgang van AI-modellen als API-endpoints naar AI-agents als standaard enterprise-infrastructuur. Drie bewegingen domineerden:

**1. Frontier race versnelt:** GPT-5.5 (23 april), Claude Opus 4.7 (22 april) en Gemini 3.1 Ultra leverden elk nieuwe benchmarkrecords. De releasefrequentie — GPT-5.5 slechts 6 weken na GPT-5.4 — suggereert dat modelfamilies nu meer op software-releases dan op wetenschappelijke doorbraken lijken. Prijspariteit aan de top ($5/M input) is een feit.

**2. Open-source comprimeert de gap:** DeepSeek V4 (24 april) leverde frontier-prestaties voor 1/20e van de prijs van GPT-5.5 of Opus 4.7, onder MIT-licentie. Gemma 4 (#3 Arena-leaderboard, Apache 2), Arcee Trinity (400B, Apache) en GLM-5 (#1 open-weight, MIT, draait op Huawei) bewijzen dat open-source de kloof heeft gesloten. Soevereine AI-deployment is nu technisch haalbaar zonder NVIDIA of cloud-API's.

**3. Agentic infrastructuur wordt standaard:** MCP (10.000+ actieve servers, overgedragen aan Agentic AI Foundation) en A2A (Google + Microsoft-endorsement) zijn de infrastructuurstandaarden waarop de markt bouwt. Google Cloud Next 2026 (22 april) zette de toon met een compleet agentic platform. Microsoft volgde met Copilot Agent Mode GA voor alle M365-gebruikers op dezelfde dag. Op 1 mei werden M365 E7 en Agent 365 de commerciële verpakking daarvan.

---

### Governance & Beleid: deadline staat, geen uitstel

De politieke dynamiek rondom de EU AI Act werd in april definitief beslist: de Omnibus-triloog op 28 april mislukte na 12 uur onderhandelen. Het voorstel om high-risk compliance te verschuiven naar december 2027 haalde geen akkoord. **De deadline van 2 augustus 2026 is een harde juridische realiteit.**

Wat al geldt:
- Verboden AI-praktijken en AI-literacy: van kracht per 2 februari 2025
- GPAI-verplichtingen en governance: van kracht per 2 augustus 2025
- **High-risk AI, transparantie, incidentmeldplicht: van kracht per 2 augustus 2026**

Aanvullende context: de EC publiceerde op 8 april de eerste praktische classificatierichtlijnen. Per 17 maart is AI in wervingsprocessen formeel high-risk. Nationale sandboxen moeten vóór augustus operationeel zijn. De Commissie trekt €63,2M vrij voor AI in gezondheid en veiligheid (21 april). De geopolitieke dimensie verschuift: Anthropic-Trump-relatie verbetert, NSA gebruikt Mythos, China's open-weight dominantie groeit.

---

### Security & Risk: dual-use AI bereikt drempelkruising

April 2026 formaliseerde wat security-onderzoekers al langer voorspelden: AI-modellen zijn dual-use geworden op een niveau dat bewuste toegangsbeperking vereist.

**Mythos als keerpunt:** Claude Mythos vond autonoom duizenden zero-days in alle grote OS'en en browsers, genereerde 181 werkende exploits voor Firefox 147. Anthropic beperkt bewust de toegang via Project Glasswing — maar zelfs die beperking bleek lek (ongeautoriseerde toegang, NSA-gebruik). OpenAI volgde met dezelfde aanpak voor zijn Cyber-model.

**MCP als aanvalsoppervlak:** De kwetsbaarheid in de officiële MCP SDK (Remote Code Execution via STDIO) raakt 200.000 instanties en tien populaire frameworks. Anthropic erkent het probleem maar patcht niet — de verantwoordelijkheid ligt bij de integrator. Dit is de meest urgente operationele kwetsbaarheid voor teams die agentic AI bouwen.

**Prompt injection in productie:** 10 gedocumenteerde in-the-wild aanvallen (29 april), AI-cybercampagne CyberStrikeAI (600+ FortiGate-firewalls, 55 landen, volledig autonoom), LangChain/LangGraph CVE's. OWASP Top 10 Agentic Applications 2026 formaliseert tien categorieën specifiek voor AI-agents.

**Schaalcijfers:** 88% van enterprises meldde AI-agent security-incident vorig jaar; aanvallers compromitteerden AI-tools bij 90+ organisaties in 2025 (CrowdStrike GTR 2026); malicieuze prompts +32% (nov 2025 → feb 2026).

---

### Markt & Adoptie: groei zonder ROI

De enterprise AI-markt groeide in april langs twee tegengestelde assen:

**Adoptie is massaal:** 88% van organisaties gebruikt AI in minimaal één functie (Stanford). 97% van executives deployt agents. Gartner verwacht dat 40% van enterprise-applicaties eind 2026 AI-agents bevat (vs. <5% in 2025). AI-softwarespend groeit 60% YoY naar $452 miljard.

**ROI blijft achter:** Slechts 29% rapporteert significante ROI. 79% ervaart implementatieknelpunten. 49% zit in pilots of is nog niet begonnen. PwC: 75% van de economische AI-winst gaat naar 20% van de bedrijven.

**Consolidatie bij grote spelers:** Microsoft ($37B AI-omzet, +123% YoY; Azure +40%), Google Cloud ($20B, +63%), Deloitte lanceert Google Cloud Agentic Practice (1.000+ industry agents). Enterprise budgetten stijgen maar concentreren bij minder leveranciers. De grote consultancybedrijven bouwen kant-en-klare agent-bibliotheken — de differentiatie verschuift van "wij begrijpen AI" naar "wij implementeren het veilig en schaalbaar".

**Verticalisering werkt:** Avoca's $1B-valuation voor een AI-agent voor loodgieters toont dat agentic ROI het duidelijkst is in smalle, herhaalbare workflows — verticale agents voor specifieke sectoren en processen zijn de sterkste ROI-propositie.

---

## 💡 Strategische implicaties voor Ctac

### 1. Microsoft Agent 365 = verkoopmoment nu
M365 E7 en Agent 365 zijn per 1 mei GA. Elke klant op Microsoft 365 heeft nu agentic capabilities aangeboden gekregen — zonder dat ze de governance, security of integratie geregeld hebben. Dit is het meest directe actie-item: proactief klanten benaderen voor impactscans, governance-kaders en agentische integraties op hun bestaande M365-omgeving.

### 2. EU AI Act readiness-scan als propositie in Q2
De augustus-deadline staat. 78% van enterprises is niet voorbereid (Vision Compliance 2026). Klanten in overheid, zorg en finance hebben een urgente compliance-behoefte. Een Ctac readiness-scan (AI-systeeminventarisatie, risicoklassificatie, documentatievereisten per systeem) is een directe propositie die nu relevant is — niet in het najaar.

### 3. MCP-kwetsbaarheid: direct actiegebied voor lopende projecten
Elk Ctac-project dat MCP gebruikt (via LangChain, LangFlow, LiteLLM, Flowise of directe Anthropic SDK) moet worden geauditeerd op STDIO-configuratie. Anthropic patcht niet. Dit is geen theoretisch risico.

### 4. Security by design als verkoopargument
10 in-the-wild prompt injection-aanvallen, OWASP Agentic Top 10, CyberStrikeAI-campagne — de markt heeft nu concrete aanvalspatronen. Elk agentic Ctac-project heeft een threat model nodig: welke databronnen leest de agent, welke acties kan hij uitvoeren, hoe wordt prompt injection gedetecteerd? Dit is zowel risicobeheer als differentiator.

### 5. Pilot-naar-productie als kernpropositie
79% ervaart implementatieknelpunten; 49% zit vast in pilots. De bottlenecks zijn data-architectuur, integratie, monitoring en security — exact Ctac's speelveld. De markt is klaar voor de volgende stap; de vraag is wie de productiestap begeleidt.

### 6. Open-source en soevereine AI voor datakritische klanten
DeepSeek V4 (MIT), Gemma 4 (Apache 2), GLM-5 (MIT) maken on-premise frontier-deployment technisch haalbaar. Voor klanten in overheid of finance met soevereiniteitsvereisten is dit een concreet alternatief voor cloud-API's. Technische kennis van lokale inference-stacks (vLLM, Ollama) + integratie is een directe differentiator.

---

## 📊 Maandcijfers in perspectief

| Indicator | Waarde | Context |
|-----------|--------|---------|
| AI-softwarespend 2026 | $452 miljard | +60% YoY (Gartner) |
| Enterprise AI-adoptie | 88% | Gebruikt AI in ≥1 functie (Stanford AI Index) |
| Agents in productie | 97% executives | Maar slechts 29% significante ROI |
| Azure-groei Q1 2026 | +40% YoY | Microsoft AI-omzet $37B run rate (+123%) |
| Google Cloud Q1 2026 | $20 miljard | +63% YoY |
| DeepSeek V4 prijs | 1/20e van GPT-5.5 | MIT-licentie, frontier-prestaties |
| MCP-instanties kwetsbaar | ~200.000 | RCE mogelijk; Anthropic patcht niet |
| Prompt injection incidents | +32% | Nov 2025 → feb 2026 (Cisco) |
| EU AI Act deadline | 93 dagen | 2 augustus 2026, high-risk AI |
| Agentic AI-marktwaarde 2026 | $8,5 miljard | → $35–45B in 2030 (Deloitte) |

---

## 📚 Bronnen

**Kernbriefings en weekoverzichten**
- [AI Weekoverzicht W16 – 13–17 april 2026](weekoverzichten/ai-weekoverzicht-2026-W16.md)
- [AI Weekoverzicht W17 – 20–24 april 2026](weekoverzichten/ai-weekoverzicht-2026-W17.md)
- [AI Weekoverzicht W18 – 27 apr–1 mei 2026](weekoverzichten/ai-weekoverzicht-2026-W18.md)

**Technologie**
- [Introducing GPT-5.5 | OpenAI](https://openai.com/index/introducing-gpt-5-5/)
- [Introducing Claude Opus 4.7 | Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
- [Google Cloud Next 2026 recap | Google Cloud Blog](https://cloud.google.com/blog/topics/google-cloud-next/next26-day-1-recap)
- [DeepSeek V4 arrives at 1/6th the cost | VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- [Microsoft three new foundational models | TechCrunch](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)
- [MCP donated to Agentic AI Foundation | Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [Stanford AI Index 2026 | Stanford HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report)

**Governance**
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU Digital Omnibus trilogue fails | The Next Web](https://thenextweb.com/news/eu-ai-act-omnibus-deal-fails-april-2026-talks)
- [EC richtlijnen AI-definitie | digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [EU AI Act 2026 compliance risks | legalnodes.com](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)

**Security**
- [Anthropic Project Glasswing | Anthropic](https://www.anthropic.com/glasswing)
- [Claude Mythos Preview | TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [Unauthorized access to Mythos | TechCrunch](https://techcrunch.com/2026/04/21/unauthorized-group-has-gained-access-to-anthropics-exclusive-cyber-tool-mythos-report-claims/)
- [MCP critical vulnerability | The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)
- [MCP supply chain risk | OX Security](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/)
- [10 in-the-wild prompt injection attacks | Infosecurity Magazine](https://www.infosecurity-magazine.com/news/researchers-10-wild-indirect/)
- [OpenAI restricts Cyber model | TechCrunch](https://techcrunch.com/2026/04/30/after-dissing-anthropic-for-limiting-mythos-openai-restricts-access-to-cyber-too/)
- [Cisco State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)

**Markt**
- [Microsoft Agent 365 & M365 E7 GA | Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/28/unlocking-human-ambition-to-drive-business-growth-with-ai/)
- [Microsoft & Google rule enterprise AI | CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Deloitte Google Cloud Agentic Practice | Deloitte US](https://www.deloitte.com/us/en/about/press-room/deloitte-launches-google-cloud-agentic-transformation-practice.html)
- [Enterprise AI adoption 2026 challenges | Writer](https://writer.com/blog/enterprise-ai-adoption-2026/)
- [Avoca $1B AI voice agent | VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Agentic AI Goes Mainstream | OutSystems](https://www.outsystems.com/news/enterprise-ai-agent-report-2026/)
