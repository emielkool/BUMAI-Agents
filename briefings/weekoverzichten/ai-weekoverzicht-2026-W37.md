---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W37
Periode: 2026-09-07 / 2026-09-13
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 37 (7–13 september 2026)

## 📅 Dagentries

### Maandag 7 september
→ Dagbriefing: [ai-briefing-2026-09-07.md](../ai-briefing-2026-09-07.md)

**Highlights:**
- **GPT-6 "Astra" gelanceerd** – OpenAI's krachtigste model ooit, maar controversieel door opaque recurrence die de chain-of-thought verbergt en auditing bemoeilijkt.
- **EU AI Act handhaving actief** – Europese AI Office enforceert per 2 augustus; deepfake-labeling, GPAI-transparantie en verbod op onaanvaardbare-risico-AI zijn nu afdwingbaar. Recruitment voor 40 extra handhavingsagenten (deadline 8 september).
- **LiteLLM-kwetsbaarheden in CISA KEV** – Twee CVEs (CVE-2026-48710 & CVE-2026-42271) die gecombineerd authenticatie-bypass en RCE mogelijk maken in LiteLLM-deployments; directe patching vereist.

**Ctac-relevantie van de dag:** EU AI Act compliance is nu urgent voor Ctac-klanten in overheid, zorg en finance; de two-speed enterprise AI-kloof (McKinsey) opent een directe adviesopdracht voor mid-market organisaties die achterblijven op AI-schaalbaarheid.

---

### Dinsdag 8 september
→ Dagbriefing: [ai-briefing-2026-09-08.md](../ai-briefing-2026-09-08.md)

**Highlights:**
- **OpenAI GPT-6 Astra uitgerold** – Meest krachtige OpenAI-model tot nu toe (uitgebracht 3 september), met autonome "computer use"-functionaliteit; Greg Brockman spreekt van potentiële AGI. API-prijs $10/$50 per miljoen tokens; beperkte cybersecurity-capabilities in v1.
- **EU AI Omnibus: disclosure-deadline al verstreken** – Hoog-risico AI-systemen (Annex III) mogen tot december 2027 wachten, maar labeling en herkomstmarkering van generatieve output moest al op 2 augustus 2026 — een compliance-risico voor veel organisaties.
- **Prompt injection escaleert naar productie-incidents** – Drie AI-codeeragenten lekten credentials via één injectiepunt; Microsoft Copilot Studio CVE patchte niet volledig. Enterprise AI-security is operationeel probleem, geen theorie.

**Ctac-relevantie van de dag:** De combinatie van GPT-6 Astra's computer-use-mogelijkheden en de inmiddels verstreken disclosure-deadline schept twee directe kansen: korte-termijn pilots rondom documentverwerking voor klanten in publieke sector en finance, én een compliance-scan op AI-labeling voor klanten die generatieve AI al inzetten.

---

### Woensdag 9 september
→ Dagbriefing: [ai-briefing-2026-09-09.md](../ai-briefing-2026-09-09.md)

**Highlights:**
- **Dichtste modelweek van het jaar:** Claude Fable 5.1 (Anthropic, 1 sept), Gemini 3.8 Flash (Google, 2 sept) en GPT-6 Astra (OpenAI, 3 sept) verschenen binnen 72 uur — GPT-6 Astra is het eerste model dat OpenAI's interne 'critical-cyber safeguard'-drempel triggert.
- **Nvidia koopt Hugging Face voor $13 miljard:** De grootste open-source AI-hub wordt onderdeel van Nvidia's ecosysteem; het platform blijft open, maar verticale integratie van chip tot modelplatform is een marktbepalende stap.
- **Prompt injection escaleert in enterprise:** Aanvalsucceskansen op AI-agenten liggen op 50–84% (OWASP LLM01); kritieke CVE's in GitHub Copilot (CVSS 9.6) en Cursor IDE (CVSS 9.8) bewijzen dat dit een operationeel productierisico is.

**Ctac-relevantie van de dag:** EU AI Act handhaving is per 2 augustus een realiteit — klanten die GPAI-modellen in productie draaien hebben nu een directe compliancy-verplichting. Ctac kan zich onderscheiden met een vendor-agnostisch agentimplementatieraamwerk én een AI-security baseline (prompt injection defense-in-depth) als standaard onderdeel van elke enterprise AI-uitrol.

---

### Donderdag 10 september
→ Dagbriefing: [ai-briefing-2026-09-10.md](../ai-briefing-2026-09-10.md)

