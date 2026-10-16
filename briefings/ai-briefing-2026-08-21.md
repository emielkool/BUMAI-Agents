---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-21
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 21 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaving gestart (2 aug):** De Europese Commissie handhaaft vanaf 2 augustus actief de AI Act — chatbots moeten zich identificeren als AI, deepfakes moeten gelabeld worden. Dit is geen verre toekomst meer maar dagelijkse realiteit.
- **OpenAI GPT-5.6 + Ultrafast:** OpenAI's nieuwe modelfamilie (Sol, Terra, Luna) is live; Sol is 14× sneller in Ultrafast-modus en 54% token-efficiënter in codeertaken. Inzetten hierop in klantprojecten is nu praktisch haalbaar.
- **Prompt injection: 94% van LLM-agents kwetsbaar:** Nieuw VentureBeat-onderzoek en Anthropic-publicaties bevestigen dat prompt injection de centrale kwetsbaarheid is in agentic AI. Drie AI-codeeragenten lekten secrets via één aanval.
- **Inference overtreft training in budget:** Wereldwijd wordt voor het eerst meer uitgegeven aan inference ($23,3 mrd) dan aan training ($19 mrd). Enterprises zijn volop aan het operationaliseren.
- **Nederland: tweede AI-exporteur Europa:** Met €80 mrd aan AI-gerelateerde goederenexport staat Nederland op de elfde plek wereldwijd — direct relevant voor positionering van Nederlandse IT-dienstverleners.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 en Ultrafast Mode**
OpenAI lanceerde begin augustus de GPT-5.6 familie in drie varianten: Sol (werkpaard), Terra (midden) en Luna (budget). Op 13 augustus werd Ultrafast Mode voor Sol beschikbaar gesteld, tot 14× sneller dan de standaardmodus. Sol is 54% token-efficiënter in AI-codeertaken. Vanaf 11 augustus zijn Daybreak-modellen beschikbaar via AWS.
→ [TechCrunch – GPT-5.6 launch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)

**Google Gemini 3.x + Robotics ER 2**
Google lanceerde drie nieuwe Gemini-modellen: 3.6 Flash, 3.5 Flash-Lite en 3.5 Flash Cyber, specifiek ontworpen voor agentic workflows. Tegelijkertijd verscheen Gemini Robotics ER 2, het krachtigste "embodied reasoning"-model voor robotica tot nu toe.
→ [Google Blog – AI updates juli 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-july-2026/)

