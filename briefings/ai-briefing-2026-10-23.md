---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-23
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 23 oktober 2026

## 🔑 Highlights van de dag

- **EU AI Act: eerste handhavingsacties.** Het AI Office heeft informatieverzoeken gestuurd aan OpenAI en Anthropic na twee incidenten in de zomer van 2026. Geen boetes nog, maar het tijdperk van papieren compliance is voorbij.
- **Agentic AI Foundation bereikt 10 projecten.** Vier nieuwe open-source agentprojecten toegevoegd op 22 oktober, waaronder bijdragen van Anthropic, OpenAI, Hugging Face en Alibaba — het ecosysteem rondom MCP/agentprotocollen consolideert zich snel.
- **Prompt injection van theorie naar exploitatie.** CVE-2025-53773 (GitHub Copilot, CVSS 9.6) en de Cline npm-compromis tonen dat AI-tools actief worden aangevallen. AI-codeerassistenten zijn nu de meest aangevallen productcategorie.
- **OpenAI breidt distributie uit naar Google Cloud.** GPT-6 en Codex-workflows worden beschikbaar via Google Cloud's Model Garden — een strategisch signaal dat OpenAI zijn afhankelijkheid van Microsoft wil verminderen.
- **Model-releases week 43.** Claude Haiku 5.5 (Anthropic), GPT-6 Pro met parallelle agents (OpenAI) en Gemini 4 Argon (Google) worden breed gemeld, maar bronnen spreken elkaar tegen op data en namen — wacht op primaire bevestiging.

---

## 🧠 Technologie & Modellen

**Modelreleases: druk maar diffuus.** Trackers melden Claude Haiku 5.5 (7 oktober, effort controls, 1M context, tweeledig prijsmodel), GPT-6 Pro met parallelle agents (16 oktober) en Gemini 4 Argon (algemene beschikbaarheid 13 oktober). Opvallend: de bronnen zijn inconsistent, sommige lijken geaggregeerd uit andere aggregators. Oordeel: de richting klopt (alle grote labs releasen sneller en goedkoper), maar verifieer modeldetails via de officiële blogs vóór klantgesprekken.

**Agentic AI Foundation — 10 projecten in jaar één.** Op 22 oktober — parallel aan AGNTCon + MCPCon in San Jose — kondigde de Agentic AI Foundation vier nieuwe projecten aan: Agent Skills (Anthropic), Open Responses (OpenAI), OpenEnv (Hugging Face) en OpenSandbox (Alibaba). Dit is een serieuze marktbewegng: het MCP-protocol en bijbehorende toolstandaarden krijgen een neutrale governance-laag, vergelijkbaar met hoe Linux Foundation open source verankerde. Voor Ctac relevant: standaardisatie verlaagt de lock-inrisico's van agentoplossingen voor klanten.

**NVIDIA Nemotron.** NVIDIA lanceerde drie open modellen (Nemotron-familie) gericht op lokale inferentie voor enterprise agents — interessant voor klanten die om data-soevereiniteit geven.

