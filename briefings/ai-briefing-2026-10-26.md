---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-26
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 26 oktober 2026

## 🔑 Highlights van de dag

- **Claude Duet gelanceerd (21 okt):** Anthropic introduceerde een Research Preview van Claude Duet — een proactieve agent die zelfstandig op de achtergrond taken oppakt. Dit markeert een verschuiving van chatbot naar persistent werkende AI-collega.
- **Hyperscaler Q3-earnings deze week:** Alphabet, Microsoft en Amazon rapporteren hun kwartaalcijfers. De vraag: levert >$800 miljard aan AI-capex aantoonbaar rendement op? De uitkomst bepaalt mede hoe agressief de markt investeert in enterprise AI-tooling.
- **EU AI Office begint actief handhaven:** Op 14 oktober stuurde het AI Office formele Requests for Information aan grote AI-labs, gericht op veiligheid, externe evaluatie en gebruik van modellen. Geen boetes nog — maar de toon is gezet.
- **Belastingdienst verlaat Microsoft 365-cloud:** Vanwege spanning tussen de Amerikaanse CLOUD Act en de AVG stapt de Belastingdienst over naar eigen servers en open source — een signaalgeving die ook andere overheidsorganisaties raakt.
- **Supply chain-aanval op agentic AI (12 okt):** Nep-npm-pakketten leidden LLM-aanroepen om en registreerden een aanvallersmachine als MCP-server. Agentic tooling blijft een aantrekkelijk doelwit.

---

## 🧠 Technologie & Modellen

**Drie grote modelreleases in twee weken:**

- **Claude Duet (Research Preview, 21 okt):** Anthropic positioneert Claude nu als achtergrondagent die proactief taken oppakt, niet alleen reageert. Dit is een architectuurverschuiving, geen incrementele update.
- **GPT-6 Pro – Parallel Agents (16 okt):** OpenAI voegt parallelle agentmogelijkheden toe aan GPT-6. Gecombineerd met de overstap van GPT-6 als ChatGPT-standaard (8 okt) verschuift OpenAI expliciet naar multi-agent workflows.
- **Gemini 4 Argon (13 okt, breed beschikbaar):** Google heeft Gemini 4 Argon na een beperkte preview breed uitgerold. De modellen worden tegelijk via Google Cloud Model Garden aangeboden samen met OpenAI-modellen (aankondiging 21 okt) — een opmerkelijke toenadering.

**Benchmark-landschap:** In de wetenschappelijke literatuur domineren agentic benchmarks zoals DuMateBench, "Act As a Real Researcher" en XPerf (LLM serving performance). Opvallend: echte vergelijkende scores zijn schaars; labs publiceren liever eigen cijfers dan neutrale benchmarks. Wees kritisch op marketingclaims.

