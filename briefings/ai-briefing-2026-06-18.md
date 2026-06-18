---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-18
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 18 juni 2026

## 🔑 Highlights van de dag

- **Anthropic overtreft OpenAI in waardering én omzet:** Na een Series H-ronde van $65 miljard ($965B waardering) heeft Anthropic vertrouwelijk een IPO-aanvraag ingediend, gericht op een beursintroductie op de Nasdaq dit najaar. ARR van $30B vs. OpenAI's $25B – de rangorde in de AI-race verschuift.
- **Microsoft lanceert eigen reasoning model MAI-Thinking-1:** Bij Build 2026 presenteerde Microsoft een familie van zeven eigen modellen. MAI-Thinking-1 (35B actieve parameters, 256K context) haalt coding-benchmarks van Opus 4.6 en presteer beter dan Sonnet 4.6 op blind tests – een directe aanval op Anthropic's marktpositie.
- **EU AI Act transparantievereisten: augustus 2026 deadline nadert:** De Code of Practice on Transparency of AI-generated content is gepubliceerd; organisaties hebben nog minder dan twee maanden om hun markering van AI-gegenereerde content op orde te brengen.
- **Google doneert A2A-protocol aan Linux Foundation:** Agentic AI-interoperabiliteit wordt steeds serieuzer genomen. A2A (Agent2Agent), nu vendor-agnostisch beheerd, wordt ondersteund door Microsoft, SAP, Salesforce, ServiceNow en >50 andere bedrijven.
- **Prompt injection blijft de achilleshiel van agentische AI:** ServiceNow's Now Assist en Google Gemini Enterprise (GeminiJack) kennen actief misbruikte kwetsbaarheden. Drie AI-codeeragents lekten geheimen via een enkele prompt injection.

---

## 🧠 Technologie & Modellen

**Microsoft MAI-modellen (Build 2026, 2 juni):** Het AI Superintelligence-team van Microsoft heeft zeven nieuwe eigen modellen uitgebracht. MAI-Thinking-1 is het eerste reasoning model van Microsoft: 35B actieve parameters, 256K contextvenster, getraind op clean en commercieel gelicenseerde data. Op SWE Bench Pro haalt het Opus 4.6-niveau; in blind tests wordt het boven Sonnet 4.6 geplaatst. Tegelijk zijn MAI-Image-2.5 en de flash-variant uitgebracht – de eerste Microsoft-modellen voor zowel text-to-image als image-to-image, respectievelijk #2 en #3 op de Arena AI-leaderboard. De modellen zijn beschikbaar via Azure AI Foundry, GitHub Copilot en externe platforms als Fireworks AI en OpenRouter.
→ Bron: [Microsoft Blog – Build 2026](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/) | [TechCrunch](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)

