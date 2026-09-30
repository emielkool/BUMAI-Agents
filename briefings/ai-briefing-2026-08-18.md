---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-18
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 18 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaving gestart:** Vanaf 2 augustus 2026 handhaaft de AI Office actief de transparantie- en governanceverplichtingen. AI-systemen die burgers bellen of met ze chatten moeten zich nu direct kenbaar maken — dit is afdwingbaar recht, geen vrijblijvende richtlijn.
- **Meta Muse Glimmer 30B gelanceerd:** Meta's nieuwste open-source model draait volledig lokaal op consumenten­hardware, ondersteunt agentische taken, tool use en multimodaliteit — Apache 2.0. Serieuze concurrent voor cloud-afhankelijke enterprise AI.
- **Anthropic onbekende model lost Riemann-deelprobeem op:** Een nog niet gepubliceerd Anthropic-model verhoogde significant de ondergrens van bewezen gevallen van de Riemann-hypothese. Symbolisch groot; praktisch nog niet toepasbaar, maar het toont waar frontier-AI naartoe beweegt.
- **Atlassian Rovo kwetsbaar voor prompt injection:** Aanvallers kunnen Rovo misleiden om Jira- en Confluence-data naar externe partijen te sturen. OWASP bevestigt: prompt injection is voor het tweede jaar op rij de #1 LLM-kwetsbaarheid.
- **SAP lanceert Business AI Platform:** SAP bundelt BTP, Business Data Cloud en Business AI tot één platform inclusief een 'Autonomous Suite' die AI-agenten inbedt in bestaande ERP-processen. Grote stap richting volledig geautomatiseerde bedrijfsprocessen bij SAP-klanten.

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 familie** (Sol, Terra, Luna) werd in juli gelanceerd; Sol wordt nu actief gepositioneerd als 's werelds beste codeermodel en beats Anthropic's Fable 5 op de benchmark — 80,2 punten vs. 77,4, met de helft van de tokens en een derde van de kosten. ([TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/))

