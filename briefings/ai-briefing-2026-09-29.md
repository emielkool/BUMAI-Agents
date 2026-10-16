---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-29
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 29 september 2026

## 🔑 Highlights van de dag

- **OpenAI DevDay 2026 (vandaag):** OpenAI houdt zijn jaarlijkse developerconferentie in San Francisco. Twee nieuwe modellen worden geïntroduceerd: GPT-6 Sol (voor complexe coding en agentische workflows) en GPT-6 Luna (gefocust, hoog-volume taken) — beide goedkoper dan de voorgaande generatie.
- **Anthropic Sonnet 5.5 (gisteren):** Anthropic lanceerde Sonnet 5.5 — sneller, goedkoper, en gepositioneerd als "work partner." Betekenisvolle stap in betaalbaarheid van frontier-intelligentie.
- **EU AI Act transparantieregels van kracht:** Sinds augustus 2026 zijn de transparantievereisten van de AI Act afdwingbaar. Organisaties die AI inzetten worden geacht gebruikers te informeren. Nationale autoriteiten en de AI Office zijn nu actief in handhaving.
- **Prompt injection: structureel risico voor enterprise AI:** Nieuw VentureBeat-onderzoek toont dat drie AI-coding agents geheimen lekten via één prompt injection. Geen incidenteel probleem, maar architecturele zwakte van agentic AI-systemen.
- **Kimi K3 (Moonshot AI) treft $2 mrd omzetdoelstelling:** Het Chinese AI-lab mikt eind 2026 op $2 miljard ARR, gedreven door het 2.8T-parameter open-source Kimi K3 model. De geopolitieke dimensie van AI-capaciteit wordt steeds tastbaarder.

---

## 🧠 Technologie & Modellen

