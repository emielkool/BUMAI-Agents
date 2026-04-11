# AI Dagbriefing – 11 april 2026

## 🔑 Highlights van de dag

- **Modelrace in volle gang**: Microsoft, Meta, Google en Anthropic hebben deze week allemaal significante releases gedaan. De concurrentiedruk op foundation model-niveau is historisch hoog – en de kwaliteitsverschillen worden kleiner.
- **EU AI Act: eindsprint begint**: De volledige toepasbaarheid van de AI Act is vastgesteld op 2 augustus 2026. Trilogiegesprekken zijn gestart; een akkoord over aanvullende amendementen wordt verwacht vóór eind april. Voor NL/BE-bedrijven breekt nu de echte compliance-sprint aan.
- **Agentic AI: adoptie loopt ver achter op ambitie**: Slechts 8,6% van de bedrijven heeft AI-agents écht in productie. 63,7% heeft geen formeel AI-initiatief. Executiegap is het kernthema van 2026 – niet het ontbreken van technologie.
- **Prompt injection: de #1 AI-kwetsbaarheid van dit moment**: OWASP plaatst het bovenaan alle LLM-risico's. Een recente CVE met CVSS-score 9.6 toont aan dat het ook actief geëxploiteerd wordt in developer-tooling (GitHub Copilot).
- **SAIL-coalitie gelanceerd**: Anthropic, Meta, Microsoft, IBM en Genentech richten gezamenlijk de *Shared AI License Foundation* op – een patent-netwerk om open innovatie in foundation models te beschermen. Strategisch signaal richting open-source AI-ecosysteem.

---

## 🧠 Technologie & Modellen

**Microsoft MAI-modellen** – Microsoft lanceerde drie nieuwe foundation models (tekst, spraak, afbeelding) als onderdeel van zijn *MAI Superintelligence*-initiatief. Dit is een directe aanval op OpenAI's marktpositie. Strategisch interessant: Microsoft bouwt nu bewust eigen modellen náást de OpenAI-samenwerking.
*Bron: [TechCrunch, 2 april](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)*

