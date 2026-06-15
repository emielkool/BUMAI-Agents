---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-17
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 17 mei 2026

## 🔑 Highlights van de dag

- **Anthropic Mythos & Project Glasswing:** Anthropic's krachtigste model tot nu toe identificeerde duizenden zero-day kwetsbaarheden in alle grote besturingssystemen en browsers – maar is te gevaarlijk voor publieke release. Een ongeautoriseerde groep heeft er al toegang toe weten te krijgen.
- **EU AI omnibus akkoord (7 mei):** De EU bereikte een politiek akkoord om de AI Act-implementatie te vereenvoudigen. Volledige handhaving van GPAI-aanbieders start 2 augustus 2026 – minder dan 3 maanden weg.
- **Microsoft M365 E7 + Agent 365 live (1 mei):** Microsoft's enterprise AI-bundel is uit preview; binnen twee maanden stonden al tientallen miljoenen agents in de Agent 365 Registry. Shadow AI is nu een bestuursvraagstuk.
- **Prompt injection: structureel onoplosbaar:** OpenAI en de beveiligingsgemeenschap erkennen dat prompt injection bij autonome agents nooit volledig te elimineren is. Slechts een derde van organisaties heeft actieve verdediging ingericht.
- **Google Agentic Data Cloud + Gemini Enterprise Agent Platform:** Google positioneert zijn clouddataplatform als redeneermotor voor enterprise AI-agents – directe concurrent van Microsoft's Agent 365.

---

## 🧠 Technologie & Modellen

