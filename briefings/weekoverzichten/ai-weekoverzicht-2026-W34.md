---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W34
Periode: 2026-08-17 / 2026-08-23
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 34 (17–23 augustus 2026)

### Maandag 17 augustus
→ Dagbriefing: [ai-briefing-2026-08-17.md](../ai-briefing-2026-08-17.md)

**Highlights:**
- **EU AI Act handhaving actief:** Transparantievereisten zijn per 2 augustus afdwingbaar — chatbots moeten zich als AI kenbaar maken, deepfakes verplicht gelabeld. De AI Omnibus verlengt de deadline voor hoog-risico systemen naar december 2027, maar compliance is nu al verplicht voor Artikel 50-toepassingen.
- **DeepSeek V4 Pro + Harness gelanceerd:** DeepSeek introduceert een open-source coding agent als alternatief voor Claude Code en stapt over op piek/dalprijs-model (per 16 aug). Met 7–17× kostenvoordeel t.o.v. Claude Sonnet en GPT-5.5 en 23% enterprise token-marktaandeel verstoort DeepSeek de vendor-verhoudingen structureel.
- **Prompt injection treft Claude Code, Gemini CLI en Copilot tegelijk:** Één aanval lekte secrets via drie coding agents. Het onderliggende probleem — modellen kunnen instructies en data niet onderscheiden — is architectureel, niet eenvoudig te patchen.

**Ctac-relevantie van de dag:** De combinatie van EU AI Act-handhaving (Artikel 50 direct afdwingbaar), DeepSeek als prijsverstoorder en agentic AI-beveiligingsincidenten maakt dit een cruciale week voor klantadvies op drie fronten: compliance-assessment, vendor-herafweging en security-architectuur voor agentic pipelines.

---

### Dinsdag 18 augustus
→ Dagbriefing: [ai-briefing-2026-08-18.md](../ai-briefing-2026-08-18.md)

**Highlights:**
- **EU AI Act handhaving: AI-telefonisten moeten zich direct identificeren** — NOS en Computable berichten dat de transparantieverplichting breed wordt opgepikt; consumenten én bedrijven krijgen nu rechtsbescherming bij AI-interacties.
- **Meta Muse Glimmer 30B gelanceerd (Apache 2.0):** Een lokaal draaiend open-source model met agentische capaciteiten en multimodaliteit — direct concurrent voor cloud-gebaseerde AI, met grote gevolgen voor on-premise deployment bij overheid en finance.
- **Atlassian Rovo kwetsbaar voor prompt injection:** Aanvallers kunnen Jira/Confluence-data exfiltreren via één aanval. OWASP bevestigt: prompt injection blijft de #1 LLM-kwetsbaarheid — enterprise AI-integraties creëren nieuwe aanvalsvectoren.

**Ctac-relevantie van de dag:** De EU AI Act-handhaving maakt compliance-assessments urgent voor klanten met AI-klantcontact. Tegelijkertijd opent Muse Glimmer kansen voor Ctac bij privacy-bewuste klanten die cloud-AI mijden. De Atlassian-kwetsbaarheid vraagt om proactieve klantcommunicatie als security-partner.

---

### Woensdag 19 augustus
→ Dagbriefing: [ai-briefing-2026-08-19.md](../ai-briefing-2026-08-19.md)

**Highlights:**
- **EU AI Act transparantievereisten van kracht:** Handhaving gestart 2 augustus — chatbots moeten zich identificeren als AI, deepfakes verplicht gelabeld. De AI Office én nationale autoriteiten hebben nu afdwingbevoegdheden; hoog-risico systemen (Annex I) krijgen uitstel tot augustus 2028 via de AI Omnibus.
- **Google Gemini 3.7 Flash en OpenAI Ultrafast mode:** Google's coding benchmark steeg in drie weken van 34% naar 44%; OpenAI's GPT-5.6 Sol draait nu op 750 tokens/seconde (14× sneller) via Cerebras. De modelrace en infrastructuursnelheid versnellen tegelijkertijd.
- **Stripe koopt OpenRouter voor $7 miljard:** Model-routing voor 400+ LLMs landt in betalingsinfrastructuur — betalingen en AI-orkestratie convergeren, met grote implicaties voor developer-tooling en enterprise AI-stacks.

