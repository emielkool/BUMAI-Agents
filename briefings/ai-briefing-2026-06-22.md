---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-22
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 22 juni 2026

## 🔑 Highlights van de dag

- **Historisch precedent:** De VS heeft een exportcontroledirectief uitgevaardigd dat Anthropic dwong Claude Fable 5 én Mythos 5 wereldwijd te deactiveren voor alle buitenlandse gebruikers — de eerste keer dat de overheid exportregelgeving inzet om een specifiek frontier-model te beperken.
- **Goedkoper frontier-AI drukt markt:** DeepSeek V4 presteert op near-frontier niveau voor 1/6e van de prijs van GPT-5.5 of Opus 4.7; concurrent MiniMax-M3 haalt zelfs betere benchmarks voor 5-10% van de prijs — de token-economie kantelt structureel.
- **EU AI Act: nog 6 weken:** De volledige toepasselijkheid op 2 augustus 2026 nadert, maar de vereiste geharmoniseerde standaarden (CEN/CENELEC) zijn nog niet klaar, wat de naleving door high-risk AI-aanbieders bemoeilijkt.
- **Agentische AI als werknemers:** McKinsey meldt dat 25.000 AI-agents naast haar 60.000 medewerkers werken; Goldman Sachs test Devin als "nieuwe medewerker" — governance en identiteitsbeheer van agents is het nieuwe urgente vraagstuk.
- **Prompt injection stijgt naar boardroomagenda:** Drie AI coding agents lekten geheimen via één prompt injection; OWASP heeft dit tot #1 LLM-risico verklaard, met slagingspercentages tussen 50-80%.

---

## 🧠 Technologie & Modellen

