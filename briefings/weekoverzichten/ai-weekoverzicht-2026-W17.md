---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W17
Datum: 2026-04-24
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 17, 2026

> Synthese van AI-intelligence voor de week van 20 april t/m 24 april 2026.
> Dagbriefings voor deze week waren niet beschikbaar; dit overzicht is samengesteld op basis van directe bronraadpleging.

---

## 🏆 Weekhighlights

1. **Google Cloud Next 2026 zet de toon voor het agentic AI-tijdperk.** Op 22 april lanceerde Google een volledig agentic AI-platform: Gemini Enterprise Agent Platform (met Agent Designer, Skills, Inbox en long-running agents), 8e generatie TPU-chips (1.152 TPUs per pod, 3x meer on-chip SRAM), Agentic Data Cloud en Agentic Defense. Tegelijkertijd committeerde Google $750 miljoen aan zijn partnernetwerk van 120.000 leden voor agentic AI-transformatie – een signaal dat de hyperscalerstrijd om enterprise-implementaties nu in een versnelling zit.

2. **MCP-kwetsbaarheid raakt 200.000 instanties wereldwijd – Anthropic weigert te patchen.** Een "by design"-kwetsbaarheid in de officiële MCP SDK (Python, TypeScript, Java, Rust) maakt Remote Code Execution mogelijk via unsafe STDIO-standaardinstellingen. OX Security documenteerde 7.000+ publiek toegankelijke servers, 150 miljoen downloads en tien CVE's in populaire frameworks (LiteLLM, LangChain, LangFlow, Flowise). Anthropic bestempelt het gedrag als "expected" – wat elk agentic project dat MCP gebruikt direct risicodragend maakt.

3. **EU Digital Omnibus-triloog op 28 april kan AI Act-deadlines fundamenteel verschuiven.** De tweede triloog beoogt een finaal akkoord over de Digital Omnibus, inclusief een voorstel om de high-risk AI-deadline te verschuiven: stand-alone systemen naar december 2027, embedded systemen naar augustus 2028. Dit geeft organisaties meer tijd, maar legt ook een hypotheek op de urgentie van compliance-trajecten die nu lopen.

4. **Claude Opus 4.7 arriveert op Amazon Bedrock – agentic AI krijgt nieuwe benchmarks.** Anthropic's Opus 4.7 (uitgebracht 16 april, week 40 op Bedrock) introduceert task budgets, een nieuw xhigh-inspanningsniveau en 2576px high-resolution vision. SWE-bench Pro-score: 64,3%. De 1M token context + sterker long-horizon reasoning bevestigen dat frontiermodellen als production-grade agenten kunnen worden ingezet.

5. **Enterprise AI voorbij het adoptiepunt van internet in jaar 3.** Op 20 april legde de Enterprise AI Adoption Curve nieuw historisch bereik vast: 88% van organisaties gebruikt AI voor minimaal één bedrijfsfunctie, 97% van executives heeft agents deployed. Paradox: 79% ondervindt implementatieknelpunten en slechts 29% ziet significante organisatorische ROI – de "pilot purgatory" is structureel en neemt toe naarmate verwachtingen stijgen.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

Google Cloud Next 2026 domineerde de week technologisch. De kernboodschap: Google positioneert zichzelf als het complete agentic AI-platform voor enterprise – van modelinfrastructuur (Gemini Enterprise, TPU 8i) en no-code bouw (Workspace Studio) tot governance (Agentic Defense, Wiz-integratie) en data (Agentic Data Cloud, cross-cloud Lakehouse). De combinatie met een $750M partnerbudget en 200+ modellen in de Model Garden (inclusief Claude) maakt dit een directe aanval op de OpenAI-enterprise-positie.

Parallel bevestigt Claude Opus 4.7 dat agentic AI op frontiermodelniveau nu schaalbaar is via alle grote platforms. De introductie van task budgets – een token-countdown die het model gebruikt om werk te prioriteren binnen een agentic loop – is architectureel interessant: het introduceert expliciet resource-bewustzijn in LLM-executie, wat een stap richting betrouwbaarder langlopende agents is.

De rode draad van de week: **agentic AI gaat van demo naar productie-infrastructuur.** Hyperscalers concurreren nu op platform-completeness, niet op modelkwaliteit.

### 🏛️ Governance & Beleid

De week stond in het teken van twee tegenstrijdige signalen. Enerzijds: de EU AI Act-deadline van 2 augustus voor GPAI-verplichtingen staat ongewijzigd. Anderzijds: de Digital Omnibus stelt voor om high-risk AI-deadlines met 1–2 jaar te verschuiven, een direct gevolg van de politieke consensus dat implementatie voor het bedrijfsleven te snel gaat. De Europese Commissie probeerde dit gedeeltelijk te compenseren met €63,2 miljoen voor AI-innovatie in gezondheid en online veiligheid (21 april) en AI Continent Action Plan-mijlpalen (9 april).

