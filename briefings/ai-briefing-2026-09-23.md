---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-23
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 23 september 2026

## 🔑 Highlights van de dag

- **OpenAI lanceerde gisteren GPT-6 Sol en Luna**: twee "mini-Astra's" die 50% goedkoper zijn dan hun 5.6-voorgangers en tot de helft minder fouten maken. Sol kost $2/$10 per miljoen tokens; een directe prijsdruk op het hele enterprise-segment.
- **Anthropic bracht Claude Opus 5.5 uit**: Fable-niveau prestaties voor 40% minder kosten dan Opus 5. Staat nu bovenaan agentic-coding-benchmarks – en kost minder dan GPT-4o kostte een jaar geleden.
- **EU AI Act volledig in werking**: per 2 augustus handhaaft het AI Office actief GPAI-modellen, verboden praktijken en transparantieverplichtingen. Klanten in gereguleerde sectoren zijn nu aansprakelijk als ze niet compliant zijn.
- **Prompt injection stijgt 340% jaar-op-jaar** en produceerde een CVSS 9.6-exploit in GitHub Copilot. Elke organisatie die AI-assistenten inzet in development of ops moet dit als productierisico behandelen.
- **Microsoft richtte Frontier Company op** ($2,5 miljard, 6.000 experts) voor enterprise AI-deployments – en concurreert nu openlijk met zijn eigen partner OpenAI.

## 🧠 Technologie & Modellen

