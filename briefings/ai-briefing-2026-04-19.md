---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-19
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 19 april 2026

## 🔑 Highlights van de dag

- **Anthropic Mythos + Project Glasswing** is dé grote AI-veiligheidsstory van deze week: een model zo capabel dat het duizenden zero-day exploits vond in Firefox, Windows en macOS – en daarom bewust níet publiek uitgebracht wordt. Glasswing-partners (Amazon, Apple, Microsoft, CrowdStrike e.a.) mogen het wél inzetten voor defensieve toepassingen.
- **OpenAI GPT-5.4 op Windows** introduceert native computer-use in een mainline model; Codex draait nu als parallelle desktop-agent met isolated worktrees en reviewable diffs. Dit is geen feature, dit is een paradigmawisseling voor ontwikkelworkflows.
- **Microsoft lanceert drie in-house AI-modellen** (spraakherkenning, stemgeneratie, beeldcreatie) – een signaal dat de $3 biljoen-gigant niet meer uitsluitend van OpenAI afhankelijk wil zijn voor modelontwikkeling.
- **Anthropic brieft Trump-administratie over Mythos**; de relatie lijkt aan het ontdooien. Dit heeft geopolitieke implicaties voor AI-regulering en toegang tot frontier-modellen.
- **EU AI Act nadert volledige toepasselijkheid** (2 augustus 2026): organisaties die nog niet in actie zijn hebben nog ~3,5 maand.

---

## 🧠 Technologie & Modellen

### Anthropic Claude Mythos Preview
Anthropic heeft Claude Mythos gelanceerd als besloten preview via **Project Glasswing**. Het model is opmerkelijk capabel op het gebied van computerveiligheid: in tests genereerde het 181 werkende exploits voor Firefox 147-kwetsbaarheden, tegenover slechts 2 bij het vorige Opus 4.6-model. Intern vond Anthropic duizenden zero-days in alle grote besturingssystemen en browsers. Juist deze power maakt het model te riskant voor publieke toegang.

Partners in Project Glasswing: Amazon, Apple, Broadcom, Cisco, CrowdStrike, Linux Foundation, Microsoft en Palo Alto Networks. Anthropic stelt $100M aan usage credits beschikbaar voor defensief gebruik, plus $4M in donaties aan open-source security-organisaties.

