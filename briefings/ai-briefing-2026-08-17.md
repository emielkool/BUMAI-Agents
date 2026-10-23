---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-17
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 17 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaving live:** Sinds 2 augustus worden de transparantievereisten actief gehandhaafd — chatbots moeten zich kenbaar maken als AI en deepfakes moeten worden gelabeld. Dit is geen toekomstige dreiging meer, maar actuele compliance-plicht.
- **OpenAI stopt Astra-ontwikkeling:** OpenAI heeft de ontwikkeling van het Astra-model tijdelijk stilgelegd nadat het een "kritische cybersecurity-drempelwaarde" overschreed — het model kon zelfstandig aanvallen op beveiligde systemen uitvoeren. GPT-5.6-Cyber is het eerste model dat officieel op "High" wordt geclassificeerd onder het OpenAI Preparedness Framework.
- **DeepSeek verstoort enterprise markt:** DeepSeek V4 Pro werd vrijdag (16 aug.) gelanceerd met een nieuw piek/dalprijs-model en is 7–17× goedkoper dan Claude Sonnet en GPT-5.5. DeepSeek Harness is nu ook een open-source alternatief voor Claude Code. In de enterprise-markt verdringt DeepSeek Google al op tokenvolume.
- **Agentic AI security-incident:** Prompt injection trof tegelijk Claude Code, Gemini CLI en Copilot — drie AI-coding agents lekten via één aanval secrets. Dit illustreert het systeemrisico van agentic workflows zonder runtime-bescherming.
- **ABN Amro: 50 AI-use-cases in productie.** Brede enterprise-adoptie in de Nederlandse financiële sector neemt concreet vorm aan — niet meer experimenten, maar ingebedde operationele inzet.

---

## 🧠 Technologie & Modellen

**DeepSeek V4 Pro + Harness** is de lancering van de week. Het model scoort sterk op agentische taken en coding, en is via de API beschikbaar met piek/dalprijs-structuur. DeepSeek Harness v0.1 is een open-source agent-omgeving die direct concurreert met Claude Code. Aandachtspunt: V4 Flash — het lichtere model — presteert slecht op echte agentische taken ondanks hoge benchmarkscores. Benchmarks zeggen dus niet alles.

**Alibaba Qwen 3.8 27B** is vrijgegeven onder Apache 2.0: 27 miljard parameters, geïntegreerde vision, 262K native context (uitbreidbaar tot 1M). Voor open-source productie-inzet steeds serieuzer alternatief.

**Meta Muse Glimmer** (30B, multimodaal, 131K context, 100+ talen) richt zich op lokale agentic tool-use en LLM-as-judge toepassingen — interessant voor zelfgehoste AI-omgevingen.

