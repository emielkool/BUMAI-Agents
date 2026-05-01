---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W18
Datum: 2026-05-01
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 18, 2026

> Synthese van de dagbriefings van 27 april t/m 1 mei 2026.
> Geen individuele dagbriefings beschikbaar voor deze week; overzicht is gebaseerd op directe bronnensynthese.

---

## 🏆 Weekhighlights

1. **DeepSeek V4 gooit de prijsdynamiek volledig overhoop.** Op 23–24 april lanceerde DeepSeek V4 Pro en Flash onder MIT-licentie: frontier-prestaties (naast GPT-5.5 en Claude Opus 4.7 in agentic benchmarks) voor 1/20e van de prijs van Opus 4.7. Dat is geen iteratie – het is een structurele repricing van het AI-marktlandschap. Anthropic en OpenAI hebben nog niet gereageerd; nieuwe low-cost tiers zijn onvermijdelijk.

2. **EU AI Act Omnibus strandde op 28 april – augustus-deadline staat weer rechtop.** De tweede politieke triloog (Europees Parlement, Raad, Commissie) op 28 april eindigde zonder akkoord. Het voorstel om de high-risk compliance-deadline te verschuiven van 2 augustus 2026 naar 2 december 2027 haalde het niet. Volgende triloog: 13 mei 2026. Tot die datum geldt de originele deadline onverminderd. Organisaties die rekenden op uitstel hebben geen buffer meer.

3. **Microsoft maakt Office volledig agentisch – standaard voor alle M365-gebruikers.** Copilot Agent Mode voor Word, Excel en PowerPoint ging GA op 22 april; op 27 april volgde een Frontier-update die Outlook agentic maakt (triage, follow-ups, kalenderconflicten). Op 1 mei lanceerde Microsoft de M365 E7- en Agent 365-bundels. De werkplek is officieel een multi-agent omgeving geworden – niet als pilot, maar als standaard product.

4. **10 nieuwe in-the-wild prompt injection-aanvallen gedocumenteerd.** Onderzoekers publiceerden in april 2026 tien concrete indirect prompt injection-payloads die actief worden ingezet tegen AI-agents: financiële fraude (PayPal-links van $5.000), bestandsverwijdering via Unix-commando's, API-key-diefstal. Het structurele probleem blijft: modellen kunnen instructies niet betrouwbaar onderscheiden van data. Elke agent die het web leest, is vatbaar.

5. **Verticale AI-agents bereiken de SMB-markt via Avoca's $1B-mijlpaal.** Op 27 april maakte Avoca (AI-voice-agent voor sanitairtechnici) bekend $125M opgehaald te hebben en een valuation van $1 miljard te bereiken. De agent beantwoordt inkomende gesprekken, boekt klussen in de CRM, stuurt follow-ups en optimaliseert capaciteitsplanning – volledig autonoom. Dit markeert een kantelpunt: AI-agents zijn niet langer een enterprise-luxe maar bereiken de kleine vakman.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De week wordt gekenmerkt door twee gelijktijdige bewegingen die elkaars tegenwicht vormen. Aan de frontier-kant is de race om de meest capabele modellen in volle gang: GPT-5.5, Claude Opus 4.7 en Gemini 3.1 Ultra bieden elk nieuwe hoogten op specialistische taken. Tegelijkertijd comprimeert DeepSeek V4 de gap tussen open-gewicht en gesloten modellen verder dan ooit. De benchmark-prestaties van V4 Pro liggen naast die van de topmodellen; de prijs is 1/20e.

De meest strategische verschuiving is de volledige agentificatie van de Microsoft Office-suite. Waar vorige maand multi-agent-infrastructuur (MCP, A2A) werd gestandaardiseerd, materialiseert die nu in concrete GA-producten die bij elke M365-gebruiker worden uitgerold. Stanford's AI Index bevestigt de trend: AI-agents halen nu 66% van menselijke computertaken – verdubbeld ten opzichte van vorig jaar.

---

### 🏛️ Governance & Beleid

De mislukte triloog van 28 april is het governance-verhaal van de week. De Digitale Omnibus – het voorstel van de Commissie om high-risk AI-compliance uit te stellen – heeft na twee mislukte rondes nog steeds geen politiek akkoord. Dit heeft directe consequenties: de 2 augustus 2026-deadline is geen theoretisch ankerpunt meer, maar een harde juridische realiteit voor elke organisatie die high-risk AI inzet.

