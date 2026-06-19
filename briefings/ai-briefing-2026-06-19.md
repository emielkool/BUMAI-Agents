---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-19
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 19 juni 2026

## 🔑 Highlights van de dag

- **Microsoft bouwt eigen AI-modelstack op:** MAI-Thinking-1, een 35B-parameter redeneermodel, luidt de introductie in van een Microsoft-eigen modelline-up — strategisch cruciaal nu de afhankelijkheid van OpenAI bewust wordt afgebouwd.
- **Prompt injection treft drie grote agentic coding tools tegelijk:** Claude Code, Gemini CLI en GitHub Copilot bleken tegelijk kwetsbaar via kwaadaardige GitHub-comments, met API-sleuteldiefstal als gevolg — een wake-up call voor enterprise AI-adoptie.
- **EU AI Act: deadline 2 augustus nadert, harmonised standards ontbreken nog:** De EC publiceerde op 17 juni de State of the Digital Decade 2026 en een code of practice voor AI-contentlabeling, maar cruciale technische standaarden zijn er nog niet.
- **Benelux koploper in Europa:** NL (61%) en BE (62%) tonen de hoogste AI-adoptiepercentages van Europa; flessenhals is het digitale talenttekort (58% van bedrijven).
- **Adobe lanceert agentic workflows over Creative Cloud:** Per 18 juni in publieke beta — een duidelijk signaal dat agentic AI productierijp wordt buiten pure softwareontwikkeling.

## 🧠 Technologie & Modellen

**Microsoft eigen modelstack** – Microsoft's AI Superintelligence Team lanceerde een familie van zeven eigen modellen, te beginnen met **MAI-Thinking-1**: een reasoning model met 35B actieve parameters en een 256K contextvenster. Dit valt samen met de lanceringen van Microsoft IQ (GitHub Copilot, Foundry, Copilot Studio) en Work IQ (GA per 16 juni). De stap naar eigen modellen versterkt Microsoft's onafhankelijkheid van OpenAI op lange termijn. ([Microsoft Build 2026 Blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/))

