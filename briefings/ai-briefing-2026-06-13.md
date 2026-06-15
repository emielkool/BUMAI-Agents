---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-13
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 13 juni 2026

## 🔑 Highlights van de dag

- **EU AI Act D-50:** De volledige handhaving van de AI Act gaat op 2 augustus 2026 in — minder dan 7 weken. De Commissie publiceert ook een Code of Practice voor het labelen van AI-gegenereerde content (10 juni). Compliance is nu een operationeel vraagstuk, geen juridische toekomst.
- **OpenAI koopt Ona:** OpenAI kondigde op 11 juni de overname aan van Ona, een startup gericht op agentic workflows. Dit past in de bredere strategie: enterprise maakt inmiddels >40% van OpenAI's omzet uit en groeit naar pariteit met consumentenomzet eind 2026.
- **Agentic AI vergroot aanvalsoppervlak:** Nieuwe bevindingen tonen aan dat AI de tijd van vulnerability-discovery tot werkend exploit comprimeert van maanden naar uren. Claude Mythos ontdekte meer dan 10.000 kritieke kwetsbaarheden in systemisch belangrijke software in één maand — inclusief een 27 jaar oud OpenBSD-lek.
- **Microsoft "vrij" van OpenAI:** Microsoft's AI-divisie heeft formele autonomie gekregen om superintelligence te achtervolgen, met eigen researchers, data-pipelines en custom silicon. Zeven MAI-modellen zijn aangekondigd. Dit vergroot de concurrentiedruk op OpenAI in de enterprise markt.
- **Google Gemini 3 en Search-agenten:** Google introduceerde Gemini 3 en schakelde Gemini 3.5 Flash in als standaardmodel in AI Mode voor Search wereldwijd. De grootste upgrade van Google Search in 25 jaar: gebruikers kunnen meerdere AI-agenten aanmaken en aansturen.

---

## 🧠 Technologie & Modellen

**GPT-5.4 en agentische workflows** zijn de motor achter OpenAI's enterprise groei. De API verwerkt meer dan 15 miljard tokens per minuut. GPT-5.4 is het eerste mainline reasoning model met geïntegreerde frontier coding-capabilities van GPT-5.3-Codex. ([OpenAI](https://openai.com/index/introducing-gpt-5-4/))