**Claude Opus 4.7 algemeen beschikbaar**
Anthropic heeft Claude Opus 4.7 uitgerold via de API, Amazon Bedrock, Google Cloud Vertex AI en Microsoft Foundry, tegen dezelfde prijzen als Opus 4.6 ($5/M input, $25/M output). Incrementele verbetering; geen paradigmaverschuiving.
*Bron: [Anthropic](https://www.anthropic.com/news/claude-opus-4-7)*

**Claude Mythos Preview – de eerste 'gevaarlijke' release**
Anthropic's nieuwste frontier model scoort 83,1% op CyberGym (vs. 66,6% voor Opus 4.6) en 93,9% op SWE-bench Verified. Het model vond duizenden zero-day kwetsbaarheden in elk groot OS en elke browser. Anthropic beperkt toegang bewust tot 40 partners (o.a. Amazon, Apple, Microsoft, CrowdStrike) via Project Glasswing en investeert $100M in credits + $4M in open-source security. Eind april bleek een ongeautoriseerde groep toch toegang te hebben.
*Bronnen: [TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) | [The Hacker News](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) | [Anthropic Glasswing](https://www.anthropic.com/glasswing)*

**OpenAI GPT-5.3 Codex**
OpenAI lanceerde GPT-5.3 Codex, 25% sneller dan zijn voorganger en het eerste model dat "instrumenteel was bij zijn eigen creatie" – een interessante symbolische claim die de aandacht vraagt voor de self-improvement-trajectorie.
*Bron: [OpenAI News](https://openai.com/news/)*

**Agentische OS: Microsoft + Salesforce**
Microsoft herstructureert Windows als "agentic OS" voor autonome agents op enterprise-schaal. Salesforce lanceerde Agentforce 2dx voor autonome, proactieve bedrijfsprocessen. OpenAI's Agentic AI Foundation is ondergebracht bij de Linux Foundation voor gedeelde, neutrale agent-infrastructuur.
*Bronnen: [VentureBeat – Microsoft](https://venturebeat.com/ai/microsoft-remakes-windows-for-an-era-of-autonomous-ai-agents) | [VentureBeat – Salesforce](https://venturebeat.com/ai/salesforce-launches-agentforce-2dx-pushing-autonomous-ai-deep-into-enterprise-workflows)*

---

## 🏛️ Governance & Ethiek

**EU AI omnibus: vereenvoudiging op komst**
Op 7 mei 2026 bereikte de EU een politiek akkoord over de 'AI omnibus' die de implementatie van de AI Act moet stroomlijnen en innovatie moet stimuleren. Tegelijk wordt een verbod op 'nudification'-apps ingevoerd. Volledig toepasselijk per 2 augustus 2026; Commissie-handhavingsbevoegdheden voor GPAI-aanbieders gaan dan ook in.
*Bronnen: [EU AI Act tracker](https://artificialintelligenceact.eu/) | [Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)*

**Nederland en België: adoptie en governance divergeren**
Nederland zet slechts 16% van bedrijven strategisch in op AI (UK: 36%); meer dan een derde van medewerkers weet niet of ze AI mogen gebruiken op het werk. België doet het beter: 34,5% van bedrijven met 10+ medewerkers gebruikt actief AI, met 40% groei jaar-op-jaar. Benelux loopt volgens recent onderzoek voorop in de Europese AI-adoptie, maar governance blijft het zwakke punt in Nederland.
*Bronnen: [Computable.nl – adoptie](https://www.computable.nl/2025/10/24/nederlandse-it-afdelingen-worstelen-met-ai-adoptie/) | [Data News – België](https://datanews.knack.be/analyse/ai-gebruik-in-belgische-bedrijven-blijft-toenemen-al-1-op-de-3-ondernemingen-zet-ai-actief-in/)*

---

## 🔐 Security & Risk

**Prompt injection: structureel onoplosbaar bij agents**
OpenAI erkent officieel: "The nature of prompt injection makes deterministic security guarantees challenging." Drie AI-coding agents lekten recentelijk geheimen via één enkele prompt-injection, terwijl slechts 34,7% van organisaties actieve verdediging heeft. De verschuiving van copilots naar autonome agents vergroot het aanvalsoppervlak fundamenteel.
*Bronnen: [VentureBeat – prompt injection](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay) | [VentureBeat – runtime attacks](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)*

**Anthropic MCP kwetsbaarheid**
Een ontwerpfout in Anthropic's Model Context Protocol (MCP) maakt Remote Code Execution mogelijk, met risico's voor de AI-supply chain. Kritisch voor organisaties die Claude-integraties bouwen.
*Bron: [The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)*

**NSA gebruikt Anthropic Mythos**
Ondanks interne spanning met het Pentagon gebruiken de NSA Mythos actief voor inlichtingenwerk. Dit illustreert de dual-use realiteit van frontier cybersecurity-modellen en de gouvernance-uitdaging rond gecontroleerde toegang.
*Bron: [TechCrunch](https://techcrunch.com/2026/04/20/nsa-spies-are-reportedly-using-anthropics-mythos-despite-pentagon-feud/)*

---

## 📈 Markt & Adoptie

**Microsoft M365 E7 + Agent 365: GA per 1 mei 2026**
Microsoft's Frontier Suite bundelt M365 E5, Copilot en Agent 365 voor €99/gebruiker/maand. Agent 365 (€15/gebruiker) biedt IT en security één controlepunt voor alle agents. In twee maanden preview: tientallen miljoenen agents in de registry, 500.000+ agents zichtbaar bij Microsoft zelf.
*Bronnen: [Microsoft Blog](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/) | [VentureBeat – Agent 365](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)*

**Google Agentic Data Cloud + Gemini Enterprise Agent Platform**
Google positioneert zijn Vertex AI-platform als redeneermotor voor enterprise-agents. Agentic Data Cloud, gelanceerd op Google Cloud Next '26, is ontworpen om legacy dataplatformen om te zetten in AI-reasoning engines. De no-code Agent Designer maakt agent-bouw toegankelijk zonder code.
*Bronnen: [CIO Dive – Google](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/) | [Google Blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/next-2026/)*

**Google investeert $40 miljard in Anthropic**
Google's meest recente committering bevestigt dat Anthropic de sleutelrol speelt in Google's AI-strategie, inclusief 5 gigawatt compute-capaciteit voor de komende vijf jaar.
*Bron: [TechCrunch](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)*

---

## 💡 Ctac-relevantie

**Agent governance is nu een verkooparticulatie.** De lancering van Microsoft Agent 365 en de zichtbare "shadow AI"-problematiek bij enterprise-klanten creëren een directe aanleiding voor Ctac om governance-diensten rond AI-agents te positioneren. Klanten in finance, overheid en zorg staan voor dezelfde vraag: hoe beheers je tientallen (of duizenden) agents die autonoom handelen in bedrijfsprocessen? Ctac kan hier als implementatie- en governancepartner optreden, zowel voor Microsoft-omgevingen als platform-agnostisch.

**EU AI Act-deadline nadert snel (2 augustus 2026).** Met minder dan drie maanden tot volledige handhaving is dit het moment om bestaande klantgesprekken te structureren rond compliance-readiness, met name voor klanten die GPAI-modellen inzetten of ontwikkelen. De AI omnibus vereenvoudigt de regels maar neemt de verplichtingen niet weg.

**Security rondom MCP en agent-integraties is een acuut aandachtspunt.** Teams die Claude of andere LLMs via MCP integreren in klantoplossingen moeten de recent ontdekte RCE-kwetsbaarheid meenemen in hun risicobeoordeling. Prompt injection bij autonome agents vraagt om expliciete architectuurkeuzes, niet om een vinkje in de checklist.

---

## 📚 Bronnen & verder lezen

- [Anthropic – Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [Anthropic – Project Glasswing](https://www.anthropic.com/glasswing)
- [TechCrunch – Anthropic Mythos preview](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [TechCrunch – Mythos ongeautoriseerde toegang](https://techcrunch.com/2026/04/21/unauthorized-group-has-gained-access-to-anthropics-exclusive-cyber-tool-mythos-report-claims/)
- [TechCrunch – Google $40B investering Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [Microsoft Blog – Frontier Suite aankondiging](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)
- [Microsoft Blog – Frontier Firms operating model](https://blogs.microsoft.com/blog/2026/05/05/how-frontier-firms-are-rebuilding-the-operating-model-for-the-age-of-ai/)
- [VentureBeat – Microsoft Agent 365 GA](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Google Cloud Next '26 recap](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/google-cloud-next-26-recap/)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [Europese Commissie – AI Act governance](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [VentureBeat – prompt injection blijft bestaan](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [VentureBeat – AI coding agents en prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [The Hacker News – Anthropic MCP kwetsbaarheid](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)
- [The Hacker News – Mythos zero-day vondsten](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
- [Computable.nl – Nederlandse AI-adoptie](https://www.computable.nl/2025/10/24/nederlandse-it-afdelingen-worstelen-met-ai-adoptie/)
- [Data News – Belgische AI-adoptie](https://datanews.knack.be/analyse/ai-gebruik-in-belgische-bedrijven-blijft-toenemen-al-1-op-de-3-ondernemingen-zet-ai-actief-in/)
