---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-04
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 4 mei 2026

## 🔑 Highlights van de dag

- **Microsoft Agent 365 is GA** – Per 1 mei is Microsoft's controleplatform voor AI-agents algemeen beschikbaar, samen met Microsoft 365 E7. Dit is het meest directe enterprise-signaal dat agentische AI de mainstream bereikt heeft.
- **Anthropic's Mythos: beperkte release vanwege veiligheidsrisico's** – Het nieuwe topmodel van Anthropic wordt vanwege significante cybersecurity-toepassingen slechts aan geselecteerde partners uitgerold. Een zeldzaam voorbeeld van een lab dat zelf de rem trekt.
- **EU AI Act: T-90 dagen tot volledige werking** – Op 2 augustus 2026 treden de transparantievereisten en toezichtbevoegdheden voor GPAI-modellen in werking. Organisaties die nu nog niet compliant zijn, lopen achter.
- **Prompt injection: OpenAI erkent dat het structureel probleem blijft** – Drie AI coding agents lekten credentials via een enkele prompt injection. Veiligheidsexperts spreken nu van een "promptware kill chain" als volwassen aanvalsvector.
- **Salesforce +6.000 enterprise-klanten in één kwartaal** – Ondanks geluiden over een AI-bubbel laat enterprise-adoptie juist versnelling zien.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.5** is uitgerold naar Plus-, Pro-, Business- en Enterprise-gebruikers van ChatGPT. OpenAI positioneert het als het "slimste en meest intuïtieve model tot nu toe" met hogere scores dan Google en Anthropic op gangbare benchmarks. Opvallend: de lancering valt samen met Anthropic's aankondiging van Mythos, wat het competitieve tempo in het topmodellensegment onderstreept.

**Anthropic Mythos** is alleen beschikbaar voor geselecteerde partners. De reden: het model heeft "significante cybersecurity-toepassingen" die misbruik reëel maken. Dit is strategisch interessant – Anthropic kiest bewust voor gecontroleerde uitrol boven marktaandeel.

**Microsoft lanceerde drie eigen AI-modellen** als directe concurrent voor OpenAI en Google, naast de lancering van Agent 365 en de Frontier Suite (Microsoft 365 E7). De interne modelstrategie van Microsoft versterkt hun positie als AI-stapelpartner die niet uitsluitend op OpenAI leunt.

**Stripe Link** is uitgebreid met ondersteuning voor autonome AI-agents die namens gebruikers aankopen kunnen doen via virtuele betaalkaarten met realtime autorisatie. Dit is infrastructureel nieuws: betalingsrails voor agentische systemen worden een standaard verwachting.

*Bronnen: [TechCrunch – GPT-5.5](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/) | [TechCrunch – Stripe Link](https://techcrunch.com/2026/04/30/stripe-link-digital-wallet-ai-agents-shopping/) | [Anthropic nieuws](https://www.anthropic.com/news)*

---

## 🏛️ Governance & Ethiek

De **EU AI Act** bereikt op **2 augustus 2026** zijn volledige werking: transparantieregels voor AI-systemen worden verplicht en de Europese AI Office krijgt formele handhavingsbevoegdheden over GPAI-modellen (zoals GPT-5.5 en Gemini). Eén aandachtspunt: de door CEN/CENELEC te ontwikkelen harmonisatienormen zijn nog steeds niet gereed – de deadline van augustus 2025 is gemist. Ondersteuningsdocumenten volgen in Q2 2026. Dit betekent dat organisaties voorlopig zonder gecertificeerde conformiteitsstandaarden moeten opereren.

De regels voor **hoog-risico AI-systemen** treden gefaseerd in werking: augustus 2026 en augustus 2027. Voor IT-dienstverleners die AI inzetten in domeinen als HR, kredietbeoordeling of overheidsdienstverlening is dit de meest urgente compliance-horizon.

*Bronnen: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) | [EC Digitale Strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)*

---

## 🔐 Security & Risk

**Prompt injection blijft structureel onopgelost.** Drie AI coding agents lekten geheimen via één enkele prompt injection-aanval – en de relevante system card had dit risico al voorspeld. VentureBeat documenteert een gestructureerde *promptware kill chain* van zeven stappen, analoog aan de MITRE ATT&CK-structuur voor traditionele malware.

