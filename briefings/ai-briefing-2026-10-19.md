---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-19
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 19 oktober 2026

## 🔑 Highlights van de dag

- **DeepSeek V4.1 Flash** (17 okt) en **Meta's Muse Spark Open** (15 okt) zijn de meest recente open-weight releases; Meta positioneert Muse Spark Open nadrukkelijk als sterkste US open-weight model voor code en agentische taken.
- **Microsoft Copilot domineert enterprise**: 73% van de grootste bedrijven gebruikt het actief of heeft het goedgekeurd; Google Gemini staat tweede (47%) en OpenAI ChatGPT Enterprise derde (44%) – de platformrace is beslist, de adoptie-uitdaging begint nu pas.
- **Agentic AI wordt het nieuwe security-hoofdpijndossier**: 65% van organisaties noemt "onverwacht agentgedrag" als toprisico (Google Cloud/Kroll); een nieuw AI-tool kan binnen twee uur opduiken in de bedrijfsomgeving (Pluto Security).
- **EU AI Act – praktisch zicht**: De AI Office heeft vanaf 2 augustus 2026 toezichts- en handhavingsbevoegdheden voor general-purpose modellen. Nieuwe Article 5-verboden (o.a. generatie van NCII en CSAM) treden in op 2 december 2026. High-risk verplichtingen (Annex III) gelden pas vanaf 2 december 2027.
- **Misbruik van AI-tooling in aanvallen neemt toe**: Een threat group zou Claude Code hebben ingezet om aanvalstooling te bouwen die 628.000 Oekraïense records comprimeerde – nog niet bevestigd via primaire bron, maar past in bredere trend van AI-versneld offensief onderzoek.

## 🧠 Technologie & Modellen

Oktober 2026 is een drukke maand voor modelreleases, al zijn de grote frontier-sprongen al eerder dit kwartaal gezet.

**Recente releases (eerste helft oktober):**
- **DeepSeek V4.1 Flash 1017** – uitgebracht op 17 oktober; specifieke capabilities nog beperkt gedocumenteerd.
- **Meta Muse Spark Open** (15 okt) – open-weight, gefocust op coding en agentische toepassingen. Meta noemt het het meest capabele US open-weight model op dit moment.
- **Google Gemini 4 Argon** – nu breed beschikbaar na een gelimiteerde release voor cyber defenders.
- **OpenAI GPT-6** – standaard geworden in ChatGPT voor alle gebruikers (7 okt).
- **Anthropic Claude Haiku 5.5** – uitgebracht op 7 oktober; de snel en goedkoop uitgeruste versie voor volume-toepassingen.
- **Mistral Large 4** – in public preview since 6 oktober.

**Wat dit betekent:** De modelstapel verdiept zich elke week. Open-weight modellen (Meta, DeepSeek) komen steeds dichter in de buurt van gesloten frontier-modellen op specifieke taken. Dat heeft prijs- en keuze-implicaties voor enterprise deployments. Yann LeCun (Meta Chief AI Scientist) stelt expliciet dat open-source modellen proprietary modellen beginnen te overtreffen.