Bronnen: [LLM Stats](https://llm-stats.com/ai-news) · [Slash Digital](https://slash-digital.io/en/insights/ai-models-2026/) · [Buildez.ai](https://buildez.ai/blog/ai-new-model-explosion-october-2026-builders)

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving begonnen, boetes nog niet:**

Sinds 2 augustus 2026 zijn de handhavingsbevoegdheden van het EU AI Office en nationale toezichthouders actief. Op 14 oktober stuurde Executive Vice-President Virkkunen formele informatievragen naar AI-labs, gericht op veiligheid, externe evaluatie en gebruik. De consultatieronde voor de boeteprocedureverordening (gepubliceerd 12 okt) loopt nog — geen boetes dus, maar het raamwerk staat.

**Watermerk en transparantie:** OpenAI kondigt aan binnen weken een onzichtbaar watermerk in ChatGPT- en Codex-tekst te implementeren voor de EU-markt, als invulling van de AI Act-transparantieverplichtingen.

**Belastingdienst verlaat Microsoft 365:** De CLOUD Act-AVG-spanning wordt concreet: de Nederlandse Belastingdienst stapt over naar eigen servers en open source. Dit is een politiek signaal dat overheidsorganisaties serieus nadenken over digitale soevereiniteit.

**Anthropic herziet gebruiksbeleid (ingangsdatum 12 november):** Strengere regels voor wapens, surveillance, autonome hardware en misleidende campagnes. Relevant voor zakelijke gebruikers van Claude API.

Bronnen: [Digital Strategy EC](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act) · [Unite.ai](https://www.unite.ai/eu-announces-first-ai-act-enforcement-actions-after-ai-agent-incidents/) · [Hetlaatsteainieuws.nl](https://www.hetlaatsteainieuws.nl/) · [AI Act 2026 fines](https://aiconference.london/news/eu-ai-act-enforcement-begins-what-the-first-fines-will-look-like-20261013-07)

---

## 🔐 Security & Risk

**Kritieke kwetsbaarheden in agentic AI:**

- **DB-GPT (CVE-2026-77932, CVSS 9.3, 20 okt):** Een unauthenticated endpoint geeft aanvallers admin-rechten; prompt kan worden omgezet in aanvallersopdrachten.
- **Supply chain via nep-npm (12 okt):** Kwaadaardige npm-pakketten leidden agentic LLM-aanroepen om en registreerden een aanvaller-gecontroleerde MCP-server. Dit raakt direct de tooling die teams inzetten voor coding agents.
- **Indirect prompt injection via EchoLeak (Microsoft 365 Copilot):** Een zero-click kwetsbaarheid waarbij een vergiftigd e-mailbericht data kan exfiltreren via Copilot — zonder enige gebruikersinteractie.

**Structureel probleem:** Het LLM-contextvenster maakt geen architecturaal onderscheid tussen systeminstructies, gebruikersinput en externe data — de wortel van de meeste injection-aanvallen. Dat lost geen enkele patch op; het vereist een ontwerpverandering.

Bronnen: [Airia.com](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) · [GitHub incident timeline](https://github.com/webpro255/awesome-ai-agent-attacks) · [Cycode](https://cycode.com/blog/ai-security-vulnerabilities/)

---

## 📈 Markt & Adoptie

**Earnings-week is de lakmoesproef:** Alphabet, Microsoft en Amazon rapporteren deze week. Met meer dan $800 miljard aan verwacht hyperscaler AI-capex in 2026 verwacht de markt zichtbare productie-inzet, niet alleen pilots.

**Microsoft Copilot Studio domineert enterprise:** 160.000 organisaties met 400.000+ custom agents zijn de meest geciteerde cijfers. Azure staat op 79% in de Morgan Stanley CIO-survey (AWS 66%, Google Cloud 43%). Microsoft is vooralsnog de duidelijkste enterprise AI-speler.

**SAP lanceert 1.000 AI-agenten (19 okt, TechEd):** Direct beschikbaar voor S/4HANA Cloud en SuccessFactors. SAP sluit hiermee aan bij de trend dat ERP-leveranciers agentic AI als standaardfunctionaliteit positioneren, niet als add-on.

**OpenAI × Google Cloud:** OpenAI-modellen komen beschikbaar via Google Cloud Model Garden — een opvallend partnership dat de "hyperscaler rivaliteit" nuanceert en klanten keuzevrijheid geeft binnen bestaande cloudomgevingen.

Bronnen: [VentureBeat/af.net](https://af.net/realtime/enterprise-ai-adoption-surges-as-microsoft-salesforce-and-google-drive-innovation/) · [SAP TechEd](https://emergent.sh/news/sap-unveils-1-000-ai-agents-teched-2026) · [OpenAI × Google Cloud](https://www.ciol.com/news/openai-moves-into-googles-cloud-microsoft-remains-in-the-picture-12716687) · [Kai Waehner](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)

---

## 💡 Ctac-relevantie

**Agentic AI wordt de nieuwe standaard — positiebepaling is nu urgent.** Claude Duet, GPT-6 Parallel Agents en SAP's 1.000-agenten-lancering signaleren dat "agentic" van experiment naar product gaat. Voor Ctac betekent dit: klanten in de sectoren overheid, finance en industrie zullen binnen 3–6 maanden concrete agentic projectvragen hebben. De AI-unit moet nu al een standpunt innemen over hoe Ctac agenten bouwt, test en beveiligt — niet pas als de vraag binnenkomt.

**CLOUD Act vs. AVG is een kans voor overheidsklanten.** De Belastingdienst-stap laat zien dat publieke organisaties actief op zoek zijn naar alternatieven voor Amerikaanse cloud. Ctac kan hier met open source-positionering en eigen hosting een concrete propositie bouwen — dit is strategisch waardevoller dan nog een Microsoft-partnerschap uitbreiden.

**Security is geen afterthought meer bij AI-implementaties.** De supply chain-aanval via npm en de EchoLeak-kwetsbaarheid in Copilot laten zien dat agentic tooling een serieus aanvalsoppervlak is. Klanten die Ctac vragen om AI-implementaties zullen steeds vaker ook een security review verwachten. Investeer in kennis op dit vlak binnen de AI-unit, of werk samen met Ctac's security-competentie.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI News October 2026](https://llm-stats.com/ai-news)
- [EU AI Office enforcement framework](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [Unite.ai – First EU AI Act enforcement actions](https://www.unite.ai/eu-announces-first-ai-act-enforcement-actions-after-ai-agent-incidents/)
- [Airia – Prompt Injection in 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [GitHub – Awesome AI Agent Attacks timeline](https://github.com/webpro255/awesome-ai-agent-attacks)
- [SAP TechEd 2026 – 1.000 AI agents](https://emergent.sh/news/sap-unveils-1-000-ai-agents-teched-2026)
- [OpenAI × Google Cloud deal](https://www.ciol.com/news/openai-moves-into-googles-cloud-microsoft-remains-in-the-picture-12716687)
- [Hetlaatsteainieuws.nl – NL AI nieuws](https://www.hetlaatsteainieuws.nl/)
- [Buildez.ai – October 2026 model releases](https://buildez.ai/blog/ai-new-model-explosion-october-2026-builders)
- [Kai Waehner – Enterprise Agentic AI 2026](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)
