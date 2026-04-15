---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-13
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2026-04-13

## 🔑 Highlights van de dag

- **Anthropic houdt Mythos achter slot**: Het nieuwe frontier model Mythos is zo bedreven in het vinden en exploiteren van kwetsbaarheden dat Anthropic het niet publiek uitbrengt. Slechts 12 partnerorganisaties (waaronder Apple, Microsoft, Cisco) krijgen toegang voor defensief beveiligingswerk.
- **Google Gemma 4 beschikbaar als open model**: Google lanceert Gemma 4 in vier maten (tot 31B), met Apache 2-licentie, multimodaal (tekst, beeld, audio) en topscore op open model-leaderboards. Dit is de meest concrete open-source challenger van gesloten frontier modellen tot nu toe.
- **EU AI Act: de deadline van augustus nadert**: Per 2 augustus 2026 is de AI Act volledig van kracht. De Commissie werkt in Q2 2026 aan richtlijnen voor high-risk systemen, transparantieverplichtingen en incidentrapportage — voor veel organisaties is de urgentie nu voelbaar.
- **MCP wordt industrie-standaard**: Anthropic heeft het Model Context Protocol (MCP) overgedragen aan de Agentic AI Foundation, samen met Block en OpenAI. Met 10.000+ actieve servers is MCP de facto connector-standaard voor AI-agenten.
- **Prompt injection: structureel probleem erkend**: OpenAI erkent officieel dat prompt injection "likely to never be fully solved" is — enterprise-implementaties van AI-agenten blijven daarmee structureel blootgesteld aan dit aanvalsvector.

---

## 🧠 Technologie & Modellen

