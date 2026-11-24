---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-16
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 16 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaving gestart (2 aug):** De Europese Commissie handhaaft vanaf 2 augustus actief de transparantieregels — chatbots en deepfakes moeten nu wettelijk herkenbaar zijn als AI. Boetes lopen op tot €35M of 7% van de wereldwijde omzet.
- **Meta lanceert Muse Glimmer (30B, open-weight):** Op 10 augustus lanceerde Meta een open-source model van 30 miljard parameters dat volledig lokaal op consumentenhardware draait en ontworpen is voor agentic taken — een serieuze concurrent voor closed API-modellen.
- **OpenAI GPT-5.6 Sol krijgt Ultrafast mode:** 14× snellere inferentie aangekondigd op 13 augustus voor het flagship Sol-model; ook beschikbaar op AWS Bedrock. De race om inference-snelheid is even belangrijk geworden als modelkwaliteit.
- **Microsoft bereikt 20M+ Copilot-seats:** AI-omzetrun rate overschrijdt $37 miljard (+123% YoY). Enterprise AI-adoptie accelereert sterk; Microsoft domineert, Google volgt op agentic AI.
- **AI-infrastructuuruitgaven overschrijden $1 biljoen:** Schaalgrens bereikt — hyperscalers investeren nu ook in forward-deployed engineering om enterprises daadwerkelijk tot adoptie te krijgen.

---

## 🧠 Technologie & Modellen

**Meta Muse Glimmer** is de open-weight versie van Meta's gesloten topmodel Muse Spark, uitgebracht op 10 augustus. Met 30B parameters kan het op één consumer-GPU (Mac/PC) draaien en tool-calling, code schrijven en debuggen uitvoeren — precies de agentic use cases die momenteel hoog op de enterprise-agenda staan. Dit verlaagt de instapdrempel voor on-premise AI-agents aanzienlijk.

**OpenAI GPT-5.6 Sol** kreeg een "Ultrafast mode" (13 aug) die verwerking tot 14× versnelt. De GPT-5.6-familie (Sol/Terra/Luna) is ook beschikbaar via AWS Bedrock. OpenAI experimenteert bovendien met advertenties in ChatGPT — een monetisatiestrategie die spanningen kan oproepen bij enterprise-klanten die datasensitiviteit bewaken.

**Claude Opus 5** (Anthropic, 24 juli) is het meest recente frontier-model van Anthropic: Fable 5-niveau intelligentie voor circa de helft van de prijs. Dit positioneert het als interessante optie voor kostenoptimalisatie bij high-volume toepassingen.

**Open-source landschap:** Kimi K2.6 wordt aangemerkt als een van de sterkste open-weight modellen voor developers in 2026, met name voor coding, tool-use en lange agentic workflows. Qwen3.8-27B is de meest recente release (14 aug) van de Qwen-serie.

