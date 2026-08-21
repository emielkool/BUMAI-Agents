---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-22
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 22 juli 2026

## 🔑 Highlights van de dag

- **Kimi K3 zet open-source record:** Moonshot AI's Kimi K3 (2,8 biljoen parameters) scoort 91,2% op BrowseComp – een all-time record voor web-agents – en belooft open weights op 27 juli; de kloof tussen open en gesloten frontier krimpt razendsnel.
- **Google Gemini 3.6 Flash gelanceerd (21 juli):** Google's nieuwste Flash-variant is live; samen met de Agentic Data Cloud-aankondiging zet Google vol in op agent-infrastructuur richting enterprise.
- **EU AI Act deadline verschoven:** De Raad van de EU keurde eind juni het Digital Omnibus-vereenvoudigingspakket goed. De compliance-deadline voor HR-systemen schuift op van 2 augustus 2026 naar 2 december 2027 – directe adempauze voor veel organisaties.
- **99,9% van patchbare AI-kwetsbaarheden ongefixed:** Nieuw rapport (HelpNet Security, 13 juli) toont aan dat 81% van bedrijven minimaal één bekende kwetsbaarheid in AI-packages draait, terwijl bijna alle beschikbare patches niet worden uitgerold.
- **Cloudoorlog verschuift naar agentoperatie:** Google, Microsoft en AWS concurreren niet meer op modelprestaties maar op wie het complete enterprise AI-stack bezit – van inferentie tot dagelijkse werkoppervlakken.

---

## 🧠 Technologie & Modellen

**Gemini 3.6 Flash (21 juli)** – Google lanceerde gisteren Gemini 3.6 Flash, een snelle en kostenefficiënte variant bedoeld voor high-volume enterprise workloads. Dit volgt op de introductie van de Agentic Data Cloud: een platformlaag die agentische workloads via Google Cloud verbindt met bedrijfsdatasets.

**Kimi K3 – open-source frontier** – Moonshot AI's Kimi K3 is de grootste open-weight release ooit: 2,8 biljoen parameters totaal, 16 actieve experts per token. Het model zet recordscores op agentic benchmarks (BrowseComp 91,2%) en coding. Open weights verwacht 27 juli. De periode 16 juni – 16 juli wordt al gezien als de sterkste maand in open AI-geschiedenis.

**NVIDIA Nemotron 3** – NVIDIA introduceerde de Nemotron 3-familie (Nano, Super, Ultra) specifiek voor agentic toepassingen – geoptimaliseerd voor efficiënte inzet op edge en inference-hardware.

**Modellandschap bredere context:** GPT-5.6 (Sol/Terra/Luna) is sinds 9 juli GA als ChatGPT-default; Claude Fable 5 is sinds 1 juli weer wereldwijd beschikbaar na een 19-daagse export-controlpauze; Grok 4.5 is goedkoop beschikbaar ($2/$6 per 1M tokens) als coding-model.

