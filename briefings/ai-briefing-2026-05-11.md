---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-11
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 11 mei 2026

## 🔑 Highlights van de dag

- **Anthropic Claude Opus 4.7** is algemeen beschikbaar (GA sinds 16 april) met substantieel betere vision-capaciteiten, harder coderen op complexe taken, en een nieuw bijgeleverd product: Claude Design voor visuele output. Claude Security (code-kwetsbaarheidsscanning) is nu in public beta voor Enterprise-klanten.
- **EU AI Act-eindsprint:** Op 8 mei opende de Commissie een consultatie over transparantierichtlijnen; op 7 mei vereenvoudigde de EU de AI-regels voor innovatie en verbood 'nudification'-apps. Volledige toepasselijkheid volgt op 2 augustus 2026 — minder dan drie maanden.
- **1 miljoen blootgestelde AI-diensten** gevonden bij een grootschalige internetscan in mei 2026: misconfiguraties, ontbrekende authenticatie en gelekte gebruikersdata domineren het beeld. AI-infrastructuur blijkt slechter beveiligd dan vrijwel elke andere software-categorie.
- **Microsoft en Google domineren de enterprise-AI-markt** (Gartner). Google lanceerde Agentic Data Cloud; AWS en OpenAI sloten een partnerschap voor Codex op Amazon Bedrock. Multi-cloud AI-interoperabiliteit wint terrein.
- **Nederland:** 10 sectorale toezichthouders aangesteld voor AI Act-handhaving; slechts 42% van organisaties heeft een volledig AI-beleid. Cybersec Netherlands 2026 zet AI-gedrag en digitale soevereiniteit centraal.

---

## 🧠 Technologie & Modellen

