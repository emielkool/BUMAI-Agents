---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Maand: 2026-04
Periode: 2026-04-01 / 2026-04-30
Status: Afgerond
tags:
  - maandoverzicht
---

# AI Maandoverzicht – april 2026

> Synthese van de weekoverzichten W16, W17 en W18 (13 april – 1 mei 2026).

## 🏆 Maandhighlights

1. **Agentic AI is geen belofte meer – het is standaard product.** April 2026 is de maand waarin multi-agent AI de experimenteerfase definitief verliet. Microsoft rolde Copilot Agent Mode GA uit in Word, Excel, PowerPoint en Outlook – standaard voor elke M365-gebruiker. Google lanceerde op Cloud Next 2026 een compleet agentic platform met Agent Designer, Skills, Inbox en long-running agents. MCP werd overgedragen aan de Agentic AI Foundation (Anthropic, Block, OpenAI) en bereikte 10.000+ publieke servers. De infrastructuurlaag is gezet; de strijd gaat nu over wie de implementatie wint.

2. **Open-weight modellen bereiken frontier-kwaliteit – en DeepSeek V4 herprict de markt.** Google Gemma 4 (Apache 2, #3 wereldwijd), Zhipu GLM-5 (MIT, #1 open gewichtsmodel) en DeepSeek V4 Pro (MIT, 1/20e van de prijs van Claude Opus 4.7 bij vergelijkbare agentic benchmarks) maken definitief een einde aan de exclusiviteit van gesloten API-providers. On-premise en soevereine deployment van topmodellen is realistisch geworden – niet als compromis, maar als serieuze optie voor datakritische klanten. De frontier-labs hebben nog geen antwoord gegeven op DeepSeeks repricing.

3. **EU AI Act: de deadline van 2 augustus werd eerst uitgesteld – en daarna teruggedraaid.** De maand kende een volledige beleidsomkering. Begin april publiceerde de Commissie concrete richtlijnen (definitie AI-systemen). Halverwege de maand lekte het voorstel om de high-risk deadline te verschuiven naar december 2027. Op 28 april mislukte de tweede politieke triloog na twaalf uur onderhandelen. Resultaat: de originele deadline staat weer rechtop. Organisaties die anticipeerden op uitstel hebben geen buffer meer; de volgende triloog is 13 mei.

4. **Security gaat van theoretisch risico naar bewezen aanvalsoppervlak.** Drie security-verhalen domineerden april, elk een stap concreter dan het vorige. Week 16: Anthropic's Mythos vond autonoom duizenden zero-days; prompt injection structureel onoplosbaar verklaard; LangChain/LangGraph CVE's actief. Week 17: MCP-kwetsbaarheid (200.000 instanties, Remote Code Execution by design, Anthropic patcht niet). Week 18: tien concrete in-the-wild indirect prompt injection-payloads gepubliceerd – financiële fraude, API-key-diefstal, bestandsverwijdering. De aanvalsoppervlakte groeit met elke externe databron die een agent leest, en bijna elke agent leest externe data.

5. **De ROI-kloof is het grootste enterprise-vraagstuk van dit moment.** 88% van organisaties gebruikt AI, 97% heeft agents deployed – maar slechts 29% rapporteert significante ROI, 79% ervaart structurele implementatieknelpunten. "Pilot purgatory" is de term waarmee de industrie het benoemt; de bottlenecks zijn data-architectuur, integratie, security en change management. Dit gat is geen tijdelijk verschijnsel – het wordt groter naarmate de verwachtingen stijgen. Het is ook precies het werkterrein van een implementatiepartner.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De dominante beweging van april is de volledige agentificatie van de werkplek en de standaardisering van de onderliggende infrastructuur. MCP als connector-standaard, A2A voor interoperabiliteit tussen agent-platformen, en Microsoft's GA-lancering van agentic Office maken multi-agent architecturen niet langer een architectuurkeuze maar een gegeven. Wie enterprise software levert, levert nu ook agent-infrastructuur.

Parallel comprimeert de open-weight golf de frontier-gap sneller dan verwacht. DeepSeek V4 is de meest structurele verschuiving: frontier-kwaliteit voor 1/20e van de prijs, MIT-licentie, 1M context, trainbaar op Huawei Ascend-chips. Dat laatste heeft geopolitieke implicaties – het toont dat de GPU-afhankelijkheid van westerse AI-labs niet universeel is. Voor de enterprise betekent het dat "welk model?" steeds minder de vraag is; "hoe integreer je het veilig en schaalbaar?" steeds meer.

### 🏛️ Governance & Beleid

April was de meest turbulente beleidsmaand van het jaar. De Digital Omnibus-saga – van verwacht uitstel via politieke mislukking terug naar de harde deadline – legt een structureel probleem bloot: de Europese wetgevingsmachine kan de snelheid van AI-ontwikkeling niet bijhouden. Dat creëert onzekerheid die organisaties verlamt en compliance-trajecten vertraagt.

Wat vaststaat: de transparantie- en GPAI-verplichtingen per 2 augustus zijn juridisch onwrikbaar. Wat fluïde blijft: de high-risk deadline (afhankelijk van de triloog van 13 mei). De strategisch veiligste koers is tweedeling: GPAI/transparantie nu aanpakken, high-risk documentatie opbouwen met flexibele deadline. Nederland heeft tegelijkertijd stevige AI-ambities geëmbargoed (€200M Dutch AI Factory, AI in coalitieakkoord) – een nationale context die enterprise-klanten in de publieke sector actief beïnvloedt.

### 🔐 Security & Risk

April 2026 markeert het punt waarop AI-security van vakspecialisme naar randvoorwaarde voor elk AI-project verschoof. De drie dominante verhalen – Mythos dual-use, MCP-kwetsbaarheid, in-the-wild prompt injection – hebben één gemeenschappelijke kern: de aanvalsoppervlakte is inherent verbonden aan de bruikbaarheid van de agent. Een agent die web leest, e-mail verwerkt en transacties uitvoert, is per definitie kwetsbaar voor de aanvallen die deze maand zijn gedocumenteerd.

De meest zorgwekkende ontwikkeling is structureel: Anthropic erkende de MCP-kwetsbaarheid als "expected behavior" en weigerde te patchen. Daarmee ligt de verantwoordelijkheid volledig bij bouwers en integrators. Wie agentic AI implementeert zonder expliciet threat model is aansprakelijk – zowel juridisch (AI Act) als reputationeel.

### 📈 Markt & Adoptie

De markt laat in april een krachtige bifurcatie zien. Aan de top: explosieve groei (AI-softwarespend $452 miljard +60% YoY, Azure +39%, Google Cloud +50%), hyperscalers die miljarden investeren ($750M Google partnerbudget, $40B Google-Anthropic), en grote consultancyhuizen die agentic AI-bibliotheken bouwen (Deloitte, KPMG, Accenture op Google Cloud Next). Aan de basis: hetzelfde structurele adoptieknelpunt als vorig kwartaal – 79% ervaart implementatieproblemen, slechts 29% ziet ROI.

De verticalisering van AI-agents – Avoca's $1B voor loodgieters – is een signaal dat de ROI-vraag opgelost wordt via domeinspecifieke agents, niet via generieke assistenten. Wie de workflow van één industrie diep begrijpt en bezit, bezit de waarde. Dat is de marktpositie die in 2026 wordt veroverd.

---

## 💼 Ctac-maandperspectief

- **EU AI Act compliance-propositie splitsen in twee tracks en nu uitrollen.** Track 1 (onuitstelbaar): GPAI-transparantievereisten en Art. 50-verplichtingen per 2 augustus – hiervoor is een readiness assessment direct inzetbaar als propositie bij klanten in overheid, zorg en finance. Track 2 (afhankelijk van triloog 13 mei): high-risk AI-documentatie en risicoklassificatie. 78% van enterprises is niet klaar; de klant die in mei begint haalt het; wie in juli begint niet meer.

- **Pilot-naar-productie als kernpropositie verankeren – onderbouwd met marktdata.** De structurele kloof tussen 97% agent-adoptie en 29% ROI is niet te negeren in salesgesprekken. Ctac's waarde zit precies in de bottlenecks: data-architectuur, integratie, security, change management. Gebruik de Writer-, Deloitte- en OutSystems-rapporten van april als externe validatie. Formuleer een concreet "van pilot naar productie in 90 dagen"-aanbod dat die bottlenecks adresseert.

- **Security by design als contractuele baseline in elk agentic project.** De tien gedocumenteerde in-the-wild aanvallen en de MCP-kwetsbaarheid maken het onhoudbaar om agents te implementeren zonder threat model. Minimale eisen per project: inventarisatie van databronnen die de agent leest, expliciete prompt injection-mitigatie, logging en detectiecapaciteit. Dit is zowel intern kwaliteitsargument als extern verkoopargument – en na april ook een juridisch risicobeheersmaatregel.

- **Open-source en soevereine AI als gedifferentieerde propositie voor datakritische klanten.** Gemma 4 (Apache 2), DeepSeek V4 (MIT) en GLM-5 (MIT) maken on-premise deployment van frontier-kwaliteit modellen realistisch. Voor klanten met soevereiniteitsvereisten of budgetvereisten is dit geen compromis meer. Technische kennis van lokale inference-stacks (vLLM, Ollama) gecombineerd met integratieexpertise is een concreet verschilpunt dat hyperscalers niet kunnen bieden.

- **Positie bepalen in het Google Cloud agentic partner-ecosysteem vóór Q3.** Google Cloud Next bracht $750M partnerbudget, Deloitte en KPMG als early movers, en Gemini Enterprise Agent Platform als laagdrempelig startpunt voor agentic implementaties. De vraag is niet óf Ctac Google Cloud-trajecten doet, maar welke specifieke rol Ctac pakt: governance, security, klantintegratie, of verticale domeinkennis. Die positionering bepaalt op welke deals Ctac in de tweede helft van 2026 onderscheidend is.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Google Gemma 4 – blog.google](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
- [GLM-5 open source frontier model – Hugging Face blog](https://huggingface.co/blog/mlabonne/glm-5)
- [Anthropic Mythos Preview – TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [Microsoft drie nieuwe MAI-modellen – TechCrunch](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)
- [MCP overgedragen aan Agentic AI Foundation – Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [Introducing Claude Opus 4.7 – Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
- [Google Cloud Next 2026: AI agents, A2A protocol – The Next Web](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era)
- [DeepSeek V4 arrives at 1/6th the cost of Opus 4.7 – VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- [Microsoft Copilot Agent Mode GA – evermx.com](https://www.evermx.com/case/microsoft-copilot-studio-multi-agent-ga-april-2026)

**Governance & Beleid**
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU Digital Omnibus on AI – European Parliament](https://www.europarl.europa.eu/legislative-train/package-digital-package/file-digital-omnibus-on-ai)
- [EU and Parliament fail to agree on AI Act changes – The Next Web](https://thenextweb.com/news/eu-ai-act-omnibus-deal-fails-april-2026-talks)
- [EU AI Act trilogue stalls — August deadline back in play – resultsense.com](https://www.resultsense.com/news/2026-04-30-eu-ai-act-omnibus-trilogue-stalls)
- [Vision Compliance: 78% van enterprises niet voorbereid – National Law Review](https://natlawreview.com/press-releases/vision-compliance-releases-2026-eu-ai-act-readiness-report-finds-78)
- [AIC4NL vooruitblik 2026](https://aic4nl.nl/en/aic4nl/vooruitblik-2026-intensivering-van-de-uitvoering/)

**Security & Risk**
- [Anthropic Project Glasswing](https://www.anthropic.com/project/glasswing)
- [Anthropic MCP design vulnerability enables RCE – The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)
- [The mother of all AI supply chains – OX Security](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/)
- [Prompt injection: here to stay – VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [Researchers Uncover 10 In-the-Wild Indirect Prompt Injection Attacks – Infosecurity Magazine](https://www.infosecurity-magazine.com/news/researchers-10-wild-indirect/)
- [Three AI coding agents leaked secrets through a single prompt injection – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Schneier: Promptware Kill Chain](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)

**Markt & Adoptie**
- [Enterprise AI adoption curve past internet at year 3 – Asanify](https://asanify.com/blog/news/enterprise-ai-adoption-curve-april-20-2026/)
- [Enterprise AI adoption 2026: why 79% face challenges – Writer](https://writer.com/blog/enterprise-ai-adoption-2026/)
- [Agentic AI Goes Mainstream, but 94% Raise Concern About Sprawl – OutSystems](https://www.outsystems.com/news/enterprise-ai-agent-report-2026/)
- [Deloitte lanceert Google Cloud Agentic Transformation Practice](https://www.deloitte.com/us/en/about/press-room/deloitte-launches-google-cloud-agentic-transformation-practice.html)
- [Google Cloud commits $750M to accelerate partners' agentic AI – PR Newswire](https://www.prnewswire.com/news-releases/google-cloud-commits-750-million-to-accelerate-partners-agentic-ai-development-302749239.html)
- [Avoca AI voice agent for plumbers hits $1B – Asanify](https://asanify.com/blog/news/ai-agents-enterprise-stack-april-28-2026/)
- [Microsoft prepares partners to push Agent 365 bundles – CIO Dive](https://www.ciodive.com/news/microsoft-agentic-ai-365-bundles-frontier-partner-badges/818482/)
- [Enterprise AI-spend 2026 – CIO Dive](https://www.ciodive.com/news/what-to-expect-from-the-ai-boom-this-year/809783/)