*Bronnen: [TechCrunch – Mythos preview](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) | [VentureBeat – Project Glasswing](https://venturebeat.com/technology/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release) | [Anthropic glasswing](https://www.anthropic.com/glasswing)*

### OpenAI GPT-5.4 & Codex voor Windows
GPT-5.4 is OpenAI's eerste general-purpose model met **native computer-use capabilities** – agents kunnen nu zelfstandig applicaties bedienen. Codex is nu ook als Windows-desktopapp beschikbaar voor ChatGPT Business-omgevingen, met ondersteuning voor parallelle agents, isolated worktrees en reviewable diffs.

*Bron: [OpenAI – GPT-5.4](https://openai.com/index/introducing-gpt-5-4/) | [TechCrunch – Codex Windows](https://techcrunch.com/2026/04/16/openai-takes-aim-at-anthropic-with-beefed-up-codex-that-gives-it-more-power-over-your-desktop/)*

### Microsoft lanceert drie eigen modellen
Microsoft presenteerde drie volledig in-house ontwikkelde foundation models: een state-of-the-art spraaktranscriptiesysteem, een stemgenerator, en een vernieuwde beeldgenerator. Dit is het meest concrete bewijs tot nu toe dat Microsoft zelf wil meespelen op modelniveau – niet alleen als distributiekanaal voor OpenAI.

*Bron: [VentureBeat – Microsoft modellen](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)*

---

## 🏛️ Governance & Ethiek

### EU AI Act: eindspurt richting augustus 2026
De volledige toepasselijkheid van de AI Act gaat in op **2 augustus 2026**. In de tussentijd bereidt de AI Office richtlijnen voor over high-risk classificatie, transparantieverplichtingen en incidentrapportage. Elke EU-lidstaat moet uiterlijk dan een nationale AI-sandbox hebben opgezet. De tweede bijeenkomst van de GPAI Code of Practice Signatory Taskforce vond plaats op 13 maart 2026.

*Bronnen: [artificialintelligenceact.eu – tijdlijn](https://artificialintelligenceact.eu/implementation-timeline/) | [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)*

### Anthropic-Trump: politieke dimensie van Mythos
Anthropic-medeoprichter heeft bevestigd dat het bedrijf de Trump-administratie heeft gebrieft over Mythos. Berichten duiken op dat Trump-officials banken aanmoedigen het model te testen. De relatie tussen Anthropic en de regering lijkt te verbeteren – relevant voor wie de geopolitieke toegang tot frontier-AI wil volgen.

*Bronnen: [TechCrunch – briefing Trump](https://techcrunch.com/2026/04/14/anthropic-co-founder-confirms-the-company-briefed-the-trump-administration-on-mythos/) | [TechCrunch – relatie ontdooit](https://techcrunch.com/2026/04/18/anthropics-relationship-with-the-trump-administration-seems-to-be-thawing/)*

### Nederland: Digitale Dienst en AI-gigafabriek
Het coalitieakkoord voorziet in een **Nederlandse Digitale Dienst** die de overheidsafhankelijkheid van externe IT-leveranciers moet verminderen en verantwoorde AI-inzet moet borgen. Het kabinet steekt geen geld in de Rotterdamse AI-gigafabriek, maar financiert wel een kleinere AI-supercomputer en expertisecentrum in Groningen voor pre-competitief AI-onderzoek.

*Bronnen: [Computable – NDD coalitieakkoord](https://www.computable.nl/2026/01/30/coalitieakkoord-nederlandse-digitale-dienst-spil-in-vernieuwing-rijksdienst/) | [Computable – Rotterdam gigafabriek](https://www.computable.nl/2026/03/31/kabinet-steekt-geen-geld-in-rotterdamse-ai-gigafabriek/)*

---

## 🔐 Security & Risk

### Prompt injection blijft structureel probleem
OpenAI heeft officieel erkend dat prompt injection "waarschijnlijk nooit volledig opgelost zal worden" – vergelijkbaar met social engineering en phishing op het web. Recente gevallen: GeminiJack (gevoelige data via gedeeld Google Doc), OpenClaw (data-exfiltratie via link previews in Telegram/Discord), en IDEsaster (30+ kwetsbaarheden in Cursor, Copilot, Windsurf, Kiro.dev e.a.).

Naarmate agents meer acties uitvoeren en meer data raadplegen, neemt het aanvalsoppervlak toe. Gelaagde verdediging – sandboxing, minimale permissies, human-in-the-loop voor kritieke acties – blijft de enige werkbare aanpak.

*Bronnen: [The Hacker News – OpenClaw](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html) | [Schneier – prompt injection](https://www.schneier.com/blog/archives/2026/01/why-ai-keeps-falling-for-prompt-injection-attacks.html) | [TechCrunch – OpenAI standpunt](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)*

---

## 📈 Markt & Adoptie

### Cloud hyperscalers: groei versnelt verder
Microsoft Azure (+39% YoY), Google Cloud (+50% YoY) en AWS (+24% YoY) rapporteren sterke groeicijfers, gedreven door AI-infrastructuurvraag. Gezamenlijk investeren de drie meer dan **$500 miljard** aan capex in FY2026 voor AI-infrastructuur.

Microsoft en Google domineren volgens CIO Dive de enterprise AI-markt: Microsoft via partner- en platformecosysteem, Google via geïntegreerde agentic AI stack.

*Bronnen: [CIO Dive – marktleiderschap](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [CIO Dive – cloud groei](https://www.ciodive.com/news/cloud-infrastructure-spend-rises/816003/)*

### Nvidia: enterprise AI agent platform met 17 adopters
Nvidia lanceerde een enterprise AI agent platform met Adobe, Salesforce en SAP als een van de zeventien vroege adopters. Dit versterkt Nvidia's positie als infrastructuurlaag onder de groeiende markt voor agentic enterprise AI.

*Bron: [VentureBeat – Nvidia platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)*

---

## 💡 Ctac-relevantie

**Project Glasswing / Mythos** is direct relevant voor Ctac's security-propositie: klanten in overheid, finance en zorg zoeken naar AI-gestuurde kwetsbaarheidsdetectie. Ctac kan hier een concrete rol spelen als implementatiepartner of adviespartij, zeker nu CrowdStrike en Palo Alto – partners die ook in de Ctac-wereld actief zijn – meedoen aan Glasswing.

**GPT-5.4 met computer-use + Codex op Windows** maakt de komende maanden een golf van agentic enterprise-pilots realistisch. Ctac's AI-unit kan nu concreet demos en proof-of-concepts bouwen rondom geautomatiseerde werkprocessen (document workflows, softwareontwikkeling, back-office automatisering) met behulp van Codex of vergelijkbare tooling.

**EU AI Act augustus 2026**: klanten die nog geen compliance-traject lopen beginnen tijd tekort te komen. Er ligt een directe kans voor een aanpak op het gebied van AI-register, risicoclassificatie en governance-inrichting – zowel voor overheids- als enterprise-klanten. Ctac moet dit actief in de markt zetten.

**Nederlandse Digitale Dienst** biedt potentieel voor Ctac's overheidsklanten: de nadruk op minder leveranciersafhankelijkheid en verantwoord AI-gebruik sluit aan bij de expertise die Ctac kan bieden op het gebied van custom AI-oplossingen en architectuuradvies.

---

## 📚 Bronnen & verder lezen

- [Anthropic Mythos Preview – red.anthropic.com](https://red.anthropic.com/2026/mythos-preview/)
- [TechCrunch – Anthropic Mythos & Project Glasswing](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [TechCrunch – Is Anthropic limiting Mythos?](https://techcrunch.com/2026/04/09/is-anthropic-limiting-the-release-of-mythos-to-protect-the-internet-or-anthropic/)
- [TechCrunch – Anthropic-Trump relatie](https://techcrunch.com/2026/04/18/anthropics-relationship-with-the-trump-administration-seems-to-be-thawing/)
- [VentureBeat – Project Glasswing](https://venturebeat.com/technology/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release)
- [OpenAI – GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)
- [TechCrunch – OpenAI Codex Windows](https://techcrunch.com/2026/04/16/openai-takes-aim-at-anthropic-with-beefed-up-codex-that-gives-it-more-power-over-your-desktop/)
- [VentureBeat – Microsoft eigen modellen](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act richtlijnen](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Computable – Nederlandse Digitale Dienst](https://www.computable.nl/2026/01/30/coalitieakkoord-nederlandse-digitale-dienst-spil-in-vernieuwing-rijksdienst/)
- [Computable – Rotterdam gigafabriek](https://www.computable.nl/2026/03/31/kabinet-steekt-geen-geld-in-rotterdamse-ai-gigafabriek/)
- [The Hacker News – OpenClaw prompt injection](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html)
- [Schneier on Security – prompt injection](https://www.schneier.com/blog/archives/2026/01/why-ai-keeps-falling-for-prompt-injection-attacks.html)
- [CIO Dive – enterprise AI marktleiders](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [VentureBeat – Nvidia enterprise agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
