---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W39
Datum: 2026-09-25
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 39, 2026

> Synthese van de dagbriefings van 21 september t/m 25 september 2026.

## 🏆 Weekhighlights

**1. Prijsoorlog aan de frontier — modellen worden radicaal goedkoper**
Op dinsdag 22 september lanceerde Anthropic Claude Opus 5.5 (input $4 / output $20 per miljoen tokens, 20% goedkoper dan Opus 5), waarna OpenAI binnen een uur GPT-6 Sol ($2/$10) en GPT-6 Luna ($0,10/$0,50) uitbracht. Luna is goedkoper dan vrijwel elke bestaande API op de markt. Dit is geen incrementele stap — dit is een structurele prijsval die bulk-AI-verwerking economisch maakt voor vrijwel iedere onderneming.

**2. Agentic AI wordt enterprise-architectuur — Salesforce en Alibaba trekken de lijn**
Salesforce presenteerde AIforce op Dreamforce: CRM-functionaliteit die via Claude, Slack of Lightning bereikbaar is zonder de traditionele UI. Alibaba lanceerde op Apsara Conference een complete agentic stack: Qwen Book computer, AI-wearables (bril, earbuds, notitie-device), Zhenwu V900-chip en een "agentic cloud"-infrastructuurlaag. Beide initiatieven markeren een architectuuromslag: AI-agents als primaire interface voor bedrijfssoftware, gebruikers als secundair.

**3. Shadow AI op 76% — governance-crisis is reëel**
Driekwart van alle organisaties erkent dat schaduw-AI een definitief of waarschijnlijk probleem is, met gemiddeld 10 niet-goedgekeurde AI-applicaties per maand. Bijna de helft van alle enterprise AI-gesprekken verloopt via onbeheerde persoonlijke identiteiten. Geen enkel security-framework kan opereren op onzichtbare systemen — dit is de meest urgente governance-uitdaging van het jaar.

**4. Agentic AI breaches en runaway agents — security loopt achter**
1 op 8 bedrijven rapporteert een security-incident gekoppeld aan agentic systemen (Mandiant, Darktrace). Een gedocumenteerd geval: een autonoom AI-agent genereerde $50.000 aan cloudkosten door ontbrekende guardrails en prompt injection. Detecties van indirecte prompt injection namen 5x toe tussen maart en mei 2026. De aanvalsoppervlak groeit sneller dan de verdediging.

**5. EU AI Act GPAI-evaluaties — eerste echte handhavingsmijlpaal bereikt**
Op 15 september jl. moesten aanbieders van general-purpose AI-modellen boven 10²⁵ FLOP's hun eerste formele systeemrisico-evaluaties indienen bij het European AI Office. Dit is de eerste echte handhavingsactie onder de AI Act voor frontier-models. De beoordeling loopt; uitkomsten verwacht Q4 2026. Tegelijkertijd zijn de transparantieregels (artikel 57) per 2 augustus van kracht — elke EU-organisatie moet nu aantoonbaar weten welke AI-systemen ze inzet.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De modelmarkt convergeert naar een drielaagse structuur die deze week duidelijk zichtbaar werd: (1) frontier-reasoning-modellen voor complexe autonome taken (Opus 5.5, GPT-6 Sol), (2) bulk-verwerkingsmodellen voor volume en extractie (GPT-6 Luna, DeepSeek V4.1 Flash), en (3) platform-geïntegreerde modellen voor specifieke workflows (Koa van Salesforce, Qwen-familie van Alibaba). De frontier-laag wordt beter én goedkoper tegelijk — dat was historisch gezien niet vanzelfsprekend.

Het echte verhaal van de week is niet de model-releases zelf, maar de **agentic stack-race**: wie controleert de volledige stack van chip tot cloud tot OS tot applicatie? Alibaba's Apsara-aankondigingen waren de meest coherente poging tot nu toe — vergelijkbaar met hoe Apple zijn verticale integratie opbouwde, maar dan voor AI-native computing. Dit is een ontwikkeling met langetermijngevolgen voor enterprise leverancierskeuzes.

### 🏛️ Governance & Beleid

De Europese handhaving wordt concreet. De GPAI-evaluatieplicht (deadline 15 september) geeft het European AI Office voor het eerst echte tanden: frontier-modelaanbieders moeten hun red-teaming, energieverbruik en auteursrecht-compliance openleggen. Hoe streng de beoordeling uitpakt, bepaalt mede of Europa serieus wordt genomen als AI-regelgever of wegspeelt in het aanscherpen van onuitvoerbare normen.

