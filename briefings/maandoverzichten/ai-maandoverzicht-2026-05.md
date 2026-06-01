---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Maand: 2026-05
Periode: 2026-05-01 / 2026-05-31
Status: Afgerond
tags:
  - maandoverzicht
---

# AI Maandoverzicht – mei 2026

> Synthese van de weekoverzichten W18 t/m W22 (1 mei – 31 mei 2026).

## 🏆 Maandhighlights

1. **Agentic AI is standaardproduct geworden – geen pilot meer.** Mei 2026 is de maand waarin multi-agent AI de definitieve stap maakte van infrastructuurbelofte naar productiekwaliteit. Microsoft Agent 365 ging GA op 1 mei ($15/user/maand) als centrale governance-laag voor enterprise-agents. Google lanceerde op I/O 2026 Antigravity 2.0 – een autonome multi-agent omgeving die live een besturingssysteem bouwde in 12 uur. SAP presenteerde de Autonomous Enterprise met 200+ productie-agents die alle core-bedrijfsprocessen beslaan. Het Model Context Protocol (MCP) werd overgedragen aan de Agentic AI Foundation (Linux Foundation), mede gedragen door Anthropic én OpenAI, waarmee het protocol vendor-neutraal infrastructuur is geworden – vergelijkbaar met TCP/IP voor het web. De vraag is niet langer of agents werken, maar hoe je ze beheert, beveiligt en integreert.

2. **EU AI Act: van dramatische mislukking naar pragmatisch akkoord.** April eindigde met de mislukking van de politieke triloog (28 april); mei leverde op 7 mei een definitief akkoord. De high-risk compliance-deadline voor standalone AI-systemen (Annex III: HR, biometrie, kritieke infrastructuur) verschoof 16 maanden – van 2 augustus 2026 naar 2 december 2027. Product-gebonden AI (medische apparatuur, machines) krijgt uitstel tot augustus 2028. Tegelijkertijd werden nieuwe verboden versneld: nudification-apps verboden, CSAM-generatie strafbaar per 2 december 2026. De basisdatum van 2 augustus 2026 bleef overeind voor GPAI-transparantievereisten en watermarking. Dit is geen intrekking van de wet – het is kalibratie op uitvoerbaarheid. EP-stemming volgt op 14–17 juni.

3. **AI-security evolueert van vakgebied naar projectvereiste.** Geen week in mei ging voorbij zonder nieuwe concrete kwetsbaarheden in AI-infrastructuur. Semantic Kernel CVEs (CVE-2026-25592 en CVE-2026-26030, beide CVSS 9.9) maakten prompt injection tot Remote Code Execution via enterprise-grade frameworks. GitHub Copilot (CVE-2025-53773, CVSS 9.6) maakte pull request-beschrijvingen tot een aanvalsoppervlak. Week 22 bracht 30+ nieuwe CVEs in coding assistants in één week, en de 'Claudy Day' multi-stap aanvalsketen op Claude. NCSC UK bevestigde wat al lang werd gevreesd: prompt injection is structureel onoplosbaar – risicomanagement en architectuurkeuzes zijn de enige aanpak. Cisco's State of AI Security 2026 plaatst AI-dreigingen voor het eerst als de #1 opkomende risicocategorie, boven ransomware en supply chain. Wie agentic AI implementeert zonder expliciete security-architectuur, is al te laat.

4. **De ROI-kloof verdiept zich terwijl de investeringen doorstijgen.** AI-investering overstijgt $650 miljard per jaar, enterprise-adoptie groeit van 22% (2025) naar 40% (2026), maar de waarderealisatie loopt structureel achter. Deloitte's State of AI 2026 toont dat slechts 29% significante ROI rapporteert van generatieve AI en 23% van AI-agents, terwijl 79% deploymentsuitdagingen ervaart – een stijging van dubbele cijfers tegenover 2025. IBM noemde het op Think 2026 de "AI divide": organisaties die AI écht in hun operatie inbedden, presteren fundamenteel anders dan de rest. Gartner voorspelt dat 40%+ van agentic AI-projecten voor eind 2027 geannuleerd wordt wegens onduidelijke businesswaarde. Antwoord van de markt: OpenAI lanceerde een $4 miljard "DeployCo" consulting-dochter met field engineers. Het gat zit niet in de technologie – het zit in governance, data-architectuur en operationele integratie.

