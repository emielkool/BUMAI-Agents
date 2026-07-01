---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Maand: 2026-06
Periode: 2026-06-01 / 2026-06-30
Status: Afgerond
tags:
  - maandoverzicht
---

# AI Maandoverzicht – juni 2026

> Synthese van de weekoverzichten W23 t/m W27 (1 juni – 30 juni 2026).

## 🏆 Maandhighlights

1. **Geopolitiek grijpt voor het eerst direct in op frontier-modellen – en het blijft niet bij Anthropic.** Op 12 juni haalde de Amerikaanse overheid Claude Fable 5 en Mythos 5 wereldwijd offline via exportcontrole, drie dagen na lancering – de eerste keer dat een overheid een frontier-model van de markt haalt wegens nationale veiligheid. Fable 5 keerde later beperkt terug, eerst credits-only (23 juni) en aan het einde van de maand opnieuw bevestigd als gesuspendeerd voor niet-Amerikanen. Tegen maandeinde trof dezelfde overheidsbemoeienis ook OpenAI: het Witte Huis eiste "klant-voor-klant"-goedkeuring voor toegang tot GPT-5.6. Wat in mei nog een AI-veiligheidsdiscussie was, is in juni omgeslagen in actief precedent voor exportbeleid als instrument tegen AI-labs.

2. **Prompt injection en agentic security werden de constante van de maand.** Elke week leverde nieuwe, actief misbruikte kwetsbaarheden: de MCP-architectuurfout (7.000+ servers, 150M+ downloads), CVE-2025-53773 in GitHub Copilot (CVSS 9.6, RCE via PR-beschrijvingen), kritieke Semantic Kernel-CVE's, de LiteLLM supply-chain-aanval (47.000 downloads vergiftigde package in 40 minuten) en CVE-2026-5027 tegen 7.000+ LangFlow/LangChain-servers. OWASP publiceerde de Agentic Top 10 2026; onderzoek bevestigde dat 94% van LLM-agents kwetsbaar is voor prompt injection. Waar mei de escalatie liet zien, bevestigde juni dat dit een permanent, onoplosbaar risico is dat structureel gemanaged moet worden.

3. **Anthropic domineerde de maand cijfermatig, ondanks de politieke tegenwind.** Claude werd geïntegreerd in Excel (750 miljoen gebruikers), Anthropic diende vertrouwelijk een IPO-aanvraag in bij een waardering van $965 miljard, en overtrof OpenAI voor het eerst zowel in mondiale LLM-omzet (31,4% vs. 29%) als enterprise-adoptie (34,4% vs. 32,3%), gedreven door Claude Code. De maand sloot af met de lancering van Claude Sonnet 5 (30 juni) – bijna-Opus-prestaties voor een derde van de prijs, expliciet gericht op agentic workflows en daarmee een directe verlaging van de drempel voor enterprise-adoptie.

4. **De EU AI Act-klok tikte de hele maand door, met een korte adempauze.** Van "acht weken" begin juni naar "32 dagen" eind juni telde elke weekbriefing af naar 2 augustus 2026. Het Digital Omnibus-akkoord verschoof de hoog-risico (Annex III) verplichtingen naar december 2027, maar de kernverplichtingen – met name Artikel 50-transparantie en GPAI-eisen – bleven onveranderd hard op 2 augustus. De Code of Practice voor AI-contentmarkering werd in de loop van juni gefaseerd gepubliceerd, wat compliance-teams eindelijk concrete implementatiedetails gaf na maanden onzekerheid.

