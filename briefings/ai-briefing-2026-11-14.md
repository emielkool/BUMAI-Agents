---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-14
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 14 november 2026

## 🔑 Highlights van de dag

- **Gemini 4 Hydrogen gelanceerd** – Google bracht gisteren (13 nov) zijn nieuwste Gemini-generatie uit; eerder in de week verscheen ook Gemini 4 Carbon (10 nov) en Gemini Decision 1 (11 nov). Google rijgt de releases aan elkaar.
- **Nederland presenteert AI-visie** – Het kabinet publiceerde op 6 november een 28 pagina's tellende AI-strategie met open strategische autonomie als kern én toetreding tot Pax Silica, een Amerikaans partnerschap rond chips en rekenkracht.
- **EU AI Act: deadline 2 december nadert** – Vanaf die datum eindigt de nalevingsperiode voor bestaande generatieve systemen en treden twee nieuwe verboden in werking. Organisaties die nog niet hebben gehandheld moeten nú actie ondernemen.
- **AgentCore-kwetsbaarheid bij AWS** – Een enkele prompt kon metadata-credentials onttrekken en alle agents in een AWS-account en -regio overnemen. Een ernstig signaal voor iedereen die agentic workloads in de cloud draait.
- **MCP bereikt 16.000+ servers** – Het Model Context Protocol is na korte terugslag vroeg in 2026 de de-facto standaard voor agent-to-tool-integratie geworden; Google's A2A-protocol volgt voor agent-to-agent-coördinatie met meer dan 100 bedrijven achter zich.

---

## 🧠 Technologie & Modellen

