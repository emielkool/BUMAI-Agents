---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-31
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 31 mei 2026

## 🔑 Highlights van de dag

- **Google Agentic Era is formeel begonnen**: Op Google I/O (19 mei) lanceerde Google Gemini 3.5 Flash, Gemini Spark en het Antigravity-platform – Google positioneert AI niet meer als chatbot maar als autonome agent die 24/7 in de achtergrond werkt. Dit is de meest coherente agentic enterprise-strategie die Google tot nu toe heeft gepresenteerd.
- **EU AI Act Omnibus akkoord bereikt (7 mei)**: Vereenvoudiging van de AI-verordening voor MKB en middelgrote bedrijven. Hogere-risicoregels voor biometrie, onderwijs en arbeidsmarkt gaan nu pas in op 2 december 2027.
- **Claude Mythos vindt 10.000 kritieke kwetsbaarheden**: Anthropic's beperkt beschikbare model voor cybersecurity heeft via Project Glasswing 10.000 high-severity lekken blootgelegd in veelgebruikte software – waaronder elk groot besturingssysteem en elke browser. De keerzijde: ongeautoriseerde toegang via een derde leverancier is al gemeld.
- **Microsoft 365 E7 live**: Per 1 mei is Microsoft's "Frontier Suite" beschikbaar, met Copilot en de nieuwe Agent 365 governance-laag. Microsoft consolideert zijn enterprise-positie in productiviteits-AI.
- **Agentic AI = grootste cyberdreiging van 2026**: 48% van securityprofessionals noemt agentic AI nu de primaire aanvalsvector – maar slechts 29% van organisaties voelt zich klaar voor veilige inzet.

---

## 🧠 Technologie & Modellen

**Google I/O 2026 – Antigravity & Gemini 3.5 Flash**
Google zette op 19 mei definitief de stap naar een "agentic-first" strategie. Gemini 3.5 Flash is gepositioneerd als model dat frontier-intelligentie combineert met snelheid en actievermogen – het kan autonoom codeer-pipelines uitvoeren en onderzoeksprojecten beheren. Gemini Spark is een 24/7 persoonlijke AI-agent met Gmail-integratie die ook draait als het toestel uit staat. Voor ontwikkelaars is Antigravity het centrale platform; Managed Agents in de Gemini API geven ontwikkelaars een complete agentomgeving met één API-aanroep.
*(Bronnen: [TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/), [Google Blog](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/))*

