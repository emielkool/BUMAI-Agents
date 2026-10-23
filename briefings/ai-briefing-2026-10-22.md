---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-22
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 22 oktober 2026

## 🔑 Highlights van de dag

- **PHP Armageddon (21 okt):** AI-tools van OpenAI en Google Wiz ontdekten kritieke kwetsbaarheden in PHP; de NSA waarschuwde organisaties te patchen of PHP-systemen offline te halen. Overheidssites wereldwijd gingen offline. Een gedenkwaardig voorbeeld van hoe AI nu de vuurkracht achter serieuze kwetsbaarheidsopsporing is.
- **EU AI Act: eerste geharmoniseerde standaard gepubliceerd (19 okt):** De Europese Commissie publiceerde EN 18286:2026 in het Publicatieblad – de eerste officiële standaard voor kwaliteitsbeheersystemen bij high-risk AI-aanbieders. Concreet handvat voor compliance-trajecten.
- **Recursive Flint (21 okt):** Een open-weight coding model dat op een laptop draait en grotendeels door AI zelf is gebouwd. Vroeg signaal van recursieve zelfverbetering; gratis beschikbaar via Hugging Face (Apache 2.0).
- **GPT-6 Sol & Luna API-prijzen gehalveerd:** OpenAI maakt frontier AI verder betaalbaar – Sol op €2/M input tokens, Luna op €0,10/M – wat de drempel voor enterprise-adoptie verder verlaagt.
- **Microsoft AI-business: $37B+ ARR, 123% YoY groei:** Het Copilot-platform groeit explosief; Microsoft stak $2,5 miljard in een programma dat 6.000 engineers bij klanten plaatst om AI te implementeren.

---

## 🧠 Technologie & Modellen

**Recursive Flint – AI-gebouwde coding model voor de laptop**
Recursive lanceerde gisteren Flint, een open-weight coderingsmodel dat op consumenterhardware draait. Opvallend is de ontstaansgeschiedenis: het werd grotendeels gemaakt door Recursive's eigen AI-systeem "Eureka Machine", waardoor een klein team het model in minder dan vier maanden kon bouwen. De bewering dat dit recursieve zelfverbetering benadert is technisch gezien overdreven – het blijft een AI-assistent met menselijk toezicht – maar de efficiëntiewinst is reëel. Gratis, Apache 2.0, geen serverkosten, code blijft lokaal. ([TechCrunch](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/))

**Claude Opus 5.5 (Anthropic, 18 okt)**
Anthropic's zwaarste model scoort het hoogst op agentic coding en kenniswerk, en kost 40% minder te draaien dan zijn voorganger Opus 5. Relevant voor kostenbewuste enterprise-inzet van autonome agents. ([Anthropic Newsroom](https://www.anthropic.com/news))

**Meta Muse Wonder & Muse Spark Open**
Meta's eerste frontier model (Muse Wonder, 12 okt, $4/$20 per M tokens) en een 816B open-weight variant (Muse Spark Open, 15 okt) die draait op Apple Silicon. De open variant vereist enorm veel RAM; de praktische inzetbaarheid is voorlopig beperkt.

**OpenAI GPT-6 Sol & Luna – API-prijzen gehalveerd**
Sol ($2/M input, $10/M output) voor complexe taken; Luna ($0,10/$0,50) voor high-volume. GPT-6.1 Sol is inmiddels beschikbaar voor Enterprise gebruikers tegen een vijfde van de standaard prijs. Prompt caching geeft 90% korting op gecachte input. ([VentureBeat](https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more))

---

## 🏛️ Governance & Ethiek

**Eerste geharmoniseerde AI Act-standaard: EN 18286:2026 (19 okt)**
De Europese Commissie publiceerde de eerste officiële geharmoniseerde standaard onder de AI Act in het Publicatieblad. EN 18286:2026 richt zich op kwaliteitsbeheersystemen voor high-risk AI-aanbieders en biedt een vermoeden van conformiteit met Artikel 17. Dit is een praktisch ankerpunt voor bedrijven die nu wachten op houvast voor hun complianceaanpak. ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal))

**Handhaving is actief**
Vanaf 2 augustus 2026 handhaven het AI Office en nationale autoriteiten actief. Boetes voor general-purpose AI-aanbieders kunnen oplopen tot €15M of 3% van de wereldwijde jaaromzet. De "AI Omnibus"-aanpassingen (van kracht 27 juli) vereenvoudigen documentatieplichten voor mkb.

---

## 🔐 Security & Risk

**PHP Armageddon: AI vindt kritieke kwetsbaarheden, overheidssites offline (21 okt)**
OpenAI's "Patch the Planet"-initiatief en Google's Wiz-team gebruikten respectievelijk GPT-5.6 Sol, Gemini 4 Argon en de Wiz Atlas security AI-agent om meerdere kritieke kwetsbaarheden in PHP te ontdekken. De NSA adviseerde organisaties onmiddellijk te patchen of PHP-systemen uit de lucht te halen. Wiz waarschuwt dat LLMs ook helpen exploits aan te passen aan verschillende configuraties, wat de risicokwalificatie verhoogt. Patches zijn beschikbaar; er zijn nog geen meldingen van actieve exploitatie. ([TechCrunch](https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/))

