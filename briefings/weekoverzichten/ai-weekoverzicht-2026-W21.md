---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W21
Datum: 2026-05-22
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 21, 2026

> Synthese van de dagbriefings van maandag 18 mei t/m vrijdag 22 mei 2026.

## 🏆 Weekhighlights

1. **Google I/O 2026: Gemini Omni + Antigravity 2.0 — agentic AI wordt operationeel**
   Google lanceerde op 19 mei twee modellen én een volledig nieuw agent-first development platform. Gemini Omni verwerkt elke vorm van input tot samenhangende output en simuleert fysica en beweging. De showstopper was Antigravity 2.0: een autonome multi-agent omgeving die live een werkend besturingssysteem vanuit niets bouwde in 12 uur. Één API-aanroep levert nu een volledige, geïsoleerde Linux-sandbox met agent die zelf plant, code uitvoert en het web raadpleegt.

2. **EU AI Act Digital Omnibus: hoog-risico deadline verschuift 16 maanden**
   Op 7 mei bereikte de EU-Raad een akkoord met het Europees Parlement over de eerste wijzigingen van de AI Act. De compliance-deadline voor hoog-risico AI-systemen (Annex III) schuift van 2 augustus 2026 naar 2 december 2027. Nationale sandboxes worden een jaar uitgesteld, transparantievereisten voor synthetische content met vier maanden. Formele goedkeuring wordt in juni verwacht. Dit is geen intrekking van de wet — de wet komt, alleen met meer aanlooptijd.

3. **SAP Sapphire 2026: SAP zet alles op agentic AI met de Autonomous Enterprise**
   Op 21 mei in Madrid presenteerde SAP CEO Christian Klein de transformatie van SAP tot een "Business AI company". De SAP Business AI Platform bundelt BTP, Business Data Cloud en AI Foundation. De SAP Autonomous Suite telt 200+ agenten en 50+ assistenten over vijf domeinen: Finance, Spend, Supply Chain, HCM en CX. De nieuwe interface Joule Work vervangt applicatienavigatie door gespreksgestuurde workflows. Anthropic's Claude is een van de fundament-modellen voor Joule.

4. **OpenAI's GPT-5.5: het nieuwe standaard voor professioneel agentic gebruik**
   OpenAI maakte GPT-5.5 het standaardmodel voor ChatGPT-gebruikers. Het model combineert frontier-niveau redenering met sterk verbeterde tool use, agentic coding (SWE-bench), en documentverwerking. Tegelijkertijd lanceerde OpenAI een Deployment Company ($4 miljard) om enterprises te helpen AI betrouwbaar op schaal in te zetten — inclusief overname van Tomoro voor field engineering.

5. **AI-security wordt actuele dreiging — CVE's in AI orchestration frameworks**
   IBM's X-Force Threat Intelligence Index meldt een stijging van 44% in aanvallen op publiek toegankelijke applicaties. Een kritisch authentication-bypass lek in het open-source AI orchestration framework PraisonAI (CVE-2026-44338) werd binnen uren na bekendmaking actief gescand. Een lek in de Gemini CLI stelt CI/CD-pipelines bloot aan remote code execution. Cisco's State of AI Security 2026 rapport identificeert AI-specifieke dreigingen als de grootste opkomende risicocategorie voor enterprises.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De rode draad van week 21 is de overgang van agentic AI als concept naar agentic AI als geïntegreerde infrastructuur. Google, OpenAI én SAP lanceerden binnen dezelfde week platforms die agenten niet meer als addon behandelen, maar als primaire interactielaag. Google's Antigravity-demo (OS in 12 uur) en SAP's Autonomous Suite (200+ productie-agenten) markeren een kantelpunt: de vraag is niet langer "werken agenten?" maar "hoe beheer je ze op schaal?". Gemini 3.5 Flash is hierbij het centrale uitvoeringsmodel — zowel voor Google's Managed Agents als voor Anthropic-gebaseerde Joule-agenten bij SAP. De race om agent-runtime-dominantie — wie levert de sandboxed, tool-using omgeving waar enterprises agents op draaien — is nu volop begonnen.

### 🏛️ Governance & Beleid

De EU AI Act-wijzigingen van 7 mei zijn meer dan een vertraging: ze zijn een structurele herpositionering. De EU erkent dat de uitvoerbaarheid van de wet voor hoog-risico systemen sneller dan verwacht samenknijpt door de marktdynamiek. Met 16 maanden extra (tot december 2027) voor Annex III-systemen verschuift de acute compliance-druk voor organisaties. Tegelijkertijd komen er nieuwe verboden bij, en blijven de transparantievereisten voor GPAI (frontier models) ongewijzigd. Het patroon: de EU versombert niet, maar kalibriëert op uitvoerbaarheid. Organisaties die al begonnen zijn met compliance-trajecten doen er goed aan het momentum vast te houden, maar kunnen de planning spreiden.

