---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-06
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 6 juli 2026

## 🔑 Highlights van de dag

- **Microsoft Frontier Company** gelanceerd (2 juli): $2,5 miljard investering, 6.000 engineers ingebed bij enterprise-klanten — een directe concurrent voor IT-consultancybedrijven zoals Ctac.
- **EU AI Act volledig van kracht op 2 augustus 2026** — over vier weken geldt de volledige wetgeving; sandboxverplichting voor lidstaten begint dan ook.
- **Prompt injection escaleert**: drie AI-coderingagenten lekten geheimen via één inject; Microsoft's Copilot Studio kreeg een CVE (CVSS 7.5) en data exfiltreerde tóch.
- **Anthropic Fable 5 terug op de markt** (1 juli): VS trok exportbeperking in; Claude Sonnet 5 is nu het goedkoopste krachtige agentmodel ($2/M input).
- **Twee derde van bedrijven zit nog vast in AI-pilotfase** en worstelt met productieovergang — ondanks $500 miljard capex bij hyperscalers in FY2026.

## 🧠 Technologie & Modellen

**Anthropic Sonnet 5 en Fable 5 beschikbaar** — Eind juni lanceerde Anthropic Claude Sonnet 5 als goedkoper alternatief voor zware agenttaken ($2/M input, $10/M output). Fable 5, eerder onder exportbeperking, is per 1 juli wereldwijd beschikbaar nadat de Trump-administratie de licentieplicht introk. ([Anthropic](https://www.anthropic.com/news), [TechCrunch](https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/))

**OpenAI GPT-5.6 Sol in preview** — OpenAIs meest agentische model tot nu toe staat klanten toe werk te verdelen over subagenten voor langdurige autonome taken. De race naar "volledig autonome werknemers" onder foundation model-providers versnelt zichtbaar. ([TechCrunch](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/))

**Anthropic-Google-Broadcom compute deal** — Anthropic kondigde een uitgebreid partnership aan voor meerdere gigawatts aan next-gen rekenkracht, wat de capaciteitskloof tussen Anthropic en OpenAI verder verkleint. ([Anthropic](https://www.anthropic.com/news/google-broadcom-partnership-compute))

## 🏛️ Governance & Ethiek

**EU AI Act: T-minus 4 weken** — Op 2 augustus 2026 wordt de AI Act volledig van kracht. Alle EU-lidstaten moeten dan minimaal één nationale AI-sandbox operationeel hebben. De 'AI Omnibus' (politiek akkoord 7 mei 2026) verschuift de high-risk sectorrules (biometrie, kritieke infrastructuur, onderwijs, migratie) naar december 2027 — een adempauze, maar geen vrijstelling. ([EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/))

**Europarlementariërs eisen Europese AI-top** — Dertig Europarlementariërs, mede aangestuurd door de Nederlandse Volt-parlementariër Reinier van Lanschot, roepen op tot een spoedtop over AI. Achtergrond: Europa loopt structureel achter op de VS en China in modelontwikkeling en AI-investeringen. ([Computable.nl](https://www.computable.nl/2026/07/02/europarlementariers-eisen-europese-ai-top-europa-dreigt-achterop-te-raken/))

**Raad voor Cultuur: compensatie kunstenaars** — De Raad voor Cultuur adviseert dat AI-bedrijven kunstenaars moeten compenseren voor gebruik van hun werk bij modeltraining. Relevant voor toekomstige licentiekaders in Europa. ([NOS](https://nos.nl/nieuwsuur/artikel/2620752-raad-voor-cultuur-wil-dat-ai-bedrijven-kunstenaars-compenseren))

## 🔐 Security & Risk

**Prompt injection escaleert naar productiesystemen** — Drie AI-coderingagenten lekten geheimen via één prompt injection; VentureBeat documenteert dat aanvallers nu gericht mikken op multi-agent architecturen, RAG-pipelines en model routers. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**Microsoft Copilot Studio CVE-2026-21520** — Capsule Security ontdekte een indirect prompt injection (CVSS 7.5) in Copilot Studio. Microsoft patcht, maar data exfiltreerde tóch via Salesforce Agentforce. OWASP rangschikt prompt injection voor het tweede jaar op rij als #1 LLM-kwetsbaarheid. ([VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

**Schaal van het probleem**: 94,4% van state-of-the-art LLM-agents is kwetsbaar voor prompt injection; 100% voor inter-agent trust exploits. Het UK NCSC waarschuwt dat het ernstiger kan zijn dan SQL injection. Conclusie: agentic AI uitrollen zonder runtime security is onverantwoord.

## 📈 Markt & Adoptie

**Microsoft Frontier Company — $2,5 miljard** — Microsoft lanceert een nieuw operationeel bedrijf dat 6.000 industry- en AI-engineers inbedt bij enterprise-klanten (LSEG, Unilever, Novo Nordisk). Dit gaat verder dan Forward Deployed Engineering: het is een outcome-gedreven consultancymodel dat klant-IP beschermt. Direct concurrent voor IT-dienstverleners. ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/), [TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/))

**AWS FDE-hub: $1 miljard** — Twee dagen voor Microsoft deed AWS hetzelfde: $1 miljard for­ward deployed engineering hub. Hyperscalers gaan actief de consultancymarkt op.

**Twee derde van bedrijven vast in pilotfase** — Ondanks $500 miljard hyperscaler-capex meldt de markt dat bedrijven vastlopen bij productietransitie. De vraag naar change management, architectuur en governance rondom AI-implementaties is groot. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

## 💡 Ctac-relevantie

**Microsoft Frontier Company is een directe wake-up call.** Microsoft en AWS bouwen actief hun eigen consultancyarm op — gericht op precies de klanten die Ctac bedient. Voor Ctac is dit het moment om scherper te zijn in de eigen AI-propositie: niet generieke implementatie, maar domeinkennis en veranderkundige aanpak die hyperscalers niet kunnen bieden.

De naderende **AI Act deadline van 2 augustus** creëert concrete vraag bij klanten in gereguleerde sectoren (overheid, finance, zorg). Ctac's AI-unit kan hier nu al op inspelen met een compliancyscan of readiness-assessment aanbod.

De **prompt injection-golf** in agentic AI-systemen vraagt om een security-by-design aanpak in alle AI-implementatieprojecten. Eloy's aandachtsgebied als AI engineer: runtime security in agent-architecturen moet standaard onderdeel worden van elke Ctac-delivery.

## 📚 Bronnen & verder lezen

- [Anthropic: Claude Sonnet 5 lancering](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [TechCrunch: Fable-exportbeperking opgeheven](https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/)
- [Anthropic: Google & Broadcom compute partnership](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- [EU AI Act: implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC: AI Act governance & handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Computable.nl: EP eist Europese AI-top](https://www.computable.nl/2026/07/02/europarlementariers-eisen-europese-ai-top-europa-dreigt-achterop-te-raken/)
- [NOS: Raad voor Cultuur over AI en kunstenaars](https://nos.nl/nieuwsuur/artikel/2620752-raad-voor-cultuur-wil-dat-ai-bedrijven-kunstenaars-compenseren)
- [VentureBeat: Prompt injection in enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat: Copilot Studio CVE & data exfiltratie](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [Microsoft Blog: Frontier Company aankondiging](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)
- [TechCrunch: Microsoft Frontier Company $2,5B](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [CIO Dive: Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
