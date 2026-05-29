---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-20
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 20 mei 2026

## 🔑 Highlights van de dag

- **Google I/O 2026 (gisteren):** Google hield gisteren zijn jaarlijkse I/O-keynote met de verwachte onthulling van Gemini 4.0 en Android XR Glasses in samenwerking met Samsung, Warby Parker en XREAL. Dit is het meest bepalende AI-event van de maand.
- **Anthropic lanceert Claude Mythos2 Preview:** Anthropic brengt een nieuw frontier-model uit met bijzondere nadruk op cybersecurity-toepassingen — het model overtreft naar eigen zeggen "all but the most skilled humans" bij het vinden en exploiteren van softwarekwetsbaarheden.
- **Microsoft 365 E7 is live:** Per 1 mei 2026 bundelt Microsoft E5 + Entra Suite + Copilot + Agent 365 in één pakket — een significante stap in de verankering van AI-agents in enterprise-workflows.
- **EU 'AI Omnibus' akkoord bereikt:** Op 7 mei bereikte de EU een politiek akkoord over een vereenvoudiging van de AI Act-implementatie, minder dan drie maanden voor de volledige toepassingsdatum van 2 augustus.
- **Prompt injection als kritieke enterprise-dreiging:** Een nieuwe CVE in Cursor (CVE-2026-22708) en de GeminiJack-kwetsbaarheid in Gemini Enterprise tonen aan dat agentic AI-systemen actief worden aangevallen in productieomgevingen.

---

## 🧠 Technologie & Modellen

