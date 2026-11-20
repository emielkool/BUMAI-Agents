---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-18
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 18 november 2026

## 🔑 Highlights van de dag

- **Anthropic IPO morgen live op Nasdaq.** Pricing vanavond (18 nov), handelstart 19 nov onder ticker ANT. Verwachte beurswaarde $1,3–1,4 biljoen bij $70–78 per aandeel. Totale opbrengst kan oplopen tot ~$90 miljard – historisch groot voor een AI-bedrijf.
- **Google Gemini 4 Carbon is de nieuwe benchmarkkoning.** Sinds 10 november GA, positioneert Google dit als zijn sterkste model ooit. Gemini 4 Hydrogen (12 nov) volgt specifiek voor multi-stap agentische workflows.
- **CVE-record 2026 gebroken door AI-gestuurde security research.** Op 13 november passeerde het aantal CVE-meldingen de 100.000 voor dit jaar – gedreven door AI-tools in security-analyse. Tegelijk zijn AI-systemen zelf steeds vaker het doelwit.
- **SAP onthult 1.000 AI-agents bij TechEd 2026.** Finance, supply chain, HR en CX – gebouwd in samenwerking met Microsoft, Google Cloud en AWS. Direct relevant voor SAP-klanten in het Ctac-portfolio.
- **JPMorgan test AI-agents voor FX-transacties zonder menselijke tussenkomst.** Proof-of-concept met Hyundai Card uitgevoerd; governance en transactielimieten, niet technologie, zijn het eigenlijke obstakel.

---

## 🧠 Technologie & Modellen

**Anthropic** bracht op 9 november **Claude Fable 5.2** uit – 30% sneller dan versie 5.1, prijsstelling $8/$40 per miljoen tokens (input/output). Tegelijk is **Claude Mythos 5.2** gelanceerd, met beperkte toegang voor geverifieerde organisaties; details over de capabilities zijn nog niet openbaar.

**Google** bevestigde GA van **Gemini 4 Carbon** (10 nov) als meest capabele model in de Gemini-familie, gevolgd door **Gemini 4 Hydrogen** (12 nov), gericht op complexe, meerdere stappen omvattende agentic taken. Een introductieprijsperiode voor de API loopt tot 30 november.

**OpenAI** lanceerde **GPT-6 Cyber** (5 nov), exclusief voor goedgekeurde securityteams. Rapporten van llm-stats suggereren dat GPT-6.2 Astra en Sol op 17 november zijn uitgebracht ($8/$40 en $2/$10 per M tokens), maar dit kon niet bevestigd worden via officiële kanalen – behandel als onbevestigd.

**DeepSeek** bracht naar verluidt begin november een autonome coding "Super-Agent" uit. **Databricks** lanceerde Genie, een autonome AI-coworker voor langlopende taken binnen zakelijke context.

