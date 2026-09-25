---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-03
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 3 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act enforcement gestart**: Vanaf 2 augustus 2026 handhaaft de Europese AI Office actief de verplichtingen voor GPAI-modelproviders en treden transparantievereisten in werking — chatbots moeten zich als AI identificeren, deepfakes moeten worden gelabeld.
- **Claude Opus 4.7 gelanceerd**: Anthropic brengt een nieuw topmodel uit met sterk verbeterde coding-capabilities en visuele redenering, beschikbaar op AWS Bedrock, Google Vertex AI en Microsoft Foundry.
- **OpenAI GPT-5.6 'Sol'**: Eerste frontier model dat een individuele US-overheidstoetsing doorstond én 750 tokens/sec haalt via Cerebras-inference; specifiek gepositioneerd voor defensieve cybersecurity.
- **Multi-turn AI-aanvallen slaan 88% door**: Cisco testte 6.986 multi-turn aanvallen op 15 flagship LLMs; aanvallers slaagden in 88,3% van de gevallen — een blinde vlek die single-turn testing volledig mist.
- **Microsoft AI-business: $37 miljard run-rate**: 123% groei YoY, 20+ miljoen Copilot-seats. Nieuw initiatief: Microsoft Frontier Company met $2,5 miljard voor enterprise AI-deployments.

## 🧠 Technologie & Modellen

**Claude Opus 4.7** is beschikbaar via alle Anthropic-producten, API, Amazon Bedrock, Google Vertex AI en Microsoft Foundry. Het model overtreft zijn voorganger op complexe softwareontwikkeling, biedt hogere beeldresolutie en is uitgerust met ingebouwde cybersecurity-safeguards. Voor legitiem pen-test gebruik introduceert Anthropic een nieuw Cyber Verification Program. Pricing ongewijzigd: $5/$25 per miljoen tokens. Let op: Anthropic heeft ook al Claude Opus 4.8 aangeduid als volgende stap.

**OpenAI GPT-5.6** (codenamen Sol, Terra, Luna) is het eerste frontier model dat klant-per-klant door een US-overheidsreview ging. Sol haalt 750 tokens/sec op Cerebras-hardware. Het model richt zich op defensieve cybersecurity: threat modeling, code review en blue-teaming.

**Anthropic Sonnet 5** werd tijdelijk gelanceerd met bijna-Opus-4.8-prestaties voor een introductietarief van $2/$10 per miljoen tokens (geldig t/m 31 augustus 2026) — interessant vanuit kosten-efficiëntie als Ctac API-gebruik wil uitbreiden.

## 🏛️ Governance & Ethiek

**2 augustus 2026 was een mijlpaal voor de EU AI Act.** Vanaf die datum:

- Handhaaft de Europese AI Office actief de GPAI-verplichtingen: technische documentatie, evaluaties, corrigerende maatregelen en boetes tot 3% van de wereldwijde omzet.
- Gelden transparantievereisten: chatbots moeten zich identificeren als AI; deepfakes moeten worden gelabeld.
- Moeten alle EU-lidstaten minstens één AI Regulatory Sandbox operationeel hebben.
- Gelden voor HR-gerelateerde AI-tools (bijv. kandidaatscreening) verplichte risicobeoordeling, technische documentatie, bias-tests en continue monitoring.

De AI Omnibus van mei 2026 biedt enige overgangsruimte: generatieve AI-systemen die vóór 2 augustus 2026 al op de markt waren, krijgen tot 2 december 2026 de tijd voor de machine-readable marking-vereisten.

## 🔐 Security & Risk

**Multi-turn aanvallen zijn de blinde vlek van AI-security.** Cisco presenteerde bij VB Transform 2026 dat 88,3% van multi-turn aanvallen op 15 flagship LLMs slaagt — terwijl standaard single-turn tests dit volledig missen. OpenAI, Anthropic, Google en xAI-modellen zakken allemaal door deze test.

