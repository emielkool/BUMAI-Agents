---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-24
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 24 september 2026

## 🔑 Highlights van de dag

- **OpenAI GPT-6 Sol & Luna**: Afgelopen maandag (22 sept) kondigde OpenAI twee nieuwe frontier-modellen aan gericht op productiviteit; samen met GPT-6 Astra (3 sept) en GPT-Live-1 (10 sept) is september een uitzonderlijk drukke modelmaand voor OpenAI.
- **Agentic AI Foundation onder Linux Foundation**: OpenAI, Anthropic en Block richtten een neutrale stichting op voor open, interoperabele agentic AI-infrastructuur – een serieuze stap richting standaardisatie van multi-agent systemen.
- **EU AI Act in volle uitvoering**: Sinds 2 augustus 2026 zijn de AI Office en nationale autoriteiten officieel verantwoordelijk voor handhaving; de AI Omnibus (kracht vanaf 27 juli) heeft de regels voor KMO's verlicht en de rol van het AI Office versterkt.
- **Prompt injection wordt industrieel**: Drie AI coding agents (Claude Code, Gemini CLI, Copilot) werden tegelijkertijd getroffen door een gecoördineerde prompt injection-aanval; het groeiende agentic AI-landschap vergroot het aanvalsoppervlak structureel.
- **Twee derde van enterprises vast in AI-pilotfase**: Ondanks massale investeringen slagen de meeste organisaties er niet in om generatieve AI van pilot naar productie te brengen.

---

## 🧠 Technologie & Modellen

OpenAI heeft september benut om zijn modelportfolio flink uit te breiden. **GPT-6 Astra** (3 sept) positioneert OpenAI aan de frontier op coding, cybersecurity en wetenschap. Vorige week volgden **GPT-6 Sol en Luna** – twee varianten gericht op kosteneffectiviteit versus capabiliteit in dagelijkse werkomgevingen. Tussendoor introduceerde OpenAI **GPT-Live-1** voor full-duplex stemgesprekken met telephony-ondersteuning, interessant voor enterprise telefonieintegraties.

Google voegt **Gemini 3.6 Flash** toe als nieuw "workhorse model" met betere codeer- en multimodale prestaties bij lagere tokenkosten, en de **3.5 Flash-Lite** als snelste optie (350 output tokens/sec).

In open-source-land vallen op: **Agents-A1 35B** (InternScience), een Mixture-of-Experts model specifiek voor agentic workloads, en **DeepSeek V4** met 1M tokenscontextvenster. De **Agentic AI Foundation** onder de Linux Foundation – mede opgericht door OpenAI, Anthropic en Block – wil open standaarden voor agent-to-agent interoperabiliteit bevorderen, een relevante tegenhanger voor lock-in bij proprietaire platforms.

