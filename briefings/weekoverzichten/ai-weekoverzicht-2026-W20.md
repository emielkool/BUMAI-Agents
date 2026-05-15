---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W20
Periode: 2026-05-11 / 2026-05-17
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 20, 2026

> Synthese van de dagbriefings van 11 mei t/m 15 mei 2026.

---

### Maandag 11 mei

→ Dagbriefing: [ai-briefing-2026-05-11.md](../ai-briefing-2026-05-11.md)

**Highlights:**
- **Claude Opus 4.7 GA & Claude Security beta** – Anthropic's nieuwste flagship is breed beschikbaar (API, Bedrock, Vertex AI, Foundry) met betere vision en hogere codeer­kwaliteit; Claude Security voor kwetsbaarheids­scanning is in public beta voor enterprise-klanten.
- **1 miljoen blootgestelde AI-diensten** – Een grootschalige scan onthulde dat AI-infrastructuur slechter is geconfigureerd dan vrijwel iedere andere software-categorie: geen authenticatie, hardcoded credentials, root-draaiende processen.
- **EU AI Act – eindsprint** – 10 sectorale toezichthouders actief in Nederland; volledige toepasselijkheid volgt op 2 augustus 2026, minder dan drie maanden weg.

**Ctac-relevantie van de dag:** AI Security is een direct verkoopbaar aanbod nu de bevindingen over blootgestelde AI-stacks breed zijn gerapporteerd. Combineer dit met de EU Act-deadline voor een concrete dubbele propositie richting klanten die eigen AI-diensten deployen.

---

### Dinsdag 12 mei

→ Dagbriefing: [ai-briefing-2026-05-12.md](../ai-briefing-2026-05-12.md)

**Highlights:**
- **Anthropic Mythos (gelimiteerde release)** – Krachtigste model van Anthropic tot nu toe, bewust beperkt uitgerold vanwege cybersecurity-risico's; signaleert dat frontier-modellen de gevaarlijkheidsdrempel serieus nemen.
- **Microsoft: 17,8% van wereldbevolking gebruikt AI actief** – In 26 landen al boven de 30%; de kloof Noord-Zuid verdubbelt echter nog steeds.
- **Google Cloud eerste kwartaal boven $20 miljard** – Gedreven door AI-workloads (+63% YoY); Microsoft en AWS plannen samen meer dan $500 miljard capex voor AI-infrastructuur in FY2026.

**Ctac-relevantie van de dag:** De agentic coding-cijfers (Mercado Libre: 23.000 engineers, 50.000-regelige migratie in 20 uur) maken de ROI-case voor enterprise pilots onweerlegbaar; Ctac kan dit als referentie inzetten bij klanten met softwareteams van 20+ engineers.

---

### Woensdag 13 mei

*(geen briefing beschikbaar voor deze dag)*

---

### Donderdag 14 mei

→ Dagbriefing: [ai-briefing-2026-05-14.md](../ai-briefing-2026-05-14.md)

**Highlights:**
- **MCP wordt open standaard via Linux Foundation** – Anthropic en OpenAI richtten gezamenlijk de Agentic AI Foundation op; het Model Context Protocol is nu governance-neutraal, wat vendor lock-in op protocol-niveau elimineert.
- **Enterprise AI JVs: OpenAI & Anthropic** – Beide labs lanceerden begin mei joint ventures voor mid-market adoptie; Anthropic met Blackstone/Goldman Sachs, OpenAI's *The Development Company* haalde $4 miljard op.
- **Eerste AI-agent betaling in NL** – Mastercard en Rabobank voerden de eerste betaling via AI-agent uit in Nederland; klein maar concreet signaal voor financiële sector in Benelux.

**Ctac-relevantie van de dag:** MCP-standaardisatie verlaagt het technisch risico bij agentische projecten voor klanten; gebruik dit als argument bij klanten die aarzelen vanwege vendor lock-in. De enterprise JV-structuren wijzen ook op kanaalstrategie: positionering als preferred implementation partner loont nu de markt consolideert.

---

### Vrijdag 15 mei

→ Dagbriefing: [ai-briefing-2026-05-15.md](../ai-briefing-2026-05-15.md)