Nederland loopt relatief voor: de internationale AI-strategie (juli 2026), een staatssecretaris voor AI en de oprichting van een Publieke Dienst voor AI-Strategie zijn concrete stappen die de meeste EU-lidstaten nog moeten zetten. Dit creëert kansen voor Nederlandse AI-spelers — ook voor Ctac — om vroegtijdig mee te bouwen aan publieke AI-infrastructuur en beleid.

Het grote witte vlak in governance is **agentic aansprakelijkheid**: wie is verantwoordelijk als een AI-agent schade veroorzaakt in een autonome workflow? Noch de AI Act, noch nationale wetgeving geeft hier nu een helder antwoord. Dit is het governance-thema dat 2027 zal domineren.

### 🔐 Security & Risk

De drie structurele risicothema's van deze week hangen samen: **shadow AI** (onzichtbare systemen), **excessive permissions** (agents met te brede rechten) en **prompt injection** (aanvallen op agentic workflows). Ze versterken elkaar: wie shadow AI niet controleert, heeft geen zicht op agent-rechten, en is maximaal kwetsbaar voor injection.

De conclusie van alle 2026-security-rapporten is uniform: AI-aanvalstechnieken evolueren sneller dan enterprise-verdedigingstools. De kloof groeit. Dit is niet alarmerend als signaal om AI te vermijden, maar als signaal dat **security-first architectuur bij AI-adoptie niet optioneel is**.

### 📈 Markt & Adoptie

88% van de organisaties gebruikt AI, maar de diepte varieert enorm. De markt bevindt zich in een overgangsfase van brede adoptie naar gerichte schaling — en die overgang gaat gepaard met stranding: Gartner voorspelt dat >40% van de agentic AI-projecten vóór eind 2027 wordt afgeblazen vanwege onduidelijke businesswaarde of onvoldoende risicobeheer. De winnaars van de volgende fase zijn niet de eerste adopters, maar de best begeleide adopters.

OpenAI's enterprise-omzet passeert 40% — dat is sneller dan verwacht. Codex (3M weekly active users) toont dat AI-coding mainstream is. De AI coding-markt groeit 26% per jaar naar $30B in 2031. Salesforce Agentforce Coworker is nu live en zal in Q4 een implementatiegolf veroorzaken bij SI-partners.

---

## 💼 Ctac-weekperspectief

Deze week markeerde een duidelijke kanteling: AI is geen experiment meer, maar kritische bedrijfsinfrastructuur in opbouw. Ctac staat op het juiste moment in de goede positie, maar moet nu concrete keuzes maken over waar het de zwaarste kaarten op inzet.

- **Salesforce Agentforce — nu handelen:** Agentforce Coworker is beschikbaar. Ctac's Salesforce-practice moet binnen twee weken een intern assessment doen van bestaande klantinstallaties en een quickstart-propositie formuleren. De implementatiegolf in Q4 gaat razendsnel; vroeg ingeroepen SI-partners winnen meer trajecten.

- **AI governance als primaire propositie:** De shadow AI-crisis (76%) en de EU AI Act-transparantieregels (van kracht per 2 augustus) geven Ctac een concrete aanleiding voor klantgesprekken. Een "AI Governance Readiness Assessment" — inventory van AI-gebruik, risicoclassificatie, compliance-gap-analyse — is een logische eerste stap die aansluit bij Ctac's consultancy-DNA.

- **Agentic security als differentiator:** De drie security-thema's (shadow AI, excessive permissions, prompt injection) zijn voor de meeste klanten abstract. Ctac kan dit concretiseren via een "Agentic Risk Assessment" dat inging met een incident-case (de $50k cloud bill) en uitmondt in een concrete beveiligings- en governancearchitectuur. Dit is een hoogwaardige propositie met beperkte concurrentie.