Amnesty International publiceerde kritiek op de EU-vereenvoudigingswetten, met het argument dat ze rechten van burgers uithollen – een signaal dat de regulatory backlash groeit naarmate AI-regulering concreet wordt. Voor compliance-adviseurs is het patroon duidelijk: **de structuur van de AI Act staat vast, maar de exacte uitvoeringsdeadlines zijn politiek fluïde**. Sturen op de meest strikte datum (2 augustus voor transparantieregels) is de veiligste strategie.

### 🔐 Security & Risk

De MCP-kwetsbaarheid is het bepalende security-verhaal van de week – en de ernst ervan verdient heldere context. De kwetsbaarheid zit niet in een specifieke applicatie, maar in hoe de MCP-standaard zelf STDIO als transport behandelt. Dat betekent dat elk project dat de officiële Anthropic SDK gebruikt voor MCP-integratie potentieel kwetsbaar is, tenzij aantoonbaar anders geconfigureerd. De beslissing van Anthropic om de architectuur niet aan te passen vergroot de verantwoordelijkheid van bouwers en integrators.

Parallel: AI-ondersteunde cyberaanvallen stegen 89% jaar-op-jaar. De CyberStrikeAI-campagne (600+ FortiGate-firewalls in 55 landen, volledig autonoom) toont dat AI niet meer alleen de aanvaller ondersteunt maar nu **de aanvaller zelf is**. Voor teams die agentic AI bouwen geldt: de aanvalsoppervlakte groeit met elke externe databron die een agent leest, en MCP is nu formeel een kwetsbaarheidsvector.

### 📈 Markt & Adoptie

De Deloitte–Google Cloud-aankondiging (22 april) illustreert hoe het consultancylandschap zich herpositioneert: 1.000+ pre-built industry agents, 25.000 Gemini Enterprise-licenties (op te schalen naar 100.000), forward deployed engineers, en een focus op retail, zorg, financiën en overheid. KPMG en Accenture participeren eveneens in het $750M Google-partnerbudget.

Dit is structureel relevant: de grote consultancybedrijven bouwen agentic AI-bibliotheken die de implementatiekosten verlagen. Voor IT-dienstverleners zoals Ctac betekent dit dat **de differentiatie niet meer zit in "wij weten hoe AI werkt" maar in "wij implementeren het veilig, schaalbaar en klantspecifiek."** De markt schuift razendsnel van experimenteren naar productie – en wie de productie-implementatiestap niet kan zetten, verliest terrein aan consultancyreuzen met kant-en-klare agent-assets.

Het mooie en pijnlijke van de Enterprise AI Adoption Curve: de adoptie overtreft nu die van internet in jaar 3, maar de ROI volgt niet in hetzelfde tempo. 49% zit nog in pilots of is nog niet begonnen. Dat gat ís de markt.

---

## 💼 Ctac-weekperspectief

- **MCP-kwetsbaarheid: direct actie vereist voor lopende en geplande agentic projecten.** Elk project dat MCP gebruikt (via LangChain, LangFlow, LiteLLM, Flowise of directe Anthropic SDK) moet deze week worden geauditeerd op STDIO-configuratie. Dit is geen theoretisch risico: 200.000 instanties zijn kwetsbaar, Anthropic patcht niet, en aanvallers zijn actief. Zet dit op de agenda van het technisch lead van de AI-unit en communiceer proactief naar klanten met actieve agentic deployments.

- **Google Cloud Next 2026-positie bepalen vóór volgende klantgesprekken.** Google investeert $750M in zijn partnernetwerk voor agentic AI, Deloitte en KPMG stappen in. Dit vergt een standpunt: wil Ctac als Google Cloud-partner specifiek positioneren voor agentic trajecten? De Gemini Enterprise Agent Platform + Workspace Studio-combinatie verlaagt de technische implementatiedrempel – maar wie de governance, security en change management voor zijn rekening neemt, bepaalt de marge. Dit is een strategische keuze die nu gemaakt moet worden.

- **EU Digital Omnibus-beslissing van 28 april afwachten vóór compliance-communicatie aanpassen.** De potentiële verschuiving van high-risk deadlines naar 2027–2028 verandert de urgentie voor een deel van de klantenportefeuille. GPAI-transparantieregels per 2 augustus 2026 staan wél vast. Splits in klantcommunicatie: GPAI/transparantie = nu starten, high-risk AI = na 28 april definitief plannen. Wacht niet op politieke helderheid voordat je überhaupt begint.