*Bronnen: [TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/) | [OpenAI GPT-6](https://openai.com/index/gpt-5-6/) | [Google Gemini 3.6 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) | [OpenAI Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/) | [HuggingFace Open LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)*

---

## 🏛️ Governance & Ethiek

De EU AI Act bevindt zich in de handhavingsfase. Vanaf **2 augustus 2026** zijn de AI Office en nationale toezichthouders officieel verantwoordelijk voor implementatie, toezicht en handhaving. De **AI Omnibus** (politiek akkoord 7 mei, in werking 27 juli 2026) heeft de regelgeving op een aantal punten verlicht voor KMO's en midcaps, de bevoegdheden van het AI Office versterkt, en de interactie tussen de AI Act en EU-productveiligheidsregels verduidelijkt.

Het **cybersecurity- en AI-actieplan** van juli 2026 biedt lidstaten, bedrijven en overheden een gecoördineerde aanpak voor de cyberrisico's van geavanceerde AI-modellen. De AI Office is momenteel bezig met de uitwerking van implementatierichtlijnen voor de rest van 2026.

*Bronnen: [EU AI Act tracker](https://artificialintelligenceact.eu/) | [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | [Governance & enforcement](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)*

---

## 🔐 Security & Risk

Prompt injection is van theoretische kwetsbaarheid naar operationele dreiging geworden. Drie bekende AI coding agents – **Claude Code, Gemini CLI en GitHub Copilot** – werden tegelijkertijd getroffen door een gecoördineerde aanval waarbij geheimen werden gelekt. VentureBeat meldt dat eerdere aanvallen bij meer dan 90 organisaties in 2025 al meetbare schade veroorzaakten.

De kern van het probleem: taalmodellen kunnen instructies en data structureel niet van elkaar onderscheiden. Elk stuk content dat een agent verwerkt, kan als instructie worden geïnterpreteerd. Naarmate agentic systemen meer rechten krijgen (file access, API calls, browsing), neemt het aanvalsoppervlak exponentieel toe. **EchoLeak (CVE-2025-32711)** – de eerste gedocumenteerde zero-click prompt injection in Microsoft 365 Copilot – bevestigt dat dit geen nicheprobleem meer is.

*Bronnen: [VentureBeat – Prompt injection 2026](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers) | [VentureBeat – AI agent audit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [Airia – AI Security 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)*

---

## 📈 Markt & Adoptie

**Microsoft en Google domineren** de enterprise AI-markt volgens een recent Gartner-rapport: Microsoft via zijn Copilot-ecosysteem en Azure, Google via zijn geïntegreerde Gemini-stack voor agentic enterprise. SAP verenigt zijn business technology, data cloud en AI-aanbod in het **SAP Business AI Platform** en introduceert de **Autonomous Suite** met AI-agents bovenop bestaande SAP-applicaties.

Ondanks dit geweld: **twee derde van bedrijven** geeft aan vastgelopen te zijn in de pilotfase. De kloof tussen experiment en productie is structureel. Accenture en Anthropic kondigden een gezamenlijke aanpak aan voor intensieve veiligheidstesting van AI-modellen in enterprise-context.

In Nederland: Eindhovens AI-chipbedrijf **Euclyd** haalde meer dan €200 miljoen op voor energiezuinige inferentie-chips. Oud-ASML-CEO Peter Wennink is voorzitter van de raad van commissarissen geworden. Tegelijkertijd meldt Computable dat steeds meer bedrijven de stekker trekken uit cloud-AI en kiezen voor eigen servers – dataprivacy als voornaamste drijfveer.

*Bronnen: [CIO Dive – Microsoft & Google](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [CIO Dive – SAP platform](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/) | [Computable – Accenture & Anthropic](https://www.computable.nl/2026/09/22/kort-18-miljoen-voor-nieuwe-zeekabel-accenture-en-anthropic-in-front-tegen-ai-risicos-en-meer/) | [Computable – Euclyd €200M](https://www.computable.nl/2026/09/16/kort-eindhovense-ai-chipmaker-haalt-200-miljoen-op-fujitsu-rust-it-support-met-agentic-ai-uit-en-meer/)*

---

## 💡 Ctac-relevantie

**Agentic AI als propositie**: De oprichting van de Agentic AI Foundation en de beschikbaarheid van productie-waardige open-source agentic modellen (Agents-A1, DeepSeek V4) maken het uitvoerbaar om klanten te begeleiden bij het bouwen van multi-agent workflows zonder volledige lock-in op één platform. Dit is een concreet differentiatiepunt voor de Ctac AI-unit.

**Prompt injection als enterprise-risico**: De aanvallen op Claude Code, Gemini CLI en Copilot zijn een directe aanleiding om bij klanten die agentic AI introduceren een beveiligingslaag te adviseren. Ctac kan hier een rol spelen door bij implementaties input-validatie, sandboxing en runtime monitoring als standaard te positioneren – niet als optie maar als vereiste.

**Kloof pilotfase → productie**: Twee derde van enterprises loopt vast. Dit is waar IT-consultancy-waarde zit: niet in het opzetten van de demo, maar in de architecturele en organisatorische begeleiding richting schaalbare AI-productie. De Microsoft AI Playbook en SAP Autonomous Suite bieden concrete invalshoeken voor klantgesprekken.

**EU AI Act compliance**: Organisaties in gereguleerde sectoren (overheid, zorg, finance) moeten nu handelen. De AI Omnibus heeft de lat voor KMO's iets lager gelegd, maar de handhaving is actief. Ctac kan compliance-scans en risicoclassificatie positioneren als eerste stap in een bredere AI-dienstverlening.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI GPT-6 model family](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [OpenAI – GPT-6 Sol & Luna aankondiging](https://openai.com/index/gpt-5-6/)
- [Google Blog – Gemini 3.6 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)
- [OpenAI – Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/)
- [HuggingFace – Best Open-Source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [EC – AI Act governance and enforcement](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – AI agent runtime security audit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Airia – AI Security in 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Microsoft & Google enterprise AI dominance](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – SAP Business AI Platform](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [Computable – Accenture & Anthropic AI-risico's](https://www.computable.nl/2026/09/22/kort-18-miljoen-voor-nieuwe-zeekabel-accenture-en-anthropic-in-front-tegen-ai-risicos-en-meer/)
- [Computable – Euclyd €200M chipmaker](https://www.computable.nl/2026/09/16/kort-eindhovense-ai-chipmaker-haalt-200-miljoen-op-fujitsu-rust-it-support-met-agentic-ai-uit-en-meer/)
