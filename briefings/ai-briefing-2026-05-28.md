---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-28
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 28 mei 2026

## 🔑 Highlights van de dag

- **Google kiest definitief voor agents boven chatbots** – Op Google I/O (19 mei) presenteerde Google Gemini 3.5 Flash, Gemini Omni en de Gemini Spark-assistent als 24/7 actieve agent, plus het Antigravity developer-platform. De strategische boodschap was helder: het chatbot-tijdperk is voorbij.
- **Microsoft Agent 365 live per 1 mei** – De controle-laag voor AI-agents in M365-omgevingen ($15/user/maand) en het bijbehorende M365 E7 Frontier Suite-abonnement ($99/user) zijn algemeen beschikbaar. Dit is de enterprise-ingang voor beheerd agent-gebruik.
- **EU AI Act Omnibus: akkoord bereikt** – Op 7 mei werd politiek overeenstemming bereikt over een vereenvoudigingspakket voor de AI Act. Volledige toepasselijkheid blijft 2 augustus 2026, maar technische standaarden (CEN/CENELEC) lopen vertraging op wat de high-risk compliance deadline in gevaar brengt.
- **Anthropic Mythos: AI vindt duizenden zero-days autonoom** – Anthropic's geheime frontier-model Mythos Preview ontdekte in korte tijd kritieke kwetsbaarheden in alle grote besturingssystemen en browsers, waaronder een 17 jaar oude RCE-bug in FreeBSD. Het model is te gevaarlijk voor publieke release; Anthropic lanceerde Project Glasswing als afgegrensd veiligheidsprogramma.
- **Prompt injection: aanvalssucces >85%** – Een meta-analyse van 78 recente studies toont dat geavanceerde prompt injection-aanvallen meer dan 85% slagingspercentage halen tegen state-of-the-art verdedigingen. Kritieke kwetsbaarheden zijn ook gevonden in Amazon Q Developer, Google Jules en GitHub Copilot.

---

## 🧠 Technologie & Modellen

**Google I/O 2026 – het agent-tijdperk**
Google presenteerde vorige week een volledig herbouwde AI-stack. **Gemini 3.5 Flash** combineert frontier-intelligentie met actie-capaciteiten (tool use, code-executie). **Gemini Omni** verwerkt elke input-modaliteit inclusief video-editing. Belangrijker nog: **Gemini Spark** is een 24/7 persoonlijke agent die actief taken uitvoert – niet reageert op prompts, maar pro-actief handelt. Voor ontwikkelaars introduceert Google **Antigravity** als enig unified agent-platform, met Managed Agents in de Gemini API die geïsoleerde Linux-omgevingen per aanroep opstarten.
→ *Bron: [Google I/O 2026 announcements](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/) | [Gemini 3.5 Flash – TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/)*

**Open-source agentic modellen rijpen**
**Devstral** (Mistral) is specifiek gebouwd voor agentic software engineering: codebase-exploratie, multi-file edits, bugfixes met tools. **DeepSeek-V4-Pro** biedt 1M token context, tot 384K output, tool calls en zowel thinking als non-thinking modes – serieuze productierijpe optie voor lokale of private deployment.
→ *Bron: [Hugging Face – best open-source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)*

---

## 🏛️ Governance & Ethiek

**EU AI Act Omnibus: vereenvoudiging maar ook uitstelrisico**
Het politieke akkoord van 7 mei vereenvoudigt implementatievereisten, maar de technische standaarden van CEN/CENELEC zijn nog niet klaar – ze zouden er augustus 2025 al zijn. Dit brengt de high-risk deadline van **2 augustus 2026** in gevaar: organisaties die high-risk AI inzetten weten niet precies waaraan ze moeten voldoen. De EU AI Office handhaaft GPAI-model-verplichtingen wel per die datum.
→ *Bron: [artificialintelligenceact.eu – implementatie](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/) | [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)*

