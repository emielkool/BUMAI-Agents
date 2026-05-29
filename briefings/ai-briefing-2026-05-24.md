---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-24
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 24 mei 2026

## 🔑 Highlights van de dag

- **Google Gemini 3.5 Flash** is op 19 mei gelanceerd als het sterkste Google-model tot nu toe voor coding én autonome agents. Het model bouwde in interne tests een volledig besturingssysteem – een signaal dat Google de agentic race serieus neemt.
- **AI Omnibus politiek akkoord**: op 7 mei bereikte de EU een politiek akkoord over de AI-vereenvoudigingswet; tegelijk publiceerde de Commissie op 8 mei conceptrichtlijnen voor transparantieverplichtingen (Art. 50 AI Act). De deadline van augustus 2026 nadert snel.
- **UWV kiest Microsoft Copilot** boven Mistral AI, wat Kamervragen opleverde over digitale soevereiniteit. Dit is een voorbode van een bredere spanning in de Nederlandse publieke sector.
- **Prompt injection**: onderzoek toont aanvalspercentages van >85% bij AI coding agents; drie agents lekten secrets via één aanval. Problematisch voor elke organisatie die code-agents inzet.
- **Twee derde van bedrijven** zit nog vast in de pilots-fase van gen-AI; slechts 27% verwacht rendement in de komende 1-2 jaar.

## 🧠 Technologie & Modellen

**Google Gemini 3.5 Flash** werd op 19 mei 2026 gelanceerd als Google's voorlopige topmodel voor agentic toepassingen: het kan zelfstandig coding-pipelines uitvoeren, research-projecten beheren en — in interne tests — een volledig OS bouwen. Google positioneert AI niet meer als chatbot maar als actieve medewerker. Tegelijk onthulde Google I/O 2026 *information agents* in Search die continu op de achtergrond draaien. ([TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/))

**Anthropic Mythos** is in mei uitgerold naar een beperkte groep partners — beschreven als het krachtigste model ooit, met bijzondere nadruk op cybersecuritytoepassingen. Anthropic breidde ook zijn partnerschap uit met PwC en de Gates Foundation ($200M). ([Anthropic](https://www.anthropic.com/news))

**Nvidia Agent Toolkit** (aangekondigd op GTC 2026) consolideert de complexiteit van agentic deployment in één platform, met Adobe, Salesforce, SAP en 14 andere early adopters. Nemotron-modellen voor agentic reasoning en OpenShell als open-source security runtime zijn de kernelementen. ([VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among))

## 🏛️ Governance & Ethiek

**EU AI Omnibus akkoord** (7 mei 2026): politieke overeenstemming over de AI-vereenvoudigingswet. Op 8 mei volgden conceptrichtlijnen voor de transparantieverplichtingen uit Art. 50 AI Act. Volledige handhaving start 2 augustus 2026 — minder dan 80 dagen. ([EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act))

**Nederland – UWV en Microsoft Copilot**: UWV start halverwege mei een pilot met Microsoft Copilot, waarmee wordt afgestapt van Mistral AI. D66-Kamerleden stellen vragen over digitale soevereiniteit. Dit raakt bredere spanning over vendor lock-in bij overheidsinstanties. ([Dutch IT Channel](https://www.dutchitchannel.nl/news/733688/kamervragen-over-ai-keuze-uwv-voor-microsoft-copilot))

**Gemeenten en anonimisering**: zes Nederlandse gemeenten (o.a. Hoeksche Waard) lanceerden een LLM-gebaseerde tool voor bronanonimisering van documenten — een praktisch voorbeeld van verantwoord AI-gebruik binnen de overheid. ([Computable](https://www.computable.nl/2026/05/19/gemeenten-lanceren-ai-tool-voor-bron-anonimisering/))

## 🔐 Security & Risk

**Prompt injection blijft structureel probleem**: recent onderzoek laat zien dat aanvalspercentages boven de 85% liggen, zelfs bij state-of-the-art verdedigingen. Drie AI coding agents lekten secrets via één aanval; één geval betrof een Claude Code GitHub Action die uitdrukkelijk niet was gehard tegen prompt injection. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)) ([TechCrunch](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/))

**Aanbeveling**: bij inzet van code-agents of browser-agents moeten minimale privileges, human-in-the-loop voor destructieve acties en whitelisting van content-bronnen als basisarchitectuur worden gehanteerd — geen optionele hardening.

## 📈 Markt & Adoptie

**Microsoft en Google** domineren de enterprise AI-markt. Google lanceerde de *Agentic Data Cloud* voor enterprise AI-agents; Microsoft heronderhandelt de samenwerking met OpenAI terwijl Azure flexibeler wordt richting multi-cloud. ([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)) ([CIO Dive](https://www.ciodive.com/news/microsoft-openai-rework-partnership/818606/))

**SAP** heeft een geïntegreerd platform gelanceerd voor het bouwen en deployen van AI — relevant voor Ctac-klanten in de SAP-space. ([CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/))

**Pilots-stagnatie**: twee derde van bedrijven zit nog vast in de pilots-fase; slechts 27% verwacht rendement binnen 1-2 jaar. Dit laat zien dat de vertaalslag van PoC naar productie het kernprobleem is — en een dienstverlening-kans. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

**Anthropic vs. OpenAI in enterprise**: Anthropic heeft OpenAI voorbijgestreefd in business AI-adoptie, maar wordt bedreigd door drie factoren die deze voorsprong kunnen wissen. ([VentureBeat](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead))

## 💡 Ctac-relevantie

**Van pilot naar productie is de urgentste propositie.** Twee derde van enterprise-klanten is vastgelopen in de pilots-fase. Ctac kan hier een concrete acceleratiepropositie op bouwen: structureer bestaande PoC's van klanten tot productie-ready deployments met aandacht voor governance, security (prompt injection) en change management.

**SAP-klanten** worden geraakt door SAP's nieuw geïntegreerde AI-platform. Voor Ctac's SAP-praktijk is het essentieel om dit in de advisering mee te nemen — klanten verwachten dat hun partner hier wegwijs in is.

**EU AI Act – augustus 2026 deadline**: klanten in gereguleerde sectoren (overheid, finance, zorg) moeten nu in actie komen voor transparantievereisten. Ctac kan hier compliance-quickscans aanbieden.

**Agent security as a service**: de structurele kwetsbaarheid van AI-agents voor prompt injection maakt security-assessment van agentic systemen een reëel en onderscheidend aanbod — zeker nu meer klanten agents deployen.

## 📚 Bronnen & verder lezen

- [Google Gemini 3.5 Flash – TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/)
- [Anthropic nieuws mei 2026](https://www.anthropic.com/news)
- [Nvidia Agent Toolkit – VentureBeat](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [EU AI Act transparantierichtlijnen Art. 50 – EC](https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act)
- [AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [UWV Copilot Kamervragen – Dutch IT Channel](https://www.dutchitchannel.nl/news/733688/kamervragen-over-ai-keuze-uwv-voor-microsoft-copilot)
- [Gemeenten AI-anonimiseringstool – Computable](https://www.computable.nl/2026/05/19/gemeenten-lanceren-ai-tool-voor-bron-anonimisering/)
- [Prompt injection AI coding agents – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [SAP AI-platform – CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [Microsoft/Google enterprise AI markt – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Anthropic vs OpenAI enterprise adoptie – VentureBeat](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)
