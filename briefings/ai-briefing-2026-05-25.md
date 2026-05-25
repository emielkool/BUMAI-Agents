---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-25
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 25 mei 2026

## 🔑 Highlights van de dag

- **EU AI Act Omnibus akkoord (7 mei):** Een politiek akkoord over de 'AI omnibus'-amendementen is bereikt; de hoog-risico deadline van 2 augustus 2026 wordt aangepast omdat standaarden nog niet gereed zijn. Dit geeft organisaties meer ruimte, maar ook minder excuus om compliance uit te stellen.
- **Anthropic Mythos Preview – uitsluitend voor kritieke infra:** Anthropic's meest capabele model ooit is slechts beschikbaar voor ~40 gevettede organisaties via Project Glasswing. De cybersecurity-mogelijkheden overstijgen menselijke experts; dit is nadrukkelijk geen consumentenproduct.
- **Microsoft 365 E7 + Agent 365 live (1 mei):** Microsoft bracht zijn Frontier Suite op 1 mei GA. Agent 365 ($15/gebruiker) biedt centrale observatie en governance van AI-agents in de enterprise — een directe propositie voor Ctac-klanten die nu agent-governance nodig hebben.
- **Prompt injection blijft onopgelost structureel risico:** OpenAI erkent dat prompt injection "waarschijnlijk nooit volledig wordt opgelost". CVE-2026-22708 (Cursor IDE) maakt remote code execution via indirecte prompt injection mogelijk. Drie coding agents lekten secrets via één aanval.
- **Google Agentic Data Cloud + Gemini 3.5 Flash GA:** Google positioneert zijn cloudplatform als 'reasoning engine' voor enterprise data. 75% van Google Cloud-klanten gebruikt al AI-producten; Gemini 3.5 Flash is nu algemeen beschikbaar via Google Antigravity en Gemini API.

## 🧠 Technologie & Modellen

