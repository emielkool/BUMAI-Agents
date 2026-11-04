---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-04
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 4 november 2026

## 🔑 Highlights van de dag

- **November = modellenmaand:** GPT-6 Rosalind Research (OpenAI, beperkte toegang), Gemini 4 Argon GA (Google, 1M-token output + Computer Use) en Claude Haiku 5.5 (Anthropic, effort controls + 1M context) verschenen eind oktober/vroeg november — de modellen stapelen zich op.
- **EU AI Act enforcement gestart:** Handhaving loopt sinds 2 augustus 2026; nog geen boetes uitgedeeld, maar de consult­atie over boeteprocedures sluit op 9 november. Hoog-risico-verplichtingen zijn door het Digital Omnibus-pakket uitgesteld naar december 2027.
- **Microsoft Azure +48%, Google Cloud +103%:** AI-diensten drijven de cloud-groei fors op, maar Forrester twijfelt of dit echte brede enterprise-adoptie is of geconcentreerde big-spender-budgetten.
- **Copilot RCE-kwetsbaarheid (CVE-2026-103572):** Remote code execution flaw in Visual Studio/SSMS via AI coding-agent; direct patchen prioriteit voor dev-teams.
- **Agentic AI experimenteert breed, schaalt nauwelijks:** McKinsey (april 2026) stelt dat 62% van organisaties experimenteert met AI-agents, maar minder dan 10% draait ze op schaal — de implementation gap is de kans voor consultants.

---

## 🧠 Technologie & Modellen

November belooft een van de drukste modellenmaanden van het jaar te worden. OpenAI bracht **GPT-6 Rosalind Research** (30 oktober) uit, maar uitsluitend voor goedgekeurde onderzoeksklanten via Work, Codex en de API. GPT-6.1 Terra is inmiddels breder beschikbaar via Codex en staat in de catalogi van Vertex AI en Amazon Bedrock. Google's **Gemini 4 Argon** is naar general availability gegaan met Computer Use-ondersteuning en een 1 miljoen-token output-limiet — een aanzienlijke stap voor lange-context enterprise-toepassingen. Anthropic's **Claude Haiku 5.5** is de eerste Haiku-variant met effort controls en een 1M-context window, op twee prijsniveaus.

Voorbehoud: de komende weken circuleren ook geruchten over GPT-6.2, Claude Fable 5.5/Opus 5.6 en DeepSeek V4.1 Pro. Die release-windows zijn speculatief en niet bevestigd door de labs zelf.

**Agentic infrastructuur:** MCP is het dominante protocol voor tool-connectie geworden (aandeel in agentic integraties: ~75%). Frameworks als LangGraph, CrewAI, AutoGen en Semantic Kernel convergeren naar vergelijkbare abstracties. Observability wordt volwassener — Langfuse werd begin 2026 overgenomen door ClickHouse. Governance en kostenbeheersing (agent budgets, spend caps) zijn mainstream geworden als infra-concern, niet meer als bijzaak.

