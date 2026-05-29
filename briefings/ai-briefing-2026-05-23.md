---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-23
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 23 mei 2026

## 🔑 Highlights van de dag

- **Claude Opus 4.7 live** – Anthropic bracht vandaag Opus 4.7 beschikbaar via alle producten en API's, inclusief Amazon Bedrock, Google Vertex AI en Microsoft Foundry. Tegelijk is in een besloten kring "Mythos" uitgerold, omschreven als het krachtigste model tot nu toe met sterke toepassingen voor cybersecurity.
- **AI Act-deadline nadert: augustus 2026** – Een politiek akkoord op de AI Omnibus-amendementen (7 mei) én de EC-consultatieronde over uitvoeringsrichtlijnen (19 mei) markeren de eindsprint vóór volledige toepasbaarheid op 2 augustus 2026. Nu handelen is geen keuze meer.
- **Microsoft Agent 365 schaalt razendsnel** – Twee maanden na GA (1 mei) telt het Agent 365-register al tienduizenden klanten en tientallen miljoenen geregistreerde agents. Met Azure Foundry bereikt Microsoft 80% van de Fortune 500.
- **OpenAI verdiept enterprise-grip** – Codex wordt wekelijks door 4 miljoen mensen gebruikt, OpenAI is door Gartner uitgeroepen tot leider in enterprise AI coding agents, en het bedrijf neemt AI-consultancybedrijf Tomoro over om deploymentcapaciteit te vergroten.
- **Prompt injection escaleert mee met agentische AI** – 2026 vergroot het aanvalsoppervlak doordat agents meer autonomie en toolintegraties krijgen. Attack success rates overstijgen 85%; OpenAI erkent dat volledige oplossing waarschijnlijk nooit haalbaar is.

---

## 🧠 Technologie & Modellen

**Anthropic Claude Opus 4.7 + Mythos**
Anthropic lanceerde vandaag [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7), het nieuwste topmodel, breed beschikbaar via Bedrock, Vertex AI en Foundry. Daarnaast circuleert intern het model "Mythos", vooralsnog alleen voor select partners, met als speerpunt geavanceerde cybersecurity-toepassingen. Dit duidt op een bewuste strategie: een publiek algemeen model én een besloten specialistisch model voor hoogrisico-domeinen.

**OpenAI Codex & Gartner-erkenning**
OpenAI's Codex telt [4 miljoen wekelijkse gebruikers](https://openai.com/index/gartner-2026-agentic-coding-leader/) en staat bovenaan de Gartner Magic Quadrant voor Enterprise AI Coding Agents. De introductie van GPT‑5.5 verbetert tool use en enterprise-softwareintegraties. OpenAI neemt ook Tomoro over — een applied AI-firma met ~150 deployment engineers — om de implementatiekloof bij klanten te dichten.

