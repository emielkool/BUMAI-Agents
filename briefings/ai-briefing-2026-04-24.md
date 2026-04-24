---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-24
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 24 april 2026

## 🔑 Highlights van de dag

- **GPT-5.5 gelanceerd**: OpenAI bracht gisteren GPT-5.5 uit, omschreven als hun "slimste en meest intuïtieve model" tot nu toe. Het richt zich op agentic coding en kenniswerk, inclusief wetenschappelijk onderzoek en wiskunde.
- **DeepSeek V4 – open weights, frontier performance**: Een 1 biljoen parameter Mixture-of-Experts model met volledig open gewichten presteert concurrerend met Claude Opus 4.6, maar is voor slechts $5,2 miljoen getraind – een directe aanval op de businesscase van closed-source frontier labs.
- **EU AI Act: twee maanden voor volledige inwerkingtreding**: Per 2 augustus 2026 is de EU AI Act volledig van toepassing, inclusief handhaving van Artikel 14 (menselijk toezicht bij high-risk AI). Lidstaten moeten vóór die datum een nationale AI-sandbox operationeel hebben.
- **Microsoft 365 E7 "Frontier Suite" per 1 mei beschikbaar**: Microsoft bundelt M365 Copilot, Entra Suite en het nieuwe Agent 365-platform in één enterprise-licentie – dit wordt de standaard voor grote Nederlandse enterprise-klanten.
- **Vercel getroffen door supply chain hack via AI-tool**: Context AI, een populaire AI-datakoppelingstool, werd gehackt. Aanvallers kregen toegang tot Vercel-klantdata, waaronder API keys, broncode en databasegegevens.

## 🧠 Technologie & Modellen