**OpenAI GPT-upgrade:** GPT-5.2 is per 12 juni niet meer beschikbaar in ChatGPT; gebruikers worden automatisch doorgestuurd naar GPT-5.5. GPT-4.5 wordt 27 juni volledig teruggetrokken. Dit tempo van modelrotatie versnelt — relevant voor enterprise-integraties die pinnen op specifieke modelversies. ([OpenAI News](https://openai.com/news/))

**Agentic coding agents prolifereren:** Cohere lanceerde **North Mini Code** (30B MoE, 256K context, Apache 2.0) op 9 juni, en Xiaomi bracht **MiMo Code V0.1.0** uit op 10 juni (MIT-licentie, terminal-native). Het open-source landschap voor coding agents rijpt snel en vergroot de druk op commerciële spelers. ([VentureBeat – Cohere](https://venturebeat.com/technology/cohere-open-sources-a-coding-agent-that-runs-on-a-single-h100))

**Microsoft MXC + Adobe Agentic Creative Cloud:** Microsoft's **Execution Containers (MXC)** zijn een OS-niveau sandbox voor AI-agents, waarbij kernel-enforced beleidsregels bepalen wat een agent mag aanraken — direct antwoord op de groeiende security-zorgen rond agentic systemen. Adobe integreerde agentic workflows over Creative Cloud (Premiere Pro, Photoshop, Illustrator, InDesign) in publieke beta per 18 juni. ([VentureBeat – MXC](https://venturebeat.com/security/microsoft-launches-mxc-an-os-level-sandbox-for-ai-agents-with-openai-and-nvidia-already-on-board)) ([VentureBeat – Adobe](https://venturebeat.com/orchestration/adobe-embeds-agentic-ai-workflows-across-creative-cloud-shifting-from-media-generation-to-production-orchestration))

## 🏛️ Governance & Ethiek

De **EU AI Act** wordt per **2 augustus 2026** volledig van kracht voor hoog-risico toepassingen — maar harmonised standards zijn er nog niet, waardoor compliance-onzekerheid blijft voor bedrijven die nu moeten opleveren. Op 10 juni publiceerde de EC een **Code of Practice voor AI-contentlabeling** (transparantieplicht artikel 50), en op 17 juni verscheen de **State of the Digital Decade 2026**. De AI Office werkt aan praktijkrichtlijnen voor hoog-risico classificatie en incidentrapportage, maar die zijn nog niet gereed. Voor Ctac-klanten in gereguleerde sectoren is dit een urgent aandachtspunt. ([EU AI Act tijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)) ([EC – AI Act richtlijnen](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines))

## 🔐 Security & Risk

**Prompt injection treft agentic coding tools breed:** Onderzoek toonde aan dat Claude Code, Gemini CLI en GitHub Copilot tegelijk kwetsbaar zijn voor prompt injection via GitHub-comments — aanvallers kunnen API-sleutels en tokens stelen via PR-titels, issue bodies en comments. Dit is geen theoretisch risico: de aanvalsvector is actief geëxploiteerd. ([VentureBeat – AI agent security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**Microsoft Semantic Kernel RCE:** CVE-2026-25592 en CVE-2026-26030 kunnen prompt injection omzetten in host-level remote code execution bij enterprise deployments die Semantic Kernel gebruiken — direct patchen is vereist.

**Cyberaanvallen via AI nemen toe in Benelux:** DataNews België meldt een duidelijke stijging van AI-gestuurde cyberaanvallen in Nederland en België. ([DataNews](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/))

## 📈 Markt & Adoptie

Microsoft en Google domineren het enterprise AI-marktlandschap; AWS investeert $10B in North Carolina datacenters als deel van een $100B capex-plan voor 2026. Ondanks de investeringsgolf zit **twee derde van de bedrijven nog vast in de pilot-fase** van generatieve AI en verwachten executives slechts 27% ROI op korte termijn. Microsoft **Agent 365** is uit preview en nu breed beschikbaar. ([CIO Dive – marktleiders](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)) ([VentureBeat – Agent 365](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat))

**Benelux-specifiek:** NL 61%, BE 62% AI-adoptie — hoogste in Europa. Het **Vlam**-platform (soeverein rijks-AI voor ministeries) gaat in H2 2026 breed in productie. **Project Enki** (Amsterdam) onderzoekt AI-datacenters op zee naast offshore windparken samen met Vattenfall. ([Computable – Enki](https://www.computable.nl/2026/06/18/kort-project-enki-bouwt-ai-datacenters-op-zee-netwerken-binnen-drie-jaar-aan-limiet-en-meer/)) ([Computable – Vlam](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/))

## 💡 Ctac-relevantie

Drie prioriteiten voor Ctac deze week:

1. **Prompt injection als dealbreaker bij agentic AI-projecten:** De gelijktijdige kwetsbaarheid van Claude Code, Gemini CLI en Copilot in GitHub-workflows is direct relevant voor Ctac-teams die met agentic coding werken. Beoordeel of interne CI/CD-pipelines blootgesteld zijn en stel een mitigatiebeleid op — Microsoft MXC biedt een architectureel referentiekader voor sandboxing van agents.

2. **EU AI Act 2 augustus als commercieel gesprek:** Met de deadline voor hoog-risico regels naderend en standaarden nog niet gereed, heeft Ctac een opening voor compliance-advies richting klanten in overheid, zorg en finance. Het ontbreken van harmonised standards is frustrerend voor bedrijven maar creëert een concrete advieskans.

3. **Van pilot naar productie is het kernvraagstuk:** Twee derde van bedrijven zit vast in de pilot-fase. Dit is precies het patroon dat Ctac als IT-consultant kan doorbreken. Positioneer de AI-unit expliciet als brug van proof-of-concept naar productieschaal — met name voor sectoren waar Vlam en soortgelijke platforms relevant zijn (overheid, semi-overheid).

## 📚 Bronnen & verder lezen

- [Microsoft Build 2026 – MAI-Thinking-1 & Microsoft IQ](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [OpenAI News – GPT-5.5 migratie](https://openai.com/news/)
- [VentureBeat – Cohere North Mini Code (open source)](https://venturebeat.com/technology/cohere-open-sources-a-coding-agent-that-runs-on-a-single-h100)
- [VentureBeat – Prompt injection in AI coding agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – Microsoft MXC OS-sandbox voor agents](https://venturebeat.com/security/microsoft-launches-mxc-an-os-level-sandbox-for-ai-agents-with-openai-and-nvidia-already-on-board)
- [VentureBeat – Adobe Agentic Creative Cloud](https://venturebeat.com/orchestration/adobe-embeds-agentic-ai-workflows-across-creative-cloud-shifting-from-media-generation-to-production-orchestration)
- [VentureBeat – Microsoft Agent 365 GA](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act praktijkrichtlijnen](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [CIO Dive – Microsoft & Google enterprise AI dominantie](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Computable – Project Enki AI-datacenters op zee](https://www.computable.nl/2026/06/18/kort-project-enki-bouwt-ai-datacenters-op-zee-netwerken-binnen-drie-jaar-aan-limiet-en-meer/)
- [Computable – Vlam rijksbreed AI-platform](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/)
- [DataNews – Meer cyberaanvallen door AI in Benelux](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
- [Computable – Benelux koploper in AI-adoptie](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
