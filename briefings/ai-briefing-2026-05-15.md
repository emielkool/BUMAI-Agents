---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-15
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 15 mei 2026

## 🔑 Highlights van de dag

- **Claude Opus 4.7 beschikbaar** – Anthropic heeft Opus 4.7 uitgebracht met significant verbeterde beeldverwerking en hogere kwaliteit bij professionele taken (docs, slides, interfaces). Beschikbaar via API, Bedrock, Vertex AI én Microsoft Foundry.
- **Microsoft Agent 365 nu algemeen beschikbaar** – Vanaf 1 mei live: een governance-laag voor enterprise AI-agents op $15/user/maand. De bijbehorende M365 E7 "Frontier Suite" kost $99/user/maand en bundelt Copilot, Agent 365 en geavanceerde beveiliging.
- **EU AI Act 'AI omnibus' politiek akkoord** – Op 7 mei bereikten EU-onderhandelaars overeenstemming over vereenvoudiging van de AI-regels én een verbod op 'nudification'-apps. Volledige toepasselijkheid van de AI Act nadert snel: 2 augustus 2026.
- **Prompt injection: geen oplossing in zicht** – Drie AI-coderingsagenten lekten geheimen via één prompt injection-aanval. OpenAI erkent publiekelijk dat het probleem structureel is; Microsoft patcht CVE's maar data lekte desondanks.
- **DeepSeek-V4-Pro** – Open-weight model van 1,6T parameters (49B actief) met 1M-token context, bereikt topscores op codeer- en redeneer-benchmarks en dicht de kloof met gesloten modellen verder.

---

## 🧠 Technologie & Modellen

**Claude Opus 4.7** is Anthropic's nieuwste flagship-model. Verbeteringen zitten vooral in visuele verwerking (hogere resolutie, nauwkeuriger begrip) en de kwaliteit van gegenereerde documenten en interfaces. Het model is breed beschikbaar via alle grote cloud-platformen, wat enterprise-adoptie verlaagt.
→ [Introducing Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)

