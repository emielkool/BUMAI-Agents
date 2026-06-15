---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W19
Datum: 2026-05-08
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 19, 2026

> Synthese op basis van actueel AI-nieuws van 4 mei t/m 8 mei 2026.
> Geen dagbriefings beschikbaar voor deze week; overzicht opgesteld via directe bronnensynthese.

---

## 🏆 Weekhighlights

1. **EU AI Act Omnibus: high-risk deadlines 16 maanden verschoven (7 mei).** Raad en Parlement bereikten een definitieve deal: verplichtingen voor high-risk AI-systemen (biometrie, arbeidsmarkt, krediet) gelden nu per 2 december 2027 i.p.v. 2 augustus 2026. Productgebonden AI (medische apparatuur, machines) krijgt uitstel tot 2028. De ban op AI-deepfakes van identifiseerbare personen en CSAM is wél versneld, net als een kortere watermarking grace period (3 i.p.v. 6 maanden).

2. **Pentagon + NIST: VS institutionaliseert AI governance in één week.** Acht tech-giganten (Amazon, Google, Microsoft, NVIDIA, OpenAI, SpaceX, Reflection, Oracle) werden gecleard voor classified military networks (IL6/IL7). Tegelijk kondigde NIST aan dat Google, Microsoft en xAI pre-launch modelreviews door de overheid laten uitvoeren vóór publieke release – een precedent dat AI formeel in dual-use infrastructuur verankert.

3. **Chinese open-source golf: 4 frontier coding-modellen in 12 dagen.** GLM-5.1 (Z.ai), MiniMax M2.7, Kimi K2.6 en DeepSeek V4 bereiken allen frontier-niveau agentic coding met beduidend lagere inferentiekosten dan westerse gesloten API-providers. De technologische afhankelijkheid van één leveranciersecosysteem wordt structureel minder dwingend.

4. **IBM Think 2026: "AI divide" wordt zichtbare kloof.** IBM presenteerde een blueprint voor het "AI Operating Model" terwijl het de groeiende kloof diagnosticeert: organisaties die AI écht in hun operatie hebben ingebouwd presteren fundamenteel anders dan de rest. Van de $650 miljard jaarlijkse AI-investering rapporteert slechts 29% ROI op generatieve AI en 23% op AI-agents. 79% van enterprises ervaart adoptieproblemen – een stijging van dubbele cijfers tegenover 2025.

5. **Agentic governance-infrastructuur rijpt: ServiceNow, Cloudflare, Gartner.** ServiceNow (met NVIDIA) positioneert zich als de governance-laag voor enterprise-agents, ongeacht waar ze gebouwd of gedraaid worden. Cloudflare's Agents Week toonde dat agents nu autonoom kunnen onboarden, betalen en code deployen – een kwalitatieve sprong in autonomie. Gartner nuanceert de hype: 97% van executives claimt agents te deployen, maar slechts 17% heeft dat daadwerkelijk gedaan.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

Twee bewegingen domineren de week. Aan de frontier-kant: reasoning als standaardarchitectuur (GPT-5.5 uitgerold naar alle ChatGPT-gebruikers, Gemini 3.1 Ultra met 2M token context), terwijl IBM's Watson X Orchestrate multi-agent orkestratie als productieoplossing positioneert. Aan de open-source kant: de Chinese sprint van 4 modellen in 12 dagen toont dat frontier-niveau agentic coding niet langer exclusief is voor westerse API-providers.

De structurele verschuiving deze week zit in agentic autonomie. Cloudflare's "Agents Week" markeert een kantelpunt: agents die zelfstandig infrastructuur kunnen boeken en code deployen, zijn geen demo meer maar werkende productcapaciteit. Dit verschuift de discussie van "kunnen agents iets nuttigs doen?" naar "hoe gover je agents die zelfstandig handelen?"

### 🏛️ Governance & Beleid