- **Pilot-naar-productie als kernpropositie verankeren in Q2-pitches.** Het structurele knelpunt is breed gedocumenteerd: 49% van organisaties zit vast in de experimenteerfase, slechts 29% ziet echte ROI. Ctac's toegevoegde waarde ligt precies hier – custom software-expertise, integratiekennis, security-first aanpak, change management. Gebruik de Writer-/Deloitte-rapporten van deze week als gesprekshaakje in salesgesprekken: "dit is het industrieprobleem, dit is hoe Ctac het oplost."

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Google Cloud Next 2026: AI agents, A2A protocol, Workspace Studio – The Next Web](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era)
- [Next '26 Day 1 Recap – Google Cloud Blog](https://cloud.google.com/blog/topics/google-cloud-next/next26-day-1-recap)
- [Google Cloud commits $750M to accelerate partners' agentic AI development – PR Newswire](https://www.prnewswire.com/news-releases/google-cloud-commits-750-million-to-accelerate-partners-agentic-ai-development-302749239.html)
- [Google Cloud lanceert nieuwe TPU-chips – TechCrunch](https://techcrunch.com/2026/04/22/google-cloud-next-new-tpu-ai-chips-compete-with-nvidia/)
- [Introducing Claude Opus 4.7 – Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
- [Claude Opus 4.7 op Amazon Bedrock – AWS Blog](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-opus-4-7-in-amazon-bedrock-aws-interconnect-ga-and-more-april-20-2026/)
- [Claude Opus 4.7 Review 2026 – Evolink](https://evolink.ai/blog/claude-opus-4-7-review-2026)
- [April 2026 AI Models Reviewed – Medium](https://medium.com/@sanjeevpatel3007/april-2026-ai-models-every-major-release-reviewed-6ea03d7bc0b7)

**Governance & Beleid**
- [EU Digital Omnibus on AI – European Parliament Legislative Train](https://www.europarl.europa.eu/legislative-train/package-digital-package/file-digital-omnibus-on-ai)
- [EU Digital Omnibus proposes delay of AI compliance deadlines – OneTrust](https://www.onetrust.com/blog/eu-digital-omnibus-proposes-delay-of-ai-compliance-deadlines/)
- [EU simplification laws rollen rechten terug – Amnesty International](https://www.amnesty.org/en/latest/news/2026/04/eu-simplification-laws/)
- [Agentic AI governance challenges under EU AI Act – AI News](https://www.artificialintelligence-news.com/news/agentic-ais-governance-challenges-under-the-eu-ai-act-in-2026/)
- [EU AI Act – Officiële implementatietijdlijn](https://artificialintelligenceact.eu/)
- [Vision Compliance: 78% van enterprises niet voorbereid – National Law Review](https://natlawreview.com/press-releases/vision-compliance-releases-2026-eu-ai-act-readiness-report-finds-78)

**Security & Risk**
- [Anthropic MCP design vulnerability enables RCE – The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)
- [The mother of all AI supply chains – OX Security](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/)
- [MCP kwetsbaarheid: 200.000 AI-servers blootgesteld – pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/1151/anthropic-mcp-vulnerability-200000-ai-servers-rce)
- [Top MCP security resources April 2026 – Adversa AI](https://adversa.ai/blog/top-mcp-security-resources-april-2026/)
- [AI-enabled cyberattacks 2026 – Foresiet](https://foresiet.com/blog/ai-enabled-cyberattacks-2026-incidents/)
- [Cisco State of AI Security 2026 report](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)
- [Threat actor abuse of AI accelerates – Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/04/02/threat-actor-abuse-of-ai-accelerates-from-tool-to-cyberattack-surface/)
- [CVE Watchtower: Weekly Threat Intelligence April 13–19 – Security Online](https://securityonline.info/weekly-vulnerability-digest-april-2026-ai-legacy-threats/)

**Markt & Adoptie**
- [Deloitte lanceert Google Cloud Agentic Transformation Practice – Deloitte US](https://www.deloitte.com/us/en/about/press-room/deloitte-launches-google-cloud-agentic-transformation-practice.html)
- [Deloitte Accelerates AI Transformation on Gemini Enterprise – Google Cloud Press Corner](https://www.googlecloudpresscorner.com/2026-04-22-Deloitte-Accelerates-AI-Transformation-on-Gemini-Enterprise-With-Dedicated-Google-Cloud-Agentic-Transformation-Practice)
- [Enterprise AI adoption curve past internet at year 3 – Asanify](https://asanify.com/blog/news/enterprise-ai-adoption-curve-april-20-2026/)
- [Enterprise AI adoption 2026: why 79% face challenges – Writer](https://writer.com/blog/enterprise-ai-adoption-2026/)
- [Enterprise AI adoption: from pilot purgatory to production scale – TechStoriess](https://www.techstoriess.com/enterprise-ai-adoption-in-2026-from-pilot-purgatory-to-production-scale-ai-integration/)
- [State of AI in the enterprise 2026 – Deloitte NL](https://www.deloitte.com/nl/en/about/press-room/state-of-ai-in-the-enterprise-2026.html)
- [The end of single-model dependency – OpenPR](https://www.openpr.com/news/4486402/the-end-of-single-model-dependency-why-enterprises)
- [Google says it has answers for AI agent sprawl – The Register](https://www.theregister.com/2026/04/22/google_enterprise/)
