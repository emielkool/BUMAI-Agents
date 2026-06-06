---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-06
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 6 juni 2026

## 🔑 Highlights van de dag

- **Microsoft lanceert 7 eigen AI-modellen bij Build 2026**, waaronder reasoning model MAI-Thinking-1 (35B parameters) dat in blindtests beter scoort dan Claude Sonnet. Microsoft treedt zo actief in competitie met zijn eigen AI-partner OpenAI.
- **Anthropic heeft confidentieel een IPO-aanvraag ingediend** bij een waardering van $965 miljard — hoger dan OpenAI. Claude Code wordt daarbij aangemerkt als de voornaamste groeimotor.
- **Simultane prompt injection-aanval** trof Claude Code, Gemini CLI én GitHub Copilot tegelijk; drie agents lekten secrets via één aanval. Agentic coding tools zijn een serieus aanvalsoppervlak geworden.
- **EU lanceert tech sovereignty package** (3 juni): AI Office krijgt meer bevoegdheden, sandboxes worden opengesteld voor MKB én kleine midcaps.
- **Twee-derde van bedrijven zit vast in AI pilot-fase**, terwijl Microsoft en Google hun enterprise-dominantie verder uitbouwen met Agent 365 en Agentic Data Cloud.

---

## 🧠 Technologie & Modellen

**Microsoft's eigen modelstack** — Bij Build 2026 introduceerde Microsoft zeven in-house modellen. De opvallendste: MAI-Thinking-1, een reasoning model met 35B actieve parameters en 256K contextvenster dat op SWE Bench Pro vergelijkbaar presteert met Claude Opus 4.6. Aanvullend: MAI-Image-2.5 (text-to-image en image-to-image) en MAI-Transcribe-1 (speech-to-text, 3,8% WER op FLEURS top-25 talen). De modellen zijn beschikbaar via Fireworks AI, Baseten en OpenRouter. Dit is strategisch: Microsoft was tot nu toe primair afhankelijk van OpenAI-modellen en bouwt nu een eigen laag. ([VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google))

