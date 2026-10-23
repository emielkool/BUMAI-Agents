---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-17
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 17 juli 2026

## 🔑 Highlights van de dag

- **Google lanceert Gemini 3.5 Pro vandaag** – 2M-token context en 4× lagere inputkosten dan GPT-5.6; een directe aanval op OpenAI's enterprise-dominantie en een nieuw cost-per-token ijkpunt voor de markt.
- **WAIC 2026 Shanghai opent** – Xi Jinping verschijnt voor het eerst persoonlijk op de World AI Conference; een geopolitiek signaal over China's strategische AI-ambitie.
- **EU AI Act: nog 16 dagen tot volledige werking** – per 2 augustus 2026 zijn alle regels afdwingbaar; voor Ctac-klanten in high-risk sectoren is dit een harde deadline die nú aandacht vereist.
- **Microsoft Frontier Company gelanceerd ($2,5 mrd)** – een aparte deployment-tak met 6.000 experts; implementatiesucces is de nieuwe battleground, niet modelkeuze.
- **Drie AI coding agents lekten secrets via één prompt injection** – kritische waarschuwing voor enterprise AI-implementaties in CI/CD-omgevingen.

## 🧠 Technologie & Modellen

**Google Gemini 3.5 Pro – vandaag algemeen beschikbaar**
Google DeepMind maakt Gemini 3.5 Pro vandaag (17 juli) GA. Kernspecificaties: volledig nieuwe pretraining, **2-miljoen-token contextvenster** (dubbel t.o.v. huidige frontier), en een Deep Think redeneermode achter het $250/maand Ultra-abonnement. Verwachte API-prijs: ~$1,25 input / $10 output per miljoen tokens – 4× goedkoper op input dan GPT-5.6 Sol. Dit verandert de cost-per-token berekening voor grootschalige enterprise-toepassingen fundamenteel en geeft inkopers nieuwe leverage bij contractonderhandelingen.

**Moonshot Kimi K3 – China's grootste open-weight model**
Moonshot AI's Kimi K3 staat op het punt van release: 2–3 biljoen parameters, het grootste open-weight model ooit vanuit China. Verwacht prestatie-niveau: gelijkwaardig aan of beter dan Anthropic Opus 4.8. Open-weight bij deze schaal verandert de dynamiek in het open-source landschap dramatisch en verlaagt de drempel voor sovereign AI-deployments buiten de grote cloud-providers. ([TechCrunch, 16 juli](https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/))

**OpenAI GPT-5.6-familie**
OpenAI lanceerde eerder deze maand drie varianten: Sol (productie-workhorse, 54% tokenefficiënter voor coding), Terra (midrange) en Luna (budget). Samen met Gemini 3.5 Pro geeft dit enterprise-klanten aanzienlijk meer prijsdruk-leverage – iets wat iedere AI-propositie waarbij rekenkosten doorbelast worden direct raakt. ([TechCrunch, 9 juli](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/))

## 🏛️ Governance & Ethiek