**Context architectuur vervangt RAG**
[VentureBeat](https://venturebeat.com/data/context-architecture-is-replacing-rag-as-agentic-ai-pushes-enterprise-retrieval-to-its-limits) signaleert een verschuiving: hybrid retrieval intent bij enterprise steeg van 10% naar 33% in Q1 2026. Retrieval-optimalisatie is voor het eerst de topprioriteit boven evaluatie — relevant voor architectuurkeuzes bij Ctac-projecten.

---

## 🏛️ Governance & Ethiek

**AI Act: eindsprint richting augustus 2026**
Op [7 mei bereikte de EC politiek akkoord](https://artificialintelligenceact.eu/) over AI Omnibus-amendementen die de bevoegdheden van de AI Office verstevigen en het toezicht op GPAI-modellen centraliseren. Op 19 mei opende de Commissie een feedbackronde over conceptrichtlijnen voor implementatie. Volledige toepasbaarheid: **2 augustus 2026**.

De aanscherping van het AI Office vermindert governance-fragmentatie tussen lidstaten, wat voor Nederlandse en Belgische ondernemingen in theorie meer duidelijkheid biedt — maar ook minder speelruimte voor eigen interpretatie. Ctac-klanten in gereguleerde sectoren (zorg, overheid) hebben nu een concreet deadline om risk-classificaties en documentatieverplichtingen te borgen.

---

## 🔐 Security & Risk

**Prompt injection: aanhoudend structureel probleem**
OWASP rankt prompt injection als kwetsbaarheid #1 in LLM-toepassingen; [Airia](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) analyseert de 2026-variant als een "lethal trifecta" waarbij toenemende agentautonomie, bredere toolintegraties en gebrekkige sandboxing samenkomen. Aanvalssuccespercentages liggen boven de 85% als adaptieve aanvalstechnieken worden gebruikt.

**PromptPwnd: nieuwe aanvalsklasse via GitHub Actions**
Een specifieke nieuwe exploit richt zich op AI-agents gekoppeld aan kwetsbare GitHub Actions en dwingt ze tot het uitvoeren van geprivilegieerde ingebouwde tools via geïnjecteerde instructies. Dit is direct relevant voor Ctac-projecten waarbij agentische coding assistants worden gebruikt in CI/CD-pipelines.

OpenAI's eigen conclusie — prompt injection is "unlikely to ever be fully solved" — maakt duidelijk dat dit een risico is dat beheerd moet worden, niet opgelost.

---

## 📈 Markt & Adoptie

**Microsoft domineert enterprise AI-infrastructuur**
[Azure Foundry](https://azure.microsoft.com/en-us/blog/advancing-enterprise-ai-new-sap-on-azure-announcements-from-sap-sapphire-2026/) bedient 80.000 klanten (80% Fortune 500). Microsoft Agent 365 (GA 1 mei, $15/user) is het governanceplatform voor het beheer van enterprise AI-agents en groeit explosief. De SAP-Azure samenwerking (RISE with SAP Acceleration) wordt in 2026 verdubbeld — bij Ctac's SAP-klanten een direct relevant gegeven.

**OpenAI's enterprise-inkomsten passeren 40%**
Enterprise vertegenwoordigt nu >40% van OpenAI's omzet en koerst af op gelijkheid met consumer eind 2026. De [overname van Tomoro](https://openai.com/index/openai-launches-the-deployment-company/) en de oprichting van The Deployment Company ($4B, $10B-waardering) laten zien dat OpenAI de implementatiefase serieus neemt — en de marge bij consultancybedrijven wil verkleinen.

**Salesforce Agentforce Operations**
[Salesforce](https://venturebeat.com/orchestration/salesforce-launches-agentforce-operations-to-fix-the-workflows-breaking-enterprise-ai) pakt een hardnekkig probleem aan: bedrijven die AI-agents uitrollen in back-office systemen botsen op workflows die nooit voor agents zijn gebouwd. Agentforce Operations biedt monitoring en hersteltools voor falende handoffs. Dit is een signaal dat enterprise AI adoptie de "deployment gap" heeft bereikt.

---

## 💡 Ctac-relevantie

**Directe prioriteiten:**

1. **AI Act compliance-scan voor klanten** — De deadline van 2 augustus 2026 is nu minder dan 11 weken weg. Ctac moet nu klanten in hoog-risico sectoren (overheid, zorg, finance) actief benaderen voor risk-classificatie, documentatie en governanceverplichtingen. Dit is een concrete propositie die vandaag verkoopbaar is.

2. **Security-integratie in agentische projecten** — De PromptPwnd-aanvalsklasse en de aanhoudend hoge succeskans van prompt injection maken het noodzakelijk dat elke agentische oplossing die Ctac bouwt een expliciete security-laag bevat. Sandbox-isolatie, input/output-filtering en auditlogging zijn geen nice-to-have meer.

3. **Microsoft-stack is de de-facto enterprise backbone** — Met Agent 365, Azure Foundry en de SAP-uitbreiding consolideert Microsoft zijn positie als primair platform voor enterprise AI. Ctac doet er goed aan Foundry-kennis op te bouwen en Microsoft Agent 365-implementaties als propositie-item te markeren — zeker bij SAP-klanten.

4. **Deployment-gap is een kans** — OpenAI's Tomoro-overname en Salesforce's Agentforce Operations signaleren een markt die AI heeft aangeschaft maar vastloopt op implementatie. Dit is precies de ruimte waar een consultancybedrijf als Ctac waarde kan toevoegen: niet modelbouwen, maar deployen, integreren en borgen.

---

## 📚 Bronnen & verder lezen

- [Anthropic – Claude Opus 4.7 aankondiging](https://www.anthropic.com/news/claude-opus-4-7)
- [OpenAI – Gartner Magic Quadrant Enterprise AI Coding Agents](https://openai.com/index/gartner-2026-agentic-coding-leader/)
- [OpenAI – The Deployment Company lancering](https://openai.com/index/openai-launches-the-deployment-company/)
- [TechCrunch – Google declared AI design contender at IO 2026](https://techcrunch.com/2026/05/19/ai-design-tools-are-the-next-big-battleground-and-google-is-going-all-in-at-io-2026/)
- [TechCrunch – Anthropic & OpenAI enterprise joint ventures](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/)
- [EU AI Act – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act – National Implementation Plans overzicht](https://artificialintelligenceact.eu/national-implementation-plans/)
- [EC – Supporting AI Act implementation with clear guidelines](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Airia – AI Security in 2026: Prompt Injection & the Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [VentureBeat – 11 runtime attacks breaking AI security](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)
- [The Hacker News – PromptPwnd en OpenClaw AI Agent kwetsbaarheden](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html)
- [Microsoft Azure – SAP Sapphire 2026 enterprise AI aankondigingen](https://azure.microsoft.com/en-us/blog/advancing-enterprise-ai-new-sap-on-azure-announcements-from-sap-sapphire-2026/)
- [Microsoft – State of global AI diffusion in 2026](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)
- [VentureBeat – Salesforce Agentforce Operations](https://venturebeat.com/orchestration/salesforce-launches-agentforce-operations-to-fix-the-workflows-breaking-enterprise-ai)
- [VentureBeat – Context architecture vervangt RAG bij enterprise retrieval](https://venturebeat.com/data/context-architecture-is-replacing-rag-as-agentic-ai-pushes-enterprise-retrieval-to-its-limits)
