---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-18
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 18 juli 2026

## 🔑 Highlights van de dag

- **EU AI Omnibus officieel vastgesteld**: Op 8 juli ondertekend; hoge-risico AI-deadlines zijn aanzienlijk uitgesteld (Annex III → december 2027, Annex I → augustus 2028). Publicatie in het EU Publicatieblad is de laatste stap voor inwerkingtreding.
- **OpenAI GPT-5.6 familie gelanceerd**: Sol (vlaggenschip), Terra (gebalanceerd) en Luna (snel/goedkoop) vormen een drietrapsraket die frontier-AI democratiseert — Sol claimt 54% beter token-efficiënt voor codetaken dan voorganger.
- **Moonshot AI Kimi K3: grootste open-source model ooit** (2.8 biljoen parameters), presteert op niveau van de top-5 frontier modellen — het open-weight landschap wordt werkelijk competitief.
- **Enterprise AI-productiekloof alarmerend groot**: 85% van ondernemingen is AI-agents aan het piloten, maar slechts 5% heeft ze daadwerkelijk in productie. Cisco-data bevestigt wat velen vermoeden: de implementatiefase is de echte bottleneck.
- **Anthropic + Blackstone lanceerden "Ode"**: een $1,5 miljard implementatiebedrijf dat AI-engineers rechtstreeks naar klantlocaties stuurt — signaal dat grote spelers de uitvoering als de volgende winstmarkt zien.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6** (9 juli) vervangt het enkelvoudige vlaggenschip door drie permanente capability-lagen: Sol (maximale capaciteit), Terra (balanced productie) en Luna (hoge volumes, lage kosten). Toegang is momenteel beperkt tot preview-partners. CEO Altman claimt Sol scoort 80 op de Artificial Analysis Coding Agent Index, 2,8 punten boven Fable 5 van Anthropic, met minder dan de helft van de outputtokens.
([TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/) | [VentureBeat](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov))

**Thinking Machines Inkling** (15 juli) is een open-weight Mixture-of-Experts model met 975 miljard totale parameters (actief ~41B per taak). Bijzonder: het is het eerste grote model van een lab dat expliciet afstand neemt van one-size-fits-all AI en inzet op maatwerk. ([TechCrunch](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/))

**Moonshot AI Kimi K3**: 2,8 biljoen parameters, nu het grootste open-source model ter wereld, met state-of-the-art scores op BrowseComp (91,2/100). Structureel betekent dit dat open-weight modellen nu frontier-kwaliteit benaderen. ([VentureBeat](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems))

**OpenAI GPT-Red** (15 juli): geautomatiseerd red-teaming systeem gebaseerd op self-play, gericht op veiligheid, alignment en weerstand tegen prompt injection. Opvallend omdat OpenAI zelf heeft erkend dat prompt injection waarschijnlijk nooit volledig op te lossen is.

**Trend**: Open modellen zijn goed voor 29% van het traffic via Vercel's AI gateway. De echte race speelt zich niet meer alleen aan de frontier af — de productie-infrastructuur rondom open modellen wordt de nieuwe battleground. ([TechCrunch](https://techcrunch.com/2026/07/14/the-real-ai-race-may-no-longer-be-at-the-frontier-open-models-hugging-face/))

---

## 🏛️ Governance & Ethiek

**EU AI Omnibus definitief vastgesteld**: Op 29 juni gaf de EU-Raad het eindakkoord; op 8 juli ondertekend. Publicatie in het Publicatieblad volgt nog, maar de hoofdlijnen zijn zeker:
- Hoge-risico Annex III systemen (biometrie, onderwijs, HR, rechtshandhaving): compliance vereist per **2 december 2027** (was 2 augustus 2026).
- Hoge-risico Annex I (medische apparatuur, machines): uitstel tot **2 augustus 2028**.
- Nieuw verbod per december 2026: AI voor niet-consensuele seksuele beeldgeneratie en CSAM.
- AI Office krijgt uitgebreide bevoegdheden en centraal toezicht op GPAI-modellen.
([White & Case](https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules) | [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/))

Tegelijk publiceerde de Europese Commissie een actieplan voor cyberveiligheid en AI (juli 2026), gericht op lidstaten, bedrijven en overheden die te maken hebben met risico's van geavanceerde AI-modellen. ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement))

