---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-05
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 5 mei 2026

## 🔑 Highlights van de dag

- **Microsoft 365 E7 & Agent 365 live:** Microsoft maakte per 1 mei de general availability bekend van Microsoft 365 E7 en het bijbehorende Agent 365-platform – één unified control plane voor AI-agents in de enterprise. Direct relevant voor Ctac's Microsoft-klanten.
- **EU AI Act high-risk deadline dreigt te verschuiven:** Een politiek triloog op 13 mei 2026 bespreekt het Digital Omnibus-voorstel dat de compliance-deadline voor high-risk AI-systemen uitstelt van 2 augustus 2026 naar december 2027. Ademruimte voor bedrijven, maar ook risico op strategische vertraging.
- **Prompt injection: CVSS 9.6 in GitHub Copilot:** CVE-2025-53773 laat zien dat verborgen prompt injection in pull request-beschrijvingen remote code execution mogelijk maakte via GitHub Copilot. Eerder dit kwartaal meldde Unit 42 de eerste grootschalige indirecte prompt injection-aanvallen in productieomgevingen.
- **Open-source sluit kloof met closed-source:** Kimi K2.6 van Moonshot AI leidt momenteel het open-weight leaderboard (GPQA: 90,5%), naast DeepSeek V4 en Qwen 3.6 Plus. Open-weight modellen draaien inmiddels in echte engineering-pipelines.
- **Shadow AI Nederland alarmerend:** 46,8% van de Nederlandse medewerkers gebruikt AI-tools zonder dit te melden – ondanks het feit dat 97% van de bedrijven een AI-policy heeft. Governance-gap is groot.

---

## 🧠 Technologie & Modellen

De grote labs publiceerden recent een reeks significante releases. **OpenAI's GPT-5.5** (uitgebracht 24 april) richt zich op agentic coding, computer use en diepere onderzoekstaken – beschikbaar voor Plus, Pro, Business en Enterprise. **Anthropic's Claude Opus 4.7** (16 april) positioneert zich als het meest beheerste en veiligste generally available model: beter in instructie-opvolging en software engineering. **Google's Gemini 3.1 Ultra** brengt een 2-miljoen-token contextvenster en native multimodaliteit (tekst, beeld, audio, video).

In open-source domineert **Kimi K2.6** de leaderboards voor agentic coding. De trend is duidelijk: het verschil in kwaliteit tussen open-weight en closed-source modellen is verwaarloosbaar geworden voor veel enterprise use cases.

