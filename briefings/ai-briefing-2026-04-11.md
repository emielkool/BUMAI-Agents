# AI Dagbriefing – 11 april 2026

## 🔑 Highlights van de dag

- **Anthropic Mythos: krachtigste model ooit, maar niet voor iedereen** – Mythos is beperkt uitgerold via Project Glasswing aan 12 geselecteerde partners (waaronder Apple, Cisco en Microsoft) voor defensieve cybersecurity. Het model identificeerde in weken tijd duizenden zero-day kwetsbaarheden. De vraag is terecht: beschermt Anthropic het internet, of zijn eigen marktpositie?
- **EU AI Act-deadline wankelt** – Trilogiegesprekken (april/mei) kunnen de harde deadline van 2 augustus 2026 verschuiven naar december 2027 of zelfs augustus 2028. Voor NL/BE-bedrijven is dit dubbelzijdig nieuws: meer tijd, maar ook meer onzekerheid over wanneer te investeren in compliance.
- **Flowise CVSS 10.0: actieve exploitatie van AI-agent platform** – Een kritieke RCE-kwetsbaarheid in Flowise treft meer dan 12.000 publicly exposed instanties. Dit is het ernstigste AI-framework incident van 2026 tot nu toe.
- **Agentic AI accelereert toch: 33% van bedrijven ingedeeld** – KPMG meet een verdrievoudiging in agent-deployments in één kwartaal. Toch geeft 76% toe dat hun operaties nog niet klaar zijn voor autonome agents.
- **GLM-5 pakt #1 positie open-weights** – Chinees model van Zhipu AI wint de benchmark-strijd van Llama 4 en Qwen 3, staat bovenaan LMArena en Artificial Analysis. MIT-licentie, beschikbaar via Hugging Face.

---

## 🧠 Technologie & Modellen

