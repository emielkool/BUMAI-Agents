---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-06
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 6 oktober 2026

## 🔑 Highlights van de dag

- **OpenAI DevDay 2026:** Meer dan 20 aankondigingen, waaronder GPT-6.1 Sol (near-Astra intelligentie voor een vijfde van de prijs), de Agents API in public beta, en Dots – een autonome agentische assistent. Dit is de meest substantiële developer-release van OpenAI dit jaar.
- **Enterprise AI vastgelopen:** Twee derde van bedrijven zit nog in de pilot-fase en 30% meldt productiviteitsverlies na invoering van agentische AI. De bottleneck is infrastructuur, governance en ROI – niet de modellen zelf.
- **EU AI Act actief gehandhaafd:** Vanaf 2 augustus handhaaft de AI Office het AI Act. Chatbots moeten zichzelf identificeren als AI, deepfakes worden verplicht gelabeld. Boetes tot €35M of 7% van de wereldwijde jaaromzet zijn reëel.
- **AI-agent security crisis:** 88% van enterprise-organisaties rapporteerde een AI-agent-beveiligingsincident het afgelopen jaar, maar slechts 6% van het securitybudget is hierop gericht.
- **OpenAI breekt exclusiviteit met Microsoft:** OpenAI mag nu actief verkopen via AWS en Google Cloud, wat de multi-cloud AI-markt fundamenteel verandert.

## 🧠 Technologie & Modellen

**OpenAI DevDay 2026** stond in het teken van agentische AI en kostenreductie. Kernpunten:

- **GPT-6.1 Sol** is een significante upgrade op GPT-6 Sol: sterk op agentische coding, computer use en professioneel werk, tegen ~20% van de standaard GPT-6 Astra prijs. Token generatie is 6–8× sneller in Codex en de API.
- **Dots** – OpenAI's nieuwe agentische avatar – werkt hardware-onafhankelijk en voert continu achtergrondtaken uit op basis van gebruikersdoelen. Dit is geen chatbot-upgrade maar een serieuze stap naar persistent agentisch gedrag.
- **Agents API (public beta)** biedt hosted execution, memory, tools en multi-agent ondersteuning. De **Decisions API** (aangedreven door GPT-6 Luna) maakt real-time classificatie en routing binnen agentische workflows mogelijk.

**Google** introduceerde Gemini 4 Argon voor complexe probleemoplossing, met verbeterde stemtools en app-integratie. Na de Google I/O aankondigingen in mei nadert Gemini 4 nu brede enterprise beschikbaarheid.

**Microsoft** lanceerde drie eigen AI-modellen die tot 89% goedkoper zouden zijn dan OpenAI-modellen – een duidelijk signaal dat Microsoft minder afhankelijk wil zijn van zijn voormalige partner.

