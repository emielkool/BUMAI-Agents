---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-27
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 27 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act volledig van kracht**: Vanaf 2 augustus worden Europese bedrijven actief gehandhaafd op de transparantievereisten. Chatbots moeten zich als AI identificeren, deepfakes verplicht gelabeld worden — geen soft-landing meer.
- **OpenAI versnelt op alle fronten**: GPT-5.6 Sol krijgt een "Ultrafast mode" (14x sneller), API-prijzen dalen met 20%, en o3 wordt vandaag (26 aug) definitief uit ChatGPT gehaald. De modelstrategie schakelt hard naar snelheid en kostprijs.
- **Kritieke infrastructuur in het vizier**: AI-gegenereerde exploit scripts richten zich op Siemens S7 PLC's in Amerikaanse energieinfrastructuur. De combinatie van AI en industriële kwetsbaarheden maakt dit een structureel risico, ook buiten de VS.
- **Shadow AI als insider threat**: Onderzoek toont dat de top 5% van enterprise AI-gebruikers 12x intensiever met AI omgaat dan de rest — en daarmee een onevenredig hoog lekrisico via shadow AI en autonoom opererende agents creëert.
- **Big Tech capex naar $725 mrd**: Amazon, Microsoft, Meta en Google investeren gezamenlijk tot $725 mrd in infrastructuur in 2026. Cloudaanbieders groeien 40% in capex. De AI-infrastructuurrace is geen hype maar structurele herpositionering.

---

## 🧠 Technologie & Modellen