**GPT-5.5** is op 23 april uitgebracht door OpenAI en scoort op brede benchmarks hoger dan Gemini 3.1 Pro en Claude Opus 4.5. Het model sluit aan op de eerder uitgebrachte **Agents SDK-update** (mid-april), die developers een gestandaardiseerde sandboxomgeving biedt voor langlopende agentic taken. OpenAI richtte daarnaast samen met Anthropic en Block de **Agentic AI Foundation (AAIF)** op onder de Linux Foundation – bedoeld als neutrale beheerder van open, interoperabele infrastructuur voor agentic AI. AGENTS.md, de standaard voor agent-instructies, telt inmiddels 60.000+ open-source adopties.
([TechCrunch](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/) | [OpenAI](https://openai.com/index/agentic-ai-foundation/))

**DeepSeek V4** verscheen met volledig open gewichten: een 1 biljoen parameter MoE-model getraind voor slechts $5,2 miljoen dat frontier-modellen bijhoudt. Dit bevestigt dat de trainingskosten van state-of-the-art modellen snel dalen – met structurele gevolgen voor de marktpositie van closed-source aanbieders.

**Google** lanceerde de achtste generatie Tensor Processing Units (TPU 8t en 8i), specifiek ontworpen voor het agentic tijdperk, en verdiepte tegelijkertijd via een nieuw miljardendeal zijn relatie met **Thinking Machines Lab** (startup van ex-OpenAI COO Mira Murati).
([TechCrunch](https://techcrunch.com/2026/04/22/exclusive-google-deepens-thinking-machines-lab-ties-with-new-multi-billion-dollar-deal/))

## 🏛️ Governance & Ethiek

De EU AI Act gaat op **2 augustus 2026** volledig in. Artikel 14 (menselijk toezicht bij high-risk toepassingen) wordt dan gehandhaafd, en lidstaten zijn verplicht vóór die datum minimaal één nationale AI-sandbox operationeel te hebben. De Europese Commissie maakte op 21 april €63,2 miljoen vrij voor AI-innovatie in gezondheid en online veiligheid.
([artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/) | [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

**Kritische noot**: Organisaties die high-risk AI inzetten en nog geen named owners en execution traces hebben ingericht, lopen reëel handhavingsrisico. De deadline is geen verrassing meer – gebrek aan voorbereiding is nu een strategische keuze.

## 🔐 Security & Risk

**Vercel-breach via Context AI** (20 april): een supply chain-aanval op een veelgebruikte AI-datakoppelingstool leidde tot diefstal van klant-API keys, broncode en databasedata van Vercel. Het patroon is duidelijk: de aanvalsvector verschuift naar de AI-toolinglaag zelf.
([TechCrunch](https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/))

De **OWASP Agentic Top 10 2026** is geformaliseerd. De tien risico's voor agentic AI-toepassingen omvatten goal hijack, tool misuse, identiteits- en privilege-misbruik, memory poisoning en rogue agents. In 2025 werden bij 90+ organisaties AI-tools gecompromitteerd – de nieuwe generatie tools heeft meer privileges en een groter aanvalsoppervlak.
([VentureBeat](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds))

## 📈 Markt & Adoptie

**Microsoft** consolideert zijn enterprise-positie met de **Microsoft 365 E7 "Frontier Suite"** (GA: 1 mei 2026), die M365 Copilot, Entra Suite en het nieuwe **Agent 365**-platform bundelt als gecentraliseerde control plane voor agent governance. Microsoft committeert zich tevens aan Google's **Agent2Agent (A2A)**-interoperabiliteitsstandaard, wat cross-platform multi-agent workflows mogelijk maakt.
([Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/) | [CIO Dive](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/))

Gartner bevestigt: Microsoft en Google domineren de enterprise AI-markt. Microsoft wint het bij brede platformadoptie; Google bij agentic AI-stacks op enterprise-schaal. **BlackRock** introduceerde intern "RockAI", een no-code platform voor het bouwen van custom AI-agents – een signaal dat grote financiële instellingen AI-orchestratie in eigen beheer nemen.
([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

## 💡 Ctac-relevantie

De **Microsoft 365 E7-lancering per 1 mei** is direct relevant voor Ctac's enterprise-klanten. Organisaties zullen licentievragen stellen en behoefte hebben aan implementatiebegeleiding voor Agent 365 en Copilot-uitrol. Ctac kan hier direct op positioneren als technisch adviseur.

**DeepSeek V4** en de dalende trainingskosten versterken de businesscase voor private AI-deployments bij klanten die data-soevereiniteit en kostenbewuste AI-adoptie prioriteren. Dit is een propositie waarbij Ctac zich kan onderscheiden van cloudreseller-concurrenten.

De **OWASP Agentic Top 10** biedt een concreet raamwerk voor AI security assessments. Nu agentic AI in productie gaat bij enterprises, is er vraag naar partners die risico's methodisch in kaart brengen. Dit is een kans voor Ctac's AI-unit om een advisory-aanbod te ontwikkelen.

Ten slotte: de **EU AI Act deadline van 2 augustus** nadert snel. Klanten in de publieke sector en financiële dienstverlening met high-risk AI-toepassingen hebben behoefte aan compliance-ondersteuning. Dit is een concrete propositiekans voor Ctac op korte termijn.

## 📚 Bronnen & verder lezen

- [OpenAI releases GPT-5.5 – TechCrunch](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)
- [OpenAI Agents SDK update – TechCrunch](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/)
- [OpenAI Agentic AI Foundation – OpenAI](https://openai.com/index/agentic-ai-foundation/)
- [Google deepens Thinking Machines Lab deal – TechCrunch](https://techcrunch.com/2026/04/22/exclusive-google-deepens-thinking-machines-lab-ties-with-new-multi-billion-dollar-deal/)
- [EU AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act – EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Vercel security breach via Context AI – TechCrunch](https://techcrunch.com/2026/04/20/app-host-vercel-confirms-security-incident-says-customer-data-was-stolen-via-breach-at-context-ai/)
- [Agentic AI security – VentureBeat](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds)
- [Microsoft 365 E7 Frontier Suite – Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/)
- [Microsoft commits to A2A standard – CIO Dive](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [Microsoft & Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [LLM News Today april 2026 – llm-stats.com](https://llm-stats.com/ai-news)
