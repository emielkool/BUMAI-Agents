---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-02
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaving start vandaag** – Per 2 augustus 2026 treedt de volledige handhaving van de EU AI Act in werking: de AI Office mag nu corrigerende maatregelen opleggen en boetes uitschrijven aan aanbieders van GPAI-modellen. Transparantievereisten (AI moet zich als AI kenbaar maken) gelden nu ook formeel.
- **Massale prompt injection-aanval op AI coding agents** – Onderzoekers onthulden dat Claude Code, Gemini CLI en GitHub Copilot gelijktijdig werden getroffen door een prompt injection-aanval die secrets lekte bij organisaties. Ironisch genoeg voorspelde Anthropic's eigen system card dit risico al.
- **Microsoft lanceert Frontier Company** – Met een investering van $2,5 miljard en 6.000 specialisten richt Microsoft een nieuwe divisie op die zich uitsluitend richt op succesvolle enterprise-AI-deployments. Signaal: de markt verschuift van tools verkopen naar implementatiesucces garanderen.
- **Moonshot AI (China) releasing Kimi K3** – Het grootste open-source AI-model tot nu toe (2,8 biljoen parameters) is eind juli vrijgegeven en scoort gelijkwaardig aan GPT-5.6 en Claude op frontier-benchmarks. Open source is geen tweede keus meer.
- **Benelux koploper in Europa** – NL (61%) en BE (62%) lopen voorop in AI-adoptie in Europa, maar 58% van de bedrijven noemt talentschaarste als grootste blokkade voor verdere uitrol.

---

## 🧠 Technologie & Modellen

