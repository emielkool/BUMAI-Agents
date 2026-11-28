---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-26
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 26 november 2026

## 🔑 Highlights van de dag

- **Modellengolf november:** GPT-6.2 (OpenAI, 17 nov), Gemini 4 Neon (Google, 18 nov) en Claude Fable 5.2 (Anthropic, 9 nov) markeren een van de drukste modelmaanden ooit – dertien labs lanceerden ruim 22 nieuwe modellen in november.
- **AI-autonomiedebat escaleert:** Dario Amodei (Anthropic) moest publiekelijk tegengas geven aan berichten dat Anthropic menselijke controle wil overdragen aan AI; Sam Altman en Mark Zuckerberg schaarden zich aan de andere kant. Groter strategisch debat over de grenzen van autonome systemen.
- **Supply-chain aanval op Microsoft-agent library:** Twee getrojaniseerde versies van het populaire Microsoft agent-framework voor Python verschenen op PyPI (17 nov), gericht op Azure- en CI/CD-credentials – een directe aanval op de AI-ontwikkelketen.
- **EU AI Act: deadline 2 december nadert:** Twee nieuwe verboden treden in werking en de markeerplicht voor generatieve AI-uitvoer gaat in. Nederlandse en Belgische organisaties moeten voor 2 december actie ondernemen.
- **Google Cloud overtreft concurrentie:** Q3-2026 groei van 103% voor Google Cloud, deels aangedreven door als enige hyperscaler toegang te bieden tot alle drie frontier-modellfamilies (Google, Anthropic én OpenAI).

---

## 🧠 Technologie & Modellen

November 2026 bewijst zich als een exceptionele modelmaand. De meest opvallende releases:

- **GPT-6.2 Astra & Sol** (OpenAI, 17 nov): twee algemene modellen, waarbij Astra is gepositioneerd als redeneermodel en Sol als snel antwoordmodel. OpenAI had eerder al GPT-6 Cyber uitgebracht (5 nov), exclusief voor security-onderzoekers.
- **Gemini 4 Neon** (Google, 18 nov): de derde release in de Gemini 4-lijn (Carbon en Hydrogen gingen eerder in november). Google bevestigt het in context van zijn cloud-strategie.
- **Claude Fable 5.2** (Anthropic, 9 nov): positioneert zich boven Opus 5.5 als Anthropic's voorlopig krachtigste model.

De agentic revolutie zet door: productiegebruik van autonome AI-workflows neemt snel toe. Het Model Context Protocol (MCP) voor toolintegratie en Agent-to-Agent (A2A) voor inter-agent communicatie zijn inmiddels standaard geworden in het ecosysteem. Amazon Bedrock AgentCore biedt nu native ondersteuning voor multimodale, multi-agent workflows.

**Beoordeling:** de hoeveelheid releases is groot, maar het daadwerkelijke verschil in kwaliteit tussen modellen vlakt af – de concurrentie verschuift naar infrastructuur, kostprijs per token en ecosysteemintegratie.

