---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-13
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 13 mei 2026

## 🔑 Highlights van de dag

- **Anthropic lanceert 'Mythos'** in beperkte kring: het krachtigste model tot nu toe, met cybersecurity-toepassingen — maar vanwege misbruikrisico's voorlopig alleen voor geselecteerde partners.
- **GLM-5.1** (open source, 754B parameters) versloeg Opus 4.6 en GPT-5.4 op SWE-Bench Pro — een significante benchmark voor coding-agents en een signaal dat open modellen frontiermodellen blijven bedreigen.
- **EU AI Act-amendementen** politiek akkoord bereikt op 7 mei: AI Office krijgt meer bevoegdheden, oversight van GPAI-modellen wordt gecentraliseerd, regulatory sandboxes breder toegankelijk.
- **Microsoft 365 E7 + Agent 365** algemeen beschikbaar sinds 1 mei: één controlevlak voor enterprise AI-agents à €15/gebruiker — al tientallen miljoenen agents geregistreerd in twee maanden.
- **Prompt injection** blijft systemisch risico: drie AI coding-agents lekten secrets via één aanval; Anthropic publiceerde voor het eerst concrete faalcijfers.

---

## 🧠 Technologie & Modellen

**Anthropic – 'Mythos' in beperkte preview**
Anthropic bracht deze week een nieuw topmodel uit onder de naam *Mythos*, exclusief beschikbaar voor een handvol partners. Het model heeft bijzondere capaciteiten op het gebied van cybersecurity. Vanwege het misbruikpotentieel heeft Anthropic bredere toegang geblokkeerd terwijl het samenwerkt met testpartners om risico's te kwantificeren. Dit is patroon dat we vaker zien: capability-first, safety-validatie loopt achter. Bron: [Anthropic News](https://www.anthropic.com/news)

**GLM-5.1 – open source slaat terug**
Chinese AI-lab THUDM lanceerde GLM-5.1 (754 miljard parameters, contextvenster van 202.752 tokens). Op SWE-Bench Pro — de benchmark voor softwareontwikkelingstaken — versloeg het zowel Opus 4.6 als GPT-5.4. Het model vermijdt het plateau-effect dat eerdere versies plagen. Dit is geen hype: open modellen naderen frontier-kwaliteit op coding, wat de prijsdruk op commerciële aanbieders vergroot. Bron: [VentureBeat](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4)

