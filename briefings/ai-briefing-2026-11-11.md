---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-11
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 11 november 2026

## 🔑 Highlights van de dag

- **Anthropic lanceert Claude Fable 5.2 en Mythos 5.2** (9 november): Fable 5.2 is 20% goedkoper dan zijn voorganger ($8/$40 per 1M tokens) en ondersteunt 1M-token contextvensters; Mythos 5.2 is een restricted-access variant voor geverifieerde organisaties in cybersecurity en life sciences.
- **ChatGPT Enterprise via AWS Marketplace** (9 november): enterprises kunnen hun bestaande AWS-cloudcommitments nu inzetten voor OpenAI-diensten – een directe drempelverlagende move voor enterprise adoptie.
- **EU AI Act handhaving loopt**: de eerste geharmoniseerde norm (EN 18286:2026) is gepubliceerd en er is een nieuwe AI-toolbox voor overheden gelanceerd (5 november). Organisaties met AI-systemen vóór augustus 2026 hebben tot 2 december voor overgangsverplichtingen.
- **Gartner: open modellen doen 90% van agentic werk voor 1/20 van de kosten** van frontier LLMs – een uitspraak die de business case voor open-source AI in enterprise-omgevingen fundamenteel verandert.
- **NVIDIA-CEO Jensen Huang onder onafhankelijk bestuurlijk onderzoek** na berichten over een gerichte Chinese inlichtingenoperatie; Huang blijft CEO maar de markt volgt dit nauwgezet.

---

## 🧠 Technologie & Modellen