**GPT-5.6 prijsverlagingen** – OpenAI verlaagde op 30 juli de prijs van GPT-5.6 Luna met 80% en Terra met 20%. De drie-tier strategie (Sol/Terra/Luna) is nu volwassen: Sol voor frontierwerk, Terra als balans, Luna als budgetoptie. Dit drukt de drempel voor enterprise-adoptie op schaal verder naar beneden.
*(Bron: [OpenAI](https://openai.com/index/gpt-5-6/) | [TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/))*

**Claude Sonnet 5** – Anthropic positioneert Sonnet 5 als de goedkopere agent-runner (€2/M input, €10/M output t/m 31 augustus), met verbeteringen op reasoning, tool use en coding ten opzichte van Sonnet 4.6. Na 31 augustus stijgt de prijs naar €3/€15 – een gebruikelijk Anthropic-patroon om early adoption te stimuleren.
*(Bron: [TechCrunch](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/))*

**Kimi K3 (Moonshot AI)** – China's Moonshot AI bracht het grootste open-source model ter wereld uit: 2,8 biljoen parameters, presteert op niveau van de top-US-modellen op frontier-benchmarks. Gecombineerd met de eerdere Kimi K2.6 (~1,1T parameters onder Modified MIT) bevestigt dit dat open-weight modellen in 2026 volwassen zijn voor productie-inzet in coding, agentic workflows en long-context analyse.
*(Bron: [VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems) | [Hugging Face blog](https://huggingface.co/blog/daya-shankar/open-source-llms))*

---

## 🏛️ Governance & Ethiek

**EU AI Act – handhaving per vandaag actief** – Vanaf 2 augustus 2026 zijn de AI Office en nationale autoriteiten bevoegd om de AI Act te handhaven. Concreet vandaag:
- Transparantieregels: AI-systemen moeten kenbaar maken wanneer gebruikers met AI interageren en wanneer content AI-gegenereerd is.
- GPAI-handhaving: de AI Office kan technische documentatie opvragen, modellen evalueren en boetes opleggen aan aanbieders van general-purpose AI-modellen.
- Nationale AI-sandboxes: elke lidstaat moest vandaag minimaal één sandbox operationeel hebben.

Dit is geen formele mijlpaal meer – het is operationele realiteit. Organisaties die nu niet compliant zijn, lopen reëel risico.
*(Bron: [Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/))*

**Nederland blokkerings-bevoegdheid AI-overnames** – De Nederlandse overheid krijgt de bevoegdheid om overnames van Nederlandse AI-bedrijven door bedrijven uit 'niet-bevriende landen' (zoals China) te blokkeren op basis van nationale veiligheid.
*(Bron: [Computable.nl](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/))*

---

## 🔐 Security & Risk

**Prompt injection-aanval op drie major coding agents tegelijk** – Onderzoekers documenteerden een aanval die Claude Code, Gemini CLI en GitHub Copilot gelijktijdig trof via prompt injection. Secrets werden gelekt bij tientallen organisaties. Cruciaal detail: Anthropic's eigen system card vermeldde expliciet dat de GitHub Action "not hardened against prompt injection" is – en toch werd het breed uitgerold.

OWASP bevestigt prompt injection als LLM01 (meest kritische LLM-kwetsbaarheid) voor het tweede jaar op rij. OpenAI erkent dat het probleem waarschijnlijk structureel onoplosbaar is.

**Praktische boodschap voor Ctac**: vraag bij iedere AI-tool in de stack naar de "quantified injection resistance rate" en neem dit op in aanbestedingscriteria.
*(Bron: [VentureBeat Security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers))*

**Cyberaanvallen via AI nemen toe in Benelux** – Nederland registreerde 38% meer cyberaanvallen t.o.v. vorig jaar (circa het dubbele van het wereldwijde gemiddelde); België 14% meer.
*(Bron: [Data News](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/))*

---

## 📈 Markt & Adoptie

**Microsoft Frontier Company** – Microsoft richtte een nieuwe operationele divisie op met $2,5 miljard kapitaal en 6.000 specialisten, uitsluitend gericht op het realiseren van enterprise-AI-deployments. Met 20+ miljoen betaalde M365 Copilot-seats en een AI-omzet van $37 miljard (+123% j-o-j) is dit geen speculatief experiment meer.
*(Bron: [TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) | [CIO Dive](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/))*

**AWS-Google multicloud samenwerking** – AWS en Google Cloud lanceerden een gezamenlijk multicloud-netwerkproduct (preview), met uitbreiding naar Azure gepland in 2026. De hyperscalers, die traditioneel competing waren, bewegen naar interoperabiliteit – waarschijnlijk door enterprise-druk op vendor lock-in.
*(Bron: [CIO Dive](https://www.ciodive.com/news/aws-google-link-cloud-products/806705/))*

**Google Agentic Data Cloud** – Google lanceerde een platform specifiek ontworpen om enterprise AI-agents te ondersteunen, inclusief planning en iteratieve taakuitvoering met minimale menselijke input.
*(Bron: [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))*

**Benelux AI-adoptie koploper Europa** – NL 61%, BE 62% AI-adoptie (vorig jaar resp. 49% en 52%). Positief, maar 58% noemt talent-schaarste als primaire blokkade. Ctac zit in een markt die vraagt – de uitdaging is levercapaciteit, niet vraagcreatie.
*(Bron: [Computable.nl](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/))*

---

## 💡 Ctac-relevantie

**1. EU AI Act compliance wordt hét gesprek van augustus.** Vanaf vandaag is handhaving echt. Ctac-klanten in de publieke sector, zorg en finance zijn kwetsbaar als ze nog geen AI-register hebben of hun AI-systemen niet transparant hebben gelabeld. Dit is een concrete dienst die Ctac nu kan leveren: een compliance-quick-scan met GPAI-transparantie-assessment als instapproduct.

**2. Prompt injection is het nieuwe OWASP Top 10 gesprek.** De gelijktijdige aanval op Claude Code, Gemini CLI en Copilot is een wake-up call voor organisaties die coding agents breed uitrollen. Ctac kan hier positioneren als de partij die "secure AI-deployment" levert – met toetsbare beveiligingseisen in het inkoopproces.

**3. Microsoft Frontier Company verandert het partnership-gesprek.** Microsoft investeert nu actief in deployment-succes, niet alleen tool-verkoop. Voor Ctac als Microsoft-partner betekent dit: de vraag verschuift van "hebben jullie Copilot?" naar "kunnen jullie aantonen dat het werkt?" Zorg dat je een reproduceerbaar deploymentmodel hebt vóór Q4.

**4. Open-source (Kimi K3) maakt het AI-budget-argument zwakker.** Klanten die "te duur" zeggen, kunnen nu verwijzen naar frontier-quality open-weight modellen. Dit vergt een eigen positie van Ctac: niet "welk model", maar "welke architectuur, beveiliging en integratie" – daar zit de waarde.

---

## 📚 Bronnen & verder lezen

- [EU AI Act enforcement start 2 augustus 2026 – Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [GPT-5.6 – OpenAI](https://openai.com/index/gpt-5-6/)
- [Claude Sonnet 5 lancering – TechCrunch](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [Kimi K3: grootste open-source model – VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems)
- [Prompt injection aanval op AI coding agents – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Microsoft Frontier Company – TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [AWS-Google multicloud samenwerking – CIO Dive](https://www.ciodive.com/news/aws-google-link-cloud-products/806705/)
- [Microsoft Copilot groei – CIO Dive](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [Benelux AI-adoptie koploper – Computable.nl](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [Meer cyberaanvallen door AI in Benelux – Data News](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
- [Nederland blokkeert AI-overnames niet-bevriende landen – Computable.nl](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/)
