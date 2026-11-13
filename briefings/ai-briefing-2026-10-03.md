---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-03
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 3 oktober 2026

## 🔑 Highlights van de dag

- **Google lanceert Gemini 4 Argon**, nu beschreven als het krachtigste model in de Gemini-lijn. Parallel kondigt OpenAI de definitieve pricing voor GPT-Rosalind (life sciences reasoning model) aan per 5 oktober.
- **EchoLeak treft enterprise Copilot**: de eerste zero-click agentische kwetsbaarheid in een productie-enterprise-systeem is gedocumenteerd — een aanvaller stuurt een kwaadaardig e-mailbericht en Copilot exfiltreert gevoelige data zodra een gebruiker een vraag stelt, zonder klik. Relevant voor iedere Ctac-klant met M365 Copilot.
- **EU AI Act Article 50 actief**: transparantievereisten voor providers en deployers van generatieve AI zijn per 2 augustus 2026 van kracht; de volgende deadline (verbod op deepfakes/CSAM) volgt op 2 december 2026.
- **Microsoft Copilot overschrijdt 30 miljoen betaalde seats**: het meest concrete bewijs van enterprise AI-adoptie op schaal. Microsoft lanceert tegelijk *Microsoft Frontier Company* — 6.000 embedded engineers bij klanten.
- **Nederland investeert €120 miljoen in industriële AI** via deelname aan EU Ipcei-AI; overheid introduceert ook *Vlam*, een eigen veilig AI-model onder Nederlands beheer.

## 🧠 Technologie & Modellen

**Google Gemini 4 Argon** werd begin oktober 2026 gelanceerd als opvolger van Gemini 3 en wordt door Google gepresenteerd als het krachtigste model in de lijn. Details over context window en benchmarks zijn nog beperkt beschikbaar, maar eerste vergelijkingen met GPT-6.1 Sol circuleren.

**OpenAI GPT-6.1 Sol** (uitgebracht 29 september) kreeg een globale usage-reset op 2 oktober na prestatieverstoringen door hoge load bij de lancering. GPT-Rosalind — het domein-specifieke reasoning model voor biologie en drug discovery — gaat per 5 oktober 2026 in productie-pricing.

**OpenAI DevDay 2026** leverde meer dan 20 aankondigingen op rondom GPT-6 Astra, Codex en productie-API's. OpenAI heeft drie safety-onderzoekers ontslagen na een intern onderzoek naar het lekken van gevoelige informatie aan een externe veiligheidsgroep; de timing vlak voor een grote releaseweek trekt aandacht.

