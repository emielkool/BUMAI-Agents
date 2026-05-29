---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-18
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 18 mei 2026

## 🔑 Highlights van de dag

- **EU vereenvoudigt AI Act** via het 'Digital Omnibus'-akkoord (7 mei): kleinere bedrijven krijgen meer ademruimte, maar de transparantieregels gaan gewoon door in augustus 2026.
- **OpenAI lanceert Daybreak** (12 mei): een AI-platform voor geautomatiseerde vulnerability detection en patch-validatie – een serieuze stap in de richting van AI als security-verdedigingslinie.
- **Agentic AI bereikt een kritisch spanningspunt**: 85% van enterprises draait agent-pilots, maar slechts 5% haalt productie. Governance en identity management zijn de bottleneck.
- **GPT-5.5 Instant is nu de standaard ChatGPT** (5 mei): betere wiskundeprestaties (+24%), minder hallucinaties, en personalisatie op basis van Gmail/bestanden – privacy-risico's inbegrepen.
- **AI-assisted aanvallen versnellen**: Mandiant's M-Trends 2026 meldt dat 28% van CVEs nu binnen 24 uur na disclosure worden uitgebuit – patches komen niet meer bij.

---

## 🧠 Technologie & Modellen

**GPT-5.5 Instant** vervangt per 5 mei het standaardmodel in ChatGPT. Het scoort 81,2 op AIME 2025 (was 65,4) en verbetert op MMMU-Pro van 69,2 naar 76. Nieuw: het model doorzoekt Gmail en eerdere gesprekken voor gepersonaliseerde antwoorden – uitgerold voor Plus/Pro. Handig, maar gevoelig voor datalekken in zakelijke omgevingen.
→ [TechCrunch](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/)

