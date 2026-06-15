---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-01
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 1 mei 2026

## 🔑 Highlights van de dag

- **Claude Opus 4.7 is live** – Anthropic releaset zijn nieuwste flagship model op alle platforms (API, Bedrock, Vertex AI, Microsoft Foundry). Tegelijk houdt Anthropic een krachtiger model ("Mythos") achter gesloten deuren vanwege vermeende cybersecurity-risico's.
- **Microsoft lanceert M365 E7 + Agent 365** – Vandaag (1 mei) worden Microsoft 365 E7 en de bijbehorende Agent 365-controlplane algemeen beschikbaar; Mercedes-Benz is de eerste grote Europese volledige uitrol.
- **Prompt injection is structureel, niet oplosbaar** – OpenAI erkent formeel dat prompt injection in AI-agents nooit deterministisch te beveiligen is. Drie grote coding-agents lekten tegelijk gevoelige data via één indirecte aanval.
- **Open-source dicht het gat** – Qwen 3.6, GLM-5.1 en DeepSeek-V4-Pro bereiken state-of-the-art op coding- en reasoning-benchmarks en maken de dominantie van closed-source modellen steeds minder vanzelfsprekend.
- **EU AI Act-deadline nadert** – Volledige toepasselijkheid per 2 augustus 2026; harmonisatiestandaarden zijn nog niet gereed en nationale sandboxes moeten vóór die datum operationeel zijn.

---

## 🧠 Technologie & Modellen

**Anthropic Claude Opus 4.7** is vandaag uitgerold over alle distributiekanalen (Anthropic API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry). Het model positioneert zich als een nieuwe topstandaard voor redeneren en agentic taken. Opvallend: Anthropic werkt parallel aan een niet-publiek model genaamd "Mythos", dat wegens potentieel misbruik in de cybersecurity-sfeer voorlopig alleen beschikbaar is voor geselecteerde partners — een teken dat de frontier-labs steeds voorzichtiger worden met brede releases van high-capability modellen.

In het open-source segment verdienen drie releases aandacht: **Qwen 3.6-27B en -35B** (Alibaba), **GLM-5.1** (Zhipu AI) en **DeepSeek-V4-Pro**. GLM-5.1 claimt state-of-the-art op SWE-Bench Pro (autonome software-engineering). Deze modellen zijn zonder licentiekosten inzetbaar en verkleinen de TCO-argumenten voor closed-source alternatieven significant.

*Bronnen: [Anthropic – Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) | [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026) | [TechCrunch – Anthropic Mythos](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)*

---

## 🏛️ Governance & Ethiek

De **EU AI Act** wordt per 2 augustus 2026 volledig van kracht. Twee knelpunten verdienen aandacht: (1) CEN/CENELEC heeft de gevraagde harmonisatiestandaarden nog niet opgeleverd — alleen prEN 18286 (Art. 17 kwaliteitsmanagementsysteem voor hoog-risico AI) is in publieke consultatie. (2) Lidstaten moeten vóór augustus nationale AI-regulatory sandboxes ingesteld hebben; de voortgang verschilt sterk per land.

De workshops rond de **Code of Practice voor markering van AI-gegenereerde content** lopen tot en met mei 2026. Dit is relevant voor contentpublicerende organisaties en mediabedrijven.

In Nederland blijkt uit onderzoek dat **gemeenten onvoldoende nadenken over governance** bij AI-inzet: experimenteren gaat snel, kaders voor soevereiniteit en risicobeheersing blijven achter.

