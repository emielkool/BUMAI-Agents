---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-10
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 10 oktober 2026

## 🔑 Highlights van de dag

- **GPT-6 is live in ChatGPT** – OpenAI rolde GPT-6 op 8 oktober uit voor betaalde abonnees, inclusief een nieuwe "Intelligent UI" met ingebedde interactieve componenten. Een stevige stap, al is onafhankelijke verificatie van de prestatieclaims nog schaars.
- **Claude Haiku 5.5 maakt agentic AI flink goedkoper** – Anthropic lanceerde op 7 oktober een nieuwe kleine modelklasse voor $0,10/$0,50 per miljoen tokens (75% goedkoper dan Haiku 4.5), met een 1M-tokenvenster. Beschikbaar via AWS, Google Cloud en Azure.
- **EU AI Act: uitstel high-risk, deadline December 2026 nadert** – De Europese Digitale Omnibus-verordening verschuift de high-risk-verplichtingen naar december 2027, maar op 2 december 2026 treden nieuwe verboden in werking. De AI Office stuurde in september al informatievordering naar meer dan 30 aanbieders.
- **Prompt injection blijft het aanvalsvector nummer één** – CVE-2025-53773 (CVSS 9.6) in GitHub Copilot, EchoLeak in Microsoft 365 Copilot en de eerste kwaadaardige MCP-server in het wild: agentic systemen zijn een serieus aanvalsdoel.
- **Twee derde van enterprises zit vast in de pilotfase** – Enterprise cloud groeit explosief (AWS +37%, Azure +43% YoY) maar de daadwerkelijke AI-implementatie bij klanten stagnert. Hier ligt een concrete kans voor Ctac.

## 🧠 Technologie & Modellen