**OpenAI** heeft op 25 augustus "Jalapeño" aangekondigd, een inference-optimalisatielaag met "industry-leading speed and efficiency". Op 18 augustus werd een Ultrafast mode voor GPT-5.6 Sol gelanceerd (tot 14x sneller dan het standaardmodel) en kregen gratis gebruikers toegang tot GPT-5.6 Luna. Op 21 augustus werden API- en creditprijzen voor Sol met meer dan 20% verlaagd voor de komende drie maanden. Vandaag (26 aug) wordt o3 na 90 dagen uitgefaseerd uit ChatGPT.
Bron: [openai.com/news](https://openai.com/news/), [TechCrunch – GPT-5.6 launch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)

**Google** kondigde twee nieuwe Gemini-modellen aan: *Gemini Omni* (multimodaal, inclusief videogeneratie) en *Gemini 3.5*, gericht op verbeterd wereldbegrip en multimodale bewerkbaarheid.
Bron: [blog.google – Google I/O 2026](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-collection/)

**Anthropic** maakte de introductieprijs van Claude Sonnet 5 permanent ($2/$10 per miljoen tokens) en verbeterde Claude Tag in Slack: de agent leest nu volledige gesprekskontexten en is ~30% beter in het bepalen wanneer hij proactief instapt.
Bron: [TechCrunch – Claude Tag update](https://venturebeat.com/orchestration/anthropics-new-claude-tag-update-lets-its-slack-agent-read-the-full-conversation-and-jump-in-unprompted)

---

## 🏛️ Governance & Ethiek

Vanaf **2 augustus 2026** handhaaft de Europese Commissie de EU AI Act actief — een kantelpunt na twee jaar implementatievoorbereiding. De transparantievereisten (Artikel 50) zijn nu afdwingbaar:
- Chatbots en interactieve AI-systemen moeten zich bij eerste interactie als AI identificeren.
- Deepfakes en AI-gegenereerde content moeten machine-leesbaar gemarkeerd zijn.
- Markttoezichthouders per lidstaat zijn verantwoordelijk voor handhaving.

De *AI Omnibus* (vereenvoudigingsamendement) is op 27 juli 2026 in werking getreden en reduceert nalevingslasten voor een deel van de aanbieders. Er geldt een overgangsperiode voor markering tot december 2026 voor systemen die voor 2 augustus al op de markt waren.

De EC publiceerde begeleidende richtlijnen voor aanbieders en inzenders van hoog-risico AI-systemen.
Bron: [digital-strategy.ec.europa.eu – Enforcement start](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august), [computable.nl – AI Act transparantie](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)

---

## 🔐 Security & Risk

**AI-gegenereerde exploits op kritieke infrastructuur**: Dreigingsactoren gebruiken AI om exploitscripts te genereren voor Siemens S7 PLC's in Amerikaanse energieinfrastructuur. De drempel voor gerichte aanvallen op OT-omgevingen daalt structureel.
Bron: [The Hacker News – AI-Generated Exploit Scripts](https://thehackernews.com/2026/08/ai-generated-exploit-scripts-target.html)

**GhostJacking en AI-aanvalspatronen**: Recente campagnes combineren AI-gestuurde zijdelingse beweging ("GhostJacking") met EtherHiding ClickFix-technieken. 2026 wordt geduid als het jaar van AI-geassisteerde cyberaanvallen, met 28,3% van CVE's geëxploiteerd binnen 24 uur na publicatie.
Bron: [The Hacker News – ThreatsDay](https://thehackernews.com/2026/08/threatsday-ghostjacking-ai-attacks.html), [The Hacker News – 2026 AI attacks](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)

**Shadow AI als enterprise risico**: De top 5% van enterprise AI-gebruikers genereert een structureel lekrisico via shadow AI, datadeling buiten guardrails en autonoom opererende agents.
Bron: [The Hacker News – AI Super-Adopters](https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users.html)

**API reasoning-lek**: Onderzoekers ontdekten dat OpenAI, Anthropic en Google interne redeneerinhoud meestuurden in API-sessielogs — inclusief potentieel API-sleutels en wachtwoorden. Dit is inmiddels gepatcht maar toont de onrijpheid van agentische architecturen.
Bron: [TechCrunch – AI safety test](https://techcrunch.com/2026/08/09/the-ai-safety-test-is-becoming-a-safety-risk/)

---

## 📈 Markt & Adoptie

**Microsoft** heeft meer dan 20 miljoen betaalde M365 Copilot-seats, met het aantal grote enterprise-klanten (50k+ seats) dat jaar-op-jaar verviervoudigde. De AI-omzet loopt op een jaarlijks run rate van $37 mrd (+123% YoY).
Bron: [CIO Dive – Microsoft Copilot growth](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)

**Google Cloud** passeerde de $20 mrd grens, met bijna 75% van Cloud-klanten die AI-producten inzetten. Gemini Enterprise groeit 40% kwartaal-op-kwartaal in betaalde actieve gebruikers.
Bron: [CIO Dive – Google Cloud $20B](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)

**Capex-race**: Amazon, Microsoft, Meta en Google plannen gezamenlijk tot $725 mrd capex in 2026 — een stijging van ~40%. Ondanks de groei zit twee derde van de bedrijven nog vast in de pilotfase van GenAI.
Bron: [CIO Dive – Microsoft infrastructure](https://www.ciodive.com/news/Microsoft-infrastructure-cloud-growth/826658/), [CIO Dive – AI boosts cloud spending](https://www.ciodive.com/news/ai-boost-cloud-spending/810399/)

**Nvidia** lanceerde een enterprise AI agent-platform met Adobe, Salesforce en SAP als vroege adopters.
Bron: [VentureBeat – Nvidia enterprise AI agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)

---

## 💡 Ctac-relevantie

**EU AI Act – directe actie vereist**: De handhaving is gestart. Ctac's klanten in gereguleerde sectoren (overheid, finance, zorg) moeten hun AI-systemen nu aantoonbaar voldoen aan Artikel 50. Dit is een concrete advies- en implementatiekans: van classificatie tot labeling-architectuur tot GPAI-documentatie. De AI-omnibus verlaagt de drempel voor kleinere aanbieders, maar ontslaat deployers niet van transparantieplicht.

**Shadow AI = Ctac-propositie**: De data over risicovolle AI super-adopters biedt een haakje voor governance-trajecten bij enterprise klanten: AI-beleid, guardrail-architectuur, agent-monitoring. Dit is een groeiend marktsegment dat Ctac kan adresseren met een gecombineerd advies/implementatie-aanbod.

**Prijsdaling modellen**: GPT-5.6 Sol en Sonnet 5 worden structureel goedkoper. Dit maakt de businesscase voor agentische toepassingen bij klanten aantrekkelijker en verlaagt de drempel voor productisering van Ctac's AI-proposities.

**Agentsecurity als nieuw aandachtsgebied**: Het API reasoning-lek en de GhostJacking-patronen laten zien dat agentische architecturen specifieke beveiligingsrisico's introduceren die klassieke security-tooling mist. Vroeg positioneren op dit terrein — intern én richting klanten — geeft een differentiërend voordeel.

---

## 📚 Bronnen & verder lezen

- [OpenAI nieuws – augustus 2026](https://openai.com/news/)
- [TechCrunch – GPT-5.6 launch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [Anthropic – Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)
- [VentureBeat – Claude Tag Slack update](https://venturebeat.com/orchestration/anthropics-new-claude-tag-update-lets-its-slack-agent-read-the-full-conversation-and-jump-in-unprompted)
- [EC – AI Act enforcement start 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [Computable.nl – AI Act transparantie vereisten](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [The Hacker News – AI-Generated Exploit Scripts Siemens PLC](https://thehackernews.com/2026/08/ai-generated-exploit-scripts-target.html)
- [The Hacker News – Shadow AI enterprise risk](https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users.html)
- [TechCrunch – AI safety test becomes safety risk](https://techcrunch.com/2026/08/09/the-ai-safety-test-is-becoming-a-safety-risk/)
- [CIO Dive – Microsoft Copilot growth](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [CIO Dive – Google Cloud $20B](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [VentureBeat – Nvidia enterprise AI agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
