---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-26
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 26 mei 2026

## 🔑 Highlights van de dag

- **Google Gemini 3.5 + Agentic Data Cloud** – Google heeft Gemini 3.5 gelanceerd met een focus op agentic en coding-taken, gekoppeld aan de Agentic Data Cloud-architectuur die legacy enterprise data omzet naar reasoning engines. Dit is de meest serieuze uitdager van OpenAI's enterprise-propositie tot nu toe.
- **EU AI Act bijna volledig van kracht** – Op 7 mei is een politiek akkoord bereikt over de "AI Omnibus" (vereenvoudigingsamendement). De volledige AI Act wordt van kracht op 2 augustus 2026; transparantierichtlijnen zijn nog in consultatie.
- **Prompt injection raakt drie grote coding tools tegelijk** – Een gecoördineerde aanval trof Claude Code, Gemini CLI en GitHub Copilot simultaan in april. Microsoft Copilot Studio had al een patch (CVE-2026-21520), maar data-exfiltratie vond toch plaats.
- **Anthropic haalt $30 miljard op, waardering >$900 miljard** – Met 34,4% marktaandeel in betaalde AI-abonnementen in de VS is Anthropic nu marktleider boven OpenAI (32,3%). De financieringssnelheid is opmerkelijk: ARR verdubbelde in twaalf weken.
- **Enterprises vastgelopen in pilot-fase** – Twee derde van de bedrijven zit nog in experimenten en slaagt er niet in AI naar productie te brengen. Microsoft en Google richten zich actief op deze "pilot-to-production" kloof.

---

## 🧠 Technologie & Modellen

**Google Gemini 3.5** is beschikbaar met de Flash-variant als primaire keuze voor agentic taken en complexe long-horizon workflows. Google positioneert dit model als antwoord op OpenAI's o3-serie en Claude 3.7. Gemini 3.1 Pro is tegelijkertijd in preview beschikbaar voor enterprise-gebruikers. ([blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/))

**OpenAI GPT-5.5 Instant** verving eerder deze maand GPT-5.3 als standaardmodel in ChatGPT, met verbeterde betrouwbaarheid in gevoelige domeinen (recht, medisch, finance) bij behoud van lage latency. Aanvullend lanceerde OpenAI het **Frontier** enterprise-platform voor gecentraliseerd agent-beheer. ([TechCrunch](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/))

**Stability Audio 3.0** genereert professionele muziek tot zes minuten lang in vier modelgroottes. Niche voor creative-sector klanten, maar toont wel hoe snel multimodale generatie rijpt. ([TechCrunch](https://techcrunch.com/2026/05/20/stability-ai-release-a-new-audio-model-that-can-create-six-minute-songs/))

---

## 🏛️ Governance & Ethiek

De **AI Omnibus** – een vereenvoudigingsamendement op de EU AI Act – bereikte op 7 mei een politiek akkoord. Kern: de bevoegdheden van het AI Office worden versterkt en het toezicht op General Purpose AI (GPAI)-modellen wordt gecentraliseerd, waardoor governance-fragmentatie tussen lidstaten wordt teruggedrongen. ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/))

Op **2 augustus 2026** wordt de volledige AI Act van kracht. De Europese Commissie heeft consultaties geopend over conceptrichtlijnen voor transparantieverplichtingen en de classificatie van hoog-risico AI-systemen. Voor organisaties die nog niet klaar zijn, is dat geen zachte deadline meer. ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines))

