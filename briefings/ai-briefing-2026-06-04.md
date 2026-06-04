---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-04
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 4 juni 2026

## 🔑 Highlights van de dag

- **Gemini 3.5 Flash is vandaag GA**: Google's nieuwe agentic-first model levert frontier-niveau intelligentie op viermaal de snelheid van vergelijkbare modellen, en is nu live in de Gemini API, Gemini Enterprise en de Gemini-app wereldwijd.
- **EU AI Act countdown**: Met de volledige toepassingsdatum op 2 augustus 2026 is er nu minder dan twee maanden tijd — de stakeholderconsultatie over de richtlijnen sluit op 23 juni 2026.
- **"Comment and Control" aanval treft drie coding agents tegelijk**: Claude Code, Gemini CLI én Copilot bleken kwetsbaar voor een enkelvoudige prompt-injection die secrets lekt — een wake-up call voor teams die AI in hun development-workflow gebruiken.
- **Microsoft onthult eigen AI-modellen**: Op de Build-conferentie presenteerde Microsoft MAI-Code-1-Flash, zijn eerste eigen coderingsmodel, als antwoord op afhankelijkheid van OpenAI, Anthropic en Google.
- **Twee derde van bedrijven zit nog vast in pilotfase**: Ondanks miljarden aan investeringen slaagt de meerderheid van ondernemingen er niet in generatieve AI structureel in productie te brengen.

---

## 🧠 Technologie & Modellen

**Gemini 3.5 Flash (Google, GA 4 juni 2026)**
Google lanceerde vandaag Gemini 3.5 Flash als het standaardmodel in de Gemini-app en in AI Mode in Search wereldwijd. Het model scoort 76,2% op Terminal-Bench 2.1, 83,6% op MCP Atlas en 84,2% op CharXiv Reasoning (multimodaal). Prijskaartje: $1,50 per 1M input-tokens, $9 per 1M output-tokens. Bijzonder: het model kan zelfstandig codeerpipelines uitvoeren en heeft in interne tests een volledig besturingssysteem gebouwd. Google's strategie verschuift duidelijk van chatbot-AI naar agentic-AI. ([TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/), [Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/))

**Claude Opus 4.8 (Anthropic, mei 2026)**
Uitgebracht slechts 41 dagen na Opus 4.7, behaalt Opus 4.8 88,6% op SWE-bench Verified en 74,6% op Terminal-Bench 2.1. Nieuw: parallelle subagent-workflows en een 2,5x fast mode. Anthropic hintte op de komst van Mythos-class modellen voor alle klanten "binnen enkele weken". ([TechCrunch](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/))

**Microsoft MAI-Code-1-Flash**
Op Microsoft Build kondigde Microsoft zijn eerste eigen coderingsmodel aan: MAI-Code-1-Flash genereert broncode op basis van tekstbeschrijvingen. Het is een expliciete stap om minder afhankelijk te worden van OpenAI en tegelijkertijd de kosten voor developers te verlagen. ([CNBC](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html))

**Open source: DeepSeek-V4-Pro & GLM-5**
In het open-source landschap zijn twee nieuwe topdelers verschenen: DeepSeek-V4-Pro (1,6T parameters, 49B actief, 1M contextvenster) en GLM-5 van het Chinese Tsinghua (744B MoE, #1 open model op LMArena). Open-weight modellen zijn voor coding, reasoning en agentic werkstromen inmiddels serieus productiewaardig. ([Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro), [Hugging Face blog](https://huggingface.co/blog/mlabonne/glm-5))

---

## 🏛️ Governance & Ethiek

**EU AI Act: minder dan 60 dagen tot volledige toepasselijkheid**
Op 2 augustus 2026 wordt de AI Act volledig van kracht. Het politiek akkoord over de "AI Omnibus" – een pakket gerichte wijzigingen – werd bereikt op 7 mei 2026. Regels voor high-risk toepassingen in producten (liften, speelgoed) gelden pas per 2 augustus 2028. De Europese AI Office heeft een stakeholderconsultatie lopen over conceptrichtlijnen voor high-risk classificatie, transparantievereisten en incidentrapportage — deadline **23 juni 2026**. ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines), [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/))

Oordeel: De deadline is echt. Organisaties die nu nog geen compliance-traject hebben gestart, lopen achter. Voor Ctac-klanten in de publieke sector en zorg is dit urgent.

