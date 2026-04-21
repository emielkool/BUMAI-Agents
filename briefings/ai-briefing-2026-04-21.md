---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-21
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 21 april 2026

## 🔑 Highlights van de dag

- **Stanford AI Index 2026 gepubliceerd:** Organisatorische AI-adoptie is gestegen naar 88%; SWE-bench codering-benchmark bereikte bijna 100% nauwkeurigheid in één jaar. De kloof tussen AI-insiders en het grote publiek groeit echter zichtbaar.
- **PwC AI Performance Study:** 74% van de economische AI-waarde wordt afgeroomd door slechts 20% van de bedrijven. AI-leiders investeren 2,5× meer en sturen op groei, niet alleen op efficiëntie.
- **EU AI Act Q2-richtlijnen in voorbereiding:** De Europese Commissie publiceert deze zomer praktische handleidingen voor high-risk AI-systemen. Volledige werking wet volgt 2 augustus 2026.
- **Microsoft adopteert Google Agent2Agent (A2A):** Microsoft maakt zijn Copilot Studio en Azure AI Foundry compatibel met het A2A-protocol — een stap richting cross-vendor multi-agent standaardisatie.
- **Transparantie onder druk:** Foundation Model Transparency Index daalde van 58 naar 40 punten. Modellen worden krachtiger én ondoorzichtiger.

---

## 🧠 Technologie & Modellen

**Stanford AI Index 2026** bevestigt opnieuw dat de vooruitgang onverminderd doorzet — ondanks eerder geopende discussies over een 'plafond'. Op SWE-bench Verified steeg de score van 60% naar bijna 100% in één jaar. OSWorld (computertaken over besturingssystemen) bereikte 66,3%, slechts 6 procentpunt onder menselijke prestaties. Tegelijkertijd lopen autonome robots ver achter: slechts 12% succespercentage bij huishoudelijke taken.

**Google TurboQuant** (gepresenteerd op ICLR 2026) is een nieuw kwantisatie-algoritme dat de KV-cache-geheugenoverhead sterk reduceert. Praktisch effect: modellen met enorme contextvensters draaien efficiënter — relevant voor kostenoptimalisatie bij inference-zware toepassingen.

**GLM-5**, gelanceerd door Chinese onderzoeksgroep Zhipu AI, is momenteel #1 open-weight model op Artificial Analysis en LMArena Text Arena. Het scoort 77,8% op SWE-bench Verified en 92,7% op AIME 2026 — een serieuze uitdager voor Meta Llama en Qwen in de open-source categorie.

**MIT Technology Review** publiceert vandaag voor het eerst zijn jaarlijkse "10 Things That Matter in AI Right Now"-lijst — een signaal dat de mediaframing van AI verschuift van 'hype' naar 'structurele technologie'.