**Meta Muse Glimmer 30B (lokaal agentic model)**
Meta bracht Muse Glimmer 30B uit — een model met geïntegreerde perceptie-encoder, gericht op autonome agentic taken op consumenten-hardware. Bijzonder: het draait volledig lokaal, zonder cloud of netwerktoegang, en combineert multi-stap redeneren, toolgebruik en multimodaliteit.
→ [Hugging Face – Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving actief per 2 augustus 2026**
De Europese Commissie en nationale toezichthouders zijn begonnen met actieve handhaving van de AI Act. Concrete verplichtingen: chatbots moeten gebruikers informeren dat zij met AI interacteren; deepfakes (beeld, video, audio) moeten zichtbaar gelabeld zijn. Het AI Office kan boetes opleggen, documentatie opvragen en correctieve maatregelen eisen.
→ [EC Digital Strategy – Enforcement 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)

**AI Omnibus verlengt deadlines voor hoog-risico AI**
Op 27 juli 2026 trad het AI Omnibus-akkoord in werking (politiek akkoord: 7 mei 2026). Hoog-risico AI-systemen hebben nu tot 2 december 2027 de tijd; AI ingebed in producten tot 2 augustus 2028. Elke lidstaat moet per 2 augustus een nationale AI-sandbox operationeel hebben.
→ [EU AI Act tracker](https://artificialintelligenceact.eu/)

---

## 🔐 Security & Risk

**Prompt injection: structureel probleem in enterprise AI**
VentureBeat publiceerde meerdere diepgaande analyses over prompt injection als de dominante aanvalsvector in agentic AI. Drie AI-codeeragenten lekten API-tokens via één geïnjecteerde prompt. Microsoft moest een CVE (2026-21520, CVSS 7.5) patchen in Copilot Studio — data werd alsnog geëxfiltreerd. Anthropic publiceerde als eerste vendor concrete failure rates voor prompt injection, waarmee het onderwerp eindelijk meetbaar wordt.
→ [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
→ [VentureBeat – Anthropic publiceert failure rates](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)

**België: 14% meer AI-gedreven cyberaanvallen**
Data News rapporteert een stijging van 14% in cyberaanvallen in België in 2025, waarbij AI een centrale rol speelt bij aanvallers.
→ [Data News – Meer cyberaanvallen door AI](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)

---

## 📈 Markt & Adoptie

**Inference overtreft training in AI-budgetten**
Voor het eerst in 2026 overtreft wereldwijde inference-spending ($23,3 mrd) de training-spending ($19 mrd). Dit markeert een kantelpunt: de markt is volwassen genoeg om te operationaliseren. De drie grote hyperscalers (Microsoft, Google, AWS) investeren samen meer dan $500 mrd in AI-infrastructuur in FY2026.
→ [CIO Dive – AI spending enterprise maturity](https://www.ciodive.com/news/AI-spending-soars-enterprise-maturity/827488/)

**Microsoft Frontier Company + AWS forward engineering**
Microsoft lanceerde Microsoft Frontier Company ($2,5 mrd, 6.000 specialisten) voor enterprise AI-deployments. AWS investeerde $1 mrd in een forward deployed engineering hub die klanten helpt AI-systemen operationeel te maken.
→ [TechCrunch – Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
→ [CIO Dive – AWS engineering hub](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)

**AI-adoptie NL/BE stijgt fors**
In Nederland gebruikt nu 61% van bedrijven AI (vorig jaar: 49%); in België 62% (vorig jaar: 52%). Tegelijkertijd is er een structureel tekort aan digitaal talent in de Benelux — de adoptie overstijgt de capaciteit om het goed te implementeren.
→ [Computable – Benelux koploper AI](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)

**Nederland tweede AI-exporteur van Europa**
Nederland exporteerde ruim €80 mrd aan AI-gerelateerde goederen, goed voor de elfde plek wereldwijd en de tweede plek in Europa (na Duitsland).
→ [Computable – Nederland tweede Europa AI-export](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/)

---

## 💡 Ctac-relevantie

De EU AI Act-handhaving die per 2 augustus is ingegaan, is direct actie-relevant voor Ctac-klanten: elke organisatie die een chatbot of AI-systeem naar eindgebruikers uitrolt, moet dit nu correct labelen. Dit opent een concreet advies- en implementatiespoor voor de AI-unit — denk aan AI Act compliance-scans, aanpassing van bestaande chatbot-implementaties en begeleiding bij sandboxregistratie.

De schaalbare adoptiecijfers in de Benelux (61%/62%) bevestigen dat klanten AI niet meer overwegen maar operationaliseren. Het structurele talentgebrek is een kans voor Ctac: positioneer je als implementatiepartner die de kloof tussen adoptie en effectief gebruik overbrugt. De opkomst van lokaal draaiende agentic modellen (Muse Glimmer 30B) maakt het tegelijkertijd mogelijk om AI-oplossingen te bouwen zonder afhankelijkheid van cloud-API's — interessant voor klanten met privacygevoelige data.

Prompt injection als #1 kwetsbaarheid vraagt om een security-by-design aanpak in elk agentic AI-traject dat Ctac begeleidt. Neem dit op als vast onderdeel van het AI-delivery-raamwerk.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI GPT-5.6 launch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [Google Blog – AI updates juli 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-july-2026/)
- [Hugging Face – Meta Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- [EC Digital Strategy – AI Act handhaving 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat – Anthropic prompt injection failure rates](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)
- [VentureBeat – Microsoft Copilot Studio CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [CIO Dive – AI spending maturity](https://www.ciodive.com/news/AI-spending-soars-enterprise-maturity/827488/)
- [TechCrunch – Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [CIO Dive – AWS engineering hub](https://www.ciodive.com/news/aws-creates-forward-deployed-engineering-hub/824109/)
- [CIO Dive – Microsoft/Google enterprise AI leadership](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Computable – Benelux AI-adoptie](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [Computable – Nederland tweede AI-exporteur Europa](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/)
- [Data News – Meer cyberaanvallen door AI in België](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
