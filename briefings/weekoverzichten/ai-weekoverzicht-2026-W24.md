---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W24
Periode: 2026-06-08 / 2026-06-14
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 24, 2026

> Synthese van de dagbriefings van 8 juni t/m 11 juni 2026.
> Briefing voor vrijdag 12 juni was niet beschikbaar op moment van opstellen.

---

## Overzicht van de week

---

### Maandag 8 juni

→ Dagbriefing: [ai-briefing-2026-06-08.md](../ai-briefing-2026-06-08.md)

**Highlights:**
- Microsoft lanceerde bij Build 2026 zeven eigen MAI-modellen, waaronder MAI-Thinking-1 — hun eerste zelfgebouwde reasoning model (35B parameters, 256K context). Dit is een directe aanval op OpenAI's enterprise-positie.
- Prompt injection bereikte een kritiek punt: OpenAI introduceerde 'Lockdown Mode' als reactie op kwetsbaarheden die gevonden zijn in Amazon Q, Google Jules en GitHub Copilot tegelijkertijd.
- EU AI Act volledige toepasselijkheid nadert (2 augustus 2026, nog 8 weken), terwijl de 'AI Omnibus' tegelijk regeldruk verlichtte voor het mkb.

**Ctac-relevantie van de dag:** Microsoft's eigen modelfamilie via Azure Foundry vergroot de multi-vendor-opties voor Ctac-klanten; de koppeling van AI-agents aan productie-workflows versnelt en vraagt nu om concrete security-baselines in DevSecOps-trajecten.

---

### Dinsdag 9 juni

→ Dagbriefing: [ai-briefing-2026-06-09.md](../ai-briefing-2026-06-09.md)

**Highlights:**
- Claude is geïntegreerd in Excel Agent Mode — een product dat naar schatting 750 miljoen mensen gebruiken. Dit is een stille maar strategisch significante adoptiedoorbraak voor Anthropic in de enterprise-massa.
- Anthropic diende vertrouwelijk haar IPO-aanvraag in na een Series H van $65 mrd (waardering $965 mrd), gedreven door de commerciële groei van Claude Code.
- Open-source modellen (Kimi K2.6, DeepSeek-V4-Pro) halen closed-source bij op coding en agentic benchmarks — relevant voor enterprise-architecten die platformkosten willen beheersen.

**Ctac-relevantie van de dag:** De Claude-Excel-integratie maakt AI toegankelijk voor niet-technische eindgebruikers bij klanten in finance en overheid; open-weight alternatieven worden serieuze keuze voor zelf-hostende klanten die kosten of dataprivacy zwaar laten wegen.

---

### Woensdag 10 juni

→ Dagbriefing: [ai-briefing-2026-06-10.md](../ai-briefing-2026-06-10.md)

**Highlights:**
- Een architectuurfout in Anthropic's MCP SDK's treft 7.000+ publieke servers en meer dan 150 miljoen downloads; het Pentagon bestempelde Anthropic voor het eerst als "supply chain risk" — een acuut risico voor agentic AI-deployments.
- Google Cloud rapporteerde 63% omzetgroei naar $20 mrd met Gemini Enterprise +40% betaalde MAU; op agentic AI wint Google terrein op Microsoft.
- De EU AI Act Omnibus verschuift hoog-risico deadlines naar december 2027 en augustus 2028, maar de kerntoepassing per 2 augustus 2026 (inclusief GPAI) staat vast.

**Ctac-relevantie van de dag:** De MCP-kwetsbaarheid raakt elke organisatie die Anthropic-tooling inzet als agentic orchestratie-laag; Ctac-teams moeten MCP-servers die in productie draaien actief inventariseren en beveiligen — dit is ook een dienst die Ctac richting klanten kan aanbieden.

---

### Donderdag 11 juni

→ Dagbriefing: [ai-briefing-2026-06-11.md](../ai-briefing-2026-06-11.md)

**Highlights:**
- Anthropic Project Glasswing geeft een select groep strategische partners (AWS, Apple, Cisco, Google, JPMorgan Chase, Microsoft) vroegtijdige toegang tot *Claude Mythos Preview* — een nog niet publiek gelanceerd frontier model dat de huidige Claude-lijn overstijgt.
- CVE-2025-53773 (CVSS 9.6) toont remote code execution via verborgen prompt injection in GitHub pull request-beschrijvingen met GitHub Copilot, samen met kritieke Semantic Kernel-kwetsbaarheden die agents in dat framework direct bedreigen.
- Trump ondertekende een executive order die AI-bedrijven vraagt frontier modellen 30 dagen vóór release aan federale instanties te geven — een precedent dat het internationale governance-debat zal beïnvloeden.