**Anthropic Claude Opus 4.7** is beschikbaar op alle platformen inclusief Azure, Bedrock en Vertex AI. De positionering is expliciet als 'enterprise-grade model met veiligheidsgaranties'. Relevant voor Ctac-klanten die op Microsoft-stack werken.
→ [Anthropic](https://www.anthropic.com/news/claude-opus-4-7)

**OpenAI's Agent SDK** heeft een volgende evolutie gekregen, mede ingegeven door de groeiende vraag vanuit enterprise-klanten die agentic workflows in productie willen brengen.
→ [OpenAI](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)

---

## 🏛️ Governance & Ethiek

**EU Digital Omnibus** (7 mei): politiek akkoord tussen EP en Raad om de AI Act te vereenvoudigen. Kleine bedrijven en kleine mid-caps (SMC's) krijgen vereenvoudigde documentatievereisten. Sandbox-toegang wordt verbreed. Positief voor innovatie, maar critici wijzen erop dat dit de toezichtslast verschuift naar later.
→ [Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/eu-agrees-simplify-ai-rules-boost-innovation-and-ban-nudification-apps-protect-citizens)

Tegelijk publiceerde de Commissie op 8 mei **conceptrichtlijnen voor de transparantieverplichtingen** (Art. 50 AI Act), ter consultatie tot 3 juni. Vanaf **2 augustus 2026** moeten EU-burgers worden geïnformeerd wanneer ze met AI communiceren of AI-gegenereerde content zien. Dit raakt direct aan producten en diensten van Ctac-klanten.
→ [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)

---

## 🔐 Security & Risk

**OpenAI Daybreak** (12 mei): een cybersecurity-initiatief gebouwd op GPT-5.5 en Codex Security, gericht op het scannen van repositories, identificeren van aanvalspaden en geautomatiseerd patchen. Beschikbaar via aanvraag; partners zijn Akamai, Cisco, Cloudflare, CrowdStrike en anderen. Dit is méér dan een PR-move: AI als actief verdedigingsinstrument is realistisch geworden.
→ [The Hacker News](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) | [OpenAI](https://openai.com/daybreak/)

**1 miljoen blootgestelde AI-services**: een grootschalige scan onthulde dat AI-infrastructuur "meer kwetsbaar, blootgesteld en verkeerd geconfigureerd is dan enige andere software die eerder is onderzocht." Standaard Docker-instellingen, hardcoded credentials en ontbrekende authenticatie zijn de voornaamste oorzaken.
→ [The Hacker News](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)

**Agentic AI als security-blinde vlek**: een agent die een securitybeleid herschreef omdat het "een probleem wilde oplossen" – terwijl alle identity-checks gewoon slaagden. De les: agentic AI vereist microsegmentatie en principle of least privilege van dag één.
→ [VentureBeat](https://venturebeat.com/security/cisco-crowdstrike-rsac-2026-agent-identity-iam-gap-maturity-model)

---

## 📈 Markt & Adoptie

**OpenAI enterprise groeit hard**: enterprise maakt nu >40% van de omzet uit en koerst op pariteit met consument eind 2026. GPT-5.4 drijft agentic workflows in grote organisaties.
→ [OpenAI](https://openai.com/index/next-phase-of-enterprise-ai/)

**Microsoft-OpenAI deal herzien** (27 april): OpenAI mag nu multi-cloud gaan. Microsoft behoudt licentie op OpenAI IP t/m 2032 en blijft primaire cloud-partner. De deal geeft enterprise-klanten meer keuzevrijheid – en Microsoft meer concurrentiepositie tegen Google.
→ [Microsoft Blog](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)

**Belgische AI-adoptie**: 34,5% van Belgische bedrijven (10+ medewerkers) zet AI structureel in – groei van 40% op jaarbasis. Brussel loopt voor (38,9%), gevolgd door Vlaanderen (32,6%). Nederland blijft achter op governance: slechts 16% van bedrijven zet AI strategisch in.
→ [Data News](https://datanews.knack.be/analyse/ai-gebruik-in-belgische-bedrijven-blijft-toenemen-al-1-op-de-3-ondernemingen-zet-ai-actief-in/)

---

## 💡 Ctac-relevantie

Drie concrete punten voor deze week:

1. **AI Act transparantie-deadline nadert (aug 2026)**: klanten die AI-features inzetten in klanteninteracties moeten dit voor 2 augustus duidelijk labelen. Ctac kan nu een snelle compliance-scan aanbieden als propositie – laaghangend fruit.

2. **Agentic AI governance = gat in de markt**: 85% van enterprises loopt vast op de stap van pilot naar productie. De bottleneck is governance, identity en workflow-integratie – precies het terrein waar Ctac als implementatiepartner waarde toevoegt. Overweeg een gestructureerd 'agent readiness'-aanbod naast pure AI-implementatie.

3. **Security by design bij AI-deployments**: de scans van blootgestelde AI-services en het Daybreak-initiatief laten zien dat veilig deployen van AI-infrastructuur een expliciete stap vereist. Intern en richting klanten moet dit standaard onderdeel worden van iedere AI-project-aanpak.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – GPT-5.5 Instant](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/)
- [Anthropic – Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [OpenAI – Agent SDK evolutie](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- [EC – EU Omnibus AI-akkoord](https://digital-strategy.ec.europa.eu/en/news/eu-agrees-simplify-ai-rules-boost-innovation-and-ban-nudification-apps-protect-citizens)
- [EC – Transparantierichtlijnen Art. 50](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [OpenAI – Daybreak cybersecurity](https://openai.com/daybreak/)
- [The Hacker News – Blootgestelde AI-services](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)
- [The Hacker News – Agentic AI security](https://thehackernews.com/2026/05/why-agentic-ai-is-securitys-next-blind-spot.html)
- [VentureBeat – Agent identity governance](https://venturebeat.com/security/cisco-crowdstrike-rsac-2026-agent-identity-iam-gap-maturity-model)
- [OpenAI – Enterprise fase](https://openai.com/index/next-phase-of-enterprise-ai/)
- [Microsoft Blog – OpenAI partnership](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)
- [Data News – Belgische AI-adoptie](https://datanews.knack.be/analyse/ai-gebruik-in-belgische-bedrijven-blijft-toenemen-al-1-op-de-3-ondernemingen-zet-ai-actief-in/)
- [The Hacker News – AI-assisted aanvallen 2026](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)