De EU AI Act Omnibus-deal van 7 mei is het gouvernantie-evenement van het kwartaal. De 16-maands verschuiving van high-risk deadlines is niet alleen procedureel – het is een erkenning dat de implementatielast voor het bedrijfsleven te zwaar was als one-shot-deadline. Voor NL/BE-bedrijven in sectoren als HR, finance en overheid betekent dit dat de deadline die iedereen als absoluut beschouwde, niet absoluut was.

Tegelijk loopt een tegengestelde trend in de VS: NIST pre-launch reviews en Pentagon IL6/IL7-deals institutionaliseren juist méér AI-toezicht, niet minder. Dit creëert een asymmetrie die voor Europese bedrijven met VS-activiteiten dubbele compliance-architecturen vereist.

### 🔐 Security & Risk

CVE-2025-53773 (CVSS 9.6) in GitHub Copilot is de concrete security-wake-up van de week: prompt injection via pull request-beschrijvingen leidt tot remote code execution. Dit raakt elke ontwikkelomgeving die Copilot integreert – en dat zijn er veel. Het aanvalsoppervlak is niet langer alleen de productie-AI-applicatie, maar de developer-tooling zelf.

Bredere context: 28,3% van CVEs wordt geëxploiteerd binnen 24 uur van disclosure; AI-ondersteunde aanvallen verkorten exploit-tijdlijnen structureel. Een scan van 2 miljoen AI-serviceomgevingen toonde dat AI-infrastructuur stelselmatig slechter beveiligd is dan andere software-categorieën. Alleen 24% van enterprises heeft een dedicated AI security governance-team.

### 📈 Markt & Adoptie

De $650 miljard investeringsflux staat scherp tegenover de ROI-realiteit: 29% gen AI-ROI, 23% AI-agents-ROI, 79% adoptieproblemen. IBM noemt dit de "AI divide" – maar feitelijk gaat het om een implementatiekloof, geen technologiekloof. De technologie werkt; de operationele inbedding ontbreekt.

Agentic AI groeit als marktsegment van $8,5 miljard (2026) naar verwacht $45 miljard (2030) – maar het gat tussen "deployed in naam" (79%) en "echt in productie" (17%) toont dat de groei primair in de belofte zit. Organisaties die dit gat overbruggen, trekken structureel weg van de rest. Eli Lilly's $2,75 miljard AI-deal bevestigt dat buiten de tech-sector concrete, grote AI-waarde wordt gecreëerd.

---

## 💼 Ctac-weekperspectief

- **EU AI Act compliance-herplanning als strategisch venster.** De August-deadline is van de baan. Klanten die compliance-trajecten met urgentie-argumenten moesten starten, hebben nu meer ruimte – maar ook de kans om het gestructureerder te doen. Ctac kan een AI Act readiness assessment positioneren als het gestructureerde startpunt: niet meer brandblussen, maar een gefaseerd compliance-pad dat de nieuwe deadlines (december 2027 voor Annex III, 2028 voor productgebonden AI) als mijlpalen gebruikt. Dit is een direct verkoopbaar aanbod.

- **De "AI divide" is Ctac's marktpositie.** IBM diagnosticeert met gezag het probleem dat Ctac oplost: 79% van enterprises met AI-investeringen die vastlopen op implementatie. De bottlenecks zijn data-architectuur, integratie, governance en change management – precies het snijvlak van Ctac's portfolio. Gebruik IBM's Think 2026-boodschap als extern bewijs in klantgesprekken: "dit is niet Ctac's mening, dit is de industrieconsensus."

- **Developer security vereist directe aandacht in Ctac-teams.** CVE-2025-53773 (CVSS 9.6) in GitHub Copilot is niet abstract: als Ctac-developers Copilot inzetten voor pull request-review of code-generatie, is er een actief exploitpad via kwaadaardige PR-beschrijvingen. Concrete actie: controleer of Copilot-integraties in CI/CD-pipelines zijn beschermd, en zet input-validatie op pull request-content als standaard.