**Highlights:**
- **Dichtstste modelweek bevestigd:** Binnen 72 uur lanceerden Anthropic (Claude Fable 5.1 + Mythos 5.1), Google (Gemini 3.8 Flash), Meta (Muse Spark 1.3) en OpenAI (GPT-6 Astra) nieuwe frontiermodellen — "model fatigue" is nu ook mediaonderwerp.
- **Kritieke Azure OpenAI-kwetsbaarheid (CVE-2026-45499):** SSRF-flaw maakt zijwaartse beweging door aanvallers mogelijk in enterprise AI-omgevingen; 78% van de CISOs ziet AI als beveiligingsrisico (Proofpoint, vandaag gepubliceerd).
- **EU AI Act 15 september-deadline:** GPAI-aanbieders boven 10²⁵ FLOPs moeten aanstaande zondag hun eerste systeemrisico-evaluaties indienen bij het Europees AI-kantoor — voor Ctac-klanten een directe compliancy-actie.

**Ctac-relevantie van de dag:** De combinatie van de naderende GPAI-deadline én de kritieke Azure OpenAI-kwetsbaarheid vraagt om directe klantcommunicatie vóór het weekend. Tegelijk biedt de convergentie van hyperscaler-agentplatforms (Microsoft Foundry, Google, Amazon) een kans voor Ctac om klanten te helpen vendor-neutraal te evalueren — juist nu de adoptiedruk groot is maar ROI-bewijs ontbreekt.

---

### Vrijdag 11 september
→ Dagbriefing: [ai-briefing-2026-09-11.md](../ai-briefing-2026-09-11.md)

**Highlights:**
- **OpenAI Agents API in publieke beta** – Ontwikkelaars kunnen nu het gemanagde Codex-harnas gebruiken voor sessieorkestratie en contextcompressie; directe kans voor Ctac om agentic diensten te bouwen zonder eigen orkestratie-infrastructuur te schrijven.
- **Anthropic dreigingsrapport** – Biological-weapons-plots verstoord, Russische AI-gestuurde staatsespionage op Europese doelen, Chinese query-omleiding gedocumenteerd, én een vierde Claude-jailbreak erkend — AI-security is geopolitieke realiteit.
- **EU AI Act transparantieregels actief** – Per 2 augustus 2026 handhaaft de AI Office; Californië ondertekende aanvullend AI-auditwetgeving (10 sept). Enterprise-compliance kan niet langer worden uitgesteld.

**Ctac-relevantie van de dag:** De Agents API-beta combineert met de compliance-urgentie tot een dubbele kans: snel een proof-of-concept voor een klant opzetten op de nieuwe API, én klanten helpen hun AI-systemen te toetsen nu handhaving actief is.

---

## 🏆 Weekhighlights

1. **GPT-6 Astra markeert een breukpunt in AI-capabilities.** OpenAI lanceerde op 3 september zijn meest ambitieuze model met native computer use, 1,05 miljoen tokencontext en opaque recurrence — het eerste model dat OpenAI's eigen critical-cyber safeguard triggert. Frontier-AI is niet langer alleen een taalmodel maar een autonoom werkend systeem, met alle mogelijkheden én risico's van dien.

2. **EU AI Act handhaving is actief — en de eerste deadline is al verstreken.** Sinds 2 augustus 2026 handhaaft de EU AI Office; de disclosure- en labelingverplichtingen voor generatieve output gelden per die datum. De volgende deadline — systeemrisico-evaluaties voor GPAI-aanbieders boven 10²⁵ FLOPs — viel op 15 september. Compliance is geen voorbereiding meer, het is handhavingsrealiteit.

3. **Prompt injection escaleert van theorie naar geopolitieke realiteit.** Kritieke CVE's in Azure OpenAI (CVE-2026-45499 SSRF), GitHub Copilot (CVSS 9.6), Cursor IDE (CVSS 9.8) en LiteLLM (twee CISA KEV-entries) bewijzen dat enterprise AI-security een operationeel probleem is. Anthropic documenteerde statelijke actoren — Rusland en China — die frontier-AI actief inzetten voor spionage en biologische-wapenonderzoek.

4. **Nvidia neemt Hugging Face over voor $13 miljard.** De grootste consolidatiebeweging in het open-source AI-ecosysteem: verticale integratie van chip tot modelplatform. Meer dan 18 miljoen ontwikkelaars en 200.000 bedrijven zitten nu in Nvidia's ecosysteem. Het platform blijft open — vooralsnog.

5. **Hyperscalers convergeren op identieke enterprise agentarchitectuur.** Microsoft Foundry, Google Gemini Enterprise Agent Platform en Amazon Bedrock AgentCore bieden architectureel dezelfde bouwblokken (runtime, memory, tool gateway, identity, observability). OpenAI opende de Agents API als publieke beta. De drempel voor productiewaardige agentic AI is definitief verlaagd.

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De eerste week van september was historisch druk: binnen 72 uur lanceerden OpenAI (GPT-6 Astra), Anthropic (Fable 5.1 + Mythos 5.1), Google (Gemini 3.8 Flash) en Meta (Muse Glimmer 30B / Muse Spark 1.3) elk een nieuw frontiermodel — "model fatigue" is daarmee een begrip in de technologiepers. De rode draad: modellen worden agentic-first ontworpen, met computer use en multi-agent orkestratie als standaard feature in plaats van optionele uitbreiding. Open-source houdt gelijke tred: Qwen domineert met 151.000 afgeleide modellen op Hugging Face; Meta's open-weight modellen zijn nu serieus productie-rijp voor privacy-gevoelige toepassingen zonder cloudverplichting.

