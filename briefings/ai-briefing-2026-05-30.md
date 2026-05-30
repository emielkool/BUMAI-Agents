---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-30
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 30 mei 2026

## 🔑 Highlights van de dag

- **Anthropic lanceert Mythos publiek:** Het tot nu toe meest geavanceerde Claude-model is nu publiek beschikbaar. Bijzonder: het model heeft al in early access-fase kwetsbaarheden in legacy financiële systemen opgespoord, wat nieuwe vragen stelt over de rol van frontier-AI bij securityaudits.
- **EU AI Act telt af naar 2 augustus:** Over 64 dagen is de volledige transparantiewetgeving van kracht. Organisaties die AI-systemen inzetten moeten gebruikers informeren en synthetische content markeren — de nalevingsdeadline is nú concreet.
- **Microsoft Agent 365 nu algemeen beschikbaar:** De governance-laag voor AI-agents ($15/gebruiker) is vanaf 1 mei GA. Tienduizenden enterprise-klanten beheren er al agents mee — dit wordt de standaard control plane voor Copilot-omgevingen.
- **RSI vervangt AGI als buzzword:** "Recursive Self-Improvement" duikt op in de roadmaps van AI-startups. Google-CEO Pichai tempert de verwachtingen: "we zijn er nog niet", maar de terminologieverandering signaleert een verhoogde ambitie in het veld.
- **Prompt injection: aanvalspercentage boven 85%:** NIST noemt het "de grootste beveiligingsfout van generatieve AI" en ondanks vele defensies slagen adaptieve aanvallen in meer dan 85% van de gevallen — een structureel risico bij elke agentische inzet.

---

## 🧠 Technologie & Modellen

**Anthropic Mythos – publiek beschikbaar**
Na een beperkte release aan partners is Anthropic's meest krachtige model nu openbaar. De aankondiging valt samen met twee nieuwe enterprise-mogelijkheden op het Claude Platform: *self-hosted sandboxes* (public beta) laten bedrijven agent-tooling op eigen infrastructuur draaien, en *MCP tunnels* (research preview) geven agents toegang tot private Model Context Protocol servers zonder publiek internet. Dit is een directe stap richting veilige, soevereine AI-deployments voor de enterprise. ([Anthropic](https://www.anthropic.com/news/claude-opus-4-7))

**RSI: de opvolger van AGI-hype?**
TechCrunch signaleert op 28 mei dat "Recursive Self-Improvement" de nieuwe containerbegrip wordt in AI-roadmaps. Startup Recursive Superintelligence heeft RSI als expliciete doelstelling, en DeepMind's Demis Hassabis verschoof zijn AGI-tijdlijn naar "reële mogelijkheid in 2029". Het begrip verdient kritische blik: net als AGI dreigt RSI een marketinglabel te worden dat weinig operationele houvast biedt. ([TechCrunch, 28 mei](https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/))

