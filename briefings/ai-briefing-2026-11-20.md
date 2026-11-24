---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-20
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 20 november 2026

## 🔑 Highlights van de dag

- **Anthropic naar de beurs:** Gisteren (19 november) debuteerde Anthropic op de Nasdaq met ticker ANT. De koers sloot op $97,17 (+17% boven de IPO-prijs van $83), wat neerkomt op een volledig verwaterde marktkapitalisatie van $1,76 biljoen. De beursgang haalde meer dan $100 miljard op — een historisch record.
- **Microsoft Ignite: agent-cloud en zeven nieuwe modellen:** Microsoft presenteerde op Ignite de visie dat frontier-modellen commoditiseren en kondigde Azure HorizonDB (GA), Agent 365 en Microsoft Entra Agent ID aan voor enterprise agent-governance. Daarnaast lanceerde Microsoft zeven eigen AI-modellen gericht op coding en cybersecurity, waaronder MAI Code 2.
- **Google Gemini 4 Neon live:** Google bracht op 18 november Gemini 4 Neon uit, met een context van 1 miljoen tokens en geoptimaliseerd voor coding en wetenschappelijke analyse. Het model staat op de derde plek van de Artificial Analysis Intelligence Index.
- **MCP-kwetsbaarheden in opmars:** Een AWS API MCP Server policy bypass (CVSS 7.8) en een Flowise SSRF-issue werden in november gepubliceerd — een signaal dat het MCP-ecosysteem snel groeit én kwetsbaarder wordt.
- **EU AI Act: hoog-risico deadline 14 maanden uitgesteld:** Door de AI Omnibus-wijzigingen verschuift de Annex III hoog-risico deadline van 2 augustus 2026 naar 2 december 2027. Op 2 december 2026 treden wel nieuwe verboden in werking (CSAM/NCII-gegenereerde content).

---

## 🧠 Technologie & Modellen

**Google Gemini 4 Neon** (18 november) is Googles nieuwste enterprise- en coding-model met een 1M-token context. Prijs: $3 per miljoen input-tokens, $15 per miljoen output-tokens. Het model scoort #3 op de Artificial Analysis Intelligence Index. Google opende tegelijkertijd zijn Tasks AI-agent gratis in zes landen via Gemini 4. ([The Neuron, 19 nov](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-november-19-2026/))

**Microsoft MAI Code 2 en zes andere modellen** (17 november) worden gepositioneerd als goedkopere alternatieven voor OpenAI en Anthropic. Microsoft claimt dat MAI Code 2 96% van Claude Opus 5.5's prestaties haalt op vier coding-benchmarks voor 5% van de prijs. Verifieer dit zelf — het zijn vendor claims. ([eWeek](https://www.eweek.com/news/microsoft-seven-ai-models-openai-anthropic/))

**Anthropic Claude Fable/Mythos 5.2** (9 november, beperkte toegang) staat in de release-trackers maar een bevestigde officiële naam ontbreekt — de bronnen wijken af. Wacht op officiële aankondiging van Anthropic.

**OpenAI**: Voorbereiding van een nieuw model in de *Terra*-familie wordt gemeld, mogelijk komende weken. De GPT-6.2 Astra/Sol-berichten komen alleen uit onbevestigde aggregatorsites; niet betrouwbaar zonder primaire bron.

---

## 🏛️ Governance & Ethiek

**EU AI Act enforcement is per 2 augustus 2026 van kracht.** De AI Omnibus-wijzigingen (aangenomen mei/juni 2026, in werking per 27 juli) verschoven de Annex III hoog-risico verplichtingen van augustus 2026 naar **2 december 2027**. Product-embedded AI zou verschuiven naar 2028. Dit geeft organisaties extra tijd, maar ontslaat hen niet van voorbereiding.

**Nieuwe verboden per 2 december 2026** betreffen AI-gegenereerde CSAM en niet-consensuele intieme beelden. Generatieve AI die vóór 2 augustus 2026 al op de markt was, heeft tot 2 december 2026 voor de markering-vereiste (Art. 50(2)).

**Nog geen boetes:** Vanaf de eerste enforcement-datum is er tot begin november 2026 nog geen AI Act-boete gepubliceerd. De praatjes zijn nog beleidsmatig; de tanden tonen zich nog niet.