*Bron: [llm-stats.com](https://llm-stats.com/ai-news), [Skycrumbs AI Models July 2026](https://skycrumbs.com/blog/ai-models-july-2026), [ThursdAI](https://thursdai.news/releases/2026-07)*

---

## 🏛️ Governance & Ethiek

**EU AI Act Digital Omnibus goedgekeurd** – De Europese Raad gaf op 29 juni groen licht voor het eerste wijzigingspakket op de AI Act. Publicatie in het EU Publicatieblad wordt voor 2 augustus verwacht. Kernpunten:
- HR/employment-gerelateerde systemen: compliance-deadline verschuift van 2 augustus 2026 naar **2 december 2027**
- Nieuw verbod per december 2026: "nudifier" apps (niet-consensuele deepfake-beeldgeneratie)
- Bredere deadline-verlenging voor high-risk AI-systemen

**World AI Cooperation Organization gelanceerd** – De World AI Conference in Shanghai sloot op 20 juli af met de oprichting van een intergouvernementele AI-samenwerkingsorganisatie door 29 landen (o.a. Pakistan, Rusland, Kazachstan). Xi Jinping sprak voor het eerst een keynote uit. Dit markeert een geopolitieke tegenmacht naast de westerse AI-governance-arena.

**EU Cybersecurity & AI Action Plan** – De Europese Commissie publiceerde begin juli een actieplan dat lidstaten, bedrijven en overheden helpt met cybersecurity-uitdagingen van geavanceerde AI-modellen.

*Bron: [Latham & Watkins](https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines), [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [EC Cybersecurity AI plan](https://commission.europa.eu/news-and-media/news/new-eu-plan-address-risks-and-opportunities-advanced-ai-cybersecurity-2026-07-07_en)*

---

## 🔐 Security & Risk

**Patchcrisis in AI-pakketten** – Een rapport van Help Net Security (13 juli) toont: 81,2% van bedrijven met AI-packages draait minimaal één bekende kwetsbaarheid; 99,9% van beschikbare fixes blijft ongepatch. Dit is een structureel operationeel risico dat niet door het model maar door de supply chain wordt bepaald.

**GitHub Copilot RCE via prompt injection (CVSS 9.6)** – In 2026 werd aangetoond dat verborgen prompt injection in pull request-omschrijvingen remote code execution via GitHub Copilot mogelijk maakt. Agentic code-assistenten vormen een serieuze aanvalsvector in CI/CD-pipelines.

**Cursor IDE zero-click RCE** – Twee zero-click remote code execution-kwetsbaarheden in de Cursor IDE werden ontdekt waarmee aanvallers sandboxomgevingen kunnen verlaten. Directe relevantie voor teams die AI-gebaseerde IDE's inzetten.

**AI-modellen als aanvalswapen** – Berichten uit Silicon Valley en Washington wijzen op bezorgdheid dat frontier-modellen steeds effectiever worden in het identificeren van softwarekwetsbaarheden – een dual-use risico dat toezichthouders nader bestuderen.

*Bron: [HelpNet Security](https://www.helpnetsecurity.com/2026/07/13/ai-infrastructure-security-risks-report/), [eSecurity Planet](https://www.esecurityplanet.com/weekly-roundup/ai-driven-attacks-critical-exploits-and-global-breaches-define-this-week-in-july-2026-in-cybersecurity/)*

---

## 📈 Markt & Adoptie

**Microsoft $2,5 miljard enterprise AI-initiatief** – Microsoft mobiliseerde 6.000 medewerkers uitsluitend voor enterprise AI-adoptie-ondersteuning bij klanten, gekoppeld aan een investering van $2,5 miljard. Strategisch doel: het implementatiegat dichten (veel bedrijven kopen AI, weinig halen ROI).

**Google Cloud $750 miljoen ecosysteem-investering + Agentic Data Cloud** – Google koppelt zijn Cloud-platform aan agentic workloads via een nieuwe infrastructuurlaag en investeert $750M in partnernetwerk om enterprise-adoptie te versnellen.

**AWS $1 miljard AI engineers bij klanten** – Amazon Web Services stuurt AI-engineers rechtstreeks in klantteams om adoptie te versnellen. De cloud-strijd in 2026 gaat niet meer over de beste GPU of het beste model, maar over wie de volledige enterprise AI-stack bezit – van data tot dagelijkse werkoppervlakken.

**Accentbepaling: shift van model naar operatie** – Alle grote cloud-aanbieders (Google Cloud, AWS, Microsoft, Databricks) hebben hun messaging in juni/juli bewust verschoven van "beste model" naar "beste agent-operatie". De vier kernuitdagingen: business context, governance, observability en inference-kosten. Dit is waarop Ctac's klanten ook vastlopen.

*Bron: [HPCwire/BigDATAwire](https://www.hpcwire.com/bigdatawire/2026/07/06/microsoft-launches-new-2-5b-ai-initiative-with-6000-experts-to-help-enterprises-deploy-a/), [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/), [Cloud Wars](https://cloudwars.com/innovation-leadership/agentic-ai-wars-will-microsoft-aws-match-google-clouds-750-million-ecosystem-investment/)*

---

## 💡 Ctac-relevantie

**Drie directe aandachtspunten voor deze week:**

1. **EU AI Act deadline-verschuiving = verkoopmoment, geen uitstelmoment.** De verschoven HR-deadline naar december 2027 zal bij klanten de urgentie verlagen. Ctac kan dit proactief ombuigen: gebruik de adempauze om nu een solide AI-governance-baseline te leggen, zodat klanten in 2027 niet opnieuw onder tijdsdruk komen. Dit is een helder propositie-haakje voor de advies-/compliance-track.

2. **Agentic AI-operatie is het nieuwe battleground – en Ctac's niche.** De verschuiving van "model kiezen" naar "AI-agents in productie brengen en beheren" speelt recht in de handen van een implementatiepartner als Ctac. De vier operationele uitdagingen (context, governance, observability, kosten) zijn precies de problemen waar klanten partner-ondersteuning bij nodig hebben. Dit verdient een concrete serviceformulering.

3. **AI security is geen optioneel onderdeel meer.** De patchcrisis (99,9% ongefixed) en de Copilot/Cursor-kwetsbaarheden laten zien dat AI-tooling in de development-pipeline een actief aanvalsoppervlak is geworden. Voor klanten die Ctac vraagt om AI-assisted development in te richten, moet security by design standaard onderdeel zijn van de aanpak.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI Model News July 2026](https://llm-stats.com/ai-news)
- [ThursdAI – July 2026 Releases](https://thursdai.news/releases/2026-07)
- [Skycrumbs – AI Models July 2026](https://skycrumbs.com/blog/ai-models-july-2026)
- [Latham & Watkins – EU AI Act Update](https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines)
- [DLA Piper – Digital Omnibus AI Act](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Cybersecurity & AI Action Plan](https://commission.europa.eu/news-and-media/news/new-eu-plan-address-risks-and-opportunities-advanced-ai-cybersecurity-2026-07-07_en)
- [HelpNet Security – AI vulnerabilities unpatched](https://www.helpnetsecurity.com/2026/07/13/ai-infrastructure-security-risks-report/)
- [eSecurity Planet – AI-Driven Attacks July 2026](https://www.esecurityplanet.com/weekly-roundup/ai-driven-attacks-critical-exploits-and-global-breaches-define-this-week-in-july-2026-in-cybersecurity/)
- [HPCwire – Microsoft $2.5B AI Initiative](https://www.hpcwire.com/bigdatawire/2026/07/06/microsoft-launches-new-2-5b-ai-initiative-with-6000-experts-to-help-enterprises-deploy-a/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Cloud Wars – Agentic AI Wars](https://cloudwars.com/innovation-leadership/agentic-ai-wars-will-microsoft-aws-match-google-clouds-750-million-ecosystem-investment/)
- [NVIDIA Nemotron 3](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)