**NL/BE context:** NOS en Computable rapporteren over toenemende maatschappelijke weerstand en het debat over AI op de arbeidsmarkt in Nederland. In België werd Elle betrapt op het inzetten van fictieve AI-journalisten – een concreet ethisch incident dat de druk op transparantieregels vergroot. ([NOS](https://nos.nl/artikel/2572829-belgische-elle-werkte-stiekem-met-ai-boven-artikelen-stonden-nepjournalisten))

---

## 🔐 Security & Risk

De meest urgente dreiging van dit moment: **prompt injection tegen agentic coding tools**. Een gecoördineerde aanval trof Claude Code, Gemini CLI en GitHub Copilot tegelijk en lekte secrets via CI-tokens en over-gepermissioneerde agents. VentureBeat meldt dat het fundamentele probleem structureel is: modellen kunnen instructies niet betrouwbaar onderscheiden van data. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**Microsoft Copilot Studio** ontving een patch voor CVE-2026-21520 (CVSS 7.5), maar onderzoekers toonden aan dat data-exfiltratie desondanks plaatsvond. Succespercentages van adaptieve aanvalstechnieken liggen boven de 85% bij productiesystemen. OpenAI erkent nu publiekelijk dat prompt injection "structureel niet volledig oplosbaar" is – vergelijkbaar met social engineering op het web. ([VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay), [airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

---

## 📈 Markt & Adoptie

**Microsoft** rapporteert een AI-omzet van $37 miljard op jaarbasis (+123% YoY). Tegelijkertijd erkent het bedrijf in een uitgebreide blog dat de meerderheid van enterprise-klanten vastzit in pilots en dat executie – niet technologie – het nieuwe onderscheidende vermogen is. Agent 365 is uit preview, en Microsoft verwacht in juni 2026 18 agenttypen te ondersteunen. ([blogs.microsoft.com](https://blogs.microsoft.com/blog/2026/05/21/from-ai-pilots-to-enterprise-impact-why-execution-is-the-new-differentiator/))

**Google** introduceert de Agentic Data Cloud op Google Cloud Next '26: een AI-native datalaag die legacy-platformen omzet naar reasoning-engines. Gecombineerd met Gemini 3.5 positioneert Google zich sterk voor de volgende enterprise-adoptiefase. ([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))

**Cloud-capex** stijgt naar verwachting met 40% in 2026 naar $600 miljard. De vijf grote hyperscalers gaven in 2025 al $437 miljard gecombineerd uit. ([CIO Dive](https://www.ciodive.com/news/ai-boost-cloud-spending/810399/))

**Marktconcentratie:** Anthropic heeft 34,4% van de betaalde AI-abonnementen in de VS, net voor OpenAI (32,3%). Google staat op slechts 4,5%. ([Axios](https://www.axios.com/2026/05/21/google-ai-anthropic-openai-war))

---

## 💡 Ctac-relevantie

**Pilot-to-production is de nieuwe battleground** – en dit is precies het gat dat Ctac kan vullen. Twee derde van enterprise-klanten lukt het niet AI van experiment naar productie te brengen. Ctac kan zich positioneren als de implementatie-partner die wél levert: niet alleen het model kiezen, maar integreren, testen, governal inrichten en opschalen. De aankondiging van Microsoft rond "execution as differentiator" bevestigt dit als het centrale thema in enterprise AI dit jaar.

**EU AI Act deadline augustus 2026** – Klanten in sectoren als overheid, zorg en finance moeten nu concreet actie ondernemen. Compliance-scanning, risicoklassificatie van bestaande systemen en documentatieverplichtingen zijn directe advies- en implementatieopdrachten. De AI Omnibus maakt GPAI-governance duidelijker, maar verkleint niet de tijdsdruk.

**Prompt injection als enterprise risico** – Het simultane lek in Claude Code, Gemini CLI en Copilot is een wake-up call voor elke organisatie die coding agents inzet. Ctac's AI engineer-team doet er goed aan de eigen toolchain te auditen op CI-tokenbeheer en agent-permissies, én dit als adviescomponent aan te bieden bij klanttrajecten.

**Anthropic's marktpositie** – Met de $30 miljard ronde en marktleiderpositie is Anthropic geen nichespeler meer. Als Ctac werkt met Claude (via API of Claude Code), is het zinvol dit intern te formaliseren als strategische keuze, inclusief het contractuele kader richting klanten.

---

## 📚 Bronnen & verder lezen

- [Google Gemini 3.5 – blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)
- [OpenAI GPT-5.5 Instant – TechCrunch](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/)
- [Stability Audio 3.0 – TechCrunch](https://techcrunch.com/2026/05/20/stability-ai-release-a-new-audio-model-that-can-create-six-minute-songs/)
- [EU AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [AI Omnibus consultatie richtlijnen – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Belgische Elle en AI-journalisten – NOS](https://nos.nl/artikel/2572829-belgische-elle-werkte-stiekem-met-ai-boven-artikelen-stonden-nepjournalisten)
- [Prompt injection coding agents lek – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [OpenAI erkent prompt injection structureel – VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [AI Security 2026: Lethal Trifecta – airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Microsoft: van AI pilots naar enterprise impact – blogs.microsoft.com](https://blogs.microsoft.com/blog/2026/05/21/from-ai-pilots-to-enterprise-impact-why-execution-is-the-new-differentiator/)
- [Microsoft Agent 365 uit preview – VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Microsoft vs Google enterprise AI marktpositie – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Google vs Anthropic vs OpenAI AI-race – Axios](https://www.axios.com/2026/05/21/google-ai-anthropic-openai-war)
- [Cloud capex groei 2026 – CIO Dive](https://www.ciodive.com/news/ai-boost-cloud-spending/810399/)
