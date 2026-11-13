---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-18
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 18 september 2026

## 🔑 Highlights van de dag

- **OpenAI lanceert GPT-6 Astra** – het meest controversiële model tot nu toe: extreem hoge benchmarkscores (100% op ExploitBench, 96% GPQA Diamond), maar de "opaque recurrence"-techniek maakt chain-of-thought-auditing onmogelijk. OpenAI noemt het zelf het begin van het AGI-tijdperk; critici wijzen op fundamentele veiligheidsrisico's.
- **EU AI Act actief gehandhaafd** – sinds 2 augustus zijn de transparantieregels van kracht: chatbots moeten zichzelf als AI identificeren, deepfakes moeten worden gelabeld. Volgende deadline: 2 december 2026 (verbod op niet-consensuele intieme content).
- **PrismML's Bonsai 2** – een 5,9 GB-model dat 98% van Qwen3.8 27B's benchmarks behaalt; een bewijs dat het efficiëntierace met kleine modellen doorzet naast de AGI-race.
- **Prompt injection: structurele enterprise-dreiging** – drie AI-coding-agents lekten secrets via één prompt injection (VentureBeat); EchoLeak-paper documenteert eerste zero-click exploit in productie. Het is OWASP's #1 LLM-kwetsbaarheid en blijft structureel onopgelost.
- **Microsoft Copilot overschrijdt 20 miljoen betaalde seats** – AI-omzet +123% YoY, >$37 mrd ARR. Enterprise-adoptie versnelt, maar twee derde van bedrijven zit nog vast in de pilotfase.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-6 Astra** is gelanceerd als het "AGI-niveau model" met indrukwekkende benchmarkresultaten: 97,6% op FrontierMath Tier 4, 100% op ExploitBench en 98,6% op ARC-AGI-3. Vooralsnog beschikbaar via het Daybreak-cybersecurityprogramma en binnenkort via Pro/Plus/Enterprise-abonnementen en de API. De keerzijde: de *opaque recurrence*-techniek maakt externe audit van het redeneerproces nagenoeg onmogelijk, wat veiligheidsonderzoekers alarmeert.

**PrismML Bonsai 2 (27B)** comprimeert het Qwen3.8 27B-model naar 5,9 GB met slechts 2% benchmarkverlies. Dit past in de bredere trend: open/kleine modellen worden snel beter terwijl frontier-modellen recordbenchmarks behalen. Het gat tussen "bereikbaar" en "state-of-the-art" verkleint.

**Betrouwbaarheidsprobleem**: VentureBeat rapporteert dat frontier-modellen bij één op de drie productietaken falen. Stijgende benchmarkscores vertalen zich dus niet automatisch naar productiebetrouwbaarheid – een kritisch aandachtspunt voor enterprise-implementaties.

