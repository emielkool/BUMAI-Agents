---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-08
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 8 juni 2026

## 🔑 Highlights van de dag

- **Microsoft lanceert eigen modelfamilie bij Build 2026:** MAI-Thinking-1 is Microsoft's eerste zelfgebouwde reasoning model (35B parameters, 256K context), getraind op commercieel gelicenseerde data — een directe aanval op OpenAI en Google in de enterprise-markt.
- **Prompt injection bereikt kritiek punt:** OpenAI lanceerde 6 juni een 'Lockdown Mode' als reactie op aanhoudende kwetsbaarheden; tegelijkertijd zijn kritieke injectieproblemen ontdekt in Amazon Q, Google Jules én GitHub Copilot — tools die breed ingezet worden bij softwareontwikkeling.
- **EU AI Act deadline nadert:** Volledige toepassing per 2 augustus 2026 (8 weken). Tegelijkertijd bereikte de EU in mei politieke overeenstemming over vereenvoudiging van regels via de 'AI Omnibus'.
- **Google Gemini 3.5 Flash is GA:** Werd officieel beschikbaar op 19 mei bij Google I/O; outperformt Gemini 3.1 Pro op coding- en agentische benchmarks — nu standaard in Gemini-app en AI Mode in Search.
- **AI agent-adoptie verschuift van experiment naar productie:** Zowel internationaal (Writer, Scotty AI) als in Nederland zien we de transitie van pilots naar live enterprise-implementaties, waarbij multi-agentarchitecturen centraal komen te staan.

---

## 🧠 Technologie & Modellen

**Microsoft Build 2026 – eigen modelfamilie**
Microsoft heeft bij Build 2026 (begin juni) zeven nieuwe in-house modellen uitgebracht onder de naam **MAI**. Het vlaggenschip is **MAI-Thinking-1**: een reasoning model van 35B actieve parameters met 256K contextvenster, getraind van scratch op schone, commercieel gelicenseerde data (geen distillatie van andere modellen). In blind tests scoren onafhankelijke beoordelaars het beter dan Claude Sonnet 4.6 en vergelijkbaar met Claude Opus 4.6 op codering. Tevens zijn **MAI-Image-2.5** (text-to-image én image-to-image) en **Work IQ APIs** (GA 16 juni) aangekondigd.
→ [Microsoft Build 2026 blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)

**Google Gemini 3.5 Flash – GA**
Gemini 3.5 Flash combineert frontier intelligence met snelheid en is beschikbaar via de Gemini API, AI Studio en Google Cloud (Antigravity). Meer dan 8,5 miljoen ontwikkelaars bouwen maandelijks met Google's modellen; 375+ Google Cloud-klanten verwerken elk meer dan 1 biljoen tokens per jaar.
→ [Google I/O 2026 announcements](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)

