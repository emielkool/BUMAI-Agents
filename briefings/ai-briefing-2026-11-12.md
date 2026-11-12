---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-12
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 12 november 2026

## 🔑 Highlights van de dag

- **Anthropic lanceert Mythos 5.2 en Fable 5.2** (9 nov): Fable reageert 30% sneller en volgt direct na een METR-rapport over mogelijke recursieve zelfverbetering — Anthropic benadrukt dat Mythos niet covert handelt.
- **EU AI Act: transparantierichtlijnen vastgesteld** (5 nov): Artikel 50-guidelines zijn officieel aangenomen (C(2026) 7702 final); de volgende mijlpaal is 2 december 2026, wanneer de overgangsperiode voor oudere generatieve systemen eindigt.
- **Google betreedt de decision-model markt** (11 nov): Gemini Decisions API beantwoordt ja/nee-, keuze- en beoordelingsvragen tegen lage kosten — een niche maar strategisch relevante beweging richting gestructureerde agentische workflows.
- **DeepMind verifiëert Signal-encryptie met AI**: AlphaProof Code bewijst formeel de correctheid van het Signal Protocol — de eerste keer dat AI wordt ingezet voor formele verificatie van een breed uitgerold cryptografisch protocol.
- **Anthropic blokkeert Chinese entiteiten wereldwijd**: nieuwe gebruiksvoorwaarden verbieden toegang voor bedrijven met ≥50% Chinese eigendom, overal ter wereld — Amodei zegt dit honderden miljoenen kost.

## 🧠 Technologie & Modellen

**Anthropic – Mythos 5.2 & Fable 5.2** (9 nov): De nieuwste generatie modellen is uitgebracht kort nadat een externe METR-evaluatie suggereerde dat Anthropic de grens van recursieve zelfverbetering nadert. Fable 5.2 is 30% sneller; Anthropic stelt expliciet dat Mythos niet covert handelt tegen gebruikers. Dit is een signaal dat de frontier-labs nu actief communiceren over veiligheidsgedrag als concurrentiefactor. ([TechCrunch](https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/))

**Meta – Muse Ember** (9 nov): Meta's Superintelligence Lab lanceert een ultralicht model voor agentische taken (tool calls, routing) voor $0,10 per miljoen inputtokens — aanzienlijk goedkoper dan Haiku of vergelijkbare frontier-modellen. Interessant voor wie kosten wil drukken in multi-agent architecturen. ([TechCrunch](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/))

