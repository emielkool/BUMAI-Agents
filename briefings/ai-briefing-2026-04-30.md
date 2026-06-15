---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-30
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 30 april 2026

## 🔑 Highlights van de dag

- **GLM-5.1 verslaat GPT-5.4 en Opus 4.6 op SWE-Bench Pro.** Z.ai lanceerde een open-source LLM met 754 miljard parameters dat op codeer-benchmarks de beste gesloten modellen overtreft – een signaal dat de open-source frontier sneller opschuift dan verwacht.
- **Google pompte tot $40 miljard in Anthropic.** De investering – $10 mrd direct, $30 mrd conditioneel – maakt duidelijk dat het hyperscaler-tijdperk van AI-laboratorium-partnerships is aangebroken. Anthropic's positie als "enterprise-veilig" alternatief wordt hierdoor verder versterkt.
- **Prompt injection: drie coding agents lekten secrets via één aanval.** Een praktijkonderzoek toonde aan dat AI coding agents als GitHub-actions gevoelig zijn voor indirecte prompt injectie, zelfs als de aanval via een externe pull request binnenkomt.
- **EU AI Act-deadline: augustus 2026 nadert snel.** Lidstaten moeten vóór 2 augustus minimaal één nationale AI-sandbox operationeel hebben; support-instrumenten vanuit de Commissie worden in Q2 2026 gepubliceerd.
- **NVIDIA lanceert enterprise AI agent platform met SAP, Salesforce en Adobe.** Met 17 launch-partners positioneert NVIDIA zich als de infrastructuurlaag voor geïntegreerde enterprise AI agents – een beweging die directe gevolgen heeft voor CRM- en ERP-trajecten bij Ctac-klanten.

## 🧠 Technologie & Modellen

**Z.ai – GLM-5.1 (754B parameters, open source)**
Z.ai – in januari 2026 naar de beurs gegaan met een marktwaarde van $52 mrd – publiceerde GLM-5.1. Het model behaalt 63,5 op Terminal-Bench 2.0 en 66,5 in combinatie met de Claude Code harness. Op SWE-Bench Pro scoort het hoger dan GPT-5.4 en Claude Opus 4.6. Dit is geen akademisch resultaat: het model is Apache-gelicenseerd en daarmee bruikbaar zonder licentiekosten. Open-source frontier-prestaties sluiten het gat met gesloten modellen sneller dan de meeste enterprise-roadmaps anticiperen.
Bron: [VentureBeat](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4)

**Anthropic – Mythos (beperkte preview)**
Anthropic bracht eerder deze maand Mythos uit in een beperkte partnerkring. Het model heeft significante cybersecurity-toepassingen maar is vanwege misbruikrisico's nog niet breed beschikbaar. Anthropic publiceerde tevens meetbare prompt-injection-faalpercentages – een zeldzame transparantiebeweging die andere aanbieders onder druk zet.
Bron: [TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)

