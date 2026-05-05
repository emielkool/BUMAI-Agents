---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W16
Datum: 2026-04-17
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 16, 2026

> Synthese van de dagbriefings van 13 april t/m 15 april 2026.

---

## 🏆 Weekhighlights

1. **Anthropic Mythos: de grens van dual-use AI is formeel bereikt.** Het krachtigste model dat Anthropic ooit bouwde, wordt bewust achtergehouden: het vond zelfstandig duizenden zero-day kwetsbaarheden in alle grote besturingssystemen en browsers – waaronder CVE-2026-4747, een 17 jaar oud RCE-lek in FreeBSD. Project Glasswing (12 industriepartners, $100M) is het beheersmechanisme. Dit is geen hype; het is een bewezen dual-use drempeloverschrijding.

2. **EU AI Act: de deadline van 2 augustus is reëel en urgent.** Nog 3,5 maand. De Europese Commissie publiceerde op 8 april concrete richtlijnen voor de definitie van AI-systemen; komende weken volgen richtlijnen over hoog-risico classificatie, Art. 50-transparantievereisten en incidentmeldplicht. Klanten in overheid, zorg en finance zijn grotendeels niet klaar. Wie nu begint, haalt het nog net; wie in juni begint niet meer.

3. **Open-source AI haalt de frontier in.** Google Gemma 4 (#3 wereldwijd op Arena-leaderboard, Apache 2-licentie, 31B dense model) en China's GLM-5 (#1 open gewichtsmodel op LMArena, MIT-licentie, volledig getraind op Huawei Ascend-chips) tonen dat enterprise-niveau performance niet langer exclusief beschikbaar is via gesloten API-providers. On-premise en soevereine deployment van topmodellen is nu realistisch.

4. **Microsoft herpositioneert zichzelf als eigenstandig AI-lab.** MAI-Transcribe-1, MAI-Voice-1 en MAI-Image-2 zijn via Microsoft Foundry beschikbaar – eigengebouwde foundation modellen, direct competitief met OpenAI en Google. Gecombineerd met de committering aan Google's Agent2Agent-protocol (A2A) voor multi-agent interoperabiliteit vormt dit een infrastructureel keerpunt voor enterprise-klanten op het Microsoft-platform.

5. **Enterprise AI-adoptie explodeert, maar pilot→productie blijft structureel vastgelopen.** AI-softwarespend groeit 60% YoY naar $452 miljard. In Nederland gebruikt 67% van bedrijven AI (was 34% in 2023). Salesforce voegde +6.000 enterprise klanten toe in drie maanden. Toch zit twee derde van organisaties vast in de experimenteerfase. De bottlenecks zijn data-architectuur, integratie, monitoring en security – precies het speelveld van een implementatiepartner.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De week liet twee parallelle – en op gespannen voet staande – bewegingen zien. Aan de frontier-kant: Mythos, nieuwe GPT- en Gemini-versies in de pijplijn, en Meta's Muse Spark (multi-agent reasoning, "Contemplating"-modus) leggen de lat steeds hoger op specialistische taken. Aan de open-source kant: Gemma 4 en GLM-5 bewijzen dat state-of-the-art performance beschikbaar is zonder afhankelijkheid van gesloten aanbieders – en zonder NVIDIA-hardware in het geval van GLM-5, wat geopolitiek relevant is.

De meest structurele verschuiving is de standaardisering van agent-infrastructuur. MCP is overgedragen aan de Agentic AI Foundation (Anthropic, Block, OpenAI) en heeft met 10.000+ actieve publieke servers de status van de facto connector-standaard bereikt. A2A-interoperabiliteit (Microsoft + Google) wordt mainstream. Multi-agent architecturen zijn geen experimenten meer – ze worden de verwachte baseline voor enterprise AI-deployments. Het tijdperk van de single-model-call als architectuurparadigma nadert zijn einde.

### 🏛️ Governance & Beleid

De EU AI Act-deadline van 2 augustus domineerde het governance-beeld drie dagen op rij. De Commissie publiceerde op 8 april de eerste praktische richtlijnen voor AI-systeemclassificatie; komende weken volgen richtlijnen over hoog-risico classificatie, Art. 50-transparantievereisten en incidentmeldplicht. Het EU Digital Omnibus-triloogproces (28 april) kan de tijdlijn deels bijsturen maar schept geen excuus voor uitstel.

Nationaal heeft Nederland stevige AI-ambities verankerd: €200M Dutch AI Factory, €500M investeringsfonds, en AI is onderdeel van het coalitieakkoord 2026–2030. Opvallend is de discussie rond AI in militaire besluitvorming (Maven Smart System bij Defensie) – een governance-vraagstuk dat het publieke debat beïnvloedt en ook enterprise-klanten in veiligheidsgevoelige sectoren raakt.

Project Glasswing illustreert een alternatieve governance-vorm: private sectorcoördinatie die de facto industriestandaarden stelt vóórdat regelgeving bijhoudt. Het is ook een voorzichtig signaal dat zelfregulering door labs zijn grenzen bereikt heeft.

### 🔐 Security & Risk

Prompt injection is structureel onoplosbaar – dat is de consensus na drie opeenvolgende dagen berichten. OpenAI erkende het formeel: "likely to never be fully solved". Slechts 34,7% van organisaties met actieve AI-agents heeft adequate detectiecapaciteit. PoisonedRAG-onderzoek toont 90% aanvalssucces bij RAG-vergiftiging met slechts vijf geïnjecteerde documenten. Bruce Schneier's "promptware kill chain" beschrijft een gestructureerde aanvalsmethode die het risico operationeel maakt – niet langer theoretisch.

De LangChain/LangGraph CVE's (drie kwetsbaarheden, gepubliceerd maart 2026) raken direct teams die RAG-pipelines of agenten bouwen op deze populaire frameworks: aanvallers kunnen toegang krijgen tot bestandssystemen, omgevingsvariabelen (API-keys) en conversatiegeschiedenissen.

De escalatie ten opzichte van voorgaande weken zit in het dual-use karakter van Mythos: AI-gebaseerde offensieve capaciteiten voor kwetsbaarheidsdetectie zijn nu bewezen schaalbaar. Het aanvalsoppervlak groeit per externe databron die een agent leest – en autonome agenten lezen steeds meer.

### 📈 Markt & Adoptie

De enterprise AI-markt beweegt langs twee assen: enorme spend-groei (Gartner: $2 biljoen totale AI-markt; AI-software $452 miljard, +60% YoY) én structurele adoptieknelpunten. Salesforce voegde +6.000 enterprise klanten toe in drie maanden terwijl de bubble-discussie voortgaat – een signaal dat agentic AI voldoende concrete waarde levert om koopbeslissingen te drijven. Cloudcijfers bevestigen dit: Azure +39%, Google Cloud +50% YoY in Q4 2025.

NVIDIA's enterprise agent-platform (Adobe, SAP, Salesforce als early adopters bij GTC 2026) en A2A-interoperabiliteit verlagen de technische drempel voor agentic AI aanzienlijk bij enterprise. Voor dienstverleners verschuift hierdoor de waarde: niet meer de modelkeuze, maar integratie, security en change management bepalen het verschil. Meer dan 60% van beslissers verwacht >100% ROI op AI-agenten (gemiddeld 171%) – tegelijk geven C-suite executives toe dat echte transformatie nog jaren vergt. Dat gat is een structurele positie voor implementatiepartners.

---

## 💼 Ctac-weekperspectief

- **Start EU AI Act compliance-gesprekken deze week, niet volgende maand.** De deadline van 2 augustus is 3,5 maand weg. Klanten in overheid, zorg en finance zijn grotendeels niet klaar. De nieuwe EC-richtlijnen van 8 april (definitie AI-systeem) zijn een uitstekend gesprekshaakje: een readiness assessment of risicoklassificatie-sessie is direct inzetbaar als propositie. Concrete aanpak: inventariseer welke klantoplossingen onder de AI Act vallen, voer een risicoklassificatie uit, en stel documentatievereisten op per systeem.

- **Positioneer Ctac expliciet als pilot-naar-productie partner.** Twee derde van Nederlandse bedrijven zit vast in de experimenteerfase. De bottlenecks zijn data-architectuur, integratie, monitoring en security – precies het speelveld van een custom software- en transformatiepartner. Dit onderscheidt Ctac structureel van hyperscaler-resellers die infrastructuur leveren maar het implementatiewerk bij de klant laten. Aandachtspunt voor de propositie: benoem expliciet wat Ctac doet ná de pilot.

- **Security by design is een niet-onderhandelbare baseline in elk AI-traject.** Prompt injection is structureel onoplosbaar; LangChain-kwetsbaarheden raken actieve projecten direct; Mythos-niveau dual-use capaciteiten zijn bewezen schaalbaar. Elke agentic implementatie die Ctac uitvoert, moet een securityarchitectuur hebben vanaf dag één – zowel als intern kwaliteitsargument als als verkoopargument richting klanten die vragen: "Hoe veilig is dit eigenlijk?"

- **Open-source en soevereine AI als propositie voor datakritische klanten.** Gemma 4 (Apache 2) en GLM-5 (MIT) maken on-premise deployment van top-3 modellen realistisch. Voor klanten in overheid of finance met soevereiniteitsvereisten is dit een concreet alternatief voor cloudgebaseerde API's. Kennis van lokale inference-stacks (vLLM, Ollama, llama.cpp) gecombineerd met klantintegratie is een directe differentiator voor de AI-unit.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Google Gemma 4 – blog.google](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
- [Gemma 4 op Hugging Face](https://huggingface.co/blog/gemma4)
- [GLM-5 open source frontier model – Hugging Face blog](https://huggingface.co/blog/mlabonne/glm-5)
- [Anthropic Mythos Preview – TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [Mythos: te gevaarlijk voor release – Axios](https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks)
- [Mythos: bescherming of positionering? – TechCrunch](https://techcrunch.com/2026/04/09/is-anthropic-limiting-the-release-of-mythos-to-protect-the-internet-or-anthropic/)
- [Trump officials en Mythos voor banken – TechCrunch](https://techcrunch.com/2026/04/12/trump-officials-may-be-encouraging-banks-to-test-anthropics-mythos-model/)
- [Microsoft drie nieuwe MAI-modellen – TechCrunch](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)
- [Microsoft MAI-modellen – VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [Meta Muse Spark – TechCrunch](https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/)
- [MCP overgedragen aan Agentic AI Foundation – Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [LLM Stats – AI model updates april 2026](https://llm-stats.com/ai-news)

**Governance & Beleid**
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act volgende stappen](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/)
- [EC richtlijnen AI-definitie – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [EU Digital Omnibus en AI Act tijdlijn – OneTrust](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/)
- [AI Act impact NL/BE – cryptobenelux.com](https://cryptobenelux.com/kunstmatige-intelligentie/ai-act-raakt-in-2026-vooral-hr-onderwijs-en-overheid-in-nederland-en-belgie)
- [AIC4NL vooruitblik 2026](https://aic4nl.nl/en/aic4nl/vooruitblik-2026-intensivering-van-de-uitvoering/)
- [NOS: AI in militaire beslissingen](https://nos.nl/nieuwsuur/artikel/2609142-zorgen-over-gebruik-van-ai-in-oorlogen-menselijke-afweging-blijft-nodig)
- [Belgische Elle met AI-nepjournalisten – NOS](https://nos.nl/artikel/2572829-belgische-elle-werkte-stiekem-met-ai-boven-artikelen-stonden-nepjournalisten)

**Security & Risk**
- [Anthropic Project Glasswing](https://www.anthropic.com/project/glasswing)
- [Claude Mythos vindt duizenden zero-days – The Hacker News](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
- [Mythos en het detectieplafond – VentureBeat](https://venturebeat.com/security/mythos-detection-ceiling-security-teams-new-playbook)
- [Prompt injection: here to stay – VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [Anthropic publiceert prompt injection cijfers – VentureBeat](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)
- [LangChain/LangGraph kwetsbaarheden – The Hacker News](https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html)
- [Schneier: Promptware Kill Chain](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)
- [AI security 2026 – airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIS rapport prompt injection](https://www.cisecurity.org/about-us/media/press-release/new-cis-report-warns-prompt-injection-attacks-pose-growing-risk-to-generative-ai)

**Markt & Adoptie**
- [Enterprise AI-spend 2026 – CIO Dive](https://www.ciodive.com/news/what-to-expect-from-the-ai-boom-this-year/809783/)
- [Agentic AI ROI-verwachtingen – CIO Dive](https://www.ciodive.com/news/enterprise-agentic-AI-adoption-ROI-expectations-PagerDuty/744265/)
- [Microsoft commits to A2A interoperabiliteit – CIO Dive](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [Microsoft en Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [NVIDIA enterprise AI agent platform – VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Salesforce +6.000 enterprise klanten – VentureBeat](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000)
- [AI adoptie Nederland 2026 – Searchlab NL](https://searchlab.nl/blog/ai-adoptie-nederland-2026)
- [AI adoptie Benelux – ictmagazine.nl](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)
- [Enterprise agentic AI landscape 2026 – Kai Waehner](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)
- [OpenAI COO over enterprise adoptie – TechCrunch](https://techcrunch.com/2026/02/24/openai-coo-says-we-have-not-yet-really-seen-ai-penetrate-enterprise-business-processes/)
- [Cloud infrastructure Q4 2025 – Omdia](https://omdia.tech.informa.com/pr/2026/mar/global-cloud-infrastructure-spending-rose-29percent-in-q4-2025-as-hyperscalers-scaled-ai-infrastructure-investment)

---

### Donderdag 16 april

→ Dagbriefing: [ai-briefing-2026-04-16.md](../ai-briefing-2026-04-16.md)

**Highlights:**
- **Anthropic Mythos & Project Glasswing**: het meest capabele model ooit vond autonoom duizenden zero-day kwetsbaarheden in alle grote OS'en en browsers; 12 grote techpartners (waaronder Microsoft, Google, Apple) krijgen beperkt toegang voor defensieve security. De bewust gelimiteerde release is een waarschuwing: aanvallers krijgen vergelijkbare modellen onvermijdelijk ook.
- **Stanford AI Index 2026**: SWE-bench codeerscores stegen van 60% naar ~100% in één jaar; 88% van organisaties gebruikt AI; de kloof VS–China slonk naar 2,7%. Tegelijk daalde de Foundation Model Transparency Index van 58 naar 40 — frontier labs worden minder open.
- **Open-weight concurrentie en Microsoft-onafhankelijkheid**: Arcee AI Trinity (400B, Apache) en Zhipu GLM-4.6V (106B) dagen Meta's Llama uit; Microsoft lanceert eigen MAI-modellen om de OpenAI-afhankelijkheid te verminderen. Shadow AI wordt een serieus enterprise-risico naarmate autonome agents de norm worden.

**Ctac-relevantie van de dag:** Project Glasswing maakt AI voor defensieve cybersecurity een concreet klantgesprek — met name voor finance en overheid. Tegelijk schept de dalende modelltransparantie een argument voor sovereign/private AI-deployment bij compliance-kritische klanten.

---
