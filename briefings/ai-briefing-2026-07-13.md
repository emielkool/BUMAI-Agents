---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-13
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 13 juli 2026

## 🔑 Highlights van de dag

- **GPT-5.6 Sol zet nieuwe codeer-lat:** OpenAI lanceerde op 9 juli de Sol/Terra/Luna familie. Sol scoort 80/100 op de Artificial Analysis Coding Agent Index – 2,8 punten boven Fable 5 – en is tegelijk sneller en goedkoper. Algemene beschikbaarheid verwacht in de komende weken.
- **JADEPUFFER: eerste volledig autonome AI-ransomware:** Een AI-agent voerde eind juni/begin juli een complete aanvalsketen uit – van initiële toegang tot database-extortie – zonder menselijke sturing. Sysdig meldde het als mijlpaal voor "agentic threat actors".
- **Anthropic overtreft OpenAI in enterprise-adoptie:** Anthropic rapporteert $47 mld geannualiseerde omzet en verwacht al in 2029 winstgevend te zijn – een jaar vóór OpenAI. De concurrentiestrijd in de B2B-markt is nu volledig open.
- **EU AI omnibus: vereenvoudiging in zicht:** Na politiek akkoord in mei 2026 werkt de Europese Commissie aan guidelines die compliance voor bedrijven moeten verlichten. De AI Office bereidt praktische handleidingen voor over hoog-risicoclassificaties en transparantieverplichtingen.
- **Microsoft verhoogt M365-prijzen per 1 juli:** AI-mogelijkheden worden doorberekend in enterprise-abonnementen. Tegelijk lanceert Microsoft de "Frontier Company" als apart operationeel bedrijf voor AI-engineering dienstverlening.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 Sol, Terra, Luna** (lancering 9 juli) is de meest significante release van deze week. Sol is gepositioneerd als het beste codeermodel in OpenAI's portfolio, draait op Cerebras-hardware met 750 tokens/sec en scoort state-of-the-art op Terminal-Bench 2.1 en DeepSWE. Prijzen: Sol $5/$30 per 1M tokens (in/out), Terra $2,50/$15, Luna $1/$6. De preview is vooralsnog beperkt tot ~20 partnerorganisaties, maar GA wordt medio juli verwacht.
→ [TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/) | [OpenAI](https://openai.com/index/gpt-5-6/)

**SpaceXAI Grok 4.5** werd op 8 juli uitgebracht als "Opus-class model" met 2x hogere tokenefficiëntie dan concurrenten. Gericht op coding, office-automatisering en research. Interessant als alternatief, maar vooralsnog geen benchmarks die Sol of Fable 5 echt verdringen.
→ [TechCrunch](https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/)

**Google Gemini 3.5 Flash** is de nieuwe standaard in AI Mode in Google Search. Tegelijk heeft Google de Agentic Data Cloud gelanceerd – een platform gericht op enterprise AI-agenten die op data-infrastructuur opereren.
→ [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)

**Open-source:** Qwen 3 235B-A22B blijft de toonaangevende open-weight optie voor reasoning/coding; DeepSeek R1 voor wiskundige redenering; Llama 4 Scout voor lange context (10M tokens).

---

## 🏛️ Governance & Ethiek

**EU AI omnibus-vereenvoudiging:** Na het politieke akkoord van mei 2026 werkt de Commissie aan praktische guidelines voor de toepassing van de AI Act – met focus op hoog-risicoclassificatie, transparantievereisten en GPAI-model verplichtingen. Het is een netto positief signaal voor bedrijven: minder compliance-ambiguïteit.
→ [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)

**EU Cybersecurity & AI actieplan (juli 2026):** De Commissie kondigt een evaluatiecapaciteitsprogramma aan om frontier-modellen te beoordelen vóór markttoelating in de EU. Operationeel verwacht in 2027.
→ [EU AI Act tracker](https://artificialintelligenceact.eu/)

**Witte Huis/OpenAI/Anthropic/Google:** Er zijn geavanceerde gesprekken over vrijwillige frontier-modelstandaarden. OpenAI biedt de Amerikaanse overheid een 5%-belang aan ter waarde van ~$42,6 mld. Dit versterkt de verwevenheid van Big Tech met overheidsbeleid – iets dat Europese inkopers mee zullen wegen.
→ [Fortune](https://fortune.com/2026/07/02/sam-altman-new-world-order-ai-openai-google-anthropic/)

---

## 🔐 Security & Risk

**JADEPUFFER – agentic ransomware:** Dit is de meest urgente security-ontwikkeling van de week. Een bedreigingsactor exploiteerde CVE-2025-3248 in Langflow (een LLM-app bouwframework) en zette vervolgens een autonome AI-agent in die zelfstandig reconnaissance deed, credentials stal, lateraal bewoog, persistentie vestigde, privileges escaleerde en 1.342 Nacos service-configuraties versleutelde. Bijzonder verontrustend: de agent paste zich in 31 seconden aan op een mislukte loginpoging. Sysdig concludeert dat het tijdperk van "Agentic Threat Actors" (ATAs) is aangebroken.
→ [Sysdig](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion) | [BleepingComputer](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/)

**Bredere trend – AI-geholpen aanvallen:** Gemiddelde tijd om een kritieke CVE te patchen is 74 dagen. De combinatie van snellere exploitatie via AI en langzame patching bij organisaties creëert een groeiend aanvalsvenster. Organisaties die LLM-frameworks (Langflow, LangChain, etc.) in productie draaien zijn direct kwetsbaar.

---

## 📈 Markt & Adoptie

**Microsoft Frontier Company:** Microsoft lanceert een nieuw operationeel bedrijf dat "Frontier Transformation" via AI aanbiedt – inclusief industrie-expertise, change management en enterprise-grade AI-engineering. Dit is feitelijk een directe concurrent van IT-consultancyfirma's als Ctac in de AI-dienstverlening.
→ [Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)

**Hyperscaler investeringen:** AWS committeert $10 mld aan data centers in North Carolina; Google Cloud voegt $10 mld toe bovenop al geplande $75 mld. De infrastructuur-race versnelt, wat de beschikbaarheid van GPU-capaciteit op middellange termijn vergroot.

**Enterprise adoptie blijft achter:** 79% van de enterprises ervaart adoptie-uitdagingen ondanks hoge investeringen; twee derde zit vast in de pilot-fase. Dit is een structureel patroon dat consultant-kansen creëert.

**Anthropic vs. OpenAI:** Anthropic rapporteert $47 mld geannualiseerde omzet en verwacht winstgevendheid in 2029. De marktleider-positie van OpenAI is niet langer vanzelfsprekend.
→ [VentureBeat](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)

---

## 💡 Ctac-relevantie

**JADEPUFFER is directe actie vereist voor klanten:** Elke klant van Ctac die Langflow of vergelijkbare LLM-frameworks (LangChain, LlamaIndex) in productie heeft, dient CVE-2025-3248 onmiddellijk te patchen. Dit is een concrete security-adviesopportuniteit nu – vóór dat aanvallen breed worden.

**GPT-5.6 Sol voor interne tooling:** Als Ctac's AI-unit coding-assistentie wil opschalen, is Sol qua prijs-prestatie aantrekkelijk ($5/$30 per 1M tokens, sneller dan Fable 5). Vergelijk tegen Fable 5 in een interne benchmark voordat abonnementen worden verlengd.

**Microsoft Frontier Company als signaal:** Microsoft positioneert zich nadrukkelijk als concurrent van IT-consultants in AI-engineering. Ctac moet zijn eigen AI-propositie scherper neerzetten – wat maakt Ctac distinctief ten opzichte van wat Microsoft nu direct aanbiedt?

**EU omnibus-vereenvoudiging als verkoopargument:** De komende guidelines verlagen de drempel voor compliance, maar creëren ook vraag naar interpretatiehulp. Ctac kan klanten in gereguleerde sectoren (zorg, finance, overheid) helpen de guidelines te vertalen naar concrete implementatieplannen.

**Enterprise pilot-probleem = Ctac kans:** 79% adoptie-uitdagingen en twee derde stuck in pilots – dit is exact waar Ctac's implementatie-expertise waarde toevoegt. Een propositie gericht op "van AI-pilot naar productie" sluit direct aan op de marktbehoefte van dit moment.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI GPT-5.6 lancering](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [OpenAI – Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)
- [TechCrunch – Grok 4.5 release](https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/)
- [Sysdig – JADEPUFFER agentic ransomware](https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion)
- [BleepingComputer – JadePuffer ransomware AI agent](https://www.bleepingcomputer.com/news/security/jadepuffer-ransomware-used-ai-agent-to-automate-entire-attack/)
- [Forbes – Eerste AI-gestuurde ransomware aanval](https://www.forbes.com/sites/jonmarkman/2026/07/07/the-first-ransomware-attack-run-from-start-to-finish-by-an-ai-agent/)
- [Microsoft Blog – Frontier Company](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)
- [CIO Dive – Microsoft & Google enterprise AI-marktleiders](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [VentureBeat – Anthropic vs. OpenAI enterprise adoptie](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)
- [EU AI Act – Implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act guidelines](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Fortune – OpenAI concurrentiepositie](https://fortune.com/2026/07/02/sam-altman-new-world-order-ai-openai-google-anthropic/)
