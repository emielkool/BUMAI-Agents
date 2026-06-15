---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-03
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 3 mei 2026

## 🔑 Highlights van de dag

- **Microsoft Agent 365 is per 1 mei algemeen beschikbaar** – samen met de nieuwe M365 E7 "Frontier Suite" markeert dit een definitieve verschuiving van Copilot-als-assistent naar Copilot-als-autonome-agent; voor Ctac als Microsoft-partner is dit het meest directe actie-item van dit moment.
- **GPT-5.5 en Claude Opus 4.7 verhitten de topmodel-race** – OpenAI's GPT-5.5 (GA 24 april) scoort state-of-the-art op 14 benchmarks en is sterk in agentic computer use; Anthropic's Opus 4.7 (GA) leidt op software engineering. Beide modellen kosten $5/M input-tokens – prijspariteit is bereikt aan de top.
- **DeepSeek-V4 verstoort de kosten­calculus** – nabij state-of-the-art prestaties voor 1/6e de prijs van GPT-5.5 of Opus 4.7; dit zet druk op enterprise-budgetteringen voor AI-workloads.
- **EU AI Act: nog 3 maanden tot de grote deadline** – 2 augustus 2026 worden de regels voor hoog-risico AI-systemen van kracht; Q2 2026-guidance­documenten worden nu gepubliceerd, maar veel organisaties zijn nog niet compliant.
- **Prompt injection escaleert naar enterprise­niveau** – EchoLeak (Microsoft 365 Copilot) en CVE-2025-53773 (GitHub Copilot, CVSS 9.6) zijn recente voorbeelden van exploits die data exfiltreren via agentic AI-systemen.

---

## 🧠 Technologie & Modellen

**Microsoft Agent 365 & M365 E7** – Per 1 mei 2026 is Microsoft Agent 365 algemeen beschikbaar, parallel aan de launch van Microsoft 365 E7 "The Frontier Suite". Copilot heeft nu agentic capabilities in Word, Excel en PowerPoint (GA 22 april). Dit is de meest directe enterprise­integratie van agentic AI tot nu toe. ([Microsoft 365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/04/22/copilots-agentic-capabilities-in-word-excel-and-powerpoint-are-generally-available/))