**OpenAI verdiept platform** — Codex is nu breed beschikbaar voor elke rol en workflow (3 juni); frontier-modellen draaien op AWS (2 juni); GPT-Rosalind krijgt nieuwe capabilities voor life sciences-research (4 juni). Geen revolutionair nieuw model, maar een duidelijke focus op distributie en platform-verbreding. ([OpenAI](https://openai.com/news/product-releases/))

**Open source rijp voor productie** — Qwen3 235B-A22B (mixture-of-experts, Apache 2.0) leidt het open leaderboard. Hugging Face telt 13 miljoen gebruikers en 2 miljoen+ publieke modellen; open-weight modellen zijn in 2026 serieus inzetbaar voor coding, reasoning en multimodale taken in productie. ([Hugging Face](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026))

---

## 🏛️ Governance & Ethiek

**EU Tech Sovereignty Package (3 juni)** — De Europese Commissie presenteerde een pakket dat de AI Office-bevoegdheden versterkt, toezicht op GPAI-modellen centraliseert, en sandboxes openstelt voor bredere groepen innovators (inclusief kleine midcaps). De verschuiving van AI Act als 'compliance-last' naar 'innovatieframework' is relevant voor NL/BE klanten die tot nu toe afwachtten. ([EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

**Tijdlijn AI Act bevestigd** — High-risk toepassingen in biometrie en kritieke infrastructuur vallen onder verplichtingen vanaf december 2027; AI ingebouwd in producten (liften, medische devices) vanaf augustus 2028. Organisaties in NL en BE moeten hun compliance-roadmaps nu concreet plannen. ([EU AI Act tracker](https://artificialintelligenceact.eu/))

---

## 🔐 Security & Risk

**Prompt injection treft meerdere coding agents tegelijk** — Een aanval raakte Claude Code, Gemini CLI en Copilot gelijktijdig; drie agents lekten secrets via één prompt injection. Dit bevestigt OWASP LLM01 als actief risico: AI-agents met toolaccess zijn geen hypothetische dreiging meer. OpenAI erkent dat AI-browsers hier "mogelijk altijd kwetsbaar" voor blijven. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026), [Airia](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

**AI als offensief aanvalsmiddel** — Huidige Claude-modellen slagen voor multi-stage netwerkaanvallen op tientallen hosts met standaard open-source tools. De drempel voor AI-ondersteunde cyberaanvallen daalt snel; CISOs die inference-security nog als 'nice to have' zien, lopen achter. ([Schneier on Security](https://www.schneier.com/blog/archives/2026/01/ais-are-getting-better-at-finding-and-exploiting-security-vulnerabilities.html))

---

## 📈 Markt & Adoptie

**Anthropic op weg naar beursgang** — Anthropic diende confidentieel een IPO-aanvraag in bij een waardering van $965 miljard — hoger dan OpenAI. Claude Code wordt aangemerkt als voornaamste groeimotor. Een eventuele beursgang consolideert de 'big three' (OpenAI, Anthropic, Google) als permanente marktstructuur. ([CNBC](https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html))

**Microsoft Agent 365 algemeen beschikbaar** — Centrale registry en policy engine voor alle AI-agents in een enterprise (Copilot Studio, AWS Bedrock, SaaS-integraties, lokale agents). Shadow AI wordt hiermee beheersbaar. Beheer via Intune en Defender. ([VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat))

**SAP Business AI Platform** — SAP bundelt Business Technology, Data Cloud en AI onder één platform. Interessant voor SAP-klanten die AI willen integreren zonder complexe multi-cloud architecturen op te tuigen. ([CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/))

**Enterprise AI: Microsoft en Google domineren** — Gartner plaatst Microsoft (ecosysteem en productiviteitssoftware) en Google (agentic AI stack) bovenaan. Kritische noot: twee-derde van bedrijven zit nog in pilot-fase. Transitie naar productie is hét bottleneck van 2026. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

---

## 💡 Ctac-relevantie

**Direct aandacht vereist — prompt injection in coding agents:** Als Ctac Claude Code, Copilot of Gemini CLI inzet (intern of bij klanten), is dit een actueel risico. Evalueer runtime-security tools (bijv. Airia, Intune/Defender policies) en stel agent-policies in via Microsoft Agent 365 waar dat al beschikbaar is.

**Kans — Microsoft Agent 365 en SAP Business AI Platform:** Beide platformen bieden beheersbaarheid van enterprise AI-adoptie. Ctac kan direct waarde toevoegen als implementatiepartner voor klanten op Microsoft- of SAP-stack die shadow AI willen aanpakken en agent-governance willen inrichten.

**EU sandbox voor MKB en kleine midcaps:** De uitbreiding opent mogelijkheden voor Ctac-klanten om eerder te innoveren binnen een gereguleerde omgeving. Concrete propositie voor compliance-bewuste klanten in NL/BE: begeleid ze richting sandbox-deelname vóór december 2027-deadline.

**Strategische vraag — provider-alliantie:** Anthropic's IPO-filing bij ~$1T waardering en Microsoft's eigen modellaag veranderen de vendor-dynamiek. Afhankelijkheid van één provider wordt risicovoller. Ctac doet er goed aan nu een bewuste multi-provider strategie te formuleren.

---

## 📚 Bronnen & verder lezen

- [Microsoft Build 2026 – Microsoft Blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [Microsoft lanceert nieuwe AI-modellen – VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [OpenAI product releases juni 2026](https://openai.com/news/product-releases/)
- [Hugging Face: State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [EU AI Act governance – EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [AI agent runtime security & prompt injection – VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [AI Security 2026: Prompt Injection – Airia](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [AI exploiting security vulnerabilities – Schneier on Security](https://www.schneier.com/blog/archives/2026/01/ais-are-getting-better-at-finding-and-exploiting-security-vulnerabilities.html)
- [Microsoft en Google vs Anthropic en OpenAI in coding – CNBC](https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html)
- [Microsoft Agent 365 uit preview – VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [SAP Business AI Platform – CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [Microsoft/Google enterprise AI dominantie – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [LLM updates juni 2026 – LLM Stats](https://llm-stats.com/llm-updates)
