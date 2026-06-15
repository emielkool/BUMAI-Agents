---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-09
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 9 juni 2026

## 🔑 Highlights van de dag

- **Microsoft Build 2026 domineert het nieuws:** Zeven nieuwe in-house MAI-modellen gepresenteerd, waaronder het eerste eigen reasoning model (MAI-Thinking-1). Microsoft wil structureel minder afhankelijk worden van OpenAI — en laat dat strategisch duidelijk merken.
- **Claude zit nu in Excel:** Anthropic's Claude is geïntegreerd in Excel Agent Mode, gebruikt door naar schatting 750 miljoen mensen. Een stille maar significante adoptiedoorbraak voor enterprise AI.
- **Anthropic nadert de beurs:** Na een Series H van $65 miljard (valutatie: $965 miljard) diende Anthropic vertrouwelijk haar IPO-aanvraag in — gedreven door de groei van Claude Code.
- **Prompt injection raakt productie-agents:** Drie populaire coding agents (Claude Code, GitHub Copilot Agent, Google Gemini CLI) bleken kwetsbaar voor prompt injection via GitHub-commentaar, met mogelijke API-key-diefstal tot gevolg.
- **Open source haalt closed models in:** Kimi K2.6 en DeepSeek-V4-Pro zijn nu serieuze alternatieven voor gesloten modellen op coding-, reasoning- en agentic taken — relevant voor enterprise-architecten die platformkosten willen beheersen.

---

## 🧠 Technologie & Modellen