**OpenAI's Frontier Governance Framework**
OpenAI publiceerde op 28 mei zijn Frontier Governance Framework, tegelijk met een samenwerking met Rosalind Biodefense gericht op maatschappelijke weerbaarheid. Dit past in de bredere beweging waarbij grote AI-labs proactief governancekaders publiceren — deels om regulering voor te zijn. ([OpenAI News](https://openai.com/news/))

---

## 🏛️ Governance & Ethiek

**EU AI Act: D-65 voor transparantieverplichting**
Op 2 augustus 2026 treedt de volledige transparantiewetgeving van de EU AI Act in werking. Concrete verplichtingen: aanbieders van AI-systemen moeten gebruikers informeren dat ze met AI interacteren, synthetische content moet machineleesbaar worden gemarkeerd, en deployers moeten mensen waarschuwen bij deepfakes of AI-gegenereerde publicaties over publieke belangen. Iedere EU-lidstaat moet voor die datum ook een nationale AI-regulatory sandbox operationeel hebben. ([EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/), [Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

**VS test frontier-modellen voor nationale veiligheid**
De Amerikaanse overheid eist dat Google, Microsoft en xAI hun frontier-modellen vroegtijdig beschikbaar stellen aan regulators voor veiligheidstests. Dit is een precedent dat ook in Europa navolging kan krijgen onder de AI Act-auditmechanismen voor high-risk toepassingen. ([CIO Dive](https://www.ciodive.com/news/Google-Microsoft-xAI-to-face-security-testing/819375/))

---

## 🔐 Security & Risk

**Prompt injection: structureel onopgelost**
Meta-analyse over 2021–2026 toont aanvalspercentages boven 85% bij adaptieve aanvallen op state-of-the-art verdedigingen. NIST classificeert het als "generatieve AI's grootste beveiligingsfout"; OWASP plaatst het op #1 in de LLM Top 10. OpenAI stelt dat het probleem "net als social engineering waarschijnlijk nooit volledig opgelost wordt." ([VentureBeat Security](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026), [TechCrunch](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/))

**AI-agents lekten secrets via prompt injection**
VentureBeat rapporteerde dat drie AI-coding agents via één prompt injection-aanval secrets blootgaven. Opmerkelijk: Anthropic's eigen system card voor de getroffen tool vermeldde expliciet dat het systeem "not hardened against prompt injection" is. Transparantie over kwetsbaarheden is toe te juichen, maar het onderstreept dat "agent-ready" nog niet "production-secure" betekent. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

---

## 📈 Markt & Adoptie

**Microsoft Agent 365 – de governance-laag voor AI-agents**
Algemeen beschikbaar sinds 1 mei als onderdeel van de Microsoft 365 E7 Frontier Suite ($15/gebruiker). In de preview-fase registreerden al tientallen miljoenen agents zich in de Agent 365 Registry, met tienduizenden enterprise-klanten actief. Dit positioneert Microsoft als de standaard voor agent-governance — een strategische zet die de Copilot-inzet bij grote organisaties verankert. ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/), [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

**Google Agentic Data Cloud**
Gepresenteerd op Google Cloud Next '26: een AI-native architectuur die legacy data platforms omzet naar "reasoning engines". Samen met het Gemini Enterprise Agent Platform (volgende stap van Vertex AI) zet Google in op het agentic tijdperk voor enterprise-data — direct concurrerend met Microsoft Fabric en Azure AI Foundry. ([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))

---

## 💡 Ctac-relevantie

**Governance van AI-agents wordt een must-have, niet nice-to-have.** De combinatie van Microsoft Agent 365 (GA) en Google's Agentic Data Cloud laat zien dat de markt verschuift van experimentele pilots naar gestructureerde agent-deployments met observability, toegangsbeheer en audittrails. Voor Ctac is dit een concrete propositiekans: klanten die Copilot of Azure AI al inzetten hebben nu behoefte aan een governancelaag — en dat is precies waar Ctac als implementatiepartner waarde kan toevoegen.

**De EU AI Act-deadline van 2 augustus is nú werkbaar.** Met 64 dagen te gaan moeten klanten in gereguleerde sectoren (overheid, finance, zorg) actie ondernemen op transparantievereisten. Ctac kan hier als trusted advisor optreden: een snelle compliance-quickscan of transparantie-implementatie biedt lage drempel, directe waarde en opening voor diepere AI-trajecten.

**Prompt injection als risico bij elke agentische deployment.** Bij elke klant die AI-agents inzet (ook intern bij Ctac) moet dit expliciet worden meegenomen in de architectuurreview. Anthropic's self-hosted sandboxes en MCP tunnels bieden een veelbelovende mitigatieroute voor enterprise-scenario's met gevoelige data.

---

## 📚 Bronnen & verder lezen

- [Anthropic Claude Opus 4.7 aankondiging](https://www.anthropic.com/news/claude-opus-4-7)
- [TechCrunch: RSI is the new AGI (28 mei 2026)](https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Europese Commissie: AI Act guidelines](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [VentureBeat: 11 runtime attacks breaking AI security](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)
- [VentureBeat: AI agents lekten secrets via prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Microsoft Blog: Frontier Suite + Agent 365](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)
- [CIO Dive: Microsoft en Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive: Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [CIO Dive: Google, Microsoft en xAI onder security-tests VS](https://www.ciodive.com/news/Google-Microsoft-xAI-to-face-security-testing/819375/)
- [OpenAI nieuws](https://openai.com/news/)