Parallel liet de Commissie op 21 april €63,2 miljoen vrij voor AI-innovatie in gezondheid en online veiligheid – een signaal dat investeren en reguleren gelijktijdig doorgaan. De volgende triloog (13 mei) wordt cruciaal: haalt de Omnibus het voor augustus, dan is er ruimte; haalt hij het niet, dan moeten organisaties in juni compliance-klaar zijn.

---

### 🔐 Security & Risk

De security-dreiging rond AI-agents is dit week van theoretisch naar bewezen-schaalbaar overgegaan. De publicatie van tien concrete, in-the-wild gedocumenteerde indirect prompt injection-payloads is een markering: dit zijn geen proof-of-concepts meer, maar aanvalspatronen die actief worden toegepast. De doelwitten zijn precies de agents die enterprise-waarde leveren: agents met web-toegang, RAG-pipelines, e-mailverwerking en financiële transactiebevoegdheden.

Een VentureBeat-rapport toonde dat drie AI-coding-agents geheimen lekten via één prompt injection – en dat de system card van de leverancier dit risico expliciet voorspelde maar niet voorkwam. OutSystems' 2026 State of AI Development-rapport meldt dat 94% van organisaties zorgen heeft over agent sprawl. De combinatie van brede uitrol (97% van organisaties heeft agents in productie) en gebrekkige security-architectuur maakt dit tot het grootste AI-risico van dit moment.

---

### 📈 Markt & Adoptie

De marktdynamiek van week 18 laat een scherpe tweedeling zien. Enerzijds de macro: enterprise AI-adoptie is volledig ingeburgerd (88% van organisaties gebruikt AI in minimaal één bedrijfsfunctie), maar slechts 29% rapporteert significante ROI. 79% ervaart uitdagingen – een stijging van dubbele cijfers ten opzichte van 2025. De kloof tussen investering en bewezen waarde blijft het centrale knelpunt.

Anderzijds de specifieke doorbraken die dat patroon doorbreken: Avoca ($1B) voor loodgieters, Microsoft's agentic Office voor kenniswerkers, OpenAI's Workspace Agents (GA 22 april) voor organisaties op Slack/Drive/M365. De verticalisering van AI-agents – specifiek getraind op de workflow van één industrie – lijkt het antwoord op het ROI-probleem. Wie de workflow bezit, bezit de waarde. Google's commitment van $40 miljard extra aan Anthropic (bij een valuation van $350 miljard) illustreert hoe onverminderd groot de inzet op het AI-platform-niveau is.

---

## 💼 Ctac-weekperspectief

- **De EU AI Act Omnibus-mislukking op 28 april maakt compliance onuitstelbaar.** Klanten die wachtten op het uitgestelde Omnibus-tijdpad moeten nu weten dat de 2 augustus-deadline wettelijk geldt, tenzij de triloog van 13 mei alsnog akkoord bereikt. Voor klanten in overheid, zorg en finance is dit het moment om het gesprek te openen. Een concrete propositie: een EU AI Act readiness-scan in mei, zodat klanten weten wat ze te doen staat voor 2 augustus.

- **Microsoft's agentische Office-lancering is een verkoopmoment voor Ctac.** M365 E7 en Agent 365 zijn per 1 mei beschikbaar. Elke klant op Microsoft 365 krijgt nu agentic capaciteiten aangeboden zonder extra implementatie-inspanning van de softwareleverancier – maar mét de noodzaak van integratie, governance en beveiligingsinrichting. Ctac kan hier positioneren als de partner die de koppeling maakt tussen agentische Office-tools en klantspecifieke bedrijfsprocessen.

- **Security by design is niet langer een optionele toevoeging maar een contractuele basis.** De tien gedocumenteerde in-the-wild aanvallen maken het onhoudbaar om AI-agents te implementeren zonder expliciet security-kader. Elk lopend of nieuw Ctac-project met agents moet een threat model hebben: welke databronnen leest de agent, welke acties kan hij uitvoeren, en hoe wordt prompt injection gedetecteerd? Dit is zowel risicobeheer als verkoopargument.

