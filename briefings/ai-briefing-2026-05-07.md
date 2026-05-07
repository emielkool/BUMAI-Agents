---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-07
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 7 mei 2026

## 🔑 Highlights van de dag

- **Claude Opus 4.7 is live.** Anthropic lanceerde deze week haar krachtigste model met een sprong van 13% op de moeilijkste coding-taken, verbeterde zelfcorrectie en 3,75 megapixel vision — beschikbaar via AWS Bedrock, Google Vertex AI én Microsoft Foundry.
- **Anthropic én OpenAI starten tegelijkertijd enterprise joint ventures.** Anthropic haalt $1,5 mrd op met Blackstone en Goldman Sachs; OpenAI's 'The Development Company' haalt $4 mrd op bij 19 investeerders — beide modelleren hun aanpak op Palantir's forward-deployed engineers.
- **Microsoft 365 E7 + Agent 365 is op 1 mei GA gegaan.** De nieuwe enterprise suite bundelt productiviteit, identity en AI-agents in één geïntegreerd governance-platform.
- **EU AI Act-aftelling: nog minder dan drie maanden.** Op 2 augustus 2026 worden de regels voor hoog-risico AI-systemen van kracht; lidstaten moeten vóór die datum minimaal één AI-sandbox hebben ingericht.
- **Prompt injection blijft structureel risico.** Drie populaire AI-codeeragenten lekten geheimen via een enkele prompt-injectie; OpenAI erkent openlijk dat dit type aanval waarschijnlijk nooit volledig opgelost zal worden.

---

## 🧠 Technologie & Modellen

