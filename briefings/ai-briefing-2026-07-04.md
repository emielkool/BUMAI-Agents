---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-04
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 4 juli 2026

## 🔑 Highlights van de dag

- **Claude Sonnet 5 is de nieuwe standaard:** Anthropic verving per 1 juli Sonnet 4.6 als standaardmodel voor alle gratis en betaalde gebruikers. Sonnet 5 combineert bijna-Opus 4.8-prestaties met agentic browsing en terminal-gebruik — een significante verschuiving in de markt.
- **EU AI Act simplificatie formeel goedgekeurd:** De Raad van de EU gaf op 29 juni groen licht aan het Digital Omnibus-pakket. Gevolg: High-Risk AI-verplichtingen worden 16 maanden uitgesteld (tot december 2027), maar GPAI-handhaving gaat gewoon door op 2 augustus 2026.
- **Microsoft zet 6.000 medewerkers in voor AI-adoptie:** Het bedrijf lanceert tegelijk 'Microsoft Frontier Company' (€2,3 mrd) om enterprise-klanten direct te helpen AI productie-klaar te maken — en verhoogt M365-prijzen per 1 juli als dekking.
- **Agentic AI: ernstige kwetsbaarheden bevestigd:** Onderzoekers vonden een 85% exploitatiesucces-rate bij commerciële agents. 98% van productie-agents combineert privédata, externe content én uitgaande acties — een definitie van maximaal aanvalsoppervlak.
- **Open-source krachtsverhouding verschuift:** Kimi K2.6 (1,1T parameters, Modified MIT) en Qwen3 235B-A22B (Apache 2.0) bieden top-tier agentic prestaties als open gewichten, terwijl Hugging Face de 2,95 miljoen modellen-grens passeert.

## 🧠 Technologie & Modellen

**Anthropic Claude Sonnet 5** (30 juni) is Anthropics meest agentische Sonnet tot nu toe: autonome toolgebruik via browser en terminal, bijna-Opus 4.8-kwaliteit, fors goedkoper. Vanaf 1 juli is het het standaardmodel voor alle Free- en Pro-gebruikers. Tegelijkertijd werd **Claude Fable 5** na 18 dagen offline (US exportcontrole) globaal hersteld met een nieuwe veiligheidclassifier die de specifieke jailbreak-techniek in >99% van pogingen blokkeert.

**OpenAI** previewde op 26 juni de **GPT-5.6-familie** (Sol, Terra, Luna), vooralsnog achter een overheidstoegangslijst. Het eigengebouwde inferentie-chip **Jalapeño** (1 juli) is een strategische stap richting onafhankelijkheid van NVIDIA's H100-ecosysteem. **Google Gemini 3.5 Pro** gaat in juli algemeen beschikbaar — na een maand vertraging.

Noemenswaardig: Chinees **Z.ai GLM-5.2** benadert Opus 4.8/GPT-5.5-kwaliteit op coding en agentic taken voor een fractie van de prijs. Dit is geen hype — het herhaalt het DeepSeek-patroon: kostendruk op de westerse frontier-spelers.

## 🏛️ Governance & Ethiek

De **EU AI Act** nadert een cruciaal keerpunt. De Raad gaf op 29 juni definitief akkoord aan het Digital Omnibus-vereenvoudigingspakket; formele publicatie in het EU Staatsblad wordt verwacht vóór 2 augustus 2026.

Belangrijkste wijzigingen:
- **High-Risk AI (Annex III)**: verplichtingen uitgesteld van 2 augustus 2026 naar **2 december 2027**
- **GPAI-modellen**: handhaving (boetes), Article 50 transparantieplicht en nationale markttoezichtautoriteiten gaan gewoon door op **2 augustus 2026** — geen uitstel
- **Nieuwe verboden**: AI die non-consensueel intiem materiaal of CSAM genereert wordt verboden per 2 december 2026

Op 6 juli start in Genève het **VN Global Dialogue on AI Governance** — Jensen Huang (NVIDIA), Andy Jassy (AWS) en Brad Smith (Microsoft) zijn lid van de nieuwe VN AI-gouvernancecommissie. Significante signaalwaarde.

## 🔐 Security & Risk

