---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-15
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 15 juni 2026

## 🔑 Highlights van de dag

- **EU AI Act deadline nadert:** De Europese Commissie publiceerde op 10 juni de finale Code of Practice voor markering van AI-gegenereerde content. De volledige toepasselijkheid van de AI Act volgt op 2 augustus 2026 — nog zeven weken.
- **Anthropic onder druk van VS-overheid:** Het Amerikaanse ministerie schakelde op 12 juni toegang tot Claude Fable 5 en Mythos 5 uit vanwege nationale veiligheidszorgen. Opmerkelijk: Anthropic's eigen veiligheidswaarschuwingen over die modellen speelden mee in dit overheidsbesluit.
- **Google I/O 2026: Gemini Omni en 3.5 Flash gelanceerd.** Gemini Omni kan video genereren vanuit willekeurige input; Gemini 3.5 Flash is nu standaard in Google Search en de basis van het nieuwe agent-first platform Antigravity.
- **Supply chain aanval op LiteLLM:** Aanvaller TeamPCP publiceerde een vergiftigde versie van het populaire Python-package — goed voor ~47.000 downloads in 40 minuten vóór quarantaine. Raakt direct AI-infrastructuur in grote enterpriseomgevingen.
- **Enterprise agentic gap:** 85% van de enterprise-organisaties wil binnen drie jaar agentic AI inzetten, maar 76% erkent dat hun operationele processen dit niet aankunnen. Adoptie blijft ver achter op de ambitie.

---

## 🧠 Technologie & Modellen

**Google I/O 2026** leverde de grootste AI-uitrol tot nu toe. Gemini Omni is volledig multimodaal — generatie én begrip van video, audio, tekst en beeld. Gemini 3.5 Flash is het nieuwe standaardmodel in Google Search en driving Google Antigravity, een agent-first ontwikkelplatform met Information Agents, Gemini Spark en een Universal Cart voor agentic shopping. Apple kondigde bij WWDC (9 juni) een samenwerking met Google aan voor Foundation Models die Apple Intelligence ondersteunen — een merkwaardige strategische zet van Apple richting extern model-gebruik.

**Anthropic** bracht Claude Mythos 1 uit, voorlopig alleen beschikbaar voor circa 50 partners in defensief cybersecurity-onderzoek (Project Glasswing). Claude Code ontving een update met nested sub-agents, betere Chrome/VSCode-integratie en verbeterd model- en regiobeheer. De zwaardere modellen Fable 5 en Mythos 5 zijn tijdelijk onbereikbaar na het VS-overheidsingrijpen van 12 juni.

**OpenAI** lanceerde een Partner Network met een investering van $150M om wereldwijde enterprise-adoptie te versnellen. Daarnaast beter geheugen voor ChatGPT, nieuwe mogelijkheden voor GPT-Rosalind, en een vertrouwelijke concept-S-1 bij de SEC — de beursgang komt dichterbij.

