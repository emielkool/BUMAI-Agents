---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-21
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 21 juni 2026

## 🔑 Highlights van de dag

- **LiteLLM RCE actief misbruikt (CVSS 8.7):** CVE-2026-42271 wordt gecombineerd met een Starlette host-header bypass om zonder authenticatie remote code uit te voeren op AI-gatewayservers; elke organisatie die LiteLLM als proxy draait is direct kwetsbaar als men nog niet op v1.83.14-stable zit.
- **EU AI Act: nog 6 weken:** Op 2 augustus 2026 wordt de AI Act volledig van toepassing. De transparantieverplichtingen (o.a. labeling van AI-gegenereerde content) treden dan in werking; veel bedrijven blijken nog onvoldoende voorbereid.
- **Nobel-laureaat John Jumper verlaat DeepMind voor Anthropic:** De architect achter AlphaFold, die in 2024 de Nobelprijs scheikunde ontving, stapt over naar Anthropic. Dit signaleert een versnellende talent-race waarbij toppublicisten nu actief worden weggekocht bij Big Tech.
- **Microsoft Work IQ APIs nu GA:** Sinds 16 juni zijn de Work IQ APIs algemeen beschikbaar. Ze geven agentische applicaties toegang tot de volledige organisatiecontext van Microsoft 365 (e-mail, meetings, documenten, mensen), wat enterprise AI-agenten structureel bruikbaarder maakt.
- **Agentic AI: kantelmoment bevestigd:** Gartner projecteert dat 40% van enterprise-applicaties einde 2026 task-specifieke AI-agents bevat, vergeleken met minder dan 5% in 2025. MCP is nu met 10.000+ gepubliceerde servers de facto standaard voor agent-toolintegratie.

---

## 🧠 Technologie & Modellen

**John Jumper (Nobel, AlphaFold) naar Anthropic**
Gisteren bevestigde John Jumper zijn overstap na bijna negen jaar bij Google DeepMind. Hij was de lead van het AlphaFold-team en later betrokken bij Google's coding-tools. Zijn overstap volgt op Character AI-medeoprichter Noam Shazeer die eerder deze week overstapte naar OpenAI. De talentmigratie richting Anthropic en OpenAI suggereert dat beide labs sneller bewegen dan de Big Tech-labs op fundamenteel modelonderzoek.
*(Bron: [TechCrunch, 20 juni 2026](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/))*

**Google Gemini 3.5 Flash & Antigravity-platform**
Google introduceerde Gemini 3.5 Flash als hun eerste model dat "frontier intelligentie combineert met actie." Het model is beschikbaar via Antigravity, een nieuw agent-first development platform dat direct koppelt aan Google Cloud en Workspace (Sheets, Drive, Docs). Relevant voor bedrijven die Google Workspace en cloud al als primaire stack hebben.

**MCP bereikt 10.000+ servers**
Het Model Context Protocol, in 2025 gestandaardiseerd na de DeepSeek-periode, is geïntegreerd in ChatGPT, Cursor, Gemini, Microsoft Copilot en VS Code. De explosieve adoptie maakt agent-toolintegratie steeds commodityachtig — dit is infrastructuur, geen onderscheidend vermogen meer.

---

## 🏛️ Governance & Ethiek

**EU AI Act – T-minus 6 weken**
Op 2 augustus 2026 treedt het volledige toepassingsbereik van de AI Act in werking, inclusief transparantieverplichtingen rondom AI-gegenereerde content (artikel 50). De "AI omnibus" die in mei 2026 een politiek akkoord bereikte, vereenvoudigt enkele regels, maar de kernverplichtingen voor high-risk systemen en GPAI-modellen staan vast. Veel lidstaten hebben de deadline voor nationale toezichthouders (augustus 2025) gemist — implementatie loopt vertraagd.
*(Bron: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/), [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))*

**Vlam: Nederlandse overheids-AI richting landelijke uitrol**
Het Nederlands rijksoverheid chatplatform Vlam, een sovereign alternatief voor commerciële generatieve AI-diensten, bereidt een brede productiepilot voor in de tweede helft van 2026, na afronding van risico-analyses en beveiligingsprocedures. Dit versterkt de trend van overheidsinstellingen die soevereine AI-alternatieven opbouwen naast Microsoft/Google-diensten.
*(Bron: [Computable.nl, 10 juni 2026](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/))*

---

## 🔐 Security & Risk

**LiteLLM CVE-2026-42271 actief misbruikt – RCE zonder authenticatie**
Horizon3.ai heeft aangetoond dat CVE-2026-42271 (command injection, CVSS 8.7) gecombineerd kan worden met CVE-2026-48710 (Starlette BadHost bypass) om volledig zonder authenticatie code te draaien op LiteLLM-gateway servers. Succesvolle exploitatie geeft toegang tot alle provider-API-sleutels, opgeslagen secrets, en alle prompts en responses die door de proxy gaan. BerriAI heeft de volledige fix in v1.83.14-stable uitgebracht (2 mei), maar organisaties die dit nog niet bijgewerkt hebben lopen acuut risico.

