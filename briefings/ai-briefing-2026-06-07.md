---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-07
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 7 juni 2026

## 🔑 Highlights van de dag

- **Anthropic nadert biljoen-waardering:** Anthropic diende vertrouwelijk een IPO-aanvraag in na het afronden van een $65 miljard Series H-ronde op een waardering van $965 miljard — de meest waardevolle AI-startup ooit, nu boven OpenAI.
- **Gemini 3.5 Flash is beschikbaar:** Google's nieuwste model is algemeen beschikbaar met frontier-niveau intelligentie tegen 4× de snelheid van vergelijkbare modellen ($1,50/$9 per 1M tokens, 1M context) — een serieuze efficiency-sprong.
- **Microsoft vs. Google in AI-coding:** Microsoft lanceerde MAI-Code-1-Flash (eigen coding model) en Google scherpt zijn codeermodellen aan; beiden proberen OpenAI en Anthropic te doorbreken in een markt die groeit naar $30 miljard in 2031.
- **AI-agents out of control:** Slechts 10% van Fortune 500-bedrijven heeft een strategie om hun AI-agents te beheren, terwijl 80% die agents al actief heeft draaien — een governance-tijdbom.
- **Prompt injection is nu OWASP #1:** Microsoft publiceert waarschuwingen over RCE-kwetsbaarheden in agent frameworks; indirect prompt injection is gedocumenteerd in productieomgevingen op grote schaal.

---

## 🧠 Technologie & Modellen

**Gemini 3.5 Flash** is deze week algemeen beschikbaar gesteld — Google's antwoord op de kostendruk: frontier-prestaties met 4× hogere verwerkingssnelheid en een miljoentokens-contextvenster. Dit maakt het model interessant voor documentintensieve toepassingen in enterprise.

**Anthropic** rondt niet alleen een megabedrag op ($65B Series H), maar diende ook vertrouwelijk een IPO-aanvraag in. De Q2-omzet wordt verwacht op $10,9 miljard — een verdubbeling ten opzichte van Q1. Claude Opus 4.8 werd eind mei uitgebracht als hun sterkste model tot nu toe. De IPO, gepland voor oktober 2026, markeert het einde van de "startup-fase" van frontier AI.

**OpenAI** introduceert Daybreak, een cybersecurity-programma dat GPT-5.5-modellen combineert met Codex voor geautomatiseerde vulnerability-identificatie en patching. Tegelijk lanceerde OpenAI DeployCo, een eigen consulting-dochter met $4 miljard investering — een opvallende strategische verschuiving richting dienstverlening.

**Google DeepMind-CEO Demis Hassabis** schoof zijn AGI-schattingsdatum op naar 2029 — voor hem historisch vroeg. Voor strategisch plannen: houd hier rekening mee, al blijft de definitie van AGI betwist.