*Bron: [OpenAI DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/), [TechCrunch – OpenAI Dots](https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/), [VentureBeat – Microsoft modellen](https://venturebeat.com/infrastructure/microsoft-launches-new-in-house-ai-models-it-says-cut-costs-up-to-89-versus-openai)*

## 🏛️ Governance & Ethiek

**EU AI Act-handhaving is nu actief.** Vanaf 2 augustus 2026 handhaven de AI Office (Europese Commissie) en nationale autoriteiten de bepalingen van het AI Act:

- Chatbots en interactieve AI-systemen **moeten zichzelf als AI identificeren**
- Deepfakes en AI-gegenereerde content moeten machine-leesbaar worden gemarkeerd
- De AI Office heeft bevoegdheid om technische documentatie op te vragen, modellen te evalueren en corrigerende maatregelen op te leggen
- Sancties voor de zwaarste overtredingen: tot **€35 miljoen of 7% van de wereldwijde jaaromzet**

Voor providers van General Purpose AI models (zoals OpenAI, Google, Anthropic) gelden directe verplichtingen vanuit de AI Office. Nationale autoriteiten zijn verantwoordelijk voor AI-systemen in hun jurisdictie.

*Bron: [EU AI Act – enforcement framework](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act), [Implementatietijdlijn AI Act](https://artificialintelligenceact.eu/implementation-timeline/)*

## 🔐 Security & Risk

De security-situatie rondom agentische AI is zorgwekkend:

- **88% van enterprises** had het afgelopen jaar een AI-agent-beveiligingsincident; **97%** verwacht een materieel incident de komende 12 maanden
- **Prompt injection** blijft de #1 aanvalsvector (OWASP LLM01): in 2025 werden al meer dan 90 organisaties getroffen waarbij credentials en crypto werden gestolen via geïnjecteerde prompts in legitieme AI-tools
- Slechts **21% van enterprises** heeft runtime-zichtbaarheid op wat hun agents doen – een fundamenteel governance-gat
- Nieuwe dreigingscategorieën per OWASP Agentic AI Top 10: goal hijacking, tool misuse, memory poisoning, rogue agents en insecure inter-agent communicatie
- Ondertussen gaat slechts **6% van securitybudgetten** naar AI-agentrisico's

*Bron: [VentureBeat – 88% enterprise AI incidents](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds), [VentureBeat – prompt injection](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)*

## 📈 Markt & Adoptie

**De agent-belofte vs. de agent-realiteit:**

- Twee derde van organisaties gebruikt AI-agents in productie, maar **slechts 29% van die agents communiceert onderling** – ze zijn grotendeels gesilo'd
- **30% van bedrijven** zag productiviteit dalen na invoering van agentische AI door lage kwaliteit en misleidende output
- Gartner verwacht dat meer dan **40% van huidige agentische AI-projecten de 2028 niet haalt** vanwege kostenstijging, onduidelijke businesswaarde en onvoldoende risicobeheersing
- De werkelijke bottleneck is infrastructuur: 47% noemt integratie/governance als voornaamste frictie, 37% noemt stateless infrastructuur die te fragiel is voor productie

**Marktverschuivingen:**

- OpenAI verbreekt exclusiviteit met Microsoft en verkoopt nu via AWS en Google Cloud – dit opent de multi-cloud AI-markt fundamenteel
- Microsoft lanceerde Frontier Company, een outcome-gedreven organisatie met 6.000 engineers die samen met klanten AI implementeren
- Microsoft ziet een vervijfvoudiging van klanten die modellen van meerdere providers combineren

*Bron: [CIO Dive – agents siloed](https://www.ciodive.com/news/agents-remain-disconnected-enterprises-double-down/831317/), [VentureBeat – agentic reckoning](https://venturebeat.com/resources/the-agentic-reckoning-enterprise-ai-organizations-have-a-runtime-problem-not-a-model-problem), [VentureBeat – OpenAI/Microsoft deal](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)*

## 💡 Ctac-relevantie

**Agentische AI vraagt om een volwassener propositie.** De marktdata van vandaag bevestigt wat veel klanten van Ctac ook ervaren: de technologie is beschikbaar, maar de weg van pilot naar productie is hobbelig. De 30% die productiviteitsverlies rapporteert, is geen teken van slechte AI – het is een teken van onderschatte implementatiecomplexiteit. Dit is een directe kans voor Ctac: positioneer je niet als model-leverancier, maar als de partij die de governance-, integratie- en infrastructuurlaag op orde brengt.

**EU AI Act-naleving wordt urgent voor klanten.** Met actieve handhaving en serieuze boetes worden compliance-vraagstukken nu boardroom-thema's. Klanten in zorg, overheid en finance lopen het meeste risico. Een beknopte AI Act-quickscan als instapproduct voor deze sectoren kan nu relevant zijn.

**Security bij agentische implementaties is een blinde vlek.** Vrijwel geen enkele enterprise heeft voldoende visibility op agent-gedrag. Dit opent een concrete advies- en implementatiehoek: agent monitoring, prompt-injection mitigatie en governance-frameworks als onderdeel van Ctac's AI-proposities.

**OpenAI's multi-cloud vrijheid** verlaagt de drempel voor klanten om met OpenAI te werken zonder vendor lock-in bij Microsoft – wat het gesprek over AI-strategie makkelijker maakt voor klanten die Azure terughoudend zijn.

## 📚 Bronnen & verder lezen

- [OpenAI DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/)
- [TechCrunch – OpenAI lanceert Dots](https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/)
- [VentureBeat – Microsoft eigen AI-modellen](https://venturebeat.com/infrastructure/microsoft-launches-new-in-house-ai-models-it-says-cut-costs-up-to-89-versus-openai)
- [VentureBeat – OpenAI/Microsoft exclusiviteit verbroken](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)
- [EU AI Act – handhavingskader](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [VentureBeat – 88% enterprises met AI agent-beveiligingsincidenten](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds)
- [VentureBeat – prompt injection](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [CIO Dive – agents remain siloed](https://www.ciodive.com/news/agents-remain-disconnected-enterprises-double-down/831317/)
- [VentureBeat – The Agentic Reckoning](https://venturebeat.com/resources/the-agentic-reckoning-enterprise-ai-organizations-have-a-runtime-problem-not-a-model-problem)
- [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Google AI updates september 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-september-2026/)
