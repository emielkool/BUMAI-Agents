---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-23
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 23 april 2026

## 🔑 Highlights van de dag

- **Google Cloud Next 2026 domineert het nieuws**: Google presenteerde gisteren zijn 8e generatie TPU-chips (3× sneller trainen, 80% betere prijs/prestatie) én sloot een deal van enkele miljarden met Mira Murati's Thinking Machines Lab voor Nvidia GB300-infrastructuur.
- **EU AI Act definitieguidelines gepubliceerd (8 april)**: De Europese Commissie bracht richtsnoeren uit voor de definitie van 'AI-systemen' – het eerste praktische handvat voor compliance, met de volledige toepasbaarheid per 2 augustus 2026 in zicht.
- **Claude Code-broncode gelekt via npm**: Anthropic publiceerde per ongeluk 512.000 regels TypeScript; onderzoekers brachten drie aanvalsroutes in kaart. Prompt-injection blijft structureel onoplosbaar.
- **AI-uitgaven naderen 25% van alle IT-budgets**: Cloud capex stijgt in 2026 met 40% naar bijna $600 miljard; Microsoft en Google nemen de enterprise-markt voor AI in een houdgreep.
- **Agentic AI breekt door in Nederland**: Van hypotheekaanvragen tot commerce – de experimenteerfase is voorbij, grootschalige inzet begint nu.

## 🧠 Technologie & Modellen

**Google Cloud Next 2026 – 8e generatie TPUs**
Google presenteerde gisteren (22 april) twee nieuwe chipgeneraties: de TPU 8t (gericht op modeltraining) en TPU 8i (inference-geoptimaliseerd). Specificaties: tot 3× sneller trainen, 80% betere prijs/prestatieverhouding, en clusters tot 1 miljoen+ TPUs. Dit maakt Google's eigen infrastructuur direct concurrerend met Nvidia H100/GB300-clusters. Tegelijkertijd sloot Google een deal in de miljarden met Thinking Machines Lab (Mira Murati) voor toegang tot GB300-gebaseerde rekencapaciteit – opvallend: eigen chips bouwen én externe capaciteit inkopen zijn geen tegenpolen maar een bewuste portfolio-strategie. ([TechCrunch](https://techcrunch.com/2026/04/22/google-cloud-next-new-tpu-ai-chips-compete-with-nvidia/) | [Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/))

**GPT-5.4 & Anthropic Mythos**
OpenAI's GPT-5.4 bundelt redenering, coding en agentische workflows in één frontier-model. Anthropic's Mythos-preview is beschikbaar voor 40 partnerbedrijven en richt zich specifiek op cybersecurity. Geen publieke benchmarks; aankondigingen zijn hier groter dan de beschikbare evidence.

## 🏛️ Governance & Ethiek

**EU AI Act definitieguidelines – 8 april 2026**
De Europese Commissie publiceerde richtsnoeren over wat precies als 'AI-systeem' kwalificeert. Dit is het eerste concrete handvat voor compliance, nu de volledige toepasbaarheid per 2 augustus 2026 nadert. Nog te verschijnen dit jaar: guidelines voor hoog-risico-classificatie, transparantievereisten (art. 50) en incidentrapportage. Voor organisaties zonder gap-analyse loopt de tijd terug. ([EC digitale strategie](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-ai-system-definition-facilitate-first-ai-acts-rules-application))

