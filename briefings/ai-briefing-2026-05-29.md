---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-29
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 29 mei 2026

## 🔑 Highlights van de dag

- **Google I/O (19 mei) en Gemini 3.5 Flash** domineren de week: Google claimt miljarden kostenbesparingen voor enterprise en zet vol in op agents in plaats van chatbots — een strategische keuze die Microsoft direct uitdaagt.
- **Microsoft Agent 365** werd begin mei GA ($15/gebruiker) en telt al tientallen miljoenen geregistreerde agents; voor het eerst heeft enterprise-IT een centraal besturingsvlak voor AI-agents.
- **RSI (Recursive Self-Improvement)** is het nieuwe buzzword na AGI: volop in roadmaps, maar daadwerkelijke zelf-verbeterende systemen bestaan nog niet — gezonde portie scepsis gepast.
- **EU AI-omnibus** politiek akkoord bereikt op 7 mei 2026; concrete guidelines voor high-risk AI-systemen verwacht in Q2 2026, deadlines strekken tot 2027–2028.
- **Prompt injection** blijft de achilleshiel van agentic AI: kwetsbaarheid in Google Antigravity IDE, multi-stap aanval op Claude ('Claudy Day'), 30+ CVEs in coding assistants gedocumenteerd.

## 🧠 Technologie & Modellen

**Gemini 3.5 Flash en Antigravity 2.0 (Google I/O, 19 mei)**
Google lanceerde Gemini 3.5 Flash: een snel model dat presteert op par met grotere flagships op agentic benchmarks (Terminal-Bench 2.1: 76,2%) maar tegen aanzienlijk lagere inferentiekosten. Google claimt potentiële besparingen van meer dan $1 miljard per jaar voor enterprise-klanten. Tegelijkertijd verscheen Antigravity 2.0 — een standalone desktop-app met CLI en SDK voor het orkestreren van meerdere agents tegelijk — en Gemini Spark, een always-on agentic assistent met Gmail-integratie. Google zet hiermee expliciet de switch van chatbot naar agent als primaire interface.
→ [TechCrunch: Gemini 3.5 Flash](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/) | [Google Blog: 100 aankondigingen I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)

**Anthropic Claude Opus 4.7**
Anthropic bracht begin mei Opus 4.7 uit, met verbeterde prestaties op coding- en agentic taken. Onderdeel van een bredere uitbreiding van het Opus-portfolio.
→ [Anthropic: Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)

**RSI: hype of echte horizon?**
TechCrunch signaleerde gisteren (28 mei) dat 'Recursive Self-Improvement' (RSI) het nieuwe AGI is geworden — een term die in talloze vendor-roadmaps opduikt. Startups als Sochers 'Recursive Superintelligence' claimen volledig automatische AI-onderzoekscycli. De realiteit is nuchterder: zelf-gerichte RSI bestaat nog niet. Andrej Karpathy's 'Auto-Research'-project is interessant maar beperkt in scope. Bewust blijven van dit onderscheid is voor Ctac relevant in klantgesprekken.
→ [TechCrunch: RSI is the new AGI (28 mei)](https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/)

## 🏛️ Governance & Ethiek

