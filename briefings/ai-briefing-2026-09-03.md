---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-03
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 3 september 2026

## 🔑 Highlights van de dag

- **EU AI Act: handhaving nu actief.** Sinds 2 augustus 2026 handhaven de Europese AI Office en nationale autoriteiten de AI Act. Met de AI Omnibus (van kracht per 27 juli 2026) is toezicht op GPAI-modellen gecentraliseerd – compliance is geen toekomstzorg meer.
- **Meta lanceert Muse Glimmer.** Een 30B multimodaal open-sourcemodel, gedestilleerd uit het grotere Muse-model en uitgebracht onder Apache 2.0-licentie. Specifiek ontworpen voor lokale, agentische toepassingen – een directe aanval op closed-model dominantie in productie.
- **AI gebruikt om PLC-exploit te porten.** Onderzoekers gebruikten Claude om een pre-auth RCE-exploit over te zetten naar een ander PLC-model – een signaal dat AI-geassisteerde aanvallen op industriële systemen snel praktischer worden.
- **SAP lanceert Business AI Platform.** SAP verenigt BTP, Data Cloud en AI-aanbod onder één platform, inclusief de nieuwe Autonomous Suite met AI agents voor end-to-end procesautomatisering.
- **Big Tech waarschuwt voor AI-dreiging op kritieke infrastructuur.** Meer dan honderd techbedrijven roepen op tot betere beveiliging, terwijl slechts 27% van IT security-beslissers zegt klaar te zijn voor een grote aanval.

---

## 🧠 Technologie & Modellen

