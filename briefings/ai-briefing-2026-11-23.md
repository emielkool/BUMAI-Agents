---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-23
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 23 november 2026

## 🔑 Highlights van de dag

- **GPT-6.2 en Gemini 4 Neon** zijn beide in de week van 17–18 november uitgebracht; OpenAI brengt twee varianten uit (Astra en Sol) met sterk verschil in prijs en snelheid, Google positioneert Neon als kostenefficiënte middenklasse-optie die Carbon benadert.
- **Anthropic op de beurs**: het IPO op Nasdaq onder ticker ANT is dé financiële AI-mijlpaal van de maand — marktkapitalisatie en schuldpositie worden zichtbaar; dit markeert een nieuwe fase in de consolidatie van het AI-landschap.
- **Microsoft + IBM lanceren Imagine Enterprise**: 6.000+ kant-en-klare AI-agents voor enterprise; dit is geen proof-of-concept maar een directe marktpropositie die Ctac's eigen enterprise-klanten gaat bereiken.
- **EU AI Act december-deadline nadert**: vanaf 2 december 2026 treden nieuwe verboden in werking (AI-gegenereerde NCII, watermarking-verplichting einde overgangsperiode); organisaties die hier nog niet compliant voor zijn lopen concreet risico.
- **Indirecte prompt injection domineert AI-security**: aanvalsvectoren verplaatsen zich van directe gebruikersinput naar vergiftigde documenten, e-mails en webpagina's die via RAG-pipelines binnenkomen — kritisch voor iedereen die AI-agents bouwt of host.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-6.2 (Astra & Sol)** – 17 november  
OpenAI bracht twee varianten uit: Astra ($8/$40 per miljoen tokens input/output) als high-end model en Sol ($2/$10) als snel en goedkoop alternatief voor everyday-toepassingen. Naast Sol en Astra bestaat een afgeschermde GPT-6 Cyber variant beperkt tot goedgekeurde securitypartners. Bron: [LLM News Today – November 2026](https://llm-stats.com/ai-news), [AI News This Week](https://larwell.com/blog/ai-news-this-week-november-22-2026)

**Google Gemini 4 Neon** – 18 november  
Google positioneert Neon als middenklassemodel dat dicht bij het krachtigste Gemini 4 Carbon komt terwijl het taken aanzienlijk sneller afrondt. Eerder deze maand lanceerde Google ook Gemini 4 Carbon (10 november) en Hydrogen (12-13 november). Dit is serieuze multimodel-strategie: Google heeft nu bewust een product per marktsegment. Bron: [LLM Release Tracker 2026](https://nhimg.org/llm-release-tracker)

**Anthropic Claude Fable 5.2** – algemeen beschikbaar sinds 9 november  
De nieuwste Fable-variant is breed uitgerold; Claude Mythos 5.2 is nog beperkt tot geverifieerde organisaties. Antropics Nasdaq-IPO (ticker ANT) is financieel de grotere nieuwsfeit van november. Bron: [New AI Models November 2026](https://llmgateway.io/timeline)

**Microsoft Copilot Autopilot** – ca. 18 november  
Microsoft onthulde een autonome Copilot-variant met een eigen Entra-identiteit: Copilot Autopilot handelt zelfstandig taken af namens de organisatie. Dit is een significante stap richting enterprise-agentische systemen. Bron: [AI Agents News Brief 18 november](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-18-2026)

---

## 🏛️ Governance & Ethiek

**EU AI Act – December 2026 als volgende mijlpaal**  
Vanaf 2 december 2026 treden twee nieuwe verplichtingen in werking: (1) verbod op AI die niet-consensuele intieme afbeeldingen of CSAM genereert, en (2) het einde van de overgangsperiode voor watermarking van generatieve AI-inhoud die al op de markt was. De Digital Omnibus-aanpassingen (Verordening (EU) 2026/1744) verschoven de Annex III-deadline voor hoog-risico AI naar 2 december 2027, maar dit is geen excuus om stil te zitten. Bron: [EU AI Act Compliance Guide 2026](https://www.orbiqhq.com/eu-regulations/eu-ai-act-compliance), [EU digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Nederland** – conceptwetgeving in consultatiefase afgerond  
Het ministerie publiceerde in april 2026 een ontwerp-uitvoeringswet. Keuze: gedecentraliseerd toezicht via bestaande toezichthouders (RDI, AP, en sectorale autoriteiten) in plaats van één nieuw AI-orgaan. Consultatie sloot in juni 2026; finale wet is er nog niet. Dit is relevant voor Ctac-klanten in gereguleerde sectoren. Bron: [Bird & Bird – Dutch AI Act](https://www.twobirds.com/en/insights/2026/netherlands/dutch-government-publishes-draft-ai-act-implementing-legislation), [Loyens & Loeff](https://www.loyensloeff.com/insights/news--events/news/dutch-implementation-of-the-ai-act-decentralised-ai-supervision/)

**België** – achterloopt op schema  
BIPT wordt aangewezen als hoofdtoezichthouder, maar de formele wetgeving is halverwege 2026 nog niet door het parlement goedgekeurd. Bron: [The AI Act Explained in Full](https://www.ictrechtswijzer.be/en/the-ai-act/)

---

## 🔐 Security & Risk

**Indirecte prompt injection – nu de dominante aanvalsvector**  
Kwaadaardige instructies verstoppen zich in documenten, e-mails en webpagina's die via RAG-pipelines door AI-agents worden ingeladen. Redfox Security meldt dat dit patroon in 2026 de directe injecties heeft overtroffen. Recente incidenten betreffen AI-shopping- en zoekagents en een GitLab AI Gateway-lek. Bron: [RedFox Security Blog 2026](https://www.redfoxsec.com/blog/the-biggest-ai-security-vulnerabilities-discovered-in-2026-redfox-cybersecurity)

**Agent memory poisoning**  
Lakera-onderzoek (november 2026) toont aan dat vergiftigde herinneringen in agentgeheugen kunnen voortbestaan over meerdere sessies — een vector die standaard input-validatie omzeilt. Bron: [Stellar Cyber – Agentic AI Security](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/)

**China-gelieerde actor via AI-agent**  
Amazon rapporteert dat een statelijke actor een zero-day in MONAI Label (medische imaging) exploiteerde door autonome AI-agents in te zetten om de API in kaart te brengen en een reverse shell te plaatsen. Dit is het eerste breed gerapporteerde geval waarbij autonome agents worden ingezet voor advanced persistent threat-activiteit. Bron: [AI Agent News Week of November 22](https://aiagentstore.ai/ai-agent-news/this-week)

---

## 📈 Markt & Adoptie

**Microsoft + IBM: Imagine Enterprise**  
Meer dan 6.000 voorgebouwde AI-agents en assets van IBM Consulting gecombineerd met Microsofts cloud- en AI-infrastructuur. Dit is directe concurrentie voor maatwerk AI-trajecten en onvermijdelijk gespreksonderwerp bij enterprise-klanten van Ctac. Bron: [Cloud Wars – Microsoft IBM](https://cloudwars.com/cloud-wars-minute/microsoft-and-ibm-unite-to-accelerate-enterprise-ai-adoption/)

**Google Cloud groeit 103% (Q3 2026)**  
Omzet naar $30,7 miljard met een operationeel resultaat van $11,1 miljard. AI-workloads drijven deze groei significant. 87% van enterprises hanteert multi-cloud, waarbij Azure + Google Cloud het meest voorkomende koppel is. Bron: [Microsoft vs Google Cloud 2026](https://windowsnews.ai/article/microsoft-vs-google-cloud-2026-ai-flywheel-profit-gap-and-the-enterprise-edge.417378)

**Gartner: 40% enterprise apps met embedded AI agents eind 2026**  
Van minder dan 5% in 2025 naar 40% dit jaar — een exponentiele sprong die veel organisaties verrast. Bron: [Autonomous AI Agents 2026 Analysis](https://www.yaitec.com/en/blog/autonomous-ai-systems-agents-2026)

**OpenAI agents: 46% van langlopende research-taken volledig zelfstandig**  
Dit is niet meer een lab-resultaat maar een operationele benchmark. Bron: [AI News Nov 22 2026](https://riorundown.substack.com/p/ai-news-nov-22-2026-autonomous-systems)

---

## 💡 Ctac-relevantie

**1. Imagine Enterprise als concurrentiescan-prioriteit**  
Microsoft en IBM brengen 6.000+ kant-en-klare AI-agents op de markt. Voor Ctac's enterprise-klanten in finance, overheid en industrie zal dit een standaard referentiepunt worden. Ctac's propositie-onderscheid ligt in maatwerk, domeinkennis en integratie — dat verhaal moet scherper worden geformuleerd nú, niet als de klant er al over begint.

**2. Agentbeveiliging als propositie-element**  
De verschuiving van directe naar indirecte prompt injection, gecombineerd met agent memory poisoning, maakt security een must-have onderdeel van elk AI-agenttraject. Ctac kan zich differentiëren door beveiligingseisen (input-sanitization, tool-access policies, audit logging) structureel te verankeren in haar AI-agentarchitecturen. LangChain's LangSmith Tool Gateway (public beta 19 november) biedt hiervoor direct bruikbare tooling.

**3. EU AI Act compliance – urgentie voor december 2026**  
De deadline van 2 december voor watermarking en NCII-verbod is over negen dagen. Klanten in media, communicatie en overheid die generatieve AI-toepassingen draaien moeten dit gecontroleerd hebben. Dit is een directe aanleiding voor een kort compliancegesprek met relevante accounts.

**4. Nederlandstalig toezichtlandschap**  
Met de Nederlandse conceptwetgeving in circulatie en België dat achterloopt, is er een gat in kennis bij klanten. Ctac kan hier als trusted advisor optreden — niet als jurist, maar als organisatie die de operationele implicaties vertaalt.

---

## 📚 Bronnen & verder lezen

- [AI News This Week: GPT-6.2, Gemini 4 Neon, Anthropic IPO](https://larwell.com/blog/ai-news-this-week-november-22-2026)
- [LLM News Today – November 2026 (llm-stats.com)](https://llm-stats.com/ai-news)
- [LLM Release Tracker 2026](https://nhimg.org/llm-release-tracker)
- [AI Agents News Brief 18 november 2026](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-18-2026)
- [AI Agent News – Week of November 22, 2026](https://aiagentstore.ai/ai-agent-news/this-week)
- [EU AI Act – Digital Strategy EC](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU AI Act Compliance Guide 2026 (orbiqhq.com)](https://www.orbiqhq.com/eu-regulations/eu-ai-act-compliance)
- [Bird & Bird – Dutch AI Act implementatiewet](https://www.twobirds.com/en/insights/2026/netherlands/dutch-government-publishes-draft-ai-act-implementing-legislation)
- [Loyens & Loeff – Gedecentraliseerd AI-toezicht NL](https://www.loyensloeff.com/insights/news--events/news/dutch-implementation-of-the-ai-act-decentralised-ai-supervision/)
- [The AI Act Explained in Full (ictrechtswijzer.be)](https://www.ictrechtswijzer.be/en/the-ai-act/)
- [RedFox Security – AI kwetsbaarheden 2026](https://www.redfoxsec.com/blog/the-biggest-ai-security-vulnerabilities-discovered-in-2026-redfox-cybersecurity)
- [Stellar Cyber – Agentic AI Security Threats](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/)
- [Cycode – AI Security Vulnerabilities 2026](https://cycode.com/blog/ai-security-vulnerabilities/)
- [Cloud Wars – Microsoft + IBM Imagine Enterprise](https://cloudwars.com/cloud-wars-minute/microsoft-and-ibm-unite-to-accelerate-enterprise-ai-adoption/)
- [Microsoft vs Google Cloud 2026 (windowsnews.ai)](https://windowsnews.ai/article/microsoft-vs-google-cloud-2026-ai-flywheel-profit-gap-and-the-enterprise-edge.417378)
- [Autonomous AI Agents 2026 (yaitec.com)](https://www.yaitec.com/en/blog/autonomous-ai-systems-agents-2026)
- [AI News Nov 22 2026 – Autonomous Systems (riorundown)](https://riorundown.substack.com/p/ai-news-nov-22-2026-autonomous-systems)
