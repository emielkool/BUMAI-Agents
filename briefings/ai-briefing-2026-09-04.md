---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-04
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 4 september 2026

## 🔑 Highlights van de dag

- **OpenAI lanceert GPT-6 Astra** en claimt daarmee het AGI-tijdperk te hebben ingeluid: het model voert autonome multi-step taken uit op desktops, browsers en spreadsheets, en scoort voor het eerst "Critical" op cyberbeveiligingsvermogen.
- **Anthropic brengt Fable 5.1 & Mythos 5.1 uit** met 75% lagere cache-kosten en soepelere safeguards — een directe aanval op enterprise-adoptiedrempels die tot nu toe te hoog waren.
- **EU AI Act volledig van kracht** sinds 2 augustus: transparantieverplichtingen voor chatbots en deepfake-labeling zijn nu afdwingbaar, en nationale toezichthouders hebben handhavingsbevoegdheid gekregen.
- **CrowdStrike lanceert SafeMind**, een duaal agentic AI-systeem voor cybersecurity, met een offensief én defensief model die in een gesloten lus samenwerken.
- **Prompt injection-aanvallen nemen toe**: agressors compromitteerden AI-tools bij 90+ organisaties; de nieuwste agentic systemen bieden aanvallers nog meer toegang dan hun voorgangers.

## 🧠 Technologie & Modellen

**GPT-6 Astra (OpenAI, 3 september)** is de meest ambitieuze AI-release tot nu toe. Het model kan zelfstandig werken in browsers, desktopapplicaties en spreadsheets — geen instructies meer nodig per stap, maar volledig autonome workflows. Op OSWorld 2.0 scoort Astra 72,6% in gemiddeld 40 minuten per taak, 47% sneller dan GPT-5.6. OpenAI claimt dit het begin van AGI te zijn. Sceptici wijzen op het selectieve rollout-beleid (Trusted Access Program) en de controversiële cybersecurity-capaciteiten. De lancering volgt op GPT-5.6 van juli en is duidelijk bedoeld om het momentum na Anthropics recente releases te hervatten.

**Anthropic Fable 5.1 & Mythos 5.1 (1 september)** brengen twee concrete verbeteringen: cache reads dalen van $1,00 naar $0,25 per miljoen tokens (−75%), waardoor agentische workloads tot 45% goedkoper worden. Bovendien introduceert Anthropic *zero data retention* — enterprise-klanten kunnen modellen draaien op eigen infrastructuur zonder data-uitstroom. De safeguards zijn aangescherpt om false positives te verminderen, wat praktische toepasbaarheid vergroot.

**Quasar 438B (Multiverse Computing)**: Europees redeneermodel van 400B+ parameters, gepresenteerd als het best scorende Europese AI-systeem. Relevant als signaal dat EU-gebaseerde alternatieven aan slagkracht winnen — al vraagt onafhankelijke benchmarkverificatie aandacht.

