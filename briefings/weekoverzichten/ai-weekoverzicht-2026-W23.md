---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W23
Datum: 2026-06-05
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 23, 2026

> Synthese van de dagbriefings van 1 juni t/m 3 juni 2026.
> Dagbriefings voor donderdag 4 en vrijdag 5 juni waren niet beschikbaar op moment van opstellen.

---

### Maandag 1 juni

→ Dagbriefing: [ai-briefing-2026-06-01.md](../ai-briefing-2026-06-01.md)

**Highlights:**
- **Anthropic Opus 4.8 met Dynamic Workflows**: Claude Code spawnt honderden parallelle subagents voor codebase-brede migraties – een serieuze stap richting autonome softwareontwikkeling.
- **EU AI Act volledig van kracht per 2 augustus 2026**: organisaties hebben nog twee maanden; het 'AI omnibus'-akkoord verschuift high-risk deadlines naar december 2027, maar transparantieplichten gelden wél per augustus.
- **95% van enterprises ziet nog geen zinvolle ROI** op AI-investeringen (MIT-onderzoek), terwijl investeringen en consolidatie naar minder vendors versnellen.

**Ctac-relevantie van de dag:** De EU AI Act deadline maakt compliance-advies direct verkoopbaar voor klanten in overheid, zorg en finance. Dynamic Workflows in Opus 4.8 opent een concrete propositie voor klanten met grote legacy-codebases zoals SAP-migraties.

---

### Dinsdag 2 juni

→ Dagbriefing: [ai-briefing-2026-06-02.md](../ai-briefing-2026-06-02.md)

**Highlights:**
- **GLM-5.1 (754B, open-source) overtreft gesloten frontier-modellen** op SWE-Bench Pro en agentic benchmarks – een directe uitdaging aan de aanname dat dure API's noodzakelijk zijn.
- **OpenAI Daybreak lanceert AI-aangedreven kwetsbaarheidsdetectie** voor repositories, geïntegreerd bij Akamai, Cisco en CrowdStrike: offensieve AI voor defensieve security is nu reëel.
- **Benelux Europees koploper in AI-adoptie** (NL 61%, BE 62%), maar 58% van bedrijven noemt het talentgebrek als grootste blokkade voor verdere uitrol.

**Ctac-relevantie van de dag:** Het talentgebrek in de Benelux is een directe marktopening voor Ctac's AI enablement-diensten. SAP-klanten worden automatisch beïnvloed door het Nvidia enterprise agent platform – het moment om hen te begeleiden bij verantwoorde adoptie is nu.

---

### Woensdag 3 juni

→ Dagbriefing: [ai-briefing-2026-06-03.md](../ai-briefing-2026-06-03.md)

**Highlights:**
- **Anthropic breidt Project Glasswing uit naar 150+ organisaties** (Okta, Samsung, NATO, ENISA) in 15+ landen: Claude Mythos – te gevaarlijk voor publieke release – wordt ingezet bij kritische infrastructuur voor offensieve én defensieve cybersecurity.
- **EU AI Act T-60**: per 2 augustus heeft de Europese Commissie volledige handhavingsbevoegdheid over GPAI-aanbieders, inclusief boetes; de Wetenschappelijke Raad (60 experts) en Adviesforum zijn operationeel.
- **Enterprise AI structureel vast in pilots**: tweederde bereikt geen productie; het bottleneck is niet het model maar runtime-architectuur (orkestratie, audit trails, datagrounding).

**Ctac-relevantie van de dag:** EU AI Act compliance is nu urgent verkoopbaar in 60 dagen; agentic runtime-architectuur (niet modelselectie) is het nieuwe differentiatiegebied waarop Ctac's AI-unit een propositie kan bouwen.

---

### Donderdag 4 juni

*(geen briefing beschikbaar voor deze dag)*

---

### Vrijdag 5 juni

*(geen briefing beschikbaar voor deze dag)*

---

## 🏆 Weekhighlights

- **Anthropic maakt een gecombineerde sprint: Opus 4.8, Project Glasswing en IPO-filing tegelijk.** Opus 4.8 (Dynamic Workflows) werd 28 mei gelanceerd – 41 dagen na de vorige versie. Glasswing groeide naar 150+ organisaties waaronder NATO en ENISA. Tegelijk diende Anthropic vertrouwelijk een S-1 in bij een geïmpliceerde waarde van ~$965 miljard. Dit is geen toeval: Anthropic zet gericht aan tot commercialisering vóór het IPO-moment.

- **GLM-5.1 bewijst: open-source frontier-AI is productierijp.** Z.ai's 754B-parametersmodel haalt 95,3 op AIME 2026, verslaat Claude Opus 4.6 en GPT-5.4 op SWE-Bench Pro, en is volledig lokaal te hosten via vLLM of SGLang. De aanname dat gesloten API's noodzakelijk zijn voor top-prestaties is definitief achterhaald.