**Paus Leo XIV publiceert encycliek over AI**
De eerste encycliek van paus Leo XIV ('Magnifica Humanitas') richt zich op AI en de bedreiging voor menselijke solidariteit. Geen directe compliance-impact, maar illustreert hoe breed maatschappelijk de roep om AI-ethiek nu klinkt.
→ *Bron: [National Catholic Reporter](https://www.ncronline.org/vatican/vatican-news/pope-leo-calls-disarm-ai-major-document-warns-technologic-threats-humanity)*

---

## 🔐 Security & Risk

**Project Glasswing: defensief AI vs. gevaarlijke capaciteiten**
Anthropic's Mythos Preview ontdekte autonomously duizenden zero-day kwetsbaarheden, inclusief CVE-2026-4747 (17-jarige RCE in FreeBSD). Het model is zo gevaarlijk dat het niet openbaar wordt gemaakt; in plaats daarvan lanceerde Anthropic Project Glasswing met AWS, Apple, Cisco, CrowdStrike, Google, Microsoft en NVIDIA als partners om kritieke software proactief te beveiligen. Kritieke noot: een ongeautoriseerde groep heeft al toegang gekregen tot Mythos, wat de risico's van model-proliferatie onderstreept.
→ *Bron: [Anthropic Glasswing](https://www.anthropic.com/glasswing) | [TechCrunch – Mythos](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) | [TechCrunch – unauthorized access](https://techcrunch.com/2026/04/21/unauthorized-group-has-gained-access-to-anthropics-exclusive-cyber-tool-mythos-report-claims/)*

**Prompt injection: de structurele zwakte van AI-agents**
Meta-analyse van 78 studies: >85% aanvalssucces bij adaptieve prompt injection-aanvallen. NIST noemt het "generative AI's greatest security flaw". Kritieke lekken gevonden in Amazon Q Developer, Google Jules en GitHub Copilot. Organisaties dienen per augustus 2026 voor EU AI Act high-risk compliance een "quantified injection resistance rate" te kunnen aantonen.
→ *Bron: [VentureBeat – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [Schneier on Security](https://www.schneier.com/blog/archives/2026/01/ais-are-getting-better-at-finding-and-exploiting-security-vulnerabilities.html)*

---

## 📈 Markt & Adoptie

**Microsoft Agent 365 + M365 E7 nu algemeen beschikbaar**
Microsoft positioneert Agent 365 ($15/user) als de enterprise governance-laag voor alle AI-agents binnen een organisatie: observeren, beveiligen en beheren vanuit één console. M365 E7 ($99/user) bundelt dit met Copilot-functionaliteit. Tienduizenden klanten zijn al in adoptie. Dit is een directe enterprise-landingsbaan voor AI-implementaties.
→ *Bron: [Microsoft Blog – Frontier Suite](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)*

**KPMG integreert Claude in volledige workforce**
KPMG heeft een strategische alliantie gesloten met Anthropic waarbij Claude wordt geïntegreerd in de kernworkflows van alle 276.000 medewerkers. Dit is een signaal dat grote professionele dienstverleners AI niet meer als experiment behandelen maar als bedrijfskritische infrastructuur.
→ *Bron: [Anthropic nieuws](https://www.anthropic.com/news)*

**AI-adoptie stijgt: 17,8% van wereldse beroepsbevolking**
Microsoft rapporteert in zijn State of Global AI Diffusion-rapport dat het AI-gebruik in Q1 2026 steeg van 16,3% naar 17,8% van de werkende wereldbevolking – een structureel stijgende trend.
→ *Bron: [Microsoft On the Issues – AI diffusion 2026](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)*

---

## 💡 Ctac-relevantie

**Drie directe aanknopingspunten deze week:**

1. **Microsoft Agent 365 is nu beschikbaar** – De meeste Ctac-klanten zitten al in M365. Agent 365 biedt een beheerde ingang voor agent-implementatie met centrale governance. Ctac kan hier een implementatie- en adoptiepropositie op bouwen: van licentieadvies tot inrichting van governance-policies en change management. De prijs ($15/user) is laagdrempelig genoeg voor brede uitrol.

2. **EU AI Act deadline 2 augustus – urgente compliance-opdracht** – De vertraging in technische standaarden creëert onzekerheid, maar de deadline voor GPAI-modellen en (deels) high-risk systemen staat vast. Ctac-klanten in overheid, zorg en finance die AI inzetten hebben nu minder dan 10 weken. Een AI Act readiness-scan of gap-assessment is een concreet, afgebakend aanbod met duidelijke tijdsdruk.

3. **Security als onderscheidend thema** – De combinatie van Project Glasswing en de prompt injection-cijfers maakt duidelijk dat AI-veiligheid een zelfstandig vakgebied wordt. Ctac kan AI-security positioneren als onderdeel van elke agent-implementatie, in lijn met het groeiende enterprise-bewustzijn hierover (ook richting klanten die al Copilot of andere agents inzetten).

---

## 📚 Bronnen & verder lezen

- [Google I/O 2026 – alle aankondigingen](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Gemini 3.5 Flash – TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/)
- [Gemini Spark – TechCrunch](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/)
- [Microsoft Frontier Suite blog](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)
- [Microsoft – State of Global AI Diffusion 2026](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)
- [Anthropic Project Glasswing](https://www.anthropic.com/glasswing)
- [Claude Mythos Preview – red.anthropic.com](https://red.anthropic.com/2026/mythos-preview/)
- [TechCrunch – Mythos cybersecurity](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [TechCrunch – Mythos unauthorized access](https://techcrunch.com/2026/04/21/unauthorized-group-has-gained-access-to-anthropics-exclusive-cyber-tool-mythos-report-claims/)
- [VentureBeat – AI agent security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Schneier on Security – AI exploits](https://www.schneier.com/blog/archives/2026/01/ais-are-getting-better-at-finding-and-exploiting-security-vulnerabilities.html)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/)
- [EC – AI Act governance](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Hugging Face – beste open-source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