**Ctac-relevantie van de dag:** De EU AI Act-handhaving is nu volledig actief: compliance-trajecten voor klanten met chatbots en generatieve AI zijn urgent. Twee derde van bedrijven zit nog vast in de pilot-fase — dit is de openingsmarkt voor Ctac als productie-enabler. Meta Muse Glimmer (Apache 2.0, lokaal) biedt kansen bij privacy-bewuste klanten in overheid, zorg en finance.

---

### Donderdag 20 augustus
→ Dagbriefing: [ai-briefing-2026-08-20.md](../ai-briefing-2026-08-20.md)

**Highlights:**
- **EU AI Act handhaving volledig actief (2 augustus):** Transparantie-eisen zijn nu juridisch afdwingbaar — chatbots moeten zich identificeren als AI, deepfakes moeten gelabeld zijn. Het AI Office en nationale toezichthouders kunnen nu boetes opleggen. Voor Ctac-klanten met klantcontact-AI is compliance geen optie meer.
- **Prompt injection raak bij drie grote coding tools tegelijk:** Claude Code, Gemini CLI en GitHub Copilot werden gelijktijdig getroffen; credentials gelekt via besmette repositories. AI-coding agents in productie vereisen minimale IAM-permissies en onbetrouwbare input-behandeling — nu een aangetoond risico, geen theorie.
- **Microsoft Frontier Company ($2,5 miljard):** Microsoft bouwt een eigen AI-implementatiebedrijf met 6.000 experts — directe concurrent voor IT-consultancies. Enterprise AI verschuift van experiment naar productie; hyperscalers investeren gezamenlijk >$500 miljard in capex voor 2026.

**Ctac-relevantie van de dag:** Microsoft Frontier Company is de meest urgente strategische dreiging voor Ctac's implementatiediensten — maar biedt ook kansen in segmenten waar Microsoft niet direct actief is. EU AI Act-compliance assessments zijn nu tijdgevoelig. De prompt injection-incidenten creëren een onderscheidende propositieruimte rondom veilige AI-integratie.

---

### Vrijdag 21 augustus
→ Dagbriefing: [ai-briefing-2026-08-21.md](../ai-briefing-2026-08-21.md)

**Highlights:**
- **EU AI Act handhaving actief per 2 augustus:** Chatbots moeten zich als AI identificeren, deepfakes verplicht gelabeld; het AI Office en nationale autoriteiten handhaven nu actief met boetebevoegdheid. De AI Omnibus verlengt de deadline voor hoog-risico systemen tot december 2027, maar Artikel 50 is direct afdwingbaar.
- **OpenAI GPT-5.6 Ultrafast + Meta Muse Glimmer 30B lokaal:** OpenAI's Sol-model draait nu 14× sneller en is 54% token-efficiënter in codeertaken; Meta's Muse Glimmer 30B brengt volledig lokale agentic AI op consumenten-hardware — zonder cloud-afhankelijkheid, interessant voor privacy-gevoelige sectoren.
- **Prompt injection: 94% van LLM-agents kwetsbaar:** Drie AI-codeeragenten lekten secrets via één aanval; Microsoft patchte een CVE in Copilot Studio maar data werd alsnog geëxfiltreerd. Inference-spending ($23,3 mrd) overtreft nu training ($19 mrd) — enterprises operationaliseren in hoog tempo, terwijl de beveiligingsachterstand groeit.

**Ctac-relevantie van de dag:** De combinatie van actieve EU AI Act-handhaving (Artikel 50 nu afdwingbaar) en snel stijgende Benelux-adoptie (NL: 61%, BE: 62%) bevestigt dat compliance-assessments en productie-implementaties de centrale klantbehoefte zijn. Prompt injection als #1 kwetsbaarheid vraagt om security-by-design als vast onderdeel van elk agentic AI-traject dat Ctac begeleidt.

