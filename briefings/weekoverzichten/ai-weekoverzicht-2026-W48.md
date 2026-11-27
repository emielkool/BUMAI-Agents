---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W48
Datum: 2026-11-27
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 48, 2026

> Synthese van AI-ontwikkelingen van maandag 23 november t/m vrijdag 27 november 2026.
> *Noot: er zijn geen losse dagbriefings gegenereerd voor deze week. Dit weekoverzicht is samengesteld op basis van directe web searches over de betreffende periode.*

## 🏆 Weekhighlights

1. **Anthropic gaat officieel naar de beurs.** Na de confidentiële S-1 filing in oktober en een herwaardering richting $81,3 miljard begon Anthropic deze week te handelen op de Nasdaq onder ticker "ANT". Het is de eerste frontier AI-lab dat een beursnotering haalt. Wat dit betekent: Claude wordt een volwassen enterprise-product en Anthropic heeft kapitaal voor de volgende generatie modellen.

2. **Google stelt MCP-regels voor AI-agents in Workspace.** Vanaf 1 februari 2027 mogen AI-agents alleen nog officiële Google MCP-servers gebruiken voor toegang tot Gmail, Drive en Calendar. Ontwikkelaars die nu onofficiële API-koppelungen bouwen, moeten vóór die datum migreren. Dit is structureel: Google kanaliseert de hele agent-stack door zijn eigen authenticatie- en autorisatielaag.

3. **EU AI Act deadline 2 december nadert snel.** Over vijf dagen moeten aanbieders van generatieve AI die vóór 2 augustus 2026 actief waren op de EU-markt hun outputs machine-leesbaar markeren. Tegelijk gaan twee nieuwe Art. 5-verboden in op die datum: AI-gegenereerde non-consensuele intieme beelden en CSAM. De boetes zijn reëel (€15 miljoen of 3% omzet).

4. **AI-agent security: van theorie naar praktijk.** De Zwitserse NCSC rapporteerde deze week de eerste bevestigde aanvallen op Zwitserse organisaties waarbij een AI-agent als aanvalsmiddel werd ingezet. Tegelijkertijd blijkt uit een BlackFog-survey dat 56% van IT security-leiders zegt dat autonome AI-agents buiten de bestaande security controls opereren. De kloof tussen agent-deployments en governance is acuut.

5. **Microsoft lanceert eigen AI-modellen als kostenalternatief.** Op Ignite (17 november) introduceerde Microsoft zeven MAI-modellen, waaronder MAI Code 2 dat op 96% van de codeer-benchmarks van Claude Opus 5.5 uitkomt tegen 5% van de prijs (eigen vergelijking). Dagelijkse Copilot-gebruikers groeiden met 50% kwartaal-op-kwartaal, maar penetratie blijft laag: slechts 4% van de 450 miljoen M365-licenties heeft de Copilot-add-on.

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De rode draad van week 48 is **infrastructuur voor agents**. Google's MCP-verplichting, SpaceX's FCC-goedkeuring voor tot één miljoen AI computing-satellieten, en Microsoft's eigen modellijn zijn stuk voor stuk bewegingen die de laag ónder de taalmodellen vastleggen. De race is niet meer wie het beste foundation model heeft, maar wie de agent-infrastructuur controleert en hoe goedkoop die infrastructuur draait.

Modelnieuws was beperkt: GPT-6 werd ingezet voor eiwit-design, Midjourney lanceerde Niji V8 voor anime-stijl beelden, en de Gemini app voegde meer dan 60 nieuwe stemmen met regionale accenten toe. Geen grote modelreleases in de betreffende week — de nadruk lag op deployment en governance.

### 🏛️ Governance & Beleid

De **2 december 2026-deadline** is het concrete beleidsmoment van week 48. Twee verplichtingen gaan gelijktijdig in: de markerings­plicht voor bestaande generatieve AI-systemen, en de nieuwe verbods­artikelen (Art. 5) voor NCII en CSAM. Organisaties die nog geen machine-leesbare markering hebben geïmplementeerd staan direct bloot aan handhaving.

Op nationaal niveau viel de maatregel van New York op: een vijfjarig verbod op AI chatbot-speelgoed voor kinderen, met dagelijkse boetes van $15.000. Dit volgt een trend waarbij deelstaten sneller bewegen dan federale wetgevers. In Europa is de volgende grote datum pas december 2027 (high-risk AI-systemen), maar de druk op compliance-teams neemt nu al toe.

### 🔐 Security & Risk

Agent security is geen toekomstig risico meer. Drie bevestigde patronen in week 48:

- **AI-agents als aanvalsmiddel:** de Zwitserse NCSC bevestigde actieve gebruik door aanvallers, met een 24-uurs patching-verplichting als reactie op internet-facing systemen.
- **Stale vendor keys:** lekke toegangs­sleutels van AI-aanbieders (Fireworks AI bij Cursor-incident) gaven aanvallers laterale bewegingsruimte.
- **Governance gap:** de BlackFog-meting (56% agents buiten security controls) is een alarmsignaal voor iedere organisatie die pilot-agents heeft draaien zonder formeel beheer.

De NCSC UK bevestigde in een assessment dat AI de snelheid van bestaande aanvalstechnieken verhoogt; de menselijke operator blijft vooralsnog relevant. Dat kan snel veranderen.

### 📈 Markt & Adoptie

**Anthropic overtreft OpenAI in enterprise LLM-marktaandeel** (Menlo Ventures/Ramp-data: Anthropic 43,8% vs OpenAI 40,6% van de API-spending in september 2026). Dit is een omslagpunt: een jaar geleden was het verschil andersom. De beursgang versterkt die positie — institutioneel kapitaal en governance-eisen dwingen nu ook grotere klanten richting Claude.

