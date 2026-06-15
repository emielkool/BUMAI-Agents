---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-19
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 19 mei 2026

## 🔑 Highlights van de dag

- **Google I/O 2026 is vandaag van start gegaan** (19–20 mei, PT). Er worden grote Gemini-aankondigingen verwacht, waaronder een nieuw flagship modelfamilie. Live updates bevestigen Android 17 en Gemini XR-integraties.
- **Anthropic koopt Stainless** voor meer dan $300 miljoen (18 mei). Stainless bouwt API SDK-tooling die ook door OpenAI en Google wordt gebruikt — een strategische overname die Anthropic's positie in de developer toolchain versterkt.
- **Anthropic passeert OpenAI in enterprise-adoptie** voor het eerst: 34,4% van de Amerikaanse bedrijven betaalt voor Claude vs. 32,3% voor ChatGPT. Claude Code is Anthropic's snelstgroeiend product ooit.
- **EU AI Act deadline augustus 2026 nadert** — conformiteitsbeoordelingen, CE-markering en EU-database-registratie voor hoog-risico-systemen moeten vóór 2 augustus gereed zijn.
- **Prompt injection blijft hardnekkig beveiligingsrisico**: NIST noemt het "de grootste beveiligingsfout van generatieve AI"; meerdere nieuwe incidenten in Q1–Q2 2026 bij Claude, Gemini en AI coding agents.

---

## 🧠 Technologie & Modellen

**Google I/O 2026** is vandaag begonnen. Geruchten wijzen op de aankondiging van een nieuwe Gemini flagship modelgeneratie. Eerder deze maand lanceerde Google al **Gemini 3.1 Flash-Lite** — 2,5× sneller dan vorige versies en geprijsd op $0,25 per miljoen input tokens, wat het interessant maakt voor hoog-volume enterprise use cases.

**OpenAI** bracht op 5 mei **GPT-5.5 Instant** uit als standaard ChatGPT-model, met verbeterde feitelijkheid, minder hallucinaties en gepersonaliseerde antwoorden. Op 7 mei volgden nieuwe realtime spraakmodellen in de API met redeneer- en vertaalfunctionaliteit.

**Anthropic** maakte gisteren (18 mei) de overname van **Stainless** bekend — een startup die SDK-generatietools bouwt voor API-integratie. Bijzonder is dat Stainless ook door OpenAI en Google wordt ingezet; de overname geeft Anthropic directe grip op een kritiek onderdeel van de AI-developer toolstack. Prijs: >$300 miljoen.

In het **open-source landschap** lanceerde HiDream-O1-Image (8B parameters) eerder deze maand als top-ranking open-weights tekst-naar-beeld model. Op Hugging Face zijn inmiddels >2 miljoen publieke modellen beschikbaar; 30%+ van de Fortune 500 heeft een verified account.