**Google – Gemini Decisions API** (11 nov): Google stapt in de markt voor "decision models" met een goedkope API voor gestructureerde vraagtypen. Beats zeven van negen benchmarks ten opzichte van een nader genoemde concurrent. Niche nu, maar relevant voor bedrijfsprocessen die veel classificatietaken vereisen. ([SiliconANGLE](https://siliconangle.com/2026/11/11/google-enters-the-decision-model-market-with-gemini-decisions-api/))

**Open-weight leaderboard** (12 nov): Op de Hugging Face benchmarks leiden vandaag overwegend Chinese open-gewicht modellen: Darwin-180B-RSI (GPQA: 94,44), Ornith-1.5-397B (SWE-bench: 86), DeepSeek-V4.1-Flash (Terminal-bench: 90,6). De open-source competitie intensiveert, met China als dominante speler. ([DEV Community](https://dev.to/quantid/hugging-face-official-benchmarks-daily-update-2026-11-12-3d0h))

## 🏛️ Governance & Ethiek

**Artikel 50-richtlijnen EU AI Act** (5 nov): De Europese Commissie heeft de transparantievereisten voor AI-systemen formeel vastgesteld. Dit raakt direct chatbots, deepfakes en gegenereerde content die als zodanig gelabeld moet worden. Deadline 2 december 2026 voor oudere generatieve systemen is nabij. ([Praxikon](https://www.praxikon.com/en/posts/article-50-guidelines-adopted-c-2026-7702-which-reference))

**High-risk verplichtingen uitgesteld**: Via het AI Omnibus-pakket zijn de high-risk verplichtingen opgeschoven: standalone systemen naar 2 december 2027, ingebedde systemen (in gereguleerde producten) naar 2 augustus 2028. Eerste geharmoniseerde standaard EN 18286:2026 is wel al van kracht. ([Softtechhub](https://softtechhub.us/2026/11/10/eu-ai-act-high-risk-delay-2027/), [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

## 🔐 Security & Risk

**Anthropic blokkeert Chinese bedrijven** (lopend): Nieuwe voorwaarden verbieden toegang voor bedrijven met ≥50% Chinese eigendom, wereldwijd. Er zijn ontwijkingsroutes (proxy-diensten, token-brokers), die Anthropic actief monitort via tijdzone-detectie. Dario Amodei bevestigt de maatregel honderden miljoenen kost. Dit illustreert de groeiende geopolitisering van AI-toegang. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/anthropic-blocks-chinese-firms-from-claude), [TweakTown](https://www.tweaktown.com/news/112261/anthropic-says-blocking-china-from-claude-cost-it-hundreds-of-millions/index.html))

**Prompt injection blijft toprisico**: Onderzoek bevestigt 50–80% slaagkans bij aanvallen op AI coding editors; in AI-security-agents werd 100% exploitatie gerapporteerd over 14 aanvalsvarianten. Supply chain-vergiftiging van agent skills en memorypoisoning (bijv. via web tegen Copilot) worden gemeld als 2026-incidenten. ([OWASP](https://genai.owasp.org/llmrisk2023-24/llm01-24-prompt-injection/), [arXiv](https://arxiv.org/html/2506.23260v1))

## 📈 Markt & Adoptie

**Cloud-AI groei versnelt**: Google Cloud heeft 2.600 klanten die >100 miljard tokens/jaar verwerken. Microsoft 365 Copilot-klanten op consumption-based billing groeiden 75%+ kwartaal-op-kwartaal. Amazon verhoogde capex naar $125 miljard voor 2026. Totale AI-infrastructuurinvesteringen overstijgen naar schatting $700 miljard in 2026. ([Yahoo Finance / Citi](https://finance.yahoo.com/technology/ai/articles/citi-raises-ai-revenue-forecasts-114800473.html), [The Motley Fool](https://www.fool.com/investing/2026/11/11/amazon-and-microsoft-lead-the-cloud-market-one-of/))

**OpenAI – GPT-6 Cyber** (5 nov): Gericht op het opsporen en patchen van kwetsbaarheden. Beschikbaar voor topgebruikers in het Daybreak Red-programma. Interessant als signaal dat gespecialiseerde AI-modellen per domein de norm worden. ([TechCrunch](https://techcrunch.com/2026/11/05/openai-released-a-new-cybersecurity-model-is-that-enough/), [OpenAI](https://openai.com/index/introducing-gpt-6-cyber/))

## 💡 Ctac-relevantie

**Fable 5.2 / Muse Ember als productiekandidaten**: De combinatie van snellere frontier-modellen (Fable) en ultragoedkope routeringsmodellen (Muse Ember) maakt het nu aantrekkelijk om multi-agent architecturen te heroverwegen: dure calls reserveren voor complexe taken, Ember inzetten voor routing en orchestratie. Relevant voor lopende agent-proposities bij Ctac-klanten.

**EU AI Act deadline 2 december**: Klanten die generatieve AI inzetten in consumentengerichte toepassingen moeten per 2 december voldoen aan de transparantievereisten van Artikel 50. Dit is een concrete korte-termijn compliance-actie — Ctac kan hierin advieswaarde bieden.

**Geopolitiek AI-risicobeheer**: De Anthropic-blokkade van Chinese entiteiten illustreert dat bedrijven bij het inrichten van AI-supply chains nu ook geopolitiek eigendomsrisico moeten meenemen. Voor internationale Ctac-klanten is dit een nieuw aandachtspunt in AI-governance trajecten.

**Decision models**: Google's Gemini Decisions API opent een nieuw segment voor gestructureerde AI-classificatie in bedrijfsprocessen (bijv. risicoscoring, goedkeuringsflows). Laagdrempelig te integreren en kostenefficiënt — kansen voor Ctac's finance- en overheidsklanten.

## 📚 Bronnen & verder lezen

- [Anthropic releases Mythos and Fable 5.2 – TechCrunch](https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/)
- [Meta releases Muse Ember – TechCrunch](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/)
- [OpenAI GPT-6 Cyber – TechCrunch](https://techcrunch.com/2026/11/05/openai-released-a-new-cybersecurity-model-is-that-enough/)
- [GPT-6 Cyber – OpenAI](https://openai.com/index/introducing-gpt-6-cyber/)
- [Google Gemini Decisions API – SiliconANGLE](https://siliconangle.com/2026/11/11/google-enters-the-decision-model-market-with-gemini-decisions-api/)
- [Hugging Face Benchmarks 12 nov – DEV Community](https://dev.to/quantid/hugging-face-official-benchmarks-daily-update-2026-11-12-3d0h)
- [EU AI Act Artikel 50 guidelines – Praxikon](https://www.praxikon.com/en/posts/article-50-guidelines-adopted-c-2026-7702-which-reference)
- [EU AI Act high-risk delay – Softtechhub](https://softtechhub.us/2026/11/10/eu-ai-act-high-risk-delay-2027/)
- [EU AI Act tijdlijn – EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Anthropic blokkeert Chinese bedrijven – Tom's Hardware](https://www.tomshardware.com/tech-industry/anthropic-blocks-chinese-firms-from-claude)
- [Anthropic China-blokkade kosten – TweakTown](https://www.tweaktown.com/news/112261/anthropic-says-blocking-china-from-claude-cost-it-hundreds-of-millions/index.html)
- [Prompt injection in AI agents – arXiv](https://arxiv.org/html/2506.23260v1)
- [OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk2023-24/llm01-24-prompt-injection/)
- [Cloud AI markt – Citi/Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/citi-raises-ai-revenue-forecasts-114800473.html)
- [Amazon vs Microsoft cloud – The Motley Fool](https://www.fool.com/investing/2026/11/11/amazon-and-microsoft-lead-the-cloud-market-one-of/)
