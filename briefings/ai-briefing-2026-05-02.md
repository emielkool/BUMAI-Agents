---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-02
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2 mei 2026

## 🔑 Highlights van de dag

- **Microsoft 365 E7 en Agent 365 zijn gisteren (1 mei) algemeen beschikbaar geworden.** Voor €99/gebruiker bundelt Microsoft Copilot, E5-beveiliging en een centrale governance-laag voor AI-agenten. Dit is de grootste enterprise AI-herpositionering van Microsoft tot nu toe.
- **Prompt injection blijft de Achilleshiel van agentische AI.** Drie grote coding-agents (Claude Code, Gemini CLI, Copilot) werden gelijktijdig getroffen door een gecoördineerde prompt-injectie-aanval. OpenAI erkent officieel dat het probleem structureel niet volledig oplosbaar is.
- **EU AI Act: nog 93 dagen tot de volledige toepassingsdatum (2 augustus 2026).** De Europese Code of Practice voor het labelen van AI-gegenereerde content rondt haar consultatiefase af. Eerste geharmoniseerde standaard (prEN 18286) in publieke enquête.
- **DeepSeek V4-Pro en Qwen 3.6-27B** zijn beschikbaar op Hugging Face, beiden met 1 miljoen token context. Open-source frontier-kwaliteit blijft versnellen.
- **Microsoft telt ruim 20 miljoen betaalde Copilot-gebruikers** (bekendgemaakt op 29 april). Agentic AI gaat van pilot naar kerninfrastructuur.

---

## 🧠 Technologie & Modellen

