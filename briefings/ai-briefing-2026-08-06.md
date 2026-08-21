---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-06
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 6 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaving live (2 aug):** Vier dagen geleden startte de Europese Commissie officieel met handhaving van de AI Act. Chatbots moeten zichzelf kenbaar maken, deepfakes moeten gelabeld worden en AI-gegenereerde content krijgt verplicht een machine-leesbare markering. In Nederland is de AP de toezichthouder.
- **Prompt injection bereikt nieuw niveau:** Een gecoördineerde aanval trof Claude Code, Gemini CLI en Microsoft Copilot gelijktijdig. Onderzoek toont aan dat 94,4% van alle state-of-the-art LLM-agents kwetsbaar is — dit is geen niche-risico meer maar een structureel productieprobleem.
- **Enterprise AI zit vast in pilots:** Gemiddeld geeft een Amerikaans bedrijf $37,2 miljoen uit aan AI maar haalt slechts $9,9 miljoen ROI terug. Tweederde zit gevangen in de pilotfase; slechts 5–20% van pilots leidt tot enterprise-brede uitrol.
- **Agentic AI rijpt: MCP naar Linux Foundation:** Anthropic's Model Context Protocol is overgedragen aan de nieuwe Agentic AI Foundation van de Linux Foundation. Standaardisatie van agentic tooling versnelt — relevant voor wie nu een agent-platform bouwt.
- **Hyperscalers verdubbelen inzet:** Microsoft, Google en AWS plannen samen meer dan $500 miljard aan capex in FY2026. Microsoft lanceert het Frontier Company-programma met 6.000 engineers specifiek voor enterprise AI-implementaties.

## 🧠 Technologie & Modellen

**Modelraces blijft versnellen.** In de afgelopen weken lanceerden alle drie de grote labs nieuwe varianten: Google's Gemini 3.6 Flash belooft 17% minder tokengebruik bij gelijkwaardige prestaties; OpenAI's GPT-5.6 komt in drie smaken (Sol/Terra/Luna) met Sol 54% efficiënter op coderingstaken; Anthropic's Claude Sonnet 5 scoort significant beter op agentic benchmarks. De modellen worden goedkoper en sneller — de differentiatie verschuift naar infrastructuur en toepassing.

**Agentic benchmarks naderen plafond.** SWE-bench (software issues oplossen) nadert de 100%; WebArena (web-navigatietaken) staat op 74,3% en MLE-bench op 65%. De technische capaciteiten zijn er; de uitdaging zit nu in betrouwbare runtime-omgevingen.

**MCP als infrastructuurstandaard.** De overdracht van Anthropic's Model Context Protocol aan de Linux Foundation's Agentic AI Foundation is een strategisch signaal: het protocol wordt de defacto-standaard voor hoe agents met externe tools communiceren. Wie nu agentic systemen bouwt, doet er verstandig aan MCP als basis te nemen.

