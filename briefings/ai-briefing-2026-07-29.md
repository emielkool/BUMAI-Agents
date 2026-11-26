---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-29
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 29 juli 2026

## 🔑 Highlights van de dag

- **MCP krijgt grootste update ooit (28 juli):** Het Model Context Protocol is overgegaan op een volledig stateless architectuur, met officiële extensies voor rijke agent-UI's en langlopende taken — dit verlaagt de infrastructuurkosten en maakt productie-ready agent-platforms serieuzer haalbaar.
- **AI Omnibus in werking getreden (27 juli):** De EU AI Omnibus — een vereenvoudigde herziening van de AI Act — is officieel van kracht; nationale AI-sandboxen moeten uiterlijk 2 augustus 2026 operationeel zijn.
- **OpenAI-agentinbraak gereconstrueerd:** Hugging Face's securityteam documenteerde hoe de juli-breuk bij OpenAI (~17.600 aanvallersacties, days undetected) verliep — een helder signaal dat productie-AI-agenten nieuwe beveiligingsdisciplines vereisen.
- **Kimi K3: grootste open-source model ooit:** Moonshot AI publiceerde Kimi K3 (2,8 biljoen parameters, MoE, 1M-token context, native vision) — de facto een serieuze open-source rivaal van GPT-5.6 en Gemini 3.6.
- **Open Secure AI Alliance gelanceerd:** Nvidia, Microsoft, IBM en 30+ partners richtten gezamenlijk een AI-cyberdefensie-alliantie op; opvallend afwezig zijn OpenAI, Google en Anthropic.

---

## 🧠 Technologie & Modellen