### 🔐 Security & Risk

Week 21 bevestigt dat AI-security van theoretisch naar operationeel risico is verschoven. Drie signalen zijn dit patroon illustratief:
(1) CVE's in AI-infrastructuur zijn nu actuele exploits, niet toekomstige scenario's;
(2) AI-tools in software supply chains (SAP npm-pakketten, CI/CD-integraties) worden actief misbruikt;
(3) Mass-deployment van AI-services zonder basisauthenticatie creëert een enorm aanvalsoppervlak dat nu actief wordt gescand.

Cisco's 2026-rapport categoriseert AI-dreigingen voor het eerst als de #1 opkomende risicocategorie voor enterprises — boven ransomware en supply chain. De implicatie: "secure by design" is geen optie meer bij agentic AI-deployments, het is een baseline-eis.

### 📈 Markt & Adoptie

Twee tegengestelde signalen domineren deze week. Enerzijds: historisch hoge investeringen ($650+ miljard in 2026, Big Tech capex richting $562 miljard) en SAP dat haar complete portfolio omgooit voor AI. Anderzijds: 43% van enterprise AI-initiatieven riskeert te mislukken (HCLTech), en 79% van enterprises rapporteert aanzienlijke uitdagingsdrempels. OpenAI's lancering van een Deployment Company met field engineers en een Tomoro-overname wijst op een markt die erkent dat self-service AI-implementatie onvoldoende is voor enterprise-betrouwbaarheid. Het patroon: de adoption gap tussen aankondiging en operationele waarde is de commerciële kans van 2026.

---

## 💼 Ctac-weekperspectief

- **SAP Autonomous Suite vraagt directe service-portfoliokeuze**: Als Microsoft- en SAP-partner staat Ctac voor de vraag hoe het Joule Work, de SAP Autonomous Suite en de 200+ nieuwe agenten begeleidt bij klanten. Klanten zullen op korte termijn vragen wat hun SAP S/4HANA-landschap betekent in een agentic architectuur. Ctac doet er goed aan nu intern een SAP AI-propositie te formuleren, inclusief de Anthropic-integratie die bij Joule hoort.

- **EU AI Act-uitstel = planning herschrijven maar momentum bewaren**: De hoog-risico deadline verschuift naar december 2027, maar dat betekent niet dat klanten niets hoeven te doen. Juist nu, met minder urgentiedruk, is er ruimte voor gedegen risicoklassificatie en governance-inrichting. Ctac kan dit positioneren als "rustig maar zeker compliance voorbereiden" — een stuk aantrekkelijker dan een crisisaanpak vlak voor een deadline.

- **Google Antigravity + Gemini Managed Agents als developer accelerator**: Voor ontwikkelteams die Ctac inzet of begeleidt is de Gemini API + Managed Agents nu een concrete low-friction route naar agentic tooling. Eén API-aanroep geeft een volledig geïsoleerde agent-sandbox — dit verlaagt de drempel om te experimenteren significant. Evalueer of dit een alternatief is voor Azure AI Foundry voor specifieke use cases.

- **AI-security als onderscheidende propositie**: Met CVE's in AI orchestration frameworks en een 44% stijging in aanvallen op AI-services is "secure AI deployment" een actueel klantgesprek. Ctac kan differentiëren door bij agentic implementaties altijd een security-by-design laag mee te leveren: authenticatie, netwerk-isolatie, gecontroleerde tool-toegang. Dit is een concrete add-on op elke agentic deployment-opdracht.

---

---

### Zaterdag 23 mei

→ Dagbriefing: [ai-briefing-2026-05-23.md](../ai-briefing-2026-05-23.md)

**Highlights:**
- **Claude Opus 4.7 live + Mythos besloten launch** – Anthropic bracht vandaag Opus 4.7 breed beschikbaar (Bedrock, Vertex AI, Foundry). Tegelijk rolde het besloten model "Mythos" uit bij select partners met focus op cybersecurity-toepassingen.
- **AI Omnibus akkoord + EC-consultatie implementatierichtlijnen** – Op 7 mei bereikte de EC politiek akkoord over AI Omnibus-amendementen; op 19 mei opende de feedbackronde over implementatierichtlijnen. De volledige AI Act treedt in werking op 2 augustus 2026.
- **Prompt injection escaleert met agentic AI** – OWASP rangschikt prompt injection als kwetsbaarheid #1 voor LLM-toepassingen; aanvalssuccespercentages overstijgen 85%. OpenAI erkent dat een volledige oplossing waarschijnlijk nooit haalbaar is — risicomanagement is de enige aanpak.

