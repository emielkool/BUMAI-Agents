---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-02
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2 juli 2026

## 🔑 Highlights van de dag

- **Claude Sonnet 5 is live als standaard model** voor alle Free en Pro gebruikers (geldig per 1 juli). Het is de meest agentische Sonnet tot nu toe — vergelijkbaar met Opus 4.8 op veel taken, maar significant goedkoper. Dit verlaagt de drempel voor enterprise agentic AI aanzienlijk.
- **Anthropic's Fable 5 en Mythos 5 wereldwijd terug beschikbaar** na een drie weken durend Amerikaans exportverbod. De VS heeft de licentieverplichting per 30 juni opgeheven — een teken dat geopolitieke AI-exportpolitiek real-time impact heeft op enterprise toegang.
- **OpenAI GPT-5.6 lijn blijft beperkt beschikbaar** (Sol, Terra, Luna) — de Trump-administratie houdt toegang beperkt tot pre-goedgekeurde overheids- en commerciële partners. De race aan de modelfront gaat door, maar toegang is niet langer vanzelfsprekend.
- **EU AI Act is over één maand volledig van kracht** (2 augustus 2026). Met name voor biometrie, kritieke infrastructuur en HR-toepassingen geldt nu de volle complianceplicht. Ctac-klanten in die sectoren moeten nú actie ondernemen.
- **Twee derde van bedrijven zit vast in AI-pilotfase** — ze komen niet door naar productie. Dat is geen hype: het is een structureel implementatieprobleem waar Ctac direct op kan inspringen.

---

## 🧠 Technologie & Modellen

**Claude Sonnet 5 (Anthropic, 30 juni/1 juli)** is beschikbaar als standaard voor alle abonnementen. Het model is sterk verbeterd op reasoning, tool use, computer use en multi-stap agentic taken. Introductieprijs: $2 / $10 per miljoen tokens (in- en output) tot en met 31 augustus, daarna $3 / $15. Vergelijkbare kwaliteit als het zwaardere Opus 4.8 voor de meeste taken, maar een stuk voordeliger. Relevante primeur voor bedrijven die agentic workflows willen uitrollen.
→ [Anthropic: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) | [TechCrunch](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)