### 🏛️ Governance & Beleid

Week 37 markeert een definitief kantelpunt: de EU AI Act is niet langer voorbereiding maar handhavingsrealiteit. Disclosure- en labelingverplichtingen gelden per 2 augustus; de GPAI-systeemrisico-evaluatiedeadline van 15 september raakt de grootste modelaanbieders wereldwijd direct. De AI Omnibus versoepelde high-risk deadlines (Annex III) tot december 2027, maar verzwaarde de transparantievereisten die nú al gelden. Californische AI-auditwetgeving (ondertekend 10 september) fungeert historisch als voorbode voor bredere regulering. Patroon: handhaving versnelt, maar compliance-bewustzijn bij enterprise-organisaties blijft structureel achter.

### 🔐 Security & Risk

Prompt injection domineerde de week als primaire aanvalsvector: OWASP LLM01-aanvallen scoren 50–84% succeskans, en meerdere kritieke CVE's in productietools werden gedocumenteerd en geëxploiteerd. Het Anthropic dreigingsrapport (11 september) escaleerde het dreigingsniveau verder: statelijke actoren zetten frontier-AI actief in voor geopolitieke doeleinden — biologische-wapenonderzoeksplotjes verstoord, Russische staatsespionage op Europa en Oekraïne gedocumenteerd, Chinese query-omleiding bevestigd. CVE-2026-45499 (Azure OpenAI, SSRF) is de meest acuut te adresseren kwetsbaarheid voor Nederlandse enterprise-klanten die op Azure bouwen. Breder: 78% van CISOs erkent AI als beveiligingsrisico maar twee derde heeft geen adequate beveiligingsprocessen ingericht.

### 📈 Markt & Adoptie

Enterprise AI is definitief doorgebroken qua volume: Microsoft Copilot 20 miljoen betaalde seats, AI-omzetrun-rate $37 miljard (+123% YoY), EY met 150.000 medewerkers, NHS England met 500.000+ clinici. Maar: twee derde van de organisaties zit nog in pilotfase. McKinsey's two-speed race vergroot de kloof tussen enterprise (40% schaalt agents actief) en mid-market (22%). Gartner: slechts 22% heeft AI succesvol cross-business-unit geschaald. Wereldwijd AI capex 2026: $690 miljard — de infrastructuurrace gaat onverminderd door. Patroon: adoptie is breed maar oppervlakkig; de echte differentiator is werkproces-redesign rondom AI, niet toolselectie.

## 💼 Ctac-weekperspectief

- **Compliance is nu een instapproduct — handel direct.** De disclosure-deadline is verstreken, de GPAI-deadline (15 september) is dit weekend. Klanten in overheid, zorg en finance hebben nú hulp nodig bij AI-impact assessments en output-labeling. Aanbod: ontwikkel een AI-compliancescan als concreet instapproduct voor bestaande relaties — korte doorlooptijd, directe adviesbehoefte.

- **Pak de Agents API-kans voordat concurrenten dat doen.** OpenAI Agents API in publieke beta gecombineerd met de convergerende hyperscaler-platforms verlaagt de bouwdrempel voor agentic diensten drastisch. Concrete actie: start een proof-of-concept voor documentverwerking of klantservice-automatisering voor een bestaande klant — gebruik de nieuwe orkestratie-infrastructuur en bouw vendor-agnostisch zodat het migreerbaar blijft.

- **Stuur vóór maandag een security-alert over CVE-2026-45499.** De SSRF-kwetsbaarheid in Azure OpenAI treft exact het platform dat Ctac en haar klanten inzetten. Interne communicatie naar klantteams is urgente actie, geen nice-to-have. Koppel dit aan een bredere propositie: security-by-design als standaard onderdeel van elk agentic traject.

- **Positioneer Ctac als brug over de two-speed kloof.** Mid-market organisaties hangen tussen pilotfase en productie-waardige AI. McKinsey's onderscheidende factor — werkproces-redesign rondom AI in plaats van losse toolinzet — is precies het domein van Ctac's IT-consultancy. Ontwikkel een "AI-schaalbaarheidsaanpak" met de McKinsey/Gartner-criteria als onderbouwing: governance, vendor-neutrale architectuur, ROI-meting.

## 📚 Bronnenlijst

