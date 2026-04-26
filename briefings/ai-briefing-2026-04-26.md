---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-26
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 26 april 2026

## 🔑 Highlights van de dag

- **Anthropic verstopt zijn krachtigste model**: Claude Mythos bestaat en is verreweg het meest capabele model dat Anthropic ooit bouwde — maar het komt niet publiek beschikbaar. Vijftig geselecteerde organisaties krijgen gated toegang via het programma "Project Glasswing". Bewuste strategische keuze of signaal van veiligheidsangst?
- **OpenAI vs. Microsoft – publiek geworden breuk**: Een intern memo van OpenAI's revenue chief toont aan dat de Microsoft-samenwerking OpenAI actief heeft belemmerd bij enterprise-klanten. OpenAI pivot naar Amazon (AWS Bedrock) met naar eigen zeggen "staggering demand" na het $50 miljard partnerschap van februari.
- **Nederland heeft eindelijk een AI-toezichtstructuur**: Op 20 april publiceerde het kabinet de aanpak voor nationaal toezicht op de EU AI-verordening. Tien markttoezichtautoriteiten worden aangewezen; de AP en RDI krijgen een coördinerende rol. De Uitvoeringswet (UAIA) ligt t/m 1 juni in internet consultatie.
- **Prompt injection escaleert van theorie naar grootschalig risico**: Google meldt een 32% stijging in kwaadaardige promptaanvallen (nov'25–feb'26); drie AI coding agents lekten gevoelige informatie via één enkele aanval (VentureBeat). Dit is nu een productierisico, geen laboratoriumprobleem.
- **Azure vliegt, M365 Copilot kruipt**: Microsoft groeit 39% in cloud (ver boven AWS-19% en Google Cloud-30%), maar slechts 3,3% van de commerciële M365-basis converteert naar betaalde Copilot-seats. De infrastructuurlaag wint; de applicatielaag stelt teleur.

---

## 🧠 Technologie & Modellen

**Model-oorlog intensiveert aan de bovenkant én de onderkant.** GPT-5.5 is live in de API na GPT-5.4 (gelanceerd 5 maart), met recordscores op computer-use benchmarks OSWorld en WebArena. Antropic's Claude Sonnet 4.6 leidt op de GDPval-AA Elo benchmark (1.633 punten) — opvallend dat een Sonnet-tier model Opus-niveau presteert.

Open-source wint terrein: Google's GLM-5.1 verslaat GPT-5.4 op coderen onder MIT-licentie, en Gemma 4 is nu beschikbaar onder Apache 2.0. Dat is relevant voor Ctac-klanten die geen cloudafh ankelijkheid willen.

In benchmark-land: **AEC-Bench** is gelanceerd — het eerste multimodale benchmark voor AI-agents op bouw- en engineeringtaken (196 task instances, sandboxed Docker-omgeving). Relevant voor verticale sectoren. Bredere context: 79% van organisaties zet al AI-agents in; 40% van enterprise-apps heeft eind 2026 embedded agents. De verschuiving van "LLM als chatbot" naar "LLM als actor" is geen toekomst meer.