Dit is bijzonder relevant voor organisaties die LiteLLM gebruiken als multi-provider AI-gateway in hun interne AI-infrastructuur — een gangbare architectuurkeuze. Urgentie: hoog.
*(Bron: [The Hacker News – LiteLLM kwetsbaarheidsoverzicht](https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html), [VentureBeat](https://venturebeat.com/security/copilot-searched-your-mailbox-litellm-handed-out-admin))*

**Shadow AI en autonome agents: risico groeit**
Gartner en andere analisten waarschuwen dat de inzet van autonome multi-agent systemen nieuwe, moeilijk zichtbare aanvalsvectoren creëert. Agents die cross-platform opereren (Outlook, Teams, CRM, ERP) zonder expliciete audittrail vormen een snel groeiend risico voor datalekken en credential-diefstal.

---

## 📈 Markt & Adoptie

**Microsoft Work IQ APIs – GA 16 juni**
Microsoft's Work IQ APIs zijn nu algemeen beschikbaar en geven agentische applicaties context over de volledige Microsoft 365-omgeving. Samen met het bredere IQ-platform (Fabric IQ voor data, Foundry IQ voor enterprise knowledge, Web IQ voor live-web grounding) vormt dit de infrastructuur waarop Microsoft Copilot Studio-agents en externe agentische applicaties gebouwd worden. Microsoft Scout, een persoonlijke werkagent op basis van dit platform, is direct beschikbaar.
*(Bron: [Microsoft Blog, Build 2026](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/), [VentureBeat](https://venturebeat.com/data/enterprise-ai-agents-keep-creating-data-silos-microsofts-build-answer-is-microsoft-iq-and-rayfin))*

**Gartner: agentische AI kantelmoment 2026**
40% van enterprise-applicaties zal einde 2026 task-specifieke AI-agents bevatten (vs. <5% in 2025). Zowel Forrester als Gartner benoemen 2026 als doorbraakjaar voor multi-agent systemen. In de praktijk betekent dit dat veel organisaties nu snel van proof-of-concept naar productie moeten, met alle governance- en security-uitdagingen die daarbij horen.
*(Bron: [Gartner/Joget analyse](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/), [Prosus State of AI Agents](https://www.prosus.com/news-insights/2026/state-of-ai-agents-2026-autonomy-is-here))*

---

## 💡 Ctac-relevantie

**1. LiteLLM-check voor klanten: actiepunt deze week**
Verschillende Ctac-klanten zetten LiteLLM in als AI-gateway. Gezien de actief misbruikte RCE-kwetsbaarheid is een gerichte advisory aan betreffende klanten op zijn plaats: controleer de versie, update naar v1.83.14-stable, en audit de API-sleutels die via de proxy lopen.

**2. EU AI Act-deadline: positioneer Ctac als compliance-partner**
Met 6 weken tot volledige toepasselijkheid zijn veel Nederlandse middelgrote en grote bedrijven nog niet compliant, met name op transparantieverplichtingen. Ctac kan hier proactief diensten aanbieden rond AI-audit, risicoklassificatie en technische implementatie van artikel 50-verplichtingen. Dit is een concreet en tijdgebonden propositie-moment.

**3. Microsoft IQ-platform: kansen in Copilot Studio-trajecten**
De GA van Work IQ APIs maakt multi-agent workflows in de Microsoft-stack aanzienlijk waardevoller. Voor klanten die al in Microsoft 365 en Azure zitten, is dit het moment om Copilot Studio-implementaties te verdiepen richting agentische toepassingen — een gebied waar Ctac nu expertise kan opbouwen of versnellen.

**4. Talent en positionering in de markt**
De overstap van topwetenschappers (Jumper, Shazeer) naar frontier labs signaleert dat het beste AI-talent zich concentreert bij Anthropic en OpenAI. Ctac hoeft hier niet mee te concurreren, maar dit benadrukt het belang van snelle adoptie van de nieuwste modellen via API's, in plaats van te investeren in eigen modelontwikkeling.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – John Jumper leaves DeepMind for Anthropic (20 juni 2026)](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/)
- [The Hacker News – LiteLLM Vulnerability Chain (juni 2026)](https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html)
- [The Hacker News – LiteLLM CVE-2026-42271 Exploited in the Wild](https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html)
- [VentureBeat – Copilot mailbox / LiteLLM admin keys audit](https://venturebeat.com/security/copilot-searched-your-mailbox-litellm-handed-out-admin)
- [EU AI Act – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC Digital Strategy – AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Microsoft Blog – Build 2026 Work IQ](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [VentureBeat – Microsoft IQ & Rayfin](https://venturebeat.com/data/enterprise-ai-agents-keep-creating-data-silos-microsofts-build-answer-is-microsoft-iq-and-rayfin)
- [Computable.nl – Vlam rijksambtenaren AI (10 juni 2026)](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/)
- [Gartner/Joget – AI Agent Adoption 2026](https://joget.com/ai-agent-adoption-in-2026-what-the-analysts-data-shows/)
- [Prosus – State of AI Agents 2026](https://www.prosus.com/news-insights/2026/state-of-ai-agents-2026-autonomy-is-here)
- [Google I/O 2026 – alle aankondigingen](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