**Anthropic Claude Opus 4.7** (GA sinds 16 april) levert aantoonbare vooruitgang op complexe software-engineeringtaken ten opzichte van Opus 4.6. Beschikbaar via Bedrock, Vertex AI en Microsoft Foundry. De werkelijke frontier is echter **Claude Mythos Preview**, dat via [Project Glasswing](https://www.anthropic.com/glasswing) uitsluitend toegankelijk is voor een beperkte groep kritieke-infrastructuurpartners. Anthropic's ARR passeerde $30 miljard (was $9 mrd eind 2025) — de commerciële tractie is onmiskenbaar.

In het **open-source landschap** gelden Kimi K2.6 (~1,1T parameters, Modified MIT), Qwen3 en DeepSeek V4 Pro als de sterkste agentische modellen voor 2026. Voor enterprise-deployments waarbij data de organisatie niet mag verlaten, worden deze modellen steeds realistischer alternatieven.

**PhysicianBench** (arXiv, mei 2026) introduceert een benchmark voor LLM-agents in echte EHR-omgevingen — relevant voor zorgklanten van Ctac.

*Bronnen: [Anthropic Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) · [Project Glasswing](https://www.anthropic.com/glasswing) · [HuggingFace open-source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)*

## 🏛️ Governance & Ethiek

**EU AI Act Omnibus** – Op 7 mei 2026 bereikten het Europees Parlement, de Raad en de Commissie een politiek akkoord over de Digital Simplification Package-amendementen op de AI Act. De kern: de deadline voor hoog-risico verplichtingen (biometrie, kritieke infrastructuur, onderwijs, arbeidsmarkt, migratie) verschuift van 2 augustus 2026 naar 2 december 2027, omdat de benodigde standaarden en competente autoriteiten nog niet operationeel zijn. Tegelijkertijd worden vereenvoudigde regels uitgebreid naar kleine mid-cap bedrijven en krijgt de AI Office meer centraliserende bevoegdheden over GPAI-modellen.

**Praktische implicatie:** Organisaties die compliance uitgesteld hadden, hebben nu meer tijd — maar de richting staat vast. Vroeg beginnen met een AI-register en risicoklassificatie blijft de verstandigste keuze.

*Bronnen: [EU AI Act tracker](https://artificialintelligenceact.eu/) · [EC implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/) · [EC governance](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)*

## 🔐 Security & Risk

Prompt injection staat in 2026 nog steeds op #1 bij OWASP's LLM Top 10, en recente cijfers (meta-analyse van 78 studies) tonen aan dat succespercentages van aanvallen boven de 85% liggen bij adaptieve aanvalsstrategie. OpenAI's eigen erkenning dat dit probleem structureel onoplosbaar is, zou leidend moeten zijn bij het ontwerpen van agentic systemen: **vertrouw nooit blindeling op agent-output die externe data heeft verwerkt**.

**CVE-2026-22708** treft Cursor IDE: remote code execution via indirecte prompt injection in de shell-integratie. Voor developers die coding agents inzetten (ook intern bij Ctac): patchen en agent-sandboxing zijn urgent.

Een VentureBeat-onderzoek documenteert hoe drie commerciële coding agents secrets lekten via één enkele prompt injection — het systeem card van één vendor had het risico zelfs al voorspeld.

*Bronnen: [VentureBeat runtime attacks](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026) · [VentureBeat agent audit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) · [The Hacker News OpenClaw flaws](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html)*

## 📈 Markt & Adoptie

**Microsoft 365 E7 / Frontier Suite** is op 1 mei 2026 algemeen beschikbaar geworden. Het bundle omvat Microsoft 365 E5, Entra Suite, Copilot én het nieuwe **Agent 365** ($15/gebruiker/maand) — een centraal dashboard voor observatie, governance en beveiliging van alle AI-agents binnen een organisatie. Dit maakt governance van agents een standaard enterprise-product in plaats van een maatwerkoplossing.

**Google** presenteerde op Google I/O 2026 **Gemini 3.5 Flash** (GA) en de **Agentic Data Cloud** op Google Cloud Next '26 — een architectuur die legacy enterprise-dataplatforms omzet naar 'reasoning engines'. 75% van Google Cloud-klanten gebruikt reeds AI-producten; het platform verwerkt 16 miljard tokens per minuut via API.

Google investeert tot $40 miljard in Anthropic (cash + compute), wat de reeds hechte samenwerking verder verdiept.

*Bronnen: [Microsoft Frontier Suite](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/) · [Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/) · [Google I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) · [Google investeert in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)*

## 💡 Ctac-relevantie

**Agent governance wordt een product.** Microsoft's Agent 365 en Google's Gemini Enterprise Agent Platform signaleren dat de markt governance van AI-agents als aparte laag erkent en monetiseert. Voor Ctac is dit een directe propositiekans: klanten die beginnen met agent-deployments (Copilot, eigen workflows) hebben begeleiding nodig bij het inrichten van observatie, auditlogs en toestemmingsbeheer. Dit is concreet uitvoerbaar als add-on op bestaande Microsoft 365-trajecten.

**EU AI Act uitstel is geen vrijbrief.** De verschoven deadline (hoog-risico naar december 2027) biedt ruimte, maar Ctac-klanten in de sectoren overheid, zorg en finance blijven in scope. Nu is het juiste moment om AI-registers en risicoklassificaties te starten — zonder de tijdsdruk van een naderende deadline, maar mét de geloofwaardigheid van proactief handelen.

**Prompt injection als klantgesprek.** De erkenning door OpenAI dat dit probleem structureel is, gecombineerd met concrete incidenten (CVE-2026-22708, coded agent leaks), maakt security-by-design bij agentic systemen tot een verkoopbaar argument. Ctac kan hier onderscheidend zijn door dit actief te agenderen in trajecten waarbij agents externe data verwerken.

## 📚 Bronnen & verder lezen

- [Anthropic Claude Opus 4.7 aankondiging](https://www.anthropic.com/news/claude-opus-4-7)
- [Anthropic Project Glasswing](https://www.anthropic.com/glasswing)
- [Anthropic Mythos release roundup – ClaudeAPI.com](https://claudeapi.com/en/blog/news/anthropic-news-roundup-2026-05/)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC: AI Act governance en handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [VentureBeat: 11 runtime attacks in AI](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)
- [VentureBeat: agent secret leak via prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [The Hacker News: OpenClaw AI agent kwetsbaarheden](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html)
- [Microsoft Frontier Suite aankondiging](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Google I/O 2026 aankondigingen](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Google investeert $40B in Anthropic – TechCrunch](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [HuggingFace: beste open-source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [Computable: 6 gevaren van AI voor mens en maatschappij](https://www.computable.nl/2026/05/15/6-gevaren-van-ai-voor-mens-en-maatschappij/)
