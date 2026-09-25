---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-23
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 23 juli 2026

## 🔑 Highlights van de dag

- **AMD Advancing AI 2026** vindt vandaag plaats in San Francisco (22–23 juli): Lisa Su introduceert de Instinct MI450-accelerator, Zen6 EPYC Venice CPU's en het Helios rack-scale AI-systeem. Microsoft breidt Azure-infrastructuur uit met AMD MI455X.
- **EU AI Act D-9:** De transparantieverplichtingen gaan in werking op **2 augustus 2026**. Organisaties die AI-systemen inzetten moeten per direct aantoonbaar kunnen voldoen aan de disclosure-eisen — dit is geen "straks"-moment.
- **Moonshot AI lanceert Kimi K3**, een open 2-biljoen-parameter model met 1-miljoen-token contextvenster en native vision. Het is het eerste openbaar beschikbare 2T-klasse frontiermodel en loopt slechts iets achter op Fable 5 en GPT-5.6 Sol.
- **Satya Nadella waarschuwt** dat bedrijven die AI-modellen van externe labs gebruiken feitelijk hun waardevolste bedrijfskennis overdragen aan de modeleigenaren — die deze kennis kunnen inzetten om concurrenten te worden. Pleidooi voor "fair terms" en eigen learning loops.
- **VS dreigt met sancties** tegen Chinese AI-modellen wegens vermeende IP-diefstal (21 juli). Dit raakt spelers als Moonshot, GLM-5 en DeepSeek en kan het open-source AI-ecosysteem geopolitiek verder fragmenteren.

---

## 🧠 Technologie & Modellen

**AMD zet de agenda voor AI-infrastructuur (vandaag)**
De AMD Advancing AI 2026-conferentie is de grootste hardwareshow van het jaar. De Instinct MI450 en het Helios rack-systeem zijn rechtstreekse concurrenten van NVIDIA's GB200/Blackwell. Dat Microsoft Azure mee investeert, geeft AMD serieuze enterprise-geloofwaardigheid. Voor AI-workloads op schaal is concurrentie op chipniveau direct prijsrelevant. ([AMD](https://www.amd.com/en/corporate/events/advancing-ai/keynote.html), [WCCFTech](https://wccftech.com/watch-amd-advancing-ai-2026-event-live-here/))