**Microsoft lanceert 365 E7 + Agent 365 (GA: 1 mei)**
Microsoft bundelt Microsoft 365 E5, Copilot en de nieuwe Agent 365 in één SKU à $99/gebruiker/maand. Agent 365 ($15/gebruiker) fungeert als control plane voor alle AI-agenten in de organisatie: observability, governance en security in één dashboard. Wave 3 van M365 Copilot voegt agentische ervaringen toe aan Word, Excel, PowerPoint en Outlook. Dit is meer dan een product­launch — het is een positioneringsomslag: Microsoft presenteert zichzelf als de enterprise-governor van agentische AI.
*(Bron: [Microsoft Blog](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/), [VentureBeat](https://venturebeat.com/technology/microsoft-says-ungoverned-ai-agents-could-become-corporate-double-agents-its))*

**Open-source frontier: DeepSeek V4-Pro en Qwen 3.6**
DeepSeek V4-Pro (1,6 biljoen parameters, 49B actief via MoE, 1M token context) staat op Hugging Face en benadert frontier-modelprestaties op diverse benchmarks. Qwen 3.6-27B is de nieuwste open-gewichten release van Alibaba, gericht op stabiele productiviteits­toepassingen. De kloof tussen open-source en gesloten modellen blijft slinken.
*(Bron: [Hugging Face – DeepSeek V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro), [Hugging Face – Qwen3.6](https://huggingface.co/Qwen/Qwen3.6-27B))*

---

## 🏛️ Governance & Ethiek

**EU AI Act: eindsprint richting augustus 2026**
Op 2 augustus 2026 treedt het overgrote deel van de EU AI Act in werking. De Code of Practice voor het markeren van AI-gegenereerde content sluit haar werkgroepfase af; ondersteuningsinstrumenten voor compliance worden in Q2 2026 gepubliceerd. De eerste geharmoniseerde norm (prEN 18286 – kwaliteitsmanagement voor AI-systemen) doorloopt momenteel publieke consultatie. Organisaties die nog geen gap-analyse hebben gedaan, lopen achter.
*(Bron: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/), [EC Digitale Strategie](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content))*

**Nederland: overheid wil regie, maar mist strategie**
63% van de Nederlandse overheidsinstanties verkent AI-toepassingen actief, maar slechts een minderheid heeft een strategisch plan. De Nederlandse Digitale Dienst (coalitieakkoord 2026) moet de regie op data en AI bij de overheid versterken en externe IT-afhankelijkheid verminderen.
*(Bron: [Computable – Overheid360°](https://www.computable.nl/2026/04/09/overheid360-grip-houden-op-ai-data-en-digitale-autonomie-binnen-de-overheid/))*

---

## 🔐 Security & Risk

**Agentische AI: de beveiligingskloof is alarmant**
88% van de enterprises rapporteerde het afgelopen jaar een AI-agent-beveiligingsincident (VentureBeat-onderzoek). Toch heeft slechts 21% runtime-zichtbaarheid op het gedrag van hun agents, en slechts 6% van de security-budgetten adresseert dit risico expliciet. Een gecoördineerde prompt-injectie-aanval trof gelijktijdig Claude Code, Gemini CLI en Copilot — de aanval exploiteerde gedeelde bronnen (documenten, e-mails) waaruit agents context trekken.

OpenAI erkende officieel dat prompt injection "waarschijnlijk nooit volledig oplosbaar is". Anthropic publiceerde als eerste laboratorium concrete faalpercentages voor prompt-injectie in haar systeemkaarten — een stap naar meer transparantie die concurrenten nu onder druk zet om te volgen.
*(Bron: [VentureBeat – enforcement gap](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds), [VentureBeat – prompt injection agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))*

---

## 📈 Markt & Adoptie

**Microsoft: 20 miljoen betaalde Copilot-gebruikers**
Bekendgemaakt op 29 april: Microsoft overschreed de grens van 20 miljoen betaalde Copilot-gebruikers. Samen met de GA van E7 op 1 mei signaleert dit een versnelling van de enterprise AI-adoptie waarbij governance (Agent 365) nu meekomt als standaardonderdeel — niet meer een afterthought.
*(Bron: [TechCrunch](https://techcrunch.com/2026/04/29/microsoft-says-it-has-over-20m-paid-copilot-users-and-they-really-are-using-it/))*

**OpenAI Workspace Agents gaan 6 mei naar betaald model**
OpenAI's Workspace Agents — de opvolger van Custom GPTs voor enterprise — zijn gratis tot 6 mei, daarna credit-based. Ruim 30% van de Fortune 500 heeft inmiddels een geverifieerd account op Hugging Face.
*(Bron: [VentureBeat – Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more), [Hugging Face Blog](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026))*

---

## 💡 Ctac-relevantie

**Agent 365 als direct aanknopingspunt voor klantgesprekken.** De GA van Microsoft 365 E7 en Agent 365 op 1 mei is concreet verkoopbaar voor Ctac's Microsoft-praktijk: klanten die al E5 hebben, worden actief benaderd door Microsoft-partners. Ctac kan zich onderscheiden door Agent 365-governance-implementaties aan te bieden — inclusief het inrichten van observability en beleid rondom AI-agenten. Dit sluit direct aan op de beveiligingszorgen (88% incident-rate) die klanten nu voelen maar nog niet kunnen adresseren.

**Security-gap = propositiekans.** De combinatie van snel uitrollende agentische AI en een dramatisch onderbelicht beveiligingsbudget (6%) maakt AI-security-assessments tot een urgent en verkoop­baar aanbod. Ctac's AI-unit kan hier een snelle scan-aanpak ontwikkelen: welke agents draaien er, met welke rechten, en zijn ze auditeerbaar?

**EU AI Act: augustus komt snel.** Klanten in gereguleerde sectoren (overheid, zorg, finance) hebben minder dan 100 dagen. Een AI Act readiness-sprint — gap-analyse, risicoklassificatie, documentatieverplichtingen — is nu urgenter dan ooit en heeft een duidelijke deadline als haakje.

---

## 📚 Bronnen & verder lezen

- [Microsoft Blog – Frontier Suite (E7 aankondiging)](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)
- [Microsoft Blog – Partner Accelerator](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/)
- [VentureBeat – Agent 365 governance](https://venturebeat.com/technology/microsoft-says-ungoverned-ai-agents-could-become-corporate-double-agents-its)
- [TechCrunch – 20M Copilot users](https://techcrunch.com/2026/04/29/microsoft-says-it-has-over-20m-paid-copilot-users-and-they-really-are-using-it/)
- [VentureBeat – 88% AI agent incidents](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds)
- [VentureBeat – Prompt injection coding agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Code of Practice AI-gegenereerde content](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)
- [Computable – Overheid360° & digitale autonomie](https://www.computable.nl/2026/04/09/overheid360-grip-houden-op-ai-data-en-digitale-autonomie-binnen-de-overheid/)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Hugging Face – DeepSeek V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
