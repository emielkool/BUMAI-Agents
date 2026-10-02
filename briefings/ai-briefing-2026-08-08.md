---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-08
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 8 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaving gestart (2 aug):** De Europese Commissie is per 2 augustus begonnen met actieve handhaving van de AI Act, inclusief verplichte transparantie-eisen voor chatbots en deepfakes. Bedrijven riskeren boetes tot €35M of 7% omzet.
- **OpenAI lanceert GPT-5.6 (4 aug):** Drie nieuwe varianten (Sol, Terra, Luna), waarbij GPT-5.6 Sol beweert de frontier opnieuw te herdefiniëren op coding, cybersecurity en science — maar het presteert op slechts 2 van 7 benchmarks beter dan Claude Opus 5.
- **Agentic AI spant legacy IT:** Gartner stelt dat agentic AI tot $234 miljard SaaS-markt verstoort voor 2030, terwijl meer dan 80% van bedrijven hun infrastructuur moet upgraden om agents op schaal te kunnen draaien.
- **SSC-ICT, Dictu en DUO bouwen soevereine digitale werkomgeving (7 aug):** De Nederlandse rijksoverheid werkt actief aan ontkoppeling van Amerikaanse cloudleveranciers — versneld door AI Act en geopolitieke druk.
- **Prompt injection blijft kritiek risico:** Enterprise-agents, RAG-pipelines en model-routers zijn structureel kwetsbaar; Microsoft moest in 2026 al een CVE uitbrengen voor Copilot Studio.

---

## 🧠 Technologie & Modellen

**GPT-5.6 Sol** (OpenAI, 4 aug) is beschikbaar in drie tiers: Sol (flagship), Terra (mid-range) en Luna (budget). OpenAI positioneert Sol als "frontier intelligence" voor coding, kenniswerk en cybersecurity. In de praktijk wint Sol op DeepSWE en HealthBench Professional, maar verliest het op vijf andere benchmarks van Claude Opus 5 — een kanttekening die OpenAI's marketingclaims enigszins relativeert.

**Claude Opus 5** (Anthropic, 24 jul) biedt sterkere brede benchmark-prestaties dan GPT-5.6 Sol, bij lagere outputkosten ($25/M tokens vs $30/M). Voor agentic use cases die output-intensief zijn, is dat economisch relevant.

**Meta Muse Spark 1.2** (5 aug) en **DeepSeek V4-Flash** (31 jul) tonen aan dat het releaseritme in 2026 ongekend hoog is — inmiddels 337+ getracked modelreleases. De praktische les: evalueer modellen per taaktype, niet op aankondiging.