---

## 🔐 Security & Risk

**"Comment and Control" – drie coding agents tegelijk gecompromitteerd**
Onderzoekers onthulden een prompt-injection aanval die Claude Code, Gemini CLI en Copilot tegelijk treft. Via een kwaadaardige commentaarregel in een ogenschijnlijk onschuldig bestand kunnen AI-agents worden gemanipuleerd om secrets te exfiltreren. Het vergt geen expliciete gebruikersactie — een pull van een kwaadaardig package volstaat. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**IDEsaster: 30+ kwetsbaarheden in AI-IDE's**
Veiligheidsonderzoekers documenteerden meer dan 30 flaws in AI-gedreven ontwikkelomgevingen, waaronder kritieke CVE's in Cursor (remote code execution, CVE-2026-22708) en Microsoft Copilot Studio (CVE-2026-21520). Meta-analyse van 78 recente studies toont aan dat aanvalssuccespercentages bij adaptieve aanvallen boven de 85% uitkomen. ([The Hacker News](https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html), [arXiv](https://arxiv.org/pdf/2601.17548))

---

## 📈 Markt & Adoptie

**Google Cloud passeert $20 miljard in Q1 2026**
Google Cloud rapporteerde voor het eerst een kwartaalomzet boven de $20 miljard, gedreven door AI-adoptie. Gemini Enterprise groeide 40% kwartaal-op-kwartaal in betaalde maandelijkse actieve gebruikers. ([CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/))

**Agentic AI markt: van $9 miljard naar $139 miljard in 2034**
Fortune Business Insights projecteert een CAGR van 40,5% voor de global agentic AI markt. Google lanceerde daartoe de "Agentic Data Cloud" als enterprise-fundament voor AI-agent deployments. ([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))

**Twee derde van bedrijven zit vast in pilotfase**
Ondanks miljarden aan investeringen in AI-infrastructuur slaagt de meerderheid van enterprise-organisaties er niet in generatieve AI structureel in productie te brengen. De kloof tussen pilot en productie blijft het dominante adoptie-knelpunt in 2026. ([CIO Dive](https://www.ciodive.com/news/microsoft-ai-investments-questions-strategy/810906/))

---

## 💡 Ctac-relevantie

**EU AI Act deadline is nu operationeel**: Met minder dan 60 dagen tot 2 augustus is dit het moment voor Ctac om klanten actief te benaderen met compliance-assessments, vooral in de publieke sector en zorg. De stakeholderconsultatie (sluit 23 juni) biedt ook een inhoudelijk aanknopingspunt om voorop te lopen.

**Agentic AI als propositiepijler**: De release van Gemini 3.5 Flash en Opus 4.8 – beide expliciet gepositioneerd als agentic-first – bevestigen de richtingsverschuiving in de markt. Ctac kan hier concreet mee aan de slag: van chatbot-PoC's naar productie-agents die workflows autonoom uitvoeren.

**Security van AI-coding tools is onderschat risico**: De "Comment and Control"-aanval laat zien dat AI-coding assistants (die Ctac-teams en klanten al gebruiken) actieve aanvalsvectoren zijn. Een interne richtlijn over veilig gebruik van Claude Code, Copilot e.d. is nu verstandig — ook als differentiator richting klanten.

**Pilotfase-kloof = dienstverlening kans**: Twee derde van bedrijven slaagt er niet in AI van pilot naar productie te brengen. Dit is precies de gap waar Ctac's combinatie van technische delivery en strategisch advies waardevol is.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Gemini 3.5 Flash: Google bets on agents, not chatbots](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/)
- [Google Blog – Gemini 3.5 modellen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)
- [TechCrunch – Anthropic Opus 4.8](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/)
- [CNBC – Microsoft MAI-Code-1-Flash](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)
- [Hugging Face – DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [Hugging Face Blog – GLM-5](https://huggingface.co/blog/mlabonne/glm-5)
- [EU Digital Strategy – AI Act richtlijnen](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [EU AI Act tracker – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [VentureBeat – Comment and Control aanval](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [The Hacker News – IDEsaster kwetsbaarheden](https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html)
- [CIO Dive – Google Cloud boven $20 miljard](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [CIO Dive – Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [CIO Dive – twee derde zit vast in pilotfase](https://www.ciodive.com/news/microsoft-ai-investments-questions-strategy/810906/)
