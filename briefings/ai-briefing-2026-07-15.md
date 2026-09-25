---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-15
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 15 juli 2026

## 🔑 Highlights van de dag

- **EU AI Act finaliseert vóór 2 augustus deadline:** Na goedkeuring door de Raad (29 juni) wordt publicatie in het Staatsblad verwacht vóór 2 augustus; de AI Office krijgt centraal toezicht op GPAI-modellen en een deel van de high-risk verplichtingen wordt uitgesteld.
- **Microsoft zet $2,5 miljard in op deployment, niet op modellen:** Met 6.000 forward-deployed engineers bij klanten draait Microsoft's AI-strategie volledig naar implementatie — de modelstrijd is voorbij, de uitrolstrijd begint.
- **Frontier-modellen convergeren:** Claude Sonnet 5, GPT-5.6 en Gemini 3.2 Pro zitten zo dicht bij elkaar dat differentiatie verschuift naar prijs, context-window en integratie — niet naar modelkwaliteit.
- **Prompt injection: 340% meer aanvallen, twee kritieke CVE's bevestigd:** CVE-2025-53773 (GitHub Copilot, CVSS 9.6) en CVE-2025-32711 "EchoLeak" (Microsoft 365 Copilot, CVSS 9.3) illustreren dat agentic AI een nieuw aanvalsoppervlak creëert.
- **Kabinet NL presenteert internationale AI-strategie:** Op 3 juli publiceerde het Nederlandse kabinet een strategie gericht op bescherming van Nederlandse waarden en belangen in de mondiale AI-transitie.

## 🧠 Technologie & Modellen

De afgelopen twee weken kenmerken zich door een golf van frontier-releases. **Claude Sonnet 5** (Anthropic, 30 juni) levert Opus-klasse coding-prestaties voor een derde van de prijs. **GPT-5.6** (OpenAI) rolde gestaffeld uit vanaf eind juni. **Grok 4.5** (xAI, 8 juli) en **Gemini 3.2 Pro** (Google, 2M context-window) completeren het frontier-beeld. Aan open-source kant leveren **DeepSeek V4.5** (MIT-licentie) en **Meta Llama 5** sterke benchmarkscores op MMLU Pro en FrontierMath v2.

De kernboodschap: frontier-modellen zijn nagenoeg gelijkwaardig in kwaliteit. Toegevoegde waarde verschuift naar prijs, contextlengte, tooling-integratie en deployment-gemak — niet naar welk logo je kiest.

