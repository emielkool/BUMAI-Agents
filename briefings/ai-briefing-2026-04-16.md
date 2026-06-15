---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-16
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 16 april 2026

## 🔑 Highlights van de dag

- **Anthropic Project Glasswing**: Mythos, Anthropics krachtigste model ooit, identificeerde autonoom duizenden zero-day kwetsbaarheden in alle grote besturingssystemen en browsers — een keerpunt voor AI in defensieve cybersecurity, maar ook een waarschuwing voor het aanvalslandschap.
- **Stanford AI Index 2026**: SWE-bench codeerprestaties stegen van 60% naar bijna 100% in één jaar; 88% van organisaties gebruikt AI; de VS-China modelkloof is met nog maar 2,7% vrijwel gedicht.
- **Open-weight concurrentie versherpt**: Arcee AI's Trinity (400B) en Zhipu's GLM-4.6V (106B) dagen Meta's Llama-dominantie uit; het open-source landschap is uitgegroeid tot een multipolaire strijd.
- **Shadow AI als enterprise-risico**: Werknemers die AI-tools buiten IT-goedkeuring gebruiken creëren groeiende blinde vlekken — zeker met de opkomst van autonome AI-agents.
- **EU AI Act praktijk**: Ondersteuningsmaterialen voor high-risk compliance komen Q2 2026; AI voor wervingsscreening valt al per 17 maart formeel onder high-risk.

---

## 🧠 Technologie & Modellen