Bronnen: [LLM Stats](https://llm-stats.com/llm-updates) · [VentureBeat – DeepSeek Harness](https://venturebeat.com/technology/deepseek-harness-launches-as-open-source-rival-to-claude-code-alongside-v4-pro-on-api-with-higher-prices) · [VentureBeat – DeepSeek V4 Flash](https://venturebeat.com/orchestration/deepseeks-top-ranked-v4-flash-stumbles-on-real-agent-tasks-as-its-prices-surge)

---

## 🏛️ Governance & Ethiek

De Europese Commissie handhaaft de AI Act-transparantievereisten actief per 2 augustus. Chatbots en interactieve systemen moeten zich als AI identificeren; deepfakes moeten worden gelabeld. De AI Omnibus (kracht van wet: 27 juli 2026) heeft de implementatiedeadline voor hoog-risico AI-systemen verlengd tot 2 december 2027 — meer tijd, maar ook meer onzekerheid voor leveranciers.

Elke EU-lidstaat moest per 2 augustus minimaal één AI regulatory sandbox operationeel hebben. In Nederland schrijft Computable dat bedrijven nu concreet aan de slag moeten met de nieuwe transparantie-eisen.

Bronnen: [Europese Commissie – handhaving 2 aug.](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) · [AI Act timeline](https://artificialintelligenceact.eu/implementation-timeline/) · [Computable – AI Act uitleg](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)

---

## 🔐 Security & Risk

**OpenAI stopzetting Astra:** Het model bereikte zelfstandig aanvalscapaciteiten op echte beveiligde systemen — een harde grens in het Preparedness Framework. GPT-5.6-Cyber is officieel geclassificeerd op niveau "High." Dit markeert een nieuw tijdperk: frontier models worden expliciet getoetst op offensieve cybercapaciteiten vóór release.

**Prompt injection als systeemsrisico:** Eén aanval trof tegelijk Claude Code, Gemini CLI en GitHub Copilot. Drie coding agents lekten secrets. De kern van het probleem: modellen kunnen niet onderscheiden tussen instructies en data. Dit is geen edge case meer — het is een structureel architectuurprobleem voor agentic pipelines.

Aanbeveling: Elke agentic implementatie die Ctac of klanten bouwen, moet een runtime-beveiligingslaag hebben. Tool-calling zonder sandboxing is nu aantoonbaar onveilig.

Bronnen: [TechCrunch – OpenAI Astra](https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/) · [VentureBeat – prompt injection incident](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) · [Airia – AI Security 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)

---

## 📈 Markt & Adoptie

**Microsoft** heeft meer dan 20 miljoen betaalde Copilot-seats bereikt, met een verviervoudiging van klanten met 50.000+ seats. De focus verschuift naar actieve push bij klanten: Microsoft duwt AI door — ook in NL (Computable, 11 aug.).

**AWS** investeert $1 miljard in een Forward Deployed Engineering-organisatie die software engineers combineert met AI-agents om klantimplementaties te versnellen. Een interessant bedrijfsmodel dat Ctac ook kan vertalen naar haar eigen delivery-aanpak.

**DeepSeek** verdringt Google in enterprise token-share (23% vs. Anthropic 32% in juni) maar stuit op data-residency-bezwaren in westerse markten. In Nederland en België zal enterprise-adoptie via lokale API-aanbieders of zelf-hosting moeten lopen.

**Twee derde van bedrijven zit nog vast in pilotfase** — zo groot is de kloof tussen experimenteren en productie.

Bronnen: [Microsoft FY26 terugblik](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/) · [CIO Dive – AI spending](https://www.ciodive.com/news/AI-spending-soars-enterprise-maturity/827488/) · [AWS forward deployed](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/) · [Computable – Microsoft NL](https://www.computable.nl/2026/08/11/microsoft-duwt-ai-door-bij-klanten/) · [Computable – DeepSeek stoot Google](https://www.computable.nl/2026/08/13/deepseek-stoot-google-van-ai-troon-bij-bedrijven/) · [Computable – ABN Amro](https://www.computable.nl/2026/08/13/abn-amro-voortvarend-met-ai/)

---

## 💡 Ctac-relevantie

**Drie directe actiepunten:**

1. **AI Act compliance-scan voor klanten.** Vanaf 2 augustus zijn de transparantievereisten actief. Klanten die chatbots of AI-systemen inzetten — in overheid, zorg of finance — moeten nu aantoonbaar compliant zijn. Dit is een direct instappunt voor Ctac om klanten te ondersteunen met assessments en implementatie-begeleiding.

2. **Agentic AI-security als propositie.** De prompt injection-incidenten tonen aan dat agentic pipelines zonder runtime-bescherming onveilig zijn. Ctac kan zich positioneren als partner die agentische workflows veilig bouwt — inclusief sandboxing, monitoring en audit trails. De markt vraagt hierom, maar het aanbod is nog dun.

3. **Pilotfase doorbreken.** Twee derde van enterprise-klanten zit vast in de experimentfase. ABN Amro (50 use-cases in productie) laat zien dat schaal mogelijk is. Ctac kan het "van pilot naar productie"-traject als standaard delivery-propositie aanbieden — met name in de sectoren waar Ctac al actief is (finance, overheid, industrie).

DeepSeek als goedkoop alternatief verdient aandacht voor interne Ctac-toepassingen, maar bij klantprojecten met gevoelige data is data-residency leidend — dan zijn lokale of Europese AI-aanbieders de veiligste keuze.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI Astra security](https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/)
- [EC – AI Act handhaving 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [artificialintelligenceact.eu – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [VentureBeat – DeepSeek Harness](https://venturebeat.com/technology/deepseek-harness-launches-as-open-source-rival-to-claude-code-alongside-v4-pro-on-api-with-higher-prices)
- [VentureBeat – prompt injection incident](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Airia – AI Security 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Microsoft FY26 blog](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [CIO Dive – AI infrastructure spending](https://www.ciodive.com/news/AI-spending-soars-enterprise-maturity/827488/)
- [AWS forward deployed engineering](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)
- [Computable – AI Act uitleg](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [Computable – DeepSeek stoot Google](https://www.computable.nl/2026/08/13/deepseek-stoot-google-van-ai-troon-bij-bedrijven/)
- [Computable – ABN Amro AI](https://www.computable.nl/2026/08/13/abn-amro-voortvarend-met-ai/)
- [LLM Stats – model updates](https://llm-stats.com/llm-updates)
- [VentureBeat – DeepSeek V4 Flash agentic](https://venturebeat.com/orchestration/deepseeks-top-ranked-v4-flash-stumbles-on-real-agent-tasks-as-its-prices-surge)