5. **Anthropic overtreft OpenAI in waardering terwijl het modellandschap democratiseert.** Twee bewegingen raken elkaar in mei. Enerzijds: frontier-modellen worden betaalbaar voor iedereen. DeepSeek V4 levert frontier-kwaliteit voor 1/20e van de prijs van Claude Opus 4.7 onder MIT-licentie. China's open-source sprint (GLM-5.1, MiniMax M2.7, Kimi K2.6) leverde vier frontier coding-modellen in 12 dagen. GPT-5.5 werd standaardmodel voor alle ChatGPT-gebruikers. Claude Opus 4.7 ging breed GA. Anderzijds: de bedrijven die deployment begrijpen, genereren extreme waarde. Anthropic sloot een $30 miljard funding ronde met een pre-money waardering boven $900 miljard – voor het eerst hoger dan OpenAI's $852 miljard. De drijvende kracht: Claude Code, een coding agent die in mei 2026 $45 miljard ARR realiseert, verdubbeld ten opzichte van begin 2026. De paradox van mei: modellen worden commodities, maar expertise in enterprise-implementatie wordt exponentieel meer waard.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De technologische rode draad van mei is de verschuiving van modelwedloop naar platformdominantie. De maand begon met Microsoft dat Office definitief agentisch maakte en eindigde met Google's Antigravity 2.0 en SAP's 200-agent-suite als productie-realiteit. Tussenin: MCP als open standaard, Anthropic Agent Skills open source, en Cloudflare's Agents Week die aantoonde dat agents nu autonoom kunnen onboarden, betalen en code deployen.

De modelmarkt zelf laat een tweesplitsing zien. Aan de frontier: reasoning als standaardarchitectuur (GPT-5.5 Instant standaard voor 1,6 miljard ChatGPT-gebruikers, Gemini 3.1 Ultra met 2M context, Claude Opus 4.7 GA). Aan de open-weight kant: Chinese modellen die de frontier-gap definitief sluiten. Twee conclusies zijn onontkoombaar: (1) de keuze "welk model?" is minder relevant geworden, (2) de investering in agent-infrastructuur, integratie en governance is de nieuwe concurrentiefactor.

### 🏛️ Governance & Beleid

Mei was de meest bewogen beleidsmaand van het jaar. Het verhaal begon op 28 april met de mislukte Omnibus-triloog en sloot op 7 mei met een definitief akkoord – de snelste politieke koerswijziging in het AI Act-traject. Het resultaat hertekent de complianceplanning voor Europese organisaties: hoog-risico AI geeft 16 maanden lucht, maar de basislijn van 2 augustus 2026 is juridisch onontkoombaar voor GPAI-systemen.

Parallel institutionaliseerde de VS AI-governance juist strakker: NIST pre-launch modelreviews (Google, Microsoft, xAI), Pentagon IL6/IL7-clearance voor acht techbedrijven, en Microsoft's MDASH als militaire AI-beveiligingslaag. De transatlantische divergentie neemt toe: Europa verlicht high-risk regels, de VS verankert dual-use AI in nationale veiligheidsinfrastructuur. Voor Nederlandse organisaties met internationale activiteiten wordt dubbele compliance-architectuur een praktische noodzaak. In Nederland zijn 10 sectorale toezichthouders operationeel, maar slechts 42% van organisaties heeft volledig AI-beleid – de uitvoeringskloof is structureel.

### 🔐 Security & Risk

Mei markeert het punt waarop AI-security van randnotitie naar strategische boardroom-agenda verschoof. De maand kenmerkt zich door drie escalerendeniveaus: (1) theoretische aanvallen werden bewezen exploits in productiesystemen, (2) aanvalsoppervlakken breidden zich uit van AI-applicaties naar developer-tooling en supply chains, (3) gezaghebbende instanties (NCSC UK, Cisco, NIST) bevestigden structurele onverheldbaarheid van kernrisico's.

De meest zorgwekkende ontwikkeling is niet één CVE, maar het patroon: NIST registreerde een 2.000%+ stijging in AI-specifieke CVEs in 2025–2026. 80% van organisaties rapporteert al riskant agent-gedrag in productie. Slechts 24% heeft een dedicated AI security governance-team. De snelheid waarmee aanvallers AI-kwetsbaarheden exploiteren (28,3% van CVEs uitgebuit binnen 24 uur) laat geen marge voor een reactieve beveiligingshouding.

### 📈 Markt & Adoptie

Mei laat de scherpste adoptie-paradox van het jaar zien: historisch hoge investeringen gaan gepaard met historisch lage ROI-rapportage. De $650+ miljard jaarlijkse AI-investeringsklok tikt door, hyperscalers plannen gezamenlijk >$500 miljard capex voor FY2026, en Anthropic bereikte $900 miljard waardering. Tegelijkertijd: 48% van enterprise-bestuurders noemt AI-adoptie een teleurstelling, Gartner verwacht 40%+ projectcancellaties.