**Anthropic Claude Mythos Preview & Project Glasswing**
Anthropic heeft via Project Glasswing 10.000 kritieke beveiligingslekken ontdekt – inclusief CVE-2026-4747 waarmee een externe aanvaller volledige servercontrole kan krijgen. Het model is bewust niet publiek beschikbaar gesteld. Partners zijn Amazon, Apple, Microsoft, Cisco en CrowdStrike. Tegelijkertijd circuleren berichten dat een privaat online forum via een derde leverancier ongeautoriseerde toegang heeft verkregen.
*(Bron: [The Hacker News](https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html), [TechCrunch](https://techcrunch.com/2026/04/21/unauthorized-group-has-gained-access-to-anthropics-exclusive-cyber-tool-mythos-report-claims/))*

---

## 🏛️ Governance & Ethiek

**EU AI Act Omnibus – akkoord op 7 mei 2026**
Na maanden onderhandelen bereikten het Europees Parlement en de Raad overeenstemming over het AI Omnibus-voorstel. De belangrijkste wijzigingen: vereenvoudigde technische documentatievereisten voor MKB én voor middelgrote bedrijven (nieuw), ruimere toegang tot regulatoire sandboxes inclusief een EU-sandbox, en uitgestelde deadlines voor high-risk AI-toepassingen in biometrie, onderwijs, arbeidsmarkt en migratie (nu 2 december 2027). Bovendien wordt het verbod op "nudification-apps" nu expliciet in de wet verankerd.
*(Bron: [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/eu-agrees-simplify-ai-rules-boost-innovation-and-ban-nudification-apps-protect-citizens))*

**Nederland – ISO 42001 als de facto AI-keurmerk**
Computable signaleert dat "geen AI zonder keurmerk" in de NL publieke sector richting ISO 42001 gaat als de relevante standaard. Tegelijkertijd lanceerden zes gemeenten een gezamenlijke AI-tool voor bron-anonimisering – een praktisch voorbeeld van samenwerking op informatiebeveiliging.
*(Bronnen: [Computable](https://www.computable.nl/2026/05/15/geen-ai-zonder-keurmerk-waarom-vooruitlopen-op-iso-42001-slim-is/), [Computable](https://www.computable.nl/2026/05/19/gemeenten-lanceren-ai-tool-voor-bron-anonimisering/))*

---

## 🔐 Security & Risk

**Agentic AI als aanvalsvector #1**
Op RSAC 2026 presenteerden vijf grote vendors (Cisco, CrowdStrike, Palo Alto Networks, Microsoft, Cato Networks) elk een eigen agent-identity framework. De governance-infrastructuur voor autonome agents staat nog in de kinderschoenen: slechts 29% van organisaties voelt zich klaar voor veilige agentic AI-inzet, terwijl 48% het als de grootste dreiging voor 2026 beschouwt.
*(Bron: [VentureBeat](https://venturebeat.com/security/cisco-crowdstrike-rsac-2026-agent-identity-iam-gap-maturity-model))*

**Prompt injection blijft onoplosbaar structureel probleem**
Recente arXiv-analyse toont dat bij adaptieve aanvallen het succes bij state-of-the-art verdedigingsmechanismen boven de 85% uitkomt. OpenAI erkende eerder al dat AI-browsers "structureel kwetsbaar" kunnen blijven voor prompt injection. Voor Ctac-klanten die nu agents bouwen is dit een direct en onderschat risico in productie.
*(Bron: [TechCrunch](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/))*

---

## 📈 Markt & Adoptie

**Microsoft 365 E7 – Frontier Suite live**
Per 1 mei is Microsoft 365 E7 algemeen beschikbaar: een bundel van E5 (productiviteit + security), Entra Suite (identity) en Copilot met Agent 365 als governance-laag. Dit is het eerste product waarbij Microsoft Copilot én agent-beheer expliciet in één enterprise-licentie combineert. Interessant voor Ctac-klanten die al in de Microsoft-stack zitten.
*(Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))*

**Twee derde van bedrijven vast in pilotfase**
Ondanks de hype zit 67% van bedrijven nog in de experimenteerfase en slaagt er niet in AI naar productie te brengen. Merck en Mastercard tonen dat schaalbare inzet mogelijk is – maar dat de "plumbing" (data-infrastructuur, orchestratie) de kritieke voorwaarde is.
*(Bron: [VentureBeat](https://venturebeat.com/infrastructure/merck-and-mastercard-are-seeing-real-agentic-ai-results-both-say-the-plumbing-came-first))*

**Salesforce groeit door**: 6.000 nieuwe enterprise-klanten in drie maanden, terwijl de AI-bubbeldiscussie gaande is. Signaal dat enterprise-adoptie ondertussen gewoon doorgroeit.
*(Bron: [VentureBeat](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000))*

---

## 💡 Ctac-relevantie

**Propositie-kans: van pilot naar productie-begeleiding**
De data is duidelijk: 67% van bedrijven raakt niet voorbij de pilotfase. Ctac kan hier een specifieke rol pakken als "productie-accelerator" voor agentic AI – waarbij de nadruk ligt op data-infrastructuur, governance en change management. Dit is geen technisch verhaal maar een strategisch inrichtingsvraagstuk.

**EU AI Act Omnibus = raam van kans voor compliance-dienstverlening**
De vereenvoudigingen voor MKB en middelgrote bedrijven verlagen de instapdrempel voor compliance, maar creëren ook verwarring over deadlines en verplichtingen. Ctac kan nu proactief klanten begeleiden richting ISO 42001-certifcering en AI Act-readiness, zeker voor sectoren die onder de high-risk categorieën vallen (overheid, arbeidsmarkt, gezondheidszorg).

**Agentic security = urgent nieuw aandachtsgebied**
Bij elke klant die nu agents bouwt of implementeert (Copilot-extensies, workflow-agents) is prompt injection en agent-identity governance een direct risico. Dit vraagt om een Ctac-standpunt en checklist – vóórdat een klant erdoor geraakt wordt.

**Microsoft E7 als gespreksstarter**
Ctac-klanten in de Microsoft-stack krijgen nu actief van Microsoft te horen dat Agent 365 beschikbaar is. Zorg dat Ctac-consultants het verhaal kennen en proactief het gesprek aangaan over veilige adoptie.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Gemini 3.5 Flash: Google bets on agents](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/)
- [Google Blog – I/O 2026: Welcome to the agentic Gemini era](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)
- [Google Blog – 100 things announced at Google I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [The Hacker News – Claude Mythos finds 10,000 high-severity flaws](https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html)
- [TechCrunch – Unauthorized access to Anthropic's Mythos](https://techcrunch.com/2026/04/21/unauthorized-group-has-gained-access-to-anthropics-exclusive-cyber-tool-mythos-report-claims/)
- [Anthropic – Project Glasswing](https://www.anthropic.com/glasswing)
- [EC Digital Strategy – EU agrees to simplify AI rules](https://digital-strategy.ec.europa.eu/en/news/eu-agrees-simplify-ai-rules-boost-innovation-and-ban-nudification-apps-protect-citizens)
- [EU AI Act tracker – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [VentureBeat – Agentic AI agent identity at RSAC 2026](https://venturebeat.com/security/cisco-crowdstrike-rsac-2026-agent-identity-iam-gap-maturity-model)
- [VentureBeat – Merck and Mastercard agentic AI results](https://venturebeat.com/infrastructure/merck-and-mastercard-are-seeing-real-agentic-ai-results-both-say-the-plumbing-came-first)
- [CIO Dive – Microsoft, Google rule AI vendor market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Computable – ISO 42001 als AI-keurmerk](https://www.computable.nl/2026/05/15/geen-ai-zonder-keurmerk-waarom-vooruitlopen-op-iso-42001-slim-is/)
- [Computable – Gemeenten AI-tool bron-anonimisering](https://www.computable.nl/2026/05/19/gemeenten-lanceren-ai-tool-voor-bron-anonimisering/)