*Bronnen: [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/) | [EC – Guidelines AI Act](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines) | [Computable – gemeenten en AI](https://www.computable.nl/2026/03/30/gemeenten-denken-te-weinig-na-over-inzet-van-ai/)*

---

## 🔐 Security & Risk

**Prompt injection blijft het dominante aanvalsvlak voor AI-agents.** OpenAI heeft publiekelijk erkend dat dit type aanval nooit volledig deterministisch te blokkeren is — vergelijkbaar met social engineering op het web. Ondertussen toonde nieuw onderzoek aan dat Claude Code, Gemini CLI en Microsoft Copilot tegelijk vatbaar zijn voor eenzelfde indirecte prompt-injection, waarbij geheimen via een enkel kwaadaardig bestand uitlekken.

Microsoft heeft **CVE-2026-21520** (CVSS 7.5) gerepareerd in Copilot Studio, maar data-exfiltratie was in sommige gevallen al opgetreden voor de patch. Daarnaast zijn meer dan 30 kwetsbaarheden gedocumenteerd in populaire AI-IDE's (Cursor, Windsurf, GitHub Copilot, Zed) onder de naam "IDEsaster".

**Praktisch advies:** Organisaties die coding-agents of browser-agents inzetten moeten rekening houden met structurele prompt-injection-risico's en mogen niet vertrouwen op uitsluitend default-beveiligingen van de vendor.

*Bronnen: [VentureBeat – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [VentureBeat – Copilot Studio CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook) | [TechCrunch – prompt injection structureel](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)*

---

## 📈 Markt & Adoptie

**Microsoft** lanceert vandaag M365 E7, dat M365 E5, Entra Suite, Copilot en het nieuwe **Agent 365** combineert tot één enterprise AI-laag. Agent 365 fungeert als governance- en orkestratie-platform voor AI-agents binnen de Microsoft-stack. Mercedes-Benz is de eerste grote Europese uitrol. Dit signaleert dat enterprise AI-adoptie verschuift van pilotfase naar brede operationalisering.

**Google** introduceerde eerder deze maand **Agentic Data Cloud** op Google Cloud Next '26: een AI-native architectuur die legacy-dataplатformen omzet in reasoning-engines voor agents. Marktanalyse toont dat Microsoft en Google samen de enterprise AI-markt domineren, waarbij Microsoft sterk staat door ecosysteembreedte en Google door agentic AI-integratie.

**OpenAI** heeft **Workspace Agents** gelanceerd — een opvolger van Custom GPTs die direct koppelt aan Slack, Salesforce en andere enterprise-tools.

Google investeert tot **$40 miljard in Anthropic** (eerste tranche $10 miljard) en verankert daarmee zijn positie als primaire compute-partner voor Claude-modellen.

*Bronnen: [Microsoft Blog – M365 E7 launch](https://blogs.microsoft.com/blog/2026/04/28/unlocking-human-ambition-to-drive-business-growth-with-ai/) | [CIO Dive – Microsoft Google marktleiderschap](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/) | [TechCrunch – Google investeert in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)*

---

## 💡 Ctac-relevantie

**Agent 365 als enterprise-entry point:** De GA-lancering van Microsoft Agent 365 is direct relevant voor Ctac's klanten in de Microsoft-stack. Dit is het moment om governance-gesprekken bij klanten te initiëren: wie beheert welke agents, hoe wordt audit-logging ingericht, en hoe past dit in bestaande compliance-kaders (inclusief EU AI Act)? Ctac kan hier een begeleidende rol pakken vóórdat klanten zelf ad-hoc gaan implementeren.

**Prompt injection = concreet risico voor lopende en nieuwe projecten:** Nu OpenAI erkent dat prompt injection structureel is, moeten klant-facing AI-agents bij Ctac worden beoordeeld op hun blootstelling. Dit is een gesprekstrigger richting security-aware klanten (overheid, finance) én een propositie-kans voor een AI-security quickscan.

**Open-source modellen verlagen de instapdrempel:** GLM-5.1 en Qwen 3.6 presteren op het niveau van closed-source modellen in coding-taken. Voor klanten met dataprivacy-bezwaren (zorg, overheid) zijn zelf-gehoste open-source modellen nu serieus bespreekbaar als alternatief — en Ctac kan dit faciliteren.

**Nederland-specifiek:** De constatering dat Nederlandse gemeenten onvoldoende kaders hebben bij AI-inzet is een directe kans in het publieke-sector segment. Een governance-as-a-service aanbod aansluitend op de EU AI Act-vereisten heeft timing mee.

---

## 📚 Bronnen & verder lezen

- [Anthropic – Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [TechCrunch – Google investeert $40B in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [Microsoft Blog – M365 E7 & Agent 365 launch](https://blogs.microsoft.com/blog/2026/04/28/unlocking-human-ambition-to-drive-business-growth-with-ai/)
- [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [VentureBeat – AI agent runtime security & prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – Microsoft Copilot Studio CVE prompt injection](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [TechCrunch – OpenAI over prompt injection](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Richtlijnen AI Act](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Computable – Gemeenten en AI-governance](https://www.computable.nl/2026/03/30/gemeenten-denken-te-weinig-na-over-inzet-van-ai/)
