---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-12
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 12 april 2026

## 🔑 Highlights van de dag

- **Anthropic houdt sterkste model achter slot** – Claude Mythos, het krachtigste model dat Anthropic ooit bouwde, wordt niet openbaar gemaakt. Slechts 50 organisaties krijgen via "Project Glasswing" toegang – uitsluitend voor defensieve kwetsbaarheidsscans van eigen infrastructuur.
- **EU Digital Omnibus nadert beslissend moment** – Op 28 april vindt de tweede triloog plaats over de voorgestelde wijzigingen op de AI Act. De uitkomst bepaalt mede welke verplichtingen per 2 augustus 2026 van kracht worden voor aanbieders en afnemers van hoog-risico AI.
- **Prompt injection nu officieel het grootste AI-veiligheidsrisico** – OWASP classificeert prompt injection als de hoogst-risico kwetsbaarheid voor LLM-systemen; aanvallen stegen met 340% dit jaar. Indirect injection (via documenten, e-mails, APIs) is inmiddels verantwoordelijk voor meer dan 80% van de aanvallen.
- **Agentic AI verschuift van pilot naar productie** – 72% van de Global 2000-bedrijven heeft AI-agentsystemen operationeel buiten de experimenteerfase. Tegelijk worstelt twee derde van bedrijven nog met de overgang van pilot naar productie.
- **NVIDIA lanceert enterprise agent-platform** – Met Adobe, SAP en Salesforce als early adopters brengt NVIDIA zijn Agent Toolkit op de markt: een gecombineerde stack van modellen, runtime en beveiliging voor enterprise agent-deployments.

---

## 🧠 Technologie & Modellen

Het modellandschap blijft in hoog tempo bewegen. **Google Gemini 3.1 Pro** staat op dit moment bovenaan de reasoning-benchmarks met 94,3% op GPQA Diamond. **OpenAI GPT-5.4** (uitgebracht in maart) scoort recordwaarden op computer-use benchmarks en GPT-5.5 (codenaam: Spud) ligt klaar voor een Q2-aankondiging. **Anthropic Claude Sonnet 4.6** leidt de real-world work-evaluaties (GDPval-AA Elo: 1.633 punten) en biedt near-Opus-kwaliteit op Sonnet-prijsniveau — praktisch relevant voor productie-inzet.

Opvallend is Claude Mythos: Anthropic bevestigt dat dit model bestaat maar het niet publiek beschikbaar stelt. De vijftig organisaties die toegang krijgen, mogen het uitsluitend defensief inzetten. Dit is minder marketingzet en meer een signaal dat frontier-modellen nu serieus worden ingezet voor infrastructuurbeveiliging.

**xAI** introduceerde Grok 4.20 met een nieuwe multi-agent architectuur. **OpenAI Aardvark** is een autonoom security research-agent (gebouwd op GPT-5) die softwarekwetsbaarheden zelfstandig ontdekt en patcht.

De oprichting van de **Agentic AI Foundation (AAIF)** door OpenAI, Anthropic en Block onder de Linux Foundation is strategisch: neutrale governance voor interoperabele agent-infrastructuur, vergelijkbaar met hoe Linux de servermarkt normaliseerde.