**OpenCode-hack: AI-kosten doorbelast aan gebruikers (19 okt)**
Hackers misbruikten de AI coding tool OpenCode om API-kosten door te berekenen aan nietsvermoedende gebruikers – een nieuwe aanvalsvector bij het groeiende ecosysteem van AI-tools. ([TechCrunch](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/))

**Google bevroor bug bounty wegens AI-overbelasting**
Google stopte tijdelijk zijn open-source bug bounty programma vanwege een "significant rise" in AI-gegenereerde inzendingen die de beoordelingscapaciteit overbelastten. Een vroeg teken dat AI het bug-bounty-model fundamenteel verstoort. ([TechCrunch](https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/))

---

## 📈 Markt & Adoptie

**Microsoft: $37B+ ARR, 6.000 engineers bij klanten**
Microsoft's AI-omzet groeide 123% jaar-op-jaar. Met een investering van $2,5 miljard plaatst het 6.000 engineers bij klanten voor hands-on AI-implementatie – een directe concurrentiepressure voor IT-dienstverleners. ([CIO Dive](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/))

**Google: Persistent Gemini Agents voor enterprise**
Google lanceerde Persistent Gemini Agents met eigen Gmail-, Calendar- en Drive-opslag voor langlopende taken. Dit positioneert Gemini als een autonome enterprise-medewerker, niet alleen als assistant. ([VentureBeat](https://venturebeat.com/orchestration/google-cloud-unveils-persistent-gemini-agents-for-long-running-tasks-and-they-get-their-own-gmail-calendar-and-drive-storage))

**OpenAI acquireert Orchestra Bio (20 okt)**
OpenAI zet zijn eerste stap in biotech via de acquisitie van Orchestra Bio. Dit past in de bredere strategische beweging van AI-labs richting verticale sectors buiten software. ([TechCrunch](https://techcrunch.com/2026/10/20/openai-acquires-startup-orchestra-bio%E2%81%A0-to-beef-up-its-biotech-business/))

**Geheugenkosten: verdubbeling door AI-vraag**
Hyperscalers (Microsoft $190B, Amazon $200B capex dit jaar) drijven geheugenkosten omhoog; organisaties die eigen hardware willen inzetten voor AI-inferentie zien de rekening stijgen. Enterprise-adoptiesnelheid blijft achter op hyperscaler-investeringen.

---

## 💡 Ctac-relevantie

**PHP-security direct actie vereist:** Veel Nederlandse overheidsinstellingen en zakelijke klanten van Ctac draaien PHP-applicaties. De NSA-waarschuwing van gisteren is urgent: controleer of klanten de PHP-patches hebben doorgevoerd. Dit is ook een gespreksingang voor een bredere AI-security posture review.

**EN 18286:2026 als compliance-propositie:** Met de eerste geharmoniseerde AI Act-standaard nu beschikbaar, kunnen Ctac-consultants klanten helpen hun high-risk AI-kwaliteitsbeheersystemen te toetsen. Dit is een concrete, tijdgebonden kans nu de markt houvast zoekt.

**Open-weight modellen verlagen on-premise drempel:** Flint, Muse Spark Open en Claude Opus 5.5 vergroten het landschap van lokaal inzetbare modellen. Voor klanten met databehoudsvereisten (overheid, zorg, finance) is dit een sterkere propositie dan een jaar geleden. Ctac kan hierop een differentiërende propositie bouwen.

**Microsoft-pressie op dienstverlening:** Het $2,5B customer engineer programma van Microsoft is directe concurrentie voor de implementatiediensten van IT-dienstverleners zoals Ctac. De onderscheidende waarde zit in branchekennis en maatwerk – niet in headcount of tooling-dekking.

---

## 📚 Bronnen & verder lezen

- [Recursive Flint – TechCrunch (21 okt)](https://techcrunch.com/2026/10/21/recursive-launches-flint-a-laptop-coding-model-it-says-was-largely-built-by-ai/)
- [PHP Armageddon – TechCrunch (21 okt)](https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/)
- [OpenCode-hack – TechCrunch (19 okt)](https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/)
- [OpenAI acquireert Orchestra Bio – TechCrunch (20 okt)](https://techcrunch.com/2026/10/20/openai-acquires-startup-orchestra-bio%E2%81%A0-to-beef-up-its-biotech-business/)
- [GPT-6 Sol & Luna API prijzen – VentureBeat](https://venturebeat.com/technology/openai-releases-gpt-6-sol-and-luna-models-slashing-api-costs-50-or-more)
- [Anthropic Newsroom – Claude Opus 5.5](https://www.anthropic.com/news)
- [EN 18286:2026 AI Act standaard – Europese Commissie (19 okt)](https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal)
- [EU AI Act enforcement framework](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [Microsoft AI earnings – CIO Dive](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [Persistent Gemini Agents – VentureBeat](https://venturebeat.com/orchestration/google-cloud-unveils-persistent-gemini-agents-for-long-running-tasks-and-they-get-their-own-gmail-calendar-and-drive-storage)
- [Google bug bounty bevroren – TechCrunch](https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/)