- **Publieke sector — nu het moment:** De Nederlandse AI-strategie en de EU AI Act-implementatie veroorzaken overheidsinvesteringen in AI-capaciteit. Ctac moet in Q4 2026 actief aanwezig zijn in het publieke sector-debat: kennisdeling, whitepaper-publicaties, aanwezigheid bij overheidsinitiatieven. De positie die je nu opbouwt, bepaalt welke aanbestedingen je in 2027 wint.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war – Simon Willison](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/)
- [Anthropic releases Claude Opus 5.5 and OpenAI counters with GPT-6 – SiliconANGLE](https://siliconangle.com/2026/09/22/anthropic-releases-claude-opus-5-5-and-openai-counters-with-two-cheaper-gpt-6-models/)
- [OpenAI Launches GPT-6 Sol and Luna – Decrypt](https://decrypt.co/378986/openai-launches-gpt-6-sol-luna-anthropic-claude-opus-5-5)
- [AI Model Releases: September 2026 Tracker – Digital Applied](https://www.digitalapplied.com/blog/ai-model-releases-september-2026-tracker)
- [LLM News Today (September 2026) – LLM Stats](https://llm-stats.com/ai-news)
- [Alibaba Unveils Agentic Computer, AI Wearables at Apsara 2026 – Alizila](https://www.alizila.com/alibaba-unveils-agentic-computer-ai-wearables-and-more-at-2026-apsara-conference/)
- [Alibaba Qwen Book agentic computer – TechNode Global](https://technode.global/2026/09/24/alibaba-qwen-book-ai-wearables-apsara-2026/)
- [AliViews: Eddie Wu Shares Full-Stack AI Roadmap – Alizila](https://www.alizila.com/aliviews-eddie-wu-shares-alibabas-strategic-full-stack-ai-roadmap-at-the-2026-apsara-conference/)

**Governance & Beleid**
- [EU AI Act in 2026: What Applies, What Was Deferred – Regulation AI](https://www.regulation-ai.eu/en/ai-act/)
- [EU AI Act 2026: Penalties, Risk Tiers & New Deadlines – Decode The Future](https://decodethefuture.org/en/eu-ai-act-explained/)
- [AI Regulation News September 2026: Global Update – Cubbbix](https://cubbbix.com/blog/ai-regulation-september-2026-global-update)
- [CDT Europe's AI Bulletin: September 2026](https://cdt.org/insights/cdt-europes-ai-bulletin-september-2026/)
- [Kabinet presenteert internationale strategie voor veilige AI-transitie – Rijksoverheid](https://www.rijksoverheid.nl/actueel/nieuws/2026/07/03/kabinet-presenteert-internationale-strategie-voor-veilige-en-verantwoorde-ai-transitie)

**Security & Risk**
- [One runaway AI agent racked up a $50,000 cloud bill – Help Net Security](https://www.helpnetsecurity.com/2026/09/16/google-mandiant-enterprise-ai-security-risks-report/)
- [Enterprise AI Usage Risk Report 2026 – Akamai](https://www.akamai.com/lp/state-of-the-internet/enterprise-ai-risk-report)
- [State of AI Security Report 2026 – Cisco](https://www.cisco.com/c/en/us/products/security/state-of-ai-security.html)
- [AI Security Report 2026 – Check Point Research](https://research.checkpoint.com/2026/ai-security-report-2026/)
- [The State of AI Cybersecurity 2026 – Darktrace](https://www.darktrace.com/resource/the-state-of-ai-cybersecurity-2026)
- [How to Secure Enterprise AI – The Hacker News](https://thehackernews.com/2026/09/how-to-secure-enterprise-ai-from.html)

**Markt & Adoptie**
- [Salesforce Launches AIforce at Dreamforce '26 – Salesforce Ben](https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui/)
- [Dreamforce 2026: The Top Announcements – CX Foundation](https://cxfoundation.com/news/dreamforce-announcements-2026)
- [Enterprise AI Agent Stats 2026: 80% Embed, 31% Deploy](https://paul-okhrem.com/enterprise-ai-agents-statistics-2026/)
- [AI Adoption Statistics 2026: Business & Enterprise Data – AI Business Weekly](https://aibusinessweekly.net/p/ai-adoption-statistics)
- [Enterprise AI for SMBs: Google, OpenAI & Microsoft Compare – Morning Consult](https://morningconsult.com/articles/enterprise-ai-smb-brand-perception-2026)
- [The next phase of enterprise AI – OpenAI](https://openai.com/index/next-phase-of-enterprise-ai/)
- [Scaling agentic AI pilots across the enterprise – MIT Technology Review](https://www.technologyreview.com/2026/09/03/1142868/scaling-agentic-ai-pilots-across-the-enterprise/)
- [AI Agents News — Week of September 24, 2026 – AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)
