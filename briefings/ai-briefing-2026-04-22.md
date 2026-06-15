---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-22
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 22 april 2026

## 🔑 Highlights van de dag

- **Anthropic blokkeert eigen model:** Het meest capabele model ooit (intern "Mythos") wordt niet publiek uitgebracht nadat het tijdens testen duizenden zero-day kwetsbaarheden identificeerde — ASL-4 geactiveerd. Een historisch veiligheidsmoment voor de sector.
- **Stanford AI Index 2026:** 88% van organisaties zet AI in; GenAI bereikte 53% populatieadoptie in 3 jaar — sneller dan de pc of het internet. De kloof tussen koplopers en achterblijvers groeit zichtbaar.
- **EU AI Act Digital Omnibus:** Parlement (569 stemmen voor) en Raad bereikten overeenstemming. High-risk compliance schuift door naar december 2027, maar watermarking-verplichtingen gelden al per 2 november 2026.
- **Agentic AI wordt productie-infrastructuur:** NVIDIA's Agent Toolkit is nu ondersteund door SAP, Salesforce, Adobe en 14 andere grote enterprise-spelers. SAP Joule Studio is GA.
- **Prompt injection: van theorie naar incident:** EchoLeak (Microsoft 365 Copilot) en CVE-2025-53773 (GitHub Copilot RCE, CVSS 9.6) tonen dat dit geen academisch risico is.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.4** is uitgebracht in drie varianten (Standard, Thinking, Pro) met een 1,05 miljoen token context-venster. Het model maakt 33% minder feitelijke fouten dan GPT-5.2. ([llm-stats.com](https://llm-stats.com/llm-updates))

**Google Gemini 3.1 Pro** leidt 13 van 16 benchmarks en haalt qua kwaliteit GPT-5.4 Pro in, maar kost via de API slechts een derde van de prijs — een significante kostendruk op OpenAI's enterprise-positie. ([llm-stats.com](https://llm-stats.com/ai-news))

**Claude Opus 4.7** (uitgebracht 16 april) vervangt Opus 4.6 als standaard Anthropic-model. Parallel houdt Anthropic het geavanceerdere "Mythos"-model achter vanwege veiligheidsoverwegingen — ASL-4 protocol. ([renovateqr.com](https://renovateqr.com/blog/ai-models-april-2026))

**Open source:** Google Gemma 4 (Apache 2.0, 2.3B–31B parameters, natively multimodaal), Meta Llama 4 Scout (10M token context, MoE) en DeepSeek V4 (1 biljoen parameters, open gewichten, trainingskosten slechts $5,2 miljoen) maken frontier-kwaliteit steeds toegankelijker. ([fazm.ai](https://fazm.ai/blog/new-llm-releases-april-2026))

---

## 🏛️ Governance & Ethiek

De **Digital Omnibus** (Parlement: 569 voor, Raad: akkoord 13 maart) stelt de high-risk compliance-deadline uit van augustus 2026 naar **december 2027** voor standalone systemen en **augustus 2028** voor systemen in gereguleerde producten. Positief voor bedrijven die tijd nodig hebben; risico is dat urgentie verdwijnt.

**Watermarking-verplichting** voor AI-gegenereerde audio, beeld, video en tekst gaat al in per **2 november 2026** — dit is concreet en nabij.

Handhaving blijft een zwak punt: de meeste EU-lidstaten hebben nog geen nationale markttoezichthouders aangewezen. De governance-structuur staat formeel, de tanden ontbreken nog. Triloog-conclusie verwacht mei–juni 2026. ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/), [onetrust.com](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/))

---

## 🔐 Security & Risk

**EchoLeak** is een zero-click prompt injection in Microsoft 365 Copilot die enterprise-data stil kan exfiltreren zonder gebruikersinteractie. Hoog risico voor Copilot-gebruikers in de enterprise. ([airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

**CVE-2025-53773:** Verborgen prompt injection in pull request-beschrijvingen leidt tot remote code execution via GitHub Copilot (CVSS 9.6). Direct relevant voor softwareontwikkelteams die GitHub Copilot inzetten. ([securityboulevard.com](https://securityboulevard.com/2026/04/ai-prompt-injection-attacks-examples-prevention-grip/))

**CIS-rapport (1 april 2026)** bestempelt prompt injection als "real and immediate risk." Verdediging is niet volledig mogelijk; risicoreductie vereist inputvalidatie, toegangsbeperking en menselijk toezicht op hoge-risico acties. ([cisecurity.org](https://www.cisecurity.org/about-us/media/press-release/new-cis-report-warns-prompt-injection-attacks-pose-growing-risk-to-generative-ai))

---

## 📈 Markt & Adoptie

**Stanford AI Index 2026:** 88% van organisaties gebruikt AI; 70% heeft GenAI ingezet in minstens één bedrijfsfunctie (was 33% in 2023). In Europa ligt regelmatig AI-gebruik op 40–48% van medewerkers. ([hai.stanford.edu](https://hai.stanford.edu/ai-index/2026-ai-index-report))

**PwC 2026 AI Performance Study:** 75% van de economische AI-winsten gaat naar slechts 20% van de bedrijven. Winnaars zijn gericht op groei, niet alleen op productiviteitsoptimalisatie. ([pwc.com](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html))

**NVIDIA Agent Toolkit** is nu operationeel met SAP, Salesforce en Adobe als eerste grote adopters. SAP Joule Studio (agentbouwer) is GA; Salesforce Headless 360 bouwt het volledige platform om tot AI-agent-infrastructuur (alle capabilities als API/MCP/CLI). ([venturebeat.com](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among))

**Microsoft** verlaagt de instapdrempel voor Copilot-korting van 1.500 naar 1.000 licenties en kondigt prijswijzigingen per 1 juli 2026 aan. ([learn.microsoft.com](https://learn.microsoft.com/en-us/partner-center/announcements/2026-april))

---

## 💡 Ctac-relevantie

**Directe veiligheidsactie vereist:** EchoLeak en de GitHub Copilot RCE zijn geen abstracte risico's — ze treffen Ctac-klanten die Copilot of GitHub Copilot actief gebruiken. Een snelle security- en governance-check op Copilot-implementaties is een concrete dienst die Ctac nu kan aanbieden.

**SAP-kans:** SAP Joule Studio GA + NVIDIA-integratie opent de deur voor de eerste productieve agentische SAP-implementaties. Ctac's SAP-expertise is hier een directe hefboom; klanten in finance en industrie lopen risico voorop te worden voorbijgestreefd als ze nu niet starten.

**Adoptie-kloof wordt strategisch:** De PwC-bevinding (20% pakt 75% van de waarde) maakt duidelijk dat snelheid van AI-adoptie bij klanten bepalend is voor hun concurrentiepositie. Ctac kan zich positioneren als "adoption accelerator" — niet als adviseur maar als uitvoerende partner die daadwerkelijk helpt implementeren.

**EU AI Act watermarking (november 2026):** Dit is de eerste concrete, nahbare deadline voor klanten in overheid, finance en zorg. Ctac kan nu al compliancescans aanbieden gericht op deze specifieke verplichting.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI Updates April 2026](https://llm-stats.com/llm-updates)
- [LLM Stats – AI News Today](https://llm-stats.com/ai-news)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [OneTrust – Digital Omnibus & AI Act](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/)
- [Airia – Prompt Injection & AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Security Boulevard – Prompt Injection Attacks](https://securityboulevard.com/2026/04/ai-prompt-injection-attacks-examples-prevention-grip/)
- [CIS – Prompt Injection Risk Report](https://www.cisecurity.org/about-us/media/press-release/new-cis-report-warns-prompt-injection-attacks-pose-growing-risk-to-generative-ai)
- [VentureBeat – NVIDIA Agent Toolkit met SAP/Salesforce](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Stanford HAI – AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- [PwC – 2026 AI Performance Study](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html)
- [Fazm – New LLM Releases April 2026](https://fazm.ai/blog/new-llm-releases-april-2026)
- [Kai Waehner – Enterprise Agentic AI Landscape 2026](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)
- [Microsoft Partner Center – April 2026 Announcements](https://learn.microsoft.com/en-us/partner-center/announcements/2026-april)