**NL-signaal**: Computable meldde op 16 juli dat de AI-hype in het Nederlandse IT-kanaal plaats maakt voor nuchterheid — 35% van medewerkers geeft aan onvoldoende uitleg te krijgen over AI-gebruik binnen hun organisatie. ([Computable](https://www.computable.nl/2026/07/16/ai-hype-maakt-plaats-voor-nuchterheid-geen-autonoom-wondermiddel/))

---

## 🔐 Security & Risk

Prompt injection blijft OWASP LLM01 — het meest kritieke risico voor enterprise AI. Uit recent VentureBeat-onderzoek blijkt dat aanvallers actief RAG-pipelines, agent-routers en multi-agent architecturen aanvallen. Microsoft's Copilot Studio had een CVE-2026-21520 (CVSS 7.5): gepatcht in januari, maar data was al geëxfiltreerd. ([VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers) | [VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

Moltbook's agentplatform lekte 1,5 miljoen API-tokens waaronder plaintext OpenAI-sleutels — een reminder dat agent-infrastructuur nieuwe attack surfaces introduceert die anders zijn dan traditionele applicaties.

In België signaleert Data News een toename van AI-gedreven cyberaanvallen: sneller, overtuigender en moeilijker te detecteren. ([datanews.knack.be](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/))

---

## 📈 Markt & Adoptie

Microsoft rapporteert **20+ miljoen betaalde Copilot-seats** en een AI-business run rate van **$37 miljard** (+123% YoY). Google Cloud overtroeg voor het eerst **$20 miljard** kwartaalomzet. De drie hyperscalers investeren gezamenlijk **>$500 miljard** in AI-infrastructuur dit fiscale jaar. ([CIO Dive](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/) | [CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/))

**Anthropic + Blackstone: "Ode"** — een $1,5 miljard joint venture (mei 2026) dat AI-engineers fysiek naar klantlocaties stuurt voor implementatie. Niet een model-business, maar een uitvoeringsservice. Tegelijk deed OpenAI hetzelfde. Dit is een fundamentele strategische move: de hyperscalers begrijpen dat het verschil niet in modellen zit maar in implementatie. ([TechCrunch](https://techcrunch.com/2026/07/15/anthropic-blackstone-bet-the-next-trillion-dollar-ai-business-is-implementation-not-models/))

**De agentic kloof**: 85% piloot AI-agents, maar slechts 5% draait ze in productie. Cisco-cijfers bevestigen dat enterprise-infrastructuur is gebouwd voor mensen, niet voor agents — dit is de systeemfout die de doorbraak blokkeert.

**Benelux**: IT-dienstverleners zien AI als grootste groeikatalysator; 30% verwacht significante groei, 10% denkt dat AI hun primaire inkomstenbron wordt. ([Computable](https://www.computable.nl/2026/05/18/gtia-ai-geeft-spanning-tussen-it-kanaal-en-tech-leveranciers/))

---

## 💡 Ctac-relevantie

**Implementatie als kernpropositie**: Dat Anthropic en OpenAI elk een apart implementatiebedrijf lanceren bevestigt wat voor Ctac de centrale kans is: niet modellen verkopen, maar AI-implementatie leveren. De kloof tussen 85% pilot en 5% productie is precies de ruimte waar een betrouwbare IT-consultant waarde toevoegt. Ctac zou een helder aanbod moeten formuleren rond "van pilot naar productie" voor enterprise AI-agents.

**EU AI Omnibus geeft lucht én urgentie**: De verlengde deadlines voor hoge-risico AI zijn goed nieuws voor klanten die nog niet compliant zijn, maar de boodschap moet zijn: gebruik deze tijd verstandig, want de regelgeving wordt niet weggemoffeld. Klanten in zorg, HR, en overheid (Annex III-toepassingen) hebben tot december 2027 — gebruik dat voor gestructureerde compliance-trajecten waar Ctac op kan adviseren.

**Open modellen veranderen de propositie-calculus**: Kimi K3 (open, 2.8T parameters) en Inkling (open-weight MoE) betekenen dat frontier-kwaliteit AI straks niet meer Microsoft of Google vereist. Voor Ctac's klanten die vendor lock-in willen vermijden of specifieke deploymentbehoeften hebben (on-premise, privacy-gevoelig), worden open-weight modellen een serieuze optie om in het advies mee te nemen.

**Prompt injection is een klantrisico**: Elke klant die AI-agents aan externe content blootstelt (e-mail parsing, web browsing, documenten verwerken) heeft een prompt-injection-risico. Ctac kan dit adresseren als onderdeel van een verantwoord AI-implementatieaanbod.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – GPT-5.6 lancering](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [VentureBeat – GPT-5.6 Sol, Terra, Luna](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)
- [TechCrunch – Thinking Machines Inkling](https://techcrunch.com/2026/07/15/thinking-machines-amps-up-its-bet-against-one-size-fits-all-ai-with-its-first-open-model-inkling/)
- [VentureBeat – Moonshot AI Kimi K3](https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems)
- [TechCrunch – Open modellen vs. frontier](https://techcrunch.com/2026/07/14/the-real-ai-race-may-no-longer-be-at-the-frontier-open-models-hugging-face/)
- [White & Case – EU AI Omnibus](https://www.whitecase.com/insight-alert/eu-agrees-digital-omnibus-deal-simplify-ai-rules)
- [Gibson Dunn – EU AI Omnibus uitgestelde deadlines](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [digital-strategy.ec.europa.eu – AI Act governance](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – Microsoft Copilot Studio CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [CIO Dive – Microsoft earnings Q3 2026](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [CIO Dive – Google Cloud $20B](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [TechCrunch – Anthropic + Blackstone "Ode"](https://techcrunch.com/2026/07/15/anthropic-blackstone-bet-the-next-trillion-dollar-ai-business-is-implementation-not-models/)
- [CIO Dive – Microsoft vs Google enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Computable – AI-hype maakt plaats voor nuchterheid](https://www.computable.nl/2026/07/16/ai-hype-maakt-plaats-voor-nuchterheid-geen-autonoom-wondermiddel/)
- [Data News – Meer cyberaanvallen door AI in België](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
