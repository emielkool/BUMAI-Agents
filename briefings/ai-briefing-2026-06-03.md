---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-03
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 3 juni 2026

## 🔑 Highlights van de dag

- **Anthropic breidt Project Glasswing uit naar 150+ organisaties** – waaronder NATO en ENISA: Claude Mythos, te gevaarlijk voor publieke release, wordt ingezet bij kritische infrastructuur in 15+ landen. Dit herdefiniëert de rol van AI in cybersecurity.
- **EU AI Act D-dag: 2 augustus 2026** – over exact 60 dagen heeft de Europese Commissie volledige handhavingsbevoegdheid over GPAI-aanbieders. Organisaties die nog niet compliant zijn, lopen nu concreet risico op boetes.
- **Anthropic dient vertrouwelijk S-1 in bij de SEC** voor een beursgang; bij een waardering van ~$965 miljard en een recente $65 miljard-ronde is dit de grootste AI-IPO ooit in aantocht.
- **Enterprise AI zit structureel vast in pilots**: tweederde van bedrijven rolt AI niet succesvol uit in productie. Het probleem is niet het model, maar de runtime-architectuur – orkestratie, audit trails en datagrounding.
- **OpenAI als Gartner-leider** in Enterprise AI Coding Agents 2026; Codex groeit 5x jaar-over-jaar en wordt gebruikt door 4 miljoen mensen per week.

## 🧠 Technologie & Modellen

**Anthropic Opus 4.8** werd op 28 mei gelanceerd – slechts 41 dagen na Opus 4.7. De versnelde releasecyclus signaleert Anthropic's sprint richting IPO-moment. De nieuwe 'dynamic workflow'-tool maakt Opus 4.8 beter geschikt voor agentische taken. ([TechCrunch](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/))

**OpenAI GPT-5.5-Cyber** rolt in een beperkt partnernetwerk uit: een cybersecurity-gespecialiseerd model als directe tegenhanger van Mythos. De race naar AI-gedreven offensieve én defensieve security-capaciteiten is in volle gang.

**Nvidia Agent Toolkit** (GTC 2026) bundelt Nemotron-modellen, AI-Q (enterprise knowledge blueprint), OpenShell (policy-based security runtime) en cuOpt in één platform. Adobe, Salesforce en SAP zijn vroege adopters. Een serieuze zet om de agentic AI-stack te standaardiseren vóór de rest. ([VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among))

**Context architecture vervangt RAG** als dominante keuze voor enterprise AI-agents; de RAG-limieten worden te knellend bij multi-stap agentische flows. ([VentureBeat](https://venturebeat.com/data/context-architecture-is-replacing-rag-as-agentic-ai-pushes-enterprise-retrieval-to-its-limits))

## 🏛️ Governance & Ethiek

**EU AI Act – T-60**: Per 2 augustus 2026 heeft de Europese Commissie volledige handhavingsbevoegdheid over GPAI-aanbieders, inclusief de bevoegdheid tot boetes. De recent operationeel gestelde Wetenschappelijke Raad (60 onafhankelijke experts) en het Adviesforum ondersteunen de AI Office en nationale toezichthouders. ([EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support))

**Kritisch**: De handhavingskloof is nog groot. Veel bedrijven in NL/BE missen de conformiteitsdocumentatie voor high-risk AI-toepassingen. Nationale implementatieplannen van lidstaten lopen achter op het Brusselse schema.

## 🔐 Security & Risk

**Project Glasswing scaling** is de belangrijkste AI-security-beweging van de week. Claude Mythos – dat zelfstandig zero-day kwetsbaarheden in open-source codebases kan vinden én exploiteren – staat nu beschikbaar voor Okta, Samsung, SK Hynix, NATO en ENISA in 15+ landen. Anthropic noemt het zelf te gevaarlijk voor brede publieke release, maar geeft het aan geselecteerde partijen. ([TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/))

**Prompt injection blijft stelselmatig risico**: Drie AI-coding-agents lekten secrets via één prompt injection-aanval. NIST kwalificeert prompt injection als "de grootste security-fout van generatieve AI"; runtime-beveiligingsmaatregelen zijn nog geen standaard in enterprise deployments. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

## 📈 Markt & Adoptie

**Anthropic richting beurs**: Bij ~$965 miljard waardering en een vertrouwelijke S-1-indiening is een IPO in 2026 realistisch. Google investeerde al $40 miljard in Anthropic; de commercialisering versnelt. ([TechCrunch](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/))

**Google Cloud: $20+ miljard** in Q1 2026 (+63% j/j); enterprise generatieve AI-producten groeien +800% j/j. Gemini Enterprise: +40% kwartaal-over-kwartaal in betaalde gebruikers. ([CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/))

**AWS Kiro case**: Een engineering-team herontwierp een 18-maanden project (30 developers) met 6 mensen in 76 dagen via spec-driven agentic development. Dit daagt directe aannames over IT-projectplanning uit.

## 💡 Ctac-relevantie

**Drie concrete actiepunten:**

1. **EU AI Act compliance = nu verkoopbaar**: Met 2 augustus als deadline heeft Ctac 60 dagen om klanten in high-risk sectoren (overheid, zorg, finance) te helpen met gap-analyses en conformiteitsdocumentatie. Dit is een propositie die nu urgent is – niet over drie maanden.

2. **Agentic runtime is het nieuwe differentiatiegebied**: De markt verschuift van "welk model?" naar "hoe implementeer je agents veilig op schaal?" Orkestratie, audit trails en datasecurity zijn de echte bottlenecks. Ctac's AI-unit kan hier een architectuurpropositie op bouwen – niet modelgericht, maar implementatiegerecht.

3. **Anthropic via AWS Bedrock**: Zodra Anthropic naar de beurs gaat, versnelt enterprise-commercialisering van Claude-modellen. Ctac's AWS-partnerschap biedt nu al toegang via Bedrock. De vraag is of dit actief in klantproposities zit – zo niet, is dat een directe kans.

## 📚 Bronnen & verder lezen

- [Anthropic scales Claude Mythos to 15+ countries – TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)
- [Anthropic files to go public – TechCrunch](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/)
- [Anthropic raises $65B, nears $1T valuation – TechCrunch](https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/)
- [Anthropic releases Opus 4.8 – TechCrunch](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/)
- [Project Glasswing – Anthropic](https://www.anthropic.com/glasswing)
- [AI Act enforcement gets expert support – EC](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support)
- [AI Act governance & enforcement – EC](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Google Cloud tops $20B – CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [The Agentic Reckoning – VentureBeat](https://venturebeat.com/resources/the-agentic-reckoning-enterprise-ai-organizations-have-a-runtime-problem-not-a-model-problem)
- [AI agent runtime security – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [OpenAI Gartner 2026 Enterprise AI Coding Leader](https://openai.com/index/gartner-2026-agentic-coding-leader/)
- [Nvidia enterprise AI agent platform – VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Agentic coding: spec-driven development – VentureBeat](https://venturebeat.com/orchestration/agentic-coding-at-enterprise-scale-demands-spec-driven-development)
- [Context architecture replacing RAG – VentureBeat](https://venturebeat.com/data/context-architecture-is-replacing-rag-as-agentic-ai-pushes-enterprise-retrieval-to-its-limits)