- **Chinese open-source modellen versterken souvereine AI-propositie.** GLM-5.1 en DeepSeek V4 op frontier-niveau met lage inferentiekosten maken on-premise deployments voor datakritische klanten (overheid, finance) aantrekkelijker dan ooit. Ctac's kennis van lokale inference-stacks (vLLM, Ollama) gecombineerd met klantintegratie is een concrete differentiator die steeds minder door hyperscalers kan worden ondervangen.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [IBM Think 2026: Blueprint voor AI Operating Model – newsroom.ibm.com](https://newsroom.ibm.com/2026-05-05-think-2026-ibm-delivers-the-blueprint-for-the-ai-operating-model-as-the-ai-divide-widens)
- [IBM Think 2026: Enterprise AI Sovereignty & Quantum – simplywall.st](https://simplywall.st/stocks/us/software/nyse-ibm/international-business-machines/news/ibm-think-2026-highlights-enterprise-ai-sovereignty-quantum)
- [AI Model Releases May 2026 – llm-stats.com](https://llm-stats.com/ai-news)
- [Cloudflare Agents Week in review – blog.cloudflare.com](https://blog.cloudflare.com/agents-week-in-review/)
- [ServiceNow + NVIDIA: Autonomous AI Agents for Enterprises – blogs.nvidia.com](https://blogs.nvidia.com/blog/servicenow-autonomous-ai-agents-enterprises/)
- [Gartner Hype Cycle for Agentic AI 2026 – gartner.com](https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai)

**Governance & Beleid**
- [EU Raad + Parlement: akkoord AI Act vereenvoudiging (7 mei) – consilium.europa.eu](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [EU AI Act Omnibus deal uitgelegd – modulos.ai](https://www.modulos.ai/blog/eu-ai-act-omnibus-deal/)
- [EU AI Act high-risk deadlines naar 2027 – ppc.land](https://ppc.land/eu-ai-act-gets-its-first-real-haircut-high-risk-deadlines-pushed-to-2027/)
- [IAPP: AI Act Omnibus – what happened and what's next – iapp.org](https://iapp.org/news/a/ai-act-omnibus-what-just-happened-and-what-comes-next)
- [Pentagon AI-deals met 8 tech-bedrijven – CNN Business](https://www.cnn.com/2026/05/01/tech/pentagon-ai-anthropic)
- [NIST pre-launch review Google, Microsoft, xAI – Washington Post](https://www.washingtonpost.com/technology/2026/05/05/google-microsoft-xai-ai-review/)
- [Microsoft, Google, xAI geven VS toegang tot modellen – CNN Business](https://www.cnn.com/2026/05/05/tech/microsoft-google-xai-government-test-ai-models)

**Security & Risk**
- [2026: Year of AI-Assisted Attacks – thehackernews.com](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)
- [We Scanned 1 Million Exposed AI Services – thehackernews.com](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)
- [Cisco State of AI Security 2026 – blogs.cisco.com](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)
- [AI Security Statistics 2026 – practical-devsecops.com](https://www.practical-devsecops.com/ai-security-statistics-2026-research-report/)
- [Supply Chain Attacks & AI Security May 2026 – esecurityplanet.com](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/)

**Markt & Adoptie**
- [AI Investment $650B+ – globenewswire.com](https://www.globenewswire.com/news-release/2026/05/05/3288006/0/en/AI-Investment-Activity-to-Surpass-650-Billion-Annually-as-Enterprise-Adoption-Accelerates-Toward-2026.html)
- [Enterprise AI adoption: 79% faces challenges – writer.com](https://writer.com/blog/enterprise-ai-adoption-2026/)
- [Deloitte: State of AI in the Enterprise 2026 – deloitte.com](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html)
- [Where Enterprises are Actually Adopting AI – a16z.com](https://a16z.com/where-enterprises-are-actually-adopting-ai/)
- [Enterprise AI Agents Mid-Year Report – ampcome.com](https://www.ampcome.com/post/enterprise-ai-agents-2026-mid-year-report)
- [NVIDIA State of AI Report 2026 – blogs.nvidia.com](https://blogs.nvidia.com/blog/state-of-ai-report-2026/)
