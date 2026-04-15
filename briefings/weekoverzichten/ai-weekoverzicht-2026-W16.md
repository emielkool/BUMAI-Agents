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
> Briefings voor donderdag 16 en vrijdag 17 april waren niet beschikbaar op moment van opstellen.

---

## 🔑 Weekhighlights

- **Anthropic Mythos: de grens van dual-use AI is bereikt.** Het krachtigste model dat Anthropic ooit bouwde, wordt bewust achtergehouden omdat het zelfstandig duizenden zero-day kwetsbaarheden vond in alle grote OS'en en browsers – inclusief bugs die 27 jaar menselijke review overleefden. Project Glasswing (12 partners, $100M) is het beheersmechanisme.
- **EU AI Act: nog 3,5 maand tot volledige toepassing.** Per 2 augustus 2026 geldt de verordening volledig. Op 8 april publiceerde de Europese Commissie nieuwe richtlijnen voor de definitie van een AI-systeem – een concreet ankerpunt voor compliance-trajecten die nu gestart moeten worden.
- **Open-source AI is serieuze concurrent geworden.** Google Gemma 4 (#3 wereldwijd op Arena-leaderboard, Apache 2) en China's GLM-5 (#1 open gewichtsmodel, MIT-licentie, getraind op Huawei-chips) tonen dat state-of-the-art performance niet langer exclusief is voor gesloten API-providers.
- **Microsoft positioneert zich als eigenstandig AI-lab.** De drie MAI-foundational modellen (tekst, spraak, beeld) via Microsoft Foundry markeren een directe concurrentiestelling richting OpenAI – strategisch relevant voor enterprise-klanten op het Microsoft-platform.
- **Enterprise AI-adoptie explodeert, maar pilot → productie blijft hét knelpunt.** AI-softwarespend groeit bijna 60% YoY naar $452 miljard; 67% van Nederlandse bedrijven gebruikt AI (was 34% in 2023). Toch zit twee derde van organisaties nog vast in de experimenteerfase.

---

## 🧠 Technologie & Modellen – Weekpatroon

De week liet twee parallelle bewegingen zien die op gespannen voet staan. Aan de ene kant versnelt de frontier-race: Mythos, GPT-5.4/5.5, Gemini 3.1 Pro en Grok 4.20 leggen de lat steeds hoger op specialistische taken. Aan de andere kant haalt open-source serieus in: Gemma 4 en GLM-5 bewijzen dat enterprise-niveau performance nu beschikbaar is zonder afhankelijkheid van gesloten API-providers.

De meest structurele verschuiving is de standaardisering van agent-infrastructuur. MCP is overgedragen aan de Agentic AI Foundation (OpenAI, Anthropic, Block); A2A-interoperabiliteit wordt mainstream (Microsoft + Google); multi-agent architecturen (Meta Muse Spark, Grok 4.20) worden de verwachte baseline. Het tijdperk van de single-model-call eindigt; gespecialiseerde, samenwerkende modellen worden de norm.

---

## 🏛️ Governance & Ethiek – Weekpatroon

De EU AI Act-deadline van 2 augustus domineerde het governance-beeld drie dagen op rij – een signaal dat de urgentie nu breed wordt gevoeld. De Commissie publiceerde op 8 april praktische richtlijnen voor AI-systeemclassificatie; komende weken volgen richtlijnen over high-risk-classificatie, Art. 50-transparantievereisten en incidentmeldplicht.

Parallel lopen de EU Digital Omnibus-onderhandelingen (triloog 28 april), die de AI Act-tijdlijn deels kunnen bijsturen. Nationaal: Nederland investeert €700M+ (Dutch AI Factory + investeringsfonds) en verankert AI in het coalitieakkoord 2026–2030. Project Glasswing illustreert een alternatieve governance-vorm: private sectorcoördinatie die de-facto industriestandaarden stelt vóórdat regelgeving bijhoudt. Het is ook een voorzichtig signaal dat zelfregulering door labs zijn grenzen bereikt.

---

## 🔐 Security & Risk – Weekpatroon

Prompt injection is structureel onoplosbaar geworden – dat is de consensus na drie opeenvolgende dagen berichten. OpenAI erkende het formeel; slechts 34,7% van organisaties met actieve AI-agents heeft adequate detectiecapaciteit. De LangChain/LangGraph CVE's (drie kwetsbaarheden, gepubliceerd maart 2026) raken direct teams die RAG-pipelines of agenten bouwen op deze populaire frameworks.

De escalatie ten opzichte van voorgaande weken zit in het dual-use karakter: Mythos-niveau capaciteiten voor kwetsbaarheidsdetectie zijn nu bewezen schaalbaar. De "promptware kill chain" (Schneier) biedt aanvallers een gestructureerde aanpak op LLM-gebaseerde agents. Het aanvalsoppervlak groeit per externe databron die een agent leest – en agenten lezen steeds meer.

---

## 📈 Markt & Adoptie – Weekpatroon

De enterprise AI-markt beweegt langs twee assen: enorme spend-groei (Gartner: $2 biljoen totaal AI-markt; AI-software $452 miljard, +60% YoY) én structurele adoptieknelpunten. Salesforce voegde +6.000 enterprise klanten toe in drie maanden terwijl de bubble-discussie voortgaat – een signaal dat agentic AI voldoende concrete waarde levert om koopbeslissingen te drijven. De cloudcijfers bevestigen dit (Azure +39%, Google Cloud +50% YoY in Q4 2025).

NVIDIA's enterprise agent-platform (Adobe, SAP, Salesforce als early adopters) en A2A-interoperabiliteit verlagen de technische drempel voor agentic AI aanzienlijk bij enterprise. Voor dienstverleners verschuift hierdoor de waarde: niet meer de modelkeuze, maar integratie, security en change management bepalen het verschil.

---

## 💡 Ctac-relevantie – Weekperspectief

- **Start EU AI Act compliance-gesprekken deze week, niet volgende maand.** De deadline van 2 augustus is 3,5 maand weg. Klanten in overheid, zorg en finance zijn grotendeels niet klaar. De nieuwe EC-richtlijnen van 8 april zijn een uitstekend gesprekshaakje: een readiness assessment of risicoklassificatie-sessie is direct inzetbaar als propositie. Wie in mei begint, heeft net genoeg tijd; wie in juni begint niet meer.

- **Positioneer Ctac expliciet als pilot-naar-productie partner.** Twee derde van Nederlandse bedrijven zit vast in de experimenteerfase. De bottlenecks zijn data-architectuur, integratie, monitoring en security – precies het speelveld van een custom software- en transformatiepartner. Dit onderscheidt Ctac van hyperscaler-resellers die infrastructuur leveren maar het implementatiewerk overlaten aan de klant.

- **Security by design is vanaf nu een niet-onderhandelbare baseline in elk AI-traject.** Prompt injection is structureel onoplosbaar; LangChain-kwetsbaarheden raken actieve projecten; Mythos-niveau dual-use capaciteiten zijn bewezen schaalbaar. Elke agentic implementatie die Ctac uitvoert, moet een securityarchitectuur hebben vanaf dag één – zowel als kwaliteitsargument intern als als verkoopargument richting klanten.

- **Open-source en soevereine AI als propositie voor datakritische klanten.** Gemma 4 (Apache 2) en GLM-5 (MIT) maken on-premise deployment van top-3 modellen realistisch. Voor klanten in overheid of finance met soevereiniteitsvereisten is dit een concreet alternatief voor cloudgebaseerde API's. Technische kennis van lokale inference-stacks (vLLM, Ollama, llama.cpp) gecombineerd met klantintegratie is een differentiator voor de AI-unit.

---

## 📚 Alle bronnen van de week

**Technologie & Modellen**
- [Google Gemma 4 – blog.google](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
- [Gemma 4 op Hugging Face](https://huggingface.co/blog/gemma4)
- [GLM-5 open source frontier model – Hugging Face blog](https://huggingface.co/blog/mlabonne/glm-5)
- [Anthropic Mythos Preview – TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [Mythos: te gevaarlijk voor release – Axios](https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks)
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
- [AI adoptie Benelux – ictmagazine.nl](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)
- [Belgische Elle met AI-nepjournalisten – NOS](https://nos.nl/artikel/2572829-belgische-elle-werkte-stiekem-met-ai-boven-artikelen-stonden-nepjournalisten)
- [NOS: AI in militaire beslissingen](https://nos.nl/nieuwsuur/artikel/2609142-zorgen-over-gebruik-van-ai-in-oorlogen-menselijke-afweging-blijft-nodig)

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
- [NVIDIA enterprise AI agent platform – VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Salesforce +6.000 enterprise klanten – VentureBeat](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000)
- [AI adoptie Nederland 2026 – Searchlab NL](https://searchlab.nl/blog/ai-adoptie-nederland-2026)
- [Microsoft en Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Enterprise agentic AI landscape 2026 – Kai Waehner](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)
- [OpenAI COO over enterprise adoptie – TechCrunch](https://techcrunch.com/2026/02/24/openai-coo-says-we-have-not-yet-really-seen-ai-penetrate-enterprise-business-processes/)
- [Cloud infrastructure Q4 2025 – Omdia](https://omdia.tech.informa.com/pr/2026/mar/global-cloud-infrastructure-spending-rose-29percent-in-q4-2025-as-hyperscalers-scaled-ai-infrastructure-investment)
