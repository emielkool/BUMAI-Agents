---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-16
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 16 juni 2026

## 🔑 Highlights van de dag

- **US overheid sluit Anthropic's krachtigste modellen af.** Claude Fable 5 en Mythos 5 zijn per overheidsorder offline gehaald wegens nationale veiligheidszorgen — drie dagen na lancering van Fable 5. Historisch precedent voor AI-regulering.
- **EU AI Act: 47 dagen tot volledige toepasselijkheid.** Op 2 augustus 2026 geldt de wet volledig. EC publiceert nu Code of Practice voor labeling van AI-gegenereerde content; enterprises die nog niet beginnen, lopen ernstige achterstand op.
- **Microsoft Agent 365 general availability.** Shadow AI is een boardroom-issue: 29% van AI-agents in organisaties draait zonder goedkeuring van IT of security. Agent 365 biedt nu runtime-blokkering en Defender-integratie.
- **OpenAI dient confidentieel IPO-papieren in.** Volgt daarmee Anthropic (S-1 ingediend op 1 juni). De twee grootste AI-labs gaan tegelijk naar de beurs — markant signaal over de sector.
- **Open-weight modellen bereiken productierijpheid.** Kimi K2.6 (1,1T parameters, Modified MIT) en Qwen3 worden serieus genomen voor enterprise deployments — niet langer alleen als goedkopere alternatieven.

## 🧠 Technologie & Modellen

**Google Gemini 3.5 Flash** is het nieuwe standaardmodel in AI Mode voor Search, wereldwijd uitgerold. Het combineert "frontier intelligence" met lage latency — relevant voor real-time enterprise toepassingen. **Gemini 3.5 Pro** (2M token context, Deep Think reasoning mode) wordt vóór 30 juni verwacht.

**OpenAI GPT-Rosalind** is als research preview beschikbaar in ChatGPT, Codex en de API — het eerste model in OpenAI's Life Sciences-serie, gericht op gekwalificeerde klanten in farmacie en biotech.

In de open-source wereld springt **Kimi K2.6** (Moonshot AI) eruit: 1,1T parameters onder Modified MIT-licentie, sterk voor agentic workflows en coding. Naast Qwen3 en Phi-4 laat dit zien dat open-weight modellen de kloof met closed models sluiten voor specifieke usecases.

## 🏛️ Governance & Ethiek

**EU AI Act: countdown begonnen.** 2 augustus 2026 is de deadline voor volledige toepasselijkheid. De EC publiceert in juni een Code of Practice voor AI-content labeling en richtlijnen voor high-risk classificatie. Het "AI Omnibus" akkoord van 7 mei vereenvoudigt een aantal regels, maar verzacht de kern niet.

**Anthropic roept op tot FAA-model voor AI.** CEO Dario Amodei pleit voor licentievereisten voor krachtige modellen, vergelijkbaar met luchtvaartcertificering. Tegelijk heeft de US overheid twee Anthropic-modellen afgesloten — waarmee overheidsingrijpen in AI-releases realiteit is geworden, niet langer hypothetisch.

**OpenAI erkent: prompt injection is structureel.** In reactie op onderzoeksbevindingen stelt OpenAI dat dit risico "vergelijkbaar met phishing op het web" is en nooit volledig zal worden opgelost — een eerlijke maar verontrustende positie voor enterprises die AI-agents inzetten.

## 🔐 Security & Risk

Prompt injection blijft het toprisico (OWASP LLM01:2025). Nieuw onderzoek toont aan dat AI coding agents — waaronder GitHub Copilot Agent en Claude Code — kwetsbaar zijn via kwaadaardige GitHub-comments: PR-titels en issue bodies worden aanvalsvectoren voor API key- en tokendiefstal.

**Machine identities overtreffen menselijke 82:1** in enterprise omgevingen. Legacy IAM-systemen zijn niet gebouwd voor deze verhouding, waardoor AI-agents een blinde vlek vormen in beveiligingsarchitecturen.