**Highlights:**
- **Microsoft Agent 365 GA (1 mei)** – Centrale governance-laag voor enterprise-agents op $15/user/maand, met runtime-blokkering via Defender en uitbreiding naar 18 agenttypen (incl. Claude Code) in juni; M365 E7 "Frontier Suite" bundelt dit voor $99/user/maand.
- **EU AI Act 'AI omnibus' politiek akkoord (7 mei)** – Vereenvoudiging van regels plus verbod op nudification-apps; volledige AI Act-toepasselijkheid op 2 augustus 2026 is nog 79 dagen weg.
- **Prompt injection als structureel enterprise-risico** – Drie AI-coderingsagenten lekten secrets via één aanval; Microsoft CVE-2026-21520 gepatcht maar data geëxfiltreerd; OpenAI erkent dat het probleem niet deterministisch op te lossen is.

**Ctac-relevantie van de dag:** Agent governance wordt het concrete verkoopgesprek: klanten die Copilot of Claude Code uitrollen moeten nu nadenken over beheer, beveiliging en audit van agents. Ctac kan hier een advies- en implementatierol pakken — zeker met de EU Act-deadline als stok achter de deur.

---

## 🏆 Weekhighlights

- **Anthropic Mythos: bewuste zelfinperking als veiligheidsparadigma.** Mythos, Anthropic's krachtigste model ooit, werd beperkt uitgerold wegens security-risico's. Tegelijk weigert Anthropic de EU toegang te verlenen – in contrast met OpenAI dat GPT-5.5-Cyber wel opengesteld heeft voor vetted EU-teams. De geopolitieke dimensie van modeltoegang is daarmee permanent onderdeel van het AI-landschap.

- **EU AI Act omnibus: gestructureerde verlichting, maar basislijn blijft.** Het akkoord van 7 mei verschuift de deadline voor standalone high-risk AI naar december 2027 en embedded high-risk AI naar augustus 2028. Maar GPAI-transparantie, NCII-verboden (december 2026) en de basisdatum van 2 augustus 2026 blijven ongewijzigd. Met 79 dagen te gaan is dit geen uitstelkans maar een hertekening van de prioriteiten.

- **MCP wordt governance-neutrale infrastructuurstandaard.** Anthropic doneerde het Model Context Protocol aan de Agentic AI Foundation (Linux Foundation), mede opgericht door OpenAI. Vendor lock-in op protocol-niveau verdwijnt. Dit is de definitieve bevestiging dat agentische interoperabiliteit infrastructuur is geworden – vergelijkbaar met TCP/IP voor het web.

- **Microsoft Agent 365 GA: enterprise agent governance is product geworden.** Vanaf 1 mei live op $15/user/maand, met runtime-blokkering via Defender en bundeling in de M365 E7 "Frontier Suite" ($99/user/maand). Combineer dit met MDASH (multi-agent securitysysteem dat Mythos verslaat op CyberGym) en het Pentagon-contract: Microsoft positioneert zich als de meest complete enterprise AI-leverancier.

- **Prompt injection escaleert naar Remote Code Execution.** Drie AI-coderingsagenten (Claude Code, Gemini CLI, GitHub Copilot) lekten secrets via één gecoördineerde aanval. De eerder onthulde Semantic Kernel CVEs (CVSS 9.9, CVE-2026-25592 en CVE-2026-26030) tonen dat prompt injection naar directe code-uitvoering kan escaleren – zonder geheugenbugs of bijlagen. OpenAI erkent dat dit structureel onoplosbaar is.

---

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De week liet drie parallelle bewegingen zien. **Eén:** de frontier splitst – Mythos beperkt beschikbaar, GPT-5.5-Cyber voor EU open, Claude Opus 4.7 breed GA, DeepSeek-V4-Pro (1,6T params) als open-weight alternatief. **Twee:** agentinfrastructuur standaardiseert razendsnel – MCP naar Linux Foundation, Anthropic Agent Skills open source, Microsoft Agent 365 GA. **Drie:** open-source haalt structureel in – Hugging Face telt 13 miljoen gebruikers, 2 miljoen modellen; DeepSeek sluit de kloof met frontier-prestaties. Het resultaat: enterprise-modelkeuzes worden complexer terwijl kosten dalen en de noodzaak voor integratie- en gouvernancepartners stijgt.