**Claude Opus 4.7 (Anthropic, GA):** De meest opvallende release van de afgelopen weken is Opus 4.7, beschikbaar via Claude-producten, API, Amazon Bedrock, Google Vertex AI en Microsoft Foundry. Sterke punten: complexe en langlopende codeertaken, hogere beeldresolutie bij vision-taken, en output-verificatie vóór rapportage. Naast Opus 4.7 lanceerde Anthropic *Claude Design* (visuele samenwerkingstool voor prototypes, slides en one-pagers) en *Claude Security* (code-kwetsbaarheidsscanning) in public beta voor Enterprise.
- Bron: [Anthropic nieuws](https://www.anthropic.com/news)

**Agentic coding – wedloop OpenAI vs. Anthropic:** OpenAI bracht eerder dit jaar GPT-5.3 Codex uit (25% sneller dan 5.2), terwijl Anthropic zijn agentic coding-model minutenlang vervroegd publiceerde om de concurrent voor te zijn. Anthropic's eigen *2026 Agentic Coding Trends Report* laat zien dat software-engineering ~50% van alle agentische activiteit voor zijn rekening neemt.
- Bron: [TechCrunch – OpenAI vs Anthropic agentic coding](https://techcrunch.com/2026/02/05/openai-launches-new-agentic-coding-model-only-minutes-after-anthropic-drops-its-own/)

**Windows als AI-native OS:** Microsoft herschrijft Windows 11 als een platform voor autonome AI-agents die beveiligd taken uitvoeren op 1,4 miljard apparaten. Dit is strategisch: Microsoft verplaatst het AI-battleground van de cloud naar het endpoint.
- Bron: [VentureBeat – Microsoft remakes Windows](https://venturebeat.com/ai/microsoft-remakes-windows-for-an-era-of-autonomous-ai-agents)

---

## 🏛️ Governance & Ethiek

**EU AI Act – finale rechte lijn:** De volledige verordening wordt van toepassing op 2 augustus 2026. Concrete mijlpalen van deze week: consultatie over conceptrichtlijnen voor AI-transparantieverplichtingen (8 mei) en vereenvoudiging van regels voor innovatie inclusief verbod op nudification-apps (7 mei). Lidstaten moeten uiterlijk 2 augustus ook een nationale AI-sandbox hebben.
- Bronnen: [EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/) | [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Nationale implementatie Nederland:** Tien toezichthouders — waaronder ACM, AP en RDI — bewaken sectorgericht de naleving. Onderlinge kennisdeling staat nog in de kinderschoenen. Computable meldt dat Europese tech-CEO's de politiek oproepen tot meer daadkracht op AI-beleid.
- Bronnen: [Computable – tien toezichthouders](https://www.computable.nl/2026/04/22/tien-toezichthouders-bewaken-naleving-ai-verordening/) | [Computable – Cybersec Netherlands](https://www.computable.nl/2026/05/06/ai-gedrag-en-soevereiniteit-centraal-op-cybersec-netherlands-2026/)

---

## 🔐 Security & Risk

**1 miljoen blootgestelde AI-diensten (The Hacker News, mei 2026):** Een scan van ruim 2 miljoen hosts identificeerde 1 miljoen onbeveiligde AI-diensten: geen authenticatie bij fresh installs, hardcoded credentials, applicaties draaiend als root, en blootgestelde gebruikersconversaties. De conclusie is onthutsend: AI-infrastructuur is slechter geconfigureerd dan vrijwel iedere andere software-categorie ooit onderzocht.
- Bron: [The Hacker News – 1M exposed AI services](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)

**2026: jaar van AI-ondersteunde aanvallen:** 28,3% van CVE's wordt nu binnen 24 uur na disclosure uitgebuit. AI-gegenereerde malware ontwijkt traditionele detectietools. Minder dan 1% van kwetsbaarheden die AI-systemen vinden, worden daadwerkelijk gepatcht — een kritische kloof tussen detectie en herstel.
- Bron: [The Hacker News – AI-Assisted Attacks](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)

**Shadow AI in enterprises:** Medewerkers delen klantdata, financiële informatie en interne documenten met niet-goedgekeurde AI-tools, met ongecontroleerde data-exposure en uitgebreide aanvalsvlakken als gevolg.
- Bron: [The Hacker News – Shadow AI](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html)

---

## 📈 Markt & Adoptie

**Microsoft en Google aan kop (Gartner):** Microsoft domineert enterprise-brede AI-adoptie dankzij zijn partner- en platform-ecosysteem; Google wint in agentische enterprise-AI met zijn geïntegreerde stack. AWS sluit een partnerschap met OpenAI om Codex en de nieuwste modellen op Amazon Bedrock aan te bieden.
- Bronnen: [CIO Dive – Microsoft/Google domineren](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [AWS Weekly Roundup mei 2026](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-whats-next-with-aws-2026-amazon-quick-openai-partnership-and-more-may-4-2026/)

**Google Agentic Data Cloud:** Gepresenteerd op Google Cloud Next '26, met een AI-native architectuur die legacy-dataplatformen omvormt tot redenerende engines. Tevens groeit multicloud AI-interoperabiliteit: Google en AWS werken al samen; Microsoft sluit later in 2026 aan.
- Bron: [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)

**Google investeert $40 miljard in Anthropic:** Direct $10 miljard bij een waardering van $350 miljard, met nog $30 miljard conditioneel. Dit consolideert de strategische alliantie tussen Google en Anthropic verder.
- Bron: [TechCrunch – Google investeert in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)

---

## 💡 Ctac-relevantie

**Governance-deadline nadert:** Op 2 augustus 2026 — minder dan drie maanden — wordt de EU AI Act volledig van kracht. Ctac-klanten, met name in de publieke sector en finance, zijn naar verwachting nog niet compliant. Dit is een concreet, tijdgebonden aanknopingspunt voor een AI Act readiness-dienst: gap-analyse, risicoklassificatie en documentatiebegeleiding.

**AI Security als propositie:** De schokkende bevindingen rond blootgestelde AI-infrastructuur geven Ctac een kans om AI Security expliciet onderdeel te maken van projectaanbod. Zeker bij klanten die zelf AI-diensten deployen (chatbots, RAG-pipelines, agents), is een security-review van de AI-stack een directe, verkoopbare toegevoegde waarde.

**Agentic AI integreren in delivery:** Claude Opus 4.7 en vergelijkbare modellen zijn nu sterk genoeg voor complexe software-engineering-taken. Ctac's AI-engineer kan verkennen hoe deze modellen de interne delivery versnellen — denk aan code-review, testgeneratie en architectuurvalidatie als geautomatiseerde stap in CI/CD.

**Shadow AI bij opdrachtgevers:** Slechts 42% van organisaties heeft een volledig AI-beleid. Ctac kan opdrachtgevers helpen een pragmatisch AI-governancebeleid op te stellen — niet als papieren oefening, maar als werkend raamwerk met tooling en training.

---

## 📚 Bronnen & verder lezen

- [Anthropic nieuws – Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [TechCrunch – OpenAI vs Anthropic agentic coding](https://techcrunch.com/2026/02/05/openai-launches-new-agentic-coding-model-only-minutes-after-anthropic-drops-its-own/)
- [VentureBeat – Microsoft remakes Windows for autonomous AI agents](https://venturebeat.com/ai/microsoft-remakes-windows-for-an-era-of-autonomous-ai-agents)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act regelgevingskader](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Computable – tien toezichthouders AI-verordening](https://www.computable.nl/2026/04/22/tien-toezichthouders-bewaken-naleving-ai-verordening/)
- [Computable – Cybersec Netherlands 2026](https://www.computable.nl/2026/05/06/ai-gedrag-en-soevereiniteit-centraal-op-cybersec-netherlands-2026/)
- [The Hacker News – 1M exposed AI services](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)
- [The Hacker News – 2026: Year of AI-Assisted Attacks](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)
- [The Hacker News – Shadow AI in Enterprises](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html)
- [CIO Dive – Microsoft & Google rule enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [AWS Weekly Roundup – OpenAI partnership mei 2026](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-whats-next-with-aws-2026-amazon-quick-openai-partnership-and-more-may-4-2026/)
- [TechCrunch – Google investeert $40B in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