**OpenAI GPT-5.5 en Google Gemini 3.5 Flash:** OpenAI introduceerde GPT-5.5 als "smartest model yet" voor coding, research en data-analyse. Google lanceerde Gemini 3.5 Flash via Google Antigravity (Google's nieuwe AI-platform), beschikbaar voor enterprise-klanten. Apple integreert Gemini in de Foundation Models-framework voor iOS/Xcode (WWDC 2026, 9 juni).
→ Bron: [OpenAI News](https://openai.com/news/) | [Google Blog – WWDC](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/)

**Opmerking:** De modelreleases zijn indrukwekkend in benchmark-termen, maar de echte vraag is welk model wint in productie-context bij enterprise-klanten. MAI-Thinking-1 is relevant als Microsoft dit stevig in M365 Copilot integreert.

---

## 🏛️ Governance & Ethiek

**EU AI Act – Code of Practice transparantie gepubliceerd:** De Europese Commissie publiceerde in juni de Code of Practice on Transparency of AI-generated content. Dit is de praktische handleiding voor naleving van Artikel 50 (transparantievereisten), die per 2 augustus 2026 van kracht wordt. Elke lidstaat moet bovendien vóór 2 augustus een nationale AI-sandbox operationeel hebben.
→ Bron: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/) | [EC Digitale Strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Nederland blokkeert AI-overnames uit onvriendelijke landen:** Het Nederlandse kabinet krijgt per 1 januari de bevoegdheid om overnames van Nederlandse AI-bedrijven door partijen uit landen als China te blokkeren. Minister Herbert breidt de Wet Veiligheidstoets investeringen, fusies en overnames (Vifo) uit.
→ Bron: [Computable.nl](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/)

**Benelux koploper in Europa:** 61% van de Nederlandse en 62% van de Belgische bedrijven heeft AI geïmplementeerd, ruim boven het EU-gemiddelde van 54%. Grootste knelpunt blijft het tekort aan digitaal talent.
→ Bron: [Computable.nl – Benelux koploper](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)

---

## 🔐 Security & Risk

**Prompt injection: geen theorie maar actuele bedreiging:** Drie concrete incidenten domineren het securitylandschap:
1. **ServiceNow Now Assist** – second-order prompt injection maakt privilege-escalatie en data-exfiltratie mogelijk in standaardconfiguraties.
2. **GeminiJack** – kwetsbaarheid in Gemini Enterprise waarmee aanvallers via gedeelde documenten, agenda-uitnodigingen of e-mails gevoelige bedrijfsdata kunnen buitenhalen.
3. **AI coding agents** – drie populaire AI-codeeragents lekten secrets via een enkele kwaadaardige prompt injection; één vendor had het risico al voorspeld in eigen documentatie.

Het UK National Cyber Security Centre stelt dat prompt injection nooit volledig te elimineren is en adviseert risicovermindering als strategie, niet eliminatie.
→ Bron: [TechCrunch – OpenAI over prompt injection](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/) | [VentureBeat – AI agent security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [The Hacker News – ServiceNow](https://thehackernews.com/2026/01/servicenow-patches-critical-ai-platform.html)

**AI versterkt cybercriminaliteit in Benelux:** AI stelt aanvallers in staat meerdere technieken te combineren, waardoor phishing-aanvallen effectiever worden en ransomware geautomatiseerd op schaal ingezet kan worden.
→ Bron: [Data News – cyberaanvallen](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)

---

## 📈 Markt & Adoptie

**Anthropic overtreft OpenAI:** Met $30B ARR (vs. OpenAI's $25B) en een groeifactor van ~10x per jaar (vs. ~3,4x bij OpenAI) is Anthropic nu de meest waardevolle AI-startup ter wereld. De IPO-aanvraag richt zich op een Nasdaq-beursgang in oktober 2026, met Goldman Sachs, JPMorgan en Morgan Stanley als lead underwriters. Drijvende kracht: Claude Code en de snelle enterprise-adoptie van de API.
→ Bron: [TechCrunch – Anthropic IPO](https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/) | [Fortune](https://fortune.com/2026/06/01/anthropic-confidentially-files-ipo-965-billion-valuation/)

**A2A-protocol naar Linux Foundation – industriestandaard voor AI-agenten:** Google heeft het Agent2Agent (A2A) interoperabiliteitsprotocol overgedragen aan de Linux Foundation, waardoor het vendor-agnostisch wordt. Microsoft ondersteunt A2A al in Azure AI Foundry en Copilot Studio. Meer dan 50 partijen – waaronder SAP, Salesforce, ServiceNow, Workday – sluiten aan. Naast A2A wint ook MCP (Model Context Protocol) snel terrein als standaard voor tool-integratie in agenten.
→ Bron: [VentureBeat – A2A & MCP](https://venturebeat.com/ai/ais-big-interoperability-moment-why-a2a-and-mcp-are-key-for-agent-collaboration) | [CIO Dive – Microsoft A2A](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)

**Microsoft Work IQ APIs GA (16 juni):** De Work IQ APIs van Microsoft zijn nu algemeen beschikbaar, waarmee agenten toegang krijgen tot organisatorische context (e-mail, agenda, documenten) via Copilot Studio en GitHub Copilot.
→ Bron: [Microsoft Blog – Build 2026](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)

---

## 💡 Ctac-relevantie

**Agentische AI als dienstverlening – nu is het moment:** De combinatie van A2A als open standaard (Linux Foundation), MCP als tool-protocol, en GA-status van Work IQ APIs betekent dat agentische AI-architecturen rijp worden voor productie. Ctac kan hier proactief op inspelen door een **referentiearchitectuur voor enterprise AI-agenten** te ontwikkelen die A2A + MCP integreert op het Microsoft-platform (Azure AI Foundry, Copilot Studio). Dit is een concreet propositi-ankerpunt richting klanten in de komende kwartalen.

**EU AI Act deadline (2 augustus) – urgente kans voor klantbegeleiding:** Met minder dan twee maanden tot de transparantieverplichtingen van de EU AI Act kunnen Ctac-adviseurs directe waarde leveren aan klanten die hun AI-gegenereerde content nog niet van een label voorzien of hun AI-systeem-inventarisatie niet op orde hebben. De gepubliceerde Code of Practice geeft nu voldoende handvatten voor een gestandaardiseerde audit-aanpak.

**Prompt injection = risico voor elke agentische implementatie:** Ctac moet bij het bouwen of adviseren over AI-agenten standaard een threat model opnemen dat prompt injection adresseert. De ServiceNow en Gemini-kwetsbaarheden tonen aan dat dit ook bij tier-1 enterprise-platforms actueel is. Een security-by-design principe in Ctac's agentische proposities is geen luxe maar vereiste.

**Talent en positionering in Benelux:** Met de Benelux als Europees AI-koploper is de vraag naar implementatiepartners groot – maar het digitaal talenttekort remt door. Dit versterkt de positie van Ctac als partner die kennis en capaciteit combineert, mits de AI-unit snel genoeg opschaalt.

---

## 📚 Bronnen & verder lezen

- [Microsoft Build 2026 – Be yourself at work](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [TechCrunch – Microsoft drie nieuwe foundational models](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)
- [OpenAI News](https://openai.com/news/)
- [Google Blog – Gemini voor Apple developers (WWDC)](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/)
- [TechCrunch – Anthropic raises $65B, IPO](https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/)
- [Fortune – Anthropic files IPO confidentially](https://fortune.com/2026/06/01/anthropic-confidentially-files-ipo-965-billion-valuation/)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/)
- [EC Digitale Strategie – AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Computable.nl – AI-overnames blokkeren](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/)
- [Computable.nl – Benelux koploper](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [VentureBeat – A2A & MCP interoperabiliteit](https://venturebeat.com/ai/ais-big-interoperability-moment-why-a2a-and-mcp-are-key-for-agent-collaboration)
- [CIO Dive – Microsoft + A2A](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [TechCrunch – OpenAI over prompt injection](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)
- [VentureBeat – AI agent security 2026](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Data News – cyberaanvallen door AI](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
