---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-13
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 13 november 2026

## 🔑 Highlights van de dag

- **Drie grote modellen in vier dagen:** Google (Gemini 4 Carbon, 10 nov), Anthropic (Claude Fable 5.2, 9 nov) en OpenAI (GPT Image 2.6, 4 nov) lanceerden elk een nieuw product – een compressie van releases die illustreert hoe competitief de frontier nu is.
- **EU AI Act: transparantieregels voor generatieve AI gepubliceerd.** De Commissie publiceerde op 12 november haar Article 50-richtsnoeren in het Publicatieblad. Deadline voor naleving (synth. content markering) volgt op 2 december 2026.
- **Microsoft Ignite (12 nov) zet AI-agents centraal.** Microsoft-aandeel steeg op verwachting van verdere groei van Copilot en Agent 365; 30 miljoen betaalde Copilot-seats bereikt in FY2026.
- **Prompt injection blijft dé zwakte van agentische AI.** OWASP bevestigt het als LLM01, en in 2025 werden al meer dan 90 organisaties actief aangevallen via inject-aanvallen in productieomgevingen.
- **Governance-kloof vergroot bij agent-deployments.** Gartner voorspelt 40% enterprise-app-penetratie van agents eind 2026, maar slechts 21% van organisaties heeft een volwassen governance-model.

## 🧠 Technologie & Modellen

**Google Gemini 4 Carbon** (10 nov) wordt door Google gepositioneerd als zijn meest capabele model tot nu toe, boven Gemini 4 Argon. Details over benchmarks zijn nog schaars; check Google's officiële blog voor technische specificaties.

**Anthropic Claude Fable 5.2** (9 nov) is het nieuwste lid van de Claude 5-familie, met een context-window van 1 miljoen tokens. Tegelijkertijd lanceerde Anthropic Claude Mythos 5.2 en drie Workspace-producten: Claude Sheets, Claude Meetings en Claude Whiteboards – een directe aanval op het Microsoft 365- en Google Workspace-segment.

**OpenAI GPT Image 2.6** (4 nov) brengt twee varianten (Sunburst en Flare), 50% sneller dan zijn voorganger, met GIF-ondersteuning toegevoegd. GPT-5.5 en ChatGPT Finances (koppeling US-bankrekening, voice) zijn ook recent uitgebreid.

*Noot:* Berichten dat OpenAI GPT-6 Astra AGI zou zijn, zijn niet bevestigd vanuit primaire bron. Treat as hype totdat OpenAI zelf communiceert.