**MCP 2026-07-28 specificatie** is de grootste wijziging sinds de lancering. Het protocol stapt over op een stateless request/response-kern, harden de authenticatie, introduceert een formeel 12-maanden deprecatiebeleid en maakt twee nieuwe extensies officieel: *MCP Apps* (server-rendered agent-UI's) en *MCP Tasks* (duurzame task-handles voor langlopende bewerkingen). Beheer is overgedragen aan de Agentic AI Foundation (Linux Foundation). ([VentureBeat](https://venturebeat.com/infrastructure/mcp-just-got-its-biggest-update-ever-heres-what-changes-for-ai-agents))

**Kimi K3** van Moonshot AI (China) is uitgebracht als open-source: 2,8T MoE-parameters, native visueel begrip, 1M-token context en 2,5× hogere efficiëntie ten opzichte van de voorgaande architectuur. Dit is het grootste open-source model ooit gepubliceerd en daarmee direct vergelijkbaar met de frontiermodellen van OpenAI en Google. ([VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems))

**Google Gemini 3.6 Flash** (21 juli) biedt verbeterde coding- en multimodale prestaties bij 17% lagere tokenprijzen dan Gemini 3.5 Flash. OpenAI's GPT-5.6 (Sol/Terra/Luna, 9 juli) en SpaceXAI's Grok 4.5 (8 juli) brachten dezelfde week uitgebreid modelaanbod. De concurrentie op tokenefficiëntie is nu het dominante marktthema. ([TechCrunch Gemini](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/) | [TechCrunch GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/))

---

## 🏛️ Governance & Ethiek

**AI Omnibus in werking getreden (27 juli 2026):** De verordening vereenvoudigt de AI Act voor het MKB, verlengt een aantal termijnen en biedt meer experimenteerruimte. Tegelijkertijd moeten alle EU-lidstaten vóór 2 augustus 2026 minimaal één nationaal AI-sandbox-regime operationeel hebben. ([Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force))

**EU Cybersecurity & AI actieplan (juli 2026):** De Commissie presenteerde een gecoördineerde aanpak voor AI-modelbeveiliging, inclusief een call om de EU-evaluatiecapaciteit van frontier-modellen te vergroten vóór markttoelating. Een onafhankelijk derde-partij-beoordelingsstelsel wordt verwacht in 2027. ([EU Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

**Kanttekening:** De AI Omnibus maakt compliance voor kleinere spelers makkelijker, maar de kernvereisten voor hoog-risico AI blijven. Voor Ctac-klanten in overheid en zorg verandert er inhoudelijk weinig aan de risicodrempel.

---

## 🔐 Security & Risk

**OpenAI-agentinbraak gereconstrueerd:** Hugging Face publiceerde een gedetailleerde post-mortem van de inbraak op OpenAI's agent-platform (9-13 juli): ~17.600 aanvallersacties, dagenlang onopgemerkt, de FBI moest OpenAI informeren voordat het bedrijf zelf doorhad dat een eigen agent was gecompromitteerd. Moltbook's AI-agentplatform lekte eerder dit jaar 1,5 miljoen API-tokens in plaintext. ([AI News Today](https://aiweekly.co/ai-news-today))

**Open Secure AI Alliance (27 juli):** Nvidia, Microsoft, IBM, Hugging Face en de Linux Foundation — maar niet OpenAI, Google of Anthropic — lanceerden een gedeelde AI-cyberdefensie-coalitie. De strategische splitsing tussen 'frontier' en 'open' aanbieders wordt ook in security zichtbaar. ([AI News July 28](https://www.buildfastwithai.com/blogs/ai-news-today-july-28-2026))

**Capital One VulnHunter (17 juli):** Capital One open-sourcede een agentisch beveiligingstool dat broncoderepositories scant op uitbuitbare kwetsbaarheden vóór aanvallers dat doen. Praktisch bruikbaar voor dev-teams. ([VentureBeat](https://venturebeat.com/technology/capital-one-releases-vulnhunter-an-open-source-ai-tool-that-finds-software-flaws-before-hackers-do))

**Prompt injection** blijft OWASP LLM-risico nr. 1 en is aantoonbaar moeilijker volledig te elimineren dan SQL-injectie. Recent: Microsoft Copilot Studio (CVE-2026-21520, CVSS 7.5). ([VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers))

---

## 📈 Markt & Adoptie

**Microsoft FY26 afsluiting (28 juli):** Microsoft karakteriseert FY26 als de verschuiving "van AI-experiment naar Frontier Transformation" en investeert $2,5 miljard in het insluiten van eigen engineers bij klanten. AWS spiegelt dit met $1 miljard voor vergelijkbare Forward Deployed Engineering-programma's. ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/) | [CIO Dive AWS](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/))

**Twee derde van bedrijven zit vast in pilotfase:** Ondanks miljarden-investeringen is het productieklaar maken van AI de hardnekkigste belemmering. Microsoft verhoogde zijn enterprise-prijzen gemiddeld 16% per juli 2026 — terwijl adoptie achterblijft, stijgen de kosten.

**Nederland:** 61% van de Nederlandse bedrijven heeft AI ingevoerd (vs. 49% vorig jaar), maar SAP stelt dat de Nederlandse markt achterblijft in agent-adoptie — bedrijven blijven hangen bij persoonlijke productiviteitstoepassingen. 58% van de Benelux-bedrijven noemt gebrek aan AI-talent de voornaamste rem. ([Computable](https://www.computable.nl/2026/07/08/sap-pompt-100-miljoen-in-meer-inzet-van-ai-agents/) | [NOS](https://nos.nl/artikel/2572670-rijk-steekt-nu-ook-70-miljoen-in-ai-fabriek-groningen))

---

## 💡 Ctac-relevantie

**MCP als infrastructuurfundament voor agentic dienstverlening:** De nieuwe MCP-specificatie (stateless, MCP Tasks, MCP Apps) maakt het bouwen van productie-waardige multi-agent-workflows concreter haalbaar. Ctac kan dit positioneren als onderdeel van een "agentic backbone"-propositie voor klanten die nu vast zitten in pilotfasen — precies de meerderheid van de markt.

**SAP-bevinding over Nederlandse markt is een directe kans:** Als bedrijven in NL inderdaad achterlopen op agent-adoptie en hangen bij persoonlijke productiviteit, dan is er ruimte voor een implementatiepartner die het gat van experiment naar operationele inzet dicht. Ctac's combinatie van SAP-kennis en AI-unit is hiervoor goed gepositioneerd.

**AI Omnibus en compliance-dienstverlening:** Klanten in overheid en zorg moeten hun AI-systemen opnieuw tegen de (licht vereenvoudigde) AI Act-vereisten leggen. Dit levert directe advies- en implementatievragen op, zeker nu sandboxes verplicht zijn. Ctac kan hier actief op insteken.

**Security is geen bijzaak meer:** De OpenAI-agentinbraak en de Open Secure AI Alliance maken duidelijk dat agent-security een eigen discipline wordt. Klanten die agents in productie nemen hebben behoefte aan securityreviews, red-teaming en monitoring — een aanvullende propositielijn voor Ctac's AI-unit.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [TechCrunch – Gemini 3.6 Flash](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)
- [TechCrunch – SpaceXAI Grok 4.5](https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/)
- [VentureBeat – MCP grootste update ooit](https://venturebeat.com/infrastructure/mcp-just-got-its-biggest-update-ever-heres-what-changes-for-ai-agents)
- [VentureBeat – Kimi K3](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – Capital One VulnHunter](https://venturebeat.com/technology/capital-one-releases-vulnhunter-an-open-source-ai-tool-that-finds-software-flaws-before-hackers-do)
- [Europese Commissie – AI Omnibus in werking](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Microsoft Blog – FY26 terugblik](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [CIO Dive – Microsoft $2,5B engineer-programma](https://www.ciodive.com/news/microsoft-25b-embed-engineers/824392/)
- [CIO Dive – AWS $1B FDE-hub](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)
- [Computable – SAP en AI-agents in Nederland](https://www.computable.nl/2026/07/08/sap-pompt-100-miljoen-in-meer-inzet-van-ai-agents/)
- [AI Weekly – nieuws 29 juli 2026](https://aiweekly.co/ai-news-today)
- [Build Fast With AI – 16 biggest stories 28 juli](https://www.buildfastwithai.com/blogs/ai-news-today-july-28-2026)