**EU AI-omnibus: politiek akkoord op 7 mei**
Er werd een politiek akkoord bereikt over het AI-omnibusvoorstel. De tijdlijn: high-risk AI-systemen in biometrie, kritieke infrastructuur, onderwijs en arbeidsmarkt vallen onder de regels vanaf **december 2027**; voor producten (liften, speelgoed) geldt **augustus 2028**. In Q2 2026 publiceert de Commissie guidelines over high-risk classificatie, transparantievereisten en incidentrapportage.
→ [EU AI Act tracker](https://artificialintelligenceact.eu/) | [EC: AI Act implementatie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Nederland: 70 miljoen voor AI-fabriek Groningen**
Het Rijk investeert 70 miljoen euro in de AI-fabriek Groningen (expertisecentrum + gespecialiseerde supercomputer voor model-training). Start verwacht na EC-goedkeuring, najaar 2026.
→ [NOS: AI-fabriek Groningen](https://nos.nl/artikel/2572670-rijk-steekt-nu-ook-70-miljoen-in-ai-fabriek-groningen)

## 🔐 Security & Risk

**Prompt injection: structureel architectuurrisico**
Drie recente kwetsbaarheden illustreren hoe groot het risico is nu AI-agents actief taken uitvoeren:
1. **Google Antigravity IDE** (april 2026): prompt injection-flaw leidde tot remote code execution — inmiddels gepatcht.
2. **'Claudy Day'-aanvalsketen** op Claude: drie stappen gecombineerd maken het mogelijk om een chatsessie stil te overnemen en data te exfiltreren met één klik.
3. **30+ CVEs** gedocumenteerd in coding assistants, waaronder credential theft en volledige systeemcompromis.

Het NCSC UK stelt dat prompt injection "nooit volledig gemitigeerd" kan worden. Dit is een structureel architectuurrisico, geen patch-bare bug.
→ [The Hacker News: Antigravity IDE flaw](https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html) | [VentureBeat: AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)

## 📈 Markt & Adoptie

**Microsoft Agent 365: besturingsvlak voor enterprise AI (GA 1 mei)**
Agent 365 ($15/gebruiker/maand) geeft IT- en securityleiders één plek voor het observeren, beheren en beveiligen van agents. In twee maanden: tientallen miljoenen agents in de Registry, tienduizenden klanten actief. De gelijktijdige GA van **Microsoft 365 E7 (Frontier Suite)** bundelt M365 E5, Entra Suite, Copilot en Agent 365 in één enterprise AI-platform.
→ [Microsoft Blog: Frontier Suite](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/) | [CIO Dive: Microsoft & Google domineren](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

**Microsoft adopteert Google's A2A-interoperabiliteitsstandaard**
Microsoft committeert zich aan het Agent-to-Agent (A2A) protocol van Google — een opmerkelijke stap richting open standaarden in de agentmarkt die op termijn vendor lock-in kan verminderen.
→ [CIO Dive: A2A interoperabiliteit](https://www.ciodive.com/news/Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)

**Google: 8,5 miljoen ontwikkelaars, 375 klanten > 1 biljoen tokens/jaar**
Google rapporteerde bij I/O 2026: 8,5 miljoen ontwikkelaars bouwen maandelijks met hun modellen, en 375 Google Cloud-klanten verwerken elk meer dan 1 biljoen tokens per jaar — een indicatie van de schaal van enterprise AI-gebruik.
→ [Google Blog: Sundar Pichai I/O 2026](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)

## 💡 Ctac-relevantie

**Agent 365 en Frontier Suite openen nieuwe propositie**
Voor Ctac-klanten die al met Microsoft 365 Copilot werken is Agent 365 de logische volgende stap. Dit opent proposities rond agent governance, integratie met bestaande Ctac-implementaties (SAP, Dynamics, custom software) en complianceadvies — concreet op te pakken in bestaande trajecten.

**Prompt injection als delivery-standaard**
Nu Ctac meer agentic oplossingen bouwt, wordt prompt injection een concreet leveringsrisico. Input-validatie, sandboxing en het expliciteren van vertrouwensgrenzen horen standaard in projectarchitecturen thuis — niet als optionele extra.

**EU AI Act: 18 maanden voor high-risk klanten**
Met guidelines in Q2 2026 en deadlines vanaf december 2027 hebben klanten in zorg, overheid en HR nu ~18 maanden om compliant te worden. Concrete aanleiding voor een AI-governance propositie naar deze sectoren vanuit de BUM AI-unit.

**RSI-terminologie: nuchter duiding geven**
Vendors zullen RSI-claims steeds vaker inzetten. Ctac kan zich onderscheiden door klanten te helpen onderscheid te maken tussen werkelijke capability en roadmap-marketing.

## 📚 Bronnen & verder lezen

- [TechCrunch: RSI is the new AGI (28 mei 2026)](https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/)
- [TechCrunch: Gemini 3.5 Flash bets on agents](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/)
- [TechCrunch: Antigravity 2.0](https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/)
- [Google Blog: 100 aankondigingen I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Google Blog: Sundar Pichai I/O-keynote 2026](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)
- [VentureBeat: Gemini 3.5 Flash enterprise besparingen](https://venturebeat.com/technology/google-says-gemini-3-5-flash-can-slash-enterprise-ai-costs-by-more-than-1-billion-a-year)
- [Anthropic: Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [EC: AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC: AI Act governance](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [NOS: AI-fabriek Groningen](https://nos.nl/artikel/2572670-rijk-steekt-nu-ook-70-miljoen-in-ai-fabriek-groningen)
- [The Hacker News: Google Antigravity IDE flaw](https://thehackernews.com/2026/04/google-patches-antigravity-ide-flaw.html)
- [VentureBeat: AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Microsoft Blog: Frontier Suite](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)
- [CIO Dive: A2A interoperabiliteit](https://www.ciodive.com/news/Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [CIO Dive: Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