---

## 🏆 Weekhighlights

1. **EU AI Act is per 2 augustus afdwingbaar – en dat is echt.** De transparantievereisten (Artikel 50) zijn nu juridisch van kracht: chatbots moeten zich als AI identificeren, deepfakes verplicht gelabeld, met boetebevoegdheid voor het AI Office en nationale autoriteiten. De high-risk verplichtingen zijn via de AI Omnibus uitgesteld tot december 2027, maar de directe vereisten gelden nu. Voor klanten met AI in klantcontact is dit een complianceplicht, geen aanbeveling.

2. **Prompt injection domineert de beveiligingsagenda van de week.** Maandag troffen aanvallers Claude Code, Gemini CLI en GitHub Copilot simultaan – credentials gelekt via één besmette repository. Dinsdag bleek Atlassian Rovo kwetsbaar voor data-exfiltratie via Jira/Confluence. Vrijdag bevestigde onderzoek: 94% van LLM-agents is kwetsbaar. OWASP bevestigt: prompt injection blijft de #1 LLM-kwetsbaarheid. Het probleem is architectureel: modellen onderscheiden instructies en data fundamenteel niet.

3. **Microsoft bouwt een concurrent voor IT-consultancies.** Microsoft Frontier Company: $2,5 miljard commitment, 6.000 AI-implementatie-experts gericht op enterprise. Samen met AWS Forward Deployed Engineering en Google Agentic Data Cloud stappen alle hyperscalers direct de implementatieruimte in. Dit is geen verafgelegen dreiging voor consultancies – het is een directe concurrent die actief klanten werft.

4. **DeepSeek herschrijft de vendor-verhoudingen.** DeepSeek V4 Pro (GA) plus de open-source Harness coding agent bieden 7–17× kostenvoordeel ten opzichte van Claude Sonnet en GPT-5.5, met 23% enterprise token-marktaandeel. Het piek/dalprijsmodel (per 16 aug) verhoogt de druk verder. Computable bericht dat DeepSeek Google van de AI-troon heeft gestoten bij Nederlandse bedrijven. De model-keuze in klantproposities vraagt heroverweging.

5. **Open-source agentic AI is productie-klaar geworden.** Meta Muse Glimmer 30B (Apache 2.0) draait volledig lokaal op consumentenhardware met multimodale en agentic capaciteiten – zonder cloud-afhankelijkheid. Gecombineerd met Stripe's overname van OpenRouter ($7 mrd) en OpenAI GPT-5.6 Ultrafast (14× sneller, 54% token-efficiënter), zien we dat de infrastructuurlaag rondom AI fundamenteel verandert: sneller, goedkoper en meer decentraal.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De week laat een driedubbele versnelling zien: performance (OpenAI Sol 14× sneller, Google Gemini 3.7 Flash +10 procentpunt coding in drie weken), kosten (DeepSeek 7–17× goedkoper) en lokale deployability (Muse Glimmer 30B on-device). De modelrace is geen benchmarkwedstrijd meer – het is een race naar enterprise-adoptie via snelheid, prijs en distributie. Stripe's overname van OpenRouter voor $7 miljard signaleert dat AI-orkestratie en transactie-infrastructuur convergeren: betalingen worden AI-triggers en vice versa.

Een apart signaal: een nog niet uitgebracht Anthropic-model maakte aantoonbare voortgang op de Riemann-hypothese – een van de grootste open wiskundige problemen. Dit is geen productnyheid, maar een existentieel datapoint over waar frontier-capaciteiten naartoe gaan.

### 🏛️ Governance & Beleid

EU AI Act Artikel 50 is actief: de week begon en eindigde met berichten over handhaving. Het onderscheid tussen wat nu geldt (transparantie-ID-verplichting, deepfake-labeling) en wat uitgesteld is (high-risk Annex III tot dec 2027, Annex I tot aug 2028) is voor klanten cruciaal om helder te krijgen. Veel organisaties verwarren de niveaus en zijn óf onterecht gerust óf onterecht in paniek.