**Ctac-relevantie van de dag:** De EU AI Act Code of Practice voor content-labeling wordt deze maand gepubliceerd en de volledige wet geldt per 2 augustus — klanten in overheid, zorg en finance hebben nú advies nodig; de GitHub Copilot-kwetsbaarheid vraagt directe actie in lopende DevSecOps-trajecten.

---

### Vrijdag 12 juni

*(geen briefing beschikbaar voor deze dag)*

---

## 🏆 Weekhighlights

- **Microsoft breekt definitief met OpenAI-afhankelijkheid.** Bij Build 2026 lanceerde Microsoft zeven eigen MAI-modellen — met MAI-Thinking-1 als eerste zelfgebouwde reasoning model (35B, 256K context, getraind op commercieel gelicenseerde data). In blind tests scoort het vergelijkbaar met Claude Opus 4.8. Dit is geen experiment: het signaleert een strategische koerswijziging waarbij Microsoft zichzelf als volwaardig modellab positioneert naast OpenAI. Voor enterprise-klanten op het Microsoft-platform verandert de leverancierskeuze.

- **Prompt injection bereikte de productiedrempel.** Twee op elkaar gestapelde events markeren een keerpunt: OpenAI lanceerde Lockdown Mode (6 juni) en CVE-2025-53773 (CVSS 9.6) bewijst dat verborgen injectie via GitHub PR-beschrijvingen leidt tot remote code execution via Copilot. Tegelijkertijd treft een MCP-architectuurfout 7.000+ servers en 150M+ downloads. Prompt injection is niet langer theoretisch — het is gedocumenteerd misbruikt in productie. OWASP #1, +340% YoY.

- **EU AI Act: 8 weken resterende, compliance-kloof bij klanten.** De volledige toepasselijkheid per 2 augustus 2026 is ongewijzigd. De AI Omnibus verlichtte de Annex III-deadline (naar dec. 2027), maar de GPAI-verplichtingen golden al en de Code of Practice voor content-markering wordt déze maand gepubliceerd. De meeste klanten in overheid, zorg en finance zijn nog niet klaar — dit is een acuut adviesvenster voor Ctac.

- **Anthropic versnelt richting enterprise én beurs.** Claude is nu ingebouwd in Excel (750 miljoen gebruikers). Anthropic diende vertrouwelijk haar IPO-aanvraag in na een waardering van $965 miljard. Project Glasswing geeft strategische partners (AWS, Apple, Google, Microsoft) vroegtijdig toegang tot het nog niet publieke Mythos-model. Claude is geen niche-tool meer — het is enterprise-infrastructuur geworden.

- **Agentic AI gaat van belofte naar productie.** Gartner voorspelt dat 40% van enterprise-applicaties eind 2026 AI-agents bevat. Google lanceerde de Agentic Data Cloud; Microsoft brengt Agent 365 GA. De markt groeit van $7,8 mrd nu naar $52 mrd in 2030. Tegelijk zit twee derde van enterprises nog vast in de pilotfase — de pilot-naar-productie kloof is het centrale implementatievraagstuk van dit moment.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De week stond in het teken van platformconsolidatie en modelproliferatie tegelijk. Microsoft's 7-modellen-offensief bij Build 2026 is de meest structurele verschuiving: voor het eerst bouwt een cloudleverancier een complete, zelfstandige modellenfamilie die direct concurreert met zijn eigen strategische partners (OpenAI, Anthropic). Azure Foundry met 11.000+ modellen is bewust vendor-agnostisch ingericht. Het tijdperk van "één model per leverancier" is voorbij — enterprise-klanten moeten straks kiezen uit een matrix van modellen per taak, provider en compliance-profiel.

Tegelijkertijd bewijst de week dat open-source een serieuze keuze is geworden. Kimi K2.6 en DeepSeek-V4-Pro presteren top op coding en reasoning. Claude in Excel en Anthropic's IPO-traject bevestigen dat de markt consolideert rond twee lagen: commoditymodellen voor standaardtaken en frontier-modellen (Mythos Preview, MAI-Thinking-1) voor gespecialiseerde of risicovolle toepassingen.