**Claude Opus 4.7** is nu algemeen beschikbaar via de Anthropic API en alle grote cloudplatformen (Bedrock, Vertex AI, Microsoft Foundry). Verbeteringen ten opzichte van Opus 4.6: +13% op de 93-taaks coding-benchmark, hogere nauwkeurigheid bij lange agenttaken, verfijnde instructieopvolging en beeldverwerking tot 3,75 megapixel. Prijs blijft gelijk: $5 / $25 per miljoen tokens input/output. Nieuw: een Cyber Verification Program voor legitiem gebruik door security-professionals. Dit is een solide verbetering — geen revolutie, maar wel een duidelijke stap dichter naar onbegeleide taakuitvoering.
([Anthropic](https://www.anthropic.com/news/claude-opus-4-7) | [VentureBeat](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm))

**Microsoft 365 E7 / Agent 365** ging op 1 mei GA. De suite bundelt Microsoft 365 E5, Entra Suite (identity) en Copilot onder één governance-laag, met Agent 365 als control plane voor het beheren en schalen van AI-agents in de enterprise. De beweging maakt duidelijk dat Microsoft agents als infrastructuur-product positioneert, niet als feature.
([Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/28/unlocking-human-ambition-to-drive-business-growth-with-ai/))

**Sierra** haalde $950 mln op (4 mei) om verdere groei te financieren; het bedrijf claimt meer dan 40% van de Fortune 50 als klant en behandelt miljarden agent-interacties. Dit onderstreept dat de markt voor enterprise-agentplatforms snel consolideert.
([TechCrunch](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/))

---

## 🏛️ Governance & Ethiek

**EU AI Act** nadert de volgende kritieke datum: 2 augustus 2026 treden de regels voor hoog-risico AI-systemen in werking, inclusief de handhavingsbevoegdheden van de Europese Commissie voor GPAI-aanbieders. Probleem: CEN/CENELEC hebben de gevraagde standaarden nog niet afgerond, waardoor er onzekerheid bestaat voor organisaties die op die standaarden willen steunen voor compliance-bewijs.

Elke lidstaat — inclusief Nederland en België — moet vóór 2 augustus minimaal één nationale AI-sandbox operationeel hebben. In de nationale implementatieplannen lopen de voortgangen sterk uiteen. Organisaties die hoog-risico AI-systemen ontwikkelen of inzetten, doen er goed aan hun compliance-status te toetsen vóór de zomervakantie.
([artificialintelligenceact.eu](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/) | [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

---

## 🔐 Security & Risk

**AI-coding-agents en prompt injection:** onderzoek toont aan dat drie gangbare AI-codeeragenten geheimen (credentials, tokens) lekten via één gerichte prompt-injectie-aanval. Bijzonder zorgelijk: de system cards van de vendors hadden dit risico al beschreven, maar er waren geen afdoende runtime-controls geïmplementeerd.
([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

OpenAI erkent publiekelijk dat prompt injection — net als social engineering op het web — waarschijnlijk nooit volledig wordt opgelost. De aanbeveling voor enterprise: defence-in-depth (sandboxing, output-validatie, least-privilege tool access) in plaats van vertrouwen op modelweerbaarheid alleen.
([TechCrunch](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/))

Het Pentagon sloot deals met Nvidia, Microsoft en AWS voor AI-inzet op geclassificeerde netwerken (1 mei). Dit signaleert dat soevereine AI-infrastructuur — ook in Europa — een prioriteit wordt die verder gaat dan compliance-argumenten.
([TechCrunch](https://techcrunch.com/2026/05/01/pentagon-inks-deals-with-nvidia-microsoft-and-aws-to-deploy-ai-on-classified-networks/))

---

## 📈 Markt & Adoptie

**Anthropic + OpenAI enterprise joint ventures** (4 mei): beide bedrijven bouwen parallelle commerciële structuren waarin investeerders (PE/VC) preferred sales-toegang krijgen tot hun portfoliobedrijven. Dit is een belangrijke marktverschuiving: Anthropic en OpenAI bewegen van SaaS-model naar consultatief, Palantir-achtig deployment-model met embedded engineers.
([TechCrunch](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/))

**Agentic AI-adoptie loopt achter op ambitie:** 85% van enterprises wil binnen drie jaar 'agentic' zijn, maar 76% erkent dat hun operationele processen daar nu niet voor ingericht zijn. Dit gat tussen intentie en gereedheid is een belangrijk signaal voor partners die enterprise-transformaties begeleiden.
([VentureBeat](https://venturebeat.com/orchestration/enterprise-agentic-ai-requires-a-process-layer-most-companies-havent-built))

**Microsoft en Google** domineren de enterprise AI-markt volgens Gartner: Microsoft via ecosysteem en platformintegratie (Microsoft 365), Google via Agentic Data Cloud en geïntegreerde agenttechstack.
([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

---

## 💡 Ctac-relevantie

**Agent 365 / Microsoft 365 E7** is direct relevant voor Ctac's klantenpraktijk. Nu dit per 1 mei GA is, zullen enterprise-klanten (overheid, finance, industrie) vragen stellen over governance en implementatie van agents in hun Microsoft-omgeving. Ctac kan hier een concrete begeleidingspropositie op bouwen: van agent-strategie tot operationele inrichting van Agent 365.

**De Anthropic/OpenAI enterprise-venturebewegingen** tonen dat de markt consolideert rondom grote, diep geïntegreerde implementatiepartners. Voor Ctac is dit een moment om te bepalen: willen we een erkend implementation partner worden van één of meer van deze platforms? De toegang tot enterprise-deals verschuift richting partijen met een aantoonbaar forward-deployment track record.

**EU AI Act compliance (deadline 2 augustus)** biedt een korte termijn aanleiding voor klantgesprekken: welke AI-systemen vallen onder hoog-risico? Wat is de compliance-status? Ctac kan hier als trusted advisor optreden, met name voor klanten in de publieke sector en financiële dienstverlening.

**Prompt injection als structureel risico** onderstreept de noodzaak van security-by-design in alle agentic projecten die Ctac begeleidt of ontwikkelt. Dit is geen academisch probleem — het raakt direct aan klantdata en aansprakelijkheid.

---

## 📚 Bronnen & verder lezen

- [Anthropic: Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [VentureBeat: Anthropic releases Claude Opus 4.7](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm)
- [TechCrunch: Anthropic and OpenAI enterprise joint ventures](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/)
- [TechCrunch: Sierra raises $950M](https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/)
- [Microsoft Blog: Agent 365 / Microsoft 365 E7](https://blogs.microsoft.com/blog/2026/04/28/unlocking-human-ambition-to-drive-business-growth-with-ai/)
- [CIO Dive: Microsoft, Google rule AI vendor market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [TechCrunch: Pentagon AI deals met Nvidia, Microsoft, AWS](https://techcrunch.com/2026/05/01/pentagon-inks-deals-with-nvidia-microsoft-and-aws-to-deploy-ai-on-classified-networks/)
- [VentureBeat: AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [TechCrunch: Prompt injection in AI browsers](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)
- [VentureBeat: Agentic AI process layer](https://venturebeat.com/orchestration/enterprise-agentic-ai-requires-a-process-layer-most-companies-havent-built)
- [artificialintelligenceact.eu: Implementation next steps](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/)
- [EC Digital Strategy: AI Act governance](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