Bronnen: [tecadmin.net](https://tecadmin.net/november-2026-ai-model-releases/), [capitalandcompute.net](https://capitalandcompute.net/blog/new-ai-models-november-2026/), [llmgateway.io](https://llmgateway.io/timeline)

---

## 🏛️ Governance & Ethiek

**EU AI Act – 2 december deadline:** Per 2 december 2026 treden twee nieuwe verboden in werking (rond niet-consensuele intieme beelden en CSAM), en eindigt de overgangsperiode voor generatieve AI-markering. Organisaties die generatieve content produceren moeten machine-leesbare markering aanbieden. Dit geldt onverkort voor NL/BE.

De Europese Commissie verzocht op 16 november om feedback op een concepttemplate voor grondrechtimpactbeoordelingen (artikel 27), gericht aan deployers van hoog-risico systemen. Dit is de volgende stap in de operationalisering van de AI Act, na de inwerkingtreding van de Digital Omnibus (Reg. 2026/1744) in juli die de hoofddeadlines voor hoog-risico systemen verschoof naar december 2027.

Onbevestigd: één bron meldt een Commissievoorstel (16 nov) voor regulering van autonome AI-agenten; verificatie via EUR-Lex wordt aanbevolen.

**Het AI-autonomiedebat** heeft een nieuwe fase bereikt: media-aandacht voor de grens tussen AI als assistent vs. AI als beslisser is een indicator dat de governance-discussie ook publiek wordt.

Bronnen: [blog.mean.ceo](https://blog.mean.ceo/eu-ai-act-news-november-2026/), [beyondhorizons.sg roundup](https://www.insights.beyondhorizons.sg/p/ai-law-regulation-roundup-november-2026), [euaiact.com](https://www.euaiact.com/)

---

## 🔐 Security & Risk

November 2026 laat een zorgwekkende concentratie van AI-gerelateerde incidenten zien:

- **ARTEX (FBI-waarschuwing, 13 nov):** Open-source framework waarmee aanvallers AI-agents inzetten voor geautomatiseerde, multi-fase cyberaanvallen. Een China-gelinkte groep misbruikte dit al om 200+ organisaties in 11 dagen aan te vallen.
- **LiteLLM CVE-2026-40217:** CISA plaatste deze kwetsbaarheid in de AI-gateway op de Known Exploited Vulnerabilities-lijst (18 nov), federale agencies moeten voor 2 december patchen.
- **PyPI supply chain (17 nov):** Twee besmette versies van een Microsoft agent-framework library. Direct risico voor teams die AI-agenten bouwen op Python; controleer afhankelijkheden.
- **Copilot RCE (CVE-2026-103572):** Via een trailing-dot bestandsnaamtruc kon Copilot in Visual Studio en SSMS schrijven naar eigen MCP- en settings-bestanden, resulterend in code-executie.
- **Amazon Bedrock AgentCore:** Eén prompt op een publiek toegankelijke agent kon metadata-credentials ophalen en andere agents in hetzelfde account overnemen.

**Patroon:** de AI-stack (agents, model-serving, MCP-integraties, Python libraries) wordt een aantrekkelijk aanvalsdoel. Supply-chain security voor AI-tooling verdient directe aandacht.

Bronnen: [adversa.ai agent security](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/), [adversa.ai GenAI security](https://adversa.ai/blog/top-genai-security-resources-november-2026/), [adversa.ai coding agents](https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/), [btigroup.com](https://www.btigroup.com/post/ai-cybersecurity-update-november-20-2026/)

---

## 📈 Markt & Adoptie

- **Google Cloud overtreft:** Q3-groei van ~103% naar $30,7 mrd omzet; als enige hyperscaler biedt Google Cloud nu toegang tot Google-, Anthropic- én OpenAI-modellen – een sterk enterprise-argument.
- **Microsoft vs. Google:** Microsoft's voordeel zit in Azure als databedrijf ("de modellen naar de data"); Google's voordeel in brede modelkeuze. 87% van enterprises hanteert al een multi-cloud-strategie.
- **Capital supercycle (GlobeNewswire, 25 nov):** Rapporten signaleren massale infrastructuurinvesteringen voor agentic AI. De verschuiving is van model-experimentatie naar productie-infrastructuur.
- **Adoptiewijze verschuift:** Enterprises bewegen van cloud-gebaseerde deployments en volledige SaaS-afhankelijkheid naar hybride setups met eigen model-hosting voor privacy-gevoelige workloads.

Bronnen: [ciodive.com](https://www.ciodive.com/news/Microsoft-Google-booming-AI/873258/), [cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-is-a-leader-in-the-2026-gartner-magic-quadrant), [globenewswire.com](https://www.globenewswire.com/news-release/2026/11/25/3410268/0/en/ai-industry-enters-capital-supercycle-as-agentic-systems-and-infrastructure-investment-redefine-enterprise-adoption.html)

---

## 💡 Ctac-relevantie

**2 december deadline – direct actie:** Als Ctac generatieve AI-tools inzet in klantprojecten of eigen producten, moeten output-markeringen vóór 2 december 2026 zijn geïmplementeerd. Dit is geen optie maar verplichting. De grondrechtimpactbeoordeling (artikel 27) voor hoog-risico deployers is nu in consultatie – goed moment om de eigen dienstverlening te toetsen of klanten proactief te adviseren.

**AI-agenten als risico én kans:** De PyPI supply chain-aanval en het Bedrock AgentCore-incident zijn concrete signalen dat elk klantproject met AI-agents een expliciete security-review nodig heeft. Tegelijk is agentic AI de propositiekans voor 2027: Ctac kan zich onderscheiden door veilig ontworpen agent-architecturen aan te bieden, inclusief credential-isolatie en MCP-sandboxing.

**Modelkeuze voor klantprojecten:** De beschikbaarheid van GPT-6.2, Fable 5.2 en Gemini 4 via Google Cloud (als multi-model platform) verandert het advies bij klanten: je hoeft niet meer platform-loyaal te zijn. Ctac kan als onafhankelijk adviseur optreden voor model-selectie op basis van use case, kosten en compliance.

---

## 📚 Bronnen & verder lezen

- [November 2026 AI model releases – tecadmin.net](https://tecadmin.net/november-2026-ai-model-releases/)
- [LLM timeline november 2026 – llmgateway.io](https://llmgateway.io/timeline)
- [AI autonomy debate – Newsweek/Cryptopolitan](https://www.cryptopolitan.com/openai-meta-push-back-anthropic-vision/)
- [EU AI Act Digital Omnibus 2026 – euaiact.com](https://www.euaiact.com/)
- [AI law roundup november 2026 – beyondhorizons.sg](https://www.insights.beyondhorizons.sg/p/ai-law-regulation-roundup-november-2026)
- [GenAI security november 2026 – adversa.ai](https://adversa.ai/blog/top-genai-security-resources-november-2026/)
- [AI agent security november 2026 – adversa.ai](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/)
- [Microsoft/Google AI revenue – ciodive.com](https://www.ciodive.com/news/Microsoft-Google-booming-AI/873258/)
- [Capital supercycle AI – globenewswire.com](https://www.globenewswire.com/news-release/2026/11/25/3410268/0/en/ai-industry-enters-capital-supercycle-as-agentic-systems-and-infrastructure-investment-redefine-enterprise-adoption.html)
- [Google Cloud Gartner Magic Quadrant 2026](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-is-a-leader-in-the-2026-gartner-magic-quadrant)