Bronnen: [EC AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | [DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) | [Cubbbix](https://cubbbix.com/blog/ai-regulation-november-2026-global-update)

---

## 🔐 Security & Risk

**Recordaantal CVE's in 2026**: het totaal overschreed de 100.000 — mede aangedreven door AI-gebruik in security-onderzoek. De mediane tijd van disclosure naar exploitatie daalde van 120 dagen (2025) naar 80 dagen (H1 2026). ([SC World](https://www.scworld.com/brief/artificial-intelligence-drives-record-surge-in-software-vulnerabilities))

**LiteLLM AI gateway kwetsbaarheid** (CVE-2026-40217) werd op 18 november door CISA aan de KEV-catalogus toegevoegd, met een federale patch-deadline van 2 december. Organisaties die LiteLLM gebruiken als AI-gateway moeten dit urgentiegewijs oppakken. ([BTI Group, 20 nov](https://www.btigroup.com/post/ai-cybersecurity-update-november-20-2026/))

**MCP-ecosysteem kwetsbaar**: Een AWS API MCP Server policy bypass (CVSS 7.8, 10 november) en Flowise SSRF (CVSS 7.1, 17 november) staan in de AI Model Vulnerability Tracker. MCP is het koppelprotocol voor AI-agents aan tools — groeiend adoptieniveau, groeiend aanvalsoppervlak. ([axis-intelligence](https://axis-intelligence.com/research/ai-model-vulnerability-tracker/))

**Bank of England + FCA** publiceerden op 19 november richtlijnen voor het managen van AI-cyberrisico bij financiële instellingen — een voorteken voor sectorspecifieke regulering buiten de EU AI Act.

**Arizona AG opent strafrechtelijk onderzoek** naar OpenAI en andere AI-bedrijven vanwege vermeende infiltratie van banksystemen door autonome AI-agents.

---

## 📈 Markt & Adoptie

**Anthropic IPO** is het marktnieuws van de week. Met een waardering van $1,76 biljoen is Anthropic nu groter dan veel traditionele techgiganten. Dit signaleert dat investeerders frontier-AI-labs als strategische infrastructuur waarderen — niet als startup-speculatie. ([CNBC](https://www.cnbc.com/2026/11/19/anthropic-ipo-ant-live-updates.html))

**Microsoft Ignite**: Azure HorizonDB (PostgreSQL-compatible met ingebouwde vector-indexering) is GA. Agent 365 en Microsoft Entra Agent ID bieden enterprise governance voor het ontdekken en auditeren van AI-agents. Dit is Microsofts antwoord op de wildgroei van autonome agents in bedrijfsomgevingen. ([DEV Community digest](https://dev.to/hiroki-ii-ai/ai-daily-digest-november-18-2026-microsoft-builds-the-agent-cloud-openai-agents-enter-the-2eia))

**OpenAI in de zorg**: Computer-use agents zijn via de API en ChatGPT for Healthcare beschikbaar voor zorginstellingen. Eerste stap naar gereguleerd AI-gebruik in een hoog-risicosector.

**Benelux AI-adoptie**: België heeft ~34,5% van bedrijven met 10+ medewerkers AI geadopteerd (EU gemiddelde: 20%). Nederland zit op ~33%. Uit een Xebia/Data Expo-rapport blijkt dat 74% van Benelux-organisaties actief generatieve AI gebruikt, maar slechts 24% de businesswaarde effectief meet — en 69% maakt zich zorgen over Shadow AI. ([Xebia](https://xebia.com/news/xebia-data-expo-benelux-ai-readiness-report-2026/))

---

## 💡 Ctac-relevantie

**Anthropic IPO is strategisch nieuws voor Ctac.** Claude-modellen vormen de basis van meerdere Ctac-initiatieven. Een beursgenoteerd Anthropic met $1,76 biljoen marktwaarde is een stabieler maar ook commerciëler partnership-perspectief. Volg de product- en prijsstrategie na beursintroductie nauwgezet.

**Microsoft Ignite-announcements raken Ctac direct.** Azure HorizonDB (vector-native) verlaagt de drempel voor RAG-architecturen bij klanten. Microsoft Entra Agent ID is interessant voor Ctac-klanten die agent-governance willen inrichten — dit sluit aan op de 69% Shadow AI-zorg in de Benelux. Dit kan een concrete propositielijn zijn: "Wij helpen u uw AI-agents inventariseren en beheersen."

**MCP-kwetsbaarheden zijn een actie-item voor het Ctac AI-team.** Als Ctac MCP-servers gebruikt of bouwt voor klantintegraties (tools, databronnen, workflows), moeten de november-advisories worden gecontroleerd. Het AWS API MCP Server-lek is concreet genoeg om nu te checken.

**De EU AI Act Omnibus-uitbreiding geeft klanten lucht, maar geen vrijheid.** De deadline-verlenging voor hoog-risico toepassingen (naar december 2027) geeft klanten in overheid, zorg en finance meer implementatietijd. Gebruik dit als opening in gesprekken: "U heeft meer tijd, maar begint u nu dan kunt u de compliance as-a-service bij Ctac beleggen."

**Benelux markt is rijp.** Met ~34% AI-adoptie in België en ~33% in NL, en slechts 24% die businesswaarde meet, ligt er een duidelijke kans voor Ctac in AI-ROI-consultancy en governance-diensten.

---

## 📚 Bronnen & verder lezen

- [Anthropic IPO – CNBC live updates](https://www.cnbc.com/2026/11/19/anthropic-ipo-ant-live-updates.html)
- [Anthropic valued at $1.76 trillion – CNN](https://cnn.com/2026/11/19/business/live-news/anthropic-ipo)
- [Microsoft Ignite AI Digest – DEV Community](https://dev.to/hiroki-ii-ai/ai-daily-digest-november-18-2026-microsoft-builds-the-agent-cloud-openai-agents-enter-the-2eia)
- [Microsoft lanceert 7 AI-modellen – eWeek](https://www.eweek.com/news/microsoft-seven-ai-models-openai-anthropic/)
- [The Neuron – AI Today 19 november](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-thursday-november-19-2026/)
- [EU AI Act – Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [AI Omnibus hoog-risico uitstel – DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [AI regulation november 2026 – Cubbbix](https://cubbbix.com/blog/ai-regulation-november-2026-global-update)
- [AI Cybersecurity Update 20 nov – BTI Group](https://www.btigroup.com/post/ai-cybersecurity-update-november-20-2026/)
- [AI Model Vulnerability Tracker 2026 – axis-intelligence](https://axis-intelligence.com/research/ai-model-vulnerability-tracker/)
- [Record CVE's in 2026 – SC World](https://www.scworld.com/brief/artificial-intelligence-drives-record-surge-in-software-vulnerabilities)
- [Xebia Benelux AI Readiness Report 2026](https://xebia.com/news/xebia-data-expo-benelux-ai-readiness-report-2026/)
- [PwC AI Business Predictions 2026 – België](https://www.pwc.be/en/news-publications/2026/ai-business-predictions-2026.html)
- [AI Model Release Tracker november – nocode.mba](https://www.nocode.mba/ai-release-tracker/2026/11)
- [LLM Release Timeline – llmgateway](https://llmgateway.io/timeline)
