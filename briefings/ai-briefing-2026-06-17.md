---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-17
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 17 juni 2026

## 🔑 Highlights van de dag

- **Claude Opus 4.8 staat op #1**: Anthropic's meest recente flagship-model domineert de Artificial Analysis Intelligence Index (score 61.4) — relevant voor Ctac's model-selectie.
- **EU AI Act D-47**: Over 47 dagen is de wet volledig van kracht (2 augustus 2026). De Europese Commissie publiceert nu praktijkrichtlijnen; klanten zonder compliance-roadmap lopen nu echt achter.
- **Microsoft Agent 365 is GA**: Het enterprise AI-agent platform is uit preview, maar 29% van alle agents in organisaties blijkt 'shadow AI' — buiten IT-goedkeuring om.
- **Prompt injection: structureel onoplosbaar**: OpenAI lanceerde Lockdown Mode én erkent publiekelijk dat het probleem nooit volledig weg zal zijn. OWASP rankt het als het #1 LLM-risico.
- **Capex-race escaleert verder**: Microsoft + AWS investeren gezamenlijk >$500 miljard in AI-infrastructuur dit jaar; Google Cloud overschreed $20 miljard kwartaalomzet.

## 🧠 Technologie & Modellen

**Claude Opus 4.8** (uitgebracht 28 mei 2026) pakt de toppositie op de Artificial Analysis Intelligence Index: score 61.4, +4.1 punt t.o.v. Opus 4.7. Prestaties: 84% op Online-Mind2Web en als eerste model boven de 10% op de Legal Agent Benchmark. Praktisch relevant: code is ~4× minder likely om fouten onopgemerkt te laten. Nieuw: een Fast Mode-tier ($10/$50 per miljoen tokens, 2,5× sneller) en dynamische workflows in Claude Code.

**Google I/O 2026** introduceerde **Gemini Omni** (video-first, multimodaal wereldbegrip) en **Gemini 3.5 Flash** — nu standaard in Google Search AI Mode wereldwijd. Google's Antigravity platform positioneert zich als agent-first ontwikkelomgeving: agents die handelen in plaats van alleen schrijven.

De **juni 2026 launch wave** is uitzonderlijk druk: naast Gemini 3.5 Pro wordt ook **Claude Mythos 1** (Anthropic) verwacht, plus het al lang aangekondigde **Grok 5** van xAI. Topposities op benchmarks zijn momenteel een kwestie van weken, geen kwartalen.

## 🏛️ Governance & Ethiek

De **EU AI Act is over 47 dagen volledig van kracht** (2 augustus 2026). De Europese Commissie publiceert in Q2 2026 praktijkrichtlijnen voor high-risk classificatie, transparantieverplichtingen en incidentrapportage. Het European AI Office bewaakt de handhaving, met bijzondere focus op General Purpose AI Models (GPAI).

Kritische noot: governance- en GPAI-verplichtingen gelden al, maar uit onderzoek blijkt dat twee derde van bedrijven nog vastloopt in de pilotfase. De High-Risk-regels voor biometrie, kritieke infrastructuur en HR volgen pas in december 2027 — dat geeft ruimte, maar ook een vals gevoel van urgentie.

## 🔐 Security & Risk

**OpenAI lanceerde Lockdown Mode** (6 juni) als bescherming tegen prompt injection vanuit webpagina's en externe content. Tegelijk erkent OpenAI dat prompt injection — vergelijkbaar met social engineering — nooit volledig opgelost zal worden.

**Microsoft** introduceert het concept *double agents*: AI-agents die via prompt injection gemanipuleerd worden tot data-exfiltratie. Defender krijgt in juni 2026 real-time blokkering via Intune, inclusief asset context mapping (welke devices, MCP-servers en cloud-resources een agent kan bereiken). In 29% van onderzochte organisaties draaien agents al buiten IT-goedkeuring.

Groeiend signaal: **machine-identiteiten overtreffen menselijke 82:1**. Traditionele IAM-systemen zijn hier niet op gebouwd — een structureel nieuwe attack surface.

## 📈 Markt & Adoptie

**Microsoft Agent 365** is uit preview en positioneert AI-agents als enterprise-grade infrastructuur met governance-tooling. Parallel daarmee: **Microsoft Copilot Cowork** integreert Anthropic's Claude rechtstreeks in Microsoft 365-apps — een opvallende verdieping van de Microsoft-Anthropic samenwerking.

**Google Cloud** overschreed $20 miljard kwartaalomzet op de rug van AI-adoptie. Microsoft en AWS kondigden gezamenlijk >$500 miljard capex aan voor AI-infrastructuur in FY2026. De hyperscalers zetten daarmee alles op GPU-capaciteit en lock-in.

Enterprise-adoptie versnelt, maar twee derde van bedrijven slaagt er nog niet in AI van pilot naar productie te brengen.

## 💡 Ctac-relevantie

**EU AI Act D-47 = urgente adviesopdracht.** Klanten in overheid, zorg en finance die nog geen compliance-roadmap hebben, hebben maximaal zes weken. Gap-analyse, risicoclassificatie en een governance-framework zijn nu directe proposities — geen 'nice to have' meer.

**Shadow AI en agent-governance** zijn een concrete pijn bij enterprise-klanten. De Microsoft Defender + Agent 365 stack biedt Ctac een integratieroute als implementatiepartner: visibility op onbeheerde agents, policy-enforcement en incident-response inrichten. Dit sluit aan op bestaande Microsoft-klantrelaties.

**Claude Opus 4.8 als #1 model** is relevant voor de interne AI-unit: voor complexe redenering en code-review is Opus 4.8 nu de beste keuze. Fast Mode maakt het kostenefficiënt voor hoge-volume gebruik.

**Copilot Cowork + Anthropic** versterkt de Microsoft-stack die Ctac al bedient — gecombineerde kennis van beide platformen wordt een onderscheidend voordeel bij enterprise-klanten die aan beide kanten staan.

## 📚 Bronnen & verder lezen

- [Claude Opus 4.8 – Artificial Analysis benchmarks](https://artificialanalysis.ai/articles/claude-opus-4-8-analysis-and-benchmarks)
- [Google I/O 2026 – alle aankondigingen](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Google Search I/O 2026: AI agents](https://blog.google/products-and-platforms/products/search/search-io-2026/)
- [June 2026 AI launch wave – WaveSpeed](https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/)
- [OpenAI Lockdown Mode – TechCrunch](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – richtlijnen AI Act implementatie](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Microsoft Agent 365 naar GA – VentureBeat](https://venturebeat.com/ai/microsofts-agent-365-shifts-ai-agents-from-sandbox-tools-to-enterprise-grade-infrastructure)
- [Microsoft double agents / shadow AI – VentureBeat](https://venturebeat.com/technology/microsoft-says-ungoverned-ai-agents-could-become-corporate-double-agents-its)
- [Shadow AI risico – CIO Dive](https://www.ciodive.com/news/shadow-ai-security-risks-netskope/808880/)
- [Machine identities 82:1 – VentureBeat](https://venturebeat.com/security/machine-identities-outnumber-humans-82-to-1-legacy-iam-cant-keep-up)
- [Microsoft Copilot Cowork + Anthropic – VentureBeat](https://venturebeat.com/orchestration/microsoft-announces-copilot-cowork-with-help-from-anthropic-a-cloud-powered)
- [Google Cloud >$20B – CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [Microsoft + Google heersen enterprise AI-markt – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