*Bronnen: [TechCrunch – Astra](https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/) | [VentureBeat – GPT-6 Astra AGI](https://venturebeat.com/technology/welcome-to-the-agi-era-openai-launches-gpt-6-astra) | [TechCrunch – PrismML](https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai/) | [VentureBeat – AI reliability](https://venturebeat.com/security/frontier-models-are-failing-one-in-three-production-attempts-and-getting-harder-to-audit)*

---

## 🏛️ Governance & Ethiek

**EU AI Act – handhaving actief**: sinds 2 augustus 2026 zijn de transparantieverplichtingen van kracht. Systemen die interacteren met mensen moeten zichzelf als AI kenbaar maken; synthetische content moet worden gemarkeerd. De AI Office van de Europese Commissie kan nu technische documentatie opvragen, modellen evalueren en boetes opleggen. Volgende mijlpaal: 2 december 2026 – verbod op generatie van niet-consensueel intiem materiaal en CSAM.

**Nederland – WBSO verruimd voor AI**: het kabinet breidde per 16 september de WBSO-regeling uit zodat ondernemers die software ontwikkelen *in relatie tot AI* sneller gebruik kunnen maken van de fiscale stimulering. De innovatiebox voor het mkb gaat volgend jaar omhoog van €25.000 naar €100.000. Een concreet fiscaal voordeel voor Nederlandse AI-softwarebedrijven.

**"Vlam" – soeverein AI-platform rijksoverheid**: SSC-ICT en AIVD-ontwikkeld Veilige Lokale AI Modellen-platform gaat in H2 2026 breed uitgerold worden bij de rijksoverheid. NOS rapporteert tegelijkertijd dat de overheid "volop gebruikmaakt van AI, maar vaak niet naar risico's kijkt."

*Bronnen: [EU AI Act enforcement](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [Computable – WBSO AI](https://www.computable.nl/2026/09/16/wbso-wordt-opgerekt-voor-software-ontwikkeling-met-ai/) | [NOS – overheid AI-risico](https://nos.nl/artikel/2540979-overheid-maakt-volop-gebruik-van-ai-maar-kijkt-vaak-niet-naar-risico-s)*

---

## 🔐 Security & Risk

**Prompt injection: structureel en groeiend probleem**. Drie AI-coding-agents lekten geheimen via één geïnjecteerde prompt – VentureBeat publiceerde een uitgebreide audit van system cards en veiligheidsdocumenten. EchoLeak (arXiv) is de eerste gedocumenteerde zero-click prompt injection exploit in een productie-LLM-omgeving. Microsoft patcht regelmatig Copilot Studio-kwetsbaarheden (recent CVE-2026-21520, CVSS 7.5), maar exfiltratie van data bleef mogelijk ondanks de patch.

OpenAI erkent openlijk dat prompt injection "waarschijnlijk nooit volledig opgelost kan worden." OWASP rankt het als #1 LLM-kwetsbaarheid; het UK NCSC schat de ernst hoger dan SQL-injection.

Bijkomende zorg: GPT-6 Astra scoort 100% op ExploitBench – het model is dus bijzonder goed in het exploiteren van computersystemen. Dit bevestigt het dual-use-risico van frontier-modellen.

*Bronnen: [VentureBeat – agent secrets leak](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [VentureBeat – Copilot Studio patch](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook) | [EchoLeak paper](https://arxiv.org/pdf/2509.10540) | [VentureBeat – prompt injection enterprise](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)*

---

## 📈 Markt & Adoptie

**Microsoft** overschrijdt 20 miljoen betaalde Copilot-seats en rapporteert een AI-omzet-ARR van >$37 mrd (+123% YoY). Gartner bestempelt Microsoft als marktleider voor enterprise AI in breedte, en Google als marktleider in agentic AI-stacks.

**Hyperscaler-investering**: Microsoft, Google en AWS investeren in FY2026 samen >$500 mrd in datacenter-infrastructuur voor AI. De race om capaciteit gaat onverminderd door.

**Adoptieknelpunt**: twee derde van bedrijven zit gevangen in de pilotfase en slaagt er niet in GenAI naar productie te brengen. Ondanks oplopende licentie-uitgaven blijft concrete waarderealisatie achter.

**UN × Google**: de VN schakelt Google in om haar wereldwijde datasets klaar te maken voor AI-agents – een markant signaal dat agentic AI nu ook op multilateraal niveau serieus genomen wordt.

*Bronnen: [CIO Dive – Microsoft Copilot](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/) | [CIO Dive – Microsoft/Google marktleiders](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [TechCrunch – UN Google](https://techcrunch.com/2026/09/17/un-turns-to-google-to-make-its-global-data-ready-for-ai-agents/)*

---

## 💡 Ctac-relevantie

**WBSO-kans voor AI-softwareontwikkeling**: de uitbreiding van de WBSO-regeling is direct relevant. Als Ctac custom AI-software bouwt voor klanten, kunnen deze ontwikkelkosten fiscaal gestimuleerd worden. Bespreek dit intern met finance en de AI-unit-opbouw.

**Productie-gap als propositiekans**: het gegeven dat 2/3 van bedrijven niet uit de pilotfase komt, is precies de ruimte waar Ctac als implementatiepartner waarde kan leveren. De marktbehoefte is: begeleiding van pilot naar schaalbare productie-inzet, niet nog een demo. Positioneer Ctac hier concreet.

**Prompt injection is nu een enterprise-compliancevraagstuk**: met de EU AI Act actief gehandhaafd worden veiligheidsvereisten voor high-risk AI-systemen strenger. Klanten die agentic AI inzetten moeten prompt injection aantoonbaar adresseren. Ctac kan hier een beveiligingsassessment en implementatiestandaard als dienst positioneren.

**Astra/AGI-hype: kritisch blijven**: OpenAI's AGI-claim verdient scepsis. De auditblokkering via opaque recurrence is een rode vlag voor enterprise-inzet. Adviseer klanten om Astra nog niet in productieve omgevingen te gebruiken totdat onafhankelijke audits beschikbaar zijn.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI lanceert Astra](https://techcrunch.com/2026/09/03/openai-launches-astra-its-powerful-and-controversial-new-model/)
- [VentureBeat – GPT-6 Astra: Welcome to the AGI era](https://venturebeat.com/technology/welcome-to-the-agi-era-openai-launches-gpt-6-astra)
- [TechCrunch – Astra en cybersecurity-risico](https://techcrunch.com/2026/09/01/open-ais-astra-model-is-on-the-way-and-very-good-at-breaking-into-computer-systems/)
- [TechCrunch – PrismML Bonsai 2](https://techcrunch.com/2026/09/17/prismml-hopes-its-tiny-llm-could-change-how-we-all-use-ai/)
- [VentureBeat – AI reliability: 1 op 3 mislukt in productie](https://venturebeat.com/security/frontier-models-are-failing-one-in-three-production-attempts-and-getting-harder-to-audit)
- [EU AI Act enforcement – Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [Computable – WBSO verruimd voor AI](https://www.computable.nl/2026/09/16/wbso-wordt-opgerekt-voor-software-ontwikkeling-met-ai/)
- [NOS – Overheid en AI-risico's](https://nos.nl/artikel/2540979-overheid-maakt-volop-gebruik-van-ai-maar-kijkt-vaak-niet-naar-risico-s)
- [VentureBeat – Prompt injection: enterprise design flaw](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – AI agent secrets leak via prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [arXiv – EchoLeak zero-click exploit](https://arxiv.org/pdf/2509.10540)
- [CIO Dive – Microsoft Copilot seats Q3 2026](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [CIO Dive – Microsoft/Google leiden AI-markt enterprise](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [TechCrunch – UN × Google AI-agents](https://techcrunch.com/2026/09/17/un-turns-to-google-to-make-its-global-data-ready-for-ai-agents/)