**GPT-5.5** – OpenAI positioneert dit als "smartest and most intuitive model yet", sterk in agentic computer use, coding en economische kenniswerktaken. API-prijs: $5/M input, $30/M output. ([OpenAI](https://openai.com/index/introducing-gpt-5-5/) | [TechCrunch](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/))

**Claude Opus 4.7** – Anthropic's krachtigste GA-model, het sterkst op software engineering en redeneren-zonder-tools. Beschikbaar via API, Amazon Bedrock, Google Vertex AI én Microsoft Foundry. Bijzonder: Anthropic's beperkt uitgerold model "Mythos" (preview bij partners) is nog krachtiger met focus op cybersecurity-toepassingen. ([Anthropic](https://www.anthropic.com/news/claude-opus-4-7) | [VentureBeat](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm))

**DeepSeek-V4 & open-source inhaalslag** – DeepSeek-V4 biedt nabij-SOTA prestaties voor 1/6e de prijs van Opus 4.7 en GPT-5.5. Mistral lanceerde een nieuw 128B-model met agentic "Work mode"; Qwen3.5 verbeterde multimodale redenering. De kloof tussen open-source en proprietary is nagenoeg gesloten op veel benchmarks. ([VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5))

---

## 🏛️ Governance & Ethiek

**EU AI Act – 3 maanden tot de grote deadline** – 2 augustus 2026 worden de bepalingen voor hoog-risico AI-systemen van kracht, inclusief transparantievereisten en de verplichting voor lidstaten om nationale toezichthouders aan te wijzen. De Europese Commissie publiceert in Q2 2026 ondersteunings­instrumenten en guidance­documenten – die komen er nu dus aan. Organisaties die nog niet zijn begonnen met classificatie van hun AI-systemen lopen reëel compliancerisico. ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/) | [Legalnodes](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks))

**Governance achterloopt op agentische deployments** – Een recent stuk in ICT Magazine NL stelt dat AI-agents breed worden ingezet terwijl governance structureel achterblijft. Dit is geen theoretisch risico: 96% van enterprise-organisaties zet al AI-agents in, maar beleid en controlelaag ontbreken vaak. ([ICT Magazine NL](https://www.ictmagazine.nl/nieuws/ai-agents-worden-overal-ingezet-maar-governance-blijft-ver-achter/))

---

## 🔐 Security & Risk

**EchoLeak – zero-click data-exfiltratie via M365 Copilot** – Onderzoekers ontdekten een kwetsbaarheid waarbij een prompt injection in een document of e-mail Copilot kon instrueren om enterprise­data stil te exfiltreren, zonder gebruikersinteractie. Microsoft heeft gepatcht, maar het incident illustreert het aanvalsoppervlak van agentic AI in productiviteitssoftware.

**CVE-2025-53773 – GitHub Copilot remote code execution (CVSS 9.6)** – Een verborgen prompt injection in pull request-omschrijvingen activeerde remote code execution via GitHub Copilot. Dit is een directe dreiging voor development-teams die Copilot gebruiken in CI/CD-pipelines. ([Google Security Blog](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html) | [airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

**Schaal neemt toe** – Unit 42 documenteerde in maart 2026 de eerste grootschalige indirecte prompt injection-aanvallen in het wild, inclusief ad review-ontwijking en system prompt leakage op commerciële platforms. Malicieuze prompts namen 32% toe tussen november 2025 en februari 2026. Prompt injection blijft OWASP's #1 LLM-risico. ([Cisco State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report))

---

## 📈 Markt & Adoptie

**Google Cloud: 800% YoY groei in enterprise AI** – In Q1 2026 boekte Google Cloud $20 miljard omzet (+63% YoY), met enterprise AI als primaire groeidriver. Gemini 3.1 Ultra (2M-token contextvenster, natively multimodaal) wordt gepositioneerd als platform voor organisaties die "AI-first" willen herbouwen. ([FourWeekMBA](https://fourweekmba.com/ai-cloud-ai-race-q1-2026-aws-28-azure-40-google-cloud-800-ai-gr/) | [TechResearchOnline](https://techresearchonline.com/news/google-cloud-next-2026-enterprise-ai-agents/))

**Microsoft AI op $37 miljard run rate** – Azure groeide 40% in Q1 2026; Microsoft's AI-business vertegenwoordigt een jaarlijkse omzet van $37 miljard (+123% YoY). Dragon Copilot voor de healthcare-sector is nu ook beschikbaar in Nederland. ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/))

**Agentic AI-markt: $8,5 miljard in 2026** – Deloitte schat de agentic AI-markt op $8,5 miljard dit jaar, groeiend naar $35–45 miljard in 2030. Gartner verwacht dat 40% van enterprise-applicaties eind 2026 AI-agents bevat (vs. <5% in 2025).

---

## 💡 Ctac-relevantie

**Directe actie: Microsoft Agent 365 & M365 E7 positionering** – Ctac is Microsoft-partner en de GA van Microsoft Agent 365 (1 mei) is hét moment om klanten proactief te benaderen. De vraag is niet meer "wanneer beginnen we met AI", maar "welke agents implementeren we eerst en hoe borgen we controle?" Ctac kan hier als trusted advisor fungeren door governance-kaders en implementatie-aanpak te bieden naast technische integratie.

**EU AI Act compliance als propositie** – Met de augustus-deadline nadert is er een concreet adviesbehoeftevenster voor klanten in gereguleerde sectoren (overheid, zorg, finance). Ctac kan nu een beknopte AI-risicoaudit aanbieden waarmee klanten inzicht krijgen in hun expositie. De guidance­documenten die de EC dit kwartaal publiceert kunnen als basis dienen.

**Security-bewustzijn bij agentic deployments** – EchoLeak en CVE-2025-53773 laten zien dat het gebruik van Microsoft 365 Copilot en GitHub Copilot actieve security-aandacht vereist. Bij klanten die deze tools al inzetten is een korte threat-awareness sessie goed verdedigbaar en differentiërend voor Ctac.

**DeepSeek-V4 als kostenverlaging voor interne tools** – Voor interne of klantgerichte AI-toepassingen waarbij topkwaliteit niet kritisch is, is DeepSeek-V4 een serieuze optie geworden. Dit verlaagt de drempel voor MVP-ontwikkeling en pilot-projecten aanzienlijk.

---

## 📚 Bronnen & verder lezen

- [OpenAI: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [TechCrunch: OpenAI releases GPT-5.5](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)
- [Anthropic: Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [VentureBeat: Claude Opus 4.7](https://venturebeat.com/technology/anthropic-releases-claude-opus-4-7-narrowly-retaking-lead-for-most-powerful-generally-available-llm)
- [VentureBeat: DeepSeek-V4 vs Opus 4.7 / GPT-5.5](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- [Microsoft 365 Blog: Copilot agentic capabilities GA](https://www.microsoft.com/en-us/microsoft-365/blog/2026/04/22/copilots-agentic-capabilities-in-word-excel-and-powerpoint-are-generally-available/)
- [Microsoft Blog: Accelerating Frontier Transformation with partners](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [LegalNodes: EU AI Act 2026 compliance](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [Google Security Blog: Prompt injections in the wild](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html)
- [airia.com: AI Security in 2026 – Prompt Injection](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Cisco State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)
- [FourWeekMBA: Cloud AI race Q1 2026](https://fourweekmba.com/ai-cloud-ai-race-q1-2026-aws-28-azure-40-google-cloud-800-ai-gr/)
- [ICT Magazine NL: AI agents en governance](https://www.ictmagazine.nl/nieuws/ai-agents-worden-overal-ingezet-maar-governance-blijft-ver-achter/)
- [LLM-stats: AI News May 2026](https://llm-stats.com/ai-news)
