---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-19
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 19 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act live**: Vanaf 2 augustus zijn de transparantievereisten van kracht — chatbots moeten zich identificeren als AI, deepfakes krijgen verplicht een label. Europa heeft nu echte tanden op AI-handhaving.
- **Google Gemini 3.7 Flash**: Alweer een generatiestap in drie weken — coding benchmarks sprongen van 34% naar 44% (FrontierCode) en agentische automatisering van 17% naar 30%. De modelrace versnelt merkbaar.
- **OpenAI Ultrafast mode**: GPT-5.6 Sol draait via Cerebras nu op 750 tokens/seconde — 14× sneller dan standaard. Real-time agentic toepassingen worden plotseling heel realistisch.
- **Stripe koopt OpenRouter voor $7 mrd**: Stripe integreert zo routing over 400+ modellen voor 8 miljoen ontwikkelaars. Betalingsinfrastructuur en AI-infrastructuur groeien naar elkaar toe.
- **Prompt injection blijft nr. 1-risico**: CVE-2026-21520 in Microsoft Copilot Studio (CVSS 7.5) én een datalek van 1,5 miljoen API-tokens bij Moltbook tonen aan dat enterprise AI-agents structureel kwetsbaar zijn.

---

## 🧠 Technologie & Modellen

**Google Gemini 3.7 Flash** is uitgebracht — drie weken na 3.6 Flash. De coding score op FrontierCode steeg van 34,4% naar 43,6%, DeepSWE van 49% naar 65,3%, en AutomationBench van 17% naar 30,4%. Introductieprijs: $0,75/M input en $3,75/M output tot eind 2026. Dit zijn geen marginale verbeteringen — Google duwt snel.
*(Bron: [AI Weekly, aug. 2026](https://aiweekly.co/ai-news-today))*

**OpenAI Ultrafast mode** (API preview): GPT-5.6 Sol draait via Cerebras op ~750 output tokens/seconde — tot 14× sneller dan reguliere verwerking. Dit opent de deur naar echte real-time spraak- en agentische toepassingen.
*(Bron: [OpenAI Newsroom](https://openai.com/news/product-releases/))*

**Meta Muse Glimmer** is uitgebracht op Hugging Face: multimodaal, lokaal te draaien, ontworpen voor agentic use cases, 30B parameters, Apache 2.0 licentie. Tegelijk domineert China de open-source top: in vrijwel elke maand van 2026 was het grootste open model (tot 2,78 biljoen parameters) Chinees.
*(Bron: [Hugging Face Blog](https://huggingface.co/blog/muse-glimmer), [State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026))*

**OpenAI o3** wordt 26 augustus uit ChatGPT verwijderd — opgevolgd door GPT-5.4 mini, nu beschikbaar voor gratis gebruikers via de Thinking-functie.

---

## 🏛️ Governance & Ethiek

**EU AI Act transparantievereisten** zijn op 2 augustus 2026 van kracht geworden. Verplichtingen: (1) chatbots en interactieve AI-systemen moeten de gebruiker informeren dat ze met AI praten, (2) deepfakes moeten worden gelabeld. De AI Office en nationale autoriteiten hebben nu handhavingsbevoegdheden. Hoog-risico systemen krijgen extra tijd (Annex I tot augustus 2028, Annex III tot december 2027) dankzij de AI Omnibus-vereenvoudiging.
*(Bron: [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august))*

**White House-bijeenkomst** (3 augustus): het Witte Huis ontving OpenAI, Anthropic en andere top-AI-bedrijven voor een eerste grote reguleringsronde. Amerikaanse AI-regulering begint inhoud te krijgen.
*(Bron: [CNN Business](https://www.cnn.com/2026/08/03/tech/white-house-meet-with-top-ai-companies-big-regulation-push))*

---

## 🔐 Security & Risk

**CVE-2026-21520** (CVSS 7.5): Microsoft Copilot Studio bleek kwetsbaar voor indirecte prompt injection — ontdekt door Capsule Security, patch uitgerold 15 januari 2026. Een eerder lek bij Moltbook's agent-platform lekte 1,5 miljoen API-tokens in plaintext.

CrowdStrike's 2026 Threat Report documenteerde prompt injection aanvallen bij meer dan 90 organisaties in 2025. Conclusie: RAG-pipelines, agentic systemen en model routers zijn het nieuwe aanvalsoppervlak. Prompt injection bovenaan OWASP Top 10 voor LLM-applicaties is geen theorie meer — het is dagelijkse realiteit.
*(Bron: [VentureBeat Security](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers))*

---

## 📈 Markt & Adoptie

**Microsoft** domineert enterprise AI: 20M+ betaalde Copilot-seats, AI-business groeit 123% jaar-op-jaar naar $37 miljard omzetrun. Nieuw: **Microsoft Frontier Company** — een apart bedrijf met $2,5B investering en 6.000 experts voor enterprise AI-deployments. Microsoft verkoopt ook eigen MAI-modellen op eigen Maia-chips.
*(Bron: [TechCrunch](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/), [CIO Dive](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/))*

**Google** lanceerde eerder Agentic Data Cloud (Google Cloud Next '26): legacy enterprise data-platformen omgevormd tot reasoning engines voor AI-agents.

**Stripe + OpenRouter** ($7 mrd deal, 16 augustus): Stripe integreert model-routing voor 400+ modellen. Dit is infrastructuurconsolidatie — betalingen en AI-orkestratie in één hand.

Ondanks alles: **twee derde van bedrijven** zit nog vast in de pilot-fase en slaagt er niet in AI naar productie te brengen.
*(Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))*

---

## 💡 Ctac-relevantie

**EU AI Act nu actief** — Ctac-klanten die chatbots of generatieve AI inzetten moeten per direct voldoen aan transparantievereisten. Dit is een directe opdracht voor de AI-unit: compliance-scans aanbieden en klanten begeleiden bij implementatie van AI-labels en disclaimers.

**Prompt injection in enterprise agents** is geen edge case meer. Klanten die Copilot, custom RAG-oplossingen of agentic pipelines gebruiken lopen reëel risico. Ctac kan hier onderscheidend zijn door security-by-design als standaard op te nemen in AI-trajecten.

**Microsoft Frontier Company** is relevant als Ctac Microsoft-partner is: het vergroot Microsoft's directe enterprise-aanwezigheid, wat zowel een kans (co-delivery, kennistransfer) als concurrentiedruk (Microsoft gaat zelf implementeren) kan zijn.

**Twee derde van bedrijven zit vast in pilots** — dit is het speelveld voor Ctac. De markt heeft geen tekort aan AI-experimenten, maar aan begeleiding richting productie. Positioneer de AI-unit expliciet als productie-enabler, niet als een nieuwe experimenteerpartner.

**Meta Muse Glimmer** (open source, lokaal, agentic, Apache 2.0) is interessant voor klanten met data-privacy-eisen die geen cloud-LLM mogen gebruiken — denk overheid, zorg, finance.

---

## 📚 Bronnen & verder lezen

- [EC Digital Strategy – AI Act enforcement 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [AI Weekly – OpenAI & Google augustus 2026](https://aiweekly.co/ai-news-today)
- [OpenAI Newsroom – product releases](https://openai.com/news/product-releases/)
- [TechCrunch – Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [CIO Dive – Microsoft Copilot growth](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [VentureBeat – Prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [Hugging Face – State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [Hugging Face – Meta Muse Glimmer](https://huggingface.co/blog/muse-glimmer)
- [CNN Business – White House AI regulation](https://www.cnn.com/2026/08/03/tech/white-house-meet-with-top-ai-companies-big-regulation-push)
- [AIToolsRecap – AI News August 2026](https://aitoolsrecap.com/Blog/AINewsAugust2026.aspx)
