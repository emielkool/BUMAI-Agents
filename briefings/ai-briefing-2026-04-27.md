---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-27
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 27 april 2026

## 🔑 Highlights van de dag

- **DeepSeek V4 gooit de handschoen neer:** Het Chinese lab lanceerde op 24 april V4-Pro (1,6 biljoen parameters, 1M-token context) voor slechts een zevende van de prijs van GPT-5.5 – een serieuze kostendruk op de westerse frontier-markt.
- **Google investeert tot $40 miljard in Anthropic:** Een signaal dat de compute-armen race in een nieuwe fase treedt; niet het model zelf, maar de infrastructuurcapaciteit wordt het strijdtoneel.
- **EU AI Act: deadline over honderd dagen:** Op 2 augustus 2026 worden de handhavingsbevoegdheden voor GPAI-modellen en de volledige verplichtingen voor hoog-risico systemen van kracht. Organisaties zonder compliance-plan lopen reëel risico.
- **Prompt injection: structureel, niet opgelost:** Drie AI-codeeragenten lekten secrets via prompt injection; OpenAI erkent dat het probleem inherent is. Anthropic publiceert nu kwantificeerbare aanvalspercentages voor gebruik in procurement.
- **Nvidia Agent Toolkit live:** Met 17 enterprise-adopters (SAP, Salesforce, Adobe, Siemens) positioneert Nvidia zich als het platform van het agentische tijdperk – een niveau boven de modellaag.

---

## 🧠 Technologie & Modellen

**DeepSeek V4** (24 april) is het opvallendste bericht van het weekend. De Preview bestaat uit twee mixture-of-experts modellen: V4-Pro (1,6T parameters, 1M-token context) en V4-Flash (284B parameters). Op MMLU-Pro en coding-benchmarks presteert V4-Pro vergelijkbaar met GPT-5.4, maar de echte klap zit in de prijs: circa 1/7e van GPT-5.5 en 1/6e van Opus 4.7. De modellen zijn open-source beschikbaar. Openstaande vraag: of de V4-generatie echt frontier-kwaliteit levert of slechts dicht genoeg in de buurt komt voor de meeste enterprise-use-cases – dat maakt praktisch weinig uit voor adoptiebeslissingen.
([TechCrunch](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/) | [VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5))

**Microsoft** lanceerde drie eigen foundation models (spraaktranscriptie, stemgeneratie, beeldcreatie) – bewijs dat het bedrijf minder afhankelijk wil worden van OpenAI. Een strategische beweging die de partner-relatie verder onder druk zet.
([VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google))

---

## 🏛️ Governance & Ethiek

**EU AI Act – countdown begonnen.** Op 2 augustus 2026 treden de handhavingsbevoegdheden van het AI Office voor GPAI-modellen in werking. Tegelijkertijd moeten alle EU-lidstaten vóór die datum minimaal één nationale AI-sandbox hebben ingericht. Standaardisatiewerk (CEN/CENELEC) loopt achter op schema, wat compliance voor high-risk systemen bemoeilijkt.
([EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/) | [Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

**Nederland:** Tien toezichthouders zijn aangewezen voor de handhaving van de AI-verordening (Computable, 22 april). De Autoriteit Persoonsgegevens (AP) en de Rijksinspectie Digitale Infrastructuur (RDI) coördineren. Dit is praktisch nieuws voor Ctac-klanten die high-risk systemen inzetten: het toezicht is nu concreet benoemd.
([Computable](https://www.computable.nl/2026/04/22/tien-toezichthouders-bewaken-naleving-ai-verordening/))

---

## 🔐 Security & Risk

**Prompt injection is een systeem-risico, geen edge case.** Drie AI-codeeragenten lekten secrets via een niet-gehardende GitHub Action (Claude Code Security Review). Gelijktijdig kregen Copilot Studio (CVE-2026-21520, CVSS 7.5) en Salesforce Agentforce een prompt injection-aanval via een publiek leadformulier – zonder authenticatie, zonder volumelimiet op de geëxfiltreerde CRM-data.

Anthropic publiceerde kwantificeerbare aanvalspercentages: indirecte prompt injection via een RAG-architectuur scoort 90% aanvalsucces bij injectie van slechts vijf kwaadaardige teksten in een database van miljoenen documenten. OpenAI stelt expliciet dat prompt injection, net als social engineering op het web, structureel onoplosbaar is.

**Implicatie:** Elke AI-agent die externe data raadpleegt of code uitvoert, is een aanvalsoppervlak. Dit geldt onverkort voor agentische Ctac-implementaties.
([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [VentureBeat – Anthropic metrics](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers))

---

## 📈 Markt & Adoptie

**Google $40 miljard in Anthropic** (24 april): het grootste externe AI-investeringsbedrag tot nu toe, inclusief TPU-compute-capaciteit van 5 gigawatt via Google Cloud tot 2031. Dit bindt Anthropic infrastructureel aan Google – interessant voor de concurrentiepositie van Microsoft/Azure.
([TechCrunch](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/))

**Nvidia Agent Toolkit** (GTC 2026, maart): SAP, Salesforce, Adobe, Siemens en 13 andere enterprise-partijen adopteren het platform. Voor SAP betekent dit agents ingeweven in transactionele ERP-processen; voor Salesforce cross-platform agents via Slack. Nvidia's strategie: eigenaar worden van de platform-laag van het agentische tijdperk.
([VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among))

**Google Agentic Data Cloud** (Google Cloud Next '26): AI-native architectuur die legacy dataplat­formen omzet in redeneer-engines voor enterprise AI-agents – directe concurrent van Microsoft Fabric + Copilot-stack.
([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))

---

## 💡 Ctac-relevantie

**Compliance-urgentie voor klanten:** De EU AI Act-deadline van 2 augustus 2026 is geen abstract risico meer. Met tien aangewezen Nederlandse toezichthouders kunnen klanten in finance, zorg en overheid – allen typische Ctac-doelgroepen – actief worden aangesproken. Ctac kan nu een concreet compliance-scan aanbod formuleren gericht op high-risk systemen en GPAI-gebruik bij klanten.

**Agentische architectuur = security-vraagstuk:** De prompt injection-incidenten bij Copilot Studio en Agentforce onderstrepen dat agentische implementaties een eigen security-laag vereisen. Ctac doet er goed aan dit als standaard onderdeel van elke agentische solutionarchitectuur op te nemen – dit is een differentiator die klanten nu actief zoeken.

**Modelkeuze heroverweging:** DeepSeek V4-Pro biedt frontier-nabije prestaties tegen een fractie van de kosten van GPT-5.5 of Opus 4.7. Voor use-cases waarbij data in de EU blijft (en open-source deployment mogelijk is), wordt dit een serieuze optie naast Azure OpenAI. Het is het moment om een modelkeuze-framework voor klantprojecten op te stellen.

---

## 📚 Bronnen & verder lezen

- [DeepSeek V4 preview – TechCrunch](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/)
- [DeepSeek V4 prijs vs. frontier – VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- [Google $40B in Anthropic – TechCrunch](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act governance & handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Tien NL toezichthouders AI-verordening – Computable](https://www.computable.nl/2026/04/22/tien-toezichthouders-bewaken-naleving-ai-verordening/)
- [Prompt injection AI agents lekken secrets – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Anthropic prompt injection metrics – VentureBeat](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)
- [Microsoft Copilot Studio CVE – VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [Nvidia Agent Toolkit GTC 2026 – VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Microsoft 3 eigen AI modellen – VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
