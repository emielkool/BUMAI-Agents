---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-30
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 30 juni 2026

## 🔑 Highlights van de dag

- **OpenAI limiteert GPT-5.6** op aandringen van het Witte Huis – het eerste concrete geval van directe overheidsbemoeienis met modelreleases in de VS; een precedent voor de rest van de industrie.
- **EU AI Act-deadline nadert**: transparantieverplichtingen (Artikel 50) treden 2 augustus in werking; de Code of Practice voor AI-gegenereerde content is afgelopen week gepubliceerd.
- **Microsoft lanceert MAI-Thinking-1** – een eigen 35B reasoning model, volledig in-house getraind, plus Work IQ en Web IQ APIs nu algemeen beschikbaar.
- **Prompt injection is actief misbruikt**: CVE-2026-5027 staat op de exploited-vulnerabilities lijst; drie AI coding agents lekten data via één enkele aanval.
- **Agent governance wordt volwassen**: Microsoft's open ACS-standaard en NewCore ($66M) richten zich op authenticatie en controle van autonome agents in enterprise-omgevingen.

## 🧠 Technologie & Modellen

**OpenAI – GPT-5.6 beperkt uitgerold**
OpenAI rolt GPT-5.6 (modellen Sol, Terra en Luna) slechts uit naar "een kleine groep vertrouwde partners" na druk van de Trump-administratie, die AI-bedrijven vraagt nieuwe modellen eerst voor overheidsevaluatie in te dienen. Sol overtreft Anthropic's Mythos 5 licht op coding benchmarks, bij een derde van de outputtokens. OpenAI accepteert de beperking maar noemt het "geen norm." ([TechCrunch](https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/))

**Microsoft – eigen AI-stack versterkt**
Microsoft lanceerde op Build 2026 zeven eigen modellen, met MAI-Thinking-1 als vlaggenschip: 35B parameters, 256K contextvenster, commercieel gelicenseerde trainingsdata. Work IQ APIs en Web IQ (MCP-native zoekstack) zijn nu GA. Dit is een directe aanval op OpenAI's positie in Microsoft's eigen ecosysteem. ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/))

**Ecosysteem bredder dan ooit**
Alibaba's Qwen-AgentWorld (24 juni) simuleert agent-omgevingen voor zeven domeinen en verbetert benchmarks zonder expliciete agent-training. TechCrunch stelt vast: de strijd is niet meer "Anthropic vs. OpenAI", maar een breed ecosysteem van Microsoft, Alibaba, open source en gespecialiseerde startups. ([TechCrunch](https://techcrunch.com/2026/06/26/its-not-about-anthropic-vs-openai-anymore/))

## 🏛️ Governance & Ethiek

**EU AI Act – minder dan 40 dagen**
Per 2 augustus 2026 treden de transparantieverplichtingen van Artikel 50 in werking. De Code of Practice on Transparency of AI-generated content is in juni gepubliceerd. Organisaties die generatieve AI in productie hebben, moeten voor 2 december 2026 machine-leesbare markering (watermarking) geïmplementeerd hebben. Elk EU-lidstaat moet ook een nationale AI-sandbox gereed hebben. ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/))

**VS – overheidsbemoeienis neemt toe**
De Trump-administratie heeft een executive order getekend die AI-bedrijven verzoekt nieuwe modellen vrijwillig voor overheidstests in te dienen. Dit is een significante verschuiving: overheidstoezicht vóór publieke release kan de productontwikkelingscyclus structureel vertragen. ([TechCrunch](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/))

**Nederland**
Het kabinet werkt aan de uitvoeringswet AI-verordening voor nationaal toezicht. Tegelijk waarschuwt de NVM dat Nederland door gebrek aan datacenterruimte dreigt de AI-race te missen – een structureel knelpunt voor de nationale AI-positie.

## 🔐 Security & Risk