**Microsoft Build 2026 – de MAI-familie**
Microsoft presenteerde deze week zeven eigen modellen onder de MAI-vlag: MAI-Thinking-1 (reasoning, #1 op eigen evaluaties vs. Claude Sonnet 4.6), MAI-Image-2.5 (tekst-naar-beeld en beeld-naar-beeld, #2 op Arena-leaderboard), MAI-Transcribe-1.5 (state-of-the-art over 43 talen), MAI-Voice-2, en MAI-Code-1 voor GitHub-integraties. Alle modellen zijn via Azure Foundry beschikbaar — één endpoint, één factuurrelatie, naast 11.000+ andere modellen. De 'zelfvoorzieningsstrategie' is real: Microsoft wil structureel minder afhankelijk zijn van OpenAI.
*(Bron: [blogs.microsoft.com](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/) | [GeekWire](https://www.geekwire.com/2026/microsoft-unveils-seven-homegrown-ai-models-in-bid-for-long-term-self-sufficiency/))*

**Google Gemini 3.5 Flash – nu GA, Pro komt eraan**
Gemini 3.5 Flash is since 19 mei GA via de Gemini API en Google AI Studio ($1,50 / $9,00 per miljoen tokens). CEO Sundar Pichai beloofde Gemini 3.5 Pro "volgende maand". Google positioneert Gemini 3.5 als de eerste modellenfamilie die frontier-intelligentie combineert met agentic actie.
*(Bron: [llm-stats.com](https://llm-stats.com/llm-updates))*

**Open-source: Kimi K2.6 en DeepSeek-V4-Pro**
Moonshot AI's Kimi K2.6 ondersteunt multimodale, paralleliseerbare agentic workflows — van document tot website tot spreadsheet in één autonome run. DeepSeek-V4-Pro-Max scoort top op coding benchmarks en dicht de kloof met closed-source modellen op reasoning. Beide zijn open-weight en volledig zelf te hosten.
*(Bron: [huggingface.co](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026))*

---

## 🏛️ Governance & Ethiek

**EU AI Act: politiek akkoord en tijdlijnupdate**
Op 7 mei 2026 werd een politiek akkoord bereikt over amendementen op de AI Act, met name rondom versterking van de AI Office en centralisatie van toezicht op GPAI-modellen. Praktisch relevant: systemen in high-risk toepassingen (biometrie, kritieke infrastructuur, onderwijs, arbeidsmarkt) moeten per 2 december 2027 compliant zijn. Elke lidstaat is verplicht om minimaal één nationale AI-sandbox op te zetten vóór 2 augustus 2026 — dit loopt voor NL via het Digital Infrastructure-traject. Guidelines voor praktische toepassing van de hoge-risico-classificatie worden dit jaar uitgewerkt.
*(Bron: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/) | [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines))*

---

## 🔐 Security & Risk

**Prompt injection treft productie-agents — nu via GitHub**
Onderzoekers toonden aan dat Claude Code, GitHub Copilot Agent en Google's Gemini CLI kwetsbaar zijn voor prompt injection via GitHub-commentaar: kwaadwillenden kunnen PR-titels, issue-bodies of commentaar inzetten als aanvalsvector voor het stelen van API-sleutels en tokens. Dit is geen theoretische dreiging meer — het raakt direct de coding workflows die enterprise-teams dagelijks inzetten.

De kern van het probleem: agentic AI-systemen kunnen niet betrouwbaar onderscheid maken tussen instructies en data. Verdediging vereist least-privilege tooling, input/output-filtering, menselijke goedkeuring voor risicovolle acties én regelmatig adversarieel testen. OpenAI en het NCSC (UK) stellen expliciet dat prompt injection "nooit volledig opgelost zal worden."
*(Bron: [VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) | [The Hacker News](https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html))*

---

## 📈 Markt & Adoptie

**Anthropic richting IPO — Claude Code drijft de groei**
Na een Series H van $65 miljard (valutatie $965 miljard) diende Anthropic op 1 juni vertrouwelijk een IPO-aanvraag in. De motor: Claude Code, dat volgens marktanalisten Anthropic naar de koppositie heeft geleid ten opzichte van OpenAI in developer-adoptie. Anthropic opent kantoren in Milaan en Seoul en lanceert het Claude Partner Network.
*(Bron: [buildfastwithai.com](https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026))*

**Enterprise AI: twee derde vast in pilotfase**
Ondanks miljardenbedragen aan investeringen zit twee derde van de enterprises nog in de pilotfase, zo blijkt uit recent onderzoek. Microsoft en Google domineren de markt als AI-leverancier; Microsoft pakt dit aan met Agent 365 (nu GA) en de nieuwe Microsoft IQ context-laag die agents verankert in enterprise-data. De koppeling van Copilot Cowork met Anthropic's Claude is een teken dat het ecosysteem snel consolideert rondom hybride multi-model orkestratie.
*(Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat))*

**OpenAI op AWS**
Per 2 juni zijn OpenAI's frontier-modellen en Codex beschikbaar via Amazon Web Services — een directe concurrent voor Microsofts Azure-monopolie op OpenAI-toegang.
*(Bron: [openai.com/news](https://openai.com/news/product-releases/))*

---

## 💡 Ctac-relevantie

**Multi-model orkestratie wordt de standaard — Ctac moet kiezen**
De integratie van Claude in Excel, de MAI-familie in Azure Foundry, en Gemini in Google Workspace betekenen dat grote enterprise-klanten binnenkort geen "één model"-keuze meer maken, maar multi-model workflows inrichten. Voor Ctac's AI-unit is dit een propositiekans: adviseren over model-selectie per use case, governance-inrichting en kosten-optimalisatie is iets dat de meeste enterprise-IT-teams niet intern kunnen.

**Prompt injection als reëel risico voor klantprojecten**
Als Ctac AI-coding-agents (Claude Code, Copilot) inzet in klantomgevingen met GitHub-toegang, is prompt-injection-beveiliging nu een verplicht onderdeel van de architectuurreview. Dit is een concrete aanbeveling richting klanten in finance en overheid.

**EU AI Act sandbox-deadline nadert (augustus 2026)**
Klanten in gereguleerde sectoren (zorg, overheid, finance) moeten voor augustus 2026 aantoonbaar bezig zijn met AI Act compliance. De Ctac AI-unit kan hier een begeleidingstraject op ontwikkelen — van gap-analyse tot sandbox-deelname.

---

## 📚 Bronnen & verder lezen

- [Microsoft Build 2026 Blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [GeekWire – Microsoft MAI-modellen](https://www.geekwire.com/2026/microsoft-unveils-seven-homegrown-ai-models-in-bid-for-long-term-self-sufficiency/)
- [TechTimes – Claude in Excel](https://www.techtimes.com/articles/317988/20260608/claude-now-works-inside-excel-microsoft-drops-anthropics-ai-spreadsheet-750-million-people-use)
- [TechTimes – MAI vs. Claude blind test](https://www.techtimes.com/articles/317989/20260608/microsoft-built-its-own-ai-depend-openai-anthropic-less-says-it-just-beat-claude-blind-tests.htm)
- [buildfastwithai.com – AI News June 7, 2026](https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026)
- [VentureBeat – Prompt injection coding agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [airia.com – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [The Hacker News – Google Gemini Calendar flaw](https://thehackernews.com/2026/01/google-gemini-prompt-injection-flaw.html)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [digital-strategy.ec.europa.eu – AI Act guidelines](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [CIO Dive – Microsoft/Google enterprise dominantie](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [llm-stats.com – AI model updates juni 2026](https://llm-stats.com/llm-updates)