**EU AI Act: deadline 2 augustus – nog 16 dagen**
Per **2 augustus 2026** is de EU AI Act volledig van kracht. De transparantieregels voor AI-systemen worden dan afdwingbaar. De 'AI Omnibus' (politiek akkoord mei 2026) vereenvoudigt de regels maar versterkt tegelijkertijd de bevoegdheden van het Europees AI-Bureau en centraliseert het toezicht op GPAI-modellen. Voor organisaties die nog niet compliant zijn, resteert vrijwel geen marge meer. ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement), [artificialintelligenceact.eu](https://artificialintelligenceact.eu/))

**Open brief van 200+ experts over arbeidsmarktimpact**
Meer dan 200 economen en AI-onderzoekers – waaronder 16 Nobelprijswinnaars – ondertekenden een open brief die beleidsmakers oproept *nú* te handelen inzake de economische effecten van AI op werkgelegenheid. Dit vergroot de politieke druk op nationale AI-strategieën in NL en BE en maakt het onderwerp onvermijdelijk in boardroomdiscussies bij Ctac-klanten. ([Al Jazeera, 13 juli](https://www.aljazeera.com/economy/2026/7/13/hundreds-of-experts-warn-the-world-must-prepare-now-for-ais-impact))

## 🔐 Security & Risk

**Drie AI coding agents lekken secrets via één prompt injection**
VentureBeat rapporteert dat drie (anoniem gehouden) AI coding agents via één zorgvuldig geconstrueerde prompt injection gevoelige credentials hebben gelekt. De vendors hadden dit risico al beschreven in hun system cards – maar afdoende runtime-mitigaties ontbraken. Dit is een directe waarschuwing voor elke organisatie die AI coding assistants inzet in CI/CD-pipelines of productieomgevingen. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**Microsoft Copilot Studio CVE – data-exfiltratie ondanks patch**
Een prompt injection kwetsbaarheid in Copilot Studio (in combinatie met Salesforce Agentforce) leidde tot data-exfiltratie nádat een patch was uitgebracht. De workaround bleek onvoldoende. OWASP LLM01 (prompt injection) blijft voor het tweede achtereenvolgende jaar de meest kritische kwetsbaarheid voor LLM-gebaseerde enterprise systemen – en wordt erger naarmate agents meer autonomie krijgen. ([VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook), [airia.com](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

## 📈 Markt & Adoptie

**Microsoft Frontier Company – $2,5 mrd deployment-tak**
Microsoft lanceerde een aparte business unit uitsluitend gericht op succesvolle enterprise AI-implementaties: $2,5 miljard investering, 6.000 industrie- en engineering-experts. De marktboodschap is helder: modelkeuze is niet het probleem, deployment-succes wél. Microsoft 365 Copilot heeft inmiddels 20+ miljoen betaalde seats, met een ARR van $37 miljard (123% YoY groei). ([TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/), [Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/))

**OpenAI biedt VS-overheid aandelenbelang van $42,6 mrd**
OpenAI deed de Amerikaanse overheid een aandelenbelang aan ter waarde van $42,6 miljard – een ongekende stap die de politieke en financiële verwevenheid tussen AI-labs en overheden verder verdiept en het geopolitieke speelveld scherper maakt.

**Google Agentic Data Cloud**
Google lanceerde de Agentic Data Cloud specifiek voor enterprise AI-agents: data-orchestratie voor autonome agents out of the box. Gartner positioneert Google als marktleider in agentic enterprise AI; Microsoft en AWS zijn directe concurrenten. ([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/), [CIO Dive – marktaandeel](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

## 💡 Ctac-relevantie

**Gemini 3.5 Pro als kostenoptimalisatie-kans**: De 4× lagere inputkosten t.o.v. GPT-5.6 en het 2M-token contextvenster bieden directe besparingen in door Ctac gebouwde AI-oplossingen. Voor klanten in documentintensieve sectoren (overheid, zorg, finance) vervalt de noodzaak voor complexe chunking-architecturen – dit verlaagt zowel de bouwkosten als de beheerslast.

**EU AI Act – propositiekans nú**: Over 16 dagen is de wet volledig van kracht. Ctac-klanten in high-risk categorieën (HR-systemen, kredietbeoordeling, kritieke infrastructuur) moeten nu conformiteitsdocumentatie hebben. Dit is een concrete en tijdgebonden propositie: Ctac als AI Act compliance-partner, ook voor klanten die dit nog niet op orde hebben.

**Prompt injection als enterprise-urgent thema**: De incidenten van deze week laten zien dat AI coding assistants in productieomgevingen concrete en aantoonbare risico's meebrengen. Ctac kan dit adresseren met gestructureerde AI security reviews als vast onderdeel van implementatietrajecten – dit differentieert van leveranciers die alleen modellen leveren.

**Microsoft Frontier Company bevestigt het speelveld**: De marktbeweging onderstreept dat de waarde verschuift van modelleverantie naar implementatiesucces. Dit is exact waar Ctac's consultancy-DNA een differentiator is – mits de AI-unit dat scherp en consistent naar buiten brengt.

## 📚 Bronnen & verder lezen

- [Google Gemini 3.5 Pro – AI News July 2026 (AIToolsRecap)](https://aitoolsrecap.com/Blog/AINewsJuly2026.aspx)
- [Moonshot Kimi K3 expected to rival Anthropic Opus 4.8 (TechCrunch)](https://techcrunch.com/2026/07/16/moonshots-upcoming-kimi-3-is-expected-to-close-the-gap-with-anthropics-opus-4-8/)
- [OpenAI GPT-5.6 family launch (TechCrunch)](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [EU AI Act – Governance & Enforcement (EC)](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [EU AI Act Explorer (artificialintelligenceact.eu)](https://artificialintelligenceact.eu/)
- [Hundreds of experts warn on AI's economic impact (Al Jazeera)](https://www.aljazeera.com/economy/2026/7/13/hundreds-of-experts-warn-the-world-must-prepare-now-for-ais-impact)
- [Three AI coding agents leaked secrets via prompt injection (VentureBeat)](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Microsoft Copilot Studio prompt injection CVE (VentureBeat)](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [AI Security in 2026 – Prompt Injection (airia.com)](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Microsoft Frontier Company $2.5B launch (TechCrunch)](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [Microsoft Frontier Company blog (Microsoft)](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)
- [Google Agentic Data Cloud (CIO Dive)](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Microsoft & Google rule AI enterprise market (CIO Dive)](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Prompt injection exploiting enterprise AI design flaws (VentureBeat)](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