Microsoft Copilot groeit snel in gebruik maar blijft dun in penetratie. Dat laat een opening voor alternatieven. Canada breidt zijn AI compute-fonds uit naar C$1 miljard, deels als reactie op de VS-chiprestrities die Chinese AI-ontwikkeling raken. Voor de Benelux relevant: Nederland en België behoren tot de Europese koplopers in AI-adoptie, maar de overgang van pilots naar volledige integratie — en zeker naar agentic AI — is slechts voor een kleine minderheid van bedrijven bereikt.

## 💼 Ctac-weekperspectief

- **Anthropic-beursgang = commerciële volwassenheid, handelbaar voor klanten.** Het IPO maakt Claude minder afhankelijk van durfkapitaal en geeft enterprise-klanten meer vertrouwen in de continuïteit van de dienst. Ctac kan dit benutten als argument om Claude-gebaseerde proposities te verankeren in meerjarige klanttrajecten — inclusief SLA-afspraken die eerder gevoelig lagen.

- **Google MCP-deadline (1 feb 2027) = nu bouwen of straks herstellen.** Klanten met Workspace die AI-agents willen, moeten nu starten met de officiële Google MCP-servers. Als Ctac klanten heeft met Workspace-integraties in de pijplijn, is dit het moment om de architectuur goed neer te zetten — migreren in januari 2027 onder tijdsdruk is vermijdbaar.

- **EU AI Act 2 december: doe een snelle check voor generatieve tools bij klanten.** Klanten die Ctac-gebouwde of -geadviseerde generatieve AI-tools inzetten vóór augustus 2026 moeten output-markering actief hebben. Een korte compliance-scan vóór 2 december is een directe dienstverleningskans en vermijdt reputatierisico.

- **Agent security governance als nieuw propositie-onderdeel.** De combinatie van de Zwitserse NCSC-rapportage en de BlackFog-survey maakt een sterk verhaal: 56% van bedrijven heeft geen governance op hun agents. Ctac kan een "AI Agent Security Scan" aanbieden als laagdrempelige instap — inventariseer welke agents draaien, met welke rechten, buiten welke controls.

## 📚 Bronnenlijst

**Technologie & Modellen**
- [The Neuron – AI Today November 26, 2026](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-26-2026/)
- [The Neuron – AI Today November 27, 2026](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-27-2026/)
- [LLM Gateway – November 2026 Model Releases](https://llmgateway.io/timeline/2026)
- [TecAdmin – November 2026 AI Model Releases](https://tecadmin.net/november-2026-ai-model-releases/)
- [Google Workspace MCP servers documentation](https://developers.google.com/workspace/guides/configure-mcp-servers)
- [Microsoft – Seven MAI Models (eWeek)](https://www.eweek.com/news/microsoft-seven-ai-models-openai-anthropic/)
- [Microsoft Copilot adoption (PYMNTS)](https://www.pymnts.com/earnings/2026/microsoft-sees-enterprise-ai-adoption-accelerate-as-copilot-usage-grows/)

**Governance & Beleid**
- [EU AI Act – Europese Commissie officieel](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU AI Act Timeline 2026 (Alice Labs)](https://alicelabs.ai/en/insights/eu-ai-act-timeline-2026)
- [EU AI Act Compliance Guide (Orbiq)](https://www.orbiqhq.com/eu-regulations/eu-ai-act-compliance)
- [Digital Omnibus – FPF Timeline](https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus)
- [AI Regulation Weekly Report – 23 november 2026](https://www.originbrief.app/en/reports/ai-regulation-policy/2026-11-23/weekly)
- [EU AI Act December Deadline (Holistic AI)](https://www.holisticai.com/blog/eu-ai-acts-deadline-moved-2027)

**Security & Risk**
- [AI Agent Security November 2026 (Adversa AI)](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/)
- [Enterprise AI Security Risks Surge (InfotechLead)](https://infotechlead.com/security/enterprise-ai-security-risks-surge-ai-enabled-breaches-cost-6-million-as-companies-struggle-to-protect-data-and-agents-99624)
- [Cloud Security Alliance – Frontier Ready Daily 26 Nov](https://labs.cloudsecurityalliance.org/research/frontier-ready-daily-20261126/)
- [AI Security News November 2026 (Software Strategies Blog)](https://softwarestrategiesblog.com/ai-security-news/)
- [OpenAI Rogue Agents – Blaming Computer (BleepingComputer)](https://bleepingcomputer.com/news/security/openai-details-more-cases-of-ai-agents-taking-unauthorized-actions)

**Markt & Adoptie**
- [Enterprise LLM Market Share 2026 (Blocksize)](https://ai.blocksize.hr/blog/en/enterprise-llm-market-share-business-adoption-2026)
- [2026: State of Enterprise AI (Menlo Ventures)](https://menlovc.com/perspective/2026-the-state-of-enterprise-ai/)
- [Anthropic IPO (TechCrunch)](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/)
- [AI Adoptie Benelux (Customer Impact)](https://www.customerimpact.be/kennis/ai-zoekadoptie-benelux-cijfers/)
- [België bij Europese koplopers AI-adoptie (ITdaily)](https://itdaily.com/news/software/belgium-european-leaders-ai-adoption/)
- [Nederland aan kop Europese AI-adoptie (Consultancy.nl)](https://www.consultancy.nl/nieuws/59956/onderzoek-nederland-aan-kop-in-de-europese-ai-adoptie)