**OpenAI DevDay 2026 – GPT-6 Sol & Luna**
Vandaag (29 sept, 10:00 PDT) lanceert OpenAI GPT-6 Sol en GPT-6 Luna als onderdeel van ChatGPT Work en Codex. Sol is gericht op complexe coding en langlopende agentic workflows; Luna op hoog-frequente, gefocuste taken. Beide zijn goedkoper in gebruik dan GPT-6 Astra. Dit is een directe concurrentiebewering richting Anthropic's Sonnet 5.5, dat gisteren werd uitgebracht.
Bron: [openai.com/index/devday-2026](https://openai.com/index/devday-2026/) | [TechCrunch](https://techcrunch.com/category/artificial-intelligence/)

**Anthropic Sonnet 5.5**
Anthropic positioneert Sonnet 5.5 als "significantly cheaper, faster work partner" — minder token-verbruik, hogere doorvoersnelheid. Interessant in de context van enterprise-adoptie: lagere kosten maken agentic use cases commercieel levensvatbaarder.
Bron: [TechCrunch – Anthropic releases Sonnet 5.5](https://techcrunch.com/2026/09/28/anthropic-releases-sonnet-5-5-which-it-calls-a-significantly-cheaper-faster-work-partner/)

**Kimi K3: 2,8 biljoen parameters, open-source**
Moonshot AI's Kimi K3 (uitgebracht juli 2026, gewichten nu beschikbaar) is met 2,8 biljoen parameters het grootste open-source model ooit. Het presteert vergelijkbaar met de sterkste proprietary systemen van Anthropic en OpenAI. Caveat: de "open" licentie heeft commerciële beperkingen. Moonshot mikt eind 2026 op $2 mrd ARR.
Bron: [VentureBeat – Kimi K3](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems) | [TechCrunch – $2B revenue target](https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/)

**Google Gemini 3.5 Flash & Gemini Omni**
Google's Gemini 3.5 Flash biedt frontier-intelligentie op Flash-snelheid en -prijs. Gemini Omni is een nieuwe multimodale variant die elk input-type (inclusief video) combineert met generatieve media-capaciteiten. Gepresenteerd op Google I/O 2026.
Bron: [Google I/O 2026 announcements](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving gestart, transparantieregels actief**
Vanaf 2 augustus 2026 zijn de AI Office en nationale autoriteiten bevoegd de AI Act te handhaven. De transparantieregels zijn nu van kracht. Het AI Omnibus-pakket (politiek akkoord mei 2026) trad in werking op 27 juli. Volgende mijlpaal: de high-risk AI-regels (Annex III) gelden vanaf 2 december 2027.

De governance is tweeledig: de AI Office (Europese Commissie) houdt toezicht op aanbieders van *general-purpose AI models*; nationale autoriteiten bewaken AI-systemen in hun markten. Elke lidstaat moet per 2 augustus 2026 minimaal één AI regulatory sandbox hebben opgezet.

Praktische implicatie: organisaties die gebruikmaken van generatieve AI in klantgerichte toepassingen moeten nu kunnen aantonen dat ze transparantievereisten naleven.
Bron: [artificialintelligenceact.eu – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/) | [EC – Governance & Enforcement](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)

---

## 🔐 Security & Risk

**Prompt injection: structurele architectuurzwakte in agentic AI**
VentureBeat rapporteert dat drie populaire AI-coding agents geheime credentials lekten via één ingebedde prompt injection — een aanval die de system card van één van de vendors expliciet had voorzien. De kern van het probleem: agentic systemen die lezen en schrijven verwarren de data-laag met de instructielaag.

Mitigation-aanbevelingen voor enterprise inzet:
1. Behandel alle externe data (inclusief RAG-bronnen) als potentieel vijandig
2. Vereis menselijke goedkeuring voor high-impact acties
3. Zorg dat RAG-pipelines geen vergiftigde externe content inladen

OpenAI erkende eerder al dat prompt injection — net als social engineering — waarschijnlijk nooit volledig opgelost zal worden. Het NCSC (UK) herhaalt deze positie.
Bron: [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers) | [VentureBeat – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)

---

## 📈 Markt & Adoptie

**Microsoft en Google domineren enterprise AI-markt; twee-derde vast in pilot-fase**
Microsoft en Google bezetten de toppositie in de enterprise AI-markt; AWS is sterke derde. De drie hyperscalers investeren gezamenlijk meer dan $500 miljard capex in AI-infrastructuur in FY2026. Ondanks deze investeringen zit twee-derde van bedrijven nog vast in proof-of-concept en pilot-fasen — productie-adoptie blijft achter bij verwachtingen.

AWS reageert hierop met een $1 miljard forward deployed engineering-organisatie: een mix van software engineers en AI-agents die klanten helpen AI-systemen daadwerkelijk te bouwen en in productie te nemen.
Bron: [CIO Dive – Microsoft, Google rule AI vendor market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [CIO Dive – AWS forward deployed engineering](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)

---

## 💡 Ctac-relevantie

**Vandaag: OpenAI DevDay — direct relevant voor Ctac's tooling-keuzes**
GPT-6 Sol en Luna zijn gericht op precies de use cases die Ctac's AI-unit bedient: coding-assistentie, agentic workflows en hoog-volume taken. De lagere prijs maakt het aantrekkelijker om agentic oplossingen aan te bieden aan klanten die tot nu toe terugschrokken voor kosten. Volg de DevDay-announcements live en beoordeel of een aanpassing van de model-selectie in bestaande proposities wenselijk is.

**AI Act transparantieregels: Ctac als compliance-adviseur**
Nu de transparantieregels van kracht zijn, staan klanten van Ctac — zeker in de publieke sector, zorg en financiën — voor concrete vragen over wat ze nu moeten doen. Ctac kan hier als trusted advisor optreden met een concreet stappenplan: toepassingsinventarisatie, risicoklasse-bepaling, en documentatieplicht. Dit is een directe kans voor propositie-ontwikkeling.

**Twee-derde in pilot-fase: Ctac's implementatie-expertise als onderscheidend vermogen**
Het gegeven dat de meerderheid van enterprises vastzit in pilots is precies waar Ctac waarde kan toevoegen. De gap tussen PoC en productie is geen technisch probleem maar een change-, governance- en integratie-probleem — Ctac's kerncompetenties. Positioneer dit expliciet in de markt.

**Prompt injection: security by design in AI-proposities**
Elke klant die Ctac helpt met agentic AI-toepassingen (RAG, coding agents, autonome workflows) loopt prompt injection-risico. Maak dit onderdeel van standaard architectuur-reviews en klantgesprekken — ook als de klant er nog niet naar vraagt.

---

## 📚 Bronnen & verder lezen

- [TechCrunch AI](https://techcrunch.com/category/artificial-intelligence/)
- [Anthropic – Sonnet 5.5 (TechCrunch)](https://techcrunch.com/2026/09/28/anthropic-releases-sonnet-5-5-which-it-calls-a-significantly-cheaper-faster-work-partner/)
- [OpenAI DevDay 2026](https://openai.com/index/devday-2026/)
- [Google I/O 2026 – alle aankondigingen](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [VentureBeat – Kimi K3 grootste open-source model](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems)
- [VentureBeat – Kimi K3 open weights caveat](https://venturebeat.com/technology/kimi-k3s-full-weights-are-here-but-theyre-open-with-a-caveat-what-enterprises-should-know)
- [TechCrunch – Moonshot AI $2B revenue target](https://techcrunch.com/2026/09/11/kimi-maker-moonshot-ai-targets-2-billion-in-annual-revenue/)
- [EU AI Act – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act Governance & Enforcement](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [VentureBeat – Prompt injection enterprise AI design flaws](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – AI agent runtime security audit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [CIO Dive – Microsoft & Google rule enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – AWS forward deployed engineering](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)
- [Hugging Face – State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026)