5. **Het model- en platformlandschap versplinterde verder, met opkomst van nieuwe spelerstypen.** Microsoft lanceerde bij Build 2026 zeven eigen MAI-modellen en braak zo met zijn OpenAI-afhankelijkheid; Google herwon terrein met Gemini 2.5 Pro Deep Think; open-source modellen (GLM-5.1, Kimi K2.6/2.7, DeepSeek V4, MiniMax M2.7/M3) evenaarden gesloten frontier-prestaties tegen een fractie van de prijs. SpaceX kocht AI-code-editor Cursor voor $60 miljard en kondigde een eigen 1,5 biljoen-parameter codeermodel aan – een teken dat industriële spelers buiten de traditionele AI-labs nu zelf frontier-modellen bouwen. De Amerikaanse exportrestricties versnelden bovendien de opkomst van Aziatische alternatieven (Sakana AI's Fugu, Kimi K2.7) die het gat vulden.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

Juni was de maand waarin het "één leverancier, één model"-tijdperk definitief eindigde. Microsoft's zeven MAI-modellen (met MAI-Thinking-1 op Opus 4.6-niveau) en Google's Gemini 2.5 Pro Deep Think braken de aanname dat frontier-kwaliteit voorbehouden is aan Anthropic en OpenAI. Tegelijk bewees de open-source stroom (GLM-5.1, Kimi-serie, DeepSeek V4, MiniMax) dat lokaal hostbare modellen commercieel concurrerend zijn geworden – een trend die versnelde doordat Amerikaanse exportbeperkingen westerse frontier-modellen minder betrouwbaar beschikbaar maakten. Aan het einde van de maand verlaagde Claude Sonnet 5 de prijsdrempel voor agentic AI verder, terwijl SpaceX's overname van Cursor een geheel nieuwe categorie speler introduceerde: niet-AI-labs die zelf frontier-codeermodellen trainen. De vraag verschoof structureel van "welk model is het beste" naar "welke combinatie van modellen, kosten en beschikbaarheidsrisico past bij mijn architectuur."

### 🏛️ Governance & Beleid

De EU AI Act bleef het meest voorspelbare governance-verhaal: een gestage aftelling naar 2 augustus, verzacht door het Digital Omnibus (Annex III naar december 2027) maar onveranderd hard op Artikel 50-transparantie en GPAI-verplichtingen. De echt disruptieve governance-ontwikkeling kwam echter uit de VS: het offline halen van Fable 5/Mythos 5 via exportcontrole, gevolgd door soortgelijke overheidsbemoeienis bij OpenAI's GPT-5.6, normaliseert directe statelijke controle over frontier-modelreleases. Dit is een fundamenteel ander governance-model dan de EU-aanpak van gereguleerde marktoegang, en het vergroot de transatlantische divergentie: Europa reguleert via wetgeving en documentatieplicht, de VS grijpt in via exportbeleid en nationale veiligheid. Voor internationaal opererende organisaties betekent dit twee onafhankelijke compliance-assen die niet synchroon lopen.

### 🔐 Security & Risk

Geen andere maand liet zo'n aaneengesloten reeks concrete, actief misbruikte kwetsbaarheden zien: de MCP-ontwerpfout, GitHub Copilot RCE, Semantic Kernel-CVE's, de LiteLLM supply-chain-aanval en CVE-2026-5027 tegen LangFlow/LangChain volgden elkaar wekelijks op. De publicatie van OWASP's Agentic Top 10 2026 en het onderzoek dat 94% van LLM-agents kwetsbaar bevond voor prompt injection bevestigen: dit is geen incident meer, maar een structureel kenmerk van de huidige generatie agentic AI. Tegen het einde van de maand verschoof het narratief van "kwetsbaarheden ontdekken" naar "agents als autonome insider-dreiging" – een prompt injection kan nu direct leiden tot databases leegmaken of back-ups wissen. Machine-identiteiten die mensen 82:1 overtreffen, terwijl 29% van agents zonder IT-goedkeuring draait, maakt dit een governance-probleem dat traditionele IAM niet aankan.

### 📈 Markt & Adoptie

De markt liet in juni een duidelijke winnaar zien: Anthropic, dat OpenAI zowel in omzet als enterprise-adoptie voorbijstreefde ondanks – of deels dankzij – de politieke tegenwind rond zijn meest geavanceerde modellen. Tegelijk bleef de onderliggende adoptieparadox uit mei bestaan: twee derde van enterprises zit vast in de pilotfase, ook al is agentic infrastructuur (A2A nu bij de Linux Foundation, MCP als industriestandaard, Microsoft Agent 365 GA) volledig productierijp. De $60 miljard SpaceX-Cursor-deal en de aanhoudende hyperscaler-capex (Microsoft en Google beide >$20-39% groei) tonen dat kapitaal ongehinderd naar AI blijft stromen, terwijl de vertaalslag naar bedrijfswaarde – zoals in mei – de bottleneck blijft.

---

## 💼 Ctac-maandperspectief

- **Artikel 50-compliance is het meest urgente, tijdgebonden aanbod van dit moment.** Met nog vier tot vijf weken tot 2 augustus en een inmiddels gepubliceerde Code of Practice, is er geen ruimte meer voor uitstel bij klanten die chatbots of AI-gegenereerde content richting eindgebruikers inzetten. Positioneer een compacte, uitvoerbare compliance-sprint (2-4 weken) specifiek gericht op transparantiemeldingen en contentmarkering, apart van het bredere en minder urgente Annex III-traject dat nu tot december 2027 loopt.

- **Bouw agent-security tot een verplicht onderdeel van elk agentic AI-project, niet als losstaand adviesproduct.** De aaneenschakeling van MCP-, Copilot-, Semantic Kernel- en LangFlow-kwetsbaarheden in juni bewijst dat prompt injection een permanent architectuurrisico is. Elke Ctac-delivery met agentic AI moet vanaf dag één een security-baseline bevatten: dependency-controle, IAM voor machine-identiteiten, en audit-logging. Dit is inmiddels kwaliteitsvereiste, geen upsell.

- **Adviseer klanten expliciet over leverancierrisico na de exportcontrole-precedenten.** Het offline halen van Fable 5/Mythos 5 en de beperkingen op GPT-5.6 laten zien dat afhankelijkheid van één Amerikaans frontier-model een operationeel continuïteitsrisico is geworden, los van prijs of prestatie. Adviseer klanten in gereguleerde sectoren (overheid, finance, zorg) een multi-model-architectuur met expliciete fallback-opties, inclusief open-weight- of Europese alternatieven waar soevereiniteit telt.

- **Gebruik Claude Sonnet 5 en de bredere prijsdaling om PoC-drempels te verlagen.** Nu agentic AI-capaciteit tegen een fractie van de eerdere prijs beschikbaar is (Sonnet 5, GLM-5.1, Kimi, DeepSeek), kan Ctac sneller en goedkoper pilots opzetten bij klanten die eerder terugschrokken voor de kosten van frontier-modellen. Combineer dit met de sterkere positie van Claude Code in enterprise-adoptie om een concreet Q3-aanbod te bouwen.

- **Volg de Microsoft-stack-verschuiving actief: MAI-modellen, hogere M365-prijzen en Agent 365 GA veranderen het gesprek met bestaande klanten.** De 16%-prijsstijging op M365 door ingebedde Copilot-functionaliteit levert een directe aanleiding voor ROI-gesprekken; Microsoft's eigen modelfamilie vergroot tegelijk de keuzematrix die Ctac als onafhankelijk adviseur kan invullen. Update de interne modelkeuze- en kostenmatrix voor klantadvies vóór het derde kwartaal.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Anthropic – Claude Opus 4.8 release](https://www.anthropic.com/news/claude-opus-4-8)
- [Microsoft Build 2026 – zeven MAI-modellen](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [TechTimes – Claude in Excel](https://www.techtimes.com/articles/317988/20260608/claude-now-works-inside-excel-microsoft-drops-anthropics-ai-spreadsheet-750-million-people-use)
- [Google Blog – Gemini 2.5 Deep Think rollout](https://blog.google/products-and-platforms/products/gemini/gemini-2-5-deep-think/)
- [VentureBeat – GLM-5.1 verslaat gesloten modellen](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4)
- [VentureBeat – Anthropic vs. OpenAI enterprise-adoptie](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead/)

**Governance & Beleid**
- [artificialintelligenceact.eu – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act – Artikel 50 transparantieregels](https://artificialintelligenceact.eu/transparency-rules-article-50/)
- [TechCrunch – VS haalt Anthropic-modellen offline](https://techcrunch.com/2026/06/12/anthropics-safety-warnings-may-just-backfired-the-government-has-pulled-the-plug-on-its-most-powerful-ai/)
- [Whitehouse.gov – AI Innovation and Security Executive Order](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)

**Security & Risk**
- [SecurityWeek – MCP by-design flaw](https://www.securityweek.com/by-design-flaw-in-mcp-could-enable-widespread-ai-supply-chain-attacks/)
- [Microsoft Security Blog – RCE in AI agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [VentureBeat – LiteLLM supply chain-aanval](https://venturebeat.com/security/supply-chain-incidents-openai-anthropic-meta-release-surface-vendor-questionnaire-matrix)
- [VentureBeat – Machine identities 82:1](https://venturebeat.com/security/machine-identities-outnumber-humans-82-to-1-legacy-iam-cant-keep-up)
- [Cisco – State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)

**Markt & Adoptie**
- [Fortune – Anthropic IPO $965B waardering](https://fortune.com/2026/06/01/anthropic-confidentially-files-ipo-965-billion-valuation/)
- [VentureBeat – A2A & MCP interoperabiliteit naar Linux Foundation](https://venturebeat.com/ai/ais-big-interoperability-moment-why-a2a-and-mcp-are-key-for-agent-collaboration)
- [CIO Dive – Microsoft en Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Computable – Benelux koploper in AI, talentgebrek](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
