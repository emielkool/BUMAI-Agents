---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-02
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2 november 2026

## 🔑 Highlights van de dag

- **Google Gemini 4 Carbon** is gelanceerd als gespecialiseerd cybersecurity-model voor het vinden en patchen van kwetsbaarheden – early access is beperkt tot geverifieerde verdedigers, wat de drempel bewust hoog houdt.
- **Apple Intelligence** rolt in China uit via Alibaba's Qwen-model; ontwikkelaarstests starten 4 november, publieke release volgt met iOS 27.3 in december. Dit is strategisch: Apple kiest lokale partners om regulatory en marktdrempels te omzeilen.
- **Prompt injection gaat operationeel**: de Cloud Security Alliance documenteert 12 live-exploitaties van indirect prompt injection tegen AI-agents, en Microsoft patchte een kritieke Semantic Kernel-kwetsbaarheid (CVE-2026-26030) waarbij injectie kon escaleren naar host-level RCE.
- **Anthropic** maakte een tijdelijke trainings­pauze bekend wegens veiligheids- en testproblemen – opvallend open communicatie, en bijzonder relevant gezien geruchten dat de IPO de week van 16 november zou plaatsvinden.
- **EU AI Act**: per 2 december 2026 gelden verboden op non-consensuele intieme beelden en CSAM via generatieve AI; generatieve systemen die vóór augustus 2026 op markt waren moeten dan ook machine-leesbare markering hebben.

---

## 🧠 Technologie & Modellen

