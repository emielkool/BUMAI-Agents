---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-25
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 25 april 2026

## 🔑 Highlights van de dag

- **GPT-5.5 is live** – OpenAI lanceerde gisteren GPT-5.5 (en Pro-variant) via de API; sterk op agentic coding en computer use, beschikbaar voor Plus/Pro/Business/Enterprise.
- **Google pompt $40 mrd in Anthropic** – Alphabet verhoogt zijn inzet enorm: $10 mrd direct + $30 mrd prestatiegebonden, bij een waardering van $800 mrd+. IPO mogelijk al in oktober.
- **Microsoft 365 E7 op 1 mei** – De "Frontier Suite" (Copilot + Agent 365 + Entra) is vanaf volgende week GA. De enterprise-markt versnelt van pilot naar agent-productie.
- **EU AI Act: ~99 dagen tot high-risk deadline** – Op 2 augustus 2026 worden de regels voor high-risk AI volledig van kracht. Normen van CEN/CENELEC zijn nog niet klaar, wat compliance-onzekerheid vergroot.
- **Prompt injection blijft structureel gevaar** – Drie coding agents lekten credentials via één prompt injection; Microsoft Copilot Studio had een CVSS 7.5-kwetsbaarheid (CVE-2026-21520) waarbij data ondanks patching werd geëxfiltreerd.

## 🧠 Technologie & Modellen

**OpenAI GPT-5.5** (24 april)
OpenAI lanceerde GPT-5.5 en GPT-5.5 Pro via de API en ChatGPT. Het model excelleert in agentic coding, computer use, web research en data-analyse. Agentic tools als Codex zijn 5× gegroeid in gebruik ten opzichte van begin 2026. GPT-5.5 markeert een verschuiving: AI werkt niet meer als copilot naast de gebruiker, maar als agent-team dat zelfstandig taken afrondt.
*(Bron: [OpenAI – Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/))*

**ChatGPT Images 2.0** (21 april)
Het nieuwe image-model heeft "thinking capabilities": web-search tijdens generatie, meerdere iteraties vanuit één prompt en accurate tekstweergave in afbeeldingen. Productierijp voor menu's, infographics en marketing.
*(Bron: [TechCrunch](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/))*

**Google investeert tot $40 mrd in Anthropic** (24 april)
De deal heeft meerdere lagen: Google koopt strategische positie én compute-aankoop ($5 GW capaciteit over tijd). Amazon deed eerder deze maand al $5 mrd. Samen richting $100 mrd aan kapitaal – ongekend voor een AI-lab. Anthropic overweegt een IPO in oktober. Strategisch: Google investeert in zijn directe concurrent, maar waarborgt zo ook zijn eigen infrastructuurpositie.
*(Bron: [TechCrunch](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/))*

## 🏛️ Governance & Ethiek

**EU AI Act: 99 dagen tot volledige handhaving**
Op 2 augustus 2026 worden de high-risk regels van de AI Act van kracht. Probleem: CEN en CENELEC hebben de harmonisatienormen niet op tijd afgerond, waardoor organisaties die CE-markering nastreven voor high-risk systemen momenteel in een normatief vacuüm opereren. De Europese Commissie werkt aan aanvullende richtlijnen voor risico-classificatie en incidentrapportage, maar timing is onzeker.

Wachten op normen is geen strategie: organisaties die nu niet beginnen met inventarisatie, missen de boot.
*(Bron: [EU AI Act – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/), [European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))*

## 🔐 Security & Risk

**Prompt injection: structureel en ernstig**
Drie AI coding agents lekten credentials via een enkele prompt injection — bij één waarschuwde het eigen system card van de vendor al voor dit risico. Microsoft patchte CVE-2026-21520 (CVSS 7.5) in Copilot Studio, maar data werd alsnog geëxfiltreerd voordat de patch volledig was uitgerold. Anthropic publiceerde als eerste vendor kwantitatieve faalpercentages voor prompt injection — ontnuchterend maar nuttig als meetlat voor de sector.

De EU AI Act August-deadline dwingt nu al procurement-teams om vendors te vragen naar *aantoonbare* injection-resistentie. Leveranciers zonder cijfers worden een compliance-risico.
*(Bron: [VentureBeat – AI agent prompt injection exploit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026), [VentureBeat – Copilot Studio CVE-2026-21520](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))*

## 📈 Markt & Adoptie

**Microsoft 365 E7 – The Frontier Suite (GA: 1 mei)**
Microsoft bundelt Copilot, Agent 365 en Entra Suite in een nieuw enterprise-tier. De boodschap: van copilot naar agent-orkestrator, van pilot naar productie. CIO Dive bevestigt dat Microsoft en Google de enterprise AI-markt domineren — Microsoft breed op platform en partner, Google specifiek sterk in agentic AI.
*(Bron: [Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/), [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))*

**Google Agentic Data Cloud**
Google lanceerde op Google Cloud Next '26 de "Agentic Data Cloud": een AI-native data-architectuur die legacy enterprise dataplatforms omzet in reasoning engines voor AI agents. Directe concurrent van Microsoft Fabric + Copilot-stack, en relevant voor Ctac-klanten met complexe datapijplijnen.
*(Bron: [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))*

## 💡 Ctac-relevantie

**Drie directe aandachtspunten voor de AI-unit:**

1. **Agent 365 GA (1 mei)** – De vraag naar agent-implementatie bij Microsoft-klanten versnelt nu concreet. Ctac moet vóór de zomer helder hebben welke agent-configuraties, governance-frameworks en beheermodellen het kan leveren. Dit is geen product van de toekomst — dit is de vraag van volgende maand.

2. **EU AI Act compliance als propositie** – De combinatie van de naderende August-deadline en ontbrekende normen creëert urgente vraag naar pragmatische begeleiding. Een Ctac quick-scan dienst — inventarisatie van AI-portfolio's op high-risk classificatie, plus roadmap naar compliance — is direct verkoopbaar aan klanten in zorg, overheid en finance.

3. **Prompt injection security review** – Klanten die Copilot Studio of vergelijkbare tools inzetten hebben nu een concrete CVE op tafel. Ctac kan security-reviews aanbieden die specifiek kijken naar prompt injection risico's in productiesystemen. Dit sluit aan bij de bestaande securitypropositie en positioneert Ctac als verantwoorde AI-partner.

## 📚 Bronnen & verder lezen

- [OpenAI – Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [TechCrunch – ChatGPT Images 2.0](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/)
- [TechCrunch – Google investeert $40B in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [TechCrunch – Anthropic compute deal Google & Broadcom](https://techcrunch.com/2026/04/07/anthropic-compute-deal-google-broadcom-tpus/)
- [TechCrunch – OpenAI Agents SDK update](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/)
- [EU AI Act – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [European Commission – AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [VentureBeat – AI agent prompt injection exploit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – Microsoft Copilot Studio CVE-2026-21520](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [Microsoft Blog – Accelerating Frontier Transformation](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/)
- [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