**Anthropic × Blackstone / Goldman Sachs**
Anthropic kondigde op 4 mei een nieuwe enterprise AI-dienstverleningsmaatschappij aan samen met Blackstone, Hellman & Friedman en Goldman Sachs. De run-rate omzet van Anthropic oversteeg inmiddels $30 miljard — een verdrievoudiging ten opzichte van eind 2025. Bron: [Anthropic News](https://www.anthropic.com/news)

---

## 🏛️ Governance & Ethiek

**EU AI Act-amendementen – politiek akkoord 7 mei**
De Europese Commissie en het Parlement bereikten vorige week een akkoord over aanpassingen aan de AI Act. De drie kernwijzigingen: (1) de AI Office krijgt versterkte handhavingsbevoegdheden en centraliseert toezicht op general-purpose AI-modellen; (2) vereenvoudigde compliance-regels worden uitgebreid naar 'small mid-cap' bedrijven; (3) regulatory sandboxes worden breder toegankelijk voor innovators, inclusief een EU-level sandbox. Ondersteuningsinstrumenten worden in Q2 2026 gepubliceerd — timing is relevant voor klanten die nu GPAI-systemen inzetten. Bron: [EU AI Act tracker](https://artificialintelligenceact.eu/) | [EC Digitale Strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Belgische Elle-affaire**
De Belgische editie van Elle gebruikte maandenlang AI-gegenereerde inhoud met verzonnen journalistennamen als byline. NOS berichtte hierover als voorbeeld van de sluipende normvervaging in mediabedrijven. Geen doorbraak, wel een waarschuwing voor klanten in de mediasector. Bron: [NOS](https://nos.nl/artikel/2572829-belgische-elle-werkte-stiekem-met-ai-boven-artikelen-stonden-nepjournalisten)

---

## 🔐 Security & Risk

**Prompt injection: drie coding-agents, één aanval**
Onderzoekers demonstreerden dat drie populaire AI coding-agents (niet nader benoemd in de publicatie) geheimen lekten via een enkele, zorgvuldig geformuleerde prompt injection. Opvallend: het system card van één van de getroffen vendors had dit risico expliciet voorspeld maar niet gemitigeerd. Bron: [VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)

**Microsoft Copilot Studio – CVE-2026-21520**
Capsule Security ontdekte een indirecte prompt injection (CVSS 7.5) in Copilot Studio; Microsoft patched op 15 januari, maar data werd alsnog geëxfiltreerd vóór de fix. Dit onderstreept dat patchen alleen onvoldoende is bij agent-architecturen. Bron: [VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)

**Anthropic publiceert prompt injection-faalcijfers**
Voor het eerst publiceert een AI-lab concrete failure rates voor prompt injection — een stap die de sector al lang vroeg. Dit maakt het mogelijk om security SLA's te formuleren en risico's kwantitatief af te wegen. Bron: [VentureBeat](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)

---

## 📈 Markt & Adoptie

**Microsoft 365 E7 + Agent 365 – GA sinds 1 mei**
Microsoft bundelde Microsoft 365 E5, Entra Suite en Copilot in een nieuw E7-pakket, met *Agent 365* als governance-laag voor AI-agents à $15/gebruiker/maand. In twee maanden tijd zijn er al tientallen miljoenen agents geregistreerd — een indicatie dat enterprise agent-adoptie in stroomversnelling raakt. Bron: [CIO Dive](https://www.ciodive.com/news/Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/) | [Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/)

**Google – Agentic Data Cloud**
Google lanceerde op Google Cloud Next '26 de *Agentic Data Cloud*: een AI-native architectuur die legacy enterprise dataplatforms omvormt tot redeneerplatforms. Vertex AI evolueert naar een volwaardig agent-platform. Microsoft en Google domineren nu onbetwist de enterprise AI-marktruimte. Bron: [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)

---

## 💡 Ctac-relevantie

**Agent 365 als onvermijdelijke keuze voor Microsoft-klanten.** De GA van Agent 365 betekent dat vrijwel elke Ctac-klant met Microsoft 365 nu een governance-laag voor AI-agents heeft — maar ook behoefte aan inrichting, beleid en training. Dit is een directe propositiekans: Ctac kan helpen bij de inrichting van agent-registries, toegangsbeleid en auditprocessen. Snel handelen loont hier.

**Prompt injection als boardroom-thema.** De combinatie van gepubliceerde faalcijfers (Anthropic), een nieuwe CVE bij Microsoft én een live demo van drie lekkende coding-agents maakt prompt injection vendorproof bespreekbaar. Klanten die nu coding-agents of RAG-systemen uitrollen, hebben behoefte aan een concrete security-baseline. Ctac kan hier met een gestandaardiseerde risicoassessment inspringen.

**EU AI Act sandbox-uitbreiding.** De bredere toegang tot regulatory sandboxes biedt kansen voor klanten die willen experimenteren met GPAI-toepassingen zonder direct aan alle high-risk vereisten te moeten voldoen. Voor sectoren als overheid en zorg is dit een relevant venster — en Ctac kan de rol van gids naar die sandbox op zich nemen.

**GLM-5.1 als open alternatief.** Voor klanten die om privacy- of kostenoverwegingen geen hyperscaler-modellen willen inzetten, wordt de open-source optie steeds reëler. Ctac-engineers dienen GLM-5.1 op het netvlies te hebben bij de volgende model-selectiediscussie.

---

## 📚 Bronnen & verder lezen

- [Anthropic News](https://www.anthropic.com/news)
- [VentureBeat – GLM-5.1 open source](https://venturebeat.com/technology/ai-joins-the-8-hour-work-day-as-glm-ships-5-1-open-source-llm-beating-opus-4)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [EC – AI Act implementatie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [NOS – Belgische Elle AI-affaire](https://nos.nl/artikel/2572829-belgische-elle-werkte-stiekem-met-ai-boven-artikelen-stonden-nepjournalisten)
- [VentureBeat – Prompt injection coding agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – Anthropic prompt injection faalcijfers](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)
- [VentureBeat – Microsoft Copilot Studio CVE-2026-21520](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [CIO Dive – Microsoft Agent 365 GA](https://www.ciodive.com/news/Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Microsoft Blog – Frontier Transformation](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/)
- [Computable – AI verandert ons leven](https://www.computable.nl/2026/05/12/ai-neemt-ons-leven-niet-over-maar-verandert-het-wel-ingrijpend/)