**Anthropic Claude Fable 5.2 / Mythos 5.2** – Uitgebracht op 9 november. Fable 5.2 biedt 1M-token contextvensters en is gericht op veeleisend redeneerwerk en langlopende agent-taken. De prijsverlaging van 20% t.o.v. Fable 5.1 is strategisch: Anthropic versnelt enterprise-adoptie terwijl de concurrentie met OpenAI aanscherpt. Mythos 5.2 (zelfde model, lossere bio/cyber-safeguards) is alleen toegankelijk voor geverifieerde organisaties en roept terecht vragen op over tweeërlei gebruik.
([ETV Bharat](https://www.etvbharat.com/en/technology/major-ai-upgrades-meta-muse-openai-dot-multi-device-support-google-maps-platform-in-ai-studio-and-claude-fable-mythos-enn26111002884) | [Releasebot](https://releasebot.io/updates/anthropic))

**OpenAI GPT-6 Cyber & Rosalind / GPT Image 2.6** – OpenAI heeft meerdere modelupdates doorgevoerd: GPT Image 2.6 Flare en Sunburst (4 november, inclusief animated GIF-generatie) en GPT-6 Cyber en Rosalind. Details zijn schaars; verificatie via OpenAI's eigen blog is aangeraden.

**Google Gemini Omni 1.2 Flash GA + Robotics** – Gemini Omni 1.2 Flash is op 5 november algemeen beschikbaar gekomen op Google Cloud, met video output tot 15 seconden. Google lanceerde ook Gemini Robotics 2.5 en nieuwe TPUs (Cloud Pathways). NVIDIA presenteerde GR00T 2 op een roboticaconferentie.

**Gartner over open modellen** – Volgens Gartner kunnen open-weight modellen 90% van agentic werk uitvoeren voor een twintigste van de kosten van frontier LLMs. Kanttekening: open modellen zijn soms uitgebreider en doen vaker een herpoging, wat de TCO-berekening complexer maakt.
([The Register](https://www.theregister.com/ai-and-ml/2026/11/03/open-models-can-do-90-percent-of-agentic-work-at-a-twentieth-of-the-cost-of-a-frontier-llm-gartner/5307132))

---

## 🏛️ Governance & Ethiek

**EU AI Act – handhaving gestart, eerste norm gepubliceerd** – Per 2 augustus 2026 zijn de AI Office en nationale bevoegde autoriteiten handhavingsbevoegd. De Digital Omnibus (27 juli 2026) creëert ruimte voor overgangstermijnen. Op 14 oktober is de eerste geharmoniseerde norm EN 18286:2026 (kwaliteitsmanagement) gepubliceerd in het EU Publicatieblad. Op 5 november volgde een AI-toolbox voor overheden ter ondersteuning van de Apply AI Strategy.
([EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | [Lexia](https://www.lexia.it/en/2026/11/09/data-technology-insight-november/))

**Australië kondigt AI-toezichthouder aan** – Premier Albanese reageert op een OpenAI-datalek bij een Australisch overheidssysteem (juni 2026) met de aankondiging van een nationale AI-safety regulator. Frontier AI-aanbieders die in Australië willen opereren, moeten straks aan wetgevende normen voldoen.
([Hipther](https://hipther.com/news/2026/11/10/161670/ai-dispatch-daily-trends-and-innovations-november-10-2026-u-s-data-centers-australia-s-ai-regulator-))

---

## 🔐 Security & Risk

**52 prompt injection CVEs in 2026** – Per 6 november telt de NVD 52 CVEs in LLM- en agent-software waarbij prompt injection oorzaak of gevolg is. OWASP heeft het voor het tweede jaar op rij als de #1 LLM-kwetsbaarheid gerangschikt. Zorgelijk: aanvallers hebben met tien pogingen nog steeds ~50% kans op succes, en indirect prompt injection-risico neemt toe naarmate modellen krachtiger (en gehoorzamer) worden.
([DEV Community](https://dev.to/koeseo/52-prompt-injection-cves-in-2026-so-far-what-the-numbers-say-3apj) | [Vectra AI](https://www.vectra.ai/topics/prompt-injection))

**CVE-2026-24307: "Reprompt" aanval op Microsoft Copilot** – Vectra beschrijft een aanval die single-click data-exfiltratie bij Microsoft Copilot Personal mogelijk maakt. De Cursor IDE kende eerder een triple-CVE chain. Dit onderstreept dat enterprise AI-tools nog steeds kwetsbare aanvalsvectoren zijn voor supply-chain en social engineering aanvallen.

**NVIDIA-CEO onder onderzoek** – Het NVIDIA-bestuur heeft een onafhankelijk onderzoek geopend nadat bleek dat CEO Jensen Huang doelwit was van een Chinese inlichtingenoperatie. Het bedrijf stelt dat er geen bewijs is van compromittering; Huang blijft aan. De casus toont hoe AI-infrastructuurspelers strategisch doelwit zijn geworden.
([Rio Rundown](https://riorundown.substack.com/p/ai-news-nov-10-2026-ai-security-and))

---

## 📈 Markt & Adoptie

**Microsoft 365 Copilot passeert 30 miljoen betaalde seats** – En het groeit: het aantal klanten op consumptiegebaseerde billing steeg >75% per kwartaal (bron: Citi-analyse op basis van Microsoft's FY2026 proxy). Dragon Copilot is in gebruik bij meer dan 100.000 zorgverleners in de VS.

**ChatGPT Enterprise op AWS Marketplace** – Vanaf 9 november kunnen enterprises OpenAI's diensten afrekenen via bestaande AWS cloudcommitments. Dit verlaagt de drempel aanzienlijk en versterkt de hybride cloud/AI-strategie van Amazon.
([404K Research](https://404kresearch.substack.com/p/456x-morning-brief-november-10-2026))

**SAP Autonomous Enterprise + 1.000 AI agents** – SAP presenteerde op TechEd 2026 zijn SAP Business AI Platform met brede partnerallianties (Anthropic, AWS, Google Cloud, Microsoft). Een Economist/SAP-onderzoek toont dat 66% van CFOs zegt dat AI-adoptie sneller gaat dan de workforce-transformatie – een governancekloof die risico's oplevert.
([SAP News](https://news.sap.com/2026/11/new-economist-enterprise-research-ai-moving-faster-than-organizations-can-adapt/) | [Futurum](https://futurumgroup.com/insights/sap-bets-the-enterprise-on-autonomous-ai-but-can-it-deliver/))

**AI en arbeidsmarkt** – Een Fortune-studie meldt dat bijna 20% van Amerikanen die door AI hun baan verloren later alsnog werd heraaangenomen, vaak voor nieuwe AI-gerelateerde taken. In zorg passen cardiologen 50,6% van AI-gegenereerde rapportages wezenlijk aan – wat nuance geeft aan de hype over volledige autonomie.

---

## 💡 Ctac-relevantie

**Claude Fable 5.2 als nieuwe standaard voor Ctac-projecten.** De prijsverlaging (20%) en het 1M-token contextvenster maken dit de sterkste kandidaat voor complexe kennisintensieve toepassingen – denk aan documentanalyse, langetermijn agentic workflows en code-intensieve projecten. De Mythos-variant (restricted access) is relevant om te begrijpen welke mogelijkheden geverifieerde security- of life-science klanten binnenkort kunnen inzetten.

**ChatGPT Enterprise via AWS Marketplace verlaagt drempel voor Ctac-klanten.** Klanten met bestaande AWS Enterprise Agreements kunnen nu AI-capaciteit activeren zonder nieuw inkoopproces – dit is een argument dat Ctac kan inzetten in gesprekken met klanten die aarzelen vanwege procurement-complexiteit.

**Gartner's open model-stelling vraagt om een standpunt.** Als 90% van agentic werk voor 1/20 van de kosten kan met open-weight modellen, waarom kiezen klanten dan voor frontier LLMs? Ctac heeft hier een advieskans: help klanten de juiste modelkeuze maken op basis van use case, compliance en TCO – in plaats van standaard te adviseren op de duurste frontier-optie.

**EU AI Act EN 18286:2026 norm is nu actief.** Voor klanten in gereguleerde sectoren (overheid, zorg, finance) is een kwaliteitsmanagementsysteem conform deze norm binnenkort een minimumvereiste. Ctac's AI-unit kan zich hier positioneren met assessment- en implementatiediensten.

**Prompt injection als structureel risico in Copilot-implementaties.** Met 52 CVEs dit jaar en een bewezen Copilot-aanvalsvector (CVE-2026-24307), is dit het moment om bij klanten die Microsoft Copilot uitrollen expliciet beveiligings- en governance-review op de agenda te zetten.

---

## 📚 Bronnen & verder lezen

- [ETV Bharat – Claude Fable & Mythos, Meta Muse, Google maps AI](https://www.etvbharat.com/en/technology/major-ai-upgrades-meta-muse-openai-dot-multi-device-support-google-maps-platform-in-ai-studio-and-claude-fable-mythos-enn26111002884)
- [Releasebot – Anthropic Release Notes november 2026](https://releasebot.io/updates/anthropic)
- [LLM Stats – AI nieuws november 2026](https://llm-stats.com/ai-news)
- [The Register – Gartner: open modellen voor agentic werk](https://www.theregister.com/ai-and-ml/2026/11/03/open-models-can-do-90-percent-of-agentic-work-at-a-twentieth-of-the-cost-of-a-frontier-llm-gartner/5307132)
- [EC Digital Strategy – EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Lexia – Data & Technology Insight november 2026](https://www.lexia.it/en/2026/11/09/data-technology-insight-november/)
- [Hipther – AI Dispatch 10 november 2026](https://hipther.com/news/2026/11/10/161670/ai-dispatch-daily-trends-and-innovations-november-10-2026-u-s-data-centers-australia-s-ai-regulator-)
- [DEV Community – 52 prompt injection CVEs in 2026](https://dev.to/koeseo/52-prompt-injection-cves-in-2026-so-far-what-the-numbers-say-3apj)
- [Vectra AI – Prompt injection types, CVEs en enterprise defenses](https://www.vectra.ai/topics/prompt-injection)
- [Rio Rundown – AI News Nov 10, 2026 (security & cloud)](https://riorundown.substack.com/p/ai-news-nov-10-2026-ai-security-and)
- [404K Research – Morning Brief 10 november: ChatGPT Enterprise op AWS](https://404kresearch.substack.com/p/456x-morning-brief-november-10-2026)
- [SAP News – Economist Enterprise onderzoek AI-adoptie](https://news.sap.com/2026/11/new-economist-enterprise-research-ai-moving-faster-than-organizations-can-adapt/)
- [Futurum – SAP Autonomous Enterprise strategie](https://futurumgroup.com/insights/sap-bets-the-enterprise-on-autonomous-ai-but-can-it-deliver/)
- [BenchLM – LLM Agent Benchmarks november 2026](https://benchlm.ai/llm-agent-benchmarks)
- [MarketScale – Enterprise AI ROI 2026](https://www.marketscale.com/industries/software-and-technology/enterprise-ai-is-generating-business-insights-but-not-saving-money-and-the-governance-gap-is-widening)
