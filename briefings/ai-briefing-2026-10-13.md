---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-13
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 13 oktober 2026

## 🔑 Highlights van de dag

- **GPT-6 is nu de standaard in ChatGPT** (uitgerold 7 oktober): gratis gebruikers krijgen GPT-6 Luna, betaalde gebruikers GPT-6 Sol. De "Intelligent UI" mengt tekst, grafieken, kaarten en interactieve formulieren in één antwoord – een duidelijke stap richting AI als interface, niet alleen als chatbot.
- **EU AI Act: enforcement loopt, deadlines verschuiven.** Handhaving is actief sinds 2 augustus 2026, maar de AI Omnibus (Verordening 2026/1744) duwde de verplichtingen voor hoogrisicorisicosystemen door naar december 2027. Op 2 december 2026 gaan de CSAM- en deepfake-verbodsbepalingen in.
- **Prompt injection blijft het #1 AI-beveiligingsrisico.** De OWASP Top 10 voor LLM-applicaties behoudt prompt injection als hoogste risico; GitLab patcht CVE-2026-90970 (sandbox-escape in Duo Agent Platform, gefixed 2 oktober).
- **Runtime governance wordt de nieuwe compliance-uitdaging.** Altijd-aan agents die over meerdere platforms opereren zijn ontworpen met controles voor deterministisch software – die zijn simpelweg niet toereikend voor LLM-gedreven agents (SiliconANGLE, 12 oktober).
- **Benelux: 74% gebruikt gen AI, maar slechts 24% meet de businesswaarde.** Xebia/Data Expo-rapport (415 respondenten): adoptie loopt voor op volwassenheid. Positief: 85% steunt Europese AI-onafhankelijkheid.

## 🧠 Technologie & Modellen

**GPT-6 van OpenAI** (7 oktober) is nu standaard in ChatGPT, met een gelaagd model: GPT-6 Luna (gratis) en GPT-6 Sol (betaald). De "Intelligent UI" in ChatGPT integreert dynamische interface-elementen in antwoorden – een functioneel interessante aanpak die de grens tussen chat en applicatie vervaagt.

**Claude Haiku 5.5** (Anthropic, 7 oktober) sluit de 5.5-familie af als snel, klein model – als eerste Haiku met instelbare inspanning (*adjustable effort*). Dit maakt het interessant voor kostenefficiënte productiescenario's waar je inference-budget wil beheren.

**Mistral Large 4** (6 oktober) is open-weight en beweert te concurreren met de beste gesloten modellen. De open gewichten volgen op 27 oktober – voor Ctac relevant bij klanten met data-soevereiniteitseisen of on-premise-voorkeur.

**Microsoft Work IQ** (oktober preview) koppelt Copilot en autonome agents aan live Dynamics 365- en Power Platform-data. Geen GA-datum of prijzen nog bekend, maar het signaleert de richting: agents niet als chatbot-uitbreiding, maar als geïntegreerde procesautomatisering.

**Gartner** voorspelt dat 40% van enterprise-software tegen eind 2026 taakspecifieke AI-agents zal bevatten – een maatstaf om klantgesprekken mee te voeren.

## 🏛️ Governance & Ethiek

De **EU AI Act** handhaaft actief sinds 2 augustus 2026 via het AI Office (GPAI-modellen) en nationale autoriteiten. De **AI Omnibus** (Verordening 2026/1744, van kracht 27 juli 2026) heeft de verplichtingen voor hoogrisicorisicosystemen uitgesteld: Bijlage III-systemen naar 2 december 2027, Bijlage I-producten naar 2 augustus 2028.

Meest urgent voor dit najaar: op **2 december 2026** gelden de verbodsbepalingen voor het genereren van niet-consensuele intieme content en CSAM. Organisaties die met generatieve media werken moeten dit nu regelen.

Boetes kunnen oplopen tot €15 miljoen of 3% van de wereldwijde jaaromzet. Niet alle lidstaten hebben hun nationale handhavingsautoriteit volledig aangesteld – dat is een compliance-risico voor cross-border opererende klanten.

## 🔐 Security & Risk

**CVE-2026-90970 (GitLab):** Een geauthenticeerde gebruiker van het Duo Agent Platform kon via een kwaadaardige flow-configuratie de prompt-sandbox ontsnappen en commando's uitvoeren op de AI Gateway. Gefixed 2 oktober. Dit is een schoolvoorbeeld van agentic AI-risico: het aanvalsoppervlak verschuift van de applicatielaag naar de agent-orkestratie.