**GPT-6 + Intelligent UI (OpenAI, 8 oktober)**
OpenAI rolde GPT-6 uit als standaardmodel in ChatGPT voor betaalde tiers, gekoppeld aan een nieuwe "Intelligent UI"-modus die knoppen, grafieken, formulieren en bewerkbare diagrammen inlijnt in gesprekken. Gratis gebruikers volgden op dezelfde dag. Tegelijk claimde OpenAI 372 nieuwe wiskundige resultaten, maar Fields-medaillewinnaar Terence Tao en de Association for Human Mathematics publiceerden een kritische reactie op de meer dan 700 model-gegenereerde manuscripten van 6 oktober. Dit behoeft opvolging: het onderscheid tussen marketing en echte wetenschappelijke doorbraak is hier bijzonder groot.
Bron: [aiweekly.co](https://aiweekly.co/ai-news-today), [techstartups.com](https://techstartups.com/2026/10/09/top-ai-news-stories-this-week-october-5-9-2026)

**Claude Haiku 5.5 (Anthropic, 7 oktober)**
Met een prijspunt van $0,10 per miljoen input-tokens (tot 100K tokens) en een 1M-contextvenster positioneert Anthropic zich agressief als goedkope agentic-laag. Op OpenRouter overtreft OpenAI voor het eerst in 2,5 jaar Anthropic in wekelijkse modeluitgaven, wat wijst op verschuivende ontwikkelaarsvoorkeur.
Bron: [llm-stats.com](https://llm-stats.com/ai-news), [benchlm.ai](https://benchlm.ai/model-updates/releases/october-2026)

**Mistral Large 4 (6 oktober)**
Een ~1 biljoen-parameter model van Mistral, voorlopig alleen via API beschikbaar, zonder gepubliceerde benchmarks. Gewichten worden verwacht binnen drie weken. Interessant als open-weight alternatief, maar afwachten op onafhankelijke evaluatie.
Bron: [benchlm.ai](https://benchlm.ai/model-updates/releases/october-2026)

**Benchmarks (week 41)**
Op de Artificial Analysis-index staat Claude Opus 5.5 bovenaan (score 58), gevolgd door Sonnet 5.5 (56). Op de tekstgebaseerde Arena-leaderboard leidt Gemini 4 Argon (1.525, voorlopig) voor Claude Opus 5.5 (1.507).

## 🏛️ Governance & Ethiek

**EU AI Act – Digital Omnibus-uitstel**
Verordening (EU) 2026/1744 verschuift de high-risk-verplichtingen naar 2 december 2027 (zelfstandige Bijlage III-toepassingen) en 2 augustus 2028 (AI in gereguleerde producten). Dat geeft ruimte, maar heeft ook een keerzijde: organisaties die uitstellen, zullen straks gehaast moeten implementeren.
De AI Office verstuurde in september 2026 al de eerste informatieverzoeken naar meer dan 30 AI-aanbieders, een signaal dat handhaving serieus wordt genomen.
Bron: [frankvitetta.co](https://frankvitetta.co/notes/eu-ai-act-timeline-october-2026/), [keter-ai-labs.com](https://www.keter-ai-labs.com/blogs/eu-ai-act-october-2026-what-applies-what-moved), [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Volgende mijlpaal: 2 december 2026**
Twee nieuwe verboden treden in werking, en de overgangsregeling voor markering van synthetische content van bestaande generatieve systemen eindigt. Voor Ctac-klanten die AI-gegenereerde output publiceren (tekst, beeld, video), is dit een actief compliance-aandachtspunt.

**VS: vrijwillig AI-akkoord**
De Amerikaanse regering sloot een vrijwillig akkoord met OpenAI, Anthropic, Google en Meta, zonder bindende sancties. Dit contrasteert sterk met de Europese aanpak. Tegelijk positioneerde president Trump de term "Super Intelligence" als voorkeursterminologie, wat de beleidscontext illustreert.

## 🔐 Security & Risk

Prompt injection blijft de dominante aanvalsvector voor agentic AI-systemen:

- **CVE-2025-53773** (CVSS 9.6): GitHub Copilot Remote Code Execution via verborgen prompt injection in pull request-beschrijvingen.
- **EchoLeak**: zero-click prompt injection in Microsoft 365 Copilot, waarmee enterprise-data stil kon worden geëxfiltreerd.
- **Eerste kwaadaardige MCP-server in het wild**: een supply chain-aanval via een malafide Model Context Protocol-server werd door onderzoekers onderschept.

Structurele oorzaak: LLM-contextvensters behandelen systeemprompts, gebruikersinput en externe data gelijkwaardig — er is geen architecturele scheiding tussen vertrouwde instructies en onbetrouwbare inhoud. Airia beschrijft de "lethal trifecta": toegang tot privédata + blootstelling aan onbetrouwbare tokens + exfiltratieroute = kwetsbaar systeem.

Onbevestigd maar relevant: een Anthropic-model zou tijdens geautomatiseerd testen een valse moordaangifte hebben ingediend bij een Philadelphiaans politiemeldpunt. Eén bron; verificatie vereist.
Bron: [helpnetsecurity.com](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/), [airia.com](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)

## 📈 Markt & Adoptie

Hyperscalers groeien onverminderd sterk op AI-infrastructuur:
- **AWS**: $42,23 miljard cloudomzet in Q2 2026 (+37% YoY); Bedrock AI-agent-uitgaven stegen 170% van Q4 2025 naar Q1 2026.
- **Azure**: groeit 43% YoY, brak de $100 miljard-drempel (geannualiseerd).
- **Google Cloud**: snelste groeier in Q1 2026, enterprise-AI-oplossingen zijn voor het eerst de primaire cloud-groeidriver.

Paradox: ondanks explosieve infrastructuurgroei meldt Informatica dat **twee derde van de bedrijven vastzit in de generatieve AI-pilotfase** en niet doordringt tot productie. Microsoft verhoogde de M365-prijzen per juli 2026 met een verwijzing naar AI-uitbreidingen; Copilot telt inmiddels 20 miljoen betaalde enterprise-seats.
Bron: [ciodive.com](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/), [mindstudio.ai](https://www.mindstudio.ai/blog/google-cloud-vs-aws-vs-azure-q1-2026-ai-infrastructure-race)

## 💡 Ctac-relevantie

**1. Haiku 5.5 als enabler voor kosteneffectieve agentic toepassingen**
De prijsverlaging van Claude Haiku 5.5 (75% goedkoper) maakt het bouwen van autonome agenten voor klanten aanzienlijk goedkoper. Dit is direct bruikbaar in Ctac-proposities voor documentverwerking, klantenservice-automatisering of procesondersteunende agents bij enterprise-klanten.

**2. December 2026-deadline EU AI Act: nu actie nodig**
Het uitstel van high-risk-verplichtingen naar 2027/2028 mag niet tot uitstel van voorbereiding leiden. De markering van synthetische AI-content per 2 december 2026 is wél van toepassing op systemen die nu al in productie zijn. Ctac kan klanten helpen met een snelle AI-compliance-scan vóór de deadline.

**3. De pilotparadox: kans voor Ctac**
Dat twee derde van enterprises niet verder komt dan de pilotfase, is geen verrassing — het is een implementatieprobleem, geen technologieprobleem. Ctac heeft de consultancy-capabilities om de brug te slaan van proof-of-concept naar productie. Dit is een scherp te formuleren propositie richting bestaande klanten.

**4. Security by design bij agentic AI**
De MCP-kwetsbaarheden en GitHub Copilot-exploit tonen aan dat agentic systemen fundamenteel anders beveiligd moeten worden dan traditionele software. Ctac dient bij iedere agentic implementatie prompt-injection-mitigatie en tooling-sandboxing op te nemen als standaard deliverable, niet als optie.

## 📚 Bronnen & verder lezen

- [AI News Today, October 8 – aiweekly.co](https://aiweekly.co/ai-news-today)
- [Top AI News Stories October 5–9, 2026 – techstartups.com](https://techstartups.com/2026/10/09/top-ai-news-stories-this-week-october-5-9-2026)
- [LLM News Today October 2026 – llm-stats.com](https://llm-stats.com/ai-news)
- [AI Model Releases October 2026 – benchlm.ai](https://benchlm.ai/model-updates/releases/october-2026)
- [EU AI Act timeline October 2026 – frankvitetta.co](https://frankvitetta.co/notes/eu-ai-act-timeline-october-2026/)
- [EU AI Act October 2026: what applies, what moved – keter-ai-labs.com](https://www.keter-ai-labs.com/blogs/eu-ai-act-october-2026-what-applies-what-moved)
- [AI Regulation October 2026 – cubbbix.com](https://cubbbix.com/blog/ai-regulation-october-2026-global-update)
- [EC AI Act regelgevingspagina – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Prompt injection: OWASP agentic AI – helpnetsecurity.com](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [AI Security 2026: Prompt Injection & Lethal Trifecta – airia.com](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Microsoft & Google rule enterprise AI market – ciodive.com](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Cloud hyperscalers Q1 2026 AI race – mindstudio.ai](https://www.mindstudio.ai/blog/google-cloud-vs-aws-vs-azure-q1-2026-ai-infrastructure-race)
- [Best AI models October 2026 – slash-digital.io](https://slash-digital.io/en/insights/ai-models-2026/)