*Bronnen: [TechCrunch – Meta Glimmer](https://techcrunch.com/2026/08/10/metas-new-glimmer-ai-model-offers-a-hint-at-zuckerbergs-personal-intelligence-vision/), [OpenAI News](https://openai.com/news/product-releases/), [AI Release Tracker](https://aireleasetracker.com/latest), [HuggingFace Blog – Open Source LLMs](https://huggingface.co/blog/daya-shankar/open-source-llms)*

---

## 🏛️ Governance & Ethiek

**EU AI Act handhaving begonnen op 2 augustus 2026.** De Europese Commissie treedt actief op. De nieuwe transparantievereisten verplichten AI-chatbots en deepfake-content zichzelf als zodanig te labelen. Sancties:
- Verboden AI-praktijken: tot **€35M of 7% van de wereldwijde omzet**
- Hoog-risico AI-systemen: tot €15M of 3% — de deadline voor hoog-risico-verplichtingen is echter verschoven naar **december 2027**, wat organisaties enige ademruimte geeft.

**AI Omnibus** (in werking getreden 27 juli) brengt gerichte vereenvoudiging: lagere nalevingslast voor mkb, maar met behoud van fundamentele veiligheids- en grondrechtenwaarborgen.

De combinatie van actieve handhaving + vereenvoudiging geeft een duidelijk signaal: de EU is niet aan het terugkrabbelen, maar probeert wel pragmatisch te zijn. Voor Ctac-klanten die AI-toepassingen hebben uitgerold, is compliance nu urgent.

*Bronnen: [Europese Commissie – AI Act handhaving](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august), [AI Omnibus](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force), [Computable.nl – transparantie-eisen](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)*

---

## 🔐 Security & Risk

**Prompt injection is het grootste AI-securityprobleem van dit moment.** Uit het CrowdStrike Global Threat Report 2026 blijkt dat aanvallers bij meer dan 90 organisaties kwaadaardige prompts in productieve enterprise AI-tools hebben geïnjecteerd. Het fundamentele probleem: LLM's maken geen onderscheid tussen data en instructies.

**EchoLeak (CVE-2025-32711, CVSS 9.3)** was de eerste gedocumenteerde zero-click prompt injection op een productiesysteem — Microsoft 365 Copilot. Eén kwaadaardig opgestelde e-mail was genoeg om Copilot interne bestanden te laten exfiltreren naar een externe server.

Met het groeiende gebruik van agentic AI (meer toolaccess, meer autonomie, diepere systeemintegraties) neemt het aanvalsoppervlak exponentieel toe. Het UK NCSC vergelijkt de ernst van prompt injection met SQL injection in de begintijd van webapplicaties.

*Bronnen: [VentureBeat – Prompt Injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers), [Airia – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)*

---

## 📈 Markt & Adoptie

**Microsoft** domineert de enterprise AI-markt met meer dan 20 miljoen Microsoft 365 Copilot-seats. De AI-omzetrun rate van $37 miljard groeide 123% jaar-op-jaar. Microsoft en Google worden door analisten als de twee topspelers gezien — Microsoft breed via het partner-ecosysteem, Google specifiek sterk op agentic AI.

**SAP** presenteert zijn nieuwe **Business AI Platform** — een unified platform dat Business Technology Platform, Data Cloud en AI samenvoegt — inclusief een **Autonomous Suite** die end-to-end procesautomatisering met AI-agents aan bestaande SAP-applicaties toevoegt. Koppelingen met Google Cloud, Microsoft en AWS voor agent-to-agent interoperabiliteit zijn uitgebreid.

**AI-infrastructuuruitgaven** overschreden wereldwijd de $1 biljoen grens (HPCwire, 4 aug). AWS en Microsoft investeren nu ook in "forward-deployed engineering" — directe on-site hulp bij adoptie — om het gat tussen investering en daadwerkelijk gebruik te dichten.

*Bronnen: [CIO Dive – Microsoft Copilot](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/), [CIO Dive – SAP AI Platform](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/), [HPCwire – AI infrastructure $1T](https://www.hpcwire.com/bigdatawire/2026/08/04/ai-infrastructure-spending-has-surpassed-1-trillion-heres-where-the-money-is-going-and-whats-next/), [VentureBeat – Nvidia enterprise agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)*

---

## 💡 Ctac-relevantie

**EU AI Act compliance is nu urgent voor klanten.** De handhaving begon op 2 augustus. Ctac-klanten die AI-toepassingen inzetten (chatbots, AI-gestuurde documentverwerking, assistenten) moeten nu voldoen aan de transparantievereisten. Dit is een directe adviesopportunity: Ctac kan compliance-scans, labeling-implementaties en governance-frameworks aanbieden. Hoog-risico AI heeft tot december 2027, maar wacht niet te lang.

**SAP Business AI Platform** is direct relevant voor Ctac's SAP-klanten. De nieuwe Autonomous Suite maakt het mogelijk om bestaande SAP-processen te automatiseren met AI-agents — een concreet verkoopgesprek voor klanten in finance, overheid en industrie die SAP S/4HANA gebruiken.

**Prompt injection is nu een acuut risico voor Copilot-klanten.** Gezien het EchoLeak-incident en de schaal van aanvallen (90+ organisaties) is een security-review van enterprise AI-deployments — met name Microsoft 365 Copilot — een logische stap voor klanten die Ctac begeleid heeft bij implementatie.

**Meta Glimmer opent de deur voor on-premise AI-agents.** Een 30B open-weight model dat lokaal draait verlaagt de drempel voor klanten met dataprivacy-eisen (overheid, zorg) die nu terughoudend zijn met cloud-AI. Dit is een argument voor een lokale AI-pilot.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Meta Muse Glimmer lancering](https://techcrunch.com/2026/08/10/metas-new-glimmer-ai-model-offers-a-hint-at-zuckerbergs-personal-intelligence-vision/)
- [OpenAI Product Releases](https://openai.com/news/product-releases/)
- [Europese Commissie – AI Act handhaving gestart 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [AI Omnibus in werking](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force)
- [Computable.nl – EU AI Act transparantie-eisen](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [Airia – AI Security 2026: Prompt Injection & The Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Microsoft domineert enterprise AI-markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – SAP Business AI Platform](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [HPCwire – AI infrastructuuruitgaven $1 biljoen](https://www.hpcwire.com/bigdatawire/2026/08/04/ai-infrastructure-spending-has-surpassed-1-trillion-heres-where-the-money-is-going-and-whats-next/)
- [HuggingFace – Best Open-Source LLM Models 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [AI Release Tracker – augustus 2026](https://aireleasetracker.com/latest)