*Bronnen: [TechCrunch – Astra](https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/) | [OpenAI GPT-6 Astra](https://openai.com/index/gpt-6-astra/) | [TechCrunch – Fable 5.1](https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/) | [VentureBeat – Fable 5.1](https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads) | [Anthropic – Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)*

## 🏛️ Governance & Ethiek

**EU AI Act volledig actief** — vanaf 2 augustus zijn alle vier de handhavingspijlers operationeel: (1) het verbod op onaanvaardbare AI-praktijken, (2) verplichte transparantie voor chatbots en deepfake-content, (3) toezicht door de AI Office op GPAI-modellen, en (4) nationale bevoegde autoriteiten voor hoog-risico AI-systemen. Nederland en België vallen als lidstaten volledig onder dit regime. De AI Omnibus (Digital Simplification Package) van juni 2026 — gericht op vereenvoudiging voor innovatie — trad op 27 juli in werking.

De transparantieverplichting is direct zichtbaar: chatbots moeten zich identificeren als AI, en gegenereerde of gemanipuleerde media moeten worden gelabeld als deepfake. Organisaties die dit niet implementeren lopen nu reëel handhavingsrisico.

*Bronnen: [EC – AI Act enforcement 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) | [EC – Governance & enforcement](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)*

## 🔐 Security & Risk

**GPT-6 Astra en cybersecurity-capaciteiten**: Astra is het eerste OpenAI-model dat de classificatie "Critical" haalt binnen hun Preparedness Framework — het kan zonder menselijke sturing zero-day kwetsbaarheden ontdekken en exploiteren. OpenAI publiceert een gedetailleerde safety overview en werkt alleen met geselecteerde organisaties in een Trusted Access Program. Dit is geen hype: het is een fundamentele verandering in het dreigingslandschap voor red-teaming en security-operaties.

**CrowdStrike SafeMind**: Een duaal agentic systeem waarbij Red Tempest (offensief, getraind op 15 jaar incident response) en Blue Solano (defensief, patches kwetsbaarheden) in een gesloten lus opereren. Interessant concept, maar onafhankelijke audit-data over effectiviteit ontbreekt vooralsnog.

**Prompt injection-dreiging escaleert**: Aanvallers hebben AI-tools bij meer dan 90 organisaties gecompromitteerd. De nieuwe generatie agentic systemen heeft meer privileges dan hun voorgangers — dezelfde aanvalsvector heeft nu hogere impact. OWASP rankt prompt injection al twee edities als #1 LLM-kwetsbaarheid. Microsoft patchte een Copilot Studio kwetsbaarheid (CVE-2026-21520, CVSS 7.5) waarbij data toch uitlekte ondanks de patch.

*Bronnen: [OpenAI – Safety overview Astra](https://openai.com/index/safety-overview-gpt-6-astra/) | [VentureBeat – SafeMind](https://venturebeat.com/security/adversaries-hijacked-ai-security-tools-at-90-organizations-the-next-wave-has-write-access-to-the-firewall) | [VentureBeat – Copilot Studio](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook) | [VentureBeat – Prompt injection enterprise](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)*

## 📈 Markt & Adoptie

**Microsoft** rapporteert meer dan 20 miljoen betaalde M365 Copilot-seats — het aantal klanten met meer dan 50.000 seats verviervoudigde jaar-op-jaar. De AI-omzet op jaarbasis groeide 123% naar meer dan $37 miljard.

**Dell** boekte Q2 FY27-inkomsten van $46,97 miljard (+58% YoY), waarvan $16,4 miljard uit AI-servers en een recordorder-boekhouding van $60,9 miljard. Dit bevestigt dat AI-hardware-infrastructuur niet afkoelt.

**Uitdaging bij enterprise-adoptie**: Twee derde van de bedrijven zit nog vast in de pilotfase en heeft moeite om AI-tools in productie te brengen; bijna 97% kampt met het aantonen van business value. Dit is een structurele rem — technologie is niet de bottleneck.

**AWS & Google Multi-cloud**: AWS en Google werken samen aan vereenvoudigd multi-cloud deployment, een signaal dat hybride omgevingen de standaard worden voor enterprise AI-hosting.

*Bronnen: [CIO Dive – Microsoft Google marktleiders](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [CIO Dive – Microsoft Q3 2026](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/) | [CIO Dive – AWS Google multi-cloud](https://www.ciodive.com/news/aws-google-link-cloud-products/806705/)*

## 💡 Ctac-relevantie

**GPT-6 Astra en agentic AI zijn het gesprek van vandaag bij elke CTO.** De positionering van Ctac als AI-partner wordt geloofwaardiger als jullie concreet kunnen aantonen hoe agentic orchestration — of het nu via Anthropic, OpenAI of open modellen is — ingezet wordt in klantsituaties. De prijs-performance verbetering van Fable 5.1 (−45% voor agentische workloads) maakt business cases voor klanten met hoge token-volumes aanzienlijk aantrekkelijker — actualiseer eventuele offertes.

**EU AI Act handhaving is nu realiteit**, niet toekomstmuziek. Klanten in de publieke sector, zorg en finance hebben concrete compliance-vragen. Ctac kan hier een praktische rol spelen: transparantie-vereisten implementeren, AI-systemen categoriseren op risiconiveau, en audittrails inrichten. Dit is een concrete propositie die nu geopend kan worden.

**Prompt injection als enterprise-risico** is onderbelicht bij veel IT-beslissers. Een security-awareness briefing of quickscan-aanbod voor klanten die Microsoft Copilot of vergelijkbare tools uitrollen, past precies in de huidige marktbehoefte — en sluit aan bij de groeiende vraag naar AI-risicomitigatie (zie ook de budgetten die hiervoor vrijkomen per CIO Dive).

## 📚 Bronnen & verder lezen

- [OpenAI – GPT-6 Astra aankondiging](https://openai.com/index/gpt-6-astra/)
- [OpenAI – Safety overview GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/)
- [TechCrunch – OpenAI Astra launch](https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/)
- [VentureBeat – Welcome to the AGI era](https://venturebeat.com/technology/welcome-to-the-agi-era-openai-launches-gpt-6-astra)
- [Anthropic – Claude Fable 5.1 & Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- [TechCrunch – Fable 5.1 release](https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/)
- [VentureBeat – Fable 5.1 kosten](https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads)
- [EC – AI Act handhaving 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – 90+ organisaties getroffen](https://venturebeat.com/security/adversaries-hijacked-ai-security-tools-at-90-organizations-the-next-wave-has-write-access-to-the-firewall)
- [CIO Dive – Microsoft & Google marktleiders](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – Microsoft Q3 2026 earnings](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