**Google Gemma 4** is uitgebracht als open model in vier varianten: E2B, E4B, 26B (MoE) en 31B (Dense). Het 31B-model staat op plek #3 in de global open model Arena-leaderboard. Gemma 4 is multimodaal, volledig Apache 2-gelicenseerd en heeft dag-één-ondersteuning voor Hugging Face, vLLM, llama.cpp, Ollama, en andere populaire inference-stacks. Dit maakt het onmiddellijk bruikbaar voor on-premise en edge deployment.
→ [blog.google](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) | [huggingface.co/blog/gemma4](https://huggingface.co/blog/gemma4)

**Anthropic Mythos Preview** is een nieuw frontier model specifiek ingezet voor cybersecurity. In tests identificeerde Mythos duizenden zero-day kwetsbaarheden in alle grote browsers en besturingssystemen. Anthropic investeert $100M in gebruik voor 12 partnerorganisaties en $4M in open-source beveiligingsinitiatieven (Project Glasswing).
→ [techcrunch.com](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) | [axios.com](https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks)

**MCP overgedragen aan Agentic AI Foundation**: Anthropic, Block en OpenAI richten samen de Agentic AI Foundation op als beheerder van het Model Context Protocol. Met 10.000+ actieve publieke servers en adoptie in ChatGPT, Cursor en Gemini is MCP de standaard voor agent-integraties.
→ [anthropic.com](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)

---

## 🏛️ Governance & Ethiek

De **EU AI Act** is volledig van kracht per 2 augustus 2026. In Q2 2026 publiceert de Europese Commissie praktische richtlijnen voor: classificatie van hoog-risico systemen, transparantieverplichtingen (art. 50), rapportage van ernstige incidenten, en verplichtingen voor providers en deployers. Elke lidstaat moet voor augustus een nationale AI-sandbox hebben ingericht.
→ [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/) | [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)

In **België** bleek tijdschrift Elle stiekem AI-gegenereerde content te publiceren onder namen van nepjournalisten — zonder markering. Dit illustreert de spanning tussen transparantieverplichtingen onder de AI Act (art. 50) en redactionele praktijk.
→ [nos.nl](https://nos.nl/artikel/2572829-belgische-elle-werkte-stiekem-met-ai-boven-artikelen-stonden-nepjournalisten)

---

## 🔐 Security & Risk

**Prompt injection blijft structureel risico**: OpenAI erkent formeel dat prompt injection "here to stay" is — net als phishing op het web. Het UK NCSC deelt die inschatting. Voor enterprise AI-agenten die externe data verwerken (e-mails, documenten, web) is dit een blijvend architectuurprobleem, geen oplosbaar bug.
→ [venturebeat.com](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)

**LangChain/LangGraph kwetsbaarheden** (drie CVE's, gepubliceerd maart 2026): aanvallers kunnen via deze populaire AI-frameworks toegang krijgen tot bestandssystemen, omgevingsvariabelen (API-keys) en conversatiegeschiedenissen. Relevant voor teams die RAG-pipelines of agenten bouwen op deze frameworks.
→ [thehackernews.com](https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html)

**Anthropic beperkt Claude-API-gebruik via third-party agents**: Vanaf 4 april 2026 werken Pro/Max-abonnementen niet meer met externe agentic tools (zoals OpenClaw). Alleen pay-as-you-go API-gebruik is nog toegestaan.
→ [venturebeat.com](https://venturebeat.com/technology/anthropic-cuts-off-the-ability-to-use-claude-subscriptions-with-openclaw-and)

---

## 📈 Markt & Adoptie

**Microsoft MAI-modellen** (MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2) zijn beschikbaar via Microsoft Foundry — eigengebouwde foundation modellen voor spraak-naar-tekst, stemgeneratie en beeldcreatie. Microsoft positioneert zich hiermee als directe concurrent van OpenAI en Google op modellaag, niet alleen als distributeur.
→ [venturebeat.com](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)

**Enterprise AI-adoptie versnelt, maar is ongelijk**: Ondanks optimistische VC-voorspellingen erkende OpenAI's COO in februari 2026 dat AI "nog niet echt in enterprise-bedrijfsprocessen is doorgedrongen". Budgetten concentreren zich bij minder leveranciers. Dit is een realistisch signaal dat de adoptiecurve steiler moet — en dat begeleiding bij implementatie meer waarde toevoegt dan ooit.
→ [techcrunch.com](https://techcrunch.com/2026/02/24/openai-coo-says-we-have-not-yet-really-seen-ai-penetrate-enterprise-business-processes/)

---

## 💡 Ctac-relevantie

**MCP als strategisch aandachtspunt**: Nu MCP industrie-standaard wordt voor agent-integraties, is kennis van MCP-servers een directe differentiator in klantprojecten. Ctac's AI-unit zou een MCP-referentie-architectuur kunnen ontwikkelen voor veelgebruikte klantomgevingen (SAP, Microsoft 365, Dynamics).

**Gemma 4 voor on-premise klanten**: De Apache 2-licentie van Gemma 4 maakt het direct inzetbaar bij klanten in overheid, zorg of finance die geen data naar cloudproviders willen sturen. Dit is een concreet propositie-argument voor de komende kwartalen.

**EU AI Act compliance als dienst**: Met de deadline van augustus 2026 en nieuwe Commissierichtlijnen in Q2 is er een duidelijk window voor een complianceaanbod: klanten helpen hun AI-systemen te classificeren, risicobeoordelingen uitvoeren en documentatieplichten invullen.

**Security in AI-projecten**: De LangChain-kwetsbaarheden en het structurele prompt injection-probleem maken duidelijk dat security review van AI-pipelines standaard onderdeel moet zijn van elk delivery-traject. Dit is een intern kwaliteitsargument én een extern verkoopargument.

---

## 📚 Bronnen & verder lezen

- [Google Gemma 4 - blog.google](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
- [Gemma 4 op Hugging Face](https://huggingface.co/blog/gemma4)
- [Anthropic Mythos Preview - TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [Mythos: te gevaarlijk voor release - Axios](https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks)
- [Anthropic Project Glasswing](https://www.anthropic.com/glasswing)
- [MCP overgedragen aan Agentic AI Foundation - Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act richtlijnen - Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Prompt injection: here to stay - VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [LangChain/LangGraph kwetsbaarheden - The Hacker News](https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html)
- [Microsoft MAI-modellen - VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [OpenAI COO over enterprise adoptie - TechCrunch](https://techcrunch.com/2026/02/24/openai-coo-says-we-have-not-yet-really-seen-ai-penetrate-enterprise-business-processes/)
- [Belgische Elle met AI-nepjournalisten - NOS](https://nos.nl/artikel/2572829-belgische-elle-werkte-stiekem-met-ai-boven-artikelen-stonden-nepjournalisten)
- [Anthropic Claude subscriptions beperkt voor third-party agents - VentureBeat](https://venturebeat.com/technology/anthropic-cuts-off-the-ability-to-use-claude-subscriptions-with-openclaw-and)