**Anthropic Claude Opus 4.8 & Project Glasswing**
Claude Opus 4.8 verscheen op 28 mei. Anthropic lanceerde tevens 'Claude Mythos' via Project Glasswing — vooralsnog niet publiek beschikbaar. Anthropic publiceert als eerste lab concrete prompt injection failure rates voor enterprise security teams.
→ [OpenAI News](https://openai.com/news/) | [VentureBeat prompt injection metrics](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)

**OpenAI: GPT-Rosalind Biodefense & GPT-4.5 sunset**
OpenAI opende op 1 juni uitgebreide toegang tot GPT-Rosalind specifiek voor biodefence en pandemiepreventie. GPT-4.5 wordt 27 juni uit ChatGPT verwijderd.

---

## 🏛️ Governance & Ethiek

**EU AI Act: volle werking in 8 weken**
De AI Act is volledig van toepassing per **2 augustus 2026** — dat is over minder dan twee maanden. Hoog-risico systemen (biometrie, onderwijs, arbeidsmarkt, grenscontrole) volgen op 2 december 2027. De Europese Commissie werkt in de loop van 2026 aan praktische guidelines rond hoog-risicoclassificatie en transparantievereisten (art. 50 AI Act).

**AI Omnibus: vereenvoudiging**
In mei 2026 werd politieke overeenstemming bereikt over gerichte wijzigingen in de AI Act ('AI Omnibus') als onderdeel van het digitale vereenvoudigingspakket. Het doel is regeldruk te verlagen voor mkb en innovatieve aanbieders zonder de kernwaarborgen aan te tasten.
→ [EU AI Act tracker](https://artificialintelligenceact.eu/) | [EC AI governance](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

---

## 🔐 Security & Risk

**OpenAI Lockdown Mode (6 juni 2026)**
OpenAI introduceerde Lockdown Mode als extra beschermingslaag tegen prompt injection — aanvallen waarbij kwaadaardige instructies verstopt zitten in webpagina's, e-mails of geüploade bestanden. OpenAI erkent expliciet dat ChatGPT kwetsbaar blijft voor injecties via gecachte webcontent.
→ [TechCrunch: OpenAI Lockdown Mode](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/)

**Brede kwetsbaarheden in AI coding tools**
Kritieke prompt injection-kwetsbaarheden zijn ontdekt in **Amazon Q Developer, Google Jules, GitHub Copilot** en tientallen andere AI-ontwikkelplatforms. Een recente VentureBeat-analyse toont hoe drie AI coding agents via één enkele injectie geheimen uitlekten. OWASP benoemt prompt injection als het **#1 risico** voor LLM-gebaseerde applicaties.
→ [VentureBeat: AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [Airia: AI Security in 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)

---

## 📈 Markt & Adoptie

**Microsoft en Google domineren enterprise AI-markt**
Volgens CIO Dive zijn Microsoft en Google de dominante leveranciers voor enterprise AI. Microsoft heronderhandelt haar partnerschap met OpenAI voor meer cloudflexibiliteit — een teken dat het eigen modelaanbod (MAI-familie) serieus genomen wordt als concurrent.
→ [CIO Dive: Microsoft/Google rule AI market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

**AI agent-platforms winnen terrein**
Writer lanceerde AI-agents die proactief handelen zonder prompts, in directe concurrentie met Amazon, Microsoft en Salesforce. In Nederland is het Utrechtse **Scotty AI** (opgericht 2023) al live in productie bij HR, logistiek, retail, overheid en evenementen — in 16 maanden.
→ [VentureBeat: Writer AI agents](https://venturebeat.com/technology/writer-launches-ai-agents-that-can-act-without-prompts-taking-on-amazon-microsoft-and-salesforce) | [Computable: maatwerk AI NL](https://www.computable.nl/persberichten/maatwerk-ai-in-de-nederlandse-tech-sector-van-experiment-naar-onmisbare-sta/)

**Marktfocus verschuift naar contextkwaliteit**
Computable signaleert een fundamentele verschuiving: organisaties willen geen generieke AI meer, maar systemen die passen bij hun eigen processen en taal. De concurrentie verschuift van 'toegang tot technologie' naar 'kwaliteit van toepassing'.

---

## 💡 Ctac-relevantie

**1. Microsoft MAI-Thinking-1 is een propositiekans.** Het model is getraind op commercieel gelicenseerde data — een argument voor compliance-gevoelige sectoren (overheid, zorg, finance). Als Microsoft-partner heeft Ctac de kans om Work IQ APIs en MAI-modellen vroegtijdig te verkennen en te vertalen naar klantproposities.

**2. EU AI Act deadline (2 augustus) is een directe selling trigger.** Klanten die nog geen AI-risicoclassificatie hebben uitgevoerd of geen transparantiedocumentatie hebben, zitten in de gevarenzone. Ctac kan hier nu actief mee aan de slag: een quick scan of readiness check als laagdrempelig instapproduct.

**3. Prompt injection in GitHub Copilot is een direct risico voor Ctac-klanten.** Klanten die GitHub Copilot of Amazon Q inzetten voor softwareontwikkeling zijn kwetsbaar. Dit is een concrete aanleiding voor een security-review dienst of awareness-sessie rond AI-ontwikkeltools.

**4. Van maatwerk-experiment naar productie:** De Nederlandse markt toont dat de race om AI-adoptie versnelt. Ctac's positie in custom softwareontwikkeling past perfect bij de verschuiving richting 'op maat afgestemde AI'. Dit is het moment om referentiecases te bouwen en zichtbaar te maken.

---

## 📚 Bronnen & verder lezen

- [Microsoft Build 2026: Be yourself at work](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [Google I/O 2026 – 100 announcements](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [OpenAI Lockdown Mode – TechCrunch](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/)
- [VentureBeat: AI agent runtime security & prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Anthropic prompt injection failure rates – VentureBeat](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)
- [Airia: AI Security in 2026 – Prompt Injection & the Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [EC: Supporting AI Act implementation](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [CIO Dive: Microsoft en Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive: Microsoft-OpenAI partnerschap heronderhandeld](https://www.ciodive.com/news/microsoft-openai-rework-partnership/818606/)
- [VentureBeat: Writer AI agents](https://venturebeat.com/technology/writer-launches-ai-agents-that-can-act-without-prompts-taking-on-amazon-microsoft-and-salesforce)
- [Computable: maatwerk AI in Nederlandse tech-sector](https://www.computable.nl/persberichten/maatwerk-ai-in-de-nederlandse-tech-sector-van-experiment-naar-onmisbare-sta/)
- [Computable: Anthropic & AI nieuws NL](https://www.computable.nl/2026/06/05/kort-anthropic-bang-van-zich-zelf-verouderde-facturatie-werkt-wanbetaling-in-de-hand-en-meer/)