**Bronnen:** [TechCrunch – GPT-5.5](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/) · [TechCrunch – Anthropic/Stainless](https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/) · [Google I/O live](https://www.androidcentral.com/phones/live/google-i-o-2026-live-blog-android-17-android-xr-glasses-and-all-the-gemini-ai-news) · [HiDream op Hugging Face](https://huggingface.co/HiDream-ai/HiDream-O1-Image)

---

## 🏛️ Governance & Ethiek

De **EU AI Act deadline van 2 augustus 2026** is nog 75 dagen weg. Organisaties die hoog-risico AI-systemen inzetten, moeten vóór die datum conformiteitsbeoordelingen afronden, technische documentatie finaliseren, CE-markering aanbrengen en registreren in de EU-database. Elke lidstaat moet ook een regulatoire sandbox operationeel hebben.

De **AI Office** van de Europese Commissie werkt dit jaar aan praktische guidelines voor hoog-risico-classificatie, transparantievereisten en incidentrapportage. Die guidelines worden verwacht in de loop van 2026 maar zijn nog niet gepubliceerd — organisaties zitten dus nog deels in een juridische grijszone.

Signaal uit NL/BE: slechts **42% van de Belgische bedrijven** heeft een volledig AI-beleid, terwijl 34,5% al actief AI gebruikt. De governance-kloof is reëel en groeit.

**Bronnen:** [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/) · [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [DataNews – AI-gebruik België](https://datanews.knack.be/analyse/ai-gebruik-in-belgische-bedrijven-blijft-toenemen-al-1-op-de-3-ondernemingen-zet-ai-actief-in/)

---

## 🔐 Security & Risk

**Prompt injection** staat opnieuw prominent in het nieuws. NIST heeft het formeel aangemerkt als "generatieve AI's grootste beveiligingsfout"; OWASP plaatst het op #1 in de LLM Top 10. OpenAI erkende eerder dat het probleem structureel onoplosbaar is zolang modellen geen betrouwbaar onderscheid kunnen maken tussen instructies en data.

Concrete incidenten in 2026:
- Een **zero-click XSS-kwetsbaarheid** in de Claude Chrome-extensie (inmiddels gepatcht) maakte het mogelijk om kwaadaardige prompts te triggeren via elke willekeurige website.
- **Drie AI coding agents** (waaronder Claude) lekten secrets via een enkele prompt-injection aanval; één vendor had dit risico al beschreven in zijn systeemkaart.
- **Google Gemini** vertoonde een kwetsbaarheid waarbij privé-agendadata uitlekte via kwaadaardige agenda-uitnodigingen.

Voor agentische systemen — die autonoom acties ondernemen — is dit een serieus aandachtspunt: de blast radius van een succesvolle aanval is groter dan bij een chatbot.

**Bronnen:** [Airia – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) · [VentureBeat – agent secrets leak](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) · [The Hacker News – Claude extensie](https://thehackernews.com/2026/03/claude-extension-flaw-enabled-zero.html)

---

## 📈 Markt & Adoptie

**OpenAI** oversteeg $25 miljard aan geannualiseerde omzet en verkent een beursgang eind 2026. **Anthropic** nadert $19 miljard. De race tussen beide labs versnelt — en verschuift van modelkwaliteit naar enterprise tooling en ecosysteem.

**JPMorgan Chase** heeft zijn AI-investeringen formeel geherkwalificeerd van experimenteel R&D naar core infrastructure: $19,8 miljard technologiebudget in 2026, 2.000 AI-medewerkers. Dit is een markant signaal dat AI-adoptie bij grote financiële instellingen operationeel fase ingaat.

**Novo Nordisk** en OpenAI sloten een strategisch partnership voor AI-integratie door de gehele bedrijfsvoering, van drug discovery tot supply chain. Een voorbeeld van "AI als bedrijfsstrategie" in een zwaar gereguleerde sector.

**Google** investeert $750 miljoen om Gemini Enterprise via partners te versnellen — met dedicated engineers bij Accenture, Deloitte en Cognizant, en een ecosysteem van 120.000 partners. **Computable** signaleert dat dit consultancy-gedreven model ook in de Nederlandse markt landt.

**Pentagon** sloot deals met Nvidia, Microsoft en AWS voor inzet van AI op geclassificeerde netwerken (1 mei).

**Bronnen:** [TechCrunch – OpenAI omzet](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/) · [Computable – Google Gemini Enterprise](https://www.computable.nl/2026/05/01/google-zet-alles-op-gemini-enterprise-ambitie-architectuur-en-een-leger-consultants/) · [TechCrunch – Pentagon](https://techcrunch.com/2026/05/01/pentagon-inks-deals-with-nvidia-microsoft-and-aws-to-deploy-ai-on-classified-networks/) · [LLM Stats](https://llm-stats.com/ai-news)

---

## 💡 Ctac-relevantie

**1. Google I/O en het Gemini Enterprise-model zijn direct relevant voor Ctac's propositie.** Google bouwt zijn enterprise-AI-strategie expliciet via een partnernetwerk van consultants en implementatiepartners. Als Ctac niet actief in dit ecosysteem stapt, verliest het positie aan Accenture en Deloitte. De vraag is concreet: welke Google Cloud/Gemini-partnerstatus heeft Ctac, en wat is de roadmap?

**2. EU AI Act compliance = onmiddellijke dienst opportunity.** Met 75 dagen tot de augustus-deadline en een groot governance-gat (42% heeft beleid, 34,5% gebruikt al AI), liggen compliance-assessments en beleidsontwikkeling klaar als kortcyclische opdrachten. Ctac kan hier nu mee naar bestaande klanten.

**3. Agentic AI Foundation (MCP-standaard naar Linux Foundation).** Anthropic doneert het Model Context Protocol aan de AAIF; OpenAI en Google steunen dit. Dit wordt de de-facto standaard voor agent-integraties. Ctac's AI-engineer moet dit kennen — het bepaalt hoe tools, agents en enterprise systemen straks koppelen.

**4. Prompt injection als risicogesprek met klanten.** Nu NIST en OWASP dit als #1-dreiging benoemen, wordt het steeds makkelijker om security-first AI-implementatiegesprekken te voeren. Ctac kan dit inzetten als differentiator: "wij implementeren AI-agents op een veilige manier."

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Anthropic koopt Stainless](https://techcrunch.com/2026/05/18/anthropic-has-acquired-the-dev-tools-startup-used-by-openai-google-and-cloudflare/)
- [VentureBeat – Anthropic passeert OpenAI in enterprise-adoptie](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)
- [OpenAI – Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/)
- [Google Cloud Next 2026 wrap-up](https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act guidelines](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Airia – AI Security in 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [VentureBeat – AI agents en secret leaks](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Computable – Google Gemini Enterprise NL](https://www.computable.nl/2026/05/01/google-zet-alles-op-gemini-enterprise-ambitie-architectuur-en-een-leger-consultants/)
- [DataNews – AI-gebruik Belgische bedrijven](https://datanews.knack.be/analyse/ai-gebruik-in-belgische-bedrijven-blijft-toenemen-al-1-op-de-3-ondernemingen-zet-ai-actief-in/)
- [LLM Stats – AI updates mei 2026](https://llm-stats.com/ai-news)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
