---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Maand: 2026-04
Periode: 2026-04-01 / 2026-04-30
Status: Afgerond
tags:
  - maandoverzicht
---

# AI Maandoverzicht – April 2026

> Synthese van de dagbriefings en het weekoverzicht van week 16 (beschikbare periode: 12–15 april 2026).
> Briefings voor de overige werkdagen in april waren niet beschikbaar op moment van opstellen.

---

## 🏆 Maandhighlights

1. **Frontier AI bereikt de dual-use grens.** De lancering van Anthropic Claude Mythos is de meest structureel relevante gebeurtenis van april. Het model is zo effectief in het vinden van zero-day kwetsbaarheden — duizenden, in alle grote OS'en en browsers, inclusief CVE's van 17–27 jaar oud — dat Anthropic het bewust achterhoudt. Project Glasswing (twaalf partners, $100M investering) is het beheersmechanisme. Dit is geen marketingzet maar een precedent: voor het eerst erkent een top-lab publiekelijk dat zijn eigen model te gevaarlijk is voor brede inzet. De implicaties voor offensieve en defensieve security zijn structureel.

2. **EU AI Act: het aftellen begint serieus.** Per 2 augustus 2026 — nog iets meer dan drie maanden — is de AI Act volledig van kracht. In april publiceerde de Europese Commissie nieuwe richtlijnen voor de definitie van een AI-systeem; komende maanden volgen richtlijnen over high-risk classificatie, transparantievereisten en incidentmeldplicht. In Nederland en België is het merendeel van publieke sector en zorg nog niet compliance-ready. Organisaties die in mei niet beginnen, hebben in augustus een probleem.

3. **Agentic AI-infrastructuur standaardiseert zich in hoog tempo.** April markeerde twee mijlpalen: MCP is overgedragen aan de Agentic AI Foundation (OpenAI, Anthropic, Block, Linux Foundation), en Microsoft committeerde zich aan Google's A2A-protocol voor agent-interoperabiliteit. Met 10.000+ actieve MCP-servers en public preview van A2A in Azure AI Foundry is dit geen concept meer. Multi-agent architecturen worden de verwachte baseline; de tijdperk van de single-model-call is voorbij.