*Bronnen: [LLM Gateway tracker](https://llmgateway.io/timeline) · [Digital Applied tracker](https://www.digitalapplied.com/blog/ai-model-releases-october-2026-tracker) · [EPC Group – DeepSeek/Llama 2026](https://www.epcgroup.net/blog/deepseek-qwen-llama-open-frontier-2026)*

## 🏛️ Governance & Ethiek

**EU AI Act – actuele stand van zaken (oktober 2026):**

- De **AI Office** en nationale toezichthouders zijn operationeel per 2 augustus 2026. De AI Office heeft directe handhavingsbevoegdheid over GPAI-modellen (inclusief het opvragen van technische documentatie, corrigerende maatregelen en boetes).
- Het **Digital Omnibus** (Regulation (EU) 2026/1744, van kracht sinds 27 juli 2026) heeft de high-risk verplichtingen verzwaard vertraagd: Annex III-systemen hoeven pas vanaf **2 december 2027** te voldoen; Annex I (product-embedded AI) zelfs pas **2 augustus 2028**.
- **Concreet naderende deadline**: **2 december 2026** – nieuwe verboden onder Article 5 worden van kracht, waaronder het genereren van non-consensuele intieme afbeeldingen en CSAM-generatie.
- De GDPR/ePrivacy 'data omnibus' heeft nog geen Raadsmandaat; onzekerheid over data governance-kader blijft.

**Takeaway:** Organisaties die now compliance-programma's voor high-risk AI uitstellen tot 2027 hebben formeel ruimte, maar de AI Office is al actief. Operationele voorbereiding begint nu.

*Bronnen: [EC digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [Swfte EU AI Act 2026](https://www.swfte.com/blog/eu-ai-act-2026-what-actually-applies-now) · [Al Jazeera – AI Act augustus 2026](https://www.aljazeera.com/news/2026/8/6/what-came-into-force-with-the-eus-ai-act-this-week-and-what-didnt)*

## 🔐 Security & Risk

**Agentic AI is het nieuwe aanvalsoppervlak:**

- **Schaduw-AI / shadow AI** blijft toprisico. Pluto Security (die $42M ophaalden in een Series B-ronde) stelt dat een nieuw AI-tool binnen twee uur na lancering al in bedrijfsomgevingen te vinden is – ver buiten elk goedkeuringskader.
- **Agentic-risico's** die organisaties nu actief rapporteren (Dataiku/Google Cloud 2026): onverwacht agentgedrag (65%), 'ghost agents' (forgotten agents with valid credentials), multi-agent drift en privilege escalation via toolchain.
- **Patch-last explodeert**: Microsoft loste in de oktober 2026 Patch Tuesday meer dan 1.400 kwetsbaarheden op – een nieuw record. AI-gestuurde tools versnellen zowel de ontdekking als de exploitatie van die kwetsbaarheden (Forrester).
- **Gemeld incident (niet geverifieerd)**: RuntimeAI meldt dat een threat group Claude Code zou hebben gebruikt om aanvalstooling te bouwen voor een datalek van 628.000 Oekraïense records. Primaire bronbevestiging ontbreekt – wacht op nadere verificatie, maar het past in bredere trend van LLM-gebruik voor offensive security.

*Bronnen: [Dark Reading – Enterprise AI Risk](https://www.darkreading.com/cyber-risk/enterprise-ai-risk-management-phase-security-concerns-rise) · [TechCrunch – Pluto Security $42M](https://techcrunch.com/2026/10/13/pluto-security-raises-42m-as-ai-gives-enterprise-security-teams-a-new-headache/) · [RuntimeAI incident roundup](https://runtimeai.io/blog/2026-10-16-ai-security-incidents.html)*

## 📈 Markt & Adoptie

**De platformkeuze is grotendeels gemaakt – nu de executie:**

- **Microsoft Copilot**: actief of goedgekeurd bij 73% van de grootste bedrijven (Morning Consult). Gartner ziet Microsoft als leider in brede enterprise-AI; Google als leider in agentic AI-stacks.
- **OpenAI–Microsoft-verhouding verschoven**: per april 2026 heeft Microsoft de exclusieve cloud-distributie van OpenAI-modellen opgegeven. OpenAI heeft nu een eigen enterprise deployment unit; enterprise is meer dan 40% van OpenAI's omzet.
- **ROI-verwachtingen bijstellen**: onderzoek geeft aan dat AI-waarde niet primair via kostenbesparing binnenkomt, maar via inzichten en procesversnelling op onverwachte plekken.
- **Vendor-concurrentie**: Anthropic houdt ~40% van enterprise LLM-gebruik (naar volume, Menlo Ventures eind 2025); Google 21%; OpenAI 27%. Cijfers lopen uiteen per meetmethode.

*Bronnen: [CIO Dive – Microsoft/Google enterprise dominance](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) · [MarketScale – Enterprise AI ROI 2026](https://www.marketscale.com/industries/software-and-technology/enterprise-ai-is-generating-business-insights-but-not-saving-money-and-the-governance-gap-is-widening) · [Morning Consult – State of Enterprise AI](https://morningconsult.com/articles/state-of-enterprise-ai)*

## 💡 Ctac-relevantie

**Drie concrete handvatten voor de AI-unit en klantpropositie:**

1. **Agentic AI governance is de volgende propositie-kans.** Nu 65% van organisaties "onverwacht agentgedrag" als toprisico benoemt en shadow-agents binnen uren de omgeving binnendringen, zoeken enterprise-klanten iemand die helpt met beleid, tooling-governance en audit-kaders voor agents. Ctac kan hier een gestructureerde AI governance-scan of -blueprint aanbieden – vóór de competitors dat doen.

2. **EU AI Act-readiness heeft nu concrete haalbaarheidsdata.** Met high-risk verplichtingen uitgesteld naar december 2027, maar de AI Office die al toezicht houdt op GPAI-modellen, is er een realistisch tijdvenster voor een phased compliance-aanpak. Klanten in finance en overheid willen zekerheid dat hun huidige tooling (Copilot, Azure AI) voldoet aan GPAI-regels. Hier ligt werk voor de komende 12 maanden.

3. **Open-weight vs. closed model – de keuze wordt strategisch.** Meta Muse Spark Open en DeepSeek V4.1 rijpen als serieuze alternatieven voor closed APIs. Voor klanten met data-soevereiniteits- of kosteisen (zorg, overheid) biedt dit nieuwe deployment-opties. De AI-engineer in het team kan hier benchmarks uitvoeren die de propositie onderbouwen.

## 📚 Bronnen & verder lezen

- [LLM Gateway – Model Release Timeline Oct 2026](https://llmgateway.io/timeline)
- [Digital Applied – AI Model Releases October 2026](https://www.digitalapplied.com/blog/ai-model-releases-october-2026-tracker)
- [EC – EU AI Act officieel framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Swfte – EU AI Act 2026: What Actually Applies Now](https://www.swfte.com/blog/eu-ai-act-2026-what-actually-applies-now)
- [Al Jazeera – AI Act augustus 2026 (inwerkingtreding)](https://www.aljazeera.com/news/2026/8/6/what-came-into-force-with-the-eus-ai-act-this-week-and-what-didnt)
- [Dark Reading – Enterprise AI Enters Risk Management Phase](https://www.darkreading.com/cyber-risk/enterprise-ai-risk-management-phase-security-concerns-rise)
- [TechCrunch – Pluto Security $42M raise](https://techcrunch.com/2026/10/13/pluto-security-raises-42m-as-ai-gives-enterprise-security-teams-a-new-headache/)
- [RuntimeAI – AI Security Incidents week 16 oktober 2026](https://runtimeai.io/blog/2026-10-16-ai-security-incidents.html)
- [CIO Dive – Microsoft en Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Morning Consult – State of Enterprise AI](https://morningconsult.com/articles/state-of-enterprise-ai)
- [MarketScale – Enterprise AI ROI 2026](https://www.marketscale.com/industries/software-and-technology/enterprise-ai-is-generating-business-insights-but-not-saving-money-and-the-governance-gap-is-widening)
- [Kroll – Agentic AI: From Model Risk to Enterprise Risk](https://www.kroll.com/en/publications/cyber/agentic-ai-from-model-risk-to-enterprise-risk)
- [EPC Group – DeepSeek, Qwen, Llama open frontier 2026](https://www.epcgroup.net/blog/deepseek-qwen-llama-open-frontier-2026)