**Google Gemini 3** is geïntroduceerd als de meest capabele Gemini-generatie tot nu toe, met Gemini 3.5 Flash nu actief als standaardmodel in Google Search AI Mode wereldwijd. ([Google Blog](https://blog.google/products-and-platforms/products/gemini/gemini-3/))

**Open-source agentische modellen** zijn in opmars: GLM-5.1, Kimi K2.6, DeepSeek V4 Pro en Qwen3 worden gezien als de voornaamste open-source alternatieven voor agentische AI-toepassingen. ([Hugging Face](https://huggingface.co/blog/daya-shankar/open-source-llms))

**Microsoft lanceert 7 MAI-modellen** over reasoning, code, imagegeneratie, transcriptie en voice — een directe uitdaging voor zowel OpenAI als Google. ([VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google))

---

## 🏛️ Governance & Ethiek

**2 augustus 2026: volledige handhaving EU AI Act.** Vanaf die datum treden de handhavingsbevoegdheden van de Commissie in werking voor GPAI-modelproviders, inclusief boetes. Alle nieuwe modellen die sinds 2 augustus 2025 zijn uitgebracht moeten al aan de GPAI-regels voldoen. ([EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/))

**Code of Practice voor AI-content labeling** (10 juni 2026): De Commissie heeft een draft gepubliceerd met verplichtingen voor het machine-readable markeren van AI-gegenereerde content. Professionele deployers moeten deepfakes en AI-teksten over publiek belang expliciet labelen. ([EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-first-draft-code-practice-marking-and-labelling-ai-generated-content))

**Consultatie hoog-risico AI-richtlijnen** is open tot 23 juni 2026 — een concrete actiekans voor organisaties die AI inzetten in gereguleerde sectoren. ([EC](https://digital-strategy.ec.europa.eu/en/news/commission-opens-consultation-draft-guidelines-ai-transparency-obligations))

**Wetenschappelijk panel van 60 experts** is per 1 juni aangesteld ter ondersteuning van de Europese AI Office bij handhaving. ([EC](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support))

---

## 🔐 Security & Risk

**AI comprimerert exploit-cyclus drastisch.** Anthropic's Claude Mythos ontdekte in samenwerking met ~50 partners meer dan 10.000 hoog- en kritiek-ernstige kwetsbaarheden in kritieke software binnen één maand — waaronder 181 werkende exploits voor Firefox. Dit is geen academische bevinding: de aanvalssnelheid in het veld neemt navenant toe. ([The Hacker News](https://thehackernews.com/2026/06/ai-broke-vulnerability-management-thats.html))

**Verizon DBIR 2026:** 32% van initial-access technieken exploiteert kwetsbaarheden; dit percentage stijgt naar verwachting door AI-gestuurde exploit-development. ([The Hacker News](https://thehackernews.com/2026/05/why-agentic-ai-is-securitys-next-blind-spot.html))

**Agentic AI als blind spot:** Brede permissies, ongecontroleerde deployments en lateral movement-risico's maken agentic AI-systemen tot het voornaamste nieuwe aanvalsoppervlak in enterprise. Shadow AI — niet-goedgekeurde tools met onveilige APIs of plugins — verergert het probleem. ([The Hacker News](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html))

---

## 📈 Markt & Adoptie

**Enterprise >40% van OpenAI's omzet**, op weg naar pariteit met consumentenomzet eind 2026. Klanten als Goldman Sachs, Philips en State Farm zijn recent aangehaakt. ([OpenAI](https://openai.com/index/next-phase-of-enterprise-ai/))

**Microsoft en Google domineren de enterprise AI-markt** volgens CIO Dive. OpenAI-producten komen nog steeds eerst op Azure, maar OpenAI levert nu ook aan alle andere cloud providers — wat de afhankelijkheid van Microsoft vermindert. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

**Multicloud is de nieuwe standaard:** Google-AWS samenwerking is actief; Microsoft sluit zich later in 2026 aan. Vendor lock-in is daarmee minder een argument voor afwachten. ([VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google))

**ROI-verwachting blijft laag:** C-suite executives verwachten pas over zes jaar of meer het volledige rendement op AI-investeringen te zien. Dit weerhoudt budgetten niet, maar vraagt wel om realistische propositie-framing richting klanten. ([CIO Dive](https://www.ciodive.com/news/microsoft-openai-rework-partnership/818606/))

---

## 💡 Ctac-relevantie

**Compliance-opdracht is concreet en urgent.** Met de volledige handhaving van de EU AI Act op 2 augustus 2026 moeten klanten van Ctac nu aantoonbaar hun hoog-risico AI-systemen in kaart hebben en de GPAI-verplichtingen nakomen. Dit is een directe dienstverlening­skans: AI Act readiness-scans, risicoregisters en documentatietrajecten zijn voor gereguleerde sectoren (overheid, finance, zorg) nu een acute behoefte, geen adviesoefening.

**Agentic AI vereist security-by-design.** De bevindingen over exploit-versnelling en shadow AI maken duidelijk dat Ctac bij elk agentisch AI-project een security assessment moet inbouwen. Dit geldt ook intern: gebruik van niet-goedgekeurde AI-tools door medewerkers creëert blootstelling die moeilijk te auditen is.

**Microsoft-autonomie verruimt het speelveld.** Nu Microsoft's AI-divisie los van OpenAI eigen modellen bouwt en uitrolt, wordt het voor Ctac relevant om de MAI-modellen te evalueren naast GPT-5.4 en Gemini 3 — met name voor klanten die al diep in het Microsoft-ecosysteem zitten (Azure, Copilot, M365). De ROI-onzekerheid bij C-suite biedt Ctac een opening: concrete, meetbare use-cases met korte terugverdientijd positioneren de AI-unit als pragmatisch partner, niet als innovatiepropaganda.

---

## 📚 Bronnen & verder lezen

- [OpenAI: GPT-5.4 introductie](https://openai.com/index/introducing-gpt-5-4/)
- [OpenAI: Ona acquisitie aankondiging](https://openai.com/news/company-announcements/)
- [OpenAI: Next phase of enterprise AI](https://openai.com/index/next-phase-of-enterprise-ai/)
- [Google: Gemini 3 introductie](https://blog.google/products-and-platforms/products/gemini/gemini-3/)
- [Google: Search IO 2026 updates](https://blog.google/products-and-platforms/products/search/search-io-2026/)
- [VentureBeat: Microsoft 7 MAI-modellen](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [VentureBeat: Microsoft "vrij" van OpenAI](https://venturebeat.com/technology/microsoft-ai-chief-says-company-was-set-free-from-openai-to-pursue-superintelligence)
- [CIO Dive: Microsoft en Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [EU AI Act tracker: implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC: Code of Practice AI-gegenereerde content](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-first-draft-code-practice-marking-and-labelling-ai-generated-content)
- [EC: Consultatie hoog-risico AI-richtlijnen](https://digital-strategy.ec.europa.eu/en/news/commission-opens-consultation-draft-guidelines-ai-transparency-obligations)
- [EC: AI Act enforcement wetenschappelijk panel](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support)
- [The Hacker News: AI broke vulnerability management](https://thehackernews.com/2026/06/ai-broke-vulnerability-management-thats.html)
- [The Hacker News: Why agentic AI is security's next blind spot](https://thehackernews.com/2026/05/why-agentic-ai-is-securitys-next-blind-spot.html)
- [The Hacker News: Shadow AI security risks](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html)
- [Hugging Face: Best open-source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
