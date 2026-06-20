---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-20
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 20 juni 2026

## 🔑 Highlights van de dag

- **Fable 5 geblokkeerd voor niet-Amerikanen** – De VS-overheid heeft een exportcontrolemaatregel uitgevaardigd die Anthropic's Fable 5 en Mythos 5 verbiedt voor buitenlandse nationals; Anthropic heeft beide modellen voor alle klanten wereldwijd uitgeschakeld. Nederlandse en Belgische gebruikers hebben nu geen toegang meer.
- **EU AI Act: nog zes weken** – De wet wordt op 2 augustus 2026 volledig van kracht. De recent aangenomen AI Omnibus biedt vereenvoudiging voor het MKB, maar kernverplichtingen voor hoog-risico systemen blijven ongewijzigd.
- **AI coding agents lekken stelselmatig credentials** – Drie agents werden via één prompt-injection-aanval gecompromitteerd; Claude Code-geassisteerde commits lekken geheimen bij 3,2% van de repositories (vs. 1,5% baseline). AI-credential-lekken stegen 81% jaar op jaar.
- **Microsoft en Google domineren enterprise-markt** – Microsoft 365 Copilot overtreft 20 miljoen betaalde seats; Google Cloud passeert $20 miljard per kwartaal. Toch geeft twee derde van de bedrijven aan vast te zitten in de pilot-fase.
- **Open-weight modellen op frontier-niveau** – Kimi K2.6, Qwen3 235B en Devstral presteren vergelijkbaar met gesloten topmodellen voor coding en agentische taken, vaak tegen een fractie van de prijs.

## 🧠 Technologie & Modellen

Claude Fable 5 (uitgebracht 9 juni 2026) brak als eerste model de 90%-grens op Anthropic's core analytics benchmark en scoorde het hoogst op FrontierBench voor coding. Het was geprijsd op $10/$50 per miljoen tokens, maar is nu buiten de VS geblokkeerd (zie Governance). Terugval voor internationale klanten is Claude Opus 4.8.

In het open-source segment bieden Alibaba's **Qwen3 235B-A22B** (Apache 2.0) en **Kimi K2.6** serieuze frontier-alternatieven: Qwen 3.7 Max evenaart Claude Opus 4.7 op agentische benchmarks voor de helft van de inputkosten. **Devstral** is specifiek gebouwd voor agentische softwareontwikkeling (codebase-exploratie, multi-file editing). De **OpenEnv-coalitie** (Meta, Nvidia, Microsoft, Hugging Face) werkt aan een open trainingomgeving voor agents – dit versnelt open-source agent-infrastructuur aanzienlijk.

*Bronnen: [Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5) · [TechCrunch](https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/) · [Hugging Face](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)*

## 🏛️ Governance & Ethiek

De **EU AI Act** is op 2 augustus 2026 volledig van kracht – nog zes weken. De **AI Omnibus** (mei 2026) regelt vereenvoudiging voor kleine en middelgrote ondernemingen en uitbreiding van regulatory sandboxes, maar verandert niets aan de eisen voor hoog-risico AI.

De grote geopolitieke schok van de dag: de VS-overheid heeft **exportcontrole** afgekondigd op Fable 5 en Mythos 5, waardoor Anthropic beide modellen wereldwijd heeft uitgeschakeld. Dit precedent – het feit dat een Amerikaans AI-bedrijf buitenlandse gebruikers in één klap kan afsluiten op overheidsbevel – maakt de discussie over AI-soevereiniteit en Europese alternatieven concreter dan ooit.

In de VS treedt Colorado's Consumer Protections for Artificial Intelligence Act op 30 juni in werking; het Congres heeft een 269 pagina's tellende discussiedraft voor een federale AI-wet gepubliceerd.

*Bronnen: [EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/) · [Anthropic statement](https://www.anthropic.com/news/fable-mythos-access) · [VentureBeat](https://venturebeat.com/technology/anthropic-blocks-all-public-access-to-claude-fable-5-mythos-5-following-us-government-order-what-enterprises-should-do)*

## 🔐 Security & Risk

Drie AI coding agents werden via één prompt-injection-aanval gecompromitteerd via **Claude Code Security Review** – een GitHub Action-feature die Anthropic's eigen system card als "not hardened against prompt injection" bestempelt. Claude Code-geassisteerde commits lekken geheimen bij 3,2% vs. 1,5% baseline; AI-credential-lekken stegen 81% jaar op jaar (GitGuardian).

Kwetsbaarheden dit kwartaal: **Cursor IDE** (remote code execution via indirect prompt injection), **Microsoft Copilot Studio** en **Salesforce Agentforce** (data-exfiltratie via indirect prompt injection), **OpenClaw** (brede systeemtoegang maakt elke prompt injection impactvol). Het patroon is structureel: agentic tools met brede rechten zijn per definitie aanvalsgevoelig.

*Bronnen: [VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) · [The Hacker News](https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html)*

## 📈 Markt & Adoptie

Microsoft telt meer dan **20 miljoen betaalde Microsoft 365 Copilot seats** (Q3 2026); AI-omzet groeit 123% jaar op jaar naar een run rate van $37 miljard. **Google Cloud** overtrof voor het eerst $20 miljard per kwartaal – primair gedreven door Gemini Enterprise (+40% kwartaal op kwartaal). Gartner: Microsoft domineert in 'enterprisewide AI', Google in 'enterprise agentic AI'. Echter: twee derde van de bedrijven geeft aan niet voorbij de pilot-fase te komen.

*Bronnen: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) · [Microsoft blog](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)*

## 💡 Ctac-relevantie

**Drie directe actiepunten:**

1. **Fable 5-blokkade checken** – Als Ctac of klanten de Anthropic API of Claude.ai gebruiken, is toegang tot Fable 5/Mythos 5 nu compleet geblokkeerd. Operationele fallback: Opus 4.8 of open-source alternatieven (Qwen3, Kimi K2.6). De geopolitieke dimensie (VS-exportcontrole op AI) maakt het argument voor Europese of open-source modellen aanzienlijk sterker.

2. **EU AI Act-propositie is nu urgent** – Met zes weken tot volledige toepasselijkheid hebben klanten in overheid, zorg en finance acute compliance-behoefte. Gap-analyse, risicoklasse-bepaling en documentatieplicht zijn concrete diensten die Ctac nu kan leveren. Dit is het venster.

3. **AI coding tool security borgen** – Bij gebruik van Claude Code, Cursor of vergelijkbare tools zijn secrets-management (geen hardcoded credentials), promptguards en auditlogs nu geen optionele hygiëne maar een vereiste. Overweeg dit als standaard op te nemen in Ctac's AI-engineeringstandaarden.

## 📚 Bronnen & verder lezen

- [Claude Fable 5 & Mythos 5 – Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Fable 5 geblokkeerd na VS-overheidsbevel – VentureBeat](https://venturebeat.com/technology/anthropic-blocks-all-public-access-to-claude-fable-5-mythos-5-following-us-government-order-what-enterprises-should-do)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [AI Omnibus – Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [AI agent prompt injection leaks – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [OpenClaw kwetsbaarheden – The Hacker News](https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html)
- [Microsoft & Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [State of Open Source AI – Hugging Face](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [TechCrunch: Anthropic Fable 5 release](https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/)
