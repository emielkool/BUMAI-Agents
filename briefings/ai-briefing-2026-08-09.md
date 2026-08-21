---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-09
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 9 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act: handhaving live** – Vanaf 2 augustus 2026 handhaaft de Europese Commissie actief de AI Act, inclusief nieuwe transparantie-eisen. AI-systemen moeten zich direct kenbaar maken; deepfakes en gegenereerde content vereisen labels en machine-leesbare markeringen.
- **Agentic AI race tussen OpenAI en Anthropic** – GPT-5.6 Sol en Claude Opus 5 domineren de coding-agent leaderboards (Terminal-Bench 2.1: 89,5% vs. 89,1%). Beide labs hebben parallel-subagent modes uitgebracht; AI werkt nu steeds vaker autonoom op meerdere taken tegelijk.
- **Rabobank investeert €2 miljard in data, IT en AI** – De bank trekt de komende drie jaar fors door op AI-opschaling: meer dan 27.000 medewerkers hebben al geavanceerde AI-trainingen gevolgd. Sterk signaal voor enterprise AI-adoptie in Nederland.
- **Prompt injection: kritieke bedreiging voor AI-agenten** – Drie populaire AI-coding-agents lekten secrets via één prompt injection. Aanvallen op agentic systemen nemen toe nu deze meer tool-access en autonomie krijgen.
- **Open source AI sterk volwassen** – Llama 4 (Meta), Qwen3 (Alibaba) en Gemma 4 (Google) zijn in 2026 serieuze productie-opties, ook voor enterprise. De kloof met closed models krimpt snel.

---

## 🧠 Technologie & Modellen