**Nederlandse overheid investeert €70 miljoen in AI-fabriek Groningen**
Het Rijk versterkt de AI-fabriek in Groningen met €70 miljoen extra, bovenop eerder regionale investeringen. Relevant voor rekencapaciteit en onderzoek, maar los van de bredere adoptie-achterstand van het Nederlandse bedrijfsleven. ([NOS](https://nos.nl/artikel/2572670-rijk-steekt-nu-ook-70-miljoen-in-ai-fabriek-groningen))

## 🔐 Security & Risk

**Claude Code broncode-lek en prompt injection**
Anthropic publiceerde per ongeluk een 59,8 MB JavaScript source map van Claude Code op npm (versie 2.1.88), waardoor ~512.000 regels TypeScript openbaar werden en direct gespiegeld op GitHub. Onderzoekers identificeerden drie concrete aanvalsroutes. Parallel exploiteerden aanvallers een prompt-injection-kwetsbaarheid in Claude Code's Security Review GitHub Action – een feature die Anthropic's eigen system card expliciet als "not hardened against prompt injection" bestempelt. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [VentureBeat – broncode-lek](https://venturebeat.com/security/claude-code-512000-line-source-leak-attack-paths-audit-security-leaders))

**Agentic AI als nieuw aanvalsoppervlak**
Drie AI-coding agents lekten gevoelige credentials via één prompt-injection-aanval doordat credential-opslag en sandboxomgeving voor onvertrouwde code gedeeld zijn. Architectuuroplossingen bestaan (credential-isolatie, zero-trust sandboxes), maar vereisen bewuste designkeuzes. OpenAI en het Britse NCSC bevestigen: prompt injection is met huidige LLM-technologie structureel niet volledig te dichten.

## 📈 Markt & Adoptie

**Cloud capex +40%, AI bereikt 25% van IT-budgets**
Cloud-providers investeren in 2026 bijna $600 miljard in infrastructuur. AI-gerelateerde uitgaven zijn al goed voor bijna een kwart van alle IT-budgets. Microsoft en Google domineren de enterprise-markt; SAP integreert agentische AI in transactionele bedrijfsprocessen via Nvidia's enterprise AI-agentplatform – met Adobe en Salesforce als vroege adopters. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among))

**Agentic AI in Nederland wordt operationeel**
2026 is het jaar waarin proefprojecten plaatsmaken voor productie. Hypotheekverstrekkers automatiseren aanvraagprocessen; retailers zetten AI-shopping-assistants in als primair klantkanaal. De adoptielat ligt hoger – organisaties die nu nog experimenteren, raken achterop. ([Computable](https://www.computable.nl/2025/12/05/fundamentele-transformatie-in-2026-door-agentic-ai/))

## 💡 Ctac-relevantie

**EU AI Act compliance wordt urgent**: Met de volledige toepasbaarheid per augustus 2026 en nieuwe definitieguidelines is dit het juiste moment voor Ctac om klanten in gereguleerde sectoren (overheid, zorg, finance) te begeleiden bij compliance-trajecten. Een concrete AI-Act gap-analyse + risicoklassificatie is nu verkoopbaar als tijdgebonden dienst.

**Agentic AI als propositie**: De Nederlandse markt is klaar voor grootschalige agentic deployments. Ctac kan concrete use cases leveren in sectoren als gemeentelijke dienstverlening, hypotheekverlening en logistiek – mits de architectuur rekening houdt met de bewezen beveiligingsrisico's (credential-isolatie, prompt-injection-mitigatie). Dit is precies het snijvlak van strategische AI-adoptie en technische solidity waar Ctac onderscheidend kan zijn.

**Security by design bij AI-tooling**: De lessen van het Claude Code-lek en de prompt-injection-exploits zijn direct toepasbaar in Ctac's eigen ontwikkelomgevingen en klantprojecten. Eloy's aandacht voor agentic architectuur kan hier een concreet securitykader aan koppelen als interne standaard.

## 📚 Bronnen & verder lezen

- [Google Cloud Next 2026: 8e gen TPUs – TechCrunch](https://techcrunch.com/2026/04/22/google-cloud-next-new-tpu-ai-chips-compete-with-nvidia/)
- [Google blog: 8th gen TPUs for the agentic era](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
- [Google deepens Thinking Machines Lab deal – TechCrunch](https://techcrunch.com/2026/04/22/exclusive-google-deepens-thinking-machines-lab-ties-with-new-multi-billion-dollar-deal/)
- [Anthropic Mythos preview – TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [EU AI Act definitieguidelines – EC digitale strategie](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-ai-system-definition-facilitate-first-ai-acts-rules-application)
- [AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [Drie AI-coding agents lekten credentials via prompt injection – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Claude Code broncode-lek: 512.000 regels – VentureBeat](https://venturebeat.com/security/claude-code-512000-line-source-leak-attack-paths-audit-security-leaders)
- [Microsoft en Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [NOS: Rijk investeert €70 mln in AI-fabriek Groningen](https://nos.nl/artikel/2572670-rijk-steekt-nu-ook-70-miljoen-in-ai-fabriek-groningen)
- [Computable: Agentic AI fundamentele transformatie 2026](https://www.computable.nl/2025/12/05/fundamentele-transformatie-in-2026-door-agentic-ai/)