*Bronnen: [TechCrunch – GPT-5.6 family](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/), [Google Blog – Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/), [OpenAI DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/), [LLM Stats – AI News October 2026](https://llm-stats.com/ai-news)*

## 🏛️ Governance & Ethiek

**EU AI Act – Article 50** (transparantievereisten) is per 2 augustus 2026 afdwingbaar. Providers en deployers van generatieve AI moeten nu watermarking- en openbaarmakingseisen naleven. De AI Omnibus-wijzigingen — bedoeld om de administratieve last voor bedrijven te verlichten — traden op 27 juli 2026 in werking.

Volgende deadline: **2 december 2026** — verbod op generatie van non-consensuele intieme beelden en CSAM. High-risk AI-systemen (Annex III) volgen pas per 2 december 2027.

**Nederland:** het kabinet investeert €120 miljoen in deelname aan het EU Ipcei-AI-programma, gericht op verlaging van ontwikkelkosten voor industriële AI, met speciale aandacht voor MKB. Daarnaast verkrijgt het kabinet per 1 januari de bevoegdheid om overnames van Nederlandse AI-bedrijven door niet-bevriende landen (zoals China) te blokkeren.

**Vlam** — een veilig, lokaal AI-model van SSC-ICT/AIVD — is beschikbaar als ChatGPT-alternatief voor rijksambtenaren. Data en modellen blijven onder Nederlands beheer.

*Bronnen: [EC – AI Act transparantieverplichtingen](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations), [EC – AI Act enforcement](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act), [Computable – €120M industriële AI](https://www.computable.nl/2026/09/21/kabinet-steekt-120-miljoen-euro-in-industriele-ai/), [Computable – AI Act transparantie-eisen](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)*

## 🔐 Security & Risk

**EchoLeak** is de meest impactvolle AI-beveiligingsincident van dit moment: een zero-click agentic aanval op productie-M365 Copilot. Een aanvaller stuurt een kwaadaardig e-mailbericht; zodra een gebruiker later een vraag aan Copilot stelt, laadt Copilot de vergiftigde mail op en exfiltreert gevoelige data via een image URL — zonder enige klik van het slachtoffer. Dit raakt direct enterprise-omgevingen.

**Prompt injection** blijft de #1 LLM-aanvalsvector (OWASP LLM01). Drie AI-coding agents lekten secrets via één prompt injection-aanval; een vendor system card had het risico al voorspeld. CrowdStrike (2026 Global Threat Report) documenteert prompt injection bij meer dan 90 organisaties in 2025, met een stijging van AI-gerelateerde aanvallen van 89% jaar-op-jaar.

Een nieuw arXiv-paper (*Prompt Injection 2.0: Hybrid AI Threats*) beschrijft hoe aanvallers prompt injection combineren met RAG-pipeline-manipulatie en model-router-targeting — complexere aanvalsketens die klassieke detectie omzeilen.

*Bronnen: [VentureBeat – EchoLeak & agent security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026), [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers), [Airia – AI Security 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)*

## 📈 Markt & Adoptie

**Microsoft 365 Copilot** overschrijdt 30 miljoen betaalde seats (vorig kwartaal: 20 miljoen). Microsoft lanceerde eind september de vernieuwde Copilot met drie modi: *Home* (persoonlijk), *Code* (development) en *Autopilot* (geautomatiseerde werkstromen). Tegelijk introduceert Microsoft *Frontier Company*: een outcome-gedreven organisatie met 6.000 embedded engineers bij klanten, al 330+ projecten afgerond bij 164 klanten.

**Google** lanceerde op Google Cloud Next '26 de *Agentic Data Cloud* — een cross-cloud lakehouse dat data-silo's verbindt voor AI-agenten — en het *Gemini Enterprise Agent Platform* (opvolger van Vertex AI) voor het bouwen, schalen en besturen van AI-agenten.

**Marktdynamiek:** de Microsoft-OpenAI-relatie wordt herzien; Microsoft concurreert steeds openlijker met eigen modellen. Hyperscalers zullen tegen 2031 twee derde van de wereldwijde datacentercapaciteit bezitten (CIO Dive).

*Bronnen: [Microsoft Blog – Nieuwe Copilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/), [CIO Dive – Copilot groei](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/), [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/), [TechCrunch – Microsoft vs OpenAI](https://techcrunch.com/2026/07/29/microsoft-is-openly-competing-with-openai-anthropic-more-than-ever/)*

## 💡 Ctac-relevantie

**Direct actie vereist — EchoLeak:** iedere Ctac-klant die M365 Copilot gebruikt loopt potentieel risico. Ctac kan proactief een quickscan aanbieden: welke e-maildata is toegankelijk voor Copilot, welke Copilot-integraties zijn actief, en zijn er prompt-injection-mitigaties ingesteld? Dit is een concrete dienst die nu relevant is.

**EU AI Act compliance-kans:** de transparantievereisten (Article 50) zijn actief maar worden door veel organisaties nog niet volledig nageleefd. Ctac's AI-unit kan een compacte compliance-check aanbieden, zeker richting sectoren als finance en overheid waar toezichthouders strenger handhaven.

**Overheid als groeisegment:** het kabinet investeert €120M in industriële AI en heeft een eigen veilig AI-model (Vlam). Dit signaleert dat Nederlandse overheidsorganisaties actief op zoek zijn naar vertrouwde AI-partners voor implementatie en integratie — een segment dat past bij Ctac's profiel.

**Microsoft Copilot-adoptie versnelt:** 30M+ seats betekent dat Ctac-klanten in de Microsoft-stack steeds vaker Copilot inzetten. Dienstverlening rondom Copilot-configuratie, governance en veilige integratie (mede in het licht van EchoLeak) is een logische volgende stap in de propositie.

## 📚 Bronnen & verder lezen

- [TechCrunch AI nieuws](https://techcrunch.com/category/artificial-intelligence/)
- [OpenAI – DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/)
- [OpenAI – GPT-Rosalind](https://openai.com/index/introducing-gpt-rosalind/)
- [Google Blog – Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/)
- [LLM Stats – AI News October 2026](https://llm-stats.com/ai-news)
- [EC – EU AI Act enforcement](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [EC – Transparantieverplichtingen AI](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations)
- [artificialintelligenceact.eu – Standard Setting](https://artificialintelligenceact.eu/standard-setting-overview/)
- [VentureBeat – EchoLeak agent security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [Airia – AI Security in 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Microsoft Blog – Nieuwe Copilot](https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/)
- [CIO Dive – Microsoft Copilot groei](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Computable – €120M industriële AI](https://www.computable.nl/2026/09/21/kabinet-steekt-120-miljoen-euro-in-industriele-ai/)
- [Computable – AI Act transparantie-eisen](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
