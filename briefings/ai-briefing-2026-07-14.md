---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-14
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 14 juli 2026

## 🔑 Highlights van de dag

- **OpenAI GPT-5.6 lancering**: Op 9 juli introduceerde OpenAI drie nieuwe modellen — Sol (coding-focus), Terra (middenklasse) en Luna (budget) — waarbij Sol expliciet tegen Anthropic's Fable wordt gepositioneerd. De uitrol loopt via een door de overheid goedgekeurde klant-per-klant preview.
- **EU AI Act op de drempel van volledige toepassing**: Op 2 augustus 2026 treedt de EU AI Act volledig in werking, inclusief transparantieregels. Elke lidstaat moet voor die datum een AI regulatory sandbox operationeel hebben — een deadline die veel organisaties verrast.
- **Prompt injection escaleert naar agentic AI**: Meerdere incidenten bevestigen dat AI-agenten met toolgangen en codeexecutie fundamenteel kwetsbaar zijn voor prompt injection — OWASP benoemt dit voor het tweede jaar op rij als de #1 LLM-kwetsbaarheid.
- **Cloud-driehoek domineert enterprise AI**: Microsoft passeert 20 miljoen betaalde Copilot-seats; Google lanceert Agentic Data Cloud; AWS investeert 1 miljard dollar in forward-deployed AI engineering. De consolidatie rond drie hyperscalers versnelt.
- **GLM-5 zet Chinese open-source op de kaart**: Zhipu AI's GLM-5 (744B MoE, MIT-licentie) staat bovenaan de Artificial Analysis open-weight ranglijst, wat het geopolitieke speelveld van AI-modellen verder compliceert.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 — drie varianten, gefaseerde uitrol**
OpenAI lanceerde op 9 juli GPT-5.6 met drie smaken: Sol (beste coding-model volgens OpenAI, 54% tokenefficiënter dan voorganger), Terra en Luna. De release is beperkt tot een preview op basis van overheidsselectie — dit patroon van reguleringsgestuurde uitrol is nieuw en suggereert dat ook de VS AI-releases steeds formeler controleert.
Bron: [TechCrunch – OpenAI GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)

**Anthropic Fable 5 & Sonnet 5**
Fable 5 keerde op 1 juli volledig terug (na een tijdelijke beperking door de Trump-administratie), samen met de release van Claude Sonnet 5 — een goedkopere variant geoptimaliseerd voor agentische taken. De concurrentiedruk tussen Anthropic en OpenAI verschuift van benchmarks naar deployment-kosten en agentic performance.
Bron: [TechCrunch – Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)

