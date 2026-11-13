---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-08
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 8 september 2026

## 🔑 Highlights van de dag

- **GPT-6 Astra is hier** — OpenAI's meest ambitieuze model tot nu toe rolde begin deze week uit (3 september), met als opvallendste feature autonome "computer use": het model navigeert een pc zoals een mens dat doet. CEO Greg Brockman noemde het potentieel de aankomst van AGI — een claim die om verifikatie vraagt, maar de richting is helder.
- **EU AI Omnibus van kracht** — Hoog-risico AI-systemen (Annex III) krijgen tot december 2027 de tijd. Maar: disclosure en labeling van generatieve output moest al per 2 augustus 2026. Wie dat gemist heeft, loopt nu risico.
- **Anthropic gooit Fable 5.1 op de markt** — Goedkoper én minder restrictief dan de vorige release. Combineer dit met Meta's Muse Glimmer (30B open-source, lokaal inzetbaar) en het is duidelijk: de access-drempel tot frontier-modellen daalt snel.
- **Prompt injection escaleert van proof-of-concept naar incident** — Drie AI-codeeragenten lekten geheimen via één geïnjecteerd prompt; een gepatchte Microsoft Copilot Studio-kwetsbaarheid bleek toch te exfiltreren. Enterprise AI-security is operationeel probleem, geen theorie meer.
- **Enterprise-adoptie op schaal** — 150.000 EY-medewerkers op Microsoft Copilot, NHS England rolt uit naar 500.000+ clinici. De vraag is niet meer óf, maar hoe snel en hoe veilig.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-6 Astra** (3 september) is OpenAI's grootste modelsprong ooit: getraind op meer dan 100.000 GPU's bij het Stargate-datacenter in Texas, met native "computer use"-functionaliteit voor autonome desktoptaken. API-prijs: $10/M input tokens, $50/M output tokens — duur, maar vergelijkbaar met wat GPT-4 kostte bij introductie. Cybersecurity-capabilities zijn bewust beperkt in de eerste release. ([Fortune](https://fortune.com/2026/09/03/openai-debuts-gpt-6-astra-computer-use-greg-brockman-says-start-of-agi/), [CNBC](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html))

**Anthropic Fable 5.1** (begin september) verlaagt kosten en versoepelt content-restricties ten opzichte van Fable 5. Beschikbaar via API en cloud-platforms. De prijsdaling bevestigt de bredere trend: geavanceerde reasoning is steeds toegankelijker. ([TechCrunch](https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/))

**Meta Muse Glimmer** — 30B-parameter multimodaal open-weight model (Apache 2.0), ontworpen voor lokale agentic deployment. Combineert een 2B vision encoder met een 28B text decoder. Interessant voor privacy-gevoelige toepassingen zonder cloud-afhankelijkheid. ([Hugging Face blog](https://huggingface.co/blog/muse-glimmer))

---

## 🏛️ Governance & Ethiek

**AI Omnibus in werking** (27 juli 2026) brengt gerichte versoepelingen van de AI Act: de deadline voor hoog-risico AI-systemen (Annex III — biometrie, kritieke infrastructuur, onderwijs, arbeidsmarkt, rechtshandhaving) is verschoven naar **2 december 2027**. De lichtere compliance-regels voor mkb zijn nu ook van toepassing op kleine midcap-bedrijven. ([Digital Strategy EC](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force))

**Cruciaal voorbehoud:** de verplichtingen rondom disclosure, labeling en herkomstmarkering van generatieve output golden **al per 2 augustus 2026** en zijn *niet* uitgesteld. Veel organisaties lijken dit te missen. ([ComplianceHub.Wiki](https://compliancehub.wiki/eu-digital-omnibus-ai-act-deadline-deferral-annex-iii-2027/))

**AI Office** is per 2 augustus 2026 operationeel voor handhaving en werft nu circa 40 contractagenten (sollicitatiedeadline: vandaag, 8 september). De toezichthouder heeft bevoegdheden om technische documentatie op te vragen, modellen te evalueren en boetes op te leggen. ([Artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/))

---

## 🔐 Security & Risk

**Prompt injection is nu operationeel risico.** Drie AI-codeeragenten lekten credentials via één injectiepunt; de aanval exploiteerde de fundamentele onmogelijkheid van LLM's om instructies van data te onderscheiden. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**Microsoft Copilot Studio CVE-2026-21520**: Microsoft patchte een prompt injection kwetsbaarheid, maar in onafhankelijke tests van Capsule Security bleek data alsnog te exfiltreren na de patch. Dit illustreert dat een CVE geen garantie is dat het risico ook effectief is gemitigeerd. ([VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook))

**Aanbeveling:** organisaties die agentic AI inzetten (met tool-access, RAG-pipelines of externe databronnen) dienen runtime-beveiligingslagen te implementeren — niet alleen op model-niveau maar ook op infrastructuur- en integratieniveau. ([Airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

---

## 📈 Markt & Adoptie

**Microsoft Copilot schaalt door:** EY rolt 365 Copilot uit naar 150.000 medewerkers met gemiddeld 15% productiviteitswinst; Atos (56.000 medewerkers, 54 landen) bouwt 19.000 AI-agents via Microsoft Foundry en Copilot Studio. NHS England bereikt 500.000+ clinici. Dit zijn geen pilots meer — dit is standaard bedrijfsoperatie. ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/))

**Google's Agentic Data Cloud** (gelanceerd op Google Cloud Next '26) is gericht op het omzetten van legacy dataplatforms naar AI reasoning engines. Bijbehorend Gemini Enterprise Agent Platform biedt orkestratie en governance voor grote agent-ecosystemen. ([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))

**Microsoft lanceerde eigen AI-modellen** — MAI-Transcribe-1, MAI-Voice-1 en MAI-Image-2 — beschikbaar via Microsoft Foundry. Dit reduceert Microsoft's afhankelijkheid van OpenAI voor specifieke use cases. ([VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google))

---

## 💡 Ctac-relevantie

**GPT-6 Astra + computer use:** de "computer use"-functionaliteit is direct relevant voor Ctac's klanten in de publieke sector en finance, waar documentverwerking en administratieve processen nog sterk manueel zijn. Ctac kan hier korte-termijn proposities op bouwen — denk aan geautomatiseerde formulierverwerking of batchverwerking van dossiers. Wel: de prijs ($50/M output tokens) maakt brede inzet vooralsnog duur; pilotscope is realistisch, productie-inzet vergt ROI-onderbouwing.

**AI Act Omnibus compliance:** klanten van Ctac die generatieve AI inzetten (chatbots, samenvattingen, co-pilots) hadden **per 2 augustus moeten voldoen** aan disclosure- en labelingverplichtingen. Dit is een concrete adviesbehoefte die de AI-unit nu kan adresseren: een snelle compliance-scan en implementatie van technische maatregelen (output-labeling, watermarking) is een haalbare propositie.

**Security bij agentic AI:** nu klanten AI-agents inzetten met tool-access (CRM, ERP, databronnen), wordt prompt injection een reëel risico in productieomgevingen. De AI-unit kan hier onderscheidend zijn door security-by-design standaard op te nemen in agent-architectuur-trajecten — niet als nagerecht maar als integraal onderdeel van de delivery.

---

## 📚 Bronnen & verder lezen

- [OpenAI GPT-6 Astra – Fortune](https://fortune.com/2026/09/03/openai-debuts-gpt-6-astra-computer-use-greg-brockman-says-start-of-agi/)
- [OpenAI GPT-6 Astra – CNBC](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)
- [Anthropic Fable 5.1 – TechCrunch](https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/)
- [Meta Muse Glimmer – Hugging Face Blog](https://huggingface.co/blog/muse-glimmer)
- [EU AI Omnibus in werking – EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force)
- [AI Act Omnibus deadlines – ComplianceHub.Wiki](https://compliancehub.wiki/eu-digital-omnibus-ai-act-deadline-deferral-annex-iii-2027/)
- [AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [Prompt injection enterprise AI – VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [AI coding agents secrets leak – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Microsoft Copilot Studio CVE – VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [AI security 2026 – Airia](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Microsoft FY26 AI adoptie – Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Microsoft eigen AI-modellen – VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