**Technologie & Modellen**
- [TechCrunch – OpenAI lanceert GPT-6 Astra](https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/)
- [Fortune – GPT-6 Astra, computer use, AGI-claim](https://fortune.com/2026/09/03/openai-debuts-gpt-6-astra-computer-use-greg-brockman-says-start-of-agi/)
- [CNBC – GPT-6 Astra cybersecurity-beperkingen](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)
- [TechCrunch – Anthropic Fable 5.1](https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/)
- [Hugging Face – Meta Muse Glimmer 30B](https://huggingface.co/blog/muse-glimmer)
- [Hugging Face – State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [Techxplore – Nvidia neemt Hugging Face over voor $13 mrd](https://techxplore.com/news/2026-09-nvidia-billion-source-platform.html)
- [CNBC – Model fatigue bij AI-labs](https://www.cnbc.com/2026/09/06/meta-google-openai-anthropic-ai-model-fatigue.html)
- [LLM Stats – AI news september 2026](https://llm-stats.com/ai-news)
- [OpenAI – Agents API publieke beta](https://openai.com/news/product-releases/)
- [arXiv – Survey on LLM Benchmarks aug 2026](https://arxiv.org/abs/2508.15361)
- [AI Weekly – Claude bewijst Fermat's Last Theorem](https://aiweekly.co/ai-news-today)

**Governance & Beleid**
- [EC Digital Strategy – EU AI Act handhaving gestart](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EC Digital Strategy – AI Omnibus in werking](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force)
- [artificialintelligenceact.eu – Implementatietijdlijn EU AI Act](https://artificialintelligenceact.eu/implementation-timeline/)
- [ComplianceHub.Wiki – AI Act Omnibus deadlines](https://compliancehub.wiki/eu-digital-omnibus-ai-act-deadline-deferral-annex-iii-2027/)
- [AnnexOps – EU AI Act implementatie 2026](https://annexops.com/eu-ai-act-implementation-2026/)
- [brightdefense.com – EU AI Act handhavingsdruk 2026](https://www.brightdefense.com/news/eu-ai-act-delay-keeps-2026-compliance-pressure/)
- [Tech Startups – Californische AI-auditwetgeving](https://techstartups.com/2026/09/10/top-tech-news-today-september-10-2026-apple-anthropic-ibm-meta-openai-spacex-more/)

**Security & Risk**
- [The Hacker News – CISA KEV LiteLLM-kwetsbaarheden](https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html)
- [The Hacker News – Enterprise AI Security 2026](https://thehackernews.com/2026/09/how-to-secure-enterprise-ai-from-adoption-to-incident-readiness.html)
- [VentureBeat – Prompt injection enterprise risico's](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – AI coding agents lekken secrets](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – Microsoft Copilot Studio CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [Help Net Security – Proofpoint CISO AI security rapport](https://www.helpnetsecurity.com/2026/09/10/proofpoint-ciso-ai-security-risks-report/)
- [Help Net Security – OWASP prompt injection rapport](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [SentinelOne – Top 14 AI Security Risks 2026](https://www.sentinelone.com/cybersecurity-101/data-and-ai/ai-security-risks/)
- [CSA – Indirect prompt injection in the wild](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/)
- [Airia – AI security & prompt injection 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Computable – Big Tech luidt noodklok kritieke infrastructuur](https://www.computable.nl/2026/09/01/big-tech-luidt-noodklok-ai-bedreigt-kritieke-infrastructuur/)
- [Datanews – Meer cyberaanvallen door AI in België](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)

**Markt & Adoptie**
- [HPCwire – McKinsey: enterprise AI two-speed race](https://www.hpcwire.com/aiwire/2026/09/02/mckinsey-report-enterprise-ai-is-becoming-a-two-speed-race/)
- [HPCwire – Gartner: 22% schaalt AI succesvol](https://www.hpcwire.com/aiwire/2026/09/01/gartner-finds-just-22-of-organizations-have-scaled-ai-across-business-units/)
- [Microsoft Blog – FY26 AI-adoptie overzicht](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [CIO Dive – Microsoft & Google enterprise AI-marktleiders](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [The New Stack – Enterprise agentconvergentie big three](https://thenewstack.io/amazon-microsoft-and-google-are-converging-on-the-same-enterprise-agent-architecture/)
- [Futurum – AI Capex 2026: $690 miljard](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/)
- [Deloitte – State of AI in the Enterprise 2026](https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html)
- [aibusinessweekly.net – AI adoptiestatistieken 2026](https://aibusinessweekly.net/p/ai-adoption-statistics)
- [VentureBeat – Microsoft eigen MAI-modellen](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [TechCrunch – Google WeatherNext 3](https://techcrunch.com/2026/09/03/googles-latest-ai-weather-model-gives-you-no-excuse-to-forget-your-umbrella/)
