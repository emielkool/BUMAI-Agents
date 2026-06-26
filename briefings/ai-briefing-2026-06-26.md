---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-26
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 26 juni 2026

## 🔑 Highlights van de dag

- **White House legt OpenAI GPT 5.6 aan banden:** De Trump-administratie heeft OpenAI gevraagd het nieuwe model voorlopig niet breed te releasen — toegang wordt "klant voor klant" door de overheid goedgekeurd. Ongekende overheidsbemoeienis met AI-productontwikkeling die precedent zet.
- **EU AI Act high-risk deadline verschoven naar december 2027:** Via het Digital Omnibus-akkoord van 7 mei is de Annex III-deadline (hoog-risico AI-systemen) met 16 maanden uitgesteld. Geeft bedrijven meer lucht, maar vraagt om strategische doelgerichtheid — compliance-uitstel is geen excuus voor stilstand.
- **Prompt injection op OWASP-positie #1 met 340% meer aanvallen:** CVE-2025-53773 (GitHub Copilot RCE via PR-beschrijvingen, CVSS 9.6) en EchoLeak in Microsoft 365 Copilot tonen aan dat agentic AI-tools een serieuze aanvalsoppervlakte vormen.
- **Anthropic dient IPO-aanvraag in bij ~$1 biljoen waardering** en kondigt compute-partnerschap aan met Google en Broadcom voor "meerdere gigawatts" aan AI-infrastructuur — een signaal over de benodigde investeringsschaal.
- **Microsoft M365 Copilot SKU's worden permanent per 1 juli 2026:** Business Standard en Business Premium met Copilot zijn voortaan vaste productconfiguraties — relevant voor iedere klant met een M365-licentie.

---

## 🧠 Technologie & Modellen

**OpenAI GPT 5.6 op hold door White House-bemoeienis**
TechCrunch berichtte op 25 juni dat de Trump-administratie OpenAI heeft verzocht zijn nieuwste model niet open te releasen. CEO Sam Altman zou intern hebben gecommuniceerd dat de overheid "klant voor klant" toegang zal goedkeuren. Dit is een opmerkelijk precedent voor overheidscontrole over frontier-modellen en kan gevolgen hebben voor de Europese beschikbaarheid.
*(Bron: [TechCrunch, 25 juni 2026](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/))*