*Bronnen: [llm-stats.com](https://llm-stats.com/ai-news), [unite.ai – AAIF](https://www.unite.ai/agentic-ai-foundation-adds-four-projects-to-reach-10-in-first-year/), [aiagentsdirectory.com](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-17-2026)*

---

## 🏛️ Governance & Ethiek

**EU AI Act: van wet naar handhaving.** Vanaf 2 augustus 2026 zijn de handhavingsbevoegdheden van het AI Office en nationale toezichthouders actief. Op 14 oktober stuurde het AI Office de eerste informatieverzoeken aan OpenAI en Anthropic naar aanleiding van twee zomerincidenten met AI-agents. Geen formele procedures of boetes gemeld, maar de drempel is overgestoken. Tegelijkertijd loopt een consultatie over de boeteprocedures van het AI Office (sluitingsdatum: 9 november).

**Wat uitgesteld is:** De AI Omnibus (EU 2026/1744) schoof de verplichtingen voor hoog-risicosystemen (Bijlage III) door naar 2 december 2027 en Bijlage I naar 2 augustus 2028. Dat geeft organisaties iets meer lucht — maar de GPAI-verplichtingen (inclusief GPT-6 en Claude) gelden nú.

*Bronnen: [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act), [unite.ai – enforcement](https://www.unite.ai/eu-announces-first-ai-act-enforcement-actions-after-ai-agent-incidents/), [aiconference.london](https://aiconference.london/eu-ai-act-enforcement-begins-what-the-first-fines-will-look-like-20261013-07)*

---

## 🔐 Security & Risk

**Prompt injection is operationeel geworden.** Twee harde feiten: (1) CVE-2025-53773 in GitHub Copilot — CVSS 9.6, remote code execution via verborgen instructies in pull request-beschrijvingen. (2) De Cline npm-compromis in februari 2026 begon met een kwaadaardig GitHub issue-title. Anthropic patchte een autorisatie-bypass in claude-code-action binnen vier dagen. Microsoft patchte CVE-2026-25592 en CVE-2026-26030 in Semantic Kernel.

**Structureel probleem.** OpenAI gaf publiekelijk toe dat prompt injection in AI-browsers "waarschijnlijk nooit volledig gepatcht" wordt. Een GitInject-paper betoogt dat het architecturaal is: frontier models (inclusief Claude Sonnet 4.5) blijven kwetsbaar als configuratiebestanden uit onbetrouwde repository-content worden geladen.

**Actie:** Beperk agent-privileges, houd onbetrouwde data weg van verhoogde credentials en patch agent frameworks actief.

*Bronnen: [cycode.com](https://cycode.com/blog/ai-security-vulnerabilities/), [labs.cloudsecurityalliance.org](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/), [microsoft.com/security](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)*

---

## 📈 Markt & Adoptie

**OpenAI op Google Cloud.** OpenAI maakt GPT-6 en Codex beschikbaar via Google Cloud Model Garden. Dit is een opvallende stap: OpenAI diversifieert zijn distributie weg van de exclusieve Microsoft-afhankelijkheid. Strategisch signaal: de hyperscalers concurreren nu ook op model-distributie, niet alleen op infrastructuur.

**Azure domineert enterprise AI.** Morgan Stanley Q3 2026 CIO-survey (gepubliceerd 12 oktober): 79% van respondenten gebruikt Azure, 66% AWS, 43% Google Cloud. Op AI-orchestratie is Microsoft marktleider met 20% versus 17% voor alle LLM-aanbieders samen.

**Benelux: ambitie vs. realiteit.** IDC voor SAS: slechts 4% van Benelux-bedrijven gebruikt AI op een transformatieve manier. België loopt iets voor op Nederland qua adoptie (34,5% vs. 33,2% van bedrijven). Consultancy-markt groeit: 48 open AI-strategie en -consultancy-vacatures in de regio per oktober.

*Bronnen: [emirates247.com – OpenAI/Google](https://www.emirates247.com/technology/openai-to-sell-gpt-6-astra-and-codex-on-google-cloud-expanding-enterprise-ai-distribution/6990), [uncoveralpha.com – Q3 survey](https://www.uncoveralpha.com/p/q3-2026-channel-checks-and-alternative), [ictmagazine.nl – Benelux](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)*

---

## 💡 Ctac-relevantie

**AI Act compliance is nu een verkoopargument.** De eerste handhavingsacties maken EU AI Act-gereedheid concreet voor klanten — ook al zijn de hoog-risicoverplichtingen uitgesteld. Ctac kan nú helpen bij GPAI-risicobeoordelingen en transparantiedocumentatie, voordat klanten worden overvallen door een informatieverzoek van het AI Office.

**Agent-security als propositie.** De prompt injection CVEs tonen dat AI-tooling productieklaar moet zijn vóórdat het de DTAP-straat ingaat. Ctac's AI engineer kan hier een concrete checklist en hardeningsaanpak van maken — een propositie die aansluit bij de "weinig vertrouwen in besluitvorming"-zorg die IDC signaleert in de Benelux.

**Standaardisatie verlaagt adoptiedrempel.** De consolidatie rond MCP en de Agentic AI Foundation-projecten maakt het eenvoudiger om agentoplossingen te bouwen zonder deep vendor lock-in. Voor Ctac's klanten in overheid en zorg — sectoren met hoge data-soevereiniteitseisen — is dit een opening om nu een robuuste agent-architectuur neer te zetten.

---

## 📚 Bronnen & verder lezen

- [llm-stats.com – AI News Oktober 2026](https://llm-stats.com/ai-news)
- [unite.ai – AAIF 10 projecten](https://www.unite.ai/agentic-ai-foundation-adds-four-projects-to-reach-10-in-first-year/)
- [unite.ai – EU AI Act eerste handhaving](https://www.unite.ai/eu-announces-first-ai-act-enforcement-actions-after-ai-agent-incidents/)
- [digital-strategy.ec.europa.eu – handhavingskader AI Act](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [aiconference.london – EU AI Act boetes](https://aiconference.london/eu-ai-act-enforcement-begins-what-the-first-fines-will-look-like-20261013-07)
- [cycode.com – AI security kwetsbaarheden 2026](https://cycode.com/blog/ai-security-vulnerabilities/)
- [labs.cloudsecurityalliance.org – indirect prompt injection](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/)
- [microsoft.com/security – RCE in AI agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [emirates247.com – OpenAI op Google Cloud](https://www.emirates247.com/technology/openai-to-sell-gpt-6-astra-and-codex-on-google-cloud-expanding-enterprise-ai-distribution/6990)
- [uncoveralpha.com – Q3 2026 cloud & AI channel checks](https://www.uncoveralpha.com/p/q3-2026-channel-checks-and-alternative)
- [ictmagazine.nl – AI adoptie Benelux](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)
- [aiagentsdirectory.com – agent news brief 17 okt](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-17-2026)
