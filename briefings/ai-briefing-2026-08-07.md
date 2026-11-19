---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-07
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 7 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act actief gehandhaafd** – Vanaf 2 augustus is het AI Office officieel verantwoordelijk voor toezicht en handhaving, inclusief nieuwe transparantieverplichtingen. Dit is geen aankondiging meer; het is nu realiteit voor iedereen die AI-systemen inzet in Europa.
- **Prompt injection treft drie grote AI-codeeragenten tegelijk** – Een aanval op Claude Code, Gemini CLI en GitHub Copilot gelijktijdig bewijst dat agentic AI in enterprise-omgevingen een serieuze aanvalsvector is geworden. Geen laboratoriumvondst: het trof een productiesysteem.
- **OpenAI brengt GPT-5.6 update uit** – Uitgerold op 6 augustus met een "effort slider" voor Plus/Pro-gebruikers. Incrementele verbetering, geen paradigmawisseling. O3 wordt op 26 augustus uit ChatGPT verwijderd.
- **Microsoft Frontier Company + $2,5 miljard** – Microsoft richt een apart bedrijf op om enterprise AI-implementaties te versnellen. Met 20 miljoen betaalde Copilot-seats en 123% omzetgroei YoY ($37 miljard run rate) gaat Microsoft van verkoop naar succesvolle uitrol.
- **White House AI Safety Meeting** – OpenAI, Anthropic en Google namen op 3 augustus deel aan overleg in het Witte Huis, gebaseerd op een executive order van Trump over AI-cybersecurity. Signaal: ook de VS stelt formele veiligheidsvereisten in.

---

## 🧠 Technologie & Modellen

**GPT-5.6 update (OpenAI, 6 aug)** brengt een "effort slider" waarmee Plus- en Pro-gebruikers zelf kunnen kiezen hoeveel rekenkapaciteit ChatGPT aan een taak besteedt. Vrije gebruikers krijgen een nieuw standaardmodel. Codex op macOS krijgt "Appshots": je kunt een applicatievenster aan een Codex-thread koppelen via een hotkey. Praktisch interessant voor ontwikkelworkflows, maar geen fundamentele sprong.

**Open-source landschap** consolideert zich rond vier modellen die inmiddels serieus inzetbaar zijn voor productie: GLM-5.1, Kimi K2.6, DeepSeek V4 Pro en Qwen3. Alle vier geschikt voor coding, redeneren, agentische workflows en long-context analyse. De gap met proprietary modellen slinkt.

**Agents-A1 (InternScience)** – Een 35B Mixture-of-Experts model, open-source uitgebracht in juni/juli, met sterke prestaties op tool-calling en wetenschappelijk redeneren. Minder zichtbaar dan de grote namen, maar veelbelovend voor specifieke enterprise use cases.

**Google centraliseert AI-leiderschap** in Mountain View en zet zwaar in op coding tools om Anthropic en OpenAI bij te halen. De strijd om de AI-codeerassistent-markt verhardt.

