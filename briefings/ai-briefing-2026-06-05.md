---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-05
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 5 juni 2026

## 🔑 Highlights van de dag

- **Gemini 3.5 Flash nu algemeen beschikbaar** – Google's snelste frontier-model is vanaf vandaag GA via alle enterprise-kanalen; 4x sneller dan vergelijkbare modellen bij frontier-kwaliteit, en specifiek gebouwd voor autonome AI-agents.
- **Trump ondertekent AI Executive Order** – De VS kiest voor een deregulatorische aanpak: bedrijven wordt vrijwillig gevraagd nieuwe modellen 30 dagen voor release te delen met de overheid, plus een nieuw AI-cybersecurity clearinghouse.
- **EU AI Act-deadline nadert: 2 augustus 2026** – Transparantieregels worden bindend; het 'AI omnibus'-akkoord van 7 mei hervormt tevens de toezichtsstructuur en versoepelt verplichtingen voor kleinere bedrijven.
- **Kimi K2.5 (Moonshot AI) klopt GPT-5.2 en Claude Opus 4.5** – Open-source model met 1,1T parameters overtreft gesloten concurrentie op agentic benchmarks; directe relevantie voor wie geen vendor lock-in wil.
- **Cursor IDE kritieke kwetsbaarheid via prompt injection** – CVE-2026-22708 maakt remote code execution mogelijk in een populaire AI-coding IDE; waarschuwing voor alle teams die agentic ontwikkeltools gebruiken.

---

## 🧠 Technologie & Modellen

**Google Gemini 3.5 Flash** is vanaf vandaag breed beschikbaar. Het model haalt hogere scores dan het vorige frontiermodel Gemini 3.1 Pro op coding, agentic taken en multimodale redenering – maar tegen een fractie van de kosten ($1,50/$9 per 1M tokens). Google positioneert het expliciet als motor voor autonome agents, niet als chatbot. Tegelijk heeft Google de **Gemma 4 12B** uitgebracht: multimodaal open-source model dat volledig lokaal draait op een standaard 16 GB enterprise-laptop, inclusief audio- en videoanalyse.

**Kimi K2.5 van Moonshot AI** (China) is de verrassing van het kwartaal: 50,2% op de Humanity's Last Exam-benchmark mét tools, Modified MIT-licentie, beschikbaar als open-weight model. Het overtreft GPT-5.2 en Claude Opus 4.5 op agentic workflows en coding. Voor organisaties die open-source alternatieven zoeken, is dit een serieuze optie.

**Anthropic Opus 4.8** (uitgebracht 28 mei) introduceert een 'dynamic workflow'-tool en verbetert omgang met onzekere of slechte data. Binnen 41 dagen na Opus 4.7 – het modelreleasetempo neemt duidelijk toe.

---

## 🏛️ Governance & Ethiek

**Trump AI Executive Order** (ondertekend 2 juni): De VS kiest voor een lichte hand. Bedrijven wordt vrijwillig gevraagd modellen 30 dagen voor release te delen. Een verplicht vergunningStelsel is expliciet uitgesloten. Nieuw is een vrijwillig **AI Cybersecurity Clearinghouse** waar overheid en industrie kwetsbaarheden gezamenlijk aanpakken. Dit is een bewuste breuk met de Biden-aanpak.

**EU AI Act**: Het 'AI omnibus'-akkoord (7 mei) versterkt de bevoegdheden van het AI Office, centraliseert toezicht op GPAI-systemen en versoepelt vereisten voor kleinere bedrijven. Op **2 augustus 2026** treden de transparantieregels in werking – dan nog minder dan 60 dagen weg. In de VS bewegen California, New York en Rhode Island tegelijkertijd met eigen AI-wetgeving, wat de lappendeken buiten de EU verder vergroot.

---

## 🔐 Security & Risk

Prompt injection escaleert van theoretisch risico naar operationeel probleem. **CVE-2026-22708** in de Cursor AI-IDE maakt remote code execution mogelijk via indirect prompt injection – een aanvaller kan zo code laten uitvoeren in de ontwikkelomgeving van een collega. Drie AI coding agents bleken gelijktijdig secrets te lekken via een enkele prompt injection (VentureBeat, 2026).