**Google Gemini 4.0 & Android XR (Google I/O, 19 mei)**
Googles I/O-keynote stond volledig in het teken van AI: Gemini 4.0-updates, agentic coding en hardware — Android XR Glasses worden gelanceerd in samenwerking met meerdere brillenmerken. Google positioneert zich als de brede AI-platform-speler, zowel in consumenterapparaten als enterprise-infrastructuur.
*[Google I/O 2026 – Buildfastwithai](https://www.buildfastwithai.com/blogs/ai-news-today-may-18-2026)*

**Anthropic Claude Mythos & Mythos2 Preview**
Anthropic bracht Mythos uit als "meest krachtige model tot nu toe" aan een beperkte groep partners, direct gevolgd door Mythos2 Preview. Opmerkelijk: de cybersecurity-capaciteiten worden expliciet beschreven — inclusief het vermogen om kwetsbaarheden beter te vinden dan de meeste menselijke experts. Dit roept tegelijkertijd vragen op over responsible disclosure en dual-use.
*[Anthropic nieuws](https://www.anthropic.com/news) | [TechCrunch](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/)*

**OpenAI: content provenance & Dell-partnerschap**
OpenAI kondigde op 19 mei advances in content provenance aan — relevant voor AI-gegenereerde content authenticiteit. Op 18 mei werd ook een partnerschap met Dell Technologies aangekondigd voor Codex in hybrid/on-premises enterprise-omgevingen.
*[OpenAI nieuws](https://openai.com/news/)*

**Claude Code: rate limits verdubbeld + SpaceX Colossus-deal**
Anthropic verdubbelde de rate limits voor Claude Code op alle betaalde plannen en sloot een deal voor het volledige Colossus 1-supercomputer van SpaceX (220.000+ NVIDIA GPU's). Dit signaleert een stevige schaalstap in inference-capaciteit.

---

## 🏛️ Governance & Ethiek

**EU AI Omnibus: vereenvoudiging op komst**
Op 7 mei werd een politiek akkoord bereikt over de 'AI Omnibus', een wetgevingspakket dat de AI Act-implementatie moet vereenvoudigen. Volledig van toepassing: 2 augustus 2026. De Commissie krijgt dan ook handhavingsbevoegdheden over GPAI-modelproviders.

**Standaardisatieachterstand als risico**
CEN/CENELEC heeft de gevraagde standaarden niet op tijd (augustus 2025) kunnen opleveren. Dit creëert onzekerheid voor bedrijven die op die standaarden wachten voor compliance — met name in sectoren met high-risk AI-toepassingen. Voor Ctac-klanten in zorg, overheid of finance is dit een actief aandachtspunt.
*[EU AI Act tracker](https://artificialintelligenceact.eu/) | [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)*

**Microsoft AI-chief: white-collar automatisering binnen 18 maanden**
Mustafa Suleyman (Microsoft AI) stelt publiekelijk dat alle white-collar werkzaamheden binnen 18 maanden grotendeels door AI geautomatiseerd kunnen worden. Hype of realistische horizon? In elk geval een signaal dat Microsoft intern en extern maximaal op AI-adoptie inzet.
*[Fortune](https://fortune.com/article/why-microsoft-ai-chief-mustafa-suleiman-predicts-ai-automation-18-months/)*

---

## 🔐 Security & Risk

**Prompt injection: structureel probleem bij agentic AI**
Twee recente kwetsbaarheden zijn bijzonder zorgwekkend voor enterprise:
- **CVE-2026-22708 (Cursor):** Remote code execution via indirecte prompt injection in agentic IDE — aanvallers kunnen code laten uitvoeren via kwaadaardige content in bestanden of web-inhoud.
- **GeminiJack:** Kwetsbaarheid in Gemini Enterprise waarbij verborgen instructies in gedeelde documenten, agenda-uitnodigingen of e-mails gevoelige bedrijfsdata kunnen lekken.

NIST bestempelt prompt injection als "generative AI's greatest security flaw" en OWASP plaatst het op #1 in de LLM Top 10. Aanvalsuccespercentages tegen state-of-the-art verdedigingen liggen boven de 85%.

Voor organisaties die AI-coding assistants of enterprise agents uitrollen, zijn input-validatie, sandboxing en regelmatige audits nu geen optie maar vereiste.
*[The Hacker News – OpenClaw](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html) | [VentureBeat – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)*

---

## 📈 Markt & Adoptie

**Microsoft 365 E7 GA (1 mei 2026)**
De bundeling van M365 E5, Entra Suite, Copilot en Agent 365 in één SKU is een strategische zet: Microsoft maakt AI-agents de standaard in enterprise productiviteitssoftware en verlaagt de drempel voor grootschalige adoptie.
*[CIO Dive – Microsoft Google AI market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)*

**Google Agentic Data Cloud + 8e generatie TPU**
Google Cloud lanceerde Agentic Data Cloud — een AI-native data-architectuur die legacy enterprise-platforms omzet naar reasoning engines. Tegelijkertijd werden 8e generatie TPU's aangekondigd die specifiek zijn ontworpen voor de agentic era.
*[Google Cloud Blog – Next '26 wrap-up](https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up)*

**OpenAI breekt exclusiviteit met Microsoft**
Microsoft en OpenAI hebben hun exclusieve deal substantieel aangepast: OpenAI mag zijn modellen voortaan ook via AWS en Google Cloud aanbieden. Dit vergroot de beschikbaarheid maar vermindert Microsofts exclusieve voordeel.
*[VentureBeat](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)*

**Anthropic: $44B ARR + $30B funding-ronde in voorbereiding**
Anthropic rapporteerde een Q1 2026 ARR van $44 miljard (+80x jaar-op-jaar) en is in onderhandeling over een nieuwe ronde van $30 miljard bij een waardering boven $900 miljard. Schaal en momentum zijn hier ondubbelzinnig.

---

## 💡 Ctac-relevantie

**Korte termijn – nu handelen:**
De combinatie van Microsoft 365 E7 GA en de Google Agentic Data Cloud maakt dat klanten van Ctac (met name in enterprise-segmenten) actief keuzes gaan maken over hun AI-agent-infrastructuur. Ctac kan hier directe waarde leveren door implementatiebegeleiding, governance-frameworks en change management — dit is het moment om proposities voor "responsible agent deployment" te concretiseren.

**Compliance deadline nadert:**
Met de EU AI Act volledig van kracht per 2 augustus (nog 74 dagen) en de standaardisatieachterstand bij CEN/CENELEC, is er een acuut gat voor klanten in zorg, overheid en finance. Ctac kan hier positioneren als trusted advisor bij AI-risicoklassificatie en compliancereadiness.

**Security als propositiepijler:**
De toenemende CVE-dichtheid rondom agentic AI-systemen (Cursor, Gemini Enterprise, coding assistants) schept behoefte aan security-by-design begeleiding. Ctac's AI-unit kan een "AI Security Assessment" service ontwikkelen die aansluit bij bestaande security-klantrelaties.

**Meta Avocado-model (verwacht juni):**
Meta's uitgestelde open-source frontier-model verschuift naar juni. Als het uitkomt, vergroot het de keuzeruimte voor on-premises/private deployment — relevant voor klanten met data-soevereiniteitseisen.

---

## 📚 Bronnen & verder lezen

- [Google Cloud Next '26 wrap-up](https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up)
- [AI News Today – May 18, 2026 (buildfastwithai)](https://www.buildfastwithai.com/blogs/ai-news-today-may-18-2026)
- [Anthropic nieuws](https://www.anthropic.com/news)
- [OpenAI nieuws](https://openai.com/news/)
- [EU AI Act tracker – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Governance en handhaving AI Act](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [TechCrunch – Anthropic & OpenAI joint ventures enterprise](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/)
- [VentureBeat – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [The Hacker News – OpenClaw AI agent flaws](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html)
- [VentureBeat – OpenAI & Microsoft exclusiviteitsbreuk](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)
- [CIO Dive – Microsoft Google AI enterprise markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Fortune – Mustafa Suleyman over automatisering](https://fortune.com/article/why-microsoft-ai-chief-mustafa-suleiman-predicts-ai-automation-18-months/)
- [AWS Weekly Roundup – What's Next with AWS 2026](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-whats-next-with-aws-2026-amazon-quick-openai-partnership-and-more-may-4-2026/)
