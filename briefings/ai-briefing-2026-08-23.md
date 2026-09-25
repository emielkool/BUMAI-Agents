---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-23
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 23 augustus 2026

## 🔑 Highlights van de dag

- **OpenAI verlaagt GPT-5.6 Sol-prijs met >20%** voor drie maanden — de prijzenoorlog om enterprise-klanten wordt steeds scherper terwijl OpenAI terrein terugwint op Anthropic bij zakelijke gebruikers.
- **EU AI Act-handhaving is operationeel** (vanaf 2 aug.): transparantie-eisen, deepfake-labels en AI-disclosure voor chatbots zijn nu afdwingbaar; een concrete compliance-deadline voor Ctac en haar klanten.
- **Meta lanceert Muse Glimmer 30B** — een krachtig open-source agentisch model dat volledig lokaal draait op consumenten-hardware; dit verlaagt de drempel voor on-premises AI aanzienlijk.
- **Microsoft patcht critieke Copilot-kwetsbaarheid** (CVE-2026-24301): via één kwaadaardige link konden aanvallers prompts uitvoeren en Gmail/Drive uitlezen — een wake-up call voor enterprise AI-beveiliging.
- **Benelux staat voor AI-talent-paradox**: de regio loopt voorop in AI-adoptie, maar het tekort aan digitale specialisten vormt een rem op verdere opschaling.

---

## 🧠 Technologie & Modellen