Twee marktbewegingen doorbreken dit patroon. Eén: verticalisering. Avoca ($1B voor loodgieters), KPMG's Claude-implementatie bij 276.000 medewerkers in 138 landen, Eli Lilly's $2,75 miljard AI-deal – de waarde concentreert zich bij wie diep begrijpt hoe AI een specifieke workflow transformeert. Twee: consolidatie. Google Cloud overschreed $20 miljard per kwartaal (+63% YoY). Microsoft en Google domineren enterprise AI (Gartner). Labs worden zelf enterprise-dienstverleners (OpenAI DeployCo). De markt beloont schaal én specialisatie; generieke chatbot-propositiehouders raken structureel klem.

---

## 💼 Ctac-maandperspectief

- **EU AI Act compliance: herplanning én momentum bewaren.** De 16-maands verschuiving voor high-risk AI (naar december 2027) is geen uitstel van acties, maar een kans voor gedegen aanpak. Twee-track strategie blijft relevant: Track 1 (onuitstelbaar) zijn GPAI-transparantievereisten en Art. 50-verplichtingen per 2 augustus 2026 – dit geldt voor elke organisatie die grote AI-modellen inzet of chatbot-interacties verwerkt. Track 2 (bijgesteld) is hoog-risico AI-documentatie en risicoklassificatie, nu met een realistische tijdlijn tot december 2027. Klanten die door het Omnibus-uitstel in de ruststand schieten, verliezen de voorsprong op concurrenten die nu wél hun AI-governance op orde brengen. Een Ctac AI Act Readiness Scan als gestructureerd startpunt – gap-analyse, risicoklassificatie, documentatiebegeleiding – is het meest directe aanbod voor de komende maanden.

- **Agent governance als standaard service-component.** Microsoft Agent 365 ($15/user), SAP Autonomous Suite, Google Managed Agents en MCP als open standaard maken agent governance van adviesgesprek tot product-implementatie. Elke klant die M365, SAP S/4HANA of Google Workspace inzet, heeft nu een concrete aankoopdecisie voor agent-governance voor de boeg. Ctac kan hier positioneren als de partner die de koppeling maakt tussen platformcapaciteiten (Microsoft Agent 365, SAP Joule) en klantspecifieke bedrijfsprocessen – inrichting, beheer, audit en beveiligingsarchitectuur. Intern: formuleer nu een SAP AI-propositie die de Anthropic-integratie bij Joule meeneemt.

- **De "AI divide" is Ctac's marktpositionering in woorden die klanten snappen.** IBM's diagnose is krachtig en extern gevalideerd: 79% van enterprises loopt vast op dezelfde bottlenecks – data-architectuur, integratie, governance en change management. Dat is precies het werkterrein van een implementatiepartner als Ctac. Gebruik IBM Think, Deloitte State of AI en Gartner als externe referenties in salesgesprekken: "Dit is niet onze mening, dit is industrieconsensus." Formuleer een concreet "van pilot naar productie in 90 dagen"-traject met een heldere businesscase als startpunt – inclusief de structurele blockers die de markt identificeert.

- **Security by design als contractuele deliverable in elk agentic project.** De maand leverde onweerlegbaar bewijs: Semantic Kernel (CVSS 9.9), GitHub Copilot (CVSS 9.6), 30+ CVEs in één week, en NCSC UK's structurele bevestiging. Elk Ctac-project dat agentic AI inzet, moet een expliciet security-component bevatten: threat modeling van databronnen die de agent leest, prompt injection-mitigatie, netwerk-isolatie, audit-logging en gecontroleerde tool-toegang. Intern aandachtspunt: Semantic Kernel-patches zijn dit kwartaal actiepunt voor alle lopende projecten die .NET of Python SDK gebruiken (vóór v1.71.0 resp. v1.39.4). Dit is zowel intern kwaliteitsmanagement als extern onderscheidend aanbod.