*Bronnen: [llm-stats.com](https://llm-stats.com/ai-news), [whatllm.org](https://whatllm.org/blog/new-ai-models-april-2026), [openai.com/index/introducing-aardvark](https://openai.com/index/introducing-aardvark/), [openai.com/index/agentic-ai-foundation](https://openai.com/index/agentic-ai-foundation/), [venturebeat.com](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)*

---

## 🏛️ Governance & Ethiek

De **EU AI Act-tijdlijn** nadert een kritieke fase. Op **2 augustus 2026** worden de meeste resterende regels van kracht — inclusief de verplichtingen voor hoog-risico AI-systemen en transparantie-eisen. In Nederland en België is het overgrote deel van de publieke sector en zorginstellingen nog niet compliant-ready.

De **EU Digital Omnibus**-onderhandelingen lopen parallel: op 28 april vindt de tweede triloog plaats. De Raad en het Parlement hebben hun posities ingenomen; mogelijke aanpassingen raken de compliance-planning van organisaties die al volop bezig zijn met implementatie.

In de **Benelux** is het adoptiecijfer indrukwekkend: 67% van Nederlandse bedrijven gebruikt AI in 2026, verdubbeld ten opzichte van 34% in 2023. Tegelijkertijd rapporteert ICT Magazine dat Benelux-organisaties disproportioneel bezorgd zijn over dataprivacy — 12 procentpunt boven het mondiale gemiddelde. Vertrouwen in AI-besluitvorming blijft laag.

Aandachtspunt voor de komende weken: **agentic AI en governance**. Multi-agent-systemen vallen mogelijk onder aanvullende verplichtingen wanneer ze als 'general purpose AI' worden geclassificeerd. De rechtspositie is nog onduidelijk, maar de richting van de regelgever is dat meer autonomie = meer verantwoordelijkheid.

*Bronnen: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/), [onetrust.com](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/), [cryptobenelux.com](https://cryptobenelux.com/kunstmatige-intelligentie/ai-act-raakt-in-2026-vooral-hr-onderwijs-en-overheid-in-nederland-en-belgie), [ictmagazine.nl](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)*

---

## 🔐 Security & Risk

**Prompt injection is het nieuwe SQL-injection** — dat is de heldere boodschap van meerdere beveiligingsrapporten deze week. OWASP's LLM Security Project plaatst het boven data poisoning en model theft als hoogst-risico kwetsbaarheid. CIS publiceerde een waarschuwingsrapport specifiek gericht op organisaties die GenAI inzetten.

Twee ontwikkelingen vragen extra aandacht:

1. **Indirect injection domineert**: aanvallen via ingested content (e-mails, documenten, databaseinhoud, webpagina's) overtreffen directe aanvallen met 4:1. Elk nieuw extern systeem dat een AI-agent mag lezen verhoogt het aanvalsoppervlak met een factor 3–5.
2. **AI in de overheid**: Help Net Security rapporteert dat GenAI nu dagelijks in gebruik is bij overheidsdiensten, zonder dat prompt injection afdoende is gemitigeerd. Bijzonder relevant voor klanten in de publieke sector.

OpenAI Aardvark is een tweerichtingszwaard: hetzelfde framework dat kwetsbaarheden patcht, kan ook worden ingezet voor aanvallen. De vraag wie dit soort tools kan inzetten — en onder welke condities — wordt urgenter.

*Bronnen: [airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/), [cisecurity.org](https://www.cisecurity.org/about-us/media/press-release/new-cis-report-warns-prompt-injection-attacks-pose-growing-risk-to-generative-ai), [helpnetsecurity.com](https://www.helpnetsecurity.com/2026/04/09/genai-prompt-injection-enterprise-data-risk/), [markaicode.com](https://markaicode.com/prompt-injection-attacks-ai-security-2026/)*

---

## 📈 Markt & Adoptie

De cloudinfrastructuur draait op volle toeren: **Microsoft Azure groeide 39% YoY** in Q4 2025, **Google Cloud 50%**. Gartner benoemt Microsoft, Google en OpenAI als de drie dominante AI-platforms voor enterprise.

De agentic AI-markt wordt geprojecteerd op **$139 miljard in 2034** (van $9,1 miljard nu), met een CAGR van 40,5%. NVIDIA's Agent Toolkit en Microsofts Azure AI Foundry voor agentische cloud-operaties versterken de vendor lock-in-dynamiek. Kai Waehner analyseert dat **vertrouwen en vendor lock-in** de twee meest kritische spanning spunten worden in enterprise AI-architectuurbeslissingen voor 2026.

Opvallend: **twee derde van bedrijven** zit nog vast in generatieve AI-pilotfases en worstelt met de transitie naar productie. Dit is het meest concrete opportuniteitsvenster voor IT-dienstverleners: de kloof tussen "we doen pilots" en "we hebben schaalbare AI in productie" is groot en duur om zelf te overbruggen.

*Bronnen: [ciodive.com](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/), [kai-waehner.de](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/), [insights.reinventing.ai](https://insights.reinventing.ai/articles/openclaw-enterprise-adoption-march-2026-03-16), [omdia.tech.informa.com](https://omdia.tech.informa.com/pr/2026/mar/global-cloud-infrastructure-spending-rose-29percent-in-q4-2025-as-hyperscalers-scaled-ai-infrastructure-investment)*

---

## 💡 Ctac-relevantie

**1. EU AI Act deadline = concrete klantvraag.** 2 augustus 2026 is vier maanden weg. Ctac's klanten in de publieke sector (gemeenten, uitvoeringsorganisaties) en zorg zijn verplicht hun hoog-risico AI te documenteren, testen en registreren. Dit is een directe advies- en implementatieopgave waar Ctac nu op in kan spelen — compliance-scans, risicoklassificaties en AI-registerimplementaties zijn concrete proposities.

**2. Pilot-naar-productie als kern van de AI-propositie.** Twee derde van enterprise-klanten zit vast in pilots. Ctac's meerwaarde zit niet in het bouwen van het honderdste GenAI-prototype, maar in het succesvol naar productie brengen ervan: integratiewerk, beveiliging, monitoring, change management. Dit onderscheidt Ctac van hyperscaler-resellers.

**3. Agentic AI security meenemen in elk nieuw project.** Indirect prompt injection is nu de dominante aanvalsvector. Bij elke opdracht waarbij agents externe data verwerken (e-mail, documenten, databases) moet security-by-design onderdeel zijn van de technische aanpak. Dit is ook een argument richting klanten om niet blindelings op low-code agent-platforms te vertrouwen zonder beveiligingslaag.

**4. Vendor lock-in als strategisch adviesthema.** Met NVIDIA, Microsoft en Google die elk hun eigen agent-stacks pushen, wordt architectuuronafhankelijkheid een klantbehoefte. Ctac kan zich positioneren als de neutrale partij die klanten helpt een future-proof AI-architectuur op te zetten zonder onnodige afhankelijkheden.

---

## 📚 Bronnen & verder lezen

- [llm-stats.com – AI model updates april 2026](https://llm-stats.com/ai-news)
- [whatllm.org – New AI models april 2026](https://whatllm.org/blog/new-ai-models-april-2026)
- [artificialintelligenceact.eu – Implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [onetrust.com – EU Digital Omnibus en AI Act](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/)
- [legalnodes.com – EU AI Act 2026 compliance](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [airia.com – AI security & prompt injection 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [cisecurity.org – CIS report prompt injection](https://www.cisecurity.org/about-us/media/press-release/new-cis-report-warns-prompt-injection-attacks-pose-growing-risk-to-generative-ai)
- [helpnetsecurity.com – GenAI in overheid en prompt injection](https://www.helpnetsecurity.com/2026/04/09/genai-prompt-injection-enterprise-data-risk/)
- [ciodive.com – Microsoft en Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [kai-waehner.de – Enterprise agentic AI landscape 2026](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)
- [openai.com – Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/)
- [venturebeat.com – NVIDIA enterprise agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [cryptobenelux.com – AI Act impact NL/BE](https://cryptobenelux.com/kunstmatige-intelligentie/ai-act-raakt-in-2026-vooral-hr-onderwijs-en-overheid-in-nederland-en-belgie)
- [ictmagazine.nl – AI-adoptie Benelux](https://www.ictmagazine.nl/nieuws/onderzoek-ai-adoptie-benelux-veel-veiligheid-weinig-vertrouwen-in-besluitvorming/)
