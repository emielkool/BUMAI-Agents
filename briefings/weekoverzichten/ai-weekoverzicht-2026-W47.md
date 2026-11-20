---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W47
Datum: 2026-11-20
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 47, 2026

> Synthese van de AI-ontwikkelingen van 16 november t/m 20 november 2026.
> *Let op: er zijn voor deze week geen afzonderlijke dagbriefings beschikbaar. Dit weekoverzicht is op basis van directe websearch samengesteld.*

## 🏆 Weekhighlights

1. **OpenAI lanceert GPT-6.2 Astra & Sol (17 nov)** – OpenAI bracht twee nieuwe varianten uit binnen de GPT-6-familie: GPT-6.2 Astra (gericht op lange agent-taken) en GPT-6.2 Sol (lagere kosten per taak). Alibaba deed hetzelfde met Qwen4-Max op 16 november – de eerste release zonder open weights in de Qwen4-generatie. De race naar goedkopere, langlopende agentic workloads is in volle gang.

2. **Enterprise AI-spending bereikt $177 miljard – 5,4x groei in één jaar (Menlo Ventures)** – De jaarlijkse State of Enterprise AI report toont explosieve groei: Anthropic, OpenAI en Google beheersen 69% van de enterprise-spend. Toch rapporteert 79% van de organisaties adoptie-uitdagingen en koppelt slechts 15% AI-investeringen aan meetbare financiële resultaten. Hype is reëel, maar rendement blijft moeilijk aantoonbaar.

3. **CISA voegt LiteLLM-lek toe aan actief-uitgebuite kwetsbaarheden (18 nov)** – CVE-2026-40217 in de LiteLLM AI-gateway staat nu op de CISA KEV-lijst met een deadline van 2 december voor federale agencies. Op 17 november werd ook een gekapt Microsoft agent-framework-pakket op PyPI gepubliceerd. AI-tooling is een aanvalsoppervlak geworden dat organisaties actief moeten patchen.

4. **EU Digital Fairness Act gepubliceerd; AI Act enforcement loopt (11 nov)** – De Europese Commissie diende op 11 november de Digital Fairness Act in (dark patterns, gerichte reclame aan minderjarigen). Op 5 november kwamen richtsnoeren over de definitie van een AI-systeem onder de AI Act. Organisaties die nog niet bezig zijn met compliance-mapping lopen achter op de planning voor de hoge-risico-verplichtingen (2027–2028).

5. **Infrastructuurverschuiving: 55% wil AI on-premises (Schneider/Omdia, 18 nov)** – Meer dan de helft van de ondervraagde enterprise-beslissers geeft de voorkeur aan eigen infrastructuur voor agentic workloads, deels vanwege datasouvereiniteit. Agentic workloads vragen bovendien om meer dan GPU's: CPU-capaciteit en secure execution-omgevingen worden steeds kritischer.

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De week tekent zich af als een typische "dichte release-week" in een reeds volle modellen-kalender. OpenAI (GPT-6.2 Astra/Sol), Alibaba (Qwen4-Max) en Google (Gemini 4 Neon, 18 nov) brachten elk een nieuwe variant. De rode draad: alle releases richten zich op *agentic efficiency* – lagere kostprijs per langlopende taak. Modelkwaliteit is geen onderscheidende factor meer; het gevecht gaat om prijs-per-agentic-workload. Tegelijk verschuift enterprise-infrastructuur naar on-premises en hybride setups: GPU's volstaan niet meer; organisaties willen datacontrole en sovereigniteit over hun agent-omgevingen.

### 🏛️ Governance & Beleid

Europa zette in november concrete stappen: de AI Act-handhaving loopt, de definitie-richtlijnen zijn gepubliceerd en de Digital Fairness Act is in consultatie. De druk op organisaties neemt toe: 2027 brengt de hoge-risico-verplichtingen en organisaties die nu niet starten met impact assessments en governance-frameworks, komen in tijdnood. In de VS brengt de Democratische overwinning bij de Congresverkiezingen (3 nov) onzekerheid: meer kans op federale AI-regulering, maar de tijdlijn is onduidelijk. Australiës nieuwe AI-toezichthouder (10 nov) laat zien dat governance wereldwijd institutionaliseert.

### 🔐 Security & Risk

Dit was een belangrijke week voor AI-security. Twee concrete dreigingen domineerden:
- **Supply-chain aanval:** Een gekapt Microsoft agent-framework pakket op PyPI (17 nov) illustreert dat de AI-tooling-ecosysteem een favoriet aanvalspad wordt.
- **Actief uitgebuit lek:** LiteLLM CVE-2026-40217 op de CISA KEV-lijst (18 nov) met een strakke deadline.

Structureler: Gartner rapporteerde dat AI-risico's vier van de vijf toprisico's voor Q3 2026 vormen. CrowdStrike's overname van Fiddler voor agent-monitoring laat zien dat de markt begint te volwassen worden op dit terrein. Een zorgwekkend studieresultaat: slechts 24,8% van LLM-gegenereerde security patches is volledig correct – organisaties die AI inzetten voor security-fixes moeten menselijke review garanderen.

### 📈 Markt & Adoptie