- **Open-source en soevereine AI versterken de propositie voor datakritische klanten.** DeepSeek V4 (MIT, frontier-kwaliteit, 1M context), GLM-5.1 en MiniMax M2.7 maken on-premise deployment van frontier-niveau modellen realistisch – niet als compromis maar als echte optie voor klanten met soevereiniteits- of budgetvereisten. Ctac's kennis van lokale inference-stacks (vLLM, Ollama) gecombineerd met klantintegratie-expertise is een concreet verschilpunt dat hyperscalers structureel niet kunnen aanbieden. Dit is een differentiërende propositie voor overheid, finance en maakindustrie in Benelux.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Microsoft Agent 365 GA – VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [Google I/O 2026: 100 aankondigingen – Google Blog](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Google I/O 2026: Gemini Omni, Antigravity 2.0 – CyberNews](https://cybernews.com/ai-news/google-io-2026-gemini-omni-antigravity-agentic-ai/)
- [SAP Sapphire 2026: Autonomous Enterprise – SAP News Center](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/)
- [Anthropic doneert MCP aan Agentic AI Foundation – Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [Anthropic Claude Opus 4.7 GA – Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
- [OpenAI GPT-5.5 Instant standaardmodel – TechCrunch](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/)
- [DeepSeek V4: frontier voor 1/20e prijs – VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- [IBM Think 2026: blueprint voor AI Operating Model – IBM Newsroom](https://newsroom.ibm.com/2026-05-05-think-2026-ibm-delivers-the-blueprint-for-the-ai-operating-model-as-the-ai-divide-widens)
- [Cloudflare Agents Week in review – Cloudflare Blog](https://blog.cloudflare.com/agents-week-in-review/)
- [Anthropic $900B waardering – Bloomberg via Yahoo Finance](https://finance.yahoo.com/news/anthropic-targets-900-billion-valuation-220005674.html)
- [Hugging Face State of Open Source AI Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)

**Governance & Beleid**
- [EU AI Act Omnibus politiek akkoord 7 mei – Consilium EU](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [EU AI Act Omnibus: wat veranderde – TechPolicy.Press](https://www.techpolicy.press/what-the-eu-ai-omnibus-deal-changes-for-the-ai-act-and-what-lies-ahead/)
- [EU AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [NIST pre-launch modelreviews Google, Microsoft, xAI – Washington Post](https://www.washingtonpost.com/technology/2026/05/05/google-microsoft-xai-ai-review/)
- [Pentagon AI-clearance 8 techbedrijven – CNN Business](https://www.cnn.com/2026/05/01/tech/pentagon-ai-anthropic)
- [Tien toezichthouders AI Act NL – Computable](https://www.computable.nl/2026/04/22/tien-toezichthouders-bewaken-naleving-ai-verordening/)
- [EU AI Act 2026 updates: compliance vereisten – LegalNodes](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)

**Security & Risk**
- [Semantic Kernel CVEs CVSS 9.9 – Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Microsoft MDASH: defensie op AI-snelheid – Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)
- [1 miljoen blootgestelde AI-diensten – The Hacker News](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)
- [2026: jaar van AI-ondersteunde aanvallen – The Hacker News](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)
- [Cisco State of AI Security 2026 – Cisco Blogs](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)
- [Eerste AI-ontwikkelde zero-day voor 2FA-bypass – The Hacker News](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known-zero-day-2fa-bypass-for-mass-exploitation.html)
- [AI security statistics 2026 – Practical DevSecOps](https://www.practical-devsecops.com/ai-security-statistics-2026-research-report/)
- [Tenable Cloud & AI Security Risk Report 2026 – Tenable](https://www.tenable.com/cyber-exposure/cloud-and-ai-security-risk-report-2026)

**Markt & Adoptie**
- [Enterprise AI adoption 2026: 79% faces challenges – Writer](https://writer.com/blog/enterprise-ai-adoption-2026/)
- [State of AI in the Enterprise 2026 – Deloitte](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html)
- [AI Investment $650B+ jaarlijks – GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/05/3288006/0/en/AI-Investment-Activity-to-Surpass-650-Billion-Annually-as-Enterprise-Adoption-Accelerates-Toward-2026.html)
- [HCLTech: 43% enterprise AI initiatives at risk – PR Newswire](https://www.prnewswire.com/news-releases/hcltech-report-warns-43-of-enterprise-ai-initiatives-may-fail-as-leaders-face-shrinking-timelines-for-impact-302777842.html)
- [OpenAI $4B DeployCo – PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-4-billion-dollar-company-accelerate-enterprise-ai-adoption/)
- [OpenAI & Anthropic enterprise JVs – TechCrunch](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/)
- [Google Cloud overstijgt $20B/kwartaal – CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [Gartner Hype Cycle for Agentic AI 2026 – Gartner](https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai)
- [State of AI Agents 2026 – Arcade.dev](https://www.arcade.dev/blog/5-takeaways-2026-state-of-ai-agents-claude/)
- [Eerste AI-agent betaling NL: Mastercard + Rabobank – Computable](https://www.computable.nl/2026/05/05/kort-ai-ontslagen-betekenen-zelden-hoger-rendement-ai-moet-maakindustrie-verslimmen-en-meer/)