Microsoft Agent 365 introduceert als reactie hierop "asset context mapping": een relatiegraph per agent (welke devices, MCP-servers, identities, cloudresources). Nuttig instrument, maar $99/maand per gebruiker maakt dit een bewuste upsell.

## 📈 Markt & Adoptie

**Microsoft Agent 365** gaat uit preview. Naast governance-features bevat het Copilot Cowork (samen met Anthropic gebouwd) als cross-M365 agent. Microsoft Build 2026 (2 juni) zette de toon: AI-agents zijn infrastructuur, geen experiment meer.

**Google Cloud** passeerde $20B kwartaalomzet — gedreven door AI-workloads. **AWS** investeert $10B in North Carolina data centers als onderdeel van $100B capex voor 2026.

Tegelijkertijd: **twee derde van enterprises** zit nog vast in AI pilot-fase en slaagt er niet in naar productie te schalen. Wil je meer over die kloof lezen: TechCrunch signaleerde dit als het kernthema van 2026.

## 💡 Ctac-relevantie

**EU AI Act compliance is nu urgent verkoopargument.** Met 47 dagen tot 2 augustus hebben klanten van Ctac concrete hulp nodig bij classificatie, documentatie en risicobeheer. Dit is een afgebakend, tijdsgevoelig project waar Ctac direct waarde kan leveren.

**Shadow AI governance = nieuw dienstverleningsdomein.** Agent 365 laat zien dat de markt bereid is te betalen voor AI-governance. Ctac kan dit als managed service of implementatietraject positioneren — juist voor klanten die Microsoft-stack gebruiken maar nog geen grip hebben op hun agent-landschap.

**Open-weight modellen verlagen de drempel voor klanten.** Kimi K2.6 en Qwen3 zijn serieuze alternatieven voor enterprises met kostensensitiviteit of data-soevereiniteitswensen (on-premise). Ctac's AI engineer kan hier een modelkeuze-adviesaanbod op bouwen.

**Prompt injection als security-gesprek.** Elke klant die AI-agents op productiedata laat werken, heeft een kwetsbaarheid die niet verdwijnt. Ctac kan dit proactief op de agenda zetten bij security-bewuste klanten.

## 📚 Bronnen & verder lezen

- [Google Search I/O 2026 updates – blog.google](https://blog.google/products-and-platforms/products/search/search-io-2026/)
- [Gemini app next evolution – blog.google](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)
- [OpenAI GPT-Rosalind – openai.com](https://openai.com/index/introducing-gpt-rosalind/)
- [State of Open Source Hugging Face Spring 2026 – huggingface.co](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [EU AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC ondersteunt implementatie AI Act – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Anthropic's safety warnings backfired – TechCrunch](https://techcrunch.com/2026/06/12/anthropics-safety-warnings-may-have-just-backfired-the-government-has-pulled-the-plug-on-its-most-powerful-ai/)
- [Anthropic IPO-aankondiging – TechCrunch](https://techcrunch.com/2026/06/04/ahead-of-its-ipo-anthropics-daniela-amodei-shrugs-off-doubts-about-ais-returns/)
- [OpenAI confidentieel IPO ingediend – TechCrunch](https://techcrunch.com/2026/06/08/following-anthropic-openai-files-confidentially-for-ipo/)
- [Anthropic CEO FAA-model voor AI – VentureBeat](https://venturebeat.com/technology/anthropic-ceo-calls-for-faa-style-regulation-of-powerful-ai-models-what-enterprises-should-know/)
- [Prompt injection blijft bestaan – VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [AI agents kwetsbaar via GitHub comments – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Machine identities 82:1 – VentureBeat](https://venturebeat.com/security/machine-identities-outnumber-humans-82-to-1-legacy-iam-cant-keep-up)
- [Microsoft Agent 365 GA – VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [Microsoft shadow AI double agents – VentureBeat](https://venturebeat.com/technology/microsoft-says-ungoverned-ai-agents-could-become-corporate-double-agents-its)
- [Google Cloud $20B – CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [Microsoft & Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [AI Schneier on prompt injection – schneier.com](https://www.schneier.com/essays/archives/2026/01/why-ai-keeps-falling-for-prompt-injection-attacks.html)