### 🏛️ Governance & Beleid

De governance-week kende twee gezichten. Enerzijds verlichting: de AI Omnibus verschuift Annex III-deadlines en geeft organisaties extra tijd voor de zwaarste compliance-eisen. Anderzijds onveranderlijk: 2 augustus 2026 staat vast. GPAI-verplichtingen zijn van kracht; de Code of Practice voor content-markering wordt nu gepubliceerd. Het netto-effect: de tijdsdruk voor brede organisaties verschuift naar specifieke use cases — maar wie nu wacht, riskeert handhaving op GPAI-blootstelling die al actief is.

De Trump executive order (30 dagen pre-release disclosure) is politiek Amerikaans maar strategisch mondiaal: het normaliseert overheidstoezicht op frontier modellen. De Europese AI-waakhond met 60 wetenschappers versterkt dit beeld. Regulering is geen bedreiging die "nog komt" — het is operationeel.

### 🔐 Security & Risk

Dit was de zwaarste security-week van 2026 tot nu toe. Drie lagen versterken elkaar: (1) MCP-architectuurfout treft de agentic tooling-stack fundamenteel (7.000+ servers, 150M+ downloads, 492 servers zonder authenticatie); (2) CVE-2025-53773 bewijst RCE via Copilot in dagelijkse CI/CD-workflows; (3) Semantic Kernel-CVE's raken de Microsoft-orchestratie-laag. Prompt injection groeit +340% YoY en is OWASP #1.

Het Pentagon-oordeel ("Anthropic = supply chain risk") is een signaal dat de sector niet kan negeren. Organisaties die MCP-servers in productie draaien zonder authenticatie zijn objectief kwetsbaar. Het probleem is niet meer "AI security is complex" — het is "AI security is nu acuut en documenteerbaar uitgebuit." Elke agentic deployment zonder security baseline is een risico dat bestuurders persoonlijk kunnen aanspreken.

### 📈 Markt & Adoptie

Microsoft en Google domineren de enterprise-markt op omvang (Azure +39%, Google Cloud +63%), maar de strategische winst valt niet bij één speler. Anthropic heeft met Claude in Excel en het IPO-traject een adoptiedrempel bereikt die eerder alleen OpenAI had: onderdeel van de infrastructuur waarop 750 miljoen mensen dagelijks werken.

Het meest relevante marktsignaal voor dienstverleners: twee derde van enterprises zit nog in de pilotfase terwijl agentic AI productierijp is verklaard door de grootste leveranciers. De adoptiedrempel is niet technisch maar organisatorisch — data-architectuur, integratie, governance, change. Dat is het speelveld van een implementatiepartner, niet van een modelleverancier.

---

## 💼 Ctac-weekperspectief

- **EU AI Act compliance is nú het gesprek, niet volgende maand.** De deadline van 2 augustus is zeven weken weg. De GPAI Code of Practice wordt déze maand gepubliceerd. Klanten in overheid, finance en zorg die AI-gegenereerde content publiceren of GPAI-modellen inzetten, moeten dit nu in kaart hebben. Een snelle readiness-scan (classificatie, documentatieplicht, transparantievereisten) is direct inzetbaar als Ctac-propositie — laagdrempelig instappunt, hoge urgentie bij klant.

- **MCP-kwetsbaarheid vraagt directe inventarisatie bij lopende projecten.** Elke Ctac-delivery die MCP-servers of agentic AI-workflows gebruikt, moet worden geauditeerd op authenticatiegaten en tool poisoning-blootstelling. CVE-2025-53773 (GitHub Copilot) en de Semantic Kernel-CVE's raken ook standaard DevSecOps-tooling. Intern kwaliteitsvereiste én extern verkoopargument: Ctac kan AI security reviews aanbieden als onderdeel van bestaande AI-implementatietrajecten.