**Claude Opus 5 en GPT-5.6 Sol** leiden de markt voor agentic AI-systemen. Anthropic lanceerde Claude Opus 5 op 24 juli 2026 als nieuw standaardmodel in Claude Code. GPT-5.6 Sol (OpenAI) biedt een "Ultra mode" waarbij taken parallel worden verdeeld over meerdere subagents. Beide labs convergeren op dezelfde architectuur: multi-tier, recursief agentische pipelines die steeds meer zelfstandig draaien.
([TechCrunch – Anthropic launches Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)) ([OpenAI – GPT-5.6](https://openai.com/index/gpt-5-6/))

**Open source houdt gelijke tred.** Meta's Llama 4 Maverick (~400B parameters, MoE) en Llama 4 Scout (~109B) zijn beschikbaar via Hugging Face en zijn natively multimodaal met een contextvenster van 10 miljoen tokens. Qwen3 van Alibaba en Gemma 4 van Google (Apache 2.0) zijn inmiddels serieuze opties voor lokale of private deployment. Llama-downloads stegen 10x jaar-op-jaar.
([Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)) ([VentureBeat – Meta leads open-source AI boom](https://venturebeat.com/ai/meta-leads-open-source-ai-boom-llama-downloads-surge-10x-year-over-year))

**Nvidia** lanceerde een enterprise AI-agent platform met SAP, Salesforce en Adobe als adopters, wat laat zien dat de traditionele enterprise-softwarestack zich rap heroriënteert op agentic AI.
([VentureBeat – Nvidia launches enterprise AI agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among))

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving gestart per 2 augustus 2026.** De Europese Commissie, het AI Office en nationale toezichthouders zijn gestart met actieve enforcement. Nieuw verplicht:
- Chatbots en interactieve AI moeten gebruikers direct informeren dat ze met AI praten.
- Deepfakes en AI-gegenereerde content moeten gelabeld worden en machine-leesbare markeringen bevatten.
- Providers van general-purpose AI models vallen onder het AI Office; nationale autoriteiten bewaken de rest.

Tegelijk trad de "AI Omnibus" in werking (27 juli 2026): deadlines voor high-risk AI-systemen schuiven op naar 2 december 2027 en voor ingebedde AI-producten naar augustus 2028 – bedrijven krijgen meer tijd, maar de richting is onherroepelijk.
([EC – Commission starts enforcing AI Act](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)) ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/))

In Nederland berichtte NOS over de nieuwe AI-telefonistverplichting: AI-belsystemen moeten zich voortaan direct identificeren als AI. Computable meldde ook een nieuw Europees netwerk (EGDJ) dat AI in de rechtspraak onderzoekt.
([NOS – AI-telefonist moet zich direct prijsgeven](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)) ([Computable – AI in de rechtbank](https://www.computable.nl/2026/08/04/nieuw-europees-netwerk-onderzoekt-ai-in-de-rechtbank/))

---

## 🔐 Security & Risk

**Prompt injection is de dominante aanvalsvector voor agentic AI.** VentureBeat documenteerde een geval waarbij drie populaire AI-coding-agents (waaronder Claude Code, Gemini CLI en Copilot) via één prompt injection tegelijk geheimen lekten. Eerder dit jaar verloor het Moltbook-platform 1,5 miljoen API-tokens door een agent-architectuurfout.

De kern van het probleem: LLM's kunnen niet structureel onderscheid maken tussen instructies en data. Naarmate agents meer tool-access en autonomie krijgen, groeit het aanvalsoppervlak exponentieel. OWASP benoemt prompt injection voor het tweede jaar op rij als #1 LLM-kwetsbaarheid.

Organisaties wordt aangeraden: sandboxing van agent-omgevingen, strikte input-validatie, en evaluatie van vendor system cards vóór adoptie.
([VentureBeat – Three AI coding agents leaked secrets](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)) ([Airia – AI Security in 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

---

## 📈 Markt & Adoptie

**Microsoft en Google domineren enterprise AI.** Gartner plaatst beiden bovenaan voor enterprise AI-adoptie; Microsoft met 20+ miljoen Microsoft 365 Copilot-seats (klanten met >50K seats verviervoudigd y-o-y), Google met een sterke agentic data stack. Microsoft's AI-omzet overstijgt $37 miljard ARR (+123% y-o-y).

**De hyperscalers investeren massaal.** Microsoft, Google en AWS investeren gezamenlijk meer dan $500 miljard in infrastructuur voor AI-deployment in FY2026. Cloud-capex groeit bijna 40% dit jaar.

**Enterprises zitten vast in de pilot-fase.** Twee derde van bedrijven worstelt met de stap van pilot naar productie; verwacht ROI is slechts 27% in de komende 1-2 jaar. AWS ($1 mld) en Microsoft ($2,5 mld Frontier Company) investeren in Forward Deployed Engineering-programma's om klanten concreet te helpen implementeren.

**Anthropic** meldde een run-rate omzet van $30 miljard (van $9 mld eind 2025) en breidt strategisch partnership met Google en Broadcom uit voor extra gigawatts compute.
([CIO Dive – Microsoft, Google rule AI vendor market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)) ([CIO Dive – Enterprises seek help to deploy AI](https://www.ciodive.com/news/enterprises-seek-help-deploy-ai-complexity-mounts/826043/)) ([Anthropic – Google Broadcom partnership](https://www.anthropic.com/news/google-broadcom-partnership-compute))

---

## 💡 Ctac-relevantie

**EU AI Act compliance is nu urgent.** De handhaving is per 2 augustus gestart; de transparantie-eisen gelden direct. Ctac-klanten in gereguleerde sectoren (overheid, financiën, zorg) hebben nú behoefte aan een compliance-check en implementatiebegeleiding. De AI Omnibus geeft iets meer tijd voor high-risk systemen, maar de richting is helder: wie nu niet begint, komt straks in tijdnood.

**Rabobank als benchmark voor enterprise AI-adoptie in NL.** De €2 mrd investering en de 27.000 getrainde medewerkers laten zien dat grote Nederlandse organisaties AI serieus opschalen. Dit creëert een concrete propositiekans voor Ctac: begeleiding bij AI-readiness assessments, opbouw van interne AI-competenties, en rolgebaseerde trainingsprogramma's.

**Agentic AI en security vereisen nieuw aanbod.** De prompt injection-risico's bij agentic systemen zijn geen theoretisch gevaar meer – ze zijn gedocumenteerd bij grote platforms. Ctac kan klanten helpen met risicobeoordelingen van agent-architecturen en sandboxing-strategieën. Dit sluit aan op de groeiende vraag naar begeleid implementeren die AWS en Microsoft nu proactief aanbieden.

**Open source biedt kansen voor private deployments.** Llama 4 en Qwen3 zijn productierijp. Voor klanten met strikte dataprivacy-eisen (overheid, gezondheidszorg) kan Ctac private on-premise of VPC-gebaseerde AI-deployments aanbieden zonder afhankelijkheid van hyperscaler APIs.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Anthropic launches Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [OpenAI – GPT-5.6 announcement](https://openai.com/index/gpt-5-6/)
- [EC – Commission starts enforcing AI Act (2 augustus)](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [artificialintelligenceact.eu – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [VentureBeat – Three AI coding agents leaked secrets via prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Airia – AI Security in 2026: Prompt Injection](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Microsoft, Google rule AI vendor market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – Enterprises seek help to deploy AI](https://www.ciodive.com/news/enterprises-seek-help-deploy-ai-complexity-mounts/826043/)
- [VentureBeat – Nvidia enterprise AI agent platform (SAP, Salesforce, Adobe)](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [VentureBeat – Meta leads open-source AI boom](https://venturebeat.com/ai/meta-leads-open-source-ai-boom-llama-downloads-surge-10x-year-over-year)
- [Computable – Rabobank investeert miljarden in IT](https://www.computable.nl/2026/08/05/rabobank-investeert-miljarden-in-it/)
- [NOS – AI-telefonist moet zich direct prijsgeven](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)
- [Computable – AI in de rechtbank](https://www.computable.nl/2026/08/04/nieuw-europees-netwerk-onderzoekt-ai-in-de-rechtbank/)
- [Anthropic – Google & Broadcom partnership compute](https://www.anthropic.com/news/google-broadcom-partnership-compute)
