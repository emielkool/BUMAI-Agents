---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-27
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 27 juni 2026

## 🔑 Highlights van de dag

- **GPT-5.6 (Sol/Terra/Luna) gelanceerd maar geblokkeerd door de VS-overheid.** OpenAI bracht drie nieuwe modellen uit, maar het Witte Huis dwingt een gecontroleerde, klant-voor-klant rollout af op grond van een executive order van 2 juni. Ongekend signaal: overheidsingrijpen in AI-releases wordt normaal.
- **Claude Fable 5 publiek, maar ook export-gecontroleerd.** Anthropic's krachtigste model is nu beschikbaar voor het publiek, maar de VS heeft ook hierop exportbeperkingen ingesteld — een patroon dat zich lijkt te herhalen bij frontier-modellen.
- **Gaslight-malware gebruikt prompt injection tegen AI-beveiligingstooling op macOS.** Aanvallers misbruiken AI-gestuurde analysetools door fabricated systeem-messages te injecteren, waardoor securityagents hun analyse afbreken. Direct relevant voor teams die AI inzetten bij security operations.
- **EU AI Act: vijf weken tot volledige toepassing (2 augustus 2026).** De deadlines zijn niet verschoven — bedrijven die nog geen risicoanalyse hebben, lopen nu echt achter.
- **Enterprises concentreren AI-budget: meer geld, minder leveranciers.** Twee derde zit nog in pilot-fase; wie wél naar productie schaalt, kiest één of twee platforms in plaats van te verspreiden over velen.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6: Sol, Terra en Luna — beperkte preview**
OpenAI onthulde een nieuwe generatie modellen: Sol (flagship), Terra (gebalanceerd) en Luna (snel/goedkoop). De bredere release is geblokkeerd door de Trump-administratie, die eist dat overheidsinstanties de modellen eerst benchmarken op veiligheid. CEO Sam Altman bevestigde dat toegang per klant wordt goedgekeurd; een algemene release wordt "een paar weken later" verwacht. Dit is geen technische maar een politieke rem — en het is een precedent. ([TechCrunch](https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/), [VentureBeat](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov))

