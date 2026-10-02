---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-16
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 16 juli 2026

## 🔑 Highlights van de dag

- **OpenAI GPT-5.6 familie gelanceerd:** drie varianten (Sol, Terra, Luna) gericht op zakelijk gebruik, codering en wetenschappelijk onderzoek — een directe aanval op het hoge segment van de markt. ([TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/))
- **EU AI Act-deadline nadert kritisch:** per 2 augustus 2026 gelden volledige nalevingsverplichtingen voor hoog-risico AI-systemen — organisaties die dit nog niet hebben geregeld, lopen risico op handhaving. ([AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/))
- **Microsoft lanceert Frontier Company:** een nieuwe $2,5 miljard-investeringsvehikel met 6.000 experts om enterprise AI-implementaties te ondersteunen — een directe concurrent voor IT-consultants. ([TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/))
- **Prompt injection bedreigt agentic AI:** een Microsoft Copilot Studio-kwetsbaarheid (CVE-2026-21520, CVSS 7.5) toont aan dat agentic systemen actief worden aangevallen. ([VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))
- **Anthropic haalt OpenAI in bij enterprise adoptie:** Claude heeft voor het eerst meer enterprise-gebruikers dan OpenAI, maar drie strategische bedreigingen kunnen dit voordeel snel tenietdoen. ([VentureBeat](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead))

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6** is beschikbaar in drie varianten: Sol (werkpaard voor dagelijks gebruik), Terra (middenklasse) en Luna (budgetoptie). Tegelijk lanceerde OpenAI ook **GPT-Live-1** en **GPT-Live-1 mini** — spraakmodellen voor meer natuurlijke live-gesprekken. ([OpenAI](https://openai.com/index/gpt-5-6/))

**SpaceXAI Grok 4.5** werd op 8 juli uitgebracht, omschreven als een "Opus-class model" geschikt voor codering, administratief werk en kenniswerk. De release volgt snel op de beursgang van SpaceXAI. ([TechCrunch](https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/))

**Anthropic Claude Opus 4.7** is nu beschikbaar via alle Claude-producten, de API, Amazon Bedrock, Google Vertex AI en Microsoft Foundry. Verbeteringen zitten in geavanceerde software-engineering, hogere visuele resolutie en een nieuw cybersecurity-verificatieprogramma voor legitiem gebruik. Prijs ongewijzigd: $5/1M input, $25/1M output tokens. ([Anthropic](https://www.anthropic.com/news/claude-opus-4-7))

Kritische noot: de modelrace versnelt maar de kwaliteitsverschillen in de top worden kleiner. Voor enterprise-inzet wordt keuze steeds vaker bepaald door integraties, prijs en compliance — niet puur door benchmark-scores.

---

## 🏛️ Governance & Ethiek

**2 augustus 2026 is de cruciale deadline** voor volledige naleving van de EU AI Act voor hoog-risico systemen (Annex III). Verplicht zijn: conformiteitsbeoordeling, CE-markering, registratie in de EU-database en doorlopend risicomanagement. Organisaties die dit traject niet tijdig hebben gestart, lopen achterstand op. ([Frankwatching](https://www.frankwatching.com/archive/2026/05/04/eu-ai-act-regelen-voor-2-augustus/))

De **AI Omnibus** (vereenvoudigingswijziging) heeft politiek akkoord bereikt op 7 mei 2026 en verlicht de last voor kleinere midcap-bedrijven, centraliseert toezicht op GPAI-modellen bij het AI Office, en verduidelijkt de relatie met EU-productveiligheidsregels. ([EC digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement))

---

## 🔐 Security & Risk

Prompt injection blijft het toprisico voor enterprise AI (OWASP LLM01). In 2026 concentreert het gevaar zich op **agentic systemen**: RAG-pipelines, model routers en geautomatiseerde workflows worden actief aangevallen. Microsoft moest een patch uitbrengen voor CVE-2026-21520 in Copilot Studio (CVSS 7.5 indirect prompt injection), waarbij de data alsnog kon worden geëxfiltreerd ondanks de patch. ([VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers))

Aandachtspunt: naarmate organisaties AI-agents meer autonomie en tool-toegang geven, neemt het aanvalsoppervlak proportioneel toe. Dit vraagt om security-by-design in de architectuurfase, niet als latere toevoeging.

---

## 📈 Markt & Adoptie

**Microsoft** domineert de enterprise AI-markt met >20 miljoen Copilot-betaalstoelen, een AI-omzet van $37 miljard (run rate, +123% YoY) en de nieuwe Frontier Company als implementatiearm. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

**Google Cloud** passeerde de $20 miljard-grens mede dankzij AI-diensten; Gemini Enterprise groeide 40% QoQ in betaalde maandelijkse actieve gebruikers. ([CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/))

De bredere markt voor enterprise AI wordt in 2026 op meer dan **$2 biljoen** geschat. ROI-verwachtingen zijn hoog (171% gemiddeld), maar 95% van de enterprise AI-pilots levert nog steeds geen meetbare ROI op. Het probleem zit niet in het platform maar in de implementatie: organisaties missen een proceslaag. ([VentureBeat](https://venturebeat.com/orchestration/enterprise-agentic-ai-requires-a-process-layer-most-companies-havent-built))

---

## 💡 Ctac-relevantie

Twee strategische signalen voor Ctac deze week:

**1. Microsoft Frontier Company is directe concurrentie én kans.** Microsoft investeert $2,5 miljard in enterprise AI-implementatie met 6.000 eigen experts. Dit competeert direct met de klassieke IT-consultancy propositie — maar ook: Microsoft zoekt implementatiepartners, en Ctac kan zich positioneren als de lokale (NL/BE) specialist die de klantkennis heeft die een globale speler mist. De vraag is of Ctac deze positie actief claimt vóór anderen dat doen.

**2. AI Act-deadline van 2 augustus is een onmiddellijke klantkans.** Veel middelgrote organisaties in de doelgroep van Ctac (overheid, zorg, finance) hebben hun AI-systemen nog niet geclassificeerd of getoetst. Een korte AI Act compliance-scan als instapproduct kan nieuwe klantrelaties openen én Ctac positioneren als betrouwbare AI-partner. Dit is een tijdgevoelige kans: de deadline is over 17 dagen.

---

## 📚 Bronnen & verder lezen

- [GPT-5.6 aankondiging – OpenAI](https://openai.com/index/gpt-5-6/)
- [GPT-5.6 release – TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [Grok 4.5 release – TechCrunch](https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/)
- [Claude Opus 4.7 – Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
- [Claude Opus 4.7 – VentureBeat](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [AI Act augustus 2026 deadline – Frankwatching](https://www.frankwatching.com/archive/2026/05/04/eu-ai-act-regelen-voor-2-augustus/)
- [EU AI Act governance – EC](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Prompt injection enterprise AI – VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [Microsoft Frontier Company – TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [Microsoft vs Google enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Anthropic vs OpenAI enterprise adoptie – VentureBeat](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)
- [Agentic AI proceslaag ontbreekt – VentureBeat](https://venturebeat.com/orchestration/enterprise-agentic-ai-requires-a-process-layer-most-companies-havent-built)
- [Google Cloud $20B – CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
