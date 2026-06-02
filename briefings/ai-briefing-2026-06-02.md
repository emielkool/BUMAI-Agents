---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-02
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2 juni 2026

## 🔑 Highlights van de dag

- **GLM-5.1 overstijgt gesloten modellen op agentic benchmarks.** Z.ai lanceerde een 754B open-source model dat op SWE-Bench Pro beter scoort dan Claude Opus 4.6 en GPT-5.4 – een serieuze wake-up call voor enterprise-teams die dure API's betalen.
- **OpenAI lanceert Daybreak:** AI-aangedreven kwetsbaarheidsscan op basis van GPT-5.5, nu al geïntegreerd bij Akamai, Cisco, CrowdStrike en Palo Alto Networks.
- **EU AI Act countdown: nog 61 dagen.** Volledige toepasselijkheid per 2 augustus 2026; vanaf die datum moeten Europese burgers geïnformeerd worden wanneer ze met AI interacteren.
- **Benelux koploper, maar talent knelt.** 61% van de Nederlandse bedrijven gebruikt inmiddels AI (van 49% vorig jaar); 58% noemt het gebrek aan digitale vaardigheden als grootste blokkade.
- **Agentic AI verspreidt zich razendsnel in enterprise.** KPMG: 33% van organisaties zet nu AI-agenten in – een verdrievoudiging ten opzichte van twee kwartalen geleden.

## 🧠 Technologie & Modellen

