---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-06
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 6 mei 2026

## 🔑 Highlights van de dag

- **Anthropic verbindt zich aan $200 miljard bij Google Cloud** over vijf jaar — een ongeëvenaarde cloudcommitment die bevestigt dat de AI-infrastructuuroorlog in feite al gewonnen lijkt door Google qua enterprise-partnerships. ([US News](https://www.usnews.com/news/top-news/articles/2026-05-05/anthropic-commits-to-spending-200-billion-on-googles-cloud-and-chips-the-information-reports))

- **IBM Think 2026 (4–7 mei)** bracht een reeks agentic AI-aankondigingen: IBM Bob (end-to-end AI-software development companion), IBM Concert (agentic operationsplatform) en Content Cortex (enterprise content voor agentautomatisering). De boodschap is helder: IBM positioneert zich sterk als enterprise-agentic speler naast Google en Microsoft. ([IBM](https://www.ibm.com/new/announcements/ibm-announcements-at-think-2026))

- **EU AI Act dreigt in de knel**: onderhandelingen in Brussel braken af op 28 april. Een nieuwe trilogue is voorzien, maar de August 2026-deadline voor handhaving van high-risk systemen staat onder druk. Dit heeft directe compliance-consequenties voor Nederlandse bedrijven. ([AI Act tracker](https://artificialintelligenceact.eu/))

- **Pentagon sluit AI-deals** met OpenAI, Google, Microsoft, Amazon, Oracle, Nvidia, SpaceX en Reflection AI — Anthropic werd bewust uitgesloten wegens gepercipieerde supply-chain-risico's na een contractgeschil. ([gHacks](https://www.ghacks.net/2026/05/04/pentagon-signs-ai-deals-with-openai-google-microsoft-nvidia-and-others-cutting-out-anthropic/))

- **MCP (Model Context Protocol) van Anthropic** overschreed 97 miljoen installaties in maart en is overgedragen aan de Linux Foundation (v1.2). De A2A-standaard van Google telt 150 productie-organisaties. Interoperabiliteit tussen agents wordt actief gestandardiseerd. ([The Next Web](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era))

## 🧠 Technologie & Modellen

**GPT-5.5** (uitgebracht 24 april) richt zich expliciet op agentic coding, computergebruik en diepgaand onderzoek. Het rolt uit naar Plus, Pro, Business en Enterprise gebruikers. ([CNBC](https://www.cnbc.com/2026/04/23/openai-announces-latest-artificial-intelligence-model.html))

**Claude Opus 4.7** is Anthropic's meest krachtige algemeen beschikbare model: sterkere software engineering-capabilities, betere instructieopvolging. Anthropic bracht ook tien vooraf geconfigureerde AI-agents uit voor de financiële sector (investment banking, asset management, verzekeringen). ([Anthropic](https://www.anthropic.com/news/claude-opus-4-7))

**Gemini 3.1 Ultra** van Google heeft een contextvenster van 2 miljoen tokens en werkt natively multimodaal (tekst, beeld, audio, video). Google heeft Vertex AI omgedoopt tot **Gemini Enterprise Agent Platform** en Agentspace geïntegreerd. Workspace Studio biedt een no-code agent builder.

**MCP en A2A**: Anthropic's MCP (Model Context Protocol) staat nu onder Linux Foundation-governance. Google's A2A-protocol bereikt v1.2 en zit eveneens bij de Linux Foundation's Agentic AI Foundation. Beide protocollen worden de de-facto interoperabiliteitsnormen voor agent-ecosystemen — dit is geen hype maar een concrete infrastructuurverschuiving.

## 🏛️ Governance & Ethiek

De EU AI Act gaat per **2 augustus 2026** volledig gehandhaafd worden: regels voor high-risk systemen (Annex III), transparantievereisten en nationale sandbox-verplichtingen treden dan in werking. Maar trilogue-onderhandelingen in Brussel braken op 28 april af. De voornaamste knelpunten: timing van handhaving high-risk systemen, gebruik van persoonsgegevens voor training en toezichtstructuur. ([Kennedys Law](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/))

Elk EU-lidstaat moet tegen augustus minstens één nationale AI-regulatoire sandbox operationeel hebben. Voor NL-bedrijven die AI inzetten in high-risk categorieën (zoals HR, kredietbeoordeling, kritieke infrastructuur) is dit het moment om compliance-voorbereiding te versnellen, niet af te wachten of de deadline verschuift.

## 🔐 Security & Risk

**CVE-2025-53773**: een kritieke kwetsbaarheid (CVSS 9.6) waarbij verborgen prompt injection in pull request-beschrijvingen remote code execution mogelijk maakt via GitHub Copilot. Dit is een concrete waarschuwing voor teams die AI-codeerassistenten gebruiken in CI/CD-pipelines.

**AI-gegenereerde code**: ~45% introduceert bekende beveiligingsfouten; 41% van AI-gegenereerde backend code bevat te brede permissie-instellingen. Teams die Copilot, Cursor of Claude Code inzetten moeten security-reviews niet overslaan.

**Supply chain aanval op SAP npm-packages**: aanvallers stalen ontwikkelaars- en CI/CD-credentials via kwaadaardige afhankelijkheden. Enterprise SAP-omgevingen zijn een doelwit. ([eSecurity Planet](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/))

**Exploitatiesnelheid**: de tijd van CVE-publicatie tot actief misbruik is gedaald van 700+ dagen (2020) naar 44 dagen (2025); 28,3% van CVEs wordt binnen 24 uur na publicatie geëxploiteerd. Patchmanagement moet radicaal sneller.

## 📈 Markt & Adoptie

Q1-resultaten bevestigen dat AI nu de groeiformule van clouddiensten is:
- **Google Cloud**: +63% YoY → $20 miljard omzet
- **AWS**: +28% → $37,6 miljard
- **Microsoft Azure**: +40%

Gezamenlijk investeren de drie hyperscalers ~$600 miljard in capex dit jaar. ([Fortune](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/))

**Anthropic** kondigt een enterprise AI-servicebedrijf aan samen met Blackstone, Hellman & Friedman en Goldman Sachs — gericht op mid-sized bedrijven die Claude willen inzetten met dedicated applied AI-engineers van Anthropic. Dit is directe concurrentie voor IT-consultancies als Ctac.

**Nederland**: 67% van bedrijven gebruikt AI (was 34% in 2023); Nederland staat 4e in de EU AI Index. De financiële sector loopt voorop, overheid en agri-food groeien het snelst. ([Searchlab](https://searchlab.nl/statistieken/ai-in-nederland-statistieken-2026))

## 💡 Ctac-relevantie

**Agentic AI wordt de standaard.** IBM, Google, Microsoft en nu ook Anthropic positioneren zich als "enterprise agentic platform". Ctac moet nu concretiseren wat de eigen positie is in dit landschap: bouw je agents *op* deze platformen (implementatiepartner), of ontwikkel je eigen agent-logica voor specifieke klantdomeinen (IP-strategie)? De window om hier een differentierende positie in te nemen wordt kleiner.

**EU AI Act compliance = direct klantkans.** Met de August 2026-deadline in aantocht en onderhandelingen die stagneren, zijn Nederlandse bedrijven in sectoren zoals finance, zorg en overheid op zoek naar compliance-begeleiding. Ctac kan dit als concrete dienst aanbieden — maar dan moet de interne kennis van Annex III en de governance-vereisten nu op orde zijn.

**Security blind spot bij AI-gedreven development.** De CVE-2025-53773-kwetsbaarheid in GitHub Copilot en de statistieken over AI-gegenereerde code zijn een directe reminder: als Ctac AI-codeerassistenten inzet in klantprojecten, moet er een expliciete security-review-stap in de pipeline zitten. Dit is zowel risicobeheersing als verkoopargument richting klanten.

**Anthropic's enterprise services concurrentie.** Het nieuwe servicebedrijf van Anthropic met Blackstone/Goldman is een signaal dat AI-labs zelf de consultancymarkt betreden. Dit vergroot de urgentie om als Ctac *complementaire* waarde te leveren (klantcontextkennis, Nederlandse markt, sector-expertise) die deze bedrijven niet hebben.

## 📚 Bronnen & verder lezen

- [US News – Anthropic $200B Google Cloud commitment (5 mei)](https://www.usnews.com/news/top-news/articles/2026-05-05/anthropic-commits-to-spending-200-billion-on-googles-cloud-and-chips-the-information-reports)
- [IBM Think 2026 aankondigingen](https://www.ibm.com/new/announcements/ibm-announcements-at-think-2026)
- [CNBC – GPT-5.5 aankondiging](https://www.cnbc.com/2026/04/23/openai-announces-latest-artificial-intelligence-model.html)
- [Anthropic – Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [The Next Web – Google Cloud Next 2026: A2A en Gemini Enterprise Agent Platform](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era)
- [artificialintelligenceact.eu – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Kennedys Law – EU AI Act August 2026 deadline](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/)
- [IAPP – AI Act Omnibus](https://iapp.org/news/a/ai-act-omnibus-what-just-happened-and-what-comes-next)
- [eSecurity Planet – supply chain aanvallen en AI security mei 2026](https://www.esecurityplanet.com/weekly-roundup/supply-chain-attacks-ai-security-and-major-breaches-define-this-week-in-cybersecurity-in-may-2026/)
- [The Hacker News – 2026: het jaar van AI-assisted attacks](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)
- [Fortune – Microsoft, Meta en Google AI capex Q1](https://fortune.com/2026/04/29/microsoft-meta-google-ai-capex-spending-billions/)
- [CNBC – Google Cloud +63% Q1 2026](https://www.cnbc.com/2026/04/30/google-microsoft-and-amazon-all-report-cloud-beats-in-earnings.html)
- [gHacks – Pentagon AI deals (Anthropic uitgesloten)](https://www.ghacks.net/2026/05/04/pentagon-signs-ai-deals-with-openai-google-microsoft-nvidia-and-others-cutting-out-anthropic/)
- [Searchlab – AI-adoptie Nederland 2026](https://searchlab.nl/statistieken/ai-in-nederland-statistieken-2026)