**Prompt injection – actieve exploits in productie**
CVE-2026-5027 staat per 8 juni op VulnCheck's exploited-vulnerabilities lijst na in-the-wild aanvallen op AI agent frameworks. Drie populaire AI coding agents (niet nader genaamd) lieten gevoelige data lekken via één enkele prompt injection. Microsoft patchte een Copilot Studio-kwetsbaarheid, maar data werd desondanks geëxfiltreerd. VentureBeat beschrijft hoe aanvallers nu systematisch agents, RAG-pipelines en model routers targeten. ([VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)) ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

Prompt injection is geen theoretisch risico meer: het is een bewezen aanvalsvector in productie-enterprise-omgevingen.

## 📈 Markt & Adoptie

**Funding golf voor agent-infrastructuur**
Patronus AI ($50M) bouwt "digital world models" om agents pre-productie te stress-testen. NewCore ($66M) levert identiteits- en governance-lagen voor AI agents als "enterprise-medewerkers." Coralogix ($200M) bouwt observability voor agent-omgevingen. Dit zijn no-hype investeringen in operationele volwassenheid, niet in modelinnovatie.

**Kostenbeheer – urgent signaal**
Bedrijven zitten al in april 3x over hun volledige 2026 tokenbudget. De conversatie is verschoven van "snel bouwen" naar "hoe beheersen we dit?" – een sign dat agent-adoptie snel volwassen wordt. ([TechCrunch](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/))

## 💡 Ctac-relevantie

**EU AI Act compliance = nu actiewerk.** Klanten met generatieve AI in productie moeten voor augustus 2026 hun transparantieverplichtingen ingeregeld hebben. Ctac kan concreet helpen: inventariseren welke systemen onder Artikel 50 vallen, disclosure-beleid inrichten, watermarking-roadmap begeleiden naar december 2026.

**Prompt injection = actuele dreiging bij klanten.** Met actieve CVEs in agent frameworks is dit geen toekomstige zorg. Een AI-security assessment voor bestaande Copilot Studio-, RAG- en coding agent-deployments is een directe propositionele kans.

**AI FinOps als nieuwe dienst.** Klanten die agents in productie hebben, worden verrast door tokenkosten. Ctac kan kostenoptimalisatie en governance-methodieken aanbieden – aansluitend op bestaande cloud FinOps-expertise.

**Microsoft's MAI-Thinking-1 en Work IQ APIs** zijn direct relevant voor klanten op Microsoft 365/Azure. Het alternatief voor OpenAI-modellen in Microsoft Foundry verdient aandacht in klantadvies over AI-stack keuzes.

## 📚 Bronnen & verder lezen

- [TechCrunch: It's not about Anthropic vs. OpenAI anymore (26 juni)](https://techcrunch.com/2026/06/26/its-not-about-anthropic-vs-openai-anymore/)
- [TechCrunch: OpenAI limits GPT-5.6 rollout after government request (26 juni)](https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/)
- [TechCrunch: White House asks OpenAI to slow roll model release (25 juni)](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/)
- [EU AI Act: Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC: Code of Practice on transparency AI-generated content](https://digital-strategy.ec.europa.eu/en/faqs/signing-code-practice-transparency-ai-generated-content)
- [Microsoft Build 2026 Blog (2 juni)](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [CIO Dive: Microsoft, Google domineren enterprise AI-markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [VentureBeat: Prompt injection targets agents, RAG and model routers](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat: Three AI coding agents leaked secrets via prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [TechCrunch: Patronus AI lands $50M (25 juni)](https://techcrunch.com/2026/06/25/patronus-ai-lands-50m-to-build-digital-worlds-that-stress-test-ai-agents/)
- [TechCrunch: NewCore $66M voor AI agent identities (15 juni)](https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/)
- [TechCrunch: The token bill comes due (5 juni)](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/)
- [NVM: Nederland dreigt AI-race te missen](https://www.nvm.nl/nieuws/2026/nederland-dreigt-ai-race-te-missen-door-ruimtegebrek-voor-datacenters/)