**Meta Muse Glimmer (30B)** – uitgebracht vandaag op Hugging Face, Apache 2.0. Multimodaal, lokaal inzetbaar, en geoptimaliseerd voor agentische workflows. Dit is de meest directe bedreiging voor closed modellen in enterprise-omgevingen waar datasovereiniteit belangrijk is. ([Hugging Face](https://huggingface.co/blog/muse-glimmer))

**Open-source LLMs rijp voor productie.** Hugging Face's zomereditie van "State of Open Models" concludeert: voor coding, reasoning, long-context en local deployment zijn open-weight modellen in 2026 serieus productiegereed. Kleine modellen (<1B parameters) domineren downloads met 83% aandeel – dat zegt iets over hoe de markt ze inzet: embedded, on-device. ([Hugging Face](https://huggingface.co/blog/state-of-open-models-summer-2026))

**Frontier AI en kwetsbaarheidsonderzoek.** Frontier-modellen zoals Anthropic's Mythos kunnen zero-day kwetsbaarheden identificeren, complexe exploits samenstellen en zich in real time aanpassen. Het dubbele karakter hiervan – nuttig voor offensief security research, gevaarlijk in verkeerde handen – is nu praktijkwerkelijkheid. ([The Hacker News](https://thehackernews.com/2026/08/frontier-ai-vulnerability-managements.html))

---

## 🏛️ Governance & Ethiek

**EU AI Act handhaving actief** – De AI Office, de Europese Toezichthouder voor Gegevensbescherming en nationale autoriteiten handhaven nu actief. De AI Omnibus (politiek akkoord 7 mei 2026, van kracht 27 juli) centraliseert GPAI-toezicht, vermindert fragmentatie en verlicht eisen voor kleine midcap-bedrijven. Regels voor hoog-risico AI-systemen (Bijlage III) gelden pas per 2 december 2027 – maar compliance-voorbereiding moet nu beginnen. ([EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/))

**NL: kabinet overweegt blokkade AI-overnames.** Het kabinet heeft wetgeving in voorbereiding waarmee AI-overnames door entiteiten uit 'niet-bevriende landen' geblokkeerd kunnen worden. Geopolitiek risicodenken sijpelt verder door in technologiebeleid. ([Computable](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/))

---

## 🔐 Security & Risk

**AI-assisted PLC exploit-porting.** Onderzoekers porteerden een pre-auth RCE-exploit van het ene PLC-model naar het andere met behulp van Claude – wat voorheen dagen of weken vergde, duurt nu uren. Dit is geen hypothetisch risico meer voor OT/ICS-omgevingen. ([The Hacker News](https://thehackernews.com/2026/09/researchers-use-claude-to-port-pre-auth.html))

**Enterprise AI governance-kloof.** Twee derde van organisaties heeft AI uitgerold zonder volwassen governance. 73% van IT security-beslissers erkent niet klaar te zijn voor een significante cyberaanval. Gemiddelde remediatietijd voor bekende critical CVE's: 74 dagen. 45% wordt nooit gepatcht. ([The Hacker News](https://thehackernews.com/2026/09/how-to-secure-enterprise-ai-from.html))

**NL/BE: meer cyberaanvallen door AI.** Datanews bevestigt een toename van AI-gedreven aanvallen in Nederland en België, parallel aan de mondiale trend. ([Datanews](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/))

---

## 📈 Markt & Adoptie

**Microsoft domineert enterprise AI-markt.** Microsoft 365 Copilot heeft meer dan 20 miljoen betaalde seats. De AI-omzetrun-rate groeide 123% YoY naar $37 miljard. Microsoft en Google delen de marktleiding in enterprise AI, met AWS als derde. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

**Google Agentic Data Cloud.** Google Cloud presenteerde een AI-native architectuur die legacy data platforms omzet in reasoning engines met universele business-context voor AI agents – een directe aanval op de data-silo-problematiek bij enterprise-klanten. ([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))

**SAP Business AI Platform + Autonomous Suite.** SAP verenigt zijn complete aanbod (BTP, Data Cloud, AI) en voegt agentic procesautomatisering toe. Dit is relevant voor de 60–70% van Europese enterprise-klanten die SAP draaien. ([CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/))

**Pilot-fase bottleneck.** Twee derde van organisaties zit vast in proof-of-concept en komt niet in productie. De investeringen gaan omhoog, de resultaten nog niet. Dit is een structureel marktprobleem – en een kans voor adviseurs en implementatiepartners.

---

## 💡 Ctac-relevantie

**SAP Autonomous Suite is acuut relevant.** Ctac heeft een stevige SAP-praktijk. De lancering van SAP's agentische procesautomatisering is geen toekomstmuziek – het staat nu in de roadmap van klanten. Ctac moet een concreet standpunt ontwikkelen: welke SAP-processen zijn rijp voor agent-automatisering, en hoe positioneer je dat naar klanten?

**Pilot-stagnatie = implementatieopportunity.** Twee derde van enterprises zit vast in pilots. Ctac kan zich positioneren als de partner die AI van experiment naar productie brengt – maar dan moeten interne accelerators en referentiecases beschikbaar zijn.

**EU AI Act compliance wordt urgenter.** De handhaving is actief. Klanten in gereguleerde sectoren (overheid, zorg, finance) hebben nu concrete verplichtingen. Ctac's AI-unit kan compliance-assessments en implementatiebegeleiding aanbieden als directe propositie, zeker in combinatie met bestaande klantrelaties.

**Security als gespreksopener.** De combinatie van AI-gedreven aanvallen en governance-kloven bij enterprises biedt Ctac een betrouwbaar gespreksonderwerp bij klanten. Niet als angstmarketing, maar als eerlijk risicogesprek: waar zitten de blinde vlekken in hun AI-governance?

**Open-source overweging voor kostenoptimalisatie.** Muse Glimmer (Apache 2.0, 30B, lokaal) maakt het voor klanten met strenge datasovereniteitseisen realistisch om krachtige AI on-premise of in eigen cloud te draaien. Voor Ctac een argument om open-source naast closed modellen aan te bieden in klantproposities.

---

## 📚 Bronnen & verder lezen

- [Meta Muse Glimmer – Hugging Face](https://huggingface.co/blog/muse-glimmer)
- [State of Open Models: Summer 2026 – Hugging Face](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [EU AI Act implementatie-tijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act governance & handhaving – EC](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Researchers Use Claude to Port PLC Exploit – The Hacker News](https://thehackernews.com/2026/09/researchers-use-claude-to-port-pre-auth.html)
- [How to Secure Enterprise AI – The Hacker News](https://thehackernews.com/2026/09/how-to-secure-enterprise-ai-from.html)
- [Frontier AI & Vulnerability Management – The Hacker News](https://thehackernews.com/2026/08/frontier-ai-vulnerability-managements.html)
- [Microsoft & Google rule AI market – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [SAP Business AI Platform – CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Big Tech waarschuwt voor AI-dreiging op kritieke infrastructuur – Computable](https://www.computable.nl/2026/09/01/big-tech-luidt-noodklok-ai-bedreigt-kritieke-infrastructuur/)
- [Meer cyberaanvallen door AI in NL/BE – Datanews](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
- [NL kabinet blokkade AI-overnames – Computable](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/)