**Moonshot Kimi K3: open 2T-model**
Het Chinese Moonshot AI heeft Kimi K3 uitgebracht: 2 biljoen parameters, open gewichten, 1M context, native multimodaal. Het presteert beter dan alle andere open modellen en benadert de frontier. Dit is relevant omdat het de drempel verlaagt voor bedrijven die zware workloads lokaal willen draaien. ([ZoneTechify](https://www.zonetechify.com/blog/ai-news-july-2026-latest-ai-developments))

**Open-source opmars: LongCat-2.0 & SWE-1.7**
LongCat-2.0 (1,6T parameters, MIT-licentie) is het grootste open MoE-model met MIT-licentie tot nu toe. SWE-1.7 (Cognition) bouwt voort op Kimi K2.7 met RL-training voor langlopende software-engineeringtaken — relevant voor coding agents. ([Hugging Face](https://huggingface.co/blog/Svngoku/ai-models-week-july-09-2026))

---

## 🏛️ Governance & Ethiek

**EU AI Act-deadline: 2 augustus nadert snel**
De Europese Commissie heeft richtlijnen gepubliceerd voor de transparantieverplichtingen die per **2 augustus 2026** gelden. Organisaties moeten gebruikers informeren wanneer ze interacteren met AI-systemen (o.a. chatbots, deepfakes). De AI Office heeft zijn handhavingsbevoegdheden versterkt na het vereenvoudigingsakkoord van mei 2026. ([EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines), [EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/))

**VS vs. China: sanctiedreiging over AI-IP**
Washington dreigt met exportmaatregelen en sancties tegen Chinese AI-spelers wegens vermeende IP-diefstal. Dit is een escalatie ten opzichte van eerdere chiprestricties en kan het gebruik van open Chinese modellen in het Westen juridisch compliceren. ([TechCrunch, 21 juli](https://techcrunch.com/2026/07/21/us-threatens-sanctions-against-chinese-ai-models-over-ip-theft/))

---

## 🔐 Security & Risk

**Prompt injection: structureel probleem, geen incident**
Recent onderzoek bevestigt dat 94,4% van state-of-the-art LLM-agents kwetsbaar is voor prompt injection, en 100% voor inter-agent trust exploits. VentureBeat documenteert hoe drie AI coding agents secrets lekten via een enkele geïnjecteerde prompt. Anthropic's eigen system card erkende dat Claude Code Security Review "not hardened against prompt injection" is. Prompt injection is door OWASP voor het tweede jaar op rij #1 LLM-kwetsbaarheid. ([VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers))

**Nadella: AI-labs als data-concurrent**
Satya Nadella's essay is ook een security-framing: bedrijven betalen twee keer — eenmaal in tokens, eenmaal in bedrijfskennis die naar de modelleverancier stroomt. Dit is geen hypothetisch risico maar een structureel governancevraagstuk voor elke enterprise die met externe modellen werkt. ([TechCrunch](https://techcrunch.com/2026/07/13/satya-nadella-has-issued-a-shocking-warning-to-companies-using-ai/))

---

## 📈 Markt & Adoptie

**Microsoft Frontier Company: $2,5 mrd voor enterprise AI-deployment**
Microsoft richt een apart operationeel bedrijf op met 6.000 experts om enterprise-klanten te helpen AI daadwerkelijk te implementeren (niet te piloten). Twee dagen eerder deed AWS iets soortgelijks met $1 mrd. Dit signaleert dat de markt verschuift van model-verkoop naar deployment-dienstverlening. ([TechCrunch, 2 juli](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/))

**SAP unificeert AI-platform**
SAP bundelt Business Technology Platform, Data Cloud en AI in het SAP Business AI Platform, aangevuld met SAP Autonomous Suite voor end-to-end procesautomatisering. Relevant voor klanten van Ctac die SAP-landschappen beheren. ([CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/))

**Twee derde bedrijven zit nog in pilot-fase**
Ondanks alle vendor-investeringen slaagt 66% van de bedrijven er niet in AI van pilot naar productie te brengen. Dit is structureel, niet toevallig: gebrek aan data-governance, change management en use-case-selectie zijn de voornaamste oorzaken. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

---

## 💡 Ctac-relevantie

**EU AI Act D-9 is een actiepunt, geen newsitem.** Ctac-klanten die AI-chatbots of geautomatiseerde besluitvorming inzetten moeten per 2 augustus aantoonbaar voldoen aan de transparantieverplichtingen. Dit is een directe propositiekans voor compliance-advies en implementatiebegeleiding.

**De pilot-to-production gap is Ctac's speelveld.** Twee derde van de markt zit vast in pilots. Microsoft investeert $2,5 mrd in exact dit probleem. Ctac kan hier als trusted integrator inspringen: dicht bij de klant, sector-specifiek, geen hyperscaler. De SAP Autonomous Suite-introductie biedt een concrete haak voor klanten met SAP-landschappen.

**Eigenaarschap van data en learning loops** worden de volgende strategische discussie in enterprise AI (zie Nadella). Klanten helpen bij het opzetten van eigen fine-tuning- of RAG-omgevingen (on-premise of private cloud) is zowel een beveiligings- als een concurrentie-argument. Dit verdient een plek in de propositie-ontwikkeling van de AI-unit.

**Prompt injection in agentic workflows** is een reëel risico bij elk project waarbij Claude Code of andere coding agents worden ingezet. Zorg dat dit als standaard aandachtspunt wordt meegenomen in AI-projectreviews bij klanten.

---

## 📚 Bronnen & verder lezen

- [AMD Advancing AI 2026 Keynote](https://www.amd.com/en/corporate/events/advancing-ai/keynote.html)
- [Watch AMD Advancing AI 2026 Live – MI450, Helios Launch (WCCFTech)](https://wccftech.com/watch-amd-advancing-ai-2026-event-live-here/)
- [Moonshot Kimi K3 & AI News July 2026 (ZoneTechify)](https://www.zonetechify.com/blog/ai-news-july-2026-latest-ai-developments)
- [Open-source AI model week July 9 (Hugging Face)](https://huggingface.co/blog/Svngoku/ai-models-week-july-09-2026)
- [EU AI Act – Transparency obligations 2 August 2026 (EC)](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [EU AI Act Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [US threatens sanctions against Chinese AI models (TechCrunch)](https://techcrunch.com/2026/07/21/us-threatens-sanctions-against-chinese-ai-models-over-ip-theft/)
- [Prompt injection targeting enterprise AI agents (VentureBeat)](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [Three AI coding agents leaked secrets (VentureBeat)](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Satya Nadella warns AI labs will become competitors (TechCrunch)](https://techcrunch.com/2026/07/13/satya-nadella-has-issued-a-shocking-warning-to-companies-using-ai/)
- [Microsoft Frontier Company – $2.5B enterprise deployment (TechCrunch)](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [SAP Business AI Platform (CIO Dive)](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [Microsoft, Google rule AI vendor market (CIO Dive)](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Anthropic + Google + Broadcom compute partnership](https://www.anthropic.com/news/google-broadcom-partnership-compute)