**Vijil Diamond DART** (7 oktober): nieuw red-teaming platform specifiek voor enterprise AI-agents, gericht op beveiligingsfouten en beleidsschendingen. Interessant voor Ctac-klanten die agents in productie brengen.

De OWASP "lethal trifecta" voor agentsystemen: toegang tot privédata + blootstelling aan niet-vertrouwde content + externe communicatiemogelijkheid. Samen maken deze drie factoren van één geïnjecteerde prompt een exfiltratietool. Dit is geen theoretisch risico meer.

## 📈 Markt & Adoptie

De vijf grootste Amerikaanse cloud- en AI-infrastructuuraanbieders (Microsoft, Alphabet, Amazon, Meta, Oracle) besteden gezamenlijk **$660–690 miljard** aan capex in 2026 – bijna een verdubbeling ten opzichte van 2025.

**Microsoft Copilot** bereikt meer dan 300 miljoen gebruikers; Copilot Studio telt meer dan 160.000 organisaties met ruim 400.000 zelfgebouwde agents. Google hernoemde Vertex AI naar **Gemini Enterprise Agent Platform** en bundelde Agentspace daarin.

Kritische noot: twee derde van de ondervraagde bedrijven zit nog vast in pilot-fases en lukt het niet om AI naar productie te brengen. De ROI-discussie wordt urgenter naarmate de investeringen toenemen.

## 💡 Ctac-relevantie

**Voor de AI-unit:** De combinatie van GPT-6 Luna (gratis) en Haiku 5.5 (klein, instelbaar) biedt nu een sterk kostengedifferentieerd modellandschap voor klantoplossingen – gebruik dit in proposities waar kostenefficiëntie centraal staat.

**Agents in productie:** Microsoft Work IQ en de Gartner-prognose (40% enterprise software met agents eind 2026) maken het gesprek met klanten over agentische automatisering urgenter. Ctac kan dit als opening gebruiken richting Dynamics 365-klanten. Let op: runtime governance is de nieuwe compliance-drempel – bied dit als dienst aan.

**EU AI Act als verkoopargument:** De december 2026 CSAM/deepfake-deadline en de naderende Bijlage III-verplichtingen (december 2027) creëren concrete aanleiding voor compliance-gesprekken bij klanten in zorg, finance en overheid. Combineer dit met het Benelux AI Readiness-rapport (74% gebruik, 24% businesswaardemeting): er ligt een duidelijke gap die Ctac kan adresseren.

**Beveiliging als differentiator:** De GitLab CVE en de OWASP lethal trifecta zijn concrete cases om in klantgesprekken te gebruiken over veilig agent-design. Maak van security-by-design een standaard onderdeel van Ctac's agent-proposities.

## 📚 Bronnen & verder lezen

- [LLM Model Tracker – Releases October 2026](https://llmgateway.io/timeline/2026)
- [BenchLM AI – Model Updates October 2026](https://benchlm.ai/model-updates/releases/october-2026)
- [EU AI Act – Enforcement Framework (EC)](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [EU AI Act Timeline 2026 – Alice Labs](https://alicelabs.ai/en/insights/eu-ai-act-timeline-2026)
- [Al Jazeera – What came into force with the EU AI Act (augustus 2026)](https://www.aljazeera.com/news/2026/8/6/what-came-into-force-with-the-eus-ai-act-this-week-and-what-didnt)
- [OWASP Prompt Injection & AI Security Failures – Help Net Security](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [Indirect Prompt Injection: Universal Flaw – Futurum](https://futurumgroup.com/insights/indirect-prompt-injection-exposes-a-universal-ai-security-flaw-no-deployment-model-is-immune/)
- [AI Agents News Week of Oct 11, 2026 – AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)
- [AI Governance Shifts to Runtime – SiliconANGLE (12 okt 2026)](https://siliconangle.com/2026/10/12/ai-governance-shifts-runtime-always-agents-spread-dellaileadershipsymposium)
- [Microsoft & Google Rule Enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [AI Capex 2026: $690B Infrastructure Sprint – Futurum](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/)
- [Xebia & Data Expo – Benelux AI Readiness Report 2026](https://xebia.com/news/xebia-data-expo-benelux-ai-readiness-report-2026/)
