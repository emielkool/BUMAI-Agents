---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-25
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 25 juli 2026

## 🔑 Highlights van de dag

- **Anthropic lanceert Claude Opus 5** (24 juli): Frontier-niveau intelligentie voor de helft van de prijs van Fable 5 — een concrete kostendrempel voor enterprise-inzet van geavanceerde agents.
- **Nederlandse Cyberbeveiligingswet treedt in werking op 15 augustus**: AI-systemen (chatbots, RAG-indexen, agents) vallen hieronder als netwerk- en informatiesystemen; compliance is voor Ctac-klanten acuut.
- **EU lanceert actieplan Cybersecurity & AI** (7 juli): Verplichte pre-market evaluatie van AI-modellen wordt wet; Europese capaciteit wordt uitgebouwd naar 2027.
- **99,9% van patchbare AI-kwetsbaarheden blijft ongepatchd**: Prompt injection is inmiddels #1 op de OWASP Top 10 voor LLM-applicaties — een structureel risico bij agentic AI-implementaties.
- **Agentic AI bereikt productie bij 72% van early adopters**, maar 60% governance-gap en dreiging van projectannulering signaleren: de brug van pilot naar productie is nog niet gebouwd.

## 🧠 Technologie & Modellen

**Claude Opus 5 – Anthropic (24 juli 2026)**
Anthropic bracht gisteren Claude Opus 5 uit, geprijsd op $5/€ miljoen inputtokens en $25/miljoen outputtokens — de helft van wat Fable 5 kost. Het model benadert Fable 5-niveau op agentic coding en kenniswerk, en bevat een nieuw effort-toggle (low/medium/high) waarmee kosten per request instelbaar zijn. Claude Voice Mode is uitgebreid naar Opus- en Sonnet-niveau met ondersteuning voor verbonden tools zoals Gmail en Slack, en meer talen. Vierde model in twee maanden van Anthropic — het tempoverloop in de frontier is op zichzelf een signaal.
*Bron: [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-24/anthropic-unveils-more-cost-efficient-model-for-everyday-tasks), [Streetinsider](https://www.streetinsider.com/Investing/Anthropic+launches+Claude+Opus+5+AI+model+at+half+the+price/26812727.html)*

**Meta Muse Spark 1.1 & NVIDIA Nemotron-Labs-TwoTower**
Meta's Muse Spark 1.1 (1M tokencontext) positioneert zich als alternatief voor Opus 4.8 op agentic evals. NVIDIA releaste een open-weight diffusion language model (Nemotron-Labs-TwoTower) met 2,42× hogere throughput bij 98,7% kwaliteitsretentie — relevant voor on-premise inference bij latency-gevoelige klanten.
*Bron: [llm-stats.com](https://llm-stats.com/llm-updates)*

## 🏛️ Governance & Ethiek

**EU Actieplan Cybersecurity & AI** (gepubliceerd 7 juli)
De Europese Commissie verbindt AI-governance structureel aan de bredere cyberbeveiligingsagenda. Kernpunten: verplichte pre-market evaluatie van geavanceerde AI-modellen (operationeel target 2027), samenwerking met ENISA op een Europees blueprint voor veilige toegang tot AI, en een secuur testplatform voor kritische sectoren. Dit is géén papieren exercitie: het AI Office krijgt de bevoegdheid als uitvoeringsorgaan.
*Bron: [European Commission](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)*

**Nederlandse Cyberbeveiligingswet – ingangsdatum 15 augustus 2026**
De Eerste Kamer stemde op 7 juli in met de Cyberbeveiligingswet en de Wet weerbaarheid kritieke entiteiten. AI-systemen — inclusief chatbots, RAG-indexen en agents met tool-rechten — vallen als NIS-systemen onder de zorgplicht. Organisaties in sectoren als energie, financiën en zorg moeten aantoonbaar voldoen. Dit is voor Ctac-klanten een acuut compliance-vraagstuk.
*Bron: [Digibeter/Substack](https://digibeter.substack.com/p/de-maand-van-de-waarheid-augustus)*

## 🔐 Security & Risk

**Patching-crisis in AI-systemen**
Een rapport van Help Net Security (13 juli) signaleert dat 99,9% van de patchbare kwetsbaarheden in AI-infrastructuur ongepatchd blijft; 81,2% van organisaties met AI-pakketten heeft minimaal één bekende kwetsbaarheid. NIST registreerde >2.000% toename in AI-specifieke CVE's since 2022. Prompt injection staat #1 op de OWASP Top 10 voor LLM Applications.

Afzonderlijk: Cursor IDE bevatte twee zero-click RCE-kwetsbaarheden waarmee sandbox-omgevingen te omzeilen zijn — directe relevantie voor teams die AI-coderingsassistenten gebruiken.
*Bron: [Help Net Security](https://www.helpnetsecurity.com/2026/07/13/ai-infrastructure-security-risks-report/), [Security Boulevard](https://securityboulevard.com/2026/07/top-7-ai-security-risks-in-2026/), [eSecurity Planet](https://www.esecurityplanet.com/weekly-roundup/ai-driven-attacks-critical-exploits-and-global-breaches-define-this-week-in-july-2026-in-cybersecurity/)*

## 📈 Markt & Adoptie

**Microsoft en Google domineren enterprise AI-markt**
CIO Dive bevestigt: Microsoft en Google zijn de dominante AI-leveranciers voor enterprise. Microsoft Copilot groeit traag (1,3% marktaandeel in begin juli); GitHub Copilot is actief bij 90% van de Fortune 100. Microsoft biedt klanten inmiddels keuzevrijheid tussen eigen modellen, third-party (waaronder Anthropic, Google) en open-source — een erkenning dat vendor lock-in een verkoopblokkade is.

**Agentic AI: van pilot naar productie**
91% van bedrijven gebruikt AI in minstens één toepassing (2026), maar twee derde zit vast in pilotfase. De markt voor AI-agents bereikt $10,9–12,1 miljard in 2026 (CAGR ~45% t/m 2030). 40% van enterprise-applicaties zal eind 2026 task-specifieke agents bevatten — de adoptiecurve versnelt, de governance loopt achter.
*Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/), [AgenticAI Institute](https://agenticaiinstitute.org/enterprise-ai-agent-deployment-2026-roi-report/)*

## 💡 Ctac-relevantie

**1. Cyberbeveiligingswet = directe klandbehoefte (augustus 2026)**
Met ingang van 15 augustus vallen AI-implementaties bij Ctac-klanten in gereguleerde sectoren onder de zorgplicht. Dit is een concrete aanleiding voor een compliance-scan-aanbieding: welke AI-systemen heeft een klant, zijn ze geïnventariseerd, zijn risico's gedocumenteerd? Dit is een laagdrempelig instapgesprek met hoge urgentie.

**2. Claude Opus 5 verlaagt de drempel voor frontier-agents**
De halvering van de kosten van geavanceerde Anthropic-modellen maakt het business case voor productie-agents bij mid-market klanten (Ctac's kern) haalbaar. De effort-toggle is bovendien een bruikbaar argument richting klanten die worstelen met AI-kosten op schaal. Ctac kan Opus 5 als standaard aanbevelen voor agentic use cases waar Fable 5 te kostbaar was.

**3. Governance-gap als propositie**
72% van early adopters heeft agents in productie, maar 60% governance-gap — dat is precies waar Ctac als integrator en trusted advisor waarde kan toevoegen. Niet technologie leveren, maar verifiëren, beheersen en verantwoorden. Zeker richting sectoren die onder de Cyberbeveiligingswet vallen.

## 📚 Bronnen & verder lezen

- [Bloomberg – Anthropic lanceert Claude Opus 5](https://www.bloomberg.com/news/articles/2026-07-24/anthropic-unveils-more-cost-efficient-model-for-everyday-tasks)
- [AI Tools Recap – AI News Juli 24](https://aitoolsrecap.com/Blog/ai-news-july-24-2026)
- [European Commission – EU AI Act Governance & Enforcement](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Digibeter – Cyberbeveiligingswet & AI augustus 2026](https://digibeter.substack.com/p/de-maand-van-de-waarheid-augustus)
- [Help Net Security – 99,9% AI vulnerabilities unpatched](https://www.helpnetsecurity.com/2026/07/13/ai-infrastructure-security-risks-report/)
- [Security Boulevard – Top 7 AI Security Risks 2026](https://securityboulevard.com/2026/07/top-7-ai-security-risks-in-2026/)
- [CIO Dive – Microsoft & Google rule enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [AgenticAI Institute – Enterprise AI Deployment ROI 2026](https://agenticaiinstitute.org/enterprise-ai-agent-deployment-2026-roi-report/)
- [llm-stats.com – AI Model Updates Juli 2026](https://llm-stats.com/llm-updates)
- [artificialintelligenceact.eu](https://artificialintelligenceact.eu/)