Bronnen: [LLM Release Tracker](https://nhimg.org/llm-release-tracker) · [BeevR AI Model Releases](https://beevr.ai/blog/ai-model-releases-november-2026) · [AI News Roundup November 2026](https://joineta.org/blog/ai-news-roundup-november-2026)

---

## 🏛️ Governance & Ethiek

De **EU AI Act** is nu volledig operationeel voor handhaving op GPAI-modellen en voor **Article 50 transparantieplichten** (beide sinds augustus 2026). De **Omnibus-wijzigingen** (Verordening 2026/1744, ingegaan 27 juli) stroomlijnen de samenhang met de Product Liability Directive.

Cruciale deadline nadert: legacy generatieve systemen moeten vóór **2 december 2026** aan labelling-eisen voldoen. Hoog-risico AI (Annex III standalone) heeft uitstel tot december 2027; product-ingebedde systemen (Annex I) tot augustus 2028.

De Singapore Consensus (arxiv, aug 2026) constateerde dat governance-mechanismen voor agentische AI-systemen "net beginnen te ontstaan" – terwijl de systemen zelf al in productie draaien bij AT&T (500+ workflows, >1M transacties/maand).

Bronnen: [EC AI Act pagina](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [EU AI Act Timeline](https://shattered.io/eu-ai-act-world-first-ai-law-five-dates-to-2028-2026/) · [Singapore Consensus](https://arxiv.org/pdf/2608.14611)

---

## 🔐 Security & Risk

November was een zware maand voor AI-infrastructure security:

- **SGLang RCE (NEAR AI):** Aanvaller gebruikte een remote code execution-lek in de SGLang inference engine om op een productieserver te komen; in-flight requests waren zichtbaar, inclusief vertrouwelijke queries.
- **Cloudflare Workers AI cross-tenant lek:** Een grote request aan GLM-5.3 retourneerde data uit een andere inference-sessie – bug gevonden en gefixt in upstream SGLang.
- **Unsloth CVE-2026-93348 (CVSS 8.6):** Een aanvaller-gecontroleerde `model_type` in een modelconfig werd via `exec()` uitgevoerd bij laden. Update naar `unsloth_zoo ≥ 2026.8.14`.
- **GitHub Copilot CLI:** Decrypteerde een aanvallers ciphertext in eigen shell en stuurde lokale bestanden naar het aanvallerseindpunt.
- **Claude Code child session:** Startup hook in een kwaadaardig repository werd uitgevoerd zonder de bevestigingsstap die de ouder-sessie normaal vereist.
- **Amazon Bedrock AgentCore:** Credential exposure mogelijk voor agents in dezelfde AWS-regio en -account.
- **Breder beeld:** Campagnes die AI of LLMs refereren zijn verdubbeld van 5,3% naar 10,4% (Trellix Threat Report november 2026).

Bronnen: [Adversa AI Coding Agents](https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/) · [GenAI Security November 2026](https://adversa.ai/blog/top-genai-security-resources-november-2026/) · [Trellix Threat Report](https://www.trellix.com/advanced-research-center/threat-reports/november-2026/)

---

## 📈 Markt & Adoptie

**Anthropic IPO** is het marktnieuws van de week. Met een verwachte beurswaarde van $1,3–1,4 biljoen (fully diluted) en een private placement van $26 miljard naast de beursintroductie kan de totale opbrengst ~$90 miljard bedragen. Dat zou de grootste tech-IPO aller tijden zijn. Retail-investeerders mogen naar verwachting ~20% ontvangen. Ticker: **ANT**, Nasdaq, handelstart 19 november.

**SAP TechEd 2026** heeft 1.000 AI-agents gepresenteerd over finance, supply chain, HR en CX – gebouwd in samenwerking met Microsoft, Google Cloud en AWS. SAP Joule ligt op 26% adoptie binnen SAP-organisaties; Microsoft Copilot leidt met 60% (ASUG/Precisely survey). Enterprise AI levert vooralsnog meer *inzichten* dan kostenbesparingen (Economist Enterprise/SAP, 2.015 ondervraagde executives).

**JPMorgan × Hyundai Card** (CNBC, 18 nov): succesvolle PoC voor AI-agent FX-transacties zonder menselijke betrokkenheid. Governance en transactielimieten worden als voornaamste blokkade gezien, niet technologie.

Bronnen: [Anthropic IPO Bloomberg](https://www.bloomberg.com/news/articles/2026-11-02/anthropic-ipo-explained-s-1-filing-nasdaq-listing-and-key-risks) · [SAP TechEd Agents](https://emergent.sh/news/sap-unveils-1-000-ai-agents-teched-2026) · [JPMorgan AI Agents](https://www.cnbc.com/2026/11/18/jpmorgan-hyundai-card-ai-agents-payments.html) · [SAP Economist Report](https://news.sap.com/2026/11/new-economist-enterprise-research-ai-moving-faster-than-organizations-can-adapt/)

---

## 💡 Ctac-relevantie

**SAP + AI-agents is de directe kapstok.** SAP's aankondiging van 1.000 geïntegreerde agents (TechEd 2026) is geen roadmap-preview maar een productrelease. Ctac's SAP-klanten krijgen deze agents standaard aangeboden – begrijpen wat ze doen, welke data ze raken en hoe ze geconfigureerd moeten worden, is nu een kwalificatievereiste. Prioriteit: intern kennismaken met SAP Joule en de agent-ecosysteemarchitectuur.

**Anthropic IPO kan Claudeprijzen en -beschikbaarheid beïnvloeden.** Als Ctac Claude (via API of Claude Code) in de workflow heeft ingebouwd, is het verstandig om de komende kwartaalresultaten en tariefstructuur te volgen. IPO-druk richting winstgevendheid kan leiden tot prijsverhogingen of prioritering van enterprise-tiers.

**EU AI Act deadline 2 december.** Klanten met generatieve AI-toepassingen in productie moeten nu actie ondernemen op labelling. Ctac kan hier nog dit kwartaal advieswerk op uitvoeren: snel, concreet, en verplicht.

**Security in AI coding tools is geen abstract risico meer.** Copilot CLI en Claude Code hadden beide in november gedocumenteerde kwetsbaarheden. Als Ctac-engineers deze tools dagelijks gebruiken (zeer waarschijnlijk), is een intern security-briefing over safe use van AI coding tools op zijn plek.

---

## 📚 Bronnen & verder lezen

- [LLM Release Tracker november 2026 – nhimg.org](https://nhimg.org/llm-release-tracker)
- [AI News Roundup November 2026 – joineta.org](https://joineta.org/blog/ai-news-roundup-november-2026)
- [BeevR: New AI Models November 2026](https://beevr.ai/blog/ai-model-releases-november-2026)
- [Anthropic IPO – Bloomberg (2 nov 2026)](https://www.bloomberg.com/news/articles/2026-11-02/anthropic-ipo-explained-s-1-filing-nasdaq-listing-and-key-risks)
- [Anthropic IPO – cryptobriefing.com](https://cryptobriefing.com/anthropic-ipo-november-19-trillion-valuation/)
- [SAP TechEd 2026: 1.000 AI Agents – emergent.sh](https://emergent.sh/news/sap-unveils-1-000-ai-agents-teched-2026)
- [SAP/Economist Enterprise Research – sap.com](https://news.sap.com/2026/11/new-economist-enterprise-research-ai-moving-faster-than-organizations-can-adapt/)
- [JPMorgan AI Agents FX – CNBC](https://www.cnbc.com/2026/11/18/jpmorgan-hyundai-card-ai-agents-payments.html)
- [EU AI Act – Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU AI Act Timeline 2028 – shattered.io](https://shattered.io/eu-ai-act-world-first-ai-law-five-dates-to-2028-2026/)
- [Adversa AI: Coding Agent Vulnerabilities](https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/)
- [Adversa AI: GenAI Security November 2026](https://adversa.ai/blog/top-genai-security-resources-november-2026/)
- [AI Agent Security – Amazon Bedrock/MCP](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/)
- [Trellix CyberThreat Report November 2026](https://www.trellix.com/advanced-research-center/threat-reports/november-2026/)
- [Singapore Consensus AI Safety 2026 – arxiv](https://arxiv.org/pdf/2608.14611)