**Agent runtime security** is urgent: prompt injection treft productiefomgevingen als Claude Code, Gemini CLI en GitHub Copilot via gedeelde aanvalsvectoren in RAG-pipelines en model-routers. Meer dan 54% van enterprise-organisaties rapporteert al een bevestigd agent-security-incident of bijna-incident.

**Handhavingsrisico in NL/BE**: Bedrijven zonder risicobeoordeling voor HR-AI-tools (sollicitatiescreening, prestatiebeoordeling) lopen nu direct handhavingsrisico onder de EU AI Act.

## 📈 Markt & Adoptie

**Microsoft** domineert enterprise AI: $37 miljard AI-revenue run-rate (+123% YoY), 20+ miljoen betaalde Copilot-seats. Het nieuwe **Microsoft Frontier Company**-initiatief ($2,5 miljard) hanteert een forward-deployed-engineer model — exact wat Ctac als implementatiepartner ook doet.

**Google** introduceert **Agentic Data Cloud** (Google Cloud Next '26): een AI-native architectuur die legacy enterprise dataplatformen omvormt tot redenerende systemen. Relevant voor klanten met SAP- of datawarehouse-omgevingen.

**Anthropic** overstijgt $30 miljard run-rate revenue en stevent af op winstgevendheid in 2029 — een jaar eerder dan OpenAI. Amazon, Microsoft, Meta en Google plannen gezamenlijk tot $725 miljard aan capex in 2026.

**Twee derde van enterprise-organisaties** zit nog vast in de generatieve AI pilot-fase. Satya Nadella waarschuwt: bedrijven die op één AI-platform vertrouwen voor alles, overleven het niet. Multi-model strategie is de nieuwe norm.

## 💡 Ctac-relevantie

**EU AI Act compliance als directe propositie-kans.** Vanaf 2 augustus zijn HR-AI-tools onderworpen aan handhaving. Veel Ctac-klanten in NL/BE (overheid, finance, industrie) hebben dit nog niet volledig op orde. Ctac kan concreet waarde leveren: compliance-quickscans, risicobeoordeling voor bestaande AI-tooling en begeleiding bij het opzetten van documentatie en monitoring.

**Agent security wordt een must-have.** De 88%-doorbraakrate bij multi-turn aanvallen maakt duidelijk dat AI-governance niet stopt bij deployment — runtime security is een nieuwe vereiste. Kans voor Ctac om security-geïntegreerde AI-architecturen aan te bieden als onderdeel van implementatietrajecten.

**Microsoft Frontier Company volgt het forward-deployed model** — precies wat Ctac als IT-implementatiepartner al doet. Positief signaal voor de marktpositie: de vraag naar deployment-expertise groeit hard, en grote platforms bewegen die richting op, wat kansen creëert voor partners.

## 📚 Bronnen & verder lezen

- [Europese Commissie – EU AI Act enforcement start 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act – Implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act – Transparency Rules (Article 50)](https://artificialintelligenceact.eu/transparency-rules-article-50/)
- [Anthropic – Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [VentureBeat – Anthropic releases Claude Opus 4.7](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm)
- [OpenAI – Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)
- [TechCrunch – OpenAI launches GPT-5.6 family](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [VentureBeat – Multi-turn attacks broke AI models 88% of the time](https://venturebeat.com/security/openai-anthropic-google-and-xai-models-all-broke-under-multi-turn-attack-up-to-88-of-the-time)
- [VentureBeat – Prompt injection exploiting enterprise AI agents](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [TechCrunch – Microsoft launches Frontier Company with $2.5B](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [CIO Dive – Google launches Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [TechCrunch – Satya Nadella warns against single AI dependency](https://techcrunch.com/2026/07/27/satya-nadella-says-companies-that-trust-one-ai-for-everything-may-not-survive/)
- [LLM Stats – AI Updates August 2026](https://llm-stats.com/llm-updates)