- **DeepSeek V4 opent de deur naar kostefficiëntere propositieopbouw voor datakritische klanten.** MIT-licentie, 1M context, frontier-kwaliteit voor 1/20e van de prijs van Opus 4.7 – voor klanten met soevereiniteits- of kostenvereisten is DeepSeek V4 nu een serieuze optie naast Gemma 4. Technische kennis van lokale inference-stacks (vLLM, Ollama) gecombineerd met Ctac's integratie-expertise is een concreet verschilpunt voor klanten die niet afhankelijk willen zijn van cloud-API's.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [DeepSeek V4 Ships 1M Context, Open-Weights – winbuzzer.com](https://winbuzzer.com/2026/04/27/deepseek-v4-open-weights-launch-xcxwbn/)
- [DeepSeek V4 arrives at 1/6th the cost of Opus 4.7, GPT-5.5 – VentureBeat](https://venturebeat.com/technology/deepseek-v4-arrives-with-near-state-of-the-art-intelligence-at-1-6th-the-cost-of-opus-4-7-gpt-5-5)
- [DeepSeek previews new AI model that 'closes the gap' – TechCrunch](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/)
- [DeepSeek V4: The Open-Source Model That Rivals Closed Frontier Models – MindStudio](https://www.mindstudio.ai/blog/deepseek-v4-open-source-frontier-model-review)
- [GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1 Pro vs DeepSeek V4 benchmark vergelijking – Medium](https://medium.com/@mohit15856/gpt-5-5-vs-claude-opus-4-7-vs-gemini-3-1-pro-vs-deepseek-v4-18dafdcf9b5e)
- [Microsoft Copilot Studio Goes Multi-Agent: A2A Protocol GA – evermx.com](https://www.evermx.com/case/microsoft-copilot-studio-multi-agent-ga-april-2026)
- [AI News Digest, April 27, 2026: Agentic AI Office Productivity Just Became the Default – asanify.com](https://asanify.com/blog/news/agentic-ai-office-productivity-april-27-2026/)
- [LLM News Today (May 2026) – llm-stats.com](https://llm-stats.com/ai-news)

**Governance & Beleid**
- [EU and Parliament fail to agree on AI Act changes after 12 hours of talks – The Next Web](https://thenextweb.com/news/eu-ai-act-omnibus-deal-fails-april-2026-talks)
- [EU AI Act trilogue stalls — August deadline back in play – resultsense.com](https://www.resultsense.com/news/2026-04-30-eu-ai-act-omnibus-trilogue-stalls)
- [The Digital AI Omnibus: Proposed deferral of high risk AI obligations – DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [Implementation Timeline EU AI Act – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act 2026 Updates: Compliance Requirements and Business Risks – legalnodes.com](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)

**Security & Risk**
- [Researchers Uncover 10 In-the-Wild Indirect Prompt Injection Attacks – Infosecurity Magazine](https://www.infosecurity-magazine.com/news/researchers-10-wild-indirect/)
- [Three AI coding agents leaked secrets through a single prompt injection – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Agentic AI Cybersecurity: Why It's a Nightmare in 2026 – jazzcybershield.com](https://blog.jazzcybershield.com/agentic-ai-cybersecurity-nightmare-2026/)
- [AI Agent Security in 2026: Prompt Injection, Memory Poisoning, and the OWASP Top 10 – swarmsignal.net](https://swarmsignal.net/ai-agent-security-2026/)
- [When AI agents act, security has to keep up – Federal News Network](https://federalnewsnetwork.com/commentary/2026/04/when-ai-agents-act-security-has-to-keep-up/)
- [Agentic AI Goes Mainstream, but 94% Raise Concern About Sprawl – OutSystems](https://www.outsystems.com/news/enterprise-ai-agent-report-2026/)

**Markt & Adoptie**
- [AI News Digest, April 28, 2026: An AI Voice Agent For Plumbers Just Hit $1B – asanify.com](https://asanify.com/blog/news/ai-agents-enterprise-stack-april-28-2026/)
- [Enterprise AI adoption in 2026: Why 79% face challenges – writer.com](https://writer.com/blog/enterprise-ai-adoption-2026/)
- [Agentic AI Goes Mainstream in the Enterprise – OutSystems](https://www.outsystems.com/news/enterprise-ai-agent-report-2026/)
- [The State of AI Adoption in the Enterprise Q1 2026 – bsykes.substack.com](https://bsykes.substack.com/p/the-state-of-ai-adoption-in-the-enterprise)
- [Microsoft prepares partners to push AI, agentic 365 bundles – CIO Dive](https://www.ciodive.com/news/microsoft-agentic-ai-365-bundles-frontier-partner-badges/818482/)
- [Google puts AI agents at heart of its enterprise money-making push – Reuters/TradingView](https://www.tradingview.com/news/reuters.com,2026:newsml_L6N4141GL:0-google-puts-ai-agents-at-heart-of-its-enterprise-money-making-push/)
- [AI agent trends 2026 report – Google Cloud](https://cloud.google.com/resources/content/ai-agent-trends-2026)