**Claude Fable 5 — gelanceerd, gesuspendeerd, omstreden**
Anthropic lanceerde op 9 juni 2026 Claude Fable 5, de eerste publiek beschikbare versie van zijn Mythos-class model, met uitzonderlijke prestaties op software engineering, wetenschappelijk redeneren en vision. Al op 12 juni volgde een US export control directive: Anthropic moest de toegang voor alle buitenlandse staatsburgers — inclusief eigen medewerkers — direct blokkeren. De overheid stelt dat er een jailbreak is gevonden die de krachtige cybersecurity-capaciteiten van het onderliggende Mythos-model kan ontgrendelen. Anthropic spreekt dit gedeeltelijk tegen en werkt aan herstel. ([anthropic.com](https://www.anthropic.com/news/fable-mythos-access), [fortune.com](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/))

**OpenAI GPT-5.4 en de maandelijkse releasecadans**
OpenAI maakte GPT-5.4 Thinking beschikbaar voor Plus, Team en Pro-gebruikers. Opvallend: GPT-5.4 is het eerste general-purpose model met native computer-use, inclusief 1M-token context. OpenAI handhaaft een cadans van ongeveer maandelijkse major releases; GPT-5.5 verscheen al zes weken na 5.4. ([openai.com](https://openai.com/news/product-releases/))

**Gemini 3.5 Flash en Google I/O-naleveringen**
Google heeft Gemini 3.5 Flash geïntroduceerd als nieuw standaardmodel voor AI Mode in Google Search, wereldwijd voor alle gebruikers. De nadruk ligt op sustained frontier performance voor agentische workflows en coding. ([blog.google](https://blog.google/products-and-platforms/products/search/search-io-2026/))

**Prijsdisruptie: DeepSeek V4 en MiniMax-M3**
DeepSeek V4 Pro kost $1,74 per miljoen input tokens (vs. $5,00 voor GPT-5.5), en presteert op near-frontier niveau. MiniMax-M3 overtreft GPT-5.5 en Gemini 3.1 Pro op meerdere benchmarks voor 5-10% van de kosten. Dit zijn geen marginale besparingen — het is een structurele erosie van de token-marge van de westerse frontier-aanbieders. ([venturebeat.com](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5))

---

## 🏛️ Governance & Ethiek

**EU AI Act: 6 weken tot volledige toepasselijkheid**
Op 2 augustus 2026 wordt de AI Act volledig van toepassing, inclusief de transparantieregels. Echter: CEN en CENELEC hebben de vereiste geharmoniseerde standaarden voor high-risk AI-systemen nog niet gereed. De Europese Commissie overweegt de toepassingsdatum voor high-risk te koppelen aan de beschikbaarheid van die standaarden — wat de handhavingssituatie onzeker maakt. Daarnaast wordt het Code of Practice voor markering van AI-gegenereerde content gefinaliseerd, en moeten lidstaten vóór 2 augustus minstens één AI regulatory sandbox operationeel hebben. ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/), [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-first-draft-code-practice-marking-and-labelling-ai-generated-content))

**US export control als AI-governance-instrument**
De suspensie van Claude Fable 5 is het eerste bekende gebruik van US exportcontrolbevoegdheden om een specifiek frontier AI-model te beperken. Dit opent een nieuw domein van AI-governance dat verder gaat dan de EU AI Act: geopolitieke exportbeheersing als reguleringsarm. Voor Europese enterprise-gebruikers is de vraag nu: wat als een model waarop ik afhankelijk ben morgen offline gaat?

---

## 🔐 Security & Risk

**Prompt injection: van technisch risico naar boardroomprobleem**
VentureBeat rapporteert dat drie populaire AI coding agents geheimen lekten via één enkelvoudige prompt injection, iets wat door de eigen system card van een aanbieder al was voorspeld. OWASP plaatst prompt injection op positie #1 in de Top 10 LLM-risico's, met slagingspercentages van 50-80% in onderzoek. Eerder werden kritieke kwetsbaarheden onthuld in Amazon Q Developer, Google Jules en GitHub Copilot. ([venturebeat.com](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**AI als aanvalsinstrument schaalt mee**
Onderzoek toont dat huidige Claude-modellen nu zelfstandig multi-stage aanvallen kunnen uitvoeren op netwerken met tientallen hosts, gebruikmakend van alleen standaard open-source tools. AI-capability en AI-dreigingsniveau groeien gelijktijdig. ([schneier.com](https://www.schneier.com/blog/archives/2026/01/ais-are-getting-better-at-finding-and-exploiting-security-vulnerabilities.html))

---

## 📈 Markt & Adoptie

**Google Cloud passeert $20 miljard op AI-groei**
Google Cloud behaalde in Q1 2026 voor het eerst meer dan $20 miljard omzet, met 63% groei — AI-producten zijn voor het eerst de primaire groeifactor. Gemini Enterprise groeide 40% kwartaal-op-kwartaal in betaalde gebruikers. Gartner plaatst Google als leider in enterprise agentic AI; Microsoft domineert platformbreed via zijn ecosysteem. ([ciodive.com](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/))

**Twee derde enterprises zit nog in pilotfase**
Ondanks forse investeringen slagen twee derde van de bedrijven er niet in generatieve AI uit de pilotfase te tillen. VC's verwachten dat 2026 het kanteljaar wordt, met hogere budgetten en eerste echte productie-adoptie. Tegelijkertijd stijgt "kosten per token" als primair selectiecriterium sterk — van 25% naar 37% van ondervraagden. ([ciodive.com](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

**AI agents als digitale collega's: governance wordt cruciaal**
McKinsey werkt met 25.000 AI-agents naast 60.000 medewerkers. Goldman Sachs test coding agent Devin als nieuwe medewerker. NewCore haalt $66M op voor identiteits- en lifecycle-beheer van AI-agents. De consensus: agents hebben eigen identiteiten, rechten en revocatiemechanismen nodig. ([techcrunch.com](https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/))

---

## 💡 Ctac-relevantie

**EU AI Act deadline — nu echt urgent voor klanten**
Met 6 weken tot de volledige toepasselijkheid is dit het moment om gesprekken te openen met klanten over hun AI Act-readiness. De standaarden zijn nog niet af, maar de verplichting geldt wel. Ctac kan zich positioneren als implementatiepartner voor AI governance, risicoclassificatie en transparantieregistratie — concreet en direct toepasbaar.

**De Fable 5-suspensie als verkoopargument voor governance-diensten**
Het abrupte wereldwijde deactiveren van een frontier-model op overheidsbevel is precies het scenario dat klanten wakker houdt. Ctac kan dit gebruiken om een vendor-agnostische, multi-model architectuurstrategie te bepleiten: zorg dat kritieke processen niet afhankelijk zijn van één enkel model. Dat is een concrete propositie voor enterprise-klanten.

**Prijsdaling maakt AI toegankelijker voor MKB-klanten**
DeepSeek V4 voor 1/6e van de prijs van frontier-modellen maakt serieuze AI-adoptie ook voor kleinere Ctac-klanten financieel haalbaar. Geen excuus meer dat AI "te duur" is voor productie-inzet. Aandachtspunt: deze modellen vallen buiten EU-jurisdictie en roepen dataprivacyvragen op die begeleid moeten worden.

**Agent governance als nieuwe dienst**
De groei van AI agents als digitale werknemers brengt nieuwe vragen: wie beheert de toegangsrechten? Wie is aansprakelijk? Ctac kan hier een aanbod ontwikkelen rondom agent governance frameworks — in lijn met wat NewCore bouwt, maar dan als implementatiedienst voor bestaande klanten.

---

## 📚 Bronnen & verder lezen

- [Anthropic – Statement on Fable 5 & Mythos 5 suspension](https://www.anthropic.com/news/fable-mythos-access)
- [Fortune – Anthropic disables Fable and Mythos following US export ban](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/)
- [TechCrunch – Anthropic releases Claude Fable 5](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)
- [OpenAI – Product releases newsroom](https://openai.com/news/product-releases/)
- [Google – Google I/O 2026 announcements](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Microsoft – Build 2026: Be yourself at work](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [VentureBeat – DeepSeek V4 at 1/6th the cost](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- [VentureBeat – AI agent runtime security & prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [EU AI Act – Implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Code of Practice AI-gegenereerde content](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-first-draft-code-practice-marking-and-labelling-ai-generated-content)
- [CIO Dive – Google Cloud tops $20B on AI boom](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [CIO Dive – Microsoft & Google rule enterprise AI market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [TechCrunch – NewCore $66M for AI agent identities](https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/)
- [Schneier on Security – AIs getting better at exploiting vulnerabilities](https://www.schneier.com/blog/archives/2026/01/ais-are-getting-better-at-finding-and-exploiting-security-vulnerabilities.html)
