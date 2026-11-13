---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-27
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 27 juli 2026

## 🔑 Highlights van de dag
- **Kimi K3 open-weights vandaag verwacht**: Moonshot AI's 2,8-biljoen-parameter model staat #1 op coding-leaderboards en de open gewichten worden vandaag vrijgegeven. Samen met DeepSeek V4 (24 juli) is dit de grootste open-weight-release concentratie ooit.
- **VS overheid remt topmodellen**: Washington hield zowel Claude Fable 5 als GPT-5.6 aan voor verplichte pre-release review — een primeur: voor het eerst beslist de overheid wanneer de krachtigste AI naar buiten mag.
- **Microsoft kiest frontaal voor eigen modellen**: Microsoft traint salesteams om OpenAI, Google en Anthropic negatief te vergelijken met eigen MAI-modellen (tot 89% goedkoper). De Microsoft Frontier Company (€2,5 mrd) is de operationele arm hiervan.
- **EU AI Omnibus trad in werking**: De vereenvoudigde implementatieverordening is actief, samen met een actieplan voor AI en cybersecurity en een aangekondigde derde-partij-evaluatiecapaciteit voor 2027.
- **Agent-betrouwbaarheid wordt de bottleneck**: 57% van enterprises had een zelfverzekerd-maar-fout AI-agent; Amazon's AGI-directeur stelt dat reliability, niet capability, enterprise-implementatie blokkeert.

## 🧠 Technologie & Modellen

De laatste week van juli wordt recordbrekend voor open modellen. **Kimi K3** (Moonshot AI, 2,8T parameters) pakte de eerste plek op een groot coding-leaderboard en open weights worden vandaag vrijgegeven. **DeepSeek V4** volgde op 24 juli met een stabiele release. Dit is relevant: voor coding, reasoning en agentic taken zijn open-weight modellen niet langer inferieur aan gesloten varianten.

Aan de gesloten kant lanceerde **OpenAI GPT-5.6** (9 juli) in drie smaken — Sol (flagship), Terra (mid) en Luna (budget). **Google Gemini 3.6 Flash** en 3.5 Flash-Lite (21 juli) claimen 17% tokenreductie. **Grok 4.5** (xAI, 8 juli) positioneert zich op tokenefficientie voor agentic werk. **Inkling**, het eerste model van Mira Murati's Thinking Machines Lab (15 juli), is open-weight en gericht op taakafstemming boven general-purpose prestaties.

*Kritisch:* "Tokenefficientie" is het nieuwe PR-buzzword — wacht op onafhankelijke benchmarks voordat conclusies worden getrokken.

Bronnen: [TechCrunch – GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/) | [TechCrunch – Gemini](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/) | [TechCrunch – Inkling](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/)

## 🏛️ Governance & Ethiek

De **EU AI Omnibus Regulation** (politiek akkoord mei 2026) trad in werking als vereenvoudiging van de originele AI Act-implementatie. Parallel publiceerde de Commissie een actieplan voor AI en cybersecurity en kondigt ze voor 2027 een capaciteitsoproep aan voor onafhankelijke pre-markt AI-evaluaties.

Opvallender is het VS-precedent: de **executive order van 2 juni 2026** legt verplichte pre-release reviews op voor geavanceerde systemen — Claude Fable 5 en GPT-5.6 ondervonden beide vertraging. Dit kader kan ook Europese regulering beïnvloeden.

Bronnen: [EU AI Act](https://artificialintelligenceact.eu/) | [EC – governance](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement) | [LLM Stats](https://llm-stats.com/llm-updates)

## 🔐 Security & Risk

**Prompt injection staat voor het tweede jaar op rij op #1 bij OWASP's LLM Top 10.** Het risico escaleert mee met de opkomst van agentic systemen: VentureBeat beschreef hoe drie AI coding agents geheimen uitlekten via één prompt injection-aanval — terwijl de eigen system cards het risico al hadden voorspeld.

Het structurele probleem blijft: LLM's kunnen instructies en data niet betrouwbaar onderscheiden. Meer autonomie en tool-toegang vergroten het aanvalsoppervlak proportioneel.

Bronnen: [VentureBeat – agent leaks](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [Airia – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)

## 📈 Markt & Adoptie

**Microsoft decoupleert zich actief van OpenAI.** De lancering van **Microsoft Frontier Company** (2 juli, $2,5 mrd commitment) als apart AI-implementatiebedrijf, gecombineerd met eigen MAI-modellen op Bing, PowerPoint, Dynamics 365 en Azure, stuurt een duidelijk signaal aan enterprise-afnemers. Verkopers worden getraind om OpenAI en Anthropic af te troeven op kosten.

Uit de VentureBeat Agent Pulse Survey (juni 2026): 71% van wat enterprises "agents" noemen zijn feitelijk single-prompt chatbot wrappers. Toch staat 66% al productie-inzet toe zonder human-in-the-loop. Antropic's Claude is het primaire platform voor 40% van enterprise-respondenten — meer dan twee keer zoveel als nummer twee.

Bronnen: [TechCrunch – Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) | [VentureBeat – agent deployment](https://venturebeat.com/technology/amazon-agi-director-says-ai-agent-reliability-not-capability-is-blocking-enterprise-deployment-at-vb-transform-2026) | [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

## 💡 Ctac-relevantie

**1. Microsoft-advies actualiseren.** De modellen achter Microsoft 365 Copilot en Azure AI zijn steeds meer Microsoft-eigen (MAI), niet OpenAI. Klanten die vragen om GPT-kwaliteit bij Microsoft-producten krijgen iets anders dan verwacht. Ctac-consultants moeten dit actief communiceren en de proposities bijstellen.

**2. Agent-governance als onderscheidende dienst.** Het industrie-brede probleem — chatbots als agents verkopen zonder echte orkestratie of evaluatie — is een opening voor Ctac. Klanten helpen onderscheid te maken tussen schijnagents en toetsbare, betrouwbare workflows is direct verkoopbaar.

**3. Open-weight modellen evalueren.** Kimi K3 en DeepSeek V4 maken open-source serieus voor productie. Voor klanten met privacy-eisen of kostenbeheer kan fine-tunen op open modellen nu een valide alternatief zijn voor cloud-API's. Laat de AI-engineer een korte haalbaarheidscheck doen.

## 📚 Bronnen & verder lezen
- [TechCrunch – GPT-5.6 lancering](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [TechCrunch – Google Gemini 3.6 Flash](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)
- [TechCrunch – Inkling (Thinking Machines)](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/)
- [TechCrunch – Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [TechCrunch – Microsoft verkopers trainen vs OpenAI](https://techcrunch.com/2026/07/15/microsoft-is-reportedly-training-salespeople-to-talk-down-openai-and-anthropic/)
- [VentureBeat – Agent leaks via prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – Amazon AGI op enterprise reliability](https://venturebeat.com/technology/amazon-agi-director-says-ai-agent-reliability-not-capability-is-blocking-enterprise-deployment-at-vb-transform-2026)
- [Airia – AI Security in 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [EC – AI Act governance & handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [LLM Stats – model updates juli 2026](https://llm-stats.com/llm-updates)
- [CIO Dive – Microsoft & Google enterprise AI markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