De risico's rond **agentic AI** zijn niet langer theoretisch. Bevindingen van deze week:

- **GuardFall-kwetsbaarheid**: 30 jaar oude shell-injectietechnieken omzeilen de veiligheidsfilters van moderne AI-coderingsassistenten die shell-commando's uitvoeren met volledige accountrechten.
- **Privilege-escalatieschema's**: aanvallers manipuleren agents via meervoudige gespreksrondes of geïnjecteerde taakomschrijvingen om hoog-geprivilegieerde tools aan te roepen.
- **Detectiekloof**: 92% van security-leaders vertrouwt hun tooling om AI-kwetsbaarheden te vinden; 70% zag die kwetsbaarheden toch al in productie belanden.

De conclusie is duidelijk: organisaties die agents inzetten zonder expliciete privilege-beperking en sandboxing lopen significante risico's. Dit is een prioriteit voor elke AI-implementatie.

## 📈 Markt & Adoptie

Microsoft domineert enterprise-AI op volume (Azure AI $40B+ ARR, 400M+ M365-gebruikers) en zet nu 6.000 medewerkers in als "AI-adoptie-coaches" voor enterprise-klanten. De bijbehorende oprichting van **Microsoft Frontier Company** ($2,5 mrd) is bedoeld om AI-projecten daadwerkelijk productie-klaar te krijgen — een erkenning dat pilots niet vanzelf doorgroeien.

Tegelijk signaleert Gartner dat **twee derde van de bedrijven in pilot-fase vastzit**. Google wordt als winnaar gezien in enterprise agentic AI dankzij geïntegreerde tech stack; Microsoft wint op breedte en partnerecosysteem.

M365-prijsverhoging per 1 juli is een directe belasting op de bestaande softwareportefeuille van Ctac-klanten.

## 💡 Ctac-relevantie

**Korte termijn (augustus 2026):** GPAI-handhaving gaat live op 2 augustus. Klanten die Large Language Models in productie draaien (ook ingekochte modellen via API) vallen mogelijk al onder transparantieverplichtingen. Dit is een concrete compliancevraag voor Ctac's klantgesprekken nu.

**Agentic AI en security:** De bevindingen rond GuardFall en privilege-escalatie zijn direct relevant voor Ctac-projecten waarbij agents code uitvoeren of externe systemen aanroepen. Minimaal-privilege-architectuur en sandboxing moeten standaardonderdeel worden van Ctac's AI-implementatieaanpak.

**M365-prijsverhoging:** Klanten vragen waarom hun Microsoft-factuur stijgt. Dit is een gesprekskans voor Ctac om de AI-meerwaarde concreet te maken (of juist alternatieven te bespreken).

**Open-source kansen:** Kimi K2.6 en Qwen3 bieden frontier-kwaliteit onder open licenties. Voor kostenbesparende klantoplossingen zonder vendor lock-in is dit de moeite van een PoC waard.

## 📚 Bronnen & verder lezen

- [Anthropic Newsroom – Claude Sonnet 5](https://www.anthropic.com/news)
- [AI News Today July 3 2026 – Build Fast with AI](https://www.buildfastwithai.com/blogs/ai-news-today-july-3-2026)
- [EU AI Act – Digital Omnibus update (DLA Piper)](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [EU AI Act News 2026 – Axis Intelligence](https://axis-intelligence.com/eu-ai-act-news/)
- [EU AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [Microsoft mobilizes 6,000 workers for enterprise AI – American Bazaar](https://americanbazaaronline.com/2026/07/02/microsoft-mobilizes-workers-to-accelerate-enterprise-ai-adoption-483962/)
- [Microsoft, Google push AI agent governance – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Top Agentic AI Security Resources July 2026 – Adversa AI](https://adversa.ai/blog/top-agentic-ai-security-resources-july-2026/)
- [AI Security Vulnerabilities 2026 – RedFox Security](https://www.redfoxsec.com/blog/the-biggest-ai-security-vulnerabilities-discovered-in-2026-redfox-cybersecurity)
- [State of Open Source – Hugging Face Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [LLM Updates July 2026 – llm-stats.com](https://llm-stats.com/llm-updates)
- [UN AI Governance Dialogue – UN News](https://news.un.org/en/story/2026/07/1167848)