*Bronnen: [LLM Stats](https://llm-stats.com/ai-news) · [BenchLM.ai](https://benchlm.ai/) · [Build Fast with AI](https://www.buildfastwithai.com/blogs/best-ai-models-july-2026-ranked)*

## 🏛️ Governance & Ethiek

De **EU AI Act** bereikt een cruciale mijlpaal: publicatie in het Staatsblad wordt verwacht vóór **2 augustus 2026** — de datum van volledige toepasbaarheid. Kernwijzigingen uit het vereenvoudigingspakket: de AI Office krijgt gecentraliseerd toezicht over GPAI-modellen, meer organisaties krijgen toegang tot regulatory sandboxes (inclusief een EU-level sandbox), en high-risk AI-verplichtingen worden deels uitgesteld via de **Digital AI Omnibus**.

In Nederland presenteerde het **kabinet op 3 juli** een internationale AI-strategie om Nederlandse waarden en belangen te beschermen in de mondiale AI-transitie.

*Bronnen: [Consilium EU](https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/) · [DLA Piper GENIE](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) · [Rijksoverheid](https://www.rijksoverheid.nl/actueel/nieuws/2026/07/03/kabinet-presenteert-internationale-strategie-voor-veilige-en-verantwoorde-ai-transitie)*

## 🔐 Security & Risk

**Prompt injection** blijft OWASP's #1 LLM-risico en het aanvalsvolume steeg met **340% jaar-op-jaar**. Twee recente CVE's onderstrepen de ernst:

- **CVE-2025-53773** (CVSS 9.6): verborgen prompt injection in pull request descriptions activeerde remote code execution via GitHub Copilot.
- **CVE-2025-32711 "EchoLeak"** (CVSS 9.3): zero-click exfiltratie uit Microsoft 365 Copilot via verborgen instructies in PowerPoint-speakernotes — zonder gebruikersinteractie.

De consensus: filtering werkt niet betrouwbaar genoeg. Alleen **containment** (privilege separation, output validation, human-in-the-loop) biedt echte verdediging. De **Nederlandse Autoriteit Persoonsgegevens** waarschuwt dat AI cyberaanvallen makkelijker, sneller en meer gepersonaliseerd maakt.

*Bronnen: [Help Net Security](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) · [AI Agent Security Risks 2026](https://blog.cyberdesserts.com/ai-agent-security-risks/)*

## 📈 Markt & Adoptie

**Microsoft** lanceerde op 2 juli een dedicated AI deployment unit van $2,5 miljard met 6.000 medewerkers die bij klanten worden ingebed. Klanten als London Stock Exchange Group, Unilever en Land O'Lakes zijn al aangesloten. Het model: klanten kiezen zelf tussen Microsoft-modellen, third-party of open-source.

**Anthropic** is naar verluidt marktleider in AI-revenue geworden (~$47 miljard annualized, winstgevend in 2026) en voert gesprekken met Samsung over een custom AI-chip. IPO-geruchten voor oktober circuleren. **Google Cloud** introduceerde op Next '26 een Gemini Enterprise-platform voor agent-orchestratie op enterprise-schaal. **Amazon** investeert $1 miljard in forward-deployed engineers. Enterprise-AI maakt inmiddels ruim 40% van OpenAI's omzet uit.

*Bronnen: [TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) · [Fortune](https://fortune.com/2026/07/03/microsoft-big-bet-swiss-army-knife-enterprise-ai-frontier/) · [CNBC](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html)*

## 💡 Ctac-relevantie

**EU AI Act – 2 augustus over twee weken:** Ctac-klanten in regulated sectoren (overheid, finance, zorg) moeten nu actie ondernemen op AI-registerverplichtingen en high-risk classificatie. Dit is directe advisory-business. De regulatory sandbox-verbreding biedt ook kansen voor innovatieve klantprojecten.

**Microsoft's deployment pivot bevestigt Ctac's positie:** Forward deployed engineering is precies wat Ctac doet als implementatiepartner. Positioneer Ctac als de lokale tegenhanger voor de Nederlandse MKB- en midmarket-klant — vóórdat Microsoft's eigen unit ook dat segment bereikt.

**Security-actie voor M365 Copilot-klanten:** EchoLeak (CVSS 9.3) treft elke organisatie die Microsoft 365 Copilot inzet. Concrete aanbeveling: adviseer klanten om Copilot-extensies en document-ingest te controleren op privilege-scope en output-validatie, en schakel document-processing-extensies tijdelijk uit bij onbekende bestandsbronnen.

**Modelconvergentie versterkt IP-strategie:** Nu frontier-modellen kwalitatief gelijkwaardig zijn, zit de waarde van een AI-consultant niet in de modelkeuze maar in implementatiekwaliteit. Ctac's platform-gedreven IP-strategie wordt daarmee urgenter en beter verdedigbaar richting klanten.

## 📚 Bronnen & verder lezen

- [LLM Stats – AI nieuws juli 2026](https://llm-stats.com/ai-news)
- [BenchLM.ai – model benchmarks](https://benchlm.ai/)
- [Build Fast with AI – beste modellen juli 2026](https://www.buildfastwithai.com/blogs/best-ai-models-july-2026-ranked)
- [TechCrunch – Microsoft AI deployment unit](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [Fortune – Microsoft enterprise AI bet](https://fortune.com/2026/07/03/microsoft-big-bet-swiss-army-knife-enterprise-ai-frontier/)
- [CNBC – Microsoft $2,5B commitment](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html)
- [Consilium EU – AI Act vereenvoudiging](https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/)
- [DLA Piper – Digital AI Omnibus](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [Rijksoverheid – Nederlandse AI-strategie](https://www.rijksoverheid.nl/actueel/nieuws/2026/07/03/kabinet-presenteert-internationale-strategie-voor-veilige-en-verantwoorde-ai-transitie)
- [Help Net Security – OWASP prompt injection](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [AI Agent Security Risks 2026](https://blog.cyberdesserts.com/ai-agent-security-risks/)
- [artificialintelligenceact.eu – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