*Bronnen: [TechCrunch – Anthropic IPO](https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/) | [CNBC – Microsoft MAI-Code-1-Flash](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html) | [llm-stats.com](https://llm-stats.com/ai-news)*

---

## 🏛️ Governance & Ethiek

De internetconsultatie voor de **Nederlandse Uitvoeringswet AI-verordening** is op 1 juni gesloten. Het kabinet kiest voor een gedistribueerd toezichtmodel waarbij bestaande sectorale toezichthouders (ACM, AP, DNB etc.) AI binnen hun domein handhaven. Dit verlaagt de drempel voor bedrijven die al vertrouwd zijn met hun toezichthouder, maar creëert risico op fragmentatie bij cross-sectorale AI-systemen.

**Gartner** publiceert een waarschuwing: uniforme governance over alle AI-agents leidt juist tot falen. Agents vereisen gedifferentieerde governance afhankelijk van autonomie, risico en context — een nuance die veel compliance-frameworks nog missen.

*Bronnen: [ibestuur.nl – Uitvoeringswet consultatie](https://ibestuur.nl/digitale-toekomst-eu/eu-wetgeving/internetconsultatie-uitvoeringswet-ai-verordening-van-start) | [Gartner – AI Agent Governance](https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure)*

---

## 🔐 Security & Risk

**Prompt injection is nu OWASP #1-bedreiging** voor LLM-systemen. Indirect prompt injection — waarbij kwaadaardige instructies verstopt zitten in verwerkte documenten, e-mails of websites — werd in maart 2026 voor het eerst op grote schaal in productiepaden gedocumenteerd door Unit 42. Aanvallen stegen met 32% tussen november 2025 en februari 2026.

**Microsoft Security Blog (mei 2026):** RCE-kwetsbaarheden gevonden in populaire AI agent frameworks waarbij kwaadaardige prompts shellcommando's kunnen uitvoeren. Dit is geen theoretisch risico meer — het raakt elke organisatie die AI-agents met systeemtoegang inzet.

**Rubrik-onderzoek (Nederland):** 86% van Nederlandse organisaties verwacht dat AI-agents sneller groeien dan de eigen beveiligingsrichtlijnen; slechts 17% heeft volledig zicht op welke agents er actief zijn.

*Bronnen: [Microsoft Security Blog – RCE in agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/) | [airia.com – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) | [banken.nl – Rubrik onderzoek](https://www.banken.nl/nieuws/27149/rubrik-onderzoek-organisaties-verliezen-grip-op-snel-groeiend-aantal-ai-agents)*

---

## 📈 Markt & Adoptie

**Google Cloud** groeide 63% jaar-op-jaar naar $20 miljard omzet; Gemini Enterprise-gebruikers namen 40% toe afgelopen kwartaal (klanten: Bosch, Mars, Merck). **Azure** groeide 40% YoY — de sterkste divisie van Microsoft.

Toch: twee derde van de enterprise-bedrijven zit nog vast in de pilot-fase en lukt het niet AI-projecten naar productie te brengen. Dit is het dominante patroon in de markt — niet te veel AI, maar te weinig aansluiting op bedrijfsprocessen.

**IBM 2026 CEO Study (NL):** 90% van ondervraagde Nederlandse CEO's zegt AI-agents op grote schaal in te zetten. Dat wekt ook vertrouwen in de bereidheid om te investeren, maar de governance-lacune maakt die inzet risicovol.

*Bronnen: [CIO Dive – Microsoft & Google enterprise markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [Fortune – AI capex spending](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/) | [Frankwatching – Agentic AI governance](https://www.frankwatching.com/archive/2026/06/02/agentic-ai-met-deze-5-governance-regels-houd-je-de-controle/)*

---

## 💡 Ctac-relevantie

**Drie concrete kansen en één urgent risico:**

1. **AI-agent governance als propositie:** De combinatie van hoge adoptie (90% NL CEO's) en lage controle (17% heeft zicht op actieve agents) is precies het gat waar Ctac kan instappen. Een "AI Agent Governance Scan" als instapproduct voor klanten in overheid, finance en industrie is nu actueel en onderscheidend.

2. **Compliance-dienstverlening rond EU AI Act:** Nu de Nederlandse uitvoeringswet consultatie is afgerond, volgt de implementatiefase. Klanten hebben hulp nodig bij risicoklassificatie, menselijk toezicht en documentatie. Ctac's kennis van sectorale regelgeving (zorg, overheid) maakt dit een logische extensie.

3. **Model-selectie en kostenbeheer:** Gemini 3.5 Flash en aankomende efficiëntere modellen maken het haalbaar om AI-toepassingen goedkoper en sneller te bouwen. Intern: evalueer of de AI-unit hierop kan overstappen voor development en demonstrators.

4. **Urgent intern risico:** Als Ctac zelf agents inzet (intern of bij klanten), dan zijn de bevindingen over RCE-kwetsbaarheden en prompt injection direct van toepassing. Stel een minimale beveiligingsbaseline op vóór verdere uitrol — dit is geen optie meer.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Anthropic raises $65B, nears $1T valuation](https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/)
- [Fortune – Anthropic IPO filing at $965B valuation](https://fortune.com/2026/06/01/anthropic-confidentially-files-ipo-965-billion-valuation/)
- [CNBC – Microsoft MAI-Code-1-Flash](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)
- [CNBC – Microsoft & Google vs Anthropic & OpenAI in coding](https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html)
- [Microsoft Security Blog – RCE in AI agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Gartner – Uniform governance over AI agents leidt tot failure](https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure)
- [ibestuur.nl – Uitvoeringswet AI-verordening consultatie](https://ibestuur.nl/digitale-toekomst-eu/eu-wetgeving/internetconsultatie-uitvoeringswet-ai-verordening-van-start)
- [CIO Dive – Microsoft & Google domineren enterprise AI-markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [airia.com – AI Security 2026: prompt injection en lethal trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Frankwatching – 5 governance-regels voor agentic AI](https://www.frankwatching.com/archive/2026/06/02/agentic-ai-met-deze-5-governance-regels-houd-je-de-controle/)
- [Rubrik – organisaties verliezen grip op AI-agents (NL)](https://www.banken.nl/nieuws/27149/rubrik-onderzoek-organisaties-verliezen-grip-op-snel-groeiend-aantal-ai-agents)
- [llm-stats.com – AI model releases juni 2026](https://llm-stats.com/ai-news)