Bronnen: [TechCrunch – OpenAI GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/) | [TechCrunch – Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/) | [TechCrunch – Gemini 3.6](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/) | [HuggingFace – Open Source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving is gestart.** Vanaf 2 augustus 2026 is de AI Act afdwingbaar. De meest directe verplichtingen:

- Chatbots en interactieve AI-systemen moeten gebruikers informeren dat ze met AI communiceren.
- Deepfakes en AI-gegenereerde content moeten machine-leesbaar gelabeld zijn.
- Providers én deployers dragen juridische verantwoordelijkheid — ook bedrijven die alleen een AI-product van een derde partij inzetten.

In Nederland houdt de Autoriteit Persoonsgegevens (AP) toezicht. De zwaarste verplichtingen (hoog-risico AI-systemen) volgen pas per december 2027, maar de transparantieregels gelden nu.

**AI in de rechtspraak.** Onderzoekers van de Rijksuniversiteit Groningen richtten de Europese Groep voor de Digitalisering van Justitie (EGDJ) op om AI-gebruik in rechtbanken te onderzoeken. Tijdswinst is potentieel groot, maar de risico's voor rechtsstatelijke waarborgen zijn dat ook.

Bronnen: [Europese Commissie – handhavingsstart](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [Computable – AI Act uitleg](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/) | [Computable – AI in rechtbank](https://www.computable.nl/2026/08/04/nieuw-europees-netwerk-onderzoekt-ai-in-de-rechtbank/) | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/)

## 🔐 Security & Risk

**Prompt injection is nu een serieus productierisico.** Een gecoördineerde aanval trof Claude Code, Gemini CLI en Microsoft Copilot Studio gelijktijdig — drie AI coding agents lekten secrets via één enkele injectie. Microsoft heeft CVE-2026-21520 (CVSS 7.5) gepatcht, maar data was al geëxfiltreerd.

Onderzoek laat zien dat 94,4% van LLM-agents kwetsbaar is voor prompt injection, 83,3% voor retrieval-based backdoors en 100% voor interagent trust exploits. Het UK NCSC waarschuwt dat prompt injection ernstiger kan zijn dan SQL-injectie. OpenAI erkent dat het probleem waarschijnlijk nooit volledig oplosbaar is.

**Frontier models falen in productie.** Eén op de drie productie-uitvoeringen van frontier models mislukt, terwijl de systemen ook moeilijker te auditen zijn dan eerder. Dit benadrukt dat runtime-beveiliging minstens even urgent is als modelkwaliteit.

Bronnen: [VentureBeat – prompt injection agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [VentureBeat – Copilot Studio CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook) | [VentureBeat – frontier models falen](https://venturebeat.com/security/frontier-models-are-failing-one-in-three-production-attempts-and-getting-harder-to-audit) | [Computable – AI security](https://www.computable.nl/2026/08/04/hoe-houd-je-ai-security-onder-controle/)

## 📈 Markt & Adoptie

**De ROI-kloof blijft groot.** Gemiddelde AI-uitgaven bij een Amerikaans bedrijf: $37,2 miljoen. Gemiddelde ROI: $9,9 miljoen. Slechts 5–20% van AI-pilots bereikt enterprise-brede uitrol. Twee derde zit gevangen in de pilotfase; 97% van bedrijven heeft moeite de waarde aan te tonen.

De oorzaken zijn structureel: gebrek aan data-kwaliteit, skills, governance en een duidelijke strategie. Slechts 14% van enterprises heeft een heldere AI-strategie met meetbare doelen.

**Hyperscalers investeren massaal in implementatiehulp.** Microsoft lanceert het Frontier Company-programma (6.000 engineers voor klantimplementaties). AWS investeert $1 miljard in een Forward Deployed Engineering-hub. De boodschap: het model alleen is niet genoeg — begeleide implementatie is de kritieke factor.

**Multicloud als standaard.** Google en AWS lanceerden een samenwerking voor multicloud-connectiviteit; Microsoft Azure sluit zich later in 2026 aan. Enterprise AI draait straks over meerdere clouds tegelijk.

Bronnen: [CIO Dive – Microsoft & Google domineren](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [CIO Dive – AWS FDE hub](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/) | [CIO Dive – ROI](https://www.ciodive.com/news/enterprise-roi-value-savings/825234/) | [VentureBeat – agentic rebuild era](https://venturebeat.com/orchestration/ai-agents-are-entering-their-rebuild-era-as-enterprises-confront-the-reliability-problem)

## 💡 Ctac-relevantie

**EU AI Act compliance wordt een urgente klantvraag.** Nu handhaving is gestart, willen Ctac's klanten — met name in overheid, finance en zorg — weten of zij compliant zijn. Een concrete kans: een AI Act quick-scan aanbieden die transparantieverplichtingen en inventarisatie van AI-systemen dekt. Dit kan ook als instappunt voor bredere AI-governance begeleiding dienen.

**De enterprise deployment gap is Ctac's markt.** De ROI-kloof en de hoge pilotfaal-rate tonen aan dat bedrijven begeleiding nodig hebben bij het doorvertalen van AI van pilot naar productie. Ctac kan hier als implementatiepartner positioneren — niet als modelverkoper maar als degene die helpt AI structureel in werkprocessen te verankeren, inclusief datastrategie, change management en governance.

**Prompt injection vereist actie in eigen tooling.** Ctac gebruikt zelf AI coding agents (en klanten steeds meer ook). De bevindingen van deze week — 94% kwetsbaar, aanvallen op meerdere platforms tegelijk — betekenen dat een baseline security-beleid voor intern AI-gebruik geen luxe meer is. Denk aan sandboxing van agents, input-validatierichtlijnen en bewustzijnstraining voor developers.

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI GPT-5.6 lancering](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [TechCrunch – Claude Sonnet 5 voor agents](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [TechCrunch – Google Gemini 3.6](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)
- [Europese Commissie – AI Act handhaving 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act tracker – transparantieregels](https://artificialintelligenceact.eu/transparency-rules-article-50/)
- [Computable – Wat je moet weten van de AI Act](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [Computable – AI in de rechtbank](https://www.computable.nl/2026/08/04/nieuw-europees-netwerk-onderzoekt-ai-in-de-rechtbank/)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – Copilot Studio CVE prompt injection](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [VentureBeat – Agentic rebuild era](https://venturebeat.com/orchestration/ai-agents-are-entering-their-rebuild-era-as-enterprises-confront-the-reliability-problem)
- [CIO Dive – Microsoft & Google enterprise AI markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – AWS Forward Deployed Engineering](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)
- [CIO Dive – Enterprise ROI stijgt](https://www.ciodive.com/news/enterprise-roi-value-savings/825234/)
- [HuggingFace – Open Source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