**Google Gemma 4** – Google's nieuwste open-weights model is gebouwd op dezelfde architectuur als Gemini 3, ontworpen voor lokale inferentie op low-power hardware en autonomous agents. Dit is relevant voor on-premise en sovereign AI-toepassingen.
*Bron: [LLM Stats](https://llm-stats.com/llm-updates)*

**Google Gemini 3.1** – Leidt 13 van 16 standaardbenchmarks en staat gelijk aan GPT-5.4 Pro op de Artificial Analysis Intelligence Index. Real-time voice en image analysis nu ingebakken.

**Meta Superintelligence Labs** – Na de acquisitie van Scale AI (Alexandr Wang) heeft Meta een klein maar krachtig reasoning-model uitgebracht. Prestaties vergelijkbaar met grotere Llama 4-varianten, met sterke multimodale en agentic capaciteiten.
*Bron: [CNBC, 8 april](https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html)*

**Anthropic Claude Mythos 5** – Een model van 10 biljoen parameters gericht op cybersecurity en coding. Niet publiek beschikbaar – alleen voor selecte partners via *Project Glasswing*. Relevant als signaal: de frontier van modellen schuift door, maar blijft deels achter gesloten deuren.

**SAIL-coalitie** – Eerste organisatie die AI-innovatie beschermt via een collaboratief patent-netwerk. Oprichters: Anthropic, Meta, Microsoft, IBM, Genentech.
*Bron: [GlobeNewswire, 8 april](https://www.globenewswire.com/news-release/2026/04/08/3270111/0/en/AI-Pioneers-Unite-to-Launch-the-Shared-AI-License-Foundation-to-Advance-Foundation-Model-Innovation.html)*

---

## 🏛️ Governance & Ethiek

**EU AI Act – augustus 2026 is de harde deadline**: De volledige wet wordt van kracht op 2 augustus 2026. De verboden AI-toepassingen en AI-literacy-eisen gelden al sinds februari 2025. Governance-regels voor GPAI-modellen lopen al depuis augustus 2025. Wat nieuw is per augustus: de eisen voor high-risk AI-systemen (artikel 6 lid 2 e.v.) en de nationale sandboxvereisten.

**Trilogue amendementen**: Het Europees Parlement heeft zijn positie vastgesteld over aanvullende wijzigingen (o.a. via de *Digital Omnibus*). Een tweede trilogue op 28 april kan tot een akkoord leiden over aanpassingen aan de compliance-termijnen.

**Transparantie Code of Practice – eerste ontwerp gepubliceerd**: Bevat richtlijnen voor uitlegbaarheid en traceerbaarheid van AI-systemen. Verplichte watermerken voor AI-gegenereerde content (audio, beeld, video, tekst) worden verwacht per 1 november 2026.

**NIST AI RMF 2.0** (publicatie januari 2026): Bevat nu specifieke richtlijnen voor prompt injection-preventie. Bruikbaar als praktisch framework naast de EU AI Act.

*Bronnen: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) | [Kennedys Law](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/) | [OneTrust](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/)*

---

## 🔐 Security & Risk

**Prompt injection: OWASP #1-risico** – In het meest recente OWASP LLM Security Project-rapport (maart 2026) staat prompt injection bovenaan alle vulnerability-categorieën voor deployed language models – boven datapoisoning, model theft en insecure output handling.

**Indirect injection domineert**: Meer dan 80% van de gedocumenteerde aanvallen in enterprise-context is *indirect* – verborgen in documenten, e-mails, webpagina's of database-inhoud. Directe gebruikersaanvallen zijn de minderheid geworden.

**CVE-2025-53773 (CVSS 9.6)**: Kritieke kwetsbaarheid waarbij verborgen prompt injection in pull request-beschrijvingen remote code execution mogelijk maakte via GitHub Copilot. Dit raakt direct developer workflows.

**Financiële schade**: $2,3 miljard wereldwijd in 2025 door prompt injection-aanvallen (Recorded Future). 67% gericht op customer service chatbots en AI-trading systemen.

**Enterprise zichtbaarheidsprobleem**: 81% van de organisaties heeft geen zicht op hoe AI intern wordt gebruikt. Dit is de kern van het shadow AI-risico.

*Bronnen: [Airia](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) | [Cisco State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report) | [Cycode](https://cycode.com/blog/ai-security-vulnerabilities/)*

---

## 📈 Markt & Adoptie

**Microsoft & Google domineren enterprise AI**: Microsoft voert de ranglijst aan dankzij zijn partner- en platform-ecosysteem. Google wint terrein in agentic AI door een geïntegreerde tech stack. AWS houdt 32% marktaandeel in cloud, maar Azure groeit met 39% YoY en Google Cloud met 50% YoY.

**Hyperscaler capex op recordhoogte**: AWS stuurt aan op $200 miljard capex in 2026 (+50% t.o.v. 2025). Google verhoogde zijn capex-guidance naar $175–185 miljard. AI-infrastructuur is de drijvende kracht.

**Executiegap is het echte verhaal** (Deloitte State of AI 2026): Adoptie groeit snel, maar data-infrastructuur, governance en talentontwikkeling lopen sterk achter. Slechts 8,6% van de bedrijven heeft AI-agents in productie. 63,7% heeft geen formeel AI-initiatief.

*Bronnen: [Kai Waehner](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/) | [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [HPCwire/Deloitte](https://www.hpcwire.com/bigdatawire/2026/03/03/deloittes-state-of-ai-2026-why-enterprise-execution-is-falling-behind-adoption/)*

---

## 💡 Ctac-relevantie

**1. EU AI Act compliance = directe kans voor Ctac**
Met augustus 2026 als harde deadline zijn NL/BE-klanten nú in de sprint. Ctac kan als trusted IT-partner een concrete rol spelen in AI-inventarisatie, risicoklassificatie en governance-implementatie. Dit is niet hypothetisch – de deadline is over minder dan 4 maanden. Actie: verken of er een AI Act readiness-scan als dienst aangeboden kan worden, eventueel gecombineerd met Microsoft Purview of Compliance Center-tooling.

**2. Executiegap = Ctac's core opportunity**
63,7% van bedrijven heeft geen formeel AI-initiatief. De technologie is beschikbaar; de implementatiecapaciteit niet. Dit is precies waar een IT-consultancy als Ctac waarde toevoegt. De propositie moet niet zijn "wij bouwen AI" maar "wij zorgen dat AI daadwerkelijk werkt in jouw organisatie" – inclusief data-infrastructuur, change management en governance.

**3. Sovereign/lokale AI met Gemma 4**
Google's Gemma 4 is ontworpen voor lokale inferentie op low-power hardware. Dit biedt kansen voor klanten in sectoren als overheid en zorg die data niet naar de cloud mogen sturen. Ctac kan hier een on-premise AI-propositie op bouwen – voor Emiel's team interessant om te verkennen als IP-gedreven dienst.

**4. Prompt injection = security-propositie**
De combinatie van OWASP #1-status, de actieve CVE in developer-tooling en de lage enterprise-zichtbaarheid maakt AI Security tot een laagdrempelig maar hoogwaardig dienstaanbod. Een "AI Security Scan" of risicoassessment voor klanten die al LLMs gebruiken is snel te positioneren en heeft directe urgentie.

**5. Intern: zet nu een AI-governance baseline neer**
Als de AI-unit bij Ctac ook intern AI-tools gebruikt (Copilot, Claude, etc.), is dit het moment om een intern beleid te formaliseren – zowel voor compliance als als referentie richting klanten. Wat je intern opbouwt, kun je straks als best practice verkopen.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Microsoft MAI foundational models (2 april 2026)](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)
- [CNBC – Meta Superintelligence Labs nieuw model (8 april 2026)](https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html)
- [GlobeNewswire – SAIL coalitie lancering (8 april 2026)](https://www.globenewswire.com/news-release/2026/04/08/3270111/0/en/AI-Pioneers-Unite-to-Launch-the-Shared-AI-License-Foundation-to-Advance-Foundation-Model-Innovation.html)
- [LLM Stats – AI model releases april 2026](https://llm-stats.com/llm-updates)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Kennedys Law – EU AI Act deadline analyse 2026](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/)
- [OneTrust – EU Digital Omnibus en AI Act 2026](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/)
- [Airia – Prompt injection en AI security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Cisco State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)
- [Kai Waehner – Enterprise Agentic AI Landscape 2026](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)
- [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [HPCwire – Deloitte State of AI 2026](https://www.hpcwire.com/bigdatawire/2026/03/03/deloittes-state-of-ai-2026-why-enterprise-execution-is-falling-behind-adoption/)
- [Cycode – Top AI Security Vulnerabilities 2026](https://cycode.com/blog/ai-security-vulnerabilities/)