### 🏛️ Governance & Beleid

De AI Omnibus van 7 mei is de meest bepalende beleidsdaad van de week. De uitgestelde deadlines voor high-risk AI bieden lucht voor implementatietrajecten, maar de basisdatum van 2 augustus 2026 blijft het referentiepunt: GPAI-transparantieverplichtingen gelden dan. Nationaal: 10 Nederlandse toezichthouders zijn operationeel, maar slechts 42% van organisaties heeft volledig AI-beleid. De uitvoeringskloof is groot. Structureel patroon: Europese governance-daadkracht groeit (verbod nudification-apps, sterkere AI Office), maar de implementatie-capaciteit bij organisaties loopt achter op de wetgevingscyclus.

### 🔐 Security & Risk

Security domineert de week langs twee lijnen. **Offensief:** 28,3% van CVEs uitgebuit binnen 24 uur na disclosure; eerste AI-ontwikkelde zero-day voor 2FA-bypass gepubliceerd; 86% van phishingaanvallen AI-aangestuurd (KnowBe4); drie coderingsagenten lekten secrets via één aanval. **Defensief:** Microsoft MDASH (multi-agent, 100+ gespecialiseerde agents) scoort 88,45% op CyberGym en ontdekte 16 nieuwe Windows-kwetsbaarheden waaronder 4 kritieke RCE's – beter dan elk enkel-model systeem. Kernpatroon: AI versnelt zowel aanvals- als verdedigingscapaciteiten, maar het aanvalsoppervlak groeit sneller dan de gemiddelde organisatie kan bijhouden.

### 📈 Markt & Adoptie

Twee krachten domineren. **Consolidatie:** Microsoft en Google domineren het enterprise-speelveld (Gartner); Google Cloud overstijgt $20B/kwartaal (+63% YoY); hyperscalers investeren samen >$500B capex voor AI in FY2026. **Institutionalisering:** enterprise JVs van OpenAI (The Development Company, $4B) en Anthropic (met Blackstone/Goldman Sachs) signaleren dat AI-labs zelf enterprise-dienstverleners worden. De eerste AI-agent betaling in NL (Mastercard/Rabobank) is een concreet Benelux-marktsignaal. 17,8% van de wereldwijde beroepsbevolking gebruikt AI actief; in 26 landen al meer dan 30%.

---

## 💼 Ctac-weekperspectief

- **EU AI Act 2 augustus: 79 dagen – start nu met klantgesprekken.** GPAI-transparantievereisten gelden per 2 augustus; NCII-verbod per 2 december 2026. Klanten in overheid, zorg en finance zijn aantoonbaar onvoldoende voorbereid (42% volledig AI-beleid). Een Ctac AI Act Readiness Scan – gap-analyse, risicoklassificatie, documentatiebegeleiding – is de meest directe propositie voor de komende zes weken. Wie nu begint, haalt de deadline.

- **Microsoft Agent 365 als onboarding-haakje voor agent governance.** De GA van Agent 365 ($15/user/maand) is de eerstvolgende concrete aankoopdecisie voor enterprise-klanten op het Microsoft-platform. Ctac kan het inrichtings- en beheerverhaal vertellen: welke agents deployen, hoe beheer en audit je ze, en hoe past dit in de AI Act-verplichtingen. Dit combineert een directe Microsoft-propositie met een compliance-argument.

- **Semantic Kernel patchprioriteit voor alle actieve AI-projecten.** CVE-2026-25592 (.NET SDK vóór v1.71.0) en CVE-2026-26030 (Python SDK vóór v1.39.4) zijn CVSS 9.9 en direct exploiteerbaar via prompt injection. Elk Ctac-project dat Semantic Kernel inzet, moet patches uitrollen en de agent-toolchain reviewen op blootstelling. Dit is deze week actie, niet volgende week.

- **MCP-standaardisatie elimineert het vendor lock-in bezwaar.** Klanten die aarzelen bij agentische projecten wegens protocol-afhankelijkheid kunnen nu gerustgesteld worden: MCP is open standaard onder de Linux Foundation, breed gedragen door Anthropic én OpenAI. Ctac kan agentische architectuurvoorstellen doen zonder dat proprietary lock-in als dealbreaker geldt.

---

## 📚 Bronnenlijst