**GLM-5 — open-source topper uit China**
Zhipu AI's GLM-5 (744B parameters, 40B actief bij MoE-routing, MIT-licentie) staat bovenaan de Artificial Analysis open-weight ranglijst. Dit toont dat serieuze open-source alternatieven niet alleen uit het Westen komen — een factor die Ctac in sourcing- en compliance-beslissingen moet meewegen.
Bron: [Hugging Face Blog – GLM-5](https://huggingface.co/blog/mlabonne/glm-5)

---

## 🏛️ Governance & Ethiek

**EU AI Act: 2 augustus 2026 is de deadline**
De volledige AI Act-toepassing treedt in werking op 2 augustus 2026. Transparantievereisten gaan gelden voor alle AI-systemen die met burgers communiceren. Elke EU-lidstaat moet voor die datum een AI regulatory sandbox operationeel hebben. De Commissie werkt momenteel aan praktijkrichtlijnen voor hoog-risico-classificatie en transparantievereisten.
Bron: [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)

**VN lanceert AI for Good Global Commission**
Op 2 juli lanceerden de VN en ITU de AI for Good Global Commission, co-voorgezeten door Salesforce-CEO Marc Benioff en de Rwandese president Kagame. Het mandaat: mondiale standaarden voor verantwoord AI-gebruik. Dit signaleert dat het governance-debat definitief van EU-niveau naar mondiaal niveau trekt.
Bron: [UN News – AI Governance](https://news.un.org/en/story/2026/07/1167862)

**Nederland: licentirisico's en soevereiniteitsbeleid**
Het kabinet krijgt binnenkort de bevoegdheid om overnames van Nederlandse AI-bedrijven door "niet-bevriende landen" te blokkeren. Computable meldt dat bijna de helft van de Nederlandse bedrijven sterk afhankelijk is van Amerikaanse cloudproviders — een kwetsbaarheid die strategisch aandacht vraagt.
Bron: [Computable.nl – AI licentierisico](https://www.computable.nl/2026/07/07/ai-is-tikkende-licentiebom-organisaties-lopen-groot-risico-zonder-harde-businesscase/) | [Computable.nl – blokkeren overnames](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/)

---

## 🔐 Security & Risk

**Prompt injection: van proof-of-concept naar productie-aanvallen**
VentureBeat documenteerde meerdere gevallen waarbij AI coding-agenten (waaronder een integratie met een GitHub Action van Anthropic's Claude Code) gevoelige informatie lekten via prompt injection. De aanval — "Comment and Control" — misbruikte het feit dat Anthropic's eigen system card al waarschuwde dat de feature "niet gehard is tegen prompt injection". OWASP benoemt dit voor het tweede jaar op rij als de #1 LLM-kwetsbaarheid.

Kern van het probleem: LLM's kunnen geen onderscheid maken tussen instructies en data. Naarmate agenten meer autonomie en toolaccess krijgen (bestandssysteem, APIs, databases), wordt dit aanvalsoppervlak alleen maar groter.
Bron: [VentureBeat – Agent prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [Airia – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)

---

## 📈 Markt & Adoptie

**Microsoft**: 20+ miljoen betaalde 365 Copilot-seats; AI-omzet op jaarbasis $37 miljard (+123% YoY). Bron: [CIO Dive – Microsoft earnings](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)

**Google Cloud**: Introductie van Agentic Data Cloud — een AI-native architectuur die legacy dataplatforms omzet in redenerende systemen. Google voegde $10 miljard toe aan zijn capaciteitsuitbreiding. Bron: [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)

**AWS**: Investeert $1 miljard in een forward-deployed engineering organisatie die software engineers combineert met AI-agenten om systemen direct bij klanten te bouwen. Bron: [CIO Dive – AWS FDE Hub](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)

**NVIDIA**: Lanceerde een enterprise AI agent platform met Adobe, Salesforce en SAP als eerste adopters op GTC 2026 — wat de positie van NVIDIA als orchestratielaag voor enterprise-agenten versterkt. Bron: [VentureBeat – NVIDIA GTC 2026](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)

---

## 💡 Ctac-relevantie

**EU AI Act deadline is nu**: De transparantieverplichtingen van 2 augustus gelden direct voor klanten die AI-toepassingen inzetten die communiceren met burgers of medewerkers. Ctac kan zich nu onderscheiden door een snelle AI Act compliance-scan aan te bieden — handig voor overheid- en zorgklanten die dit zelf niet scherp op het netvlies hebben.

**Agentic AI security is een propositiekans**: De golf van prompt injection-incidenten maakt security-by-design voor AI-agenten urgent. Ctac's AI-unit kan hier een aanvullende dienst op bouwen: een audit- en hardening-service voor klanten die agenten implementeren op basis van Microsoft Copilot, Azure OpenAI of Claude.

**Microsoft Copilot als instapmoment**: 20 miljoen betaalde seats bij Microsoft 365 Copilot bevestigt dat dit de meest voor de hand liggende enterprise AI-instap blijft voor bestaande Microsoft-klanten. Voor Ctac is dit een kans om implementatie- en adoptiediensten te structureren rondom een bewezen platform.

**Open-source versterkt onafhankelijkheid**: GLM-5 en Cohere North Mini Code laten zien dat kwalitatieve open-weight modellen snel verbeteren. Voor klanten met strenge dataprivacy-eisen (zorg, overheid) of soevereiniteitswensen biedt dit een realistisch alternatief voor closed-source providers — een argument dat Ctac kan inzetten in gevoelige sectoren.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI GPT-5.6 lancering](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [TechCrunch – Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [Anthropic Newsroom](https://www.anthropic.com/news)
- [Hugging Face Blog – GLM-5](https://huggingface.co/blog/mlabonne/glm-5)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Europese Commissie – AI Act ondersteuning](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [UN News – AI for Good Global Commission](https://news.un.org/en/story/2026/07/1167862)
- [Computable.nl – AI licentierisico](https://www.computable.nl/2026/07/07/ai-is-tikkende-licentiebom-organisaties-lopen-groot-risico-zonder-harde-businesscase/)
- [Computable.nl – blokkeren overnames niet-bevriende landen](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/)
- [VentureBeat – Prompt injection in AI agents](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – Comment and Control aanval](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Airia – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Microsoft Copilot & earnings](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [CIO Dive – AWS Forward Deployed Engineering](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)
- [VentureBeat – NVIDIA enterprise AI agent platform](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