Bronnen: [LLM-stats AI news](https://llm-stats.com/ai-news) | [Opper model tracker](https://opper.ai/model-releases) | [Agentic AI landscape 2026](https://medium.com/@nsr16/agentic-ai-in-2026-661f5b099c2f) | [StackOne agent tools](https://www.stackone.com/blog/ai-agent-tools-landscape-2026/)

---

## 🏛️ Governance & Ethiek

**EU AI Act – Digital Omnibus:** De hoog-risico-verplichtingen (Annex III-use cases) zijn door Verordening (EU) 2026/1744 uitgesteld naar **2 december 2027**; voor AI in gereguleerde producten (bijv. medische hulpmiddelen) geldt 2 augustus 2028. De verboden, AI-geletterdheidsplicht en GPAI-verplichtingen zijn al van kracht. Op **2 december 2026** gaat een nieuwe verbodsbepaling in voor AI die niet-consensuele intieme beelden of CSAM genereert, én de watermarkingplicht voor generatieve AI-systemen die vóór 2 augustus op de markt waren. De Commission-consultatie over boeteprocedures sluit 9 november — direct relevant voor bedrijven die weten dat ze in scope zijn.

**Nederland:** Het kabinet wees een algeheel verbod op niet-Europese AI bij de overheid af, maar wil Europese en open modellen stimuleren via inkoopbeleid. Een AI-veiligheidsinstituut wordt onderzocht. Eind 2026 volgt een overkoepelende kabinetsvisie op AI. Op **12 november** vindt het AI & Overheid congres plaats in Utrecht (LEF Future Center): focus op AI als strategische motor, niet als losse pilots.

Bronnen: [DLA Piper Digital Omnibus update](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) | [EU AI Act tijdlijn 2026](https://theagentindex.io/guides/eu-ai-act-timeline/) | [iBestuur – kabinet niet-Europese AI](https://ibestuur.nl/overheid-in-transitie/politiek-en-beleid/kabinet-niet-europese-ai-weren-bij-overheid-gaat-te-ver) | [AI & Overheid 2026](https://ibestuur.nl/events/ai-en-overheid-2026)

---

## 🔐 Security & Risk

**Copilot RCE (CVE-2026-103572):** Adversa AI documenteerde een remote code execution-kwetsbaarheid in Microsoft GitHub Copilot via Visual Studio en SSMS. Prioriteer patching in dev-omgevingen. Eveneens gemeld: een Claude Code-child-session-issue waarbij hook-bevestiging werd omzeild.

**UK NCSC-waarschuwing:** Het Britse National Cyber Security Centre stelt dat AI-gestuurd ransomware "highly likely" is bij aanvallen op kritieke infrastructuur vóór 2028. Het NCSC identificeerde honderden potentiële beveiligingsproblemen in AI-systemen.

**Agentic bedreigingen:** Prompt injection, memory poisoning en supply chain-aanvallen op agent-frameworks zijn de meest genoemde risico's. Betrouwbare, gekwantificeerde statistieken ontbreken nog — vendor-claims van 43 kwetsbare framework-componenten of 520 incidenten zijn niet onafhankelijk geverifieerd.

Bronnen: [Adversa AI coding agent vulnerabilities](https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/) | [The Register NCSC ransomware](https://www.theregister.com/security/2026/11/03/britain-on-notice-ai-powered-ransomware-attacks-to-arrive-by-2028/5307200) | [Stellar Cyber agentic threats](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/)

---

## 📈 Markt & Adoptie

De Q3-resultaten (28 oktober) van Microsoft en Google laten krachtige AI-gedreven cloud-groei zien: **Azure +48%**, **Google Cloud +103%** (kwartaal-op-kwartaal ten opzichte van vorig jaar). Forrester-analist Tracy Woo plaatst een vraagteken: is dit brede enterprise-adoptie, of drijven een beperkt aantal hyperscalers en AI-native bedrijven het beeld?

**Google:** Bij Google Cloud Next 2026 kondigde Google een investering van $750 miljoen aan voor partners die AI-tools uitrollen. Het Gemini Enterprise Agent Platform was het middelpunt.

**Microsoft:** De M365 E7-bundle (M365 E5 + Copilot + Entra Suite + Agent 365) is per 1 mei 2026 live. Meer dan 20 miljoen betaalde Copilot-seats; 70% van de Fortune 500 heeft het uitgerold. Bristol Myers Squibb rapporteert 96% adoptie onder 30.000 medewerkers.

**Schaal vs. experiment:** McKinsey stelt dat 62% van organisaties AI-agents uitprobeert, maar minder dan 10% draait ze in productie. De productie-gap is reëel.

Bronnen: [CIO Dive Microsoft Google AI revenue](https://www.ciodive.com/news/Microsoft-Google-booming-AI/873258/) | [Infotechlead Copilot vs Gemini 2026](https://infotechlead.com/artificial-intelligence/microsoft-365-copilot-vs-google-gemini-enterprise-2026-adoption-productivity-gains-and-real-world-ai-deployments-98980?amp=1) | [Google Cloud Next 2026](https://blog.thecgaigroup.com/google-cloud-next-2026-enterprise-ai-inflection-point)

---

## 💡 Ctac-relevantie

**EU AI Act deadlines voor klanten:** De hoog-risico-deadline van 2 december 2027 klinkt ver weg, maar de benodigde inventarisaties, risicobeoordelingen en technische documentatie kosten tijd. Klanten in overheid, zorg en finance (Annex III) doen er verstandig aan nu te starten. Ctac kan hier een concrete readiness-scan aanbieden.

**Microsoft M365 E7 bundle:** De bundeling maakt Copilot voor veel enterprise-klanten onderdeel van de standaardomgeving. Dat verlaagt de drempel voor adoptie, maar vergroot tegelijk de behoefte aan implementatie-ondersteuning, change management en governance. Zeker relevant voor Ctac's bestaande Microsoft-klantenbasis.

**Agentic AI — de implementation gap is de propositionele opening:** 62% experimenteert, maar <10% schaalt. Organisaties die de overstap willen maken van pilot naar productie hebben een partner nodig die governance, observability en kostenbeheersing meeneemt in het ontwerp. Dat is precies waar Ctac als IT-consultancy waarde kan toevoegen — niet met het bouwen van modellen, maar met het bouwen van betrouwbare agent-systemen op bestaande infra (Azure, MCP, Semantic Kernel).

**Security:** De Copilot RCE-kwetsbaarheid raakt direct dev-teams die GitHub Copilot in Visual Studio gebruiken. Zorg dat intern gepatcht wordt en communiceer dit proactief naar klanten met soortgelijke tooling.

---

## 📚 Bronnen & verder lezen

- [LLM-stats – AI nieuws november 2026](https://llm-stats.com/ai-news)
- [Opper AI model tracker](https://opper.ai/model-releases)
- [DLA Piper Digital Omnibus – EU AI Act update](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)
- [EU AI Act tijdlijn na Digital Omnibus](https://theagentindex.io/guides/eu-ai-act-timeline/)
- [iBestuur – kabinet over niet-Europese AI](https://ibestuur.nl/overheid-in-transitie/politiek-en-beleid/kabinet-niet-europese-ai-weren-bij-overheid-gaat-te-ver)
- [AI & Overheid 2026 – congres 12 november](https://ibestuur.nl/events/ai-en-overheid-2026)
- [Adversa AI – Copilot RCE kwetsbaarheid](https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/)
- [The Register – NCSC ransomware waarschuwing](https://www.theregister.com/security/2026/11/03/britain-on-notice-ai-powered-ransomware-attacks-to-arrive-by-2028/5307200)
- [CIO Dive – Microsoft & Google AI revenue](https://www.ciodive.com/news/Microsoft-Google-booming-AI/873258/)
- [Google Cloud Next 2026](https://blog.thecgaigroup.com/google-cloud-next-2026-enterprise-ai-inflection-point)
- [StackOne – agentic AI tools 2026](https://www.stackone.com/blog/ai-agent-tools-landscape-2026/)
- [McKinsey via Medium – agentic AI 2026](https://medium.com/@nsr16/agentic-ai-in-2026-661f5b099c2f)