- **EU AI Act T-60: het compliance-venster sluit.** Per 2 augustus 2026 heeft de Europese Commissie volledige handhavingsbevoegdheid, inclusief boetes. De Wetenschappelijke Raad (60 experts) en het Adviesforum zijn operationeel. Het 'AI omnibus'-akkoord geeft extra tijd voor high-risk toepassingen (december 2027), maar transparantieplichten (Art. 50) gelden wél per augustus – ook voor al lopende systemen.

- **Enterprise AI zit structureel vast op de drempel van productie.** 95% van bedrijven ziet geen zinvolle ROI (MIT-onderzoek); tweederde rolt AI niet succesvol uit voorbij de pilot. De bottleneck is niet het model – het is de runtime-architectuur: orkestratie, audit trails en datagrounding. Context architecture (niet RAG) wordt de nieuwe standaard voor agentische enterprise-toepassingen.

- **Offensieve AI voor defensieve security is operationeel geworden.** OpenAI lanceerde Daybreak (GPT-5.5 die repositories doorzoekt op aanvalspaden, integratie bij Cisco en CrowdStrike), terwijl AWS Kiro een 18-maandenproject in 76 dagen oplevert. Tegelijk lekten drie AI-coding-agents secrets via één prompt injection-aanval – de aanvalsdichtheid groeit gelijk op met de defensieve capaciteiten.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De week laat een structurele verschuiving zien: de dominantie van gesloten frontier-modellen is aan het einde. GLM-5.1 (open-source, 754B) en de Kimi/DeepSeek/Qwen3-klasse tonen dat state-of-the-art agentic performance nu lokaal beschikbaar is. Tegelijk versnelt Anthropic zijn cyclus met Opus 4.8 – 41 dagen na de vorige release, met Dynamic Workflows als bewijs dat de architectuur richting autonome orkestratie schuift.

Het patroon van de week: elk groot lab positioneert zich op een andere as. Anthropic: veiligheid en enterprise-compliance (Glasswing, IPO). OpenAI: coding en security (Codex 5×, Daybreak, GPT-5.5-Cyber). Google: kostenleiderschap en integratie (Gemini 3.5 Flash standaard in Search, Google Cloud $20B+). De enkelvoudige "welk model is het beste?"-vraag is vervangen door "welke architectuur past bij mijn use case?"

---

### 🏛️ Governance & Beleid

De 60-dagenklok domineert het governance-beeld van de week. Concreet voor Nederlandse organisaties: transparantieverplichtingen (Art. 50) gaan per 2 augustus in. Dit geldt voor alle systemen die al live zijn én waarmee EU-burgers interacteren. De handhavingsinfrastructuur is nu compleet – de Wetenschappelijke Raad, het Adviesforum én de nationale toezichthouders zijn operationeel.

Positief nieuws voor implementatieteams: het AI omnibus-akkoord verschuift de high-risk-verplichtingen (biometrie, kritieke infrastructuur, onderwijs, arbeidsmarkt) naar december 2027 – een significante verschuiving. Maar het venster voor transparantie-compliance is definitief gesloten. Wie nu geen actie onderneemt, wacht op de eerste handhavingsbeschikking.

---

### 🔐 Security & Risk

De week tekent een paradox in de AI-security: de offensieve en defensieve capaciteiten groeien gelijktijdig en in hetzelfde ecosysteem. Anthropic's Glasswing stelt NATO en ENISA in staat om Mythos in te zetten voor kwetsbaarheidsdetectie – maar hetzelfde model is "te gevaarlijk voor publieke release." OpenAI's Daybreak scant code op aanvalspaden – maar drie AI-coding-agents lekten dezelfde week secrets via een simpele prompt injection.

NIST kwalificeert prompt injection als "de grootste security-fout van generatieve AI." Slechts een minderheid van enterprise AI-deployments heeft runtime-beveiligingsmaatregelen. De combinatie van massale agent-uitrol (33% van organisaties, 3× in twee kwartalen) zonder structurele security-architectuur is het concrete risico van dit moment.

---

### 📈 Markt & Adoptie

De Benelux-cijfers van deze week zijn opmerkelijk: 61% van de Nederlandse bedrijven gebruikt AI (van 49% een jaar eerder) – Europees koploper. Maar 58% noemt talent als kritieke blokkade. KPMG registreert een verdrievoudiging in agentic AI-adoptie in slechts twee kwartalen. Google Cloud boekte $20+ miljard in Q1 (+63% j/j).

De markt beweegt langs twee assen tegelijk: enorme investeringsgroei én structurele adoptieknelpunten. 95% van enterprises ziet nog geen ROI. Het onderscheidende verhaal voor dienstverleners is niet meer "wij implementeren AI" – dat doet iedereen. Het is "wij brengen AI succesvol naar productie." Dat is het gat dat de markt biedt.

---

## 💼 Ctac-weekperspectief

- **Start EU AI Act compliance-gesprekken nu – het venster sluit letterlijk.** Met 60 dagen tot volledige toepasselijkheid en een volledig operationele handhavingsinfrastructuur is er geen uitstel meer. Prioriteer klanten in overheid, zorg en finance. Een gap-analyse gericht op Art. 50-transparantievereisten (gebruikersinformatieplicht) is direct inzetbaar – wie in augustus een boete wil vermijden, moet in juni beginnen.