Nationaal: Nederland is de tweede AI-exporteur van Europa (Computable, 19 aug). De AI-supercomputer in Groningen boet aan rekenkracht in door oplopende kosten – een signaal dat de Nederlandse AI-infrastructuur kwetsbaar is voor budgetdruk. Het White House hield ontmoetingen met toptechbedrijven over AI-regulering, wat de internationale divergentie tussen VS, EU en China verder verdiept.

### 🔐 Security & Risk

Prompt injection was het beveiligingsthema van de hele week, niet van één dag. De incidenten bij coding agents (maandag), Atlassian Rovo (dinsdag) en de Copilot Studio CVE (vrijdag, gepatch maar data toch geëxfiltreerd) vormen samen een patroon: productie-AI-integraties creëren systemische kwetsbaarheden die niet met patches worden opgelost. Schneier schreef er een analyse over in "AI Genie in the Wild". Inference-spending ($23,3 mrd) overtreft voor het eerst training ($19 mrd) – enterprise AI operationaliseert in hoog tempo, terwijl de beveiligingsachterstand toeneemt.

### 📈 Markt & Adoptie

Benelux-adoptiecijfers stijgen door: Nederland 61%, België 62% (Computable, week 34). Nederland is de tweede AI-exporteur van Europa. Rabobank investeert miljarden in IT met AI als kern; ABN Amro zet in op AI-coding. De enterprise AI-markt is $114,87 mrd waard in 2026. Maar de overgang van pilot naar productie blijft het structurele knelpunt: twee derde van organisaties zit nog in de experimenteerfase. Microsoft Copilot groeit sterk (CIO Dive); Google lanceert Agentic Data Cloud; SAP brengt één unified Business AI Platform.

---

## 💼 Ctac-weekperspectief

- **EU AI Act compliance is nu een acute klantbehoefte, geen toekomstplanning.** Artikel 50 (transparantieverplichting) is juridisch afdwingbaar. Klanten met AI-chatbots, AI-telefonisten of deepfake-gerelateerde toepassingen moeten nu handelen. Een quick-scan van bestaande deployments bij klanten in overheid, finance en retail is een directe propositie. Wie die dienst nu aanbiedt, pakt het window voordat andere consultancies de markt overspoelen.

- **Security-by-design is geen optie meer in agentic AI-trajecten.** De simultane aanval op drie coding agents, de Atlassian Rovo-kwetsbaarheid en de Copilot Studio CVE tonen aan: elke agentic integratie heeft een aanvalsoppervlak. Ctac moet security-architectuur (minimale IAM-rechten, input-sanitization, audit-logging, human-override) als standaard onderdeel van elk agentic traject behandelen – zowel als kwaliteitseis intern als als verkoopargument. Dit differentieert van implementators die snel leveren zonder securitylaag.

- **Microsoft Frontier Company vereist een strategische respons.** 6.000 Microsoft-implementatie-experts gericht op enterprise is een directe concurrent voor Ctac's kernactiviteiten. De kans zit in de segmenten waar Microsoft niet direct actief is: klanten die Microsoft-platformonafhankelijkheid willen, privacy-bewuste sectoren met on-premise vereisten (Muse Glimmer 30B maakt dat realistisch), en klanten die diepere sector-specifieke expertise zoeken dan een hyperscaler biedt.