*Bronnen: [Stanford HAI 2026 AI Index](https://hai.stanford.edu/ai-index/2026-ai-index-report) · [TechCrunch – Stanford rapport](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/) · [Hugging Face – GLM-5](https://huggingface.co/blog/mlabonne/glm-5) · [MIT Technology Review](https://www.technologyreview.com/2026/04/14/1135298/coming-soon-10-things-that-matter-in-ai-right-now/)*

---

## 🏛️ Governance & Ethiek

**EU AI Act** treedt volledig in werking op 2 augustus 2026. In Q2 2026 publiceert de Commissie praktische richtlijnen voor: high-risk AI-classificatie, transparantie-eisen (Art. 50), incidentrapportage en verplichtingen voor providers én deployers. Elke lidstaat moet vóór 2 augustus een nationaal AI-regulatory sandbox hebben ingericht.

**Google en Microsoft ondertekenden de EU AI Act Code of Practice** — een zelfregulerings-instrument dat de brug slaat naar de formele conformiteitsvereisten. Dit verhoogt de druk op andere vendors én op enterprise-afnemers om hun eigen AI-governance op orde te hebben.

**TransparantiepaRadox:** De Foundation Model Transparency Index daalde dit jaar van 58 naar 40 punten, terwijl modellen technisch steeds sterker worden. Dit wekt terechte zorgen: hoe krachtiger de modellen, hoe minder inzicht aanbieders bieden in trainingsdata, energieverbruik en veiligheidsevaluaties.

**Publieke opinie versus AI-experts** divergeert verder. Stanford constateert dat 59% van de mensen positief staat tegenover AI (+7%), maar dat de gapende kloof met hoe experts over het potentieel denken een governance-uitdaging creëert voor overheden en werkgevers.

*Bronnen: [EU AI Act Implementation](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/) · [EC richtlijnen](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines) · [CIO Dive – Code of Practice](https://www.ciodive.com/news/Google-european-union-AI-act-code-signatory/756343/)*

---

## 🔐 Security & Risk

**Prompt injection blijft structureel probleem.** OpenAI stelt dat het fenomeen — net als social engineering op het web — nooit volledig opgelost zal worden. Toch heeft 65,3% van de organisaties nóg geen prompt injection-verdediging geïmplementeerd, ondanks groeiende incidenten.

**Model Context Protocol (MCP) kwetsbaarheid:** Onderzoekers identificeerden een aanvalsvector via de sampling-feature van MCP waarmee aanvallers hidden tool invocations kunnen uitvoeren, compute-quota kunnen uitputten en data kunnen exfiltreren. Dit is relevant voor elke organisatie die MCP-gebaseerde agent-infrastructuur uitrolt.

**NIST CVE-procedures** zijn per 15 april 2026 bijgewerkt om AI-specifieke kwetsbaarheden beter te categoriseren — een eerste stap richting gestandaardiseerde AI-securitytaxonomie.

*Bronnen: [VentureBeat – Prompt Injection](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay) · [The Hacker News – OpenClaw](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html) · [VentureBeat – 11 runtime attacks](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)*

---

## 📈 Markt & Adoptie

**PwC 2026 AI Performance Study** (1.217 executives, 25 sectoren): de top-20% AI-leiders nemen 74% van alle economische AI-waarde. Ze investeren 2,5× meer als % van omzet, sturen op groei (niet alleen kostenbesparing), en automatiseren beslissingen 2,8× sneller dan achterblijvers. Praktische les: bedrijven die AI als productiviteitstool zien, lopen structureel achter op bedrijven die het als groeicatalysator inzetten.

**Microsoft Agent2Agent (A2A):** Microsoft committeert zich aan Google's A2A-protocol, waardoor multi-agent workflows vendor-onafhankelijk kunnen worden ingericht via Azure AI Foundry en Copilot Studio. Dit is de meest concrete stap tot nu toe richting interoperabiliteit in de agent-markt.

**Microsoft lanceert 3 eigen foundation models:** een spraak-transcriptiesysteem, een voice generation-engine en een verbeterde image creator — allemaal in-house gebouwd, los van OpenAI-afhankelijkheid.

**Nvidia enterprise AI-agentplatform** (GTC 2026): adoptie door Adobe, Salesforce en SAP verankert Nvidia's positie in de enterprise AI-stack. SAP's deelname is relevant voor het Ctac-SAP-portfolio.

**Novo Nordisk + OpenAI** kondigden een strategisch partnership aan waarbij AI wordt uitgerold over het volledige bedrijf — van drug discovery tot supply chain. Een early indicator voor hoe frontier-AI-integratie eruitziet op enterprise-schaal.

*Bronnen: [PwC AI Performance Study](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html) · [CIO Dive – A2A](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/) · [VentureBeat – Nvidia GTC](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among) · [VentureBeat – Microsoft modellen](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)*

---

## 💡 Ctac-relevantie

**Van pilot naar leider:** De PwC-studie bewijst empirisch wat Ctac al als propositie kan uitdragen: de meerderheid van organisaties zit vast in AI-pilots. Ctac kan zich positioneren als de partner die de stap van 'experimenteren' naar 'schaalbaar groeien' begeleidt — inclusief governance, automatiseringsarchitectuur en ROI-frameworks.

**EU AI Act compliance window sluit:** Met augustus 2026 als deadline en Q2-richtlijnen die nu verschijnen, is dit het juiste moment voor Ctac om actief AI Act-readiness assessments bij klanten te agenderen. Sectoren als overheid, zorg en finance hebben het meeste urgentie.

**Agent interoperabiliteit (A2A/MCP):** Microsoft's adoptie van A2A en de opkomende MCP-kwetsbaarheden wijzen op een markt in transitie: multi-agent architectuur wordt standaard, maar security-risico's lopen voor op beheersing. Ctac's AI engineer kan hier directe toegevoegde waarde leveren bij klantprojecten.

**SAP + Nvidia AI-platform:** SAP's deelname in het Nvidia enterprise AI-agentplatform is een signaal dat SAP's AI-roadmap versnelt. Ctac's SAP-praktijk moet deze beweging actief volgen en klanten proactief informeren over wat dit betekent voor hun SAP-omgevingen.

---

## 📚 Bronnen & verder lezen

- [Stanford HAI – 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- [Inside the AI Index: 12 Takeaways](https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report)
- [TechCrunch – Stanford groeiende kloof AI-insiders vs publiek](https://techcrunch.com/2026/04/13/stanford-report-highlights-growing-disconnect-between-ai-insiders-and-everyone-else/)
- [PwC 2026 AI Performance Study](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html)
- [EU AI Act – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Supporting AI Act implementation](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [CIO Dive – Microsoft + A2A interoperabiliteit](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [CIO Dive – Microsoft AI investeringsstrategie](https://www.ciodive.com/news/microsoft-ai-investments-questions-strategy/810906/)
- [VentureBeat – Prompt Injection](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Hugging Face – GLM-5](https://huggingface.co/blog/mlabonne/glm-5)
- [VentureBeat – Nvidia enterprise AI platform GTC 2026](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [MIT Technology Review – 10 Things That Matter in AI](https://www.technologyreview.com/2026/04/14/1135298/coming-soon-10-things-that-matter-in-ai-right-now/)