*Bronnen: [OpenAI GPT-5.6](https://openai.com/index/gpt-5-6/) · [TechCrunch GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/) · [LLM Stats vergelijking](https://llm-stats.com/models/compare/claude-opus-5-vs-gpt-5.6-sol) · [LLM Stats nieuws](https://llm-stats.com/ai-news)*

---

## 🏛️ Governance & Ethiek

**EU AI Act-handhaving is nu realiteit.** Vanaf 2 augustus zijn de transparantie-eisen juridisch afdwingbaar: chatbots moeten zich identificeren als AI, deepfakes moeten worden gelabeld. Sancties voor verboden AI-praktijken lopen tot €35M of 7% mondiale omzet. Deadline voor hoog-risico systemen is verschoven naar december 2027 — wat bedrijven enige ruimte biedt, maar ook het risico op uitstelgedrag vergroot.

In Nederland werken **SSC-ICT, Dictu en DUO** samen aan een soevereine digitale werkomgeving, mede als antwoord op de AI Act-vereisten en het risico van afhankelijkheid van niet-EU cloud. Platform **Vlam** — het soevereine rijks-AI-platform — staat in de startblokken voor brede uitrol in H2 2026.

*Bronnen: [EC AI Act handhaving](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) · [Computable AI Act](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/) · [SSC-ICT soevereine werkomgeving](https://www.computable.nl/2026/08/07/ssc-ict-dictu-en-duo-bouwen-samen-aan-soevereine-digitale-werkomgeving/)*

---

## 🔐 Security & Risk

**Prompt injection** is inmiddels het meest gedocumenteerde risico voor enterprise AI — OWASP LLM Top 10 plaatst het op #1. In 2026 was er al een CVE voor Microsoft Copilot Studio (CVE-2026-21520, CVSS 7.5), en een incident waarbij 1,5 miljoen API-tokens lekten via Moltbook's agent-platform. De aanvalsvector verschuift van standalone chatbots naar complexe agent-ketens en RAG-pipelines, waardoor de blast radius groter wordt.

Conclusie: wie agents in productie brengt zonder expliciete prompt-injection mitigaties, neemt een structureel en slecht verzekerbaar risico.

*Bronnen: [VentureBeat prompt injection](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers) · [Microsoft Copilot CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)*

---

## 📈 Markt & Adoptie

**Microsoft** rapporteert 20M+ Copilot 365-seats (betaald), met een AI-omzet run rate van $37 miljard/jaar (+123% YoY). Het bedrijf investeert $2,5 miljard om engineers embedded bij grote klanten te plaatsen. **AWS** volgt met $1 miljard in een Forward Deployed Engineering hub. Dit signaleert een verschuiving van licentieverkoop naar klantintegratie als dominante go-to-market.

**Gartner** voorspelt dat agentic AI tot $234 miljard aan SaaS-marktwaarde zal herdefiniëren voor 2030. Tegelijk stelt een Google-rapport dat 80%+ van bedrijven hun IT-stack moet upgraden om agents op schaal te kunnen runnen — legacy architecturen zijn hiervoor niet berekend.

*Bronnen: [CIO Dive Microsoft Copilot](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/) · [CIO Dive Gartner agentic AI](https://www.ciodive.com/news/agentic-ai-disrupt-234-billion-saas-spending/824530/) · [CIO Dive agentic legacy IT](https://www.ciodive.com/news/agentic-ai-strains-legacy-it-systems/825003/) · [Microsoft $2.5B engineers](https://www.ciodive.com/news/microsoft-25b-embed-engineers/824392/)*

---

## 💡 Ctac-relevantie

**AI Act compliance als concrete dienst.** Met handhaving gestart per 2 augustus, hebben klanten van Ctac — zeker in overheid, zorg en finance — nu een urgente behoefte aan AI-compliance scans en implementatiebegeleiding. Ctac kan dit positioneren als een concrete, kortlopende opdracht met directe regeldruk als driver.

**Soevereine AI-omgevingen als groeimarkt.** De beweging bij SSC-ICT/Dictu/DUO en het Vlam-platform laat zien dat de rijksoverheid actief zoekt naar Nederlandse/Europese alternatieven voor hyperscaler-afhankelijkheid. Ctac's positie in de publieke sector maakt dit tot een strategisch relevant gesprek, met name rond Azure-alternatieven of hybrid cloud-architecturen.

**Agentische AI vraagt om infrastructuuradvies.** Het feit dat 80%+ van bedrijven hun infra moet aanpassen voor agents, opent een adviesmarkt op het snijvlak van architectuur en AI-adoptie — exact het type opdracht waar Ctac sterk in is.

**Security by design voor agents.** Prompt injection is niet langer een theoretisch risico. Bij elke agent-implementatie moet Ctac dit expliciet adresseren — zowel intern als richting klanten.

---

## 📚 Bronnen & verder lezen

- [OpenAI GPT-5.6 aankondiging](https://openai.com/index/gpt-5-6/)
- [TechCrunch: GPT-5.6 launch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [LLM Stats: Claude Opus 5 vs GPT-5.6 Sol](https://llm-stats.com/models/compare/claude-opus-5-vs-gpt-5.6-sol)
- [Europese Commissie: AI Act handhaving gestart](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [Computable: AI Act transparantie-eisen](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [Computable: SSC-ICT soevereine digitale werkomgeving](https://www.computable.nl/2026/08/07/ssc-ict-dictu-en-duo-bouwen-samen-aan-soevereine-digitale-werkomgeving/)
- [VentureBeat: Prompt injection in enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [CIO Dive: Agentic AI strains legacy IT](https://www.ciodive.com/news/agentic-ai-strains-legacy-it-systems/825003/)
- [CIO Dive: Gartner $234B agentic AI disruption](https://www.ciodive.com/news/agentic-ai-disrupt-234-billion-saas-spending/824530/)
- [CIO Dive: Microsoft Copilot groei](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [LLM Stats: AI nieuws augustus 2026](https://llm-stats.com/ai-news)