**Meta Muse Glimmer 30B** (10 aug.) is destillaat van Muse Spark en gebouwd voor autonome agentische taken op lokale hardware — zonder cloud, zonder API-kosten. De Apache 2.0 licentie maakt commercieel gebruik vrijwel onbeperkt. ([Hugging Face](https://huggingface.co/blog/muse-glimmer))

**Anthropic's onbekende wiskunde-model** (11 aug.) zette een nieuwe record voor de Riemann-hypothese. Geen product, wel een signaal: frontier AI nadert gebieden waar menselijke experts jarenlang vaststaan. ([TechCrunch](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/))

Het Hugging Face open-model-ecosysteem groeide dit jaar van 2,43 naar 2,96 miljoen repositories — de democratisering van AI-capaciteit versnelt onverminderd. ([Hugging Face](https://huggingface.co/blog/state-of-open-models-summer-2026))

## 🏛️ Governance & Ethiek

Vanaf **2 augustus 2026** handhaaft de Europese AI Office de AI Act inclusief transparantieverplichtingen. Kernpunten: AI-systemen moeten zichzelf kenbaar maken (chatbots, synthetische spraak, deepfakes), elke lidstaat moet een nationale AI-sandbox hebben, en de AI Omnibus-wijzigingen (vereenvoudiging compliance) zijn per juli 2026 van kracht. ([EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august))

In Nederland bevestigt NOS dat AI-telefonisten zich voortaan direct moeten identificeren als AI — de nieuwe transparantieregel is inmiddels breed opgepikt in publieke berichtgeving. ([NOS](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven))

Een nieuw Europees onderzoeksnetwerk (EGDJ, initiatief RUG) onderzoekt de toepassing van AI in de rechtspraak — risico's en efficiëntiewinsten. ([Computable](https://www.computable.nl/2026/08/04/nieuw-europees-netwerk-onderzoekt-ai-in-de-rechtbank/))

## 🔐 Security & Risk

**Atlassian Rovo** kan via prompt injection worden misleid om Jira- en Confluence-data naar aanvallers door te sturen — een scherp voorbeeld van hoe enterprise AI-integraties nieuwe aanvalsvectoren creëren. ([The Hacker News](https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html))

Onderzoek bevestigt dat drie AI-coderingsagenten gevoelige secrets lekten via één enkele prompt injection-aanval, terwijl de system cards van de vendors de kwetsbaarheid al impliciet erkenden. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

OWASP: prompt injection is voor het tweede opeenvolgende jaar de #1 LLM-kwetsbaarheid. Succespercentages van aanvallen liggen op 50–80%, ook bij de meest geavanceerde modellen. De EU AI Act-deadline voor high-risk AI compliance (aug. 2026) vereist nu aantoonbare injectie­resistentie.

## 📈 Markt & Adoptie

**Microsoft** en **Google** domineren de enterprise AI-markt: Microsoft via Copilot en Azure (voordeel: eigenaar van OS en productiviteitssoftware), Google via Gemini en Google Cloud Agent Stack. Microsoft sloot FY26 af onder het motto "From AI Experimentation to Frontier Transformation." ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/), [Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/))

**SAP Business AI Platform** bundelt BTP, Data Cloud en AI tot één fundament met een Autonomous Suite die AI-agenten rechtstreeks in bestaande ERP-processen inbedt — end-to-end procesautomatisering zonder maatwerk­integraties. ([CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/))

**Rabobank** investeert de komende drie jaar tot €2 miljard in data-infrastructuur en AI; meer dan 27.000 medewerkers volgden al geavanceerde AI-trainingen. Benchmark voor hoe Nederlandse financials AI structureel inbedden. ([Computable](https://www.computable.nl/2026/08/05/rabobank-investeert-miljarden-in-it/))

Cloud capex van de hyperscalers groeit in 2026 naar bijna $600 miljard (+40%) — de infrastructuurrace om AI-capaciteit is in volle gang.

## 💡 Ctac-relevantie

**EU AI Act compliance is nú urgent voor klanten.** Handhaving is gestart; klanten in de publieke sector, finance en zorg die AI-systemen inzetten moeten aantonen dat ze aan transparantie- en risicobeheersverplichtingen voldoen. Ctac kan hier een concrete dienst op bouwen: compliance-quickscans en implementatie van vereiste documentatie en labeling. Lage investeringsdrempel, directe waarde.

**SAP Autonomous Suite** raakt direct aan Ctac's SAP-klantenbasis. Klanten die de stap willen zetten naar agentische ERP-automatisering hebben een integrator nodig die zowel SAP als AI begrijpt — een combinatie die Ctac kan bieden als die kennis tijdig wordt opgebouwd.

**Muse Glimmer (lokaal, open-source)** opent deuren bij klanten met strikte datavereisten (overheid, zorg) die cloud-AI weren. Een proof-of-concept met lokale deployment van een 30B-model kan voor deze groep overtuigend zijn.

**Atlassian-kwetsbaarheid** is een wake-up call: Ctac-klanten met Jira/Confluence + Rovo moeten worden gewezen op de patch- en configuratiestatus. Proactief klanten informeren bouwt vertrouwen als security-partner.

## 📚 Bronnen & verder lezen

- [OpenAI GPT-5.6 lancering – TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [Anthropic model en Riemann-hypothese – TechCrunch](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/)
- [Meta Muse Glimmer 30B – Hugging Face](https://huggingface.co/blog/muse-glimmer)
- [State of Open Models Summer 2026 – Hugging Face](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [EU AI Act handhaving gestart – Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [AI telefonist moet zich identificeren – NOS](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)
- [AI in de rechtbank – Computable](https://www.computable.nl/2026/08/04/nieuw-europees-netwerk-onderzoekt-ai-in-de-rechtbank/)
- [Atlassian Rovo kwetsbaarheid – The Hacker News](https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html)
- [AI agenten lekken secrets via prompt injection – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Microsoft vs Google enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [SAP Business AI Platform – CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [Microsoft FY26 terugblik – Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [Rabobank investeert miljarden in IT – Computable](https://www.computable.nl/2026/08/05/rabobank-investeert-miljarden-in-it/)
- [EU AI Act transparantie-eisen – Computable](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