**Google Gemini 4 Carbon** is beschikbaar als domeinspecifiek model voor offensieve en defensieve cyberbeveiliging, met early access uitsluitend voor vetted defenders. Dit is een interessante productpositionering: Google beperkt bewust het gebruik om misbruik te voorkomen, en positioneert het model als professioneel veiligheidsinstrument.
*(Bron: [Mind and Machine Weekly, 1 nov. 2026](https://mindandmachineweekly.substack.com/p/mind-and-machine-weekly-1-november))*

**OpenAI** zou werken aan GPT-6.1 Terra en GPT-6.2 Astra, waarbij 6.2 momenteel zo'n 20% van Codex-verkeer verwerkt. Beide zijn nog niet officieel aangekondigd – de meldingen komen uit aggregatordiensten en zijn niet bevestigd door OpenAI zelf. Wees kritisch: dit is pre-release geruchten­sfeer.
*(Bron: [The Neuron, 2 nov. 2026](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-november-2-2026/))*

**Agentic AI** is volwassen geworden: Prosus rapporteert dat agents met moderne modellen uren autonoom kunnen opereren. Multi-agent orkestratie (orchestrator + specialist-agents) wordt de standaard architectuur. Open-source agent OpenClaw (vroeger Clawdbot) heeft tractie gekregen en draait lokaal op browser, terminal en bestanden.
*(Bron: [Prosus – State of AI Agents 2026](https://www.prosus.com/news-insights/2026/state-of-ai-agents-2026-autonomy-is-here))*

---

## 🏛️ Governance & Ethiek

**EU AI Act – aankomende deadline**: per **2 december 2026** worden verboden van kracht rondom het genereren of manipuleren van non-consensuele intieme beelden en CSAM via AI. Generatieve systemen die vóór augustus 2026 al op de markt waren, moeten voor dezelfde datum machine-leesbare markering implementeren. Hoog-risico verplichtingen (Bijlage III) zijn via het Digital Omnibus-amendement (Vo. 2026/1744) uitgesteld naar december 2027 – dit geeft organisaties meer tijd, maar ook minder urgentiegevoel.
*(Bron: [EC – Enforcement AI Act](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act); [Alice Labs – EU AI Act Timeline 2026](https://alicelabs.ai/en/insights/eu-ai-act-timeline-2026))*

**Handhavingsactiviteit**: tot nu toe zijn alle 14 geregistreerde AI-gerelateerde handhavingsacties in de EU gebaseerd op bestaande wetgeving (voornamelijk GDPR), niet op de AI Act zelf. De AI-regelhandhaving is dus nog de facto op papier. Pas als GPAI-modellen en hoog-risico systemen écht worden doorgelicht verandert dat.
*(Bron: [Vorplabs – EU AI Enforcement Tracker 2026](https://vorplabs.com/ai-regulatory-updates/eu-enforcement))*

---

## 🔐 Security & Risk

**Prompt injection operationeel**: de Cloud Security Alliance meldt dat indirect prompt injection de fase van proof-of-concept voorbij is. Unit 42 documenteerde 12 live-exploitaties tegen AI-agents. OWASP heeft het voor het tweede jaar op rij als #1 LLM-kwetsbaarheid gerangschikt.

**Kritieke kwetsbaarheden in enterprise AI**:
- **CVE-2026-26030** (Microsoft Semantic Kernel): prompt injection kon escaleren naar host-level RCE. Microsoft heeft de kwetsbare functie verwijderd uit het bereik van het model.
- **EchoLeak** (Microsoft 365 Copilot): zero-click injectie kon enterprise-data stil exfiltreren.
- **Cursor IDE**: een chain van drie CVE's werd gedocumenteerd in 2026.

Conclusie: **MCP-koppelingen en agentic frameworks zijn het nieuwe aanvalsvlak**. Overmatige permissies en onveilige tool­verbindingen zijn het structurele risico, niet het model zelf.
*(Bronnen: [Vectra – Prompt injection](https://www.vectra.ai/topics/prompt-injection); [CSA – Indirect Prompt Injection in the Wild 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/); [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/))*

---

## 📈 Markt & Adoptie

**Microsoft vs. Google** in enterprise: Nadella claimt dat meer dan 90% van de Fortune 500 Microsoft 365 Copilot gebruikt; Google zegt dat bijna 90% van de Fortune 100 Gemini Enterprise inzet. Beide cijfers zijn topline-claims zonder breakdown van actieve gebruikersaantallen – behandel ze als marketingstatistieken.

**Prijsmodel**: Microsoft introduceert een hybride model met per-user licenties voor dagelijks gebruik en Copilot Credits (consumption-based) voor geavanceerde en agentische taken. Dit is een relevante koerswijziging voor enterprise budgettering.

**Saudi Aramco sluit overname HUMAIN af**: Saudi Aramco verwerft 49% van HUMAIN (AI-holdingmaatschappij), met PIF op 51%. Strategie­overwegingen: petrostaten investeren actief in nationale AI-capaciteit.

**Agenda november 2026**:
- Anthropic usage policy-wijziging: 12 november
- Mogelijke Anthropic IPO: week van 16 november
- **Microsoft Ignite**: 17–20 november (verwacht: Copilot-updates, Azure AI)
- **AWS re:Invent**: start 30 november

*(Bronnen: [CIO Dive – Microsoft, Google rule AI market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/); [AI Weekly – 2 nov. 2026](https://aiweekly.co/ai-news-today); [The Hans India – Upcoming AI Updates](https://www.thehansindia.com/tech/upcoming-ai-updates-in-november-2026-major-developments-to-watch-1137527))*

---

## 💡 Ctac-relevantie

**Agentic security is urgent.** Nu prompt injection operationeel wordt misbruikt in MCP-koppelingen en agent­frameworks, is dit voor Ctac direct relevant voor klanten die AI-agents uitrollen in productie. Security-by-design in agentic architecturen – inclusief permissie-scoping en tool-isolatie – is een propositie die Ctac nu kan positioneren bij klanten die Copilot of eigen agents uitrollen.

**EU AI Act december-deadline vraagt actie.** De 2 december deadline voor generatieve systemen (machine-leesbare markering) is concreet en nabij. Klanten in zorg, overheid en finance die generatieve AI-tools aanbieden aan eindgebruikers moeten dit nu op orde hebben. Dit is een quick-win voor Ctac als compliance-partner.

**Microsoft Ignite (17–20 november) verdient opvolging.** Verwacht: updates op Copilot-pricing, agentic capabilities en Azure AI governance. Relevant voor Ctac's Microsoft-partnerschap en de propositie richting enterprise­klanten die nu op de drempel staan van brede adoptie.

---

## 📚 Bronnen & verder lezen

- [AI Weekly – AI News Today, November 2](https://aiweekly.co/ai-news-today)
- [The Neuron – Everything That Happened in AI Today, November 2, 2026](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-monday-november-2-2026/)
- [Mind and Machine Weekly, 1 november 2026](https://mindandmachineweekly.substack.com/p/mind-and-machine-weekly-1-november)
- [The Hans India – Upcoming AI Updates in November 2026](https://www.thehansindia.com/tech/upcoming-ai-updates-in-november-2026-major-developments-to-watch-1137527)
- [AI News Roundup – 10 Developments to Watch (Nov 01 2026)](https://aialvin.substack.com/p/ai-news-roundup-10-developments-to-141)
- [EC – Enforcement AI Act](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [Alice Labs – EU AI Act Timeline 2026](https://alicelabs.ai/en/insights/eu-ai-act-timeline-2026)
- [Vorplabs – EU AI Enforcement Tracker 2026](https://vorplabs.com/ai-regulatory-updates/eu-enforcement)
- [CSA – Indirect Prompt Injection in the Wild 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/)
- [Microsoft Security Blog – RCE vulnerabilities in AI agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Vectra – Prompt Injection Types, CVEs, Enterprise Defenses](https://www.vectra.ai/topics/prompt-injection)
- [CIO Dive – Microsoft, Google rule AI vendor market for enterprises](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Prosus – State of AI Agents 2026](https://www.prosus.com/news-insights/2026/state-of-ai-agents-2026-autonomy-is-here)
- [LLM Stats – AI Updates Today (November 2026)](https://llm-stats.com/llm-updates)