- **Heroverweeg vendor-adviezen in de lijn van DeepSeek.** DeepSeek V4 Pro met 7–17× kostenvoordeel is geen experimenteel model meer; het heeft 23% enterprise token-marktaandeel. Voor klanten met hoge inferentievolumes of budgetgevoelige trajecten is DeepSeek een reëel alternatief. Ctac moet in staat zijn dit onbevooroordeeld te adviseren – inclusief de beveiligings- en soevereiniteitsoverwegingen die bij Chinese modelhosting horen.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [TechCrunch – OpenAI GPT-5.6 launch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [OpenAI Newsroom – product releases](https://openai.com/news/product-releases/)
- [Google Blog – AI updates juli/augustus 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-july-2026/)
- [TechCrunch – Google Gemini 3.6 Flash](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)
- [Hugging Face – Meta Muse Glimmer 30B](https://huggingface.co/blog/muse-glimmer)
- [Hugging Face – State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [TechCrunch – Anthropic unreleased model Riemann progress](https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/)
- [VentureBeat – DeepSeek Harness launch](https://venturebeat.com/technology/deepseek-harness-launches-as-open-source-rival-to-claude-code-alongside-v4-pro-on-api-with-higher-prices)
- [VentureBeat – DeepSeek V4 Flash agentic performance](https://venturebeat.com/orchestration/deepseeks-top-ranked-v4-flash-stumbles-on-real-agent-tasks-as-its-prices-surge)
- [LLM Stats – model updates augustus 2026](https://llm-stats.com/llm-updates)
- [Computable – DeepSeek stoot Google van AI-troon](https://www.computable.nl/2026/08/13/deepseek-stoot-google-van-ai-troon-bij-bedrijven/)
- [Anthropic – Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [AI Weekly – OpenAI & Google augustus 2026](https://aiweekly.co/ai-news-today)

**Governance & Beleid**
- [EC Digital Strategy – AI Act handhaving gestart 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act tracker – implementatietijdlijn](https://artificialintelligenceact.eu/)
- [Computable – wat je moet weten van de AI Act](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [NOS – AI-telefonist moet zich direct prijsgeven](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)
- [Computable – nieuw Europees netwerk AI in rechtbank](https://www.computable.nl/2026/08/04/nieuw-europees-netwerk-onderzoekt-ai-in-de-rechtbank/)
- [CNN Business – White House AI regulation](https://www.cnn.com/2026/08/03/tech/white-house-meet-with-top-ai-companies-big-regulation-push)
- [AIToolsRecap – AI News August 2026](https://aitoolsrecap.com/Blog/AINewsAugust2026.aspx)

**Security & Risk**
- [VentureBeat – Prompt injection enterprise AI agents](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – AI agent runtime security 2026](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – six exploits broke AI coding agents IAM](https://venturebeat.com/security/six-exploits-broke-ai-coding-agents-iam-never-saw-them)
- [VentureBeat – Microsoft/Salesforce Copilot CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [The Hacker News – Atlassian Rovo prompt injection](https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html)
- [VentureBeat – Anthropic prompt injection cijfers](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)
- [Airia – AI Security 2026 trifecta](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Schneier on Security – AI Genie in the Wild](https://www.schneier.com/blog/archives/2026/08/ai-genie-in-the-wild.html)
- [Data News – Meer cyberaanvallen door AI in België](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
- [TechCrunch – OpenAI Astra security concerns](https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/)

**Markt & Adoptie**
- [TechCrunch – Microsoft Frontier Company $2,5 mrd](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [Microsoft Blog – FY26 terugblik](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [CIO Dive – Microsoft Copilot growth Q3 2026](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [CIO Dive – AWS Forward Deployed Engineering](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)
- [CIO Dive – AI spending & enterprise maturity](https://www.ciodive.com/news/AI-spending-soars-enterprise-maturity/827488/)
- [CIO Dive – Microsoft & Google enterprise AI leadership](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [SAP Business AI Platform – CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [Computable – Benelux AI-adoptie koploper](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [Computable – Nederland tweede AI-exporteur Europa](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/)
- [Computable – Rabobank investeert miljarden in IT](https://www.computable.nl/2026/08/05/rabobank-investeert-miljarden-in-it/)
- [Computable – ABN Amro AI coding](https://www.computable.nl/2026/08/13/abn-amro-voortvarend-met-ai/)
- [Computable – AI-supercomputer Groningen](https://www.computable.nl/2026/08/19/ai-supercomputer-groningen-boet-aan-rekenkracht-in-door-oplopende-kosten/)
- [AIToolsRecap – AI News August 2026](https://aitoolsrecap.com/Blog/AINewsAugust2026.aspx)
