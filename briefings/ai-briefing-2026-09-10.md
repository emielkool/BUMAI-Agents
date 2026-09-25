---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-10
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 10 september 2026

## 🔑 Highlights van de dag

- **Dichtstste modelweek ooit:** OpenAI (GPT-6 Astra), Anthropic (Claude Fable 5.1 + Mythos 5.1), Google (Gemini 3.8 Flash) en Meta (Muse Spark 1.3) lanceerden allemaal nieuwe frontiermodellen in dezelfde 72 uur (1–3 sept). De "model fatigue"-discussie barst los.
- **EU AI Act volledig van kracht:** Per 2 augustus 2026 zijn de meeste verplichtingen van toepassing, inclusief Article 50 transparantievereisten. Deadline van 15 september: GPAI-aanbieders boven 10²⁵ FLOPs moeten hun eerste systeemrisico-evaluaties indienen bij het Europees AI-kantoor.
- **Kritieke Azure OpenAI-kwetsbaarheid:** CVE-2026-45499 (SSRF-flaw) maakt zijwaartse beweging door aanvallers in enterprise AI-omgevingen mogelijk. Directe aandacht vereist voor organisaties die Azure OpenAI inzetten.
- **Convergentie enterprise agentplatforms:** Microsoft (Foundry), Google (Gemini Enterprise Agent Platform) en Amazon (Bedrock AgentCore) zijn architectureel naar hetzelfde patroon geconvergeerd: runtime, memory, tool gateway, identity en observability als standaardbouwblokken.
- **78% van de CISOs ziet AI als beveiligingsrisico:** Proofpoint-rapport van vandaag bevestigt dat AI-governance structureel achterblijft bij adoptie — GenAI creëert nieuwe dataverliesrisico's die bestaande beveiligingsprocessen niet aankunnen.

---

## 🧠 Technologie & Modellen

De eerste week van september was uitzonderlijk actief. **Anthropic** lanceerde Claude Fable 5.1 en het nieuwe Claude Mythos 5.1 op 1 september, met een prijsverlaging van 75% op cache-reads. **Google DeepMind** volgde met Gemini 3.8 Flash (inclusief een Cyber-variant exclusief voor verdedigers). **Meta** bracht Muse Spark 1.3 uit voor circa $0,10 per miljoen tokens. **OpenAI** sloot de sprint af op 3 september met GPT-6 Astra (1,05M context, 128K output, $10/$1 cached per 1M tokens).

In de open-source wereld domineert **Qwen** met 151.000 afgeleide modellen op Hugging Face — 2,6× het voetafdruk van Meta's Llama-familie. Kimi K2.6 (1,1T parameters, Modified MIT) en Coheres North Mini Code zijn de meest opvallende recente releases voor developer-toepassingen.

**GitHub Copilot Workspace** introduceert multi-agent samenwerking: aparte agents voor implementatie, testen en documentatie werken gelijktijdig via een gedeeld contextvenster.