**GLM-5.1 – de open-source agentic verrassing**
Z.ai (voorheen ZhipuAI) publiceerde [GLM-5.1](https://huggingface.co/zai-org/GLM-5.1) met 754 miljard parameters en een contextvenster van 202.752 tokens. Het model haalt 95.3 op AIME 2026 en scoort state-of-the-art op SWE-Bench Pro, waarbij het gesloten grensmodellen verslaat. Opmerkelijk: het ondersteunt 1.700 stappen in agentic workflows en wordt samen met Kimi K2.6, DeepSeek V4 Pro en Qwen3 beschouwd als een topkandidaat voor autonome agent-implementaties. Volledig lokaal te draaien via vLLM of SGLang. Bron: [VentureBeat](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4)

**Google I/O 2026 – Gemini Omni & agentisch zoeken**
Google kondigde Gemini Omni aan (volledige multimodaliteit inclusief videogeneratie) en Gemini 3.5 Flash als nieuw standaardmodel in AI Mode voor Google Search wereldwijd. Search krijgt een agentisch laag waarmee gebruikers meerdere AI-agenten direct vanuit de zoekopdracht kunnen aansturen. Bron: [blog.google](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)

**OpenAI GPT-Rosalind voor life sciences**
OpenAI presenteerde een gespecialiseerd frontier reasoning model voor genomica, proteïne-analyse en geneesmiddelenontdekking. Sector-specifieke frontier modellen worden een patroon: dit is hype noch triviaal voor Ctac's klanten in zorg en industrie. Bron: [openai.com](https://openai.com/index/introducing-gpt-rosalind/)

## 🏛️ Governance & Ethiek

**EU AI Act: 61 dagen tot volledige werking**
Per 2 augustus 2026 treedt de AI Act volledig in werking. Kernverplichting: burgers moeten geïnformeerd worden wanneer ze met AI interacteren of AI-gegenereerde content zien. Elke lidstaat moet vóór die datum minimaal één AI-sandbox operationeel hebben. Het 'AI omnibus'-pakket (politiek akkoord 7 mei 2026) verschuift hoge-risico-verplichtingen naar december 2027, maar transparantieplichten gelden wél per augustus. Bron: [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Benelux: sterk in adoptie, zwak in talent**
Computable rapporteert dat de Benelux Europees koploper is in AI-adoptie (NL 61%, BE 62%), maar dat 58% van de bedrijven het talent tekort als kritieke drempel ervaart. Dat raakt Ctac direct: klanten zoeken externen die het gat opvullen. Bron: [computable.nl](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)

## 🔐 Security & Risk

**OpenAI Daybreak: AI scant jouw code op kwetsbaarheden**
OpenAI lanceerde [Daybreak](https://openai.com/daybreak/), een initiatief waarbij GPT-5.5 in drie varianten (standaard, Trusted Access for Cyber, Cyber) repository's doorzoekt op aanvalspaden en patchvoorstellen genereert. Toegang is nog beperkt en vereist verificatie, maar Akamai, Cisco en CrowdStrike zijn al aan boord. Dit is een betekenisvolle stap: van generatieve AI naar actieve defensieve security tooling. Bron: [The Hacker News](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html)

**Enterprise AI-risico geconcentreerd bij power users**
Een nieuw rapport (The Hacker News, mei 2026) toont dat het gros van de enterprise AI-risicofeiten neerkomt bij een kleine groep zware gebruikers en een handvol dominante platforms. Zelf-gehoste AI-assistenten vertonen gemiddeld 2,6 CVE's per dag. Organisaties die AI snel uitrollen zonder governance-kader lopen significant verhoogd risico. Bron: [The Hacker News](https://thehackernews.com/2026/05/new-ai-usage-report-enterprise-ai-risk.html)

## 📈 Markt & Adoptie

**Google Cloud passeert $20 miljard omzet**
Google Cloud boekte in Q1 2026 voor het eerst meer dan $20 miljard omzet (+63% YoY), grotendeels gedreven door enterprise AI-vraag. Microsoft en AWS investeren gezamenlijk ruim $500 miljard in infrastructuur voor FY2026. De Big Three controleren nu 71% van de cloud-markt. Bron: [CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)

**Nvidia AI agent platform met SAP, Salesforce, Adobe**
Nvidia lanceerde op GTC 2026 een enterprise AI agent platform, met 17 partners waaronder SAP, Salesforce en Adobe. Dit versnelt de integratie van agentische AI in bestaande enterprise software-suites – relevant voor Ctac-klanten op SAP. Bron: [VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)

**Agentic AI: van pilot naar productie**
KPMG meldt dat 33% van de organisaties nu AI-agenten in productie heeft – drie keer zoveel als twee kwartalen eerder. De adoptiecurve verloopt aanzienlijk sneller dan analisten hadden voorspeld. Bron: [VentureBeat](https://venturebeat.com/ai/the-great-ai-agent-acceleration-why-enterprise-adoption-is-happening-faster-than-anyone-predicted)

## 💡 Ctac-relevantie

**Talent als onmiddellijke propositiekans.** De Benelux-cijfers zijn duidelijk: adoptie groeit, maar talent ontbreekt. Ctac kan deze kloof direct adresseren met AI-enablement diensten – van AI-readiness assessments tot hands-on begeleiding bij agent-implementaties. Dit is geen abstracte toekomststrategie, dit is de markt van nú.

**EU AI Act: augustus-deadline is concreet.** Klanten in gereguleerde sectoren (overheid, zorg, finance) moeten vóór 2 augustus transparantiemaatregelen hebben doorgevoerd. Ctac kan hier een gerichte sprint-dienst op bouwen: inventarisatie van AI-systemen, classificatie onder de Act, en implementatie van gebruikersinformatieplicht.

**Open-source agentic modellen zijn rijp voor productie.** GLM-5.1 en DeepSeek V4 Pro presteren op frontier-niveau en zijn lokaal te hosten. Voor klanten met data-soevereiniteitswensen of hoge API-kosten biedt dit een serieus alternatief. Ctac's AI-engineer kan hier direct mee aan de slag voor proof-of-concepts.

**SAP + Nvidia agent platform** is strategisch interessant: Ctac-klanten op SAP krijgen automatisch agent-capabilities aangeboden. Het moment om SAP-klanten te begeleiden bij verantwoorde agent-adoptie is nu, voordat de hype zonder sturing inrolt.

## 📚 Bronnen & verder lezen

- [GLM-5.1 op Hugging Face](https://huggingface.co/zai-org/GLM-5.1)
- [VentureBeat – GLM-5.1 verslaat gesloten modellen](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4)
- [Google I/O 2026 – alle aankondigingen](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [OpenAI Daybreak – kwetsbaarheidsscan](https://openai.com/daybreak/)
- [The Hacker News – Daybreak lancering](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html)
- [The Hacker News – Enterprise AI-risico rapport](https://thehackernews.com/2026/05/new-ai-usage-report-enterprise-ai-risk.html)
- [EU AI Act – Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Computable – Benelux koploper, talent tekort](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [CIO Dive – Google Cloud $20B](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [VentureBeat – Nvidia enterprise agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [VentureBeat – Agentic AI acceleratie](https://venturebeat.com/ai/the-great-ai-agent-acceleration-why-enterprise-adoption-is-happening-faster-than-anyone-predicted)
- [OpenAI – GPT-Rosalind life sciences](https://openai.com/index/introducing-gpt-rosalind/)