**Anthropic Claude Mythos Preview – Project Glasswing**
Anthropic onthulde een beperkte preview van Claude Mythos, zijn meest capabele model tot nu toe, specifiek ingezet voor defensieve cybersecurity via Project Glasswing. In de aanloop vond Mythos autonoom duizenden eerder onbekende zero-days in elk groot besturingssysteem en elke grote browser — inclusief een 17 jaar oud remote code execution-lek in FreeBSD. Het model is (vooralsnog) niet publiek beschikbaar; 12 lanceringspartners — waaronder Amazon, Apple, Cisco, CrowdStrike, Google, Microsoft en NVIDIA — krijgen toegang. Anthropic investeert $100 miljoen aan usage credits en $4 miljoen in open-source securityorganisaties. Het is een bewust beperkte release: vergelijkbare modellen komen onvermijdelijk ook in handen van aanvallers.
*(Bronnen: [Anthropic/glasswing](https://www.anthropic.com/glasswing), [TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/), [The Hacker News](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html))*

**Stanford AI Index 2026**
Het Stanford HAI publiceerde zijn jaarlijkse AI Index. Opvallendste bevindingen: SWE-bench codeerscores stegen van 60% naar bijna 100% in één jaar; het beste VS-model (Claude Opus 4.6, score 1.503 op Arena) leidt nog maar met 2,7% op ByteDance's Dola-Seed Preview. Organisatorische adoptie staat op 88%. Kanttekening: Foundation Model Transparency Index daalt van 58 naar 40 punten — frontier labs worden minder open over trainingsdata en parameters.
*(Bronnen: [Stanford HAI](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report), [TechCrunch](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/), [IEEE Spectrum](https://spectrum.ieee.org/state-of-ai-index-2026))*

**Open-weight modellen: multipolaire concurrentie**
De dominantie van Meta's Llama staat steeds meer onder druk. Arcee AI (26 medewerkers) lanceerde Trinity, een 400B-parameter open-weight model onder Apache-licentie — de grootste open-weight release ooit van een niet-Chinees bedrijf. Zhipu AI's GLM-4.6V (106B, native tool-calling, 128K context) scoort state-of-the-art op meer dan 20 benchmarks. Microsoft lanceerde drie eigen modellen (MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2) via Microsoft Foundry — een signaal dat het zich minder wil afhangen van OpenAI.
*(Bronnen: [TechCrunch/Arcee](https://techcrunch.com/2026/04/07/i-cant-help-rooting-for-tiny-open-source-ai-model-maker-arcee/), [VentureBeat/GLM](https://venturebeat.com/ai/z-ai-debuts-open-source-glm-4-6v-a-native-tool-calling-vision-model-for), [VentureBeat/Microsoft](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google))*

---

## 🏛️ Governance & Ethiek

**EU AI Act — Q2 2026 cruciale fase**
De Europese Commissie werkt aan praktische implementatiegidsen voor high-risk classificatie, transparantievereisten en incidentrapportage; publicatie verwacht in het tweede kwartaal van 2026. Elke lidstaat dient vóór 2 augustus 2026 een nationale AI regulatory sandbox te hebben. Praktisch al van kracht: per 17 maart 2026 zijn AI-tools voor kandidaatscreening en -ranking formeel aangemerkt als high-risk systemen.

De dalende transparantiescore in het Stanford-rapport (van 58 naar 40 op de Foundation Model Transparency Index) vergroot de compliance-druk voor organisaties die closed-source frontier models inzetten: minder inzicht in trainingsbronnen maakt auditbaarheid moeilijker.
*(Bronnen: [EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/), [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines))*

---

## 🔐 Security & Risk

**Project Glasswing als tweesnijdend zwaard**
Mythos laat zien dat AI-modellen het niveau hebben bereikt waarop ze beter zijn dan vrijwel alle mensen in het vinden én exploiteren van kwetsbaarheden. De beperkte release is een bewuste keuze: defensieve partijen krijgen een voorsprong voordat vergelijkbare modellen breed beschikbaar worden. Schneier schrijft kritisch over de implicaties voor offensieve overheidscapaciteiten.
*(Bron: [Schneier on Security](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html))*

**Shadow AI — blinde vlekken in enterprise**
Medewerkers nemen AI-tools in gebruik buiten formele IT-goedkeuring, wat "shadow AI" creëert. Met de opkomst van autonome AI-agents die zelfstandig acties uitvoeren in meerdere applicaties, groeien de verborgen aanvalsoppervlakken exponentieel. Dit is geen theoretisch risico meer.
*(Bron: [The Hacker News](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html))*

**LangChain/LangGraph-kwetsbaarheden**
Drie beveiligingsfouten in deze populaire LLM-frameworks stellen bestanden, environment secrets en databaseinhoud bloot bij miljoenen deployments. Relevant voor iedereen die LLM-applicaties bouwt op deze stacks.
*(Bron: [The Hacker News](https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html))*

**CISA: zes actief geëxploiteerde kwetsbaarheden**
CISA plaatste zes nieuwe kwetsbaarheden (Fortinet, Microsoft, Adobe) op de Known Exploited Vulnerabilities-lijst; patching vereist vóór 27 april voor federale instanties.
*(Bron: [The Hacker News](https://thehackernews.com/2026/04/cisa-adds-6-known-exploited-flaws-in.html))*

---

## 📈 Markt & Adoptie

**Adoptiesnelheid en ongelijke verdeling**
88% van organisaties gebruikt AI (Stanford); maar de economische winst concentreert zich: 75% gaat naar 20% van de bedrijven (PwC AI Performance Study 2026). Dat is niet per se hype — het is een patroon dat ook bij eerdere technologiegolven zichtbaar was. De uitdaging: bij de kopgroep horen.

**Microsoft vs. Google in enterprise**
Microsoft domineert qua ecosysteem en marktpositie; Google wint terrein in agentic AI via het A2A-protocol (Agent-to-Agent interoperabiliteit). Gartner voorspelt dat 40% van enterprise-applicaties eind 2026 task-specific AI agents bevat, tegenover minder dan 5% in 2025 — een vertienvoudiging in één jaar.
*(Bronnen: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/), [PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html))*

---

## 💡 Ctac-relevantie

**AI voor defensieve security — concrete propositie**
Project Glasswing is geen abstracte R&D-aankondiging: het laat zien dat AI-gedreven vulnerability hunting nu productierijp is bij toonaangevende techbedrijven. Voor Ctac's klanten in finance, overheid en industrie is dit een direct gesprek waard — zowel over de kansen (proactieve security) als de risico's (wanneer aanvallers vergelijkbare tools gebruiken). Ctac's AI-unit kan dit als inhoudelijk anker gebruiken in klantgesprekken.

**Shadow AI governance — directe dienstverlening**
De shadow AI-problematiek biedt een concrete propositiekans: veel middelgrote organisaties in Nederland en België hebben geen beleid voor AI-tool gebruik. Ctac kan helpen met een AI governance framework, tooling-selectie en medewerkerstraining — zonder dat dit een groot transformatietraject hoeft te zijn.

**EU AI Act compliance — HR-tools zijn nu high-risk**
Klanten die AI inzetten voor werving, screening of personeelsbeoordeling moeten dit nu formeel als high-risk classificeren. Dit is een direct en afgebakend compliance-adviestraject voor Ctac, met name relevant voor klanten in de publieke sector en finance.

**Open-weight modellen als alternatief voor compliance**
De dalende transparantie bij gesloten frontier labs (Foundation Model Transparency Index van 58 naar 40) maakt open-weight modellen aantrekkelijker voor klanten met strenge compliance- of data-residency-eisen. Ctac kan hierop inspelen door sovereign/private AI-deployment als propositie te versterken.

---

## 📚 Bronnen & verder lezen

- [Anthropic – Project Glasswing](https://www.anthropic.com/glasswing)
- [Anthropic – Mythos Preview](https://red.anthropic.com/2026/mythos-preview/)
- [TechCrunch – Anthropic Mythos debut](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [The Hacker News – Mythos zero-days](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
- [Schneier on Security – Glasswing analyse](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html)
- [Stanford HAI – AI Index 2026 (12 takeaways)](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report)
- [TechCrunch – Stanford rapport: insiders vs. publiek](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)
- [IEEE Spectrum – State of AI 2026](https://spectrum.ieee.org/state-of-ai-index-2026)
- [TechCrunch – Arcee AI Trinity](https://techcrunch.com/2026/04/07/i-cant-help-rooting-for-tiny-open-source-ai-model-maker-arcee/)
- [VentureBeat – Zhipu GLM-4.6V](https://venturebeat.com/ai/z-ai-debuts-open-source-glm-4-6v-a-native-tool-calling-vision-model-for)
- [VentureBeat – Microsoft MAI-modellen](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [The Hacker News – Shadow AI risico's](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html)
- [The Hacker News – LangChain kwetsbaarheden](https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html)
- [The Hacker News – CISA 6 kwetsbaarheden](https://thehackernews.com/2026/04/cisa-adds-6-known-exploited-flaws-in.html)
- [EU AI Act – implementatie-tijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act implementatiegidsen](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [CIO Dive – Microsoft/Google enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [PwC – 2026 AI Performance Study](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html)