*Bronnen: [LLM Stats](https://llm-stats.com/ai-news) | [CNBC – model fatigue](https://www.cnbc.com/2026/09/06/meta-google-openai-anthropic-ai-model-fatigue.html) | [Hugging Face blog](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)*

---

## 🏛️ Governance & Ethiek

De EU AI Act is per **2 augustus 2026** grotendeels van kracht. Handhavingsbevoegdheden liggen nu bij het Europese AI-kantoor en nationale autoriteiten. Kritieke datum komende zondag: **15 september 2026** is de deadline waarop aanbieders van GPAI-modellen die de 10²⁵ FLOPs-trainingsdrempel overschrijden hun eerste formele systeemrisico-evaluaties moeten indienen.

De **AI Omnibus** (inwerking getreden 27 juli 2026) heeft bepaalde implementatietijdlijnen verlengd en de nalevingslast voor kleine aanbieders teruggebracht — positief voor MKB-adoptie, maar ook een signaal dat de wetgever de tempo's van de industrie niet bijhoudt.

*Bronnen: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) | [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | [AnnexOps – EU AI Act 2026](https://annexops.com/eu-ai-act-implementation-2026/)*

---

## 🔐 Security & Risk

Twee concrete dreigingen verdienen directe opvolging:

1. **CVE-2026-45499** — Kritieke SSRF-kwetsbaarheid in Azure OpenAI die zijwaartse beweging mogelijk maakt voor aanvallers met beperkte initiële toegang. Risico: blootstelling van organisatiemodellen, trainingsdata en downstream cloudresources.
2. **CVE-2025-53773** — Prompt injection via pull request-beschrijvingen in GitHub Copilot, CVSS 9.6, leidt tot remote code execution. Relevant voor elke organisatie die Copilot Enterprise inzet.

Het Proofpoint CISO-rapport van vandaag (10 sept) geeft aan dat 78% van de CISOs GenAI als veiligheidsrisico beschouwt, maar twee derde van de organisaties heeft nog geen adequate AI-beveiligingsprocessen ingericht. Het verlies van klantdata via publieke AI-platforms staat bovenaan de zorglijst.

*Bronnen: [Help Net Security – Proofpoint CISO rapport](https://www.helpnetsecurity.com/2026/09/10/proofpoint-ciso-ai-security-risks-report/) | [SentinelOne – AI Security Risks](https://www.sentinelone.com/cybersecurity-101/data-and-ai/ai-security-risks/)*

---

## 📈 Markt & Adoptie

**91% van alle bedrijven** gebruikt AI in minstens één capaciteit (2026 vs. 78% in 2024), maar twee derde zit nog in pilot- of experimentfase. De board-discussie is verschoven van "moeten we adoptie?" naar "waarom betaalt het zich niet sneller terug?"

De drie hyperscalers convergeren op een identiek enterprise-agentmodel: **Amazon Bedrock AgentCore**, **Microsoft Foundry** en **Google Gemini Enterprise Agent Platform** bieden allemaal runtime, memory, tool gateway, identity, observability en governance als gestandaardiseerde bouwblokken. Dit verlaagt de adoptiedrempel maar creëert ook lock-in risico.

AI capex 2026 bedraagt wereldwijd **$690 miljard** — een recordbedrag dat aangeeft dat de infrastructuurrace onverminderd doorgaat.

*Bronnen: [The New Stack – enterprise agent convergentie](https://thenewstack.io/amazon-microsoft-and-google-are-converging-on-the-same-enterprise-agent-architecture/) | [Futurum – AI Capex 2026](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/) | [Deloitte State of AI](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html)*

---

## 💡 Ctac-relevantie

**EU AI Act deadline (15 sept):** Als Ctac klanten begeleidt die GPAI-modellen inzetten of doorontwikkelen boven de FLOPs-drempel, is dit een directe compliance-kans. Klanten in finance en overheid hebben nu concreet hulp nodig bij het opstellen van systeem­risico-evaluaties — een propositie die Ctac's AI-unit nu kan uitwerken.

**CVE-2026-45499 (Azure OpenAI):** Ctac draait zelf én bij klanten op Azure. Security-review van Azure OpenAI-integraties is geen "nice to have" meer. Dit verdient een interne communicatie naar klant­teams vóór het weekend.

**Convergentie hyperscaler-agentplatforms:** De keuze tussen Bedrock AgentCore, Microsoft Foundry of Gemini Agent Platform wordt strategisch. Ctac kan hier waarde toevoegen door vendor-neutrale evaluatiekaders en migratie-ondersteuning aan te bieden — zeker nu klanten moeite hebben de ROI van AI te bewijzen.

**Model fatigue:** De hoeveelheid nieuwe modellen maakt het voor enterprise-klanten steeds moeilijker om te kiezen. Ctac's AI-unit kan hierop inspelen met een "model selection playbook" — een praktische gids die klanten helpt snel te evalueren welk model past bij hun use case en budget.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI news september 2026](https://llm-stats.com/ai-news)
- [CNBC – Model fatigue bij AI-labs](https://www.cnbc.com/2026/09/06/meta-google-openai-anthropic-ai-model-fatigue.html)
- [artificialintelligenceact.eu – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act beleidspagina](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [AnnexOps – EU AI Act implementatie 2026](https://annexops.com/eu-ai-act-implementation-2026/)
- [Help Net Security – Proofpoint CISO AI security rapport](https://www.helpnetsecurity.com/2026/09/10/proofpoint-ciso-ai-security-risks-report/)
- [SentinelOne – Top 14 AI Security Risks 2026](https://www.sentinelone.com/cybersecurity-101/data-and-ai/ai-security-risks/)
- [The New Stack – Amazon, Microsoft, Google enterprise agent convergentie](https://thenewstack.io/amazon-microsoft-and-google-are-converging-on-the-same-enterprise-agent-architecture/)
- [Futurum – AI Capex 2026: $690B](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/)
- [Deloitte – State of AI in the Enterprise 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [AIAgentStore – AI Agent News week sept 9](https://aiagentstore.ai/ai-agent-news/this-week)