*Bronnen: [llm-stats.com](https://llm-stats.com/ai-news) · [whatllm.org](https://whatllm.org/blog/new-ai-models-april-2026) · [nomic.ai](https://www.nomic.ai/news/aec-bench-a-multimodal-benchmark-for-agentic-systems-in-architecture-engineering-and-construction)*

---

## 🏛️ Governance & Ethiek

**Nederland loopt voor de troepen uit** (althans Europees gezien). Terwijl slechts 8 van de 27 EU-lidstaten hun nationale toezichtautoriteiten hadden aangewezen per de deadline van augustus 2025, presenteerde het Nederlandse kabinet op 20 april een concrete structuur: tien domeinspecifieke markttoezichtautoriteiten, gecoördineerd door de AP en RDI. De Uitvoeringswet AI-verordening (UAIA) is in openbare consultatie t/m 1 juni 2026 — bedrijven en burgers kunnen reageren.

De **Digital Omnibus** (EU-niveau) stelt uitstel voor van de high-risk AI verplichtingen (Annex III standalone naar 2 december 2027). Maar let op: Article 50 transparantieverplichtingen voor generatieve AI en deepfakes gelden **ongeacht de Omnibus** per 2 augustus 2026.

*Bronnen: [rijksoverheid.nl](https://www.rijksoverheid.nl/actueel/nieuws/2026/04/20/kabinet-zet-stap-met-toezicht-op-europese-ai-regels) · [artificialintelligenceact.eu](https://artificialintelligenceact.eu/) · [legalnodes.com](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)*

---

## 🔐 Security & Risk

Prompt injection is in april 2026 definitief een productierisico geworden. Google's Security Blog documenteert een **32% stijging in kwaadaardige aanvallen** (november 2025 – februari 2026). VentureBeat meldt dat drie AI coding agents gevoelige informatie lekten via één prompt injection — waarbij één leverancier het risico al in zijn eigen system card had erkend maar niet gemitigeerd. Unit 42 (Palo Alto Networks) beschreef in maart de eerste grootschalige **indirecte** prompt injection aanvallen in het wild, inclusief advertentie-review omzeiling en system prompt leakage op commerciële platformen.

Het CIS heeft een formeel rapport uitgebracht dat prompt injection als ernstige en groeiende dreiging classificeert voor organisaties die generatieve AI gebruiken. Kernprobleem: LLMs kunnen structureel geen onderscheid maken tussen instructie en data.

*Bronnen: [security.googleblog.com](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html) · [venturebeat.com](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) · [helpnetsecurity.com](https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/)*

---

## 📈 Markt & Adoptie

De **OpenAI-Microsoft relatie is formeel gespannen**: OpenAI's revenue chief stelt in een intern gelekt memo dat Microsoft de enterprise-verkoop actief heeft belemmerd. De pivot naar AWS Bedrock levert naar eigen zeggen "staggering demand" op. Dit herschikt de cloudstrategie voor enterprise AI-inkoop.

**Azure groeit explosief** (39% YoY), maar Microsoft's $150 miljard jaarlijks capex toont ook hoeveel er ingezet wordt. M365 Copilot converteert slechts 3,3% van de commerciële basis — infrastructuur wint, applicatielaag volgt pas later. Intussen zetten 81% van enterprises al 3+ model families in (was 68% vorig jaar): niemand vertrouwt meer op één leverancier.

In Nederland en België is **Google AI-modus in Search** nu beschikbaar via Chrome (desktop en mobiel). Klein in schaal, groot in impact op informatiegedrag.

*Bronnen: [cnbc.com](https://www.cnbc.com/2026/04/13/openai-touts-amazon-alliance-in-memo-says-microsoft-has-limited-our-ability.html) · [geekwire.com](https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/) · [ictmagazine.nl](https://www.ictmagazine.nl/nieuws/google-zoeken-krijgt-ai-modus-in-nederland-en-belgie/)*

---

## 💡 Ctac-relevantie

**Compliance is nu concreet.** De Nederlandse UAIA-consultatie (t/m 1 juni) is een directe kans: Ctac-klanten in gereguleerde sectoren (overheid, zorg, finance) moeten hun AI-systemen classificeren vóór augustus 2026. Ctac kan hier als begeleider optreden, met name op de transparantieverplichtingen die sowieso gelden.

**Microsoft-advies vraagt nuance.** De M365 Copilot-teleurstelling (3,3% adoptie) bevestigt wat in de praktijk al zichtbaar is: tool-uitrol zonder change management werkt niet. Ctac-klanten die Copilot afnemen verdienen een eerlijk gesprek over adoptietrajecten, niet alleen licentie-verkoop.

**Multi-cloud AI is de norm geworden.** De OpenAI-Amazon pivot en de 81%-multi-model statistiek betekenen dat vendor lock-in adviezen herzien moeten worden. Ctac moet een cloud-agnostisch AI-aanbod kunnen positioneren.

**Prompt injection is nu een delivery-risico.** Elk agentic project dat Ctac bouwt of begeleidt moet een expliciete threat model hebben. De VentureBeat-case toont dat zelfs leveranciers die het risico kennen er niet altijd iets aan doen — dit is een onderscheidende propositie voor Ctac als verantwoord AI-implementatiepartner.

---

## 📚 Bronnen & verder lezen

- [llm-stats.com – AI model updates april 2026](https://llm-stats.com/ai-news)
- [whatllm.org – Anthropic Claude Mythos / Project Glasswing](https://whatllm.org/blog/new-ai-models-april-2026)
- [artificialintelligenceact.eu](https://artificialintelligenceact.eu/)
- [rijksoverheid.nl – kabinet AI-toezicht (20 april)](https://www.rijksoverheid.nl/actueel/nieuws/2026/04/20/kabinet-zet-stap-met-toezicht-op-europese-ai-regels)
- [digitaleoverheid.nl – Consultatie UAIA](https://www.digitaleoverheid.nl/nieuws/consultatie-uitvoeringswet-ai-verordening-van-start/)
- [legalnodes.com – EU AI Act 2026 compliance](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [security.googleblog.com – prompt injection state of affairs](https://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html)
- [venturebeat.com – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [helpnetsecurity.com – indirect prompt injection in the wild](https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/)
- [cnbc.com – OpenAI Amazon/Microsoft memo](https://www.cnbc.com/2026/04/13/openai-touts-amazon-alliance-in-memo-says-microsoft-has-limited-our-ability.html)
- [geekwire.com – M365 Copilot single-model era](https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/)
- [nomic.ai – AEC-Bench multimodal agentic benchmark](https://www.nomic.ai/news/aec-bench-a-multimodal-benchmark-for-agentic-systems-in-architecture-engineering-and-construction)
- [ictmagazine.nl – Google AI-modus NL/BE](https://www.ictmagazine.nl/nieuws/google-zoeken-krijgt-ai-modus-in-nederland-en-belgie/)