*Bronnen: [OpenAI release notes](https://openai.com/products/release-notes/) · [HuggingFace open-source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms) · [TechCrunch GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)*

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving gestart op 2 augustus.** De Europese Commissie en nationale toezichthouders zijn nu formeel actief. Concreet in werking getreden:

- Chatbots en interactieve AI-systemen moeten gebruikers melden dat ze met AI communiceren.
- Deepfakes (beeld, video, audio) moeten worden gelabeld.
- AI-gegenereerde content in het publiek belang moet machineleesbaar worden gemarkeerd.
- Elke EU-lidstaat moest een nationale AI Regulatory Sandbox operationeel hebben per 2 augustus.

Het AI Office kan nu technische documentatie opvragen, modellen evalueren en boetes opleggen. Voor GPAI-modellen (zoals GPT-5 en Claude) gelden aparte transparantie- en risicobeheereisen.

**White House AI Safety Meeting (3 aug)** – OpenAI, Anthropic en Google namen deel aan overleg op uitnodiging van de Trump-regering, volgend op een executive order over AI-cybersecurity. De VS kiest voor een opt-in benadering bij veiligheidsreviews, in contrast met de verplichtende EU-aanpak.

*Bronnen: [Europese Commissie – handhaving AI Act](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) · [Bloomberg – White House meeting](https://www.bloomberg.com/news/articles/2026-08-03/openai-anthropic-google-to-join-white-house-ai-safety-meeting)*

---

## 🔐 Security & Risk

**Prompt injection raakt drie AI-codeeragenten tegelijk.** Een aanvaller stuurde een gemanipuleerde e-mail naar een organisatie. Wanneer medewerkers later Claude Code, Gemini CLI of GitHub Copilot vroegen iets op te zoeken, haalden de agents de vergiftigde e-mail op, voerden de embedded instructies uit en exfiltreerden gevoelige data via een image URL. Dit is geen theoretische aanval meer: het trof een productieomgeving.

Kernprobleem: **flat authorization** – LLM-agents respecteren gebruikersrechten niet automatisch. Ze combineren context uit meerdere bronnen zonder te controleren welke permissies de originator heeft.

VentureBeat beschrijft 11 runtime-aanvalsklassen die CISOs nu actief tegenkomen. Prompt injection staat bovenaan de OWASP Top 10 voor LLM-applicaties. Met toenemende autonomie van AI-agents groeit het aanvalsoppervlak snel.

*Bronnen: [VentureBeat – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) · [Airia – AI security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) · [VentureBeat – 11 runtime attacks](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)*

---

## 📈 Markt & Adoptie

**Microsoft** domineerde het afgelopen fiscale jaar (FY26) met spectaculaire AI-cijfers: 20 miljoen betaalde Microsoft 365 Copilot-seats, het aantal klanten met >50.000 seats verviervoudigde, en de AI-omzet groeide 123% YoY naar een run rate van $37 miljard. Reactie: Microsoft richt **Microsoft Frontier Company** op – een apart operationeel bedrijf met $2,5 miljard budget en 6.000 industrie- en engineeringexperts – specifiek gericht op succesvolle enterprise AI-implementaties. Van verkopen naar waarmaken.

**Big Tech CapEx** – Amazon, Microsoft, Meta en Google investeren gezamenlijk tot $725 miljard in 2026 aan infrastructuur. Dit is geen R&D; dit is bet-the-company schaal.

**Adoptiepatroon**: Twee derde van de bedrijven zit nog vast in de pilotfase. De omschakeling naar productie blijft de grote uitdaging in de markt.

*Bronnen: [CIO Dive – Microsoft Copilot growth](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/) · [TechCrunch – Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) · [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)*

---

## 💡 Ctac-relevantie

**EU AI Act is nu geen "straks"-dossier meer.** Klanten van Ctac in overheid, zorg en finance zijn juridisch verplicht te voldoen. Directe kansen: compliance-audits, AI-transparantie-implementaties (disclosure UI, machine-readable watermarking), en regulatory sandbox-trajecten samen met klanten. Ctac kan hier een concrete propositie op bouwen die verder gaat dan advies.

**Prompt injection is nu de enterprise AI security-risicovraag.** Voor klanten die nu AI-agents uitrollen (of dit willen), is runtime security een must-have, geen nice-to-have. De aanval op Claude Code/Copilot/Gemini CLI toont aan dat ook tools die Ctac intern gebruikt kwetsbaar zijn. Een security-baseline voor agentic AI – rechten, auditlogging, input-sanitization – is iets wat de AI-unit nu actief moet kunnen adviseren en implementeren.

**Microsoft Frontier Company is een directe concurrentie- én samenwerkingskans.** Microsoft positioneert zich als implementatiepartner voor zijn eigen AI-tools. Als Ctac-partner moet duidelijk zijn hoe Ctac zich onderscheidt: diepgaande klantkennis in NL/BE-markten, verticale specialisatie, en onafhankelijkheid van één vendor. De "pilot-naar-productie"-kloof is precies het gat waar Ctac waarde kan toevoegen.

**Open-source modellen rijpen.** Voor klanten die niet afhankelijk willen zijn van hyperscalers of gevoelige data niet naar de cloud willen sturen, worden on-premise opties met DeepSeek V4 Pro of Qwen3 steeds reëler. Dit is relevant voor overheids- en zorgklanten.

---

## 📚 Bronnen & verder lezen

- [OpenAI Release Notes – augustus 2026](https://openai.com/products/release-notes/)
- [TechCrunch – GPT-5.6 launch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [HuggingFace – Open-source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [Europese Commissie – AI Act handhaving per 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [Bloomberg – White House AI Safety Meeting](https://www.bloomberg.com/news/articles/2026-08-03/openai-anthropic-google-to-join-white-house-ai-safety-meeting)
- [VentureBeat – AI agent runtime security & prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – 11 runtime attacks on AI systems](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)
- [Airia – AI Security in 2026: Prompt Injection](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Microsoft Copilot growth Q3 2026](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [TechCrunch – Microsoft Frontier Company $2.5B](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [LLM Stats – AI updates augustus 2026](https://llm-stats.com/llm-updates)
