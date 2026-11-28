---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-25
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 25 november 2026

## 🔑 Highlights van de dag

- **Drie frontier labs lanceerden tegelijk nieuwe modellen** in november: OpenAI GPT-6.2 Astra/Sol (17 nov), Anthropic Fable 5.2 & Mythos 5.2 (9 nov) en Google Gemini 4 Neon (18 nov). De concurrentie op snelheid, kosten en enterprise-toepasbaarheid versnelt zichtbaar.
- **Microsoft Ignite 2026 (17–18 nov):** Agent 365 is uit preview — Microsoft positioneert agents als een governance-uitdaging, niet meer als experimentele technologie. De koppeling met AWS en Google Cloud via registry sync is strategisch significant.
- **UK NCSC waarschuwt (24 nov):** AI-gedreven cyberaanvallen nemen sterk toe. Geen nieuwe kwetsbaarheden — maar AI vindt en exploiteert bekende zwaktes nu in minuten in plaats van weken.
- **EU AI Act: deadline 2 december nadert.** Het verbod op AI-gegenereerde deepfake-naaktbeelden en CSAM wordt afdwingbaar. Voor Nederlandse bedrijven die gegenereerde content publiceren is dit direct relevant.
- **Slechts 15% van organisaties heeft multi-agent AI op schaal uitgerold** (Deloitte). De belofte van agentic AI overstijgt de operationele realiteit vooralsnog aanzienlijk.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-6.2 Astra & Sol** zijn beschikbaar sinds 17 november. Astra richt zich op complexe professionele taken (coding, reasoning), Sol op snelheid bij multi-step workflows. Op 23 november volgde een GPT-6.2-versie voor ChatGPT met 71,7% op beeldbegreipbenchmarks (vs. 47,4% voor GPT-6). Prijsstelling is nog niet breed gecommuniceerd.
→ [OpenAI Research](https://openai.com/research/index/)

**Anthropic Fable 5.2 & Mythos 5.2** (9 nov) zijn 30% sneller dan hun voorgangers. Prijsstelling: $8/M input en $40/M output tokens — aan de hogere kant, maar in lijn met topmodellen. Claude Haiku 5.5 is ook beschikbaar als goedkoop snel model.
→ [TechCrunch: Anthropic releases Mythos and Fable models](https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/)

**Google Gemini 4 Neon** (18 nov) heeft een context van 1 miljoen tokens en scoort #3 op de Artificial Analysis Intelligence Index. Prijs: $3/M input, $15/M output. Gemini 4 Carbon (10 nov) is duurder ($4/$20) maar gericht op zwaardere taken — introductieprijs vervalt op 30 november.
→ [Google: Introducing Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

**Kritische noot:** De modelrelease-frequentie is hoog, maar de werkelijke differentiatie wordt kleiner. Voor enterprise-gebruik tellen governance, prijs en integratie inmiddels meer dan ruwe benchmarkscores.

---

## 🏛️ Governance & Ethiek

**EU AI Act enforcement is in volle gang.** Vanaf 2 augustus 2026 handhaven de AI Office en nationale autoriteiten actief. Op 16 november vergaderde het AI Act Advisory Forum en werden co-voorzitters gekozen. Op dezelfde dag vroeg de Commissie feedback op een template voor grondrechtenimpactbeoordelingen.
→ [EC: AI Act enforcement framework](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)

**Deadline 2 december 2026:** Vanaf dan verboden — AI-gegenereerde niet-consensuele intieme beelden en CSAM. Aanbieders van generatieve AI die vóór augustus 2026 al op de markt waren, moeten op die datum ook voldoen aan labelverplichtingen (artikel 50 lid 2).
→ [AI Act Explorer](https://artificialintelligenceact.eu/)

**Nederland:** De AI-tokenkosten zijn mogelijk aftrekbaar via de WBSO, maar wetswijzigingen worden pas na 2027 verwacht. De Autoriteit Persoonsgegevens houdt sectoraal toezicht; een aparte AI-toezichthouder is in discussie.
→ [Computable: Kosten van AI-tokens mogelijk aftrekbaar via WBSO](https://www.computable.nl/2026/11/09/kosten-van-ai-tokens-mogelijk-aftrekbaar-via-wbso/)

---

## 🔐 Security & Risk

**UK NCSC (24 nov):** Forse stijging van AI-gedreven cyberaanvallen. Geen nieuwe zero-days nodig — AI versnelt exploitatie van bekende zwaktes die jaren onopgemerkt bleven. Dit is een directe waarschuwing voor organisaties die achterlopen met patchbeleid.
→ [TechCrunch: UK warns AI-driven cyberattacks](https://techcrunch.com/2026/11/24/uk-warns-ai-driven-cyberattacks-are-exposing-years-of-weak-security/)

**Satya Nadella (18 nov):** Veel kritieke infrastructuur is "niet te patchen". AI maakt het makkelijker om kwetsbaarheden te vinden. Dit weerkaatst de FBI-waarschuwing over aanvallers die AI-pentesttools inzetten op ongekende snelheid.
→ [TechCrunch: Satya Nadella on unpatchable infrastructure](https://techcrunch.com/2026/11/18/amidst-fears-of-ai-cyberattacks-satya-nadella-says-lots-of-critical-infrastructure-is-unpatchable/)

**Modelrisico (Schneier, 15 nov):** Onderzoek toont aan dat sommige Chinese open-weight modellen geopolitieke triggers bevatten die de veiligheid van gegenereerde code beïnvloeden afhankelijk van context. Dit is relevant voor bedrijven die open-source modellen zonder screening inzetten.
→ [Schneier on Security: November 15, 2026](https://www.schneier.com/crypto-gram/archives/2026/1115.html)

---

## 📈 Markt & Adoptie

**Microsoft Ignite 2026** introduceerde: (1) **Agent 365** — governance-laag voor enterprise AI-agents, nu algemeen beschikbaar, met registry sync richting AWS Bedrock en Google Cloud; (2) **Code 2** — agentic coding modellen als kostenefficiënt alternatief; (3) **Microsoft IQ** — contextbeheerplatform voor agents. Copilot wordt gepositioneerd als "het nieuwe besturingssysteem voor werk".
→ [Microsoft Blog: Ignite 2026](https://blogs.microsoft.com/blog/2026/11/17/ignite-2026-building-the-frontier-ecosystem/)

**Microsoft + IBM: Imagine Enterprise** (10 nov): meer dan 6.000 kant-en-klare agents, ondersteund door forward-deployed engineers. Dit is een directe aanval op de implementatiekloof bij enterprise-klanten.
→ [CIO Dive: Microsoft IBM team up](https://www.ciodive.com/news/microsoft-ibm-team-up-ai-agent-platform/874152/)

**Implementatiekloof is reëel:** Deloitte-onderzoek (500+ tech-leaders) toont dat slechts 15% van organisaties multi-agent AI op schaal heeft uitgerold. McKinsey rapporteert dat 30% van bedrijven na adoptie van coding agents productiviteitsdaling zag. AI-agents zijn nog lang geen plug-and-play.
→ [CIO Dive: Agentic AI years away](https://www.ciodive.com/news/agentic-ai-years-away-enterprises/827737/)

---

## 💡 Ctac-relevantie

**Agent 365 en de governance-laag zijn nu het gespreksonderwerp bij enterprise-klanten.** De vraag is niet meer "kunnen we agents bouwen?" maar "hoe besturen we ze veilig?". Ctac heeft hier een concrete adviesrol: het helpen inrichten van agent governance, identity en permissiestructuren. Dit is een dienstverleningskans die aansluit bij bestaande Ctac-competenties in Microsoft-ecosystemen.

**De implementatiekloof (15% schaalbaarheid) is Ctac's marktopening.** Veel bedrijven hebben budget voor AI maar geen roadmap voor verantwoorde uitrol. Een pragmatisch AI-adoptieprogramma — inclusief data-readiness, governance en snelle ROI-validatie — is precies wat ontbreekt bij de 85% die nog niet op schaal zit.

**EU AI Act compliance (deadline 2 dec) is een directe aanleiding voor klantgesprekken.** Nederlandse bedrijven die content publiceren met generatieve AI moeten per 2 december labelen. Wie dat nog niet geregeld heeft, loopt handhavingsrisico. Dit is een concrete ingang voor de AI-unit om compliance-checks aan te bieden.

**WBSO-aftrek voor AI-tokenkosten** is in onderzoek bij de RVO. Als dit doorgaat na 2027, verandert de businesscase voor het inzetten van frontier-modellen bij innovatieprojecten. Houd dit in de gaten voor propositieontwikkeling richting klanten in R&D-intensieve sectoren.

---

## 📚 Bronnen & verder lezen

- [OpenAI Research index](https://openai.com/research/index/)
- [Anthropic: Claude Fable 5.2 & Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- [TechCrunch: Anthropic releases new Mythos and Fable models (9 nov 2026)](https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/)
- [Google: Introducing Gemini 4 Neon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)
- [Google: Gemini 4 Carbon is now available](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)
- [Microsoft Blog: Ignite 2026 – Building the frontier ecosystem](https://blogs.microsoft.com/blog/2026/11/17/ignite-2026-building-the-frontier-ecosystem/)
- [VentureBeat: Microsoft takes Agent 365 out of preview](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [CIO Dive: Microsoft + IBM team up on AI agent platform](https://www.ciodive.com/news/microsoft-ibm-team-up-ai-agent-platform/874152/)
- [CIO Dive: Full-scale AI agent adoption remains years away](https://www.ciodive.com/news/agentic-ai-years-away-enterprises/827737/)
- [TechCrunch: UK warns AI-driven cyberattacks (24 nov 2026)](https://techcrunch.com/2026/11/24/uk-warns-ai-driven-cyberattacks-are-exposing-years-of-weak-security/)
- [TechCrunch: Satya Nadella on unpatchable infrastructure (18 nov 2026)](https://techcrunch.com/2026/11/18/amidst-fears-of-ai-cyberattacks-satya-nadella-says-lots-of-critical-infrastructure-is-unpatchable/)
- [Schneier on Security: Crypto-Gram November 15, 2026](https://www.schneier.com/crypto-gram/archives/2026/1115.html)
- [EC: EU AI Act enforcement framework](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [AI Act Explorer (artificialintelligenceact.eu)](https://artificialintelligenceact.eu/)
- [Computable: Kosten van AI-tokens mogelijk aftrekbaar via WBSO](https://www.computable.nl/2026/11/09/kosten-van-ai-tokens-mogelijk-aftrekbaar-via-wbso/)