**OpenAI – GPT-5.6 Sol prijssverlaging**
Op 21 augustus verlaagde OpenAI de API- en credit-prijs van GPT-5.6 Sol met meer dan 20% voor de komende drie maanden. Sol is de flagship van de 5.6-familie (naast Terra en Luna) en scoort state-of-the-art op coding, kenniswerk en cybersecurity. De prijsverlaging duidt op forse overcapaciteit én op strategische druk om marktaandeel terug te winnen van Anthropic.
[Bron: openai.com/index/gpt-5-6/](https://openai.com/index/gpt-5-6/)

**Meta – Muse Glimmer 30B**
Meta heeft Muse Glimmer gelanceerd: een 30-miljard-parameter open-source model speciaal gebouwd voor autonome agentische taken op lokale hardware. Het integreert multi-step redenering, tool-gebruik, multimodale verwerking en foutherstel in één model — zonder cloud-afhankelijkheid. Dit is een serieuze stap richting volledig lokale AI-agents voor organisaties met data-soevereiniteitseisen.
[Bron: huggingface.co/blog/muse-glimmer](https://huggingface.co/blog/muse-glimmer)

**Open-source ecosysteem groeit sterk**
Het Hugging Face-platform telde inmiddels bijna 3 miljoen publieke modelrepositories (van 2,43M begin 2026). Chinese labs blijven qua modelgrootte de Amerikaanse labs overtreffen — een trend die de geopolitieke dimensie van de AI-race illustreert.
[Bron: huggingface.co/blog/state-of-open-models-summer-2026](https://huggingface.co/blog/state-of-open-models-summer-2026)

---

## 🏛️ Governance & Ethiek

**EU AI Act-handhaving gestart**
Vanaf 2 augustus 2026 is de Europese Commissie (via het AI Office) officieel begonnen met handhaving van de AI Act. Chatbots moeten zich kenbaar maken als AI, deepfakes worden verplicht gelabeld, en AI-gegenereerde content moet machineleesbaar gemarkeerd zijn. De AI Omnibus-aanpassing (in werking 27 juli) verlengt overgangsperiodes voor hoogrisico-systemen, maar de transparantie-eisen gelden nu.
[Bron: digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)

**Benelux AI-talent-schaarste**
Computable rapporteert dat de Benelux koploper is in AI-adoptie, maar dat het tekort aan digitaal talent een structureel knelpunt blijft. In de zorg is de adoptie het hoogst; overheid en industrie volgen versnipperd.
[Bron: computable.nl](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)

---

## 🔐 Security & Risk

**Microsoft patcht CVE-2026-24301 (CoSnitch)**
Varonis Threat Labs ontdekte een kritieke kwetsbaarheid in Microsoft Copilot: een kwaadaardige link combineerde een ongedocumenteerde URL-parameter, Copilots ingebouwde URL-fetch en persistente geheugenvergiftiging om automatisch prompts uit te voeren en verbonden Gmail- en Drive-accounts leeg te trekken. Microsoft patchte op 18 augustus.
[Bron: aiweekly.co/ai-news-today](https://aiweekly.co/ai-news-today)

**Prompt injection: structureel probleem in agentic AI**
VentureBeat documenteert hoe prompt injection nu multi-agent architecturen, RAG-pipelines en model-routers treft. Drie coding agents lekten secrets via een enkele geïnjecteerde prompt. OWASP LLM Top 10 plaatst prompt injection al twee jaar op #1 — het is geen theoretisch risico maar een operationele dreiging bij productie-deployments.
[Bron: venturebeat.com](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)

---

## 📈 Markt & Adoptie

**Enterprise AI-spend bereikt $500 miljard**
De jaarlijkse enterprise cloud-uitgaven zijn gestegen naar $500 miljard, vrijwel volledig aangedreven door AI-buildouts (Synergy Research). Microsoft en Google domineren de markt: Microsoft via zijn partner-ecosysteem, Google via zijn geïntegreerde agent-stack.
[Bron: ciodive.com](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

**OpenAI wint terrein op Anthropic bij zakelijke gebruikers**
Nieuw data (aug. 20) toont dat OpenAI marktaandeel terugwint bij business-gebruikers, mede door de GPT-5.6 prijsverlagingen en brede Copilot-integratie. Anthropic blijft sterk bij ontwikkelaars en API-gebruik.
[Bron: techcrunch.com](https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/)

**AI inference-kosten zullen 5x stijgen t/m 2028**
Naarmate AI-gebruik verschuift van assistieve features naar autonome multi-step agents, zullen inference-kosten meer dan vijfvoudig stijgen. Bijna de helft van de organisaties escaleerde AI-kostenoverschrijdingen al naar de board. Dit is geen toekomstprobleem maar een nu-probleem.
[Bron: ciodive.com](https://www.ciodive.com/news/ai-systems-outpace-cost-savings/828068/)

---

## 💡 Ctac-relevantie

**Compliance direct:** De EU AI Act-transparantie-eisen gelden nu. Ctac moet bij klanten in gesprek over welke AI-systemen disclosure verplicht zijn — met name chatbots en generatieve tools in klantcontact of HR. Dit is een concrete advies- en implementatiegelegenheid.

**Agentic AI + security als combinatie-propositie:** De CoSnitch-kwetsbaarheid en de prompt-injection-epidemie laten zien dat agentic AI een nieuw aanvalsoppervlak creëert dat de meeste security-teams nog niet bewaken. Ctac kan hier slim op inspelen: AI-agent deployment koppelen aan security-review en governance-framework.

**Muse Glimmer voor data-soevereine klanten:** Lokaal draaiende, krachtige agents (Meta Muse Glimmer) zijn nu realistisch voor organisaties die geen data naar de cloud willen sturen — denk aan overheid, zorg en finance. Dit opent on-premises agentic AI als serieuze propositielijn.

**Kostenmanagement als urgent thema:** De verwachte 5x stijging van inference-kosten betekent dat klanten die nu ongecontroleerd AI-agents uitrollen, volgend jaar voor budgetproblemen staan. Ctac kan proactief FinOps-voor-AI als dienst positioneren.

---

## 📚 Bronnen & verder lezen

- [GPT-5.6 Sol — OpenAI](https://openai.com/index/gpt-5-6/)
- [Meta Muse Glimmer 30B — Hugging Face](https://huggingface.co/blog/muse-glimmer)
- [State of Open Models Summer 2026 — Hugging Face](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [EU AI Act handhaving gestart — Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act – artificialintelligenceact.eu](https://artificialintelligenceact.eu/)
- [Benelux AI-talent-schaarste — Computable](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [CVE-2026-24301 CoSnitch — AI Weekly](https://aiweekly.co/ai-news-today)
- [Prompt injection in enterprise AI — VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [AI Security 2026 — Airia](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Microsoft & Google domineren enterprise AI — CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [OpenAI wint marktaandeel zakelijke gebruikers — TechCrunch](https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/)
- [AI inference kosten 5x stijging — CIO Dive](https://www.ciodive.com/news/ai-systems-outpace-cost-savings/828068/)
- [Workday onderzoekt AI agent geheugen — Computable](https://www.computable.nl/2026/08/21/kort-workday-onderzoekt-geheugen-en-samenwerking-van-ai-agents-private-equity-kijkt-verder-dan-it-en-meer/)