**Technologie & Modellen**
- [Anthropic Claude Opus 4.7 – Anthropic.com](https://www.anthropic.com/news/claude-opus-4-7)
- [Anthropic "Dreaming": agents leren van eigen fouten – VentureBeat](https://venturebeat.com/technology/anthropic-introduces-dreaming-a-system-that-lets-ai-agents-learn-from-their-own-mistakes)
- [Anthropic Mythos gelimiteerde release – TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [OpenAI verleent EU toegang tot GPT-5.5-Cyber – CNBC](https://www.cnbc.com/2026/05/11/openai-eu-cyber-model-anthropic-mythos-gpt.html)
- [Anthropic doneert MCP aan Agentic AI Foundation – Anthropic.com](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [OpenAI Agentic AI Foundation – OpenAI.com](https://openai.com/index/agentic-ai-foundation/)
- [Anthropic Agent Skills open source – VentureBeat](https://venturebeat.com/technology/anthropic-launches-enterprise-agent-skills-and-opens-the-standard)
- [DeepSeek V4 preview: sluit kloof met frontier – TechCrunch](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/)
- [Hugging Face State of Open Source AI Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Microsoft herschrijft Windows als AI-native OS – VentureBeat](https://venturebeat.com/ai/microsoft-remakes-windows-for-an-era-of-autonomous-ai-agents)

**Governance & Beleid**
- [EU AI Act Omnibus politiek akkoord 7 mei – Consilium EU](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [Wat de Omnibus-deal verandert – TechPolicy.Press](https://www.techpolicy.press/what-the-eu-ai-omnibus-deal-changes-for-the-ai-act-and-what-lies-ahead/)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC richtlijnen AI Act implementatie](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Tien toezichthouders bewaken naleving AI-verordening NL – Computable](https://www.computable.nl/2026/04/22/tien-toezichthouders-bewaken-naleving-ai-verordening/)
- [AI-gedrag en soevereiniteit op Cybersec Netherlands 2026 – Computable](https://www.computable.nl/2026/05/06/ai-gedrag-en-soevereiniteit-centraal-op-cybersec-netherlands-2026/)

**Security & Risk**
- [When Prompts Become Shells: RCE in AI agent frameworks – Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Defense at AI Speed: MDASH tops CyberGym – Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)
- [MDASH ontdekt 4 kritieke Windows RCE's – Help Net Security](https://www.helpnetsecurity.com/2026/05/13/microsoft-mdash-agentic-ai-security-system/)
- [1 miljoen blootgestelde AI-diensten – The Hacker News](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)
- [2026: jaar van AI-ondersteunde aanvallen – The Hacker News](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)
- [Eerste AI-ontwikkelde zero-day voor 2FA-bypass – The Hacker News](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known-zero-day-2fa-bypass-for-mass-exploitation.html)
- [Shadow AI security risico's in enterprises – The Hacker News](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html)
- [AI agent runtime security – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Promptware Kill Chain – Schneier on Security](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)

**Markt & Adoptie**
- [Microsoft Agent 365 GA – VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [Microsoft Frontier Firms operating model – Microsoft Blog](https://blogs.microsoft.com/blog/2026/05/05/how-frontier-firms-are-rebuilding-the-operating-model-for-the-age-of-ai/)
- [OpenAI & Anthropic lanceren enterprise JVs – TechCrunch](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/)
- [OpenAI CRO: enterprise AI op kantelpunt – CNBC](https://www.cnbc.com/2026/05/11/open-ai-dresser-enterprise-business.html)
- [Microsoft State of Global AI Diffusion 2026 – Microsoft On the Issues](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)
- [Google Cloud overstijgt $20B/kwartaal – CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [Microsoft en Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Pentagon deals met Nvidia, Microsoft en AWS – TechCrunch](https://techcrunch.com/2026/05/01/pentagon-inks-deals-with-nvidia-microsoft-and-aws-to-deploy-ai-on-classified-networks/)
- [Eerste AI-agent betaling NL: Mastercard + Rabobank – Computable](https://www.computable.nl/2026/05/05/kort-ai-ontslagen-betekenen-zelden-hoger-rendement-ai-moet-maakindustrie-verslimmen-en-meer/)
- [Google investeert $40B in Anthropic – TechCrunch](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