OpenAI bevestigt officieel dat prompt injection structureel nooit volledig opgelost zal worden – het is vergelijkbaar met social engineering op het web. De verschuiving van copilots naar **autonome agents** maakt dit risico urgent: agents hebben meer rechten, meer toegang en handelen vaker zonder menselijke tussenkomst.

---

## 📈 Markt & Adoptie

Google Cloud passeerde voor het eerst de **$20 miljard omzetgrens** in Q1 2026 (+63% YoY), gedreven door AI-diensten. Amazon voegt $200 miljard toe aan zijn AI-investeringsprogramma. De big three (Microsoft, Google, Amazon) besteden gezamenlijk meer dan **$500 miljard aan capex in 2026**.

Toch: **twee derde van de enterprises zit nog vast in de AI-pilotfase** en weet niet hoe door te groeien naar productie. Microsoft en Google domineren de enterprise AI-markt; Google lanceerde een **Agentic Data Cloud** specifiek voor enterprise agent-deployments. Anthropic opende op 3 juni het **Claude Partner Network** met een Services Track en Partner Hub – gericht op system integrators en consultancybedrijven.

---

## 💡 Ctac-relevantie

**EU AI Act deadline** (2 augustus) is nu acuut: klanten in high-risk sectoren (overheid, zorg, finance) moeten transparantieregels aantonen. Ctac kan dit als urgente adviesopdracht positioneren – compliance is geen nice-to-have meer.

**De "pilot trap"** is de centrale kans voor Ctac: 67% van de markt wil van proof-of-concept naar productie maar weet niet hoe. Een aanpak die AI-implementaties versnelt van experiment naar bedrijfswaarde is exact wat klanten zoeken.

**Gemini 3.5 Flash + Gemma 4 12B** bieden nieuwe propositiemogelijkheden: frontier AI-kwaliteit voor lagere operationele kosten, en een lokaal draaiende multimodale optie voor klanten met data-soevereiniteitseisen (relevant in overheid en zorg).

**Prompt injection in agentic IDEs** (Cursor CVE) is direct relevant voor alle Ctac-teams en klanten die AI-coding tools gebruiken. Aanbeveling: beoordeel welke agentic tools in gebruik zijn en controleer patchstatus.

---

## 📚 Bronnen & verder lezen

- [Anthropic releases Opus 4.8 – TechCrunch](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/)
- [Gemini 3.5: frontier intelligence with action – Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)
- [Google zegt Gemini 3.5 Flash bespaart enterprises >$1B/jaar – VentureBeat](https://venturebeat.com/technology/google-says-gemini-3-5-flash-can-slash-enterprise-ai-costs-by-more-than-1-billion-a-year)
- [Kimi K2.5 open-source LLM – VentureBeat](https://venturebeat.com/orchestration/moonshot-ai-debuts-kimi-k2-5-most-powerful-open-source-llm-beating-opus-4-5)
- [Google Gemma 4 12B multimodaal lokaal model – VentureBeat](https://venturebeat.com/technology/googles-new-open-source-gemma-4-12b-analyzes-audio-video-and-runs-entirely-locally-on-a-typical-16gb-enterprise-laptop)
- [Trump AI Executive Order – The White House](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)
- [Trump signs narrower AI oversight order – TechCrunch](https://techcrunch.com/2026/06/02/trump-signs-narrower-executive-order-on-ai-oversight-after-industry-objections/)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act nationale implementatieplannen](https://artificialintelligenceact.eu/national-implementation-plans/)
- [Cursor IDE prompt injection CVE-2026-22708 – The Hacker News](https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html)
- [Drie AI coding agents lekten secrets – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [OpenAI: prompt injection is here to stay – VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [Microsoft en Google domineren enterprise AI-markt – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Google Cloud tops $20B – CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [AI Legislative Update June 5, 2026 – Transparency Coalition](https://www.transparencycoalition.ai/news/ai-legislative-update-june5-2026)
- [LLM Stats – AI updates juni 2026](https://llm-stats.com/ai-news)