- **Positioneer Ctac als multi-model architect, niet als enkelvoudige leverancier.** Microsoft's Azure Foundry (11.000+ modellen), MAI-Thinking-1 op commercieel gelicenseerde data, Claude in Excel en open-weight alternatieven betekenen dat enterprise-klanten binnenkort modelkeuzes moeten maken per use case, compliance-profiel en kostenstructuur. Ctac's waarde zit in de onafhankelijkheid: advies over welk model wanneer, inclusief governance en risicoafweging. Dat is niet iets dat hyperscalers kunnen leveren.

- **Pilot-naar-productie is het centrale gesprek voor H2 2026.** Gartner's 40%-agents-prognose en Google's Agentic Data Cloud bevestigen: agentic AI is klaar voor productie. De bottleneck zit bij organisaties zelf. Ctac's combinatie van custom software, data-architectuur en change management is precies wat nodig is voor die overgang. Bouw nu referentiecases in één of twee sectoren (gemeente, finance, zorg) en maak ze actief zichtbaar — dit is het onderscheidend vermogen voor 2026-H2.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Microsoft Build 2026 Blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [GeekWire – Microsoft 7 MAI-modellen](https://www.geekwire.com/2026/microsoft-unveils-seven-homegrown-ai-models-in-bid-for-long-term-self-sufficiency/)
- [TechTimes – MAI-Thinking-1 vs. Claude blind test](https://www.techtimes.com/articles/317989/20260608/microsoft-built-its-own-ai-depend-openai-anthropic-less-says-it-just-beat-claude-blind-tests.htm)
- [TechTimes – Claude in Excel](https://www.techtimes.com/articles/317988/20260608/claude-now-works-inside-excel-microsoft-drops-anthropics-ai-spreadsheet-750-million-people-use)
- [CNBC – Microsoft MAI-Code-1-Flash](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)
- [CNBC – Microsoft & Google vs Anthropic & OpenAI in coding](https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html)
- [Google I/O 2026 – 100 announcements](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [LLM Stats – AI model updates juni 2026](https://llm-stats.com/ai-news)
- [WaveSpeed – June 2026 AI Launch Wave](https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Anthropic Newsroom](https://www.anthropic.com/news)
- [buildfastwithai.com – AI News June 7, 2026](https://www.buildfastwithai.com/blogs/ai-news-today-june-7-2026)
- [GeekWire – Microsoft Copilot multi-model era](https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/)

**Governance & Beleid**
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act Omnibus analyse – verifywise.ai](https://verifywise.ai/blog/eu-ai-act-omnibus-what-changed)
- [GPAI Code of Practice introductie](https://artificialintelligenceact.eu/introduction-to-code-of-practice/)
- [EC – Supporting AI Act implementation](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [EC – AI Act enforcement expert support](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support)
- [White House – AI Innovation and Security EO](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)
- [LegalNodes – EU AI Act 2026 Updates](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)

**Security & Risk**
- [TechCrunch – OpenAI Lockdown Mode](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/)
- [SecurityWeek – MCP by-design flaw](https://www.securityweek.com/by-design-flaw-in-mcp-could-enable-widespread-ai-supply-chain-attacks/)
- [The Hacker News – Anthropic MCP RCE vulnerability](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)
- [CSA Research Note – MCP Security Crisis](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-security-crisis-20260504-csa-styled/)
- [Microsoft Security Blog – RCE in AI agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [CrowdStrike – Indirect Prompt Injection](https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/)
- [VentureBeat – AI agent runtime security & prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Airia – AI Security 2026: Prompt Injection & de Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Anthropic – prompt injection failure rates (VentureBeat)](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)

**Markt & Adoptie**
- [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [VentureBeat – Microsoft Agent 365 GA](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [VentureBeat – Writer AI agents](https://venturebeat.com/technology/writer-launches-ai-agents-that-can-act-without-prompts-taking-on-amazon-microsoft-and-salesforce)
- [Morning Consult – Enterprise AI MKB perceptie](https://morningconsult.com/articles/enterprise-ai-smb-brand-perception-2026)
- [Firecrawl – Agentic AI Trends 2026](https://www.firecrawl.dev/blog/agentic-ai-trends)
- [Tech Insider – Microsoft AI spending Azure Copilot 2026](https://tech-insider.org/microsoft-ai-spending-azure-copilot-2026/)
- [Computable – maatwerk AI in Nederlandse tech-sector](https://www.computable.nl/persberichten/maatwerk-ai-in-de-nederlandse-tech-sector-van-experiment-naar-onmisbare-sta/)