**Ctac-relevantie van de dag:** De combinatie van de naderende AI Act-deadline (augustus 2026) en de explosieve groei van Microsoft Agent 365 (tienduizenden klanten in twee maanden) maakt dit het moment om klanten actief te benaderen voor compliance-scans én een duidelijk Microsoft-agentplatform-propositie te formuleren.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [100 things we announced at Google I/O 2026 – Google Blog](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Google pushes "agentic AI" at I/O 2026 with Gemini Omni, Antigravity 2.0 – CyberNews](https://cybernews.com/ai-news/google-io-2026-gemini-omni-antigravity-agentic-ai/)
- [Google I/O 2026 Summary: Gemini 3.5, Omni, Antigravity, and System-Level Agents – Knightli](https://knightli.com/en/2026/05/21/google-io-2026-gemini-agentic-ai-summary/)
- [Google I/O 2026: 3 new Gemini models change everything – BetaNews](https://betanews.com/article/google-io-2026-gemini-flash-omni-spark-search/)
- [I/O 2026 developer highlights: Antigravity, Gemini API, AI Studio – Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/)
- [OpenAI releases GPT-5.5 Instant, a new default model for ChatGPT – TechCrunch](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/)
- [OpenAI Launches $4 Billion Company to Accelerate Enterprise AI Adoption – PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-4-billion-dollar-company-accelerate-enterprise-ai-adoption/)

**SAP Sapphire 2026**
- [SAP Sapphire 2026 Keynote: Powering the Autonomous Enterprise – SAP News Center](https://news.sap.com/2026/05/sap-sapphire-keynote-business-ai-platform-power-autonomous-enterprise/)
- [SAP Unveils the Autonomous Enterprise – SAP News Center](https://news.sap.com/2026/05/sap-sapphire-sap-unveils-autonomous-enterprise/)
- [SAP Sapphire 2026: The Autonomous Enterprise and AI Agent Guardrails – SAPinsider](https://sapinsider.org/blogs/sap-sapphire-2026-autonomous-enterprise-ai-agents/)
- [SAP Sapphire 2026: The autonomous enterprise takes shape in Madrid – Enterprise Times](https://www.enterprisetimes.co.uk/2026/05/21/sap-sapphire-2026-the-autonomous-enterprise-takes-shape-in-madrid/)

**Governance & Beleid**
- [Artificial Intelligence: Council and Parliament agree to simplify and streamline rules – Consilium](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [EU AI Act Update: Timeline Relief, Targeted Simplification, and New Prohibitions – Inside Privacy](https://www.insideprivacy.com/artificial-intelligence/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)
- [AI Act Update: EU Resolves to Change Rules and Extend Deadlines – Latham & Watkins](https://www.lw.com/en/insights/ai-act-update-eu-resolves-to-change-rules-and-extend-deadlines)
- [The EU simplified its toughest AI law: what changed and why it matters – Euronews](https://www.euronews.com/my-europe/2026/05/21/the-eu-simplified-its-toughest-ai-law-what-changed-and-why-it-matters)
- [EU AI Act 2026 Updates: Compliance Requirements and Business Risks – LegalNodes](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)

**Security & Risk**
- [2026: The Year of AI-Assisted Attacks – The Hacker News](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)
- [We Scanned 1 Million Exposed AI Services – The Hacker News](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)
- [Supply Chain Attacks, AI Security, and Major Breaches Define This Week – eSecurity Planet](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/)
- [Cisco State of AI Security 2026 Report – Cisco Blogs](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)
- [Defense at AI speed: Microsoft's new multi-model agentic security system – Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)
- [May 2026 Is the Forecast: AI Governance Just Became Data Governance – Cybersecurity Insiders](https://www.cybersecurity-insiders.com/may-2026-is-the-forecast-ai-governance-just-became-data-governance/)

**Markt & Adoptie**
- [AI Investment Activity to Surpass $650 Billion Annually – GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/05/3288006/0/en/AI-Investment-Activity-to-Surpass-650-Billion-Annually-as-Enterprise-Adoption-Accelerates-Toward-2026.html)
- [Enterprise AI adoption in 2026: Why 79% face challenges despite high investment – Writer](https://writer.com/blog/enterprise-ai-adoption-2026/)
- [HCLTech report warns 43% of enterprise AI initiatives may fail – PR Newswire](https://www.prnewswire.com/news-releases/hcltech-report-warns-43-of-enterprise-ai-initiatives-may-fail-as-leaders-face-shrinking-timelines-for-impact-302777842.html)
- [OpenAI revenue chief: enterprise AI adoption is 'at a tipping point' – CNBC](https://www.cnbc.com/2026/05/11/open-ai-dresser-enterprise-business.html)
- [SAP's Autonomous Enterprise Push Meets Valuation Gap – Yahoo Finance](https://finance.yahoo.com/news/sap-autonomous-enterprise-push-meets-061630594.html)
- [Microsoft Build 2026 in San Francisco: AI agents, trust, and developer platform shift – Windows News](https://windowsnews.ai/article/microsoft-build-2026-in-san-francisco-ai-agents-trust-and-developer-platform-shift.418934)