**DeepSeek-V4-Pro** is vrijgegeven als open-weight model met 1,6 biljoen parameters en een context van één miljoen tokens. Het presteert vergelijkbaar met toonaangevende gesloten modellen op coding- en reasoning-taken, met name relevant voor teams die zelf willen fine-tunen of deployen.
→ [DeepSeek-V4-Pro op Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

**Anthropic Claude voor Small Business** lanceert een bundel connectoren en kant-en-klare workflows voor kleine bedrijven. Strategisch signaal: Anthropic breidt van enterprise naar het MKB en van pure API naar verticaal gerichte producten (ook financiële dienstverlening).
→ [Anthropic nieuws](https://www.anthropic.com/news)

---

## 🏛️ Governance & Ethiek

**EU AI Act 'AI omnibus'** – Op 7 mei bereikte de EU een politiek akkoord over een vereenvoudigingsvoorstel dat administratieve lasten verlaagt voor bedrijven. Onderdeel is ook een verbod op zogenoemde 'nudification'-apps. Met de volledige AI Act-toepassing op **2 augustus 2026** nog maar 79 dagen weg, is dit een cruciaal moment voor compliance-trajecten.
→ [EU AI Act implementatie-tijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
→ [Europese Commissie – AI Act governance](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)

**Nederlandse overheid** – 30% van overheidsinstellingen heeft nog géén beleid voor AI-gebruik, aldus recent onderzoek. Het nieuwe coalitieakkoord noemt een Nederlandse Digitale Dienst die verantwoord AI-gebruik moet bevorderen, maar de uitvoering is traag.
→ [NOS: Overheid maakt volop gebruik van AI, maar kijkt vaak niet naar risico's](https://nos.nl/l/2540979)
→ [Computable: Overheid360° – grip houden op AI](https://www.computable.nl/2026/04/09/overheid360-grip-houden-op-ai-data-en-digitale-autonomie-binnen-de-overheid/)

---

## 🔐 Security & Risk

**Prompt injection blijft structureel probleem.** Drie bekende AI-coderingsagenten (Claude Code, Gemini CLI, GitHub Copilot) lekten tegelijk geheimen via één gecoördineerde prompt injection. Microsoft ontving CVE-2026-21520 (CVSS 7.5) voor Copilot Studio – gepatcht, maar data was al geëxfiltreerd. OpenAI stelt officieel: "Prompt injection is er altijd."
→ [VentureBeat: AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
→ [Airia: AI Security in 2026 – the Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)

**'Promptware' als nieuw aanvalstype.** Bruce Schneier beschrijft een gestructureerde zeven-stappen kill chain waarbij AI-agents fungeren als malware-vector, inclusief laterale beweging door het netwerk. Met de opkomst van agents die e-mail, agenda en ERP-systemen benaderen, groeit het aanvalsoppervlak explosief.
→ [Schneier on Security: The Promptware Kill Chain](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)

---

## 📈 Markt & Adoptie

**Microsoft Agent 365 en M365 E7 algemeen beschikbaar** (GA: 1 mei 2026). Agent 365 ($15/user/maand) is een centrale governance-laag voor alle enterprise-agents met runtime-blokkering via Defender. De E7 "Frontier Suite" ($99/user/maand) bundelt dit met Copilot en Entra. Uitbreiding naar 18 agenttypen (incl. Claude Code en GitHub Copilot CLI) volgt in juni.
→ [VentureBeat: Microsoft Agent 365 GA](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
→ [Microsoft Blog: Frontier Firms operating model](https://blogs.microsoft.com/blog/2026/05/05/how-frontier-firms-are-rebuilding-the-operating-model-for-the-age-of-ai/)

**Google lanceert Agentic Data Cloud en Gemini Enterprise Agent Platform.** Google positioneert legacy enterprise-dataplatformen als "reasoning engines" via een AI-native architectuur. Beide partijen – Microsoft en Google – ondersteunen nu het A2A-interoperabiliteitsprotocol voor agent-to-agent-communicatie.
→ [CIO Dive: Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
→ [CIO Dive: Microsoft commits to Google's A2A protocol](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)

---

## 💡 Ctac-relevantie

**Agent governance is het nieuwe battleground.** De GA van Microsoft Agent 365 is direct relevant voor Ctac's klanten in de enterprise-ruimte: organisaties die nu Copilot uitrollen zullen op korte termijn moeten nadenken over hoe ze AI-agents beheren, beveiligen en auditen. Ctac kan hier een adviesrol pakken — zeker nu de security-risico's (prompt injection, data-exfiltratie) goed gedocumenteerd zijn en de tools beschikbaar komen.

**EU AI Act: augustus 2026 is hard.** Klanten in de overheid, zorg en finance moeten vóór 2 augustus hun hoog-risico AI-systemen hebben geregistreerd en gedocumenteerd. Dit is een concrete propositie voor de AI-unit: een AI Act-gereedheidscheck als kortlopende engagement.

**DeepSeek-V4-Pro en Claude Opus 4.7** zijn beide interessant voor klanten die willen fine-tunen of zelf willen deployen. Open-weight modellen maken serieuze on-premise of private cloud deployments haalbaar — een verhaal dat bij overheids- en zorgsectoren aanslaat.

---

## 📚 Bronnen & verder lezen

- [Introducing Claude Opus 4.7 – Anthropic](https://www.anthropic.com/news/claude-opus-4-7)
- [DeepSeek-V4-Pro – Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [EU AI Act implementatie-tijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act governance & handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [NOS: Overheid en AI-risico's](https://nos.nl/l/2540979)
- [Computable: Overheid360° AI-autonomie](https://www.computable.nl/2026/04/09/overheid360-grip-houden-op-ai-data-en-digitale-autonomie-binnen-de-overheid/)
- [VentureBeat: AI agent runtime security – prompt injection audit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Airia: AI Security 2026 – Prompt Injection Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Schneier: The Promptware Kill Chain](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)
- [VentureBeat: Microsoft Agent 365 GA](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [Microsoft Blog: Frontier Firms & AI operating model](https://blogs.microsoft.com/blog/2026/05/05/how-frontier-firms-are-rebuilding-the-operating-model-for-the-age-of-ai/)
- [CIO Dive: Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [CIO Dive: Microsoft & Google A2A interoperabiliteit](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [TechCrunch: GPT-5.5 release](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)