**OpenAI – GPT-5.5**
Vorige week gelanceerd als het "slimste en meest intuïtieve" model van OpenAI tot nu toe, met hogere scores dan Gemini 3.1 Pro en Claude Opus 4.5 op de meeste benchmarks. De integratie in ChatGPT als "super app"-fundament wijst op verdere platformconsolidatie.
Bron: [TechCrunch](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/) | [OpenAI](https://openai.com/index/introducing-gpt-5-5/)

## 🏛️ Governance & Ethiek

De EU AI Act is op 1 augustus 2024 in werking getreden en wordt **volledig van kracht op 2 augustus 2026** – minder dan 100 dagen verwijderd. Organisaties die nog geen conformiteitsanalyse hebben gedaan voor hoog-risico toepassingen lopen nu aanzienlijk tijdrisico. De Europese Commissie publiceert in Q2 2026 richtlijnen voor hoog-risico classificatie, transparantievereisten en incidentrapportage. Elke lidstaat moet vóór augustus een nationale AI-sandbox operationeel hebben.

Relevant voor NL: docenten op middelbare scholen gebruiken AI voor het nakijken van open vragen; de EU-regelgeving die hier betrekking op heeft is uitgesteld tot volgend jaar, maar de maatschappelijke discussie loopt al.
Bron: [EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/) | [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines) | [NOS](https://nos.nl/artikel/2609282-docenten-kijken-na-met-ai-slimme-tijdsbesparing-of-risicovol)

## 🔐 Security & Risk

**Prompt injection blijft structureel probleem voor AI agents**
Praktijkonderzoek toonde aan dat drie populaire AI coding agents secrets lekten via één prompt injection aanval via een externe pull request. Microsoft's Copilot Studio kreeg een patch voor een bekende kwetsbaarheid – maar data was al geëxfiltreerd vóór de fix. OpenAI bevestigt dat "deterministische beveiligingsgaranties" bij browser-agents onmogelijk zijn zolang modellen vrije-tekst instructies accepteren. Het "Promptware Kill Chain"-framework van Schneier biedt een bruikbaar denkmodel voor risicoanalyse bij klantprojecten.
Bronnen: [VentureBeat – coding agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [VentureBeat – Copilot Studio](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook) | [Schneier](https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html)

## 📈 Markt & Adoptie

**Google en Microsoft domineren enterprise AI**
Microsoft leidt op enterprise-brede AI (sterk partner-ecosysteem), Google wint terrein op agentic AI-stacks. AWS behoudt de grootste cloud-marktaandeel (38% IaaS), maar loopt achter op AI-platform niveau.
Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

**NVIDIA – Enterprise AI Agent Platform**
Met Adobe, Salesforce en SAP als launch-partners lanceert NVIDIA een platform dat enterprise AI agents integreert op infrastructuurniveau. Dit raakt direct aan CRM- en ERP-implementaties.
Bron: [VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)

**Google – Agentic Data Cloud**
Google lanceerde een "Agentic Data Cloud" die legacy enterprise data-platforms omzet naar reasoning engines voor AI agents. Bedoeld als tegenwicht voor Microsofts Fabric-ecosysteem.
Bron: [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)

**Siemens – Autonome industriële AI-agent (NL/BE relevant)**
Siemens presenteerde een autonome industriële AI-agent die zelfstandig beslissingen neemt in productieomgevingen. Relevant voor Ctac-klanten in de maakindustrie.
Bron: [Computable.nl](https://www.computable.nl/2026/04/21/siemens-presenteert-autonome-industriele-ai-agent/)

## 💡 Ctac-relevantie

**Drie directe actiepunten voor Ctac:**

1. **EU AI Act compliance-dienstverlening.** Met de augustus-deadline minder dan 100 dagen weg zijn klanten in sectoren zoals overheid, zorg en finance nu actief op zoek naar partijen die helpen bij hoog-risico classificatie en conformiteitsanalyse. Dit is een concrete propositiekans voor Ctac die nú relevant is.

2. **AI-security als delivery-vereiste.** De prompt injection-incidenten bij coding agents en Copilot Studio maken duidelijk dat elke Ctac-levering waarbij AI agents externe inputs verwerken (PRs, e-mails, web) een expliciete beveiligingsscan vereist. Overweeg een standaard security checklist voor agentic AI projecten.

3. **NVIDIA-platform + SAP = enterprise kans.** Ctac's SAP-expertise maakt het bedrijf een logische partner om klanten te helpen bij de integratie van NVIDIA's agentic AI platform met bestaande SAP-omgevingen. Dit is een vroege positie die binnen 6–12 maanden commercieel relevant wordt.

## 📚 Bronnen & verder lezen

- [TechCrunch – Google investeert $40B in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [TechCrunch – OpenAI GPT-5.5](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)
- [OpenAI – Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [TechCrunch – Anthropic Mythos](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [VentureBeat – GLM-5.1 open source](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4)
- [EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act guidelines](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [VentureBeat – AI coding agents prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – Copilot Studio prompt injection](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [Schneier – Cybersecurity in the age of instant software](https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html)
- [CIO Dive – Microsoft & Google enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [VentureBeat – NVIDIA enterprise agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Computable.nl – Siemens industriële AI-agent](https://www.computable.nl/2026/04/21/siemens-presenteert-autonome-industriele-ai-agent/)
- [NOS – Docenten nakijken met AI](https://nos.nl/artikel/2609282-docenten-kijken-na-met-ai-slimme-tijdsbesparing-of-risicovol)