Specifieke aanvalsvectoren die nu in het wild worden gezien:
- **RAG poisoning**: 90% succespercentage bij injectie van vijf kwaadaardige teksten in databases met miljoenen documenten (zero-click)
- **Obfuscatie-aanvallen** via Base64, ASCII-art en Unicode – tot 76% succespercentage op GPT-4, Gemini, Claude en Llama2
- **Zelf-replicerende agents**: geïnfecteerde e-mailassistenten die kwaadaardige payloads doorsturen naar alle contacten

Praktische conclusie: organisaties die AI-agents inzetten zonder runtime-beveiligingslaag lopen significant risico. Standaard safeguards en beleidsdocumenten zijn onvoldoende.

*Bronnen: [VentureBeat – AI agent security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [Schneier – Promptware Kill Chain](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)*

---

## 📈 Markt & Adoptie

**Microsoft Agent 365 (GA per 1 mei)** is het governance- en controleplatform voor AI-agents binnen de Microsoft-stack, geprijsd op $15 per gebruiker. Het wordt gebundeld in **Microsoft 365 E7 (Frontier Suite)**, die M365 E5, Entra Suite, Copilot en Agent 365 combineert. Dit is de meest concrete enterprise-productlancering van dit jaar voor de Microsoft-channel.

**Google** lanceerde op Google Cloud Next '26 de **Agentic Data Cloud** en het **Gemini Enterprise Agent Platform** – een no-code Agent Designer maakt het bouwen van trigger-gebaseerde workflows toegankelijk voor non-developers.

**NVIDIA's Agent Toolkit** heeft 17 grote adopters binnengehaald, waaronder Adobe, Salesforce en SAP. De toolkit is open-source en bevat Nemotron (reasoning models), AI-Q (enterprise knowledge agents) en cuOpt (optimalisatiebibliotheek).

**Salesforce** voegde 6.000 enterprise-klanten toe in één kwartaal – een duidelijk contra-signaal tegen de AI-bubbel-narratief.

*Bronnen: [Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/) | [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/) | [VentureBeat – Salesforce](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000) | [VentureBeat – NVIDIA](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)*

---

## 💡 Ctac-relevantie

**Microsoft 365 E7 en Agent 365 zijn directe kansen.** Ctac heeft een sterke Microsoft-practice; de GA van Agent 365 opent een nieuw propositioneel domein: begeleiding van klanten bij de governance en uitrol van AI-agents binnen hun Microsoft-omgeving. De $15/gebruiker-prijs en de bundeling met bestaande M365-licenties maken adoptie laagdrempelig – maar de implementatie-complexiteit is hoog. Hier ligt werk.

**EU AI Act compliance-advies wordt urgent.** Met nog 90 dagen tot de handhavingsdeadline voor GPAI-transparantie en hoog-risico AI zijn er klanten die nu snel compliance-assessments nodig hebben, met name in sectoren als zorg, financiën en overheid. Ctac kan hier als trusted partner op positioneren.

**Prompt injection is een boardroom-onderwerp geworden.** Het VentureBeat-onderzoek dat coding agents credentials lekten via system card-voorspelde aanvallen maakt de security-gap in AI-projecten concreet. Bij elke klant die AI-agents of RAG-architecturen inzet, verdient het aanbeveling een expliciete runtime-beveiligingslaag te bespreken – dit is een differentiator in Ctac's AI-projectaanpak.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI GPT-5.5 lancering](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)
- [Anthropic – Nieuws en releases](https://www.anthropic.com/news)
- [TechCrunch – Stripe Link voor AI-agents](https://techcrunch.com/2026/04/30/stripe-link-digital-wallet-ai-agents-shopping/)
- [artificialintelligenceact.eu – Implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act governance en handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [VentureBeat – AI agent runtime security & system card audit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Schneier on Security – Promptware Kill Chain](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)
- [Microsoft Blog – Frontier Transformation](https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [VentureBeat – NVIDIA enterprise agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [VentureBeat – Salesforce +6.000 enterprise klanten](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000)
- [TechCrunch – OpenAI Agents SDK update](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/)