Bronnen: [LLM Gateway timeline](https://llmgateway.io/timeline) · [AI Weekly – Anthropic news](https://aiweekly.co/ai-news-today/anthropic-news) · [November AI news overzicht](https://blog.mean.ceo/latest-ai-announcements-news-november-2026/)

## 🏛️ Governance & Ethiek

**EU AI Act – Article 50 transparantierichtsnoeren gepubliceerd.** Op 5 november adopteerde de Commissie haar richtsnoeren (C(2026) 7702 final) voor het markeren van AI-gegenereerde content; publicatie in het Publicatieblad volgde op 12 november. Vanaf **2 december 2026** moeten generatieve AI-systemen die al op de EU-markt zijn, voldoen aan de markeerplicht voor synthetische content en gelden nieuwe verboden op non-consensueel intiem beeldmateriaal.

Hoge-risico verplichtingen (standalone AI-systemen) zijn via de Digital Omnibus (Verordening EU 2026/1744) uitgesteld tot **2 december 2027**; voor AI ingebed in producten geldt 2 augustus 2028. De AI Office en nationale autoriteiten zijn actief als toezichthouder sinds 2 augustus 2026.

Eerste geharmoniseerde norm EN 18286:2026 (kwaliteitsmanagementsystemen voor aanbieders van hoge-risico AI) is gepubliceerd in het Publicatieblad.

Bronnen: [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [CASRAI – Art. 50 deadline](https://casrai.org/news/eu-ai-act-2-december-2026-obligations-article-50) · [i-scoop.eu – Digital Omnibus tijdlijn](https://www.i-scoop.eu/eu-ai-act-timeline-digital-omnibus/)

## 🔐 Security & Risk

**Prompt injection domineert agentische AI-risico's.** OWASP classificeert het als LLM01; CrowdStrike's Global Threat Report 2026 meldt dat kwaadwillenden in 2025 meer dan 90 organisaties actief aanvielen via geïnjected prompts in legale generatieve AI-tools.

Concrete kwetsbaarheid: **CVE-2025-53773** (GitHub Copilot) stond toe dat verborgen instructies in pull request-beschrijvingen remote code execution inleidden – CVSS-score 9.6. OpenAI heeft erkend dat prompt injection in AI-browsers mogelijk nooit volledig te patchen is.

Breder: agents met brede permissies, onveilige MCP-koppelingen en gebrek aan traceerbaarheid van acties zijn nieuwe aanvalsvectoren. Agents die toegang hebben tot privé-data én externe communicatie kunnen via één injected prompt als exfiltratietool worden ingezet.

Bronnen: [Help Net Security – OWASP rapport](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) · [Vectra – CVE-overzicht](https://www.vectra.ai/topics/prompt-injection) · [VentureBeat – agent attack surfaces](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)

## 📈 Markt & Adoptie

**Microsoft** bereikte 30 miljoen betaalde Copilot-seats in FY2026, met een duidelijke verschuiving van assistent naar agentisch platform. **Agent 365** (algemeen beschikbaar per 1 mei) stelt IT-afdelingen in staat om AI-agents te ontdekken, beheren en beveiligen over Microsoft-, SaaS- en cloud-omgevingen heen. Op Ignite (12 nov) lag de nadruk op Copilot, agents en Azure AI-infrastructuur.

**Google** verving Vertex AI met Gemini Enterprise in april, lanceerde een universele Gemini-agent (private preview) en bood beheerders een gecentraliseerd AI-beheerpaneel voor Workspace.

**Anthropic** zag zijn aandeel in enterprise API-spend stijgen van 40% naar 55% (Menlo Ventures), ten koste van Google (21% → 9%). Dit suggereert dat Claude steeds meer als de default back-end keuze geldt bij enterprise-API-afnemers.

**Agent-adoptie:** Gartner voorspelt dat 40% van enterprise-applicaties eind 2026 task-specifieke agents bevat. Slechts 21% van bedrijven beschikt echter over een volwassen governance-model (Deloitte). Voornaamste hinderpaal: integratie met bestaande systemen (46% als primaire blocker).

Bronnen: [Computerworld – Microsoft/Google agent governance](https://www.computerworld.com/article/4167054/microsoft-google-push-ai-agent-governance-into-enterprise-it-mainstream.html) · [Menlo Ventures – State of Enterprise AI 2026](https://menlovc.com/perspective/2026-the-state-of-enterprise-ai/) · [Invezz – Microsoft Ignite](https://invezz.com/za/news/2026/11/12/microsoft-stock-rises-as-ignite-conference-puts-ai-growth-narrative-in-focus/) · [Suitebriar – AI agents 2026](https://www.suitebriar.com/blog/ai-agents-in-2026-where-enterprise-adoption-stands)

## 💡 Ctac-relevantie

**Drie directe aandachtspunten voor deze week:**

1. **EU AI Act naleving nadert.** De 2-december-deadline voor Article 50 (synthetische content markering) valt over drie weken. Ctac-klanten die generatieve AI-oplossingen aanbieden of inzetten moeten nu controleren of hun systemen voldoen. Dit is een concrete compliance-kans voor Ctac's advisory practice.

2. **Anthropic's Workspace-producten (Sheets, Meetings, Whiteboards) zijn een signaal.** Grote labs bewegen zich het terrein van enterprise collaboration in. Ctac kan dit als kans benutten: klanten die Microsoft 365 Copilot evalueren naast Claude-alternatieven hebben behoefte aan onafhankelijke begeleiding. Wees alert op vendor lock-in-discussies in klantgesprekken.

3. **Agent-governance is nu de bottleneck, niet technologie.** De governance-kloof (72% productie, maar 60% zonder formeel beleid) is het meest zorgwekkende cijfer van deze week. Ctac kan zich onderscheiden door niet alleen agent-implementatie te leveren maar ook het governance-raamwerk – inclusief prompt-injection-mitigaties en audittrails. Dit is een propositionele kans die aansluit op de opbouw van de AI-unit.

## 📚 Bronnen & verder lezen

- [LLM Gateway – November 2026 release timeline](https://llmgateway.io/timeline)
- [AI Weekly – Anthropic news (11 nov)](https://aiweekly.co/ai-news-today/anthropic-news)
- [Europese Commissie – EU AI Act beleidspagina](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [CASRAI – Art. 50 verplichtingen per 2 dec 2026](https://casrai.org/news/eu-ai-act-2-december-2026-obligations-article-50)
- [i-scoop.eu – Digital Omnibus en AI Act tijdlijn](https://www.i-scoop.eu/eu-ai-act-timeline-digital-omnibus/)
- [Help Net Security – OWASP prompt injection rapport](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [VentureBeat – Prompt injection in enterprise agents](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [Computerworld – Microsoft & Google agent governance](https://www.computerworld.com/article/4167054/microsoft-google-push-ai-agent-governance-into-enterprise-it-mainstream.html)
- [Menlo Ventures – State of Enterprise AI 2026](https://menlovc.com/perspective/2026-the-state-of-enterprise-ai/)
- [Invezz – Microsoft Ignite AI focus](https://invezz.com/za/news/2026/11/12/microsoft-stock-rises-as-ignite-conference-puts-ai-growth-narrative-in-focus/)