*Bronnen: [llm-stats.com](https://llm-stats.com/ai-news) · [blog.google I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) · [TechCrunch WWDC](https://techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/)*

---

## 🏛️ Governance & Ethiek

De **EU AI Act** nadert haar eindstreep: volledige toepasselijkheid per 2 augustus 2026. De Europese Commissie publiceerde op 10 juni de finale **Code of Practice voor markering van AI-gegenereerde content** — een concrete verplichting voor aanbieders. De AI Office krijgt versterkte bevoegdheden voor toezicht op GPAI-modellen, met minder governance-fragmentatie. Een politiek akkoord uit mei 2026 vereenvoudigt de regels en verlengt implementatietijdlijnen voor sommige hoog-risico systemen — ook relevant voor mkb en mid-cap bedrijven die nu meer toegang tot regulatory sandboxes krijgen.

*Bronnen: [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [artificialintelligenceact.eu](https://artificialintelligenceact.eu/)*

---

## 🔐 Security & Risk

Twee urgente signalen deze week:

1. **LiteLLM supply chain aanval**: De Threat Group TeamPCP gebruikte gestolen credentials om een malicieuze versie van het LiteLLM Python-package te publiceren. In 40 minuten werden ~47.000 downloads gemeten vóór de quarantaine. LiteLLM is breed ingezet in AI-infrastructuurteams van grote organisaties — dit raakt de release pipeline die red teams nog niet structureel bewaken.

2. **OWASP Top 10 for Agentic Applications 2026** is gepubliceerd met tien nieuwe risico-categorieën: goal hijack, tool misuse, memory poisoning, insecure inter-agent communication en rogue agents zijn de meest kritische. Dit is de facto de nieuwe beveiligingsstandaard voor multi-agent systemen.

Bruce Schneier signaleert ook een groeiende spanning bij kwetsbaarheidsontdekking: zowel de VS als China zetten AI in voor offensieve reconnaissance, terwijl legacy systemen onvoldoende worden gepatcht.

*Bronnen: [VentureBeat supply chain](https://venturebeat.com/security/supply-chain-incidents-openai-anthropic-meta-release-surface-vendor-questionnaire-matrix) · [Schneier on Security](https://www.schneier.com/blog/archives/2026/06/vulnerability-disclosure-in-the-age-of-ai.html) · [TechCrunch Anthropic/overheid](https://techcrunch.com/2026/06/12/anthropics-safety-warnings-may-have-just-backfired-the-government-has-pulled-the-plug-on-its-most-powerful-ai/)*

---

## 📈 Markt & Adoptie

**Microsoft en Google domineren** de enterprise AI-markt volgens Gartner. Microsoft Copilot Studio leidt met 38,6% primaire platform-adoptie (feb 2026); OpenAI stijgt naar 25,7%. Alle hyperscalers stapelen enorme data center-investeringen op: Microsoft $30B (VK), Google Cloud +$10B, AWS $10B (North Carolina).

De **agentic AI markt** groeit van $9,14 miljard in 2026 naar een verwachte $139 miljard in 2034. Toch lopen technologie en praktijk ver uiteen: slechts 19% van de organisaties gebruikt vandaag multi-agent systemen, terwijl Gartner verwacht dat 40% van de enterprise applicaties in 2026 taakspecifieke AI-agents zal bevatten.

*Bronnen: [CIO Dive Microsoft/Google](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) · [VentureBeat enterprise agentic](https://venturebeat.com/orchestration/enterprise-agentic-ai-requires-a-process-layer-most-companies-havent-built)*

---

## 💡 Ctac-relevantie

**Compliance-kans:** Met de AI Act volledig van kracht per 2 augustus is er een acuut adviesvraagstuk voor Ctac-klanten met hoog-risico AI-toepassingen. De gepubliceerde Code of Practice voor AI-contentmarkering maakt het concreet en uitvoerbaar — dit is een directe propositie-kans voor de AI-unit om klanten compliance-klaar te maken in de komende zeven weken.

**Agentic AI implementatie:** De enterprise agentic gap (85% ambitie vs. 76% infrastructureel ongereed) is precies het speelveld voor Ctac. De 'process layer' die ontbreekt — orkestratie, veilige inter-agent communicatie, change management — is een uitvoerbaar advies- en implementatiedomein. Begin met één concreet pilot-domein per klant (bijv. finance of customer service).

**Security advisory:** De LiteLLM aanval en het nieuwe OWASP Agentic Top 10 framework zijn directe aanleiding om AI-security op te nemen in elke AI-implementatietraject. Advies: evalueer supply chain-risico's in bestaande AI-pipelines bij klanten en stel een minimale beveiligingsbaseline op voor multi-agent deployments.

**OpenAI Partner Network:** De $150M investering in het partner-ecosysteem is een concreet aanknopingspunt om te verkennen of Ctac als gecertificeerde implementatiepartner kan aansluiten — relevant voor enterprise sales-positionering.

---

## 📚 Bronnen & verder lezen

- [Google I/O 2026 – alle aankondigingen](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [TechCrunch WWDC 2026 – Apple Intelligence & Siri](https://techcrunch.com/2026/06/09/wwdc-2026-everything-announced-on-siri-ai-os-27-apple-intelligence-and-more/)
- [LLM Stats – AI updates juni 2026](https://llm-stats.com/ai-news)
- [EU AI Act – governance en handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [TechCrunch – Anthropic & VS-overheid](https://techcrunch.com/2026/06/12/anthropics-safety-warnings-may-have-just-backfired-the-government-has-pulled-the-plug-on-its-most-powerful-ai/)
- [VentureBeat – LiteLLM supply chain aanval](https://venturebeat.com/security/supply-chain-incidents-openai-anthropic-meta-release-surface-vendor-questionnaire-matrix)
- [Schneier on Security – kwetsbaarheid in het AI-tijdperk](https://www.schneier.com/blog/archives/2026/06/vulnerability-disclosure-in-the-age-of-ai.html)
- [VentureBeat – enterprise agentic process layer](https://venturebeat.com/orchestration/enterprise-agentic-ai-requires-a-process-layer-most-companies-havent-built)
- [CIO Dive – Microsoft en Google leiden enterprise AI-markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