**OpenAI – GPT-6 Sol & Luna (22 sept)**
OpenAI breidde de GPT-6-familie uit met Sol (gericht op dagelijks professioneel werk) en Luna (hoog-volume, snelle respons). Sol is 50% goedkoper dan GPT-5.6 Sol ($2/$10 per M tokens) en maakt "ruim twee keer minder fouten" op OpenAI's eigen benchmarks. Luna is nog goedkoper ($0,10/$0,50) voor bulk-inferentie. Dit zijn geen theoretische verbeteringen: de modellen zijn direct beschikbaar in de API en via GitHub Copilot.
Bron: [TechCrunch](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/) | [OpenAI](https://openai.com/index/gpt-6-astra/)

**Anthropic – Claude Opus 5.5 (22 sept)**
Opus 5.5 biedt Fable-niveau prestaties voor $4/$20 per M tokens – een verlaging van 20% ten opzichte van Opus 5, met cache-read kosten die dalen van $0,50 naar $0,20. VentureBeat meldt dat het model Fable 5.1 overtreft op key agentic benchmarks. Sonnet 5.5 en Haiku 5.5 volgen "in de komende weken". De snelheid van iteratie (Opus 5 verscheen pas twee maanden geleden) illustreert dat de modellencyclus drastisch is versneld.
Bron: [Anthropic](https://www.anthropic.com/claude-opus-5-5) | [VentureBeat](https://venturebeat.com/technology/anthropic-releases-claude-opus-5-5-beating-fable-5-1-on-key-agentic-benchmarks-at-60-cheaper-api-price) | [TechCrunch](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/)

**Open source: Kimi K3 als mijlpaal**
Moonshot AI's Kimi K3 (2,8 biljoen parameters, uitgebracht 16 juli) is het eerste open-weight model in de 3B-parameterklasse. In combinatie met de groei van Hugging Face naar 3 miljoen+ publieke modelrepositories toont dit dat open-source serieus concurreert voor coding, reasoning en agentic workflows. Gesloten modellen hebben geen vanzelfsprekend voordeel meer.
Bron: [Hugging Face Blog](https://huggingface.co/blog/state-of-open-models-summer-2026)

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving nu volledig actief**
Per 2 augustus 2026 handhaaft het AI Office de regels voor general-purpose AI-modellen (GPAI). Verboden praktijken zijn afdwingbaar; transparantievereisten gelden nu (chatbots moeten zich identificeren als AI, deepfakes moeten worden gelabeld). Volgende deadline: 2 december 2026 voor regels over non-consensuele intieme beelden en CSAM.
Bron: [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [AI Act Tracker](https://artificialintelligenceact.eu/implementation-timeline/)

**Nederland: decentraal toezichtmodel in consultatie**
De Nederlandse overheid publiceerde in april 2026 een conceptimplementatiewet die het toezicht verdeelt over acht sectorale autoriteiten (AP en RDI als coördinatoren). De aanpak is bewust minimalistisch – geen extra vereisten bovenop de AI Act zelf. Het meeste GPAI-regime (high-risk systemen, transparantie) geldt nu.
Bron: [Bird & Bird](https://www.twobirds.com/en/insights/2026/netherlands/dutch-government-publishes-draft-ai-act-implementing-legislation) | [Loyens & Loeff](https://www.loyensloeff.com/insights/news--events/news/dutch-implementation-of-the-ai-act-decentralised-ai-supervision/)

## 🔐 Security & Risk

**Prompt injection: #1 AI-bedreiging met 340% groei**
OWASP bevestigt prompt injection als toprisico voor LLM-toepassingen in 2026. De meest zorgwekkende recente casus: CVE-2025-53773 toont aan dat kwaadaardige inhoud in pull request-beschrijvingen remote code execution kan veroorzaken via GitHub Copilot (CVSS 9.6). De Five Eyes (CISA, NSA + equivalenten in UK, CA, AU, NZ) gaven in mei 2026 gezamenlijke richtlijnen voor agentische AI. Huidige verdedigingen zijn onvoldoende: adaptieve aanvallen omzeilen vrijwel elke gepubliceerde mitigatie.
Bron: [Help Net Security](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) | [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/)

## 📈 Markt & Adoptie

**Microsoft: van partner naar concurrent**
Microsoft lanceerde Microsoft Frontier Company met $2,5 miljard en 6.000 experts voor enterprise AI-deployments, verkoopt zijn eigen MAI-modellen op eigen Maia-chips en biedt 11.000+ modellen aan via Azure. De openlijke concurrentie met OpenAI en Anthropic is nu bevestigd. Intern rapport toont dat supply chain-cycli daalden van 10 naar 2,5 werkdagen door AI-inzet.
Bron: [TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) | [VentureBeat](https://venturebeat.com/technology/microsoft-releases-new-ai-playbook-for-enterprises/)

**Agentic software development: groei vs. ROI-kloof**
Investering in agentic software development groeit 12x van 2025 naar 2026, maar slechts 25% van bedrijven rapporteert betekenisvolle versnelling. Enterprises overschrijden hun AI-budgetten. Marktaandeel enterprise: Anthropic 44%, OpenAI 40% bij US-zakelijke gebruikers.
Bron: [CIO Dive](https://www.ciodive.com/news/enterprises-bet-coding-agents-despite-ROI/830943/) | [TechCrunch](https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/)

## 💡 Ctac-relevantie

De simultane prijsverlaging van OpenAI (GPT-6 Sol/Luna –50%) en Anthropic (Opus 5.5 –40%) is strategisch voor Ctac: geavanceerde AI-inzet in klantprojecten is nu aanzienlijk goedkoper te verantwoorden in business cases. Dit verlaagt de drempel voor klanten in overheid, zorg en finance die vanwege kosten afwachtten.

De EU AI Act is actief afdwingbaar – geen theorie meer. Ctac kan klanten in gereguleerde sectoren direct helpen met compliance-assessments op GPAI-gebruik, transparantievereisten en het aankomende CSAM/intimiteitsregime (december 2026). Dit is een concrete propositie die dit kwartaal geleverd kan worden.

Het prompt injection-risico (CVSS 9.6 via Copilot) maakt een security-review van alle lopende AI-assisted development trajecten urgent. Als Ctac coding agents inzet bij klanten, moet dit op de agenda van de volgende technische review.

Microsoft Frontier Company is een nieuwe concurrent voor IT-consultancybedrijven die enterprise AI-deployments faciliteren. Het is tegelijk een marktsignaal dat de implementatiefase de volgende grote waardecreatie-mogelijkheid is – precies het domein waar Ctac's expertise relevant is.

## 📚 Bronnen & verder lezen

- [OpenAI – GPT-6 Sol en Luna lancering (TechCrunch)](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/)
- [OpenAI – GPT-6 Astra product page](https://openai.com/index/gpt-6-astra/)
- [Anthropic – Claude Opus 5.5 aankondiging](https://www.anthropic.com/claude-opus-5-5)
- [VentureBeat – Opus 5.5 benchmark analyse](https://venturebeat.com/technology/anthropic-releases-claude-opus-5-5-beating-fable-5-1-on-key-agentic-benchmarks-at-60-cheaper-api-price)
- [TechCrunch – Opus 5.5 release](https://techcrunch.com/2026/09/22/anthropic-releases-opus-5-5-with-lower-prices-and-fable-level-performance/)
- [Hugging Face – State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [EC Digital Strategy – AI Act handhaving per 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act Tracker – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Bird & Bird – Nederlandse AI Act implementatiewet](https://www.twobirds.com/en/insights/2026/netherlands/dutch-government-publishes-draft-ai-act-implementing-legislation)
- [Help Net Security – OWASP prompt injection rapport](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [Infosecurity Magazine – Prompt injection onopgelost](https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/)
- [TechCrunch – Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [CIO Dive – Enterprise coding agents ROI-kloof](https://www.ciodive.com/news/enterprises-bet-coding-agents-despite-ROI/830943/)