**Anthropic Mythos & Project Glasswing** – Op 7 april lanceerde Anthropic een preview van Mythos, omschreven als een van hun "krachtigste modellen ooit". Het model is uitsluitend beschikbaar voor 12 partnerorganisaties (o.a. Amazon, Apple, Cisco, CrowdStrike, de Linux Foundation en Microsoft) voor defensieve cybersecurity-toepassingen. Binnen enkele weken identificeerde Mythos naar eigen zeggen duizenden kritieke zero-day kwetsbaarheden. TechCrunch stelt terecht de vraag of de beperkte toegang technisch noodzakelijk is, of strategisch.
*Bron: [TechCrunch, 7 april](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) | [Anthropic – Project Glasswing](https://www.anthropic.com/glasswing)*

**GLM-5 (Zhipu AI) – nieuw #1 open-weight model** – China's eerste beursgenoteerde AI-bedrijf heeft GLM-5 uitgebracht onder MIT-licentie. Het model staat bovenaan LMArena's Text Arena en Artificial Analysis onder open modellen, beschikbaar via Hugging Face en OpenRouter. Signaal: open-source AI-frontier is niet langer exclusief Amerikaans.
*Bron: [Hugging Face blog](https://huggingface.co/blog/mlabonne/glm-5)*

**NVIDIA Nemotron-3 Nano** – NVIDIA heeft Nemotron-3-Nano-30B uitgebracht op Hugging Face, onderdeel van het Agent Toolkit dat gelanceerd werd met steun van 17 enterprise-partners (Adobe, Salesforce, SAP, ServiceNow, Siemens). Gericht op lokale en enterprise agent-deployments.
*Bron: [VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)*

---

## 🏛️ Governance & Ethiek

**EU AI Act: deadline of uitstel?** – De harde compliance-deadline van 2 augustus 2026 staat formeel nog overeind, maar de realiteit is complexer. Cruciale guidance (high-risk classificatie, transparantie Code of Practice) is vertraagd, waardoor organisaties nauwelijks tijd hebben om te implementeren vóór de deadline. Het Europees Parlement en de Raad bespreken in de trilogue (april/mei) aanpassingen via de *AI Digital Omnibus* die de verplichtingen kunnen verschuiven naar december 2027 of augustus 2028.

Praktisch advies: behandel augustus 2026 nog steeds als werkdeadline voor interne AI-inventarisatie en risicoklassificatie – uitstel is politiek, governance-opbouw is sowieso noodzakelijk.
*Bronnen: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/) | [Legal Nodes](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks) | [Orrick](https://www.orrick.com/en/Insights/2025/11/The-EU-AI-Act-6-Steps-to-Take-Before-2-August-2026)*

**NL: defensie evalueert AI-systeem** – Het Nederlandse Ministerie van Defensie evalueert het Maven Smart System (MSS) voor militaire toepassingen. NOS Nieuwsuur bericht over brede zorgen rondom autonome AI-beslissingen in conflictsituaties – menselijk toezicht blijft juridisch en ethisch vereist.
*Bron: [NOS Nieuwsuur](https://nos.nl/nieuwsuur/artikel/2609142-zorgen-over-gebruik-van-ai-in-oorlogen-menselijke-afweging-blijft-nodig)*

---

## 🔐 Security & Risk

**Flowise RCE (CVE-2025-59528, CVSS 10.0) – actief geëxploiteerd** – De meest urgente AI-security dreiging van dit moment. De CustomMCP-node in Flowise voert willekeurige JavaScript-code uit zonder validatie, met volledige Node.js-privileges (inclusief toegang tot `child_process` en het bestandssysteem). Meer dan 12.000 publicly exposed instanties zijn kwetsbaar. Exploitatie is al waargenomen. Als jouw team of klanten Flowise gebruiken: patch onmiddellijk.
*Bron: [The Hacker News, april 2026](https://thehackernews.com/2026/04/flowise-ai-agent-builder-under-active.html)*

**AI-framework kwetsbaarheden stapelen zich op** – LangChain en LangGraph hadden in maart kritieke flaws waarbij bestanden, secrets en databases bereikbaar waren. Langflow had een CVE met exploitatie binnen 20 uur na disclosure. Patroon: AI-agent frameworks worden een prime target nu ze dieper in enterprise-infrastructuur integreren.
*Bron: [The Hacker News – LangChain/LangGraph](https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html)*

---

## 📈 Markt & Adoptie

**Agentic AI: adoptie versnelt, governance loopt achter** – Volgens KPMG deployt nu 33% van de organisaties AI-agents, een verdrievoudiging in één kwartaal. Salesforce boekte $540M omzet via Agentforce en voegde 6.000 enterprise-klanten toe in één kwartaal. Gartner raamt AI-softwarespending op $452 miljard in 2026 (+60% YoY). Maar: 76% van bedrijven geeft toe dat hun operaties nog niet gereed zijn voor autonome agents. Governance en proces-infrastructuur zijn de bottleneck, niet de technologie.
*Bronnen: [VentureBeat – Salesforce](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000) | [CIO Dive – Gartner](https://www.ciodive.com/news/generative-agentic-ai-global-spending-forecast-gartner/809783/) | [VentureBeat – process layer](https://venturebeat.com/orchestration/enterprise-agentic-ai-requires-a-process-layer-most-companies-havent-built)*

**AI-hardwarecrisis in Europa** – GPU-levertijden lopen op tot een jaar, DRAM-prijzen zijn met 171% gestegen en de nieuwste NVIDIA-chips zijn uitverkocht tot diep in 2027. EU-bedrijven die nu pas AI-infrastructuur willen bouwen, lopen serieus achter.
*Bron: [Computable.nl](https://www.computable.nl/persberichten/ai-hardwarecrisis-2026-wachten-op-chips-geen-optie-is-voor-eu-bedrijven/)*

---

## 💡 Ctac-relevantie

**1. Flowise en AI-framework security = directe kans**
Als Ctac klanten begeleidt bij het bouwen van AI-agent pipelines (LangChain, LangGraph, Flowise, n8n), is dit hét moment voor een gerichte security-check. Een "AI Infrastructure Security Scan" is direct te positioneren – er is concrete CVE-urgentie en klanten begrijpen het risico.

**2. EU AI Act: uitstel = geen excuus, maar wel ruimte**
De mogelijke verschuiving naar 2027/2028 geeft klanten een opening om governance gestructureerd op te bouwen, zonder paniek-compliance. Ctac kan dit framen als: "Doe het nu goed, niet snel." Een AI Act readiness-traject met gefaseerde aanpak past hier perfect bij.

**3. Agentic AI: de process layer is het product**
76% van bedrijven wil agents maar heeft de operationele infrastructuur niet. Ctac's kans is niet het model leveren, maar de implementatielaag: procesontwerp, data-governance, change management en monitoring. Dit is precies het consultancy-domein.

**4. Open-source frontier (GLM-5, Nemotron-3)**: Voor klanten met data-soevereiniteitseisen (overheid, zorg) zijn MIT-gelicenseerde frontier-modellen nu serieuze alternatieven voor Azure OpenAI. Emiel's team kan hier een concrete pilot rond opzetten.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Anthropic Mythos preview (7 april 2026)](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [TechCrunch – Is Anthropic limiting Mythos? (9 april 2026)](https://techcrunch.com/2026/04/09/is-anthropic-limiting-the-release-of-mythos-to-protect-the-internet-or-anthropic/)
- [Anthropic – Project Glasswing](https://www.anthropic.com/glasswing)
- [Hugging Face – GLM-5 review](https://huggingface.co/blog/mlabonne/glm-5)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [VentureBeat – NVIDIA Agent Toolkit launch](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Legal Nodes – EU AI Act 2026 compliance updates](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [Orrick – 6 stappen vóór 2 augustus 2026](https://www.orrick.com/en/Insights/2025/11/The-EU-AI-Act-6-Steps-to-Take-Before-2-August-2026)
- [NOS Nieuwsuur – AI in oorlogen](https://nos.nl/nieuwsuur/artikel/2609142-zorgen-over-gebruik-van-ai-in-oorlogen-menselijke-afweging-blijft-nodig)
- [The Hacker News – Flowise CVSS 10.0 RCE (april 2026)](https://thehackernews.com/2026/04/flowise-ai-agent-builder-under-active.html)
- [The Hacker News – LangChain/LangGraph flaws](https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html)
- [VentureBeat – Salesforce Agentforce groei](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000)
- [CIO Dive – Gartner AI spending 2026](https://www.ciodive.com/news/generative-agentic-ai-global-spending-forecast-gartner/809783/)
- [VentureBeat – Process layer voor agentic AI](https://venturebeat.com/orchestration/enterprise-agentic-ai-requires-a-process-layer-most-companies-havent-built)
- [Computable.nl – AI-hardwarecrisis 2026](https://www.computable.nl/persberichten/ai-hardwarecrisis-2026-wachten-op-chips-geen-optie-is-voor-eu-bedrijven/)