**Claude Fable 5 en Mythos 5** zijn per 1 juli wereldwijd opnieuw toegankelijk na het opheffing van Amerikaanse exportcontroles. Achtergrond: de VS voegde deze modellen op 12 juni toe aan de exportcontrolelijst vanwege zorgen over cybersecuritytoepassingen. Na Aziatische concurrentie (Fugu, Tulongfeng die Mythos-niveau benaderen) en diplomatieke druk, hief de VS de maatregel op. Anthropic heeft beloofd actief malafide gebruik te monitoren en de overheid te informeren.
→ [TechCrunch](https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/) | [VentureBeat](https://venturebeat.com/technology/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it)

**Open-source landschap** oogt sterk: GLM-5 staat #1 op open-weight modellen in de LMArena tekstranking (77,8% SWE-bench Verified), en Kimi K2.6 (1,1T parameters) scoort toonaangevend op coding en agentic use cases. De open-sourcemodellen naderen proprietary-niveau; het zelfhostende alternatief wordt steeds volwassener.
→ [Hugging Face blog: GLM-5](https://huggingface.co/blog/mlabonne/glm-5) | [Hugging Face: State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)

---

## 🏛️ Governance & Ethiek

**EU AI Act: T-minus 31 dagen.** Per 2 augustus 2026 is de verordening volledig van kracht voor high-risk AI-systemen in biometrie, kritieke infrastructuur, onderwijs, HR, migratie en grensbeheer. (Uitzondering: voor een subset van deze systemen is de deadline verschoven naar 2 december 2027 na het "AI Omnibus" politiek akkoord van 7 mei.) Élke lidstaat moet per 2 augustus tevens minimaal één nationale AI regulatory sandbox operationeel hebben.
→ [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/) | [Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Trump-executief bevel AI (2 juni 2026)** roept federale agencies op tot benchmarking en capability-assessment van nieuwe modellen vóór release. Dit is het beleidskader achter de GPT-5.6-beperking en de Fable/Mythos-episode. Het signaal: de VS stuurt actief op AI-exportbeleid als geopolitiek instrument.
→ [White House EO](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)

---

## 🔐 Security & Risk

**Prompt injection blijft de structurele zwakte van agentic AI.** De aanvalstechniek heeft zich in 2026 verder ontwikkeld en richt zich nu op multi-agent architecturen, RAG-pipelines en model routers. Drie AI-codeeragenten lekten secrets via één prompt injection aanval; Microsoft's Copilot Studio kreeg CVE-2026-21520 (CVSS 7.5) toegewezen voor een indirect prompt injection-kwetsbaarheid. Patches zijn beschikbaar, maar de kern van het probleem — modellen onderscheiden instructies en data niet betrouwbaar — is structureel en onopgelost.
→ [VentureBeat: Prompt Injection Enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers) | [VentureBeat: Copilot Studio CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)

**Five Eyes-waarschuwing:** de inlichtingenalliantie van VS, VK, Canada, Australië en Nieuw-Zeeland heeft overheden en bedrijven wereldwijd gewaarschuwd dat AI-gedreven cyberaanvallen op maandenschaal op komst zijn. Dit verhoogt de urgentie voor AI security frameworks bij overheidsklanten.

---

## 📈 Markt & Adoptie

**Microsoft M365 prijsverhoging van 16% per juli 2026**, als gevolg van de uitbreiding van het AI-aanbod in de Microsoft 365-suite. Dit is geen verrassing maar heeft directe budgetimpact voor Ctac-klanten.
→ [CIO Dive](https://www.ciodive.com/news/microsoft-365-ai-tools-higher-price/807189/)

**Google Cloud passeert $20 miljard omzet** in Q1 2026 (+63% YoY). Microsoft en AWS kondigen gezamenlijk meer dan $500 miljard capex aan voor AI-infrastructuur in FY2026. De hyperscalers rijden door — het gaat niet om hype maar om concrete infrastructuuruitbreiding.
→ [CIO Dive: Google Cloud](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)

**Twee derde van bedrijven zit vast in AI-pilotfase** — ze slagen er niet in generatieve AI van pilot naar productie te brengen. Executives verwachten slechts 27% ROI op korte termijn. Dit is het meest actuele signaal dat de adoptiekloof breed en reëel is.
→ [CIO Dive: Enterprise software spend](https://www.ciodive.com/news/ai-spend-inflates-enterprise-software-budgets-west-monroe/760662/)

**Microsoft-OpenAI partnerschap heronderhandeld** naarmate cloud-flexibiliteit groeit: OpenAI's modellen zijn nu beschikbaar via meerdere clouds, niet meer exclusief via Azure.
→ [CIO Dive](https://www.ciodive.com/news/microsoft-openai-rework-partnership/818606/)

---

## 💡 Ctac-relevantie

**Directe actie vereist: EU AI Act (2 augustus).** Ctac-klanten in sectoren als overheid, HR-tech, en kritieke infrastructuur hebben nog 31 dagen om high-risk AI-systemen compliant te maken of gebruik tijdelijk te staken. Dit is een concrete adviesopdracht die nu verkoopbaar is.

**De pilot-naar-productie kloof is Ctac's kans.** Twee derde van bedrijven haalt geen productie-niveau; dit bevestigt dat technologie niet het probleem is, maar implementatie, governance en change management. Ctac kan zich positioneren als de partij die AI-initiatieven daadwerkelijk landt — niet als modelleverancier, maar als implementatiepartner die ook het organisatorische traject begeleidt.

**Claude Sonnet 5 verlaagt de agentic AI-drempel aanzienlijk.** De combinatie van Opus 4.8-niveau intelligentie op Sonnet-prijs maakt het economisch haalbaar om agentic workflows in te zetten voor grotere klantvolumes. Voor Ctac's AI-unit is dit het moment om agentic prototypes te versnellen en in productie te brengen.

**Microsoft prijsverhoging als gespreksopener.** De 16% kostenstijging op M365 biedt een natuurlijk instappunt voor klantgesprekken over AI-governance, alternatieve tooling of optimale inzet van de nu duurdere Microsoft AI-suite.

---

## 📚 Bronnen & verder lezen

- [Anthropic: Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)
- [TechCrunch: Anthropic Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [TechCrunch: Trump drops restrictions on Fable/Mythos](https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/)
- [VentureBeat: Fable 5 globally restored](https://venturebeat.com/technology/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Europese Commissie: AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [White House EO AI Innovation & Security](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)
- [VentureBeat: Prompt Injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat: Copilot Studio CVE-2026-21520](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [CIO Dive: Microsoft/Google dominate enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive: Microsoft 365 prijsverhoging](https://www.ciodive.com/news/microsoft-365-ai-tools-higher-price/807189/)
- [CIO Dive: Google Cloud >$20B](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [Hugging Face: State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Hugging Face: GLM-5](https://huggingface.co/blog/mlabonne/glm-5)