Enterprise AI-spend is explosief ($177 miljard, 5,4x in een jaar) maar het rendement blijft achter: 79% rapporteert adoptie-obstakels en slechts 15% meet aantoonbare financiële resultaten. Dit is het kerndilemma voor IT-consultancy: klanten willen investeren maar weten niet hoe ze waarde gaan aantonen. IBM en Microsoft lanceerden "Imagine Enterprise" (10 nov) met 6.000 pre-built agents voor finance en retail – een sign dat hyperscalers het agent-platform-gevecht aangaan. Belangrijk voor bouwers: **Agent Builder sluit op 30 november** – een harde deadline die klanten raakt die daarop gebaseerde workflows hebben.

## 💼 Ctac-weekperspectief

- **Ctac's eigen context:** Patrick Rosengarten startte op 16 november als nieuwe CFO. Ctac verwacht een negatief resultaat voor 2026 door een eenmalige strop, maar rapporteert sterke operationele vraag naar AI-diensten. Dit is het moment om die vraag te concretiseren in proposities met aantoonbare ROI – juist omdat 85% van de markt dit nog niet voor elkaar heeft.

- **Agent Builder shutdown (30 nov) = klantrisico:** Organisaties die workflows hebben gebouwd op Microsoft's Agent Builder moeten uiterlijk deze week actie ondernemen. Ctac kan hier proactief advies bieden over migratiepaden richting Copilot Studio of Azure AI Foundry.

- **EU AI Act compliance urgentie:** De publicatie van de definitie-richtlijnen (5 nov) en de Digital Fairness Act (11 nov) versterken de urgentie van AI governance-diensten. Klanten in de hoge-risico-categorieën hebben minder dan een jaar om hun impact assessments en documentatie op orde te krijgen. Propositie-kans voor Ctac's AI-governance dienstverlening.

- **Security-propositie versterken:** De LiteLLM KEV en de PyPI supply-chain aanval zijn concrete klantgesprekken. Ctac kan het thema "veilige AI-tooling in de supply chain" concreet maken: welke AI-pakketten gebruikt een klant, wie monitort die, en hoe worden patches beheerd?

## 📚 Bronnenlijst

**Technologie & Modellen**
- [AI Weekly: GPT-6.2, Gemini 4 Hydrogen, Nvidia Shake-Up – AM Data Lakehouse](https://amdatalakehouse.substack.com/p/ai-weekly-gpt-62-gemini-4-hydrogen)
- [New AI Models — November 2026 LLM Releases – LLM Gateway](https://llmgateway.io/timeline)
- [Enterprise AI infrastructure moves beyond GPUs – SiliconANGLE](https://siliconangle.com/2026/11/19/enterprise-ai-pushing-cloud-infrastructure-beyond-gpu-kubeconna/)
- [Schneider Electric and Omdia: enterprise shift towards own AI infrastructure (19 nov)](https://news.europawire.eu/schneider-electric-and-omdia-research-highlights-enterprise-shift-towards-company-owned-ai-infrastructure/eu-press-release/2026/11/19/17/14/02/188827/)

**Governance & Beleid**
- [AI law and regulation: agents, incident reporting – Beyond Horizons (nov 2026)](https://www.insights.beyondhorizons.sg/p/ai-law-regulation-roundup-november-2026)
- [AI Regulation & Policy Weekly Report 16 november 2026 – Origin Brief](https://www.originbrief.app/en/reports/ai-regulation-policy/2026-11-16/weekly)
- [Most AI Governance Platforms Still Cannot Say No (18 nov)](https://genesishumanexperience.com/2026/11/18/ai-governance-platforms-cannot-say-no/)
- [AI regulation news November 2026 – mean.ceo blog](https://blog.mean.ceo/ai-regulation-news-november-2026/)

**Security & Risk**
- [AI agent security November 2026: AgentCore takeover, rogue agents – Adversa AI](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/)
- [CISO Daily Briefing 15 november 2026 – Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/ciso-daily-briefing-20261115/)
- [AI and Cybersecurity Update: Vendor Breaches Nov 2026 – BTI Group](https://www.btigroup.com/post/ai-cybersecurity-update-november-20-2026/)
- [What's new in Microsoft Security November 2026](https://www.microsoft.com/en-us/security/blog/2026/11/05/whats-new-in-microsoft-security-november-2026/)
- [Companies going all in on AI could see strategy backfire – Help Net Security](https://www.helpnetsecurity.com/2026/11/04/ai-strategy-miscalculation-gartner-report/)

**Markt & Adoptie**
- [Menlo Ventures 2026 State of Enterprise AI: $177B, 5.4x groei – GlobeNewswire](https://www.globenewswire.com/news-release/2026/11/03/3394279/0/en/menlo-ventures-2026-state-of-enterprise-ai-report-enterprise-ai-spending-hits-177b-up-5-4x-in-one-year-as-agents-take-over)
- [Enterprise AI adoption: 79% face challenges despite high investment – WRITER](https://writer.com/blog/enterprise-ai-adoption-2026/)
- [AI Agents expand enterprise reach, week 16 nov – AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-expand-enterprise-reach-tackle-complex-workflows-and-enhance-security)

**Ctac-context**
- [Ctac verwacht rood jaar 2026 door eenmalige strop – Dutch IT Channel](https://www.dutchitchannel.nl/news/763443/ctac-verwacht-rood-jaar-2026-door-eenmalige-strop/)
- [Patrick Rosengarten wordt CFO van Ctac – Dutch IT Channel](https://www.dutchitchannel.nl/people/763770/patrick-rosengarten-wordt-cfo-van-ctac)
- [Nederlandse organisaties willen sneller met AI maar missen de basis – Consultancy.nl](https://www.consultancy.nl/nieuws/68802/nederlandse-organisaties-willen-sneller-met-ai-maar-missen-de-basis)