**Claude Fable 5: Anthropic's publieke frontier-model**
Fable 5 is de publiek toegankelijke versie van Mythos 5 en scoort sterk op softwareontwikkeling, kenniswerk en vision. In high-risk domeinen (cybersecurity, biologie, chemie) zijn harde beperkingen ingebouwd. Ook dit model valt nu onder VS-exportcontroles, wat toegang buiten de VS bemoeilijkt. Anthropic bereikte inmiddels een omzet van $30 miljard run rate na 80x groei en haalde een Series H van $65 miljard op bij een waardering van $965 miljard. ([TechCrunch Fable 5](https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/), [Anthropic newsroom](https://www.anthropic.com/news))

**Anthropic compute-deal met Google en Broadcom**
Een eerder gesloten akkoord legt vast dat Anthropic toegang krijgt tot 3,5 gigawatt TPU-capaciteit vanaf 2027 — grotendeels op VS-bodem. Dit positioneert Anthropic als zelfstandige compute-speler naast de hyperscalers. ([Anthropic](https://www.anthropic.com/news/google-broadcom-partnership-compute))

---

## 🏛️ Governance & Ethiek

**EU AI Act: vijf weken tot volledige toepassing**
Op 2 augustus 2026 treedt de AI Act volledig in werking (op enkele uitzonderingen na). Tegelijkertijd moeten lidstaten voor die datum minimaal één nationale AI-sandbox hebben opgericht. Recente hervormingen versterken de rol van het AI Office en verbreden de vereenvoudigde regels naar "small mid-cap" bedrijven. ([Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement), [artificialintelligenceact.eu](https://artificialintelligenceact.eu/))

**Cloud and AI Development Act (CADA) voorgesteld**
De Europese Commissie heeft een voorstel ingediend voor de CADA, gericht op versterking van cloud- en AI-infrastructuur in Europa. Dit is Brussel's antwoord op de concentratie van compute bij de Amerikaanse hyperscalers. ([EC digitale strategie](https://digital-strategy.ec.europa.eu/en/library/proposal-cloud-and-ai-development-act-cada))

**VS: executive order dwingt AI-safety benchmarking bij releases**
Trump tekende op 2 juni een executive order waarmee federale instanties betrokken worden bij het beoordelen van nieuwe frontier-modellen vóór release. De GPT-5.6-casus laat zien dat dit al in werking is. Dit is minder een veiligheidsraamwerk dan een controle-instrument — maar de precedentwerking is reëel. ([TechCrunch](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/))

---

## 🔐 Security & Risk

**Gaslight-malware: prompt injection als wapen tegen AI-securitytools**
Nieuw ontdekte macOS-malware ("Gaslight") injecteert nep-systeemberichten in AI-gestuurde beveiligingsanalyses, waardoor securityagents hun analyse vroegtijdig afbreken. Dit is een gerichte aanval op het vertrouwen in AI als security-layer — precies op het moment dat veel teams AI-gestuurde detection & response uitrollen. ([The Hacker News](https://thehackernews.com/2026/06/new-gaslight-macos-malware-uses-prompt.html))

**Drie AI-codeeragents lekten secrets via prompt injection**
Een audit toonde aan dat drie gangbare AI-codeeragents gevoelige secrets blootlegden via prompt injection. De kwetsbaarheid zit deels in onvoldoende hardening van GitHub Actions-integraties. Aanbeveling: beperk de GITHUB_TOKEN scope, gebruik environment protection rules en first-time-contributor gates. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**Cijfers: 94,4% van LLM-agents kwetsbaar voor prompt injection**
Uit recent onderzoek blijkt dat vrijwel alle state-of-the-art LLM-agents kwetsbaar zijn voor prompt injection, 83% voor retrieval-based backdoors, en 100% voor interagent trust exploits. Wie agents in productie brengt zonder runtime-beveiligingslaag, speelt Russische roulette. ([arXiv](https://arxiv.org/pdf/2602.10465))

---

## 📈 Markt & Adoptie

**Microsoft en Google domineren enterprise AI; hyperscalers investeren $500 miljard+**
Microsoft en Google bezetten de top van de enterprise AI-markt — Microsoft via zijn ecosysteem en partnernetwerk, Google via agentische AI-integraties. De drie grote hyperscalers investeren gezamenlijk meer dan $500 miljard in AI-infrastructuur in FY2026. AWS maakte recent $10 miljard los voor data centers in North Carolina. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

**Twee derde enterprises zit vast in pilot-fase**
Ondanks de investeringsgolf slaagt het merendeel van de enterprises er niet in GenAI van proof-of-concept naar productie te brengen. Budgetten groeien wel: AI-gerelateerde uitgaven zijn bijna 25% van het totale IT-budget, en verwacht wordt dat dit in 2026 met 9% stijgt — maar geconcentreerd bij minder leveranciers. ([VentureBeat GPU utilization](https://venturebeat.com/infrastructure/5-gpu-utilization-the-401-billion-ai-infrastructure-problem-enterprises-cant-keep-ignoring), [TechCrunch VCs](https://techcrunch.com/2025/12/30/vcs-predict-enterprises-will-spend-more-on-ai-in-2026-through-fewer-vendors/))

**Anthropic overtreft OpenAI in business AI-adoptie**
In enterprise-adoptie heeft Anthropic voor het eerst OpenAI ingehaald. Drie risico's bedreigen die positie: toenemende concurrentie, exportbeperkingen op frontier-modellen, en afhankelijkheid van Google's compute-infrastructuur. ([VentureBeat](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead))

---

## 💡 Ctac-relevantie

**EU AI Act: nu is het serieus.** Met de deadline van 2 augustus vijf weken weg, is dit het moment voor Ctac om klanten actief te adviseren over AI-risicoklassificatie en compliance-eisen. Klanten in gereguleerde sectoren (overheid, zorg, finance) die nog geen risicoanalyse hebben, lopen reëel compliance-risico. Dit is een directe propositie-kans voor de AI-unit: help klanten hun AI-inventaris inzichtelijk maken en classificeren.

**Prompt injection in agentische systemen: waarschuwing voor lopende projecten.** De combinatie van Gaslight-malware en de gelekte AI-codeeragents laat zien dat agent-security geen afterthought meer kan zijn. Voor Ctac-projecten waarin AI-agents worden ingezet (code review, automatisering, RAG-toepassingen) is het verstandig nu een expliciete security-review in te plannen — zeker als die agents toegang hebben tot API-keys of interne systemen.

**Vendor-consolidatie bij enterprise: kies een verhaal.** Enterprises kiezen voor minder maar diepere AI-partnerrelaties. Ctac kan hierop inspelen door een duidelijk standpunt in te nemen over het eigen AI-platform-oordeel (Microsoft Copilot-stack vs. Anthropic/Claude via API), in plaats van voor elke klant opnieuw een open selectie te starten. Dat versnelt de sales-cyclus en vergroot de herbruikbaarheid van IP.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI limits GPT-5.6 rollout after government request](https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/)
- [VentureBeat – OpenAI unveils GPT-5.6 Sol, Terra and Luna models](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)
- [TechCrunch – The White House is asking OpenAI to slow roll the release](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/)
- [TechCrunch – Anthropic releases Claude Fable 5](https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/)
- [Anthropic – Google & Broadcom compute partnership](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- [Anthropic – Series H $65B funding](https://www.anthropic.com/news/series-h)
- [VentureBeat – Anthropic $30B revenue run rate](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth)
- [The Hacker News – Gaslight macOS malware prompt injection](https://thehackernews.com/2026/06/new-gaslight-macos-malware-uses-prompt.html)
- [VentureBeat – AI agent runtime security audit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [arXiv – Authenticated Workflows: protecting agentic AI](https://arxiv.org/pdf/2602.10465)
- [CIO Dive – Microsoft, Google rule AI vendor market for enterprises](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [VentureBeat – 5% GPU utilization: the $401B AI infrastructure problem](https://venturebeat.com/infrastructure/5-gpu-utilization-the-401-billion-ai-infrastructure-problem-enterprises-cant-keep-ignoring)
- [VentureBeat – Anthropic beats OpenAI in business AI adoption](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)
- [Europese Commissie – AI Act governance and enforcement](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [artificialintelligenceact.eu – Implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [Europese Commissie – Cloud and AI Development Act (CADA)](https://digital-strategy.ec.europa.eu/en/library/proposal-cloud-and-ai-development-act-cada)
- [TechCrunch – Trump signs executive order on AI oversight](https://techcrunch.com/2026/06/02/trump-signs-narrower-executive-order-on-ai-oversight-after-industry-objections/)