*Bronnen: [CNBC – Claude Opus 4.7](https://www.cnbc.com/2026/04/16/anthropic-claude-opus-4-7-model-mythos.html) | [CNBC – GPT-5.5](https://www.cnbc.com/2026/04/23/openai-announces-latest-artificial-intelligence-model.html) | [Bloomberg – Google AI Agents](https://www.bloomberg.com/news/articles/2026-04-22/google-releases-new-ai-agents-to-challenge-openai-and-anthropic) | [llm-stats.com](https://llm-stats.com/ai-news)*

---

## 🏛️ Governance & Ethiek

De **EU AI Act** nadert een kritiek moment. Op **13 mei 2026** vindt een politieke triloog plaats over het Digital Omnibus-voorstel, dat de compliance-deadline voor high-risk AI-systemen wil verschuiven van 2 augustus 2026 naar **2 december 2027**. Als dit doorgaat, krijgen bedrijven 16 maanden extra – maar het risico bestaat dat investeringen in compliance worden uitgesteld. Slechts 8 van de 27 EU-lidstaten hebben hun nationale contactpunten aangemeld.

In Nederland stagneren AI-adoptieambities deels door **ontbrekend overheidsbeleid** (57% van bedrijven noemt dit als grootste obstakel), gebrekkige compute-infrastructuur (43%) en beperkte private sectorparticipatie. Het is geen technisch maar een governance-probleem.

*Bronnen: [DLA Piper – Digital AI Omnibus](https://knowledge.dlapiper.com/dlapikerknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) | [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) | [ICT Magazine – AI-adoptie Benelux](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)*

---

## 🔐 Security & Risk

**Prompt injection is de #1 AI-dreiging van 2026** – en de ernst wordt steeds concreter. CVE-2025-53773 toonde aan dat verborgen instructies in GitHub Copilot pull requests remote code execution mogelijk maakten (CVSS 9.6). Unit 42 (Palo Alto Networks) documenteerde in maart 2026 de eerste grootschalige indirecte prompt injection-aanvallen in het wild: ad review-evasie en system prompt leakage op commerciële platforms.

Het volume aan kwaadaardige prompt injection-incidenten steeg met **32%** tussen november 2025 en februari 2026. Aanvallers combineren technieken tot ketens: AI-gegenereerde phishing, social engineering en prompt injection werken samen als compound exploit. Het UK NCSC stelde al dat prompt injection "mogelijk nooit volledig opgelost wordt" omdat het fundamenteel is aan hoe LLMs taal interpreteren.

*Bronnen: [Airia – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) | [Google Security Blog – Prompt Injections](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html) | [Cisco State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)*

---

## 📈 Markt & Adoptie

**Microsoft** lanceerde op 1 mei **Microsoft 365 E7** en **Agent 365** – het centrale control plane voor enterprise AI-agents, gecombineerd met Entra Suite en Microsoft 365 Copilot. Tegelijk introduceerde Microsoft **Intelligent Purview**: realtime DLP die AI-prompts en -responses scant op gevoelige informatie (creditcardnummers, IP-gevoelig materiaal). Praktisch en compliance-relevant voor enterprise-klanten.

**Google** consolideerde met de **Gemini Enterprise Agent Platform** (opvolger van Vertex AI) en **Agentic Data Cloud** – een volledig ecosysteem voor het bouwen, schalen en beheren van AI-agents. Betaalde Gemini Enterprise-gebruikers groeiden 40% kwartaal-op-kwartaal; meerdere deals van $1 miljard+.

**Nederland** scoort opvallend goed: AI-adoptie steeg van 34% (2023) naar **67% (2026)**, #4 in Europa en #9 wereldwijd. Maar de shadow AI-kloof is groot: bijna de helft van de medewerkers gebruikt AI zonder dit te melden.

*Bronnen: [Microsoft Blog – Frontier Transformation](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/) | [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/) | [Fortune – AI Capex](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/) | [Searchlab – AI Adoptie NL](https://searchlab.nl/blog/ai-adoptie-nederland-2026)*

---

## 💡 Ctac-relevantie

**Microsoft 365 E7 + Agent 365** is de directe aanleiding voor een gesprek met Ctac's Microsoft-klanten: welke agents willen ze bouwen, wie beheert ze, en hoe regelen ze governance? Dit is een concreet propositiemoment voor Ctac's AI-unit.

De **shadow AI-problematiek** (46,8% ongemeld gebruik) is een kans voor Ctac om governance-diensten te positioneren: AI-policy frameworks, tooling-inventarisatie en adoptietrajecten. Klanten *hebben* beleid, maar het werkt niet – daar zit de waarde.

De **prompt injection-dreiging** (CVSS 9.6 in Copilot) is urgent voor elke klant die Microsoft 365 Copilot of andere LLM-integraties heeft. Ctac kan hier als trusted advisor optreden met een security-review aanbod specifiek voor AI-integraties.

Het **EU AI Act uitstelscenario** vraagt om een pragmatische aanpak: communiceer aan klanten dat uitstel van de deadline niet betekent dat governance-werk kan wachten. De deadline voor GPAI-handhaving (2 augustus 2026) staat gewoon.

---

## 📚 Bronnen & verder lezen

- [CNBC – Anthropic Claude Opus 4.7](https://www.cnbc.com/2026/04/16/anthropic-claude-opus-4-7-model-mythos.html)
- [CNBC – OpenAI GPT-5.5](https://www.cnbc.com/2026/04/23/openai-announces-latest-artificial-intelligence-model.html)
- [Bloomberg – Google releases AI Agents](https://www.bloomberg.com/news/articles/2026-04-22/google-releases-new-ai-agents-to-challenge-openai-and-anthropic)
- [TechCrunch – Google investeert $40B in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [DLA Piper – Digital AI Omnibus (uitstel high-risk deadline)](https://knowledge.dlapiper.com/dlapikerknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [artificialintelligenceact.eu – handhaving EU AI Act](https://artificialintelligenceact.eu/)
- [Google Security Blog – Prompt Injections in the wild](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html)
- [Airia – AI Security 2026: Prompt Injection & the Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Cisco – State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)
- [Microsoft Blog – Frontier Transformation met partners](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Fortune – Microsoft/Meta/Google AI capex](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/)
- [ICT Magazine – AI-adoptie Benelux](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)
- [Searchlab – AI Adoptie Nederland 2026](https://searchlab.nl/blog/ai-adoptie-nederland-2026)
- [llm-stats.com – Open LLM Leaderboard](https://llm-stats.com/leaderboards/open-llm-leaderboard)