- **Positioneer Ctac als de "pilot-naar-productie"-partner voor de 95% zonder ROI.** MIT-onderzoek en KPMG-data bevestigen hetzelfde: technologie is niet het probleem. Orkestratie, audit trails en datagrounding wél. Ctac's meerwaarde zit niet in het bouwen van modellen of het verkopen van licenties, maar in het verbinden van AI aan bestaande systemen, processen en governance. Bouw dit verhaal in presentaties, pitches en klantgesprekken voor H2 2026.

- **Benelux-talentkloof = directe vraag naar Ctac's AI enablement-diensten.** 58% van bedrijven in de Benelux noemt talent als hun grootste AI-blokkade. Ctac heeft de combinatie die de markt zoekt: domeinkennis (SAP, Microsoft), AI-engineering en change management. Maak dit aanbod zichtbaar – als concreet product, niet als vage dienst – richting HR-directeuren en CTO's van middelgrote organisaties.

- **SAP-klanten zijn het kortste pad naar agentic AI-business.** Nvidia's agent platform (met SAP als early adopter) én de Opus 4.8 dynamic workflows zijn direct van toepassing op SAP-omgevingen. Ctac's SAP-expertise gecombineerd met AI-agentimplementatie is een unieke propositie die nu actueel is. Zet een concrete pilot op bij één SAP-klant in Q3 2026 – dat levert een referentiecase op het moment dat de hele markt ernaar zoekt.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Anthropic – Claude Opus 4.8 release](https://www.anthropic.com/news/claude-opus-4-8)
- [TechCrunch – Anthropic Opus 4.8 met Dynamic Workflows](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/)
- [VentureBeat – Opus 4.8 details en fast mode](https://venturebeat.com/technology/anthropics-claude-opus-4-8-is-here-with-3x-cheaper-fast-mode-and-near-mythos-level-alignment)
- [TechCrunch – RSI is de nieuwe AGI](https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/)
- [GLM-5.1 op Hugging Face – Z.ai](https://huggingface.co/zai-org/GLM-5.1)
- [VentureBeat – GLM-5.1 verslaat gesloten modellen](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4)
- [Google I/O 2026 – alle aankondigingen](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [OpenAI – ChatGPT Agent lancering](https://openai.com/index/introducing-chatgpt-agent/)
- [OpenAI – GPT-Rosalind life sciences](https://openai.com/index/introducing-gpt-rosalind/)
- [VentureBeat – Nvidia enterprise AI agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [VentureBeat – Context architecture vervangt RAG](https://venturebeat.com/data/context-architecture-is-replacing-rag-as-agentic-ai-pushes-enterprise-retrieval-to-its-limits)
- [VentureBeat – Agentic coding: spec-driven development](https://venturebeat.com/orchestration/agentic-coding-at-enterprise-scale-demands-spec-driven-development)
- [OpenAI – Gartner 2026 leader Enterprise AI Coding Agents](https://openai.com/index/gartner-2026-agentic-coding-leader/)

**Governance & Beleid**
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act governance en handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [EC – AI Act handhaving krijgt expert support](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support)
- [EC Digital Strategy – AI Act kader](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Computable – Benelux koploper in AI, talentgebrek](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)

**Security & Risk**
- [Anthropic – Project Glasswing](https://www.anthropic.com/glasswing)
- [TechCrunch – Anthropic scales Claude Mythos to 15+ countries](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)
- [OpenAI – Daybreak kwetsbaarheidsdetectie](https://openai.com/daybreak/)
- [The Hacker News – OpenAI Daybreak lancering](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html)
- [The Hacker News – Enterprise AI-risico rapport](https://thehackernews.com/2026/05/new-ai-usage-report-enterprise-ai-risk.html)
- [VentureBeat – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [TechCrunch – Prompt injection AI browsers](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)

**Markt & Adoptie**
- [TechCrunch – Anthropic files to go public (S-1)](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/)
- [TechCrunch – Anthropic raises $65B, nears $1T valuation](https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/)
- [CIO Dive – Google Cloud tops $20B](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [VentureBeat – Agentic AI adoptie versnelt (KPMG)](https://venturebeat.com/ai/the-great-ai-agent-acceleration-why-enterprise-adoption-is-happening-faster-than-anyone-predicted)
- [TechCrunch – Robinhood AI agentic trading](https://techcrunch.com/2026/05/27/robinhood-now-lets-your-ai-agents-trade-stocks/)
- [CIO Dive – Microsoft en Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Microsoft – State of Global AI Diffusion 2026](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)
- [VentureBeat – The Agentic Reckoning: runtime-architectuur](https://venturebeat.com/resources/the-agentic-reckoning-enterprise-ai-organizations-have-a-runtime-problem-not-a-model-problem)
- [Ctac – Microsoft 365 E7 Frontier Suite](https://www.ctac.nl/microsoft-365-e7)
- [Ctac – Ctac en Pipple bundelen krachten](https://www.ctac.nl/ctac-en-pipple-bundelen-krachten-voor-innovatieve-ai-oplossingen)