**Agentic AI overstijgt LLMs als dominante onderzoekscategorie**
Op ICLR 2026 was agentic AI het meest besproken onderwerp: multi-agent-systemen waarbij gespecialiseerde agents parallel werken, met een "agent harness" voor coördinatie, state en memory. Omni-modale modellen zoals SAM 3 integreren vision, audio en video in één latente ruimte.
*(Bron: [Encord – ICLR 2026 Trends](https://encord.com/iclr-2026/))*

**Microsoft MAI-modellen en Anthropic Opus 4.8**
Microsoft lanceerde op Build 2026 (2-3 juni) MAI-Code-1-Flash (code-generatie) en MAI-Thinking-1 (redeneermodel, lage tokenkosten). Anthropic bracht op 28 mei Opus 4.8 uit met een "dynamic workflow"-tool. Juni 2026 is de drukste modelreleasemaand van het jaar.
*(Bronnen: [CNBC – Microsoft modellen](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html), [TechCrunch – Opus 4.8](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/))*

---

## 🏛️ Governance & Ethiek

**EU AI Act: high-risk deadline verschoven naar december 2027**
Via het Digital Omnibus-akkoord van 7 mei 2026 is de Annex III-deadline (o.a. HR-tools, kredietscoring, kritieke infrastructuur) uitgesteld van 2 augustus 2026 naar 2 december 2027. GPAI-regels en verboden praktijken zijn al van kracht. De Europese AI Office versterkt haar positie als centrale toezichthouder; governance-fragmentatie wordt beperkt.
*(Bronnen: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/), [LegalNodes](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks))*

**Five Eyes + VS: "Careful Adoption of Agentic AI Services"**
De cyberveiligheidsdiensten van VS, Australië, Canada, Nieuw-Zeeland en VK publiceerden gezamenlijk een guidancedocument over veilige inzet van agentic AI in kritieke infrastructuur. Vijf risicocategorieën worden onderscheiden: privilege, ontwerp/configuratie, gedrag, structureel en accountability.
*(Bron: [DARPA AI Forge / CISA guidance](https://www.darpa.mil/news/2026/ai-forge-accelerating-ai-breakthroughs-national-security))*

---

## 🔐 Security & Risk

**Prompt injection: #1 AI-bedreiging van 2026**
Aanvallen namen met 340% toe jaar-op-jaar. Twee kritieke CVE's illustreren de ernst:
- **CVE-2025-53773** (CVSS 9.6): verborgen prompt injection in GitHub Copilot-PR-beschrijvingen leidde tot remote code execution.
- **EchoLeak (CVE-2025-32711)**: zero-click aanval in Microsoft 365 Copilot waarbij een kwaadaardige e-mail Copilot liet bijlagen exfiltreren naar externe servers bij een simpele inbox-samenvatting.

Unit 42 documenteerde in maart 2026 de eerste grootschalige indirecte prompt injection-aanvallen in productieomgevingen. Agentic systemen zijn extra kwetsbaar omdat succesvolle injectie reële acties triggert, niet slechts misleidende tekst.
*(Bronnen: [Help Net Security](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/), [Airia](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))*

---

## 📈 Markt & Adoptie

**Anthropic op weg naar beursgang bij ~$1 biljoen**
Anthropic diende vertrouwelijk een IPO-aanvraag in en kondigde tegelijkertijd een uitbreiding aan van zijn compute-partnerschap met Google en Broadcom voor "meerdere gigawatts" rekenkracht. Toponderzoeker John Jumper (voormalig Google DeepMind Nobel-laureaat) stapte over naar Anthropic — het AI-talent stroomt weg bij Google.
*(Bronnen: [TechCrunch – IPO](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/), [Anthropic – Google/Broadcom partnership](https://www.anthropic.com/news/google-broadcom-partnership-compute))*

**Microsoft M365 Copilot permanent en AI-governance mainstream**
Vanaf 1 juli worden Business Standard en Business Premium met Copilot vaste SKU's. Microsoft Agent 365 en Googles AI control center voor Workspace worden door CIO's en CISO's gezien als de standaard voor enterprise AI-governance. AI is geen pilot meer — governance is de volgende uitdaging.
*(Bronnen: [Microsoft Learn – June 2026 announcements](https://learn.microsoft.com/en-us/partner-center/announcements/2026-june), [CIO.com](https://www.cio.com/article/4167059/microsoft-google-push-ai-agent-governance-into-enterprise-it-mainstream-2.html))*

**AI-adoptie Nederland verdubbeld: 67% van bedrijven gebruikt nu AI**
In drie jaar is het percentage Nederlandse bedrijven dat AI inzet gestegen van 34% (2023) naar 67% (2026). De markt is duidelijk rijp, maar de kloof tussen grote en kleine bedrijven blijft zichtbaar. De volgende golft is agentic AI, ook in NL/BE.
*(Bron: [Searchlab.nl](https://searchlab.nl/blog/ai-adoptie-nederland-2026))*

**Meta herstructureert richting AI: 8.000 ontslagen, 7.000 herplaatst**
Meta voert een AI-gedreven reorganisatie door: ~10% van het personeel verliest zijn baan, terwijl 7.000 medewerkers worden herplaatst naar AI-teams. Qualcomm onderhandelt over overname van Tenstorrent ($8–10 miljard) voor AI-chipinfrastructuur op RISC-V-basis.

---

## 💡 Ctac-relevantie

**Direct actie vereist per 1 juli — M365 Copilot SKU-wijziging:**
Microsoft maakt Business Standard en Business Premium met Copilot permanent per 1 juli. Voor Ctac-klanten die nu M365-licenties hebben zonder Copilot is dit het moment om de propositie aan te scherpen. Copilot-onboarding (governance, training, use-case-selectie) is een concrete dienst die nu relevant is.

**EU AI Act uitstel = geen vrijheid, maar focus:**
De verschuiving van de Annex III-deadline naar december 2027 geeft Ctac en haar klanten extra tijd, maar wie nu begint met AI-risicoclassificatie en governance-frameworks, loopt straks voor op concurrenten die afwachten. Ctac kan hier als trusted advisor optreden.

**Prompt injection-risico in enterprise Copilot-omgevingen:**
CVE-2025-53773 en EchoLeak zijn geen academische kwetsbaarheden — ze treffen Microsoft 365 Copilot en GitHub Copilot die Ctac en haar klanten actief gebruiken. Een security-check op Copilot-configuraties (permissies, data-toegang, agent-scope) is een concrete aanbeveling richting klanten.

**Agentic AI-vraag groeit in NL-markt:**
67% AI-adoptie in Nederland en de verschuiving naar agentic systemen betekent dat klanten vragen om meer dan proof-of-concepts. Ctac's AI-unit kan differentiëren door multi-agent-architecturen, governance-tooling en security-by-design te bundelen als end-to-end implementatiedienst.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – White House vraagt OpenAI GPT 5.6 te vertragen (25 jun)](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/)
- [TechCrunch – Anthropic IPO-aanvraag](https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/)
- [Anthropic – Google & Broadcom compute-partnerschap](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- [TechCrunch – Anthropic Opus 4.8 met dynamic workflow](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/)
- [CNBC – Microsoft MAI-modellen (2 jun)](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)
- [artificialintelligenceact.eu – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [LegalNodes – EU AI Act 2026 compliance updates](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [Help Net Security – OWASP prompt injection top-1 (11 jun)](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [Airia – Prompt injection & the lethal trifecta 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO.com – Microsoft & Google AI agent governance enterprise](https://www.cio.com/article/4167059/microsoft-google-push-ai-agent-governance-into-enterprise-it-mainstream-2.html)
- [Microsoft Learn – June 2026 announcements](https://learn.microsoft.com/en-us/partner-center/announcements/2026-june)
- [Searchlab.nl – AI adoptie Nederland 2026](https://searchlab.nl/blog/ai-adoptie-nederland-2026)
- [Encord – ICLR 2026 Trends: Agentic AI & Multimodal](https://encord.com/iclr-2026/)
- [LLM Stats – AI model updates juni 2026](https://llm-stats.com/llm-updates)