**Gemini 4-familie** – Google heeft afgelopen week drie modellen gelanceerd: Gemini 4 Carbon (10 nov), Gemini Decision 1 (11 nov, kennelijk gericht op gestructureerde beslissingsondersteuning) en Gemini 4 Hydrogen (13 nov). Precieze benchmarks zijn nog niet officieel bevestigd – let op de officiële blogpost van Google voor technische details. Trackers als LLM Gateway en Opper.ai tonen de releases maar hun datums lopen soms uiteen.
([llmgateway.io](https://llmgateway.io/timeline) | [opper.ai](https://opper.ai/model-releases))

**Claude Fable 5.2** – Trackers noteren 9 november als releasedatum; Anthropic heeft dit niet officieel bevestigd via hun newspage. Behandelen als onbevestigd tot primaire publicatie beschikbaar is.

**Meta Muse Ember 1.0** – Op 10 november. Positie in de markt nog onduidelijk; interessant voor open-source-afweging.

**Agentic infrastructuur consolideert** – MCP heeft 16.000+ servers en 97 miljoen maandelijkse SDK-downloads. LangGraph, CrewAI, AutoGen en Semantic Kernel convergeren naar vergelijkbare abstracties. Langfuse (observability) is begin 2026 overgenomen door ClickHouse, wat AI-monitoring mainstream infrastructuur maakt.
([stackone.com](https://www.stackone.com/blog/ai-agent-tools-landscape-2026/))

---

## 🏛️ Governance & Ethiek

**EU AI Act – 2 december deadline** – De nalevingsperiode voor bestaande generatieve systemen loopt af op 2 december 2026. Twee aanvullende verboden treden dan ook in werking. De algemene verplichtingen (verboden praktijken, AI-geletterdheidsplicht, transparantie voor chatbots en gegenereerde content) gelden al. De Digital Omnibus (Verordening (EU) 2026/1744, in werking getreden 27 juli) heeft de high-risk-regels voor Bijlage III uitgesteld tot december 2027.
([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | [i-scoop.eu](https://www.i-scoop.eu/eu-ai-act-timeline-digital-omnibus/))

**Nederland kiest 'AI voor iedereen'** – De kabinetsbrief van 6 november legt de nadruk op open strategische autonomie: Nederland wil zelfstandig keuzes kunnen maken, maar sluit zich tegelijk aan bij Pax Silica (Amerikaans partnerschap over chips, rekenkracht en AI-infrastructuur). Concrete middelen blijven beperkt: €120 miljoen voor EU-AI-project al in september vastgelegd; verdere infrastructuurplannen volgen pas begin 2027. Een adviesrapport over een Nederlands AI-veiligheidsinstituut wordt in december verwacht.
([rijksoverheid.nl](https://www.rijksoverheid.nl/actueel/nieuws/2026/11/06/kabinet-kiest-voor-ai-die-nederland-vooruithelpt) | [dutchnews.nl](https://www.dutchnews.nl/2026/11/cabinet-sets-out-ai-plan-seeks-partners-beyond-us-and-china/))

---

## 🔐 Security & Risk

**SGLang RCE → NEAR AI-inbreuk** – Op 8 november gebruikte een aanvaller een remote code execution-lek in de open-source inferentie-engine SGLang om op een productieserver van NEAR AI te draaien. Verzoeken, ook die in "confidential mode", waren zichtbaar. Cloudflare Workers AI had een verwant cross-tenant-probleem. Betekenis: shared inference-infrastructure is een aantrekkelijk doelwit; zelf gehoste of goed geïsoleerde deployments verdienen heroverweging.
([adversa.ai](https://adversa.ai/blog/top-genai-security-resources-november-2026/))

**Amazon Bedrock AgentCore-kwetsbaarheid** – Één kwaadaardige prompt kon metadata-credentials opvragen en zo alle agents binnen een AWS-account en -regio overnemen. Voor enterprise-teams die Bedrock gebruiken is een directe controle op IAM-isolatie en promptsanitisatie aanbevolen.
([adversa.ai](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/))

**Copilot RCE gepatcht door Microsoft** – Remote code execution in Visual Studio en SSMS via GitHub Copilot; Microsoft heeft inmiddels gepatcht. Houd patchbeheer voor AI-tooling in IDE's bij op dezelfde prioriteit als reguliere software-updates.

**Supply chain in agent-frameworks** – Een Barracuda-rapport signaleerde 43 kwetsbare componenten in veelgebruikte agent-frameworks, geïntroduceerd via supply chain compromise. Combineer dit met Lakera-onderzoek naar memory poisoning (vergiftigde agentmemory die onjuiste overtuigingen in stand houdt) en het beeld is duidelijk: de aanvalsoppervlakte van AI-agents is structureel groter dan die van traditionele software.

---

## 📈 Markt & Adoptie

**IBM + Microsoft 'Imagine Enterprise'** – Op 10 november kondigden IBM en Microsoft een samenwerking aan waarbij meer dan 6.000 IBM Consulting AI-agents gecombineerd worden met Microsoft Cloud- en AI-technologie. Salesforce rapporteert 21x groei in Agentforce-gebruik over drie maanden.
([infotechlead.com](https://infotechlead.com/artificial-intelligence/top-15-enterprise-ai-agent-platforms-for-2027-microsoft-salesforce-google-aws-ibm-and-servicenow-compared-99632))

**Adoptie breed, optimalisatie smal** – Accenture-onderzoek (november 2026) stelt dat 64% van de CIO's AI aan het opschalen is, maar slechts 7% dit op enterprise-niveau heeft geoptimaliseerd. Deployment is geen eindpunt; ROI-realisatie is de nieuwe uitdaging.
([infotechlead.com](https://infotechlead.com/artificial-intelligence/64-of-cios-are-scaling-ai-but-only-7-have-optimized-it-microsoft-google-aws-and-ibm-face-enterprise-roi-test-99540))

**Cloudgroei accelereert** – Google Cloud: 2.600 klanten verbruikten de afgelopen 12 maanden meer dan 100 miljard tokens. Microsoft 365 Copilot-klanten op consumption-based billing groeiden >75% kwartaal-op-kwartaal. AWS-Fortune 500-spending vrijwel vertienvoudigd jaar-op-jaar.
([finance.yahoo.com](https://finance.yahoo.com/technology/ai/articles/citi-raises-ai-revenue-forecasts-114800473.html))

---

## 💡 Ctac-relevantie

**EU AI Act 2 december** vereist directe actie richting klanten: transparantie-eisen voor generatieve toepassingen en verboden praktijken gelden nu. Ctac kan klanten in overheid, zorg en finance helpen met een snelle gap-analyse vóór de deadline. Dit is een concrete, korte-termijn propositie.

**Nederlandse AI-visie** – De keuze voor open strategische autonomie én Pax Silica bevestigt dat de Nederlandse overheid AI als strategisch thema serieus neemt, maar het geld is vooralsnog mager. Voor Ctac's publieke-sectorpraktijk biedt dit aanknopingspunten voor gesprekken over AI-beleid en -governance, maar concrete budgetten voor AI-trajecten laten vermoedelijk op zich wachten tot 2027.

**AgentCore/agent-security** – Naarmate Ctac meer agentic oplossingen voor klanten bouwt of beheert, wordt AI-security een aparte competentie naast klassieke security. De AgentCore-kwetsbaarheid illustreert dat IAM-isolatie, promptsanitisatie en monitoring van agents als architectuureisen moeten worden meegenomen vanaf dag één.

**IBM-Microsoft partnership** – SAP (een bestaand Ctac-domein) zal als reactie op IBM-Microsoft de concurrentie voelen. Interessant om te volgen of SAP AI-partnerships versnellen.

**7%-optimalisatiekloof** – Het Accenture-gegeven is een krachtig verkoopargument: de meeste bedrijven zíjn begonnen met AI, maar halen de ROI niet. Ctac kan positioneren als de partner die van deployment naar impact beweegt.

---

## 📚 Bronnen & verder lezen

- [LLM Gateway – model release timeline](https://llmgateway.io/timeline)
- [Opper.ai – AI Model Release Tracker](https://opper.ai/model-releases)
- [Europese Commissie – EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Europese Commissie – AI Act standaardisatie](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation)
- [i-scoop.eu – EU AI Act na Digital Omnibus](https://www.i-scoop.eu/eu-ai-act-timeline-digital-omnibus/)
- [Cubbbix – EU AI Act artikel 50 en 2 december deadline](https://cubbbix.com/blog/eu-ai-act-explained-2026)
- [Rijksoverheid – AI-visie kabinet](https://www.rijksoverheid.nl/actueel/nieuws/2026/11/06/kabinet-kiest-voor-ai-die-nederland-vooruithelpt)
- [DutchNews – Dutch cabinet AI plan](https://www.dutchnews.nl/2026/11/cabinet-sets-out-ai-plan-seeks-partners-beyond-us-and-china/)
- [Binnenlands Bestuur – AI-veiligheidsinstituut NL](https://www.binnenlandsbestuur.nl/digitaal/kabinet-wil-eigen-ai-koers-maar-de-vs-is-nooit-ver-weg)
- [Adversa.ai – GenAI security november 2026](https://adversa.ai/blog/top-genai-security-resources-november-2026/)
- [Adversa.ai – AI agent security november 2026](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/)
- [Adversa.ai – AI coding agent vulnerabilities](https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/)
- [InfotechLead – IBM + Microsoft Imagine Enterprise](https://infotechlead.com/artificial-intelligence/top-15-enterprise-ai-agent-platforms-for-2027-microsoft-salesforce-google-aws-ibm-and-servicenow-compared-99632)
- [InfotechLead – Accenture 7% CIO optimalisatie](https://infotechlead.com/artificial-intelligence/64-of-cios-are-scaling-ai-but-only-7-have-optimized-it-microsoft-google-aws-and-ibm-face-enterprise-roi-test-99540)
- [Yahoo Finance / Citi – AI cloud revenue forecasts](https://finance.yahoo.com/technology/ai/articles/citi-raises-ai-revenue-forecasts-114800473.html)
- [StackOne – AI agent tools landscape 2026](https://www.stackone.com/blog/ai-agent-tools-landscape-2026/)
- [AIC4NL – Kabinet kiest voor AI voor iedereen](https://aic4nl.nl/nieuws/kabinet-kiest-voor-ai-voor-iedereen/)