4. **Open-source AI haalt structureel in op gesloten frontier modellen.** Google Gemma 4 (Apache 2, #3 wereldwijd op Arena-leaderboard) en China's GLM-5 (MIT, #1 open gewichtsmodel, getraind op Huawei-chips zonder NVIDIA) tonen dat state-of-the-art prestaties niet langer exclusief zijn voor betaalde API-providers. Dit heeft directe implicaties voor klanten met data-soevereiniteitsvereisten: on-premise deployment van frontier-kwaliteit is nu technisch en economisch haalbaar.

5. **Enterprise AI-adoptie groeit explosief maar stuit op een productieknelpunt.** AI-softwarespend groeit 60% YoY naar $452 miljard; 67% van Nederlandse bedrijven gebruikt inmiddels AI (was 34% in 2023). Maar twee derde zit nog vast in de experimenteer- en pilotfase. De transitie van pilot naar productie — data-architectuur, integratie, monitoring, security, change management — is het centrale vraagstuk van 2026. Dit is het meest concrete opportuniteitsvenster voor IT-dienstverleners.

---

## 🔍 Dominante thema's en verschuivingen

### 🧠 Technologie & Modellen

April liet een gefragmenteerd maar consistent richtingsgevend modellandschap zien. Aan de frontier-kant versnelde de race: Mythos, GPT-5.4/5.5, Gemini 3.1 Pro en Grok 4.20 leggen de lat steeds hoger op specialistische taken. Microsoft introduceerde bovendien drie eigengebouwde foundational modellen (MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2) via Microsoft Foundry — een directe concurrentiestelling richting eigen partner OpenAI. De strategische onafhankelijkheid van Microsoft neemt toe.

Tegenover deze frontier-dynamiek staat de opmars van open-source. Gemma 4 en GLM-5 maken duidelijk dat top-3 modelprestaties nu beschikbaar zijn zonder afhankelijkheid van gesloten API-providers — inclusief via hardware buiten de NVIDIA-keten. Dit is een structurele verschuiving, geen tijdelijke trend.

De meest systemische beweging in april was echter de standaardisering van agent-infrastructuur: MCP als universele connector, A2A als interoperabiliteitsprotocol. Multi-agent architecturen (Meta Muse Spark, Grok 4.20, OpenAI Aardvark) worden de architecturale verwachting, niet de uitzondering.

### 🏛️ Governance & Beleid

De EU AI Act domineerde het governance-beeld consistent gedurende de gehele beschikbare periode — een signaal dat de urgentie breed wordt gevoeld. De Commissierichtlijnen van 8 april over AI-systeemclassificatie zijn een praktisch ankerpunt; de triloog over de EU Digital Omnibus (28 april) kan de tijdlijn nog deels bijsturen.

Nationaal zette Nederland stevig in: €200M voor de Dutch AI Factory, €500M AI-investeringsfonds, en AI verankerd in het coalitieakkoord 2026–2030. Project Glasswing illustreert een alternatieve governance-vorm — private sectorcoördinatie die de-facto industriestandaarden stelt vóórdat regelgeving bijhoudt. De discussie over AI in militaire besluitvorming (NL Defensie evalueert Maven Smart System) laat zien dat ethische vragen rondom menselijke controle ook de institutionele agenda bereiken.

### 🔐 Security & Risk

April markeerde een kantelpunt in het security-landschap: prompt injection is niet langer een theoretisch risico maar een erkend, structureel onoplosbaar architectuurprobleem. OpenAI erkende formeel dat deterministische garanties niet haalbaar zijn — vergelijkbaar met phishing op het web. Slechts 34,7% van organisaties met actieve AI-agents heeft adequate detectiecapaciteit.

De escalatie ten opzichte van eerdere maanden zit in twee dimensies. Ten eerste: LangChain/LangGraph-kwetsbaarheden (drie CVE's) raken direct teams die RAG-pipelines of agenten bouwen op populaire frameworks. Ten tweede: Mythos-niveau dual-use capaciteiten zijn nu bewezen schaalbaar — offensieve AI voor kwetsbaarheidsdetectie is geen hypothese meer. De "promptware kill chain" (Schneier) biedt aanvallers een gestructureerde aanpak. Het aanvalsoppervlak groeit per externe databron die een agent leest.

### 📈 Markt & Adoptie

De marktdynamiek in april werd getekend door de paradox van explosieve groei én hardnekkige adoptieknelpunten. Cloudcijfers bevestigen de infrastructuurinvestering: Azure +39% YoY, Google Cloud +50% in Q4 2025. Gartner projecteert een totale AI-markt van meer dan $2 biljoen in 2026. Salesforce voegde +6.000 enterprise klanten toe in drie maanden — terwijl de bubble-discussie aanhield.

Tegelijk erkende OpenAI's COO dat AI "nog niet echt in enterprise-bedrijfsprocessen is doorgedrongen." Twee derde van bedrijven zit vast in pilots. De kloof tussen experimenteren en schaalbare productie is groot en duur om zelf te overbruggen — precies het speelveld waar dienstverleners onderscheidend kunnen zijn. NVIDIA's enterprise agent-platform (Adobe, SAP, Salesforce) en A2A-interoperabiliteit verlagen de technische drempel; de implementatiedrempel blijft hoog.

---

## 💼 Ctac-maandperspectief

- **EU AI Act compliance is de meest urgente korte-termijn propositie.** De deadline van 2 augustus is nu minder dan vier maanden weg. Klanten in overheid, zorg en finance zijn grotendeels niet klaar. De nieuwe Commissierichtlijnen van 8 april zijn een uitstekend gesprekshaakje. Wie in mei begint met een readiness assessment heeft net genoeg tijd; wie in juni begint niet meer. Dit is een direct inzetbare propositie met een harde deadline — gebruik die urgentie.

- **Positioneer Ctac als pilot-naar-productie partner, niet als proof-of-concept bouwer.** De bottlenecks die twee derde van Nederlandse bedrijven in de pilotfase houden — data-architectuur, integratie, monitoring, security, change management — zijn exact Ctac's speelveld als custom software- en transformatiepartner. Dit onderscheidt Ctac van hyperscaler-resellers die infrastructuur leveren maar het implementatiewerk overlaten aan de klant. Maak dit explicieter in klantgesprekken.

- **Security by design is vanaf nu een niet-onderhandelbare baseline.** Prompt injection is structureel onoplosbaar; LangChain-kwetsbaarheden raken actieve projecten; Mythos-niveau dual-use capaciteiten zijn bewezen schaalbaar. Elke agentic implementatie die Ctac uitvoert moet een securityarchitectuur hebben vanaf dag één. Intern kwaliteitsargument én extern verkoopargument — combineer ze.

- **Open-source en soevereine AI als propositie voor datakritische klanten.** Gemma 4 (Apache 2) en GLM-5 (MIT) maken on-premise deployment van frontier-kwaliteit modellen realistisch. Voor klanten in overheid of finance met soevereiniteitsvereisten is dit een concreet alternatief voor cloudgebaseerde API's. Kennis van lokale inference-stacks (vLLM, Ollama, llama.cpp) gecombineerd met klantintegratie is een differentiator die Ctac's AI-unit nu kan opbouwen.

- **Agent-architectuur en vendor lock-in als strategisch adviesthema.** Met NVIDIA, Microsoft en Google die elk hun eigen agent-stacks pushen, wordt architectuuronafhankelijkheid een klantbehoefte. MCP en A2A als open standaarden bieden een tegenwicht — maar vereisen dat Ctac er kennis van heeft. Een MCP-referentie-architectuur voor veelgebruikte klantomgevingen (SAP, Microsoft 365, Dynamics) is een concrete deliverable voor de AI-unit.

---

## 📚 Bronnenlijst april 2026

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
- [OpenAI Aardvark – openai.com](https://openai.com/index/introducing-aardvark/)
- [LLM Stats – AI model updates april 2026](https://llm-stats.com/ai-news)

**Governance & Beleid**
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act volgende stappen](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/)
- [EC richtlijnen AI-definitie – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [EU Digital Omnibus en AI Act tijdlijn – OneTrust](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/)
- [AI Act impact NL/BE – cryptobenelux.com](https://cryptobenelux.com/kunstmatige-intelligentie/ai-act-raakt-in-2026-vooral-hr-onderwijs-en-overheid-in-nederland-en-belgie)
- [AIC4NL vooruitblik 2026](https://aic4nl.nl/en/aic4nl/vooruitblik-2026-intensivering-van-de-uitvoering/)
- [AI adoptie Benelux – ictmagazine.nl](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)
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
- [NVIDIA enterprise AI agent platform – VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Salesforce +6.000 enterprise klanten – VentureBeat](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000)
- [AI adoptie Nederland 2026 – Searchlab NL](https://searchlab.nl/blog/ai-adoptie-nederland-2026)
- [Microsoft en Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Enterprise agentic AI landscape 2026 – Kai Waehner](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)
- [OpenAI COO over enterprise adoptie – TechCrunch](https://techcrunch.com/2026/02/24/openai-coo-says-we-have-not-yet-really-seen-ai-penetrate-enterprise-business-processes/)
- [Cloud infrastructure Q4 2025 – Omdia](https://omdia.tech.informa.com/pr/2026/mar/global-cloud-infrastructure-spending-rose-29percent-in-q4-2025-as-hyperscalers-scaled-ai-infrastructure-investment)
