---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-04
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 4 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act Artikel 50 is nu van kracht** – Sinds 2 augustus geldt de transparantieverplichting: chatbots moeten zichzelf kenbaar maken als AI en gegenereerde media moet machineleesbaar worden gemarkeerd. Handhaving is actief, boetes tot €15 miljoen of 3% van de wereldwijde omzet.
- **78% van bedrijven nog niet compliant** – De meeste organisaties hebben de Article 50-verplichtingen nog niet volledig geïmplementeerd, wat zowel juridisch risico als een adviesmarkt creëert.
- **Prompt injection als #1 AI-security dreiging** – Aanvallen zijn met 340% gestegen; OWASP bevestigt dat het probleem architectureel onopgelost blijft. Kritieke CVEs gevonden in Copilot, GitHub Copilot en Cursor IDE.
- **Cloud AI verschuift van modellen naar operatie** – Google, AWS en Microsoft verschuiven hun focus van modelwedloop naar het bouwen van verticaal geïntegreerde AI-stacks voor enterprises.
- **Modellandschap consolideert** – Claude Opus 5, GPT-5.6 (Sol/Terra/Luna), DeepSeek V4-Flash en Gemini 3.6 Flash domineren de bovenkant; de BenchLM leaderboard werd op 3 augustus bijgewerkt.

---

## 🧠 Technologie & Modellen

Het modellandschap is actief maar begint te consolideren. **Claude Opus 5** (Anthropic, 24 juli) is het nieuwe vlaggenschip: bijna op het niveau van Claude Fable 5 maar circa de helft goedkoper, met een instelbare "effort dial" voor cost-capabilityafweging. **GPT-5.6** van OpenAI is uitgegroeid tot een drielaagse lijn (Sol = meest capabel, Terra = mid-tier, Luna = goedkoopst); Luna kreeg op 30 juli een prijsverlaging. **DeepSeek V4-Flash-0731** (31 juli) is de zoveelste efficiënte Chinese release die frontier-prestaties levert tegen lagere kosten.

Nieuw is het **GDPval-benchmark** van OpenAI, dat prestatievergelijkingen over 44 kenniswerktaken in 9 economische sectoren biedt. Dit is relevanter voor enterprise-inkoop dan traditionele academische benchmarks — maar ook dit soort benchmarks verdient scepticisme: ze worden vaak gemaakt door de partijen die er baat bij hebben.

**Bron:** [llm-stats.com](https://llm-stats.com/llm-updates), [benchlm.ai](https://benchlm.ai/), [felloai.com](https://felloai.com/best-ai-models/)

---

## 🏛️ Governance & Ethiek

De meest concrete deadline in tijden: **2 augustus 2026 markeert het begin van actieve handhaving van EU AI Act Artikel 50**. De verplichtingen zijn:

1. **Chatbots** moeten zichzelf als AI identificeren aan gebruikers.
2. **AI-gegenereerde media** (beeld, audio, video, tekst) moet machineleesbaar worden gemarkeerd — C2PA Content Credentials is de aanbevolen standaard.
3. **Emotieherkenning** vereist actieve gebruikersinformering.

De strengere high-risk verplichtingen (Annex III: recruitment, krediet, etc.) zijn door de Digital Omnibus uitgesteld naar december 2027. Dat geeft uitstel, maar geen vrijstelling.

Opvallend: **78% van bedrijven was op de deadline nog niet compliant**. De Europese Commissie kan ook retroactief handhaven voor schendingen vanaf augustus 2025.

**Bron:** [computable.nl](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/), [tech-insider.org](https://tech-insider.org/nl/ai-act-artikel-50-transparantieplicht-2026/), [aiactblog.nl](https://www.aiactblog.nl/en/posts/article-50-transparency-checklist-2-august-2026)

---

## 🔐 Security & Risk

**Prompt injection blijft het onopgeloste kernprobleem van agentische AI.** OWASP rangschikt het als LLM01 in 2026; aanvallen zijn met 340% gestegen ten opzichte van vorig jaar. Ariel Fogel (OWASP): "It remains an unsolved architectural problem." Zelfs frontier-modellen van OpenAI, Anthropic en Google zijn kwetsbaar na toepassing van hun beste mitigaties.

Concrete incidenten in productie: kritieke CVEs in **Microsoft Copilot** (CVSS 9.3), **GitHub Copilot** (CVSS 9.6) en **Cursor IDE** (CVSS 9.8). In maart 2026 documenteerde Unit 42 de eerste grootschalige indirecte prompt injection-aanvallen in productieomgevingen.

Voor organisaties die AI-agenten inzetten: defense in depth is de enige realistische strategie; er bestaat geen architecturele silver bullet.

**Bron:** [helpnetsecurity.com](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/), [infosecurity-magazine.com](https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/)

---

## 📈 Markt & Adoptie

De cloud AI-markt laat scherpe groeicijfers zien: **Google Cloud +63%, Azure +40%, AWS +28%** in Q1 2026. AWS behoudt het grootste marktaandeel (30%), Azure staat op 25%, Google Cloud op 13%.

De strategische verschuiving is duidelijk: de grote drie bewegen van modelwedloop naar **verticale AI-stack-integratie** — van chip tot businessapplicatie. Microsoft Copilot telt inmiddels **20 miljoen betaalde enterprise seats** (van 15M in januari). 89% van enterprises hanteert nu een multi-cloud AI-aanpak.

Kerninzicht voor inkoop en advies: **de competitieve differentiatie zit niet meer in het model, maar in operationele inzet** — welk model voor welke taak, switching costs en controle over data.

**Bron:** [windowsforum.com](https://windowsforum.com/threads/2026-ai-cloud-war-aws-vs-google-vs-microsoft-building-the-enterprise-nervous-system.416394/), [mindstudio.ai](https://www.mindstudio.ai/blog/google-cloud-vs-aws-vs-azure-q1-2026-ai-infrastructure)

---

## 💡 Ctac-relevantie

**Directe actie vereist – EU AI Act Artikel 50:** Als Ctac zelf chatbots, AI-contentgeneratie of emotieherkenning inzet of levert aan klanten, is compliance per 2 augustus verplicht. Controleer nu: zijn jullie chatbots gemarkeerd als AI? Worden AI-outputs voorzien van C2PA-metadata? Dit is ook een **propositionele kans**: 78% van bedrijven is nog niet compliant — Ctac kan hier als trusted advisor optreden met een compliance-quickscan of implementatiebegeleiding.

**Agentische AI-beveiliging als propositiethema:** Met prompt injection als #1 dreiging en actieve CVEs in de meest gebruikte enterprise AI-tools, is er een concrete markt voor security reviews van AI-implementaties. Dit sluit aan op bestaande Ctac-competenties in softwarekwaliteit en risicobeheersing.

**Van modelselectie naar AI-operatie:** De verschuiving bij de hyperscalers bevestigt wat klanten van Ctac nodig hebben: niet "welk model is het beste", maar "hoe richt ik AI-gebaseerde processen in, meet ik kwaliteit, en beheers ik kosten". Dat is precies de ruimte voor een consultancypropositie.

---

## 📚 Bronnen & verder lezen

- [llm-stats.com – AI Model Releases August 2026](https://llm-stats.com/llm-updates)
- [benchlm.ai – LLM Leaderboard August 2026](https://benchlm.ai/)
- [computable.nl – EU AI Act transparantie-eisen](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [aiactblog.nl – Article 50 checklist](https://www.aiactblog.nl/en/posts/article-50-transparency-checklist-2-august-2026)
- [tech-insider.org – 78% bedrijven niet klaar AI Act](https://tech-insider.org/nl/ai-act-artikel-50-transparantieplicht-2026/)
- [helpnetsecurity.com – Prompt injection OWASP rapport](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [infosecurity-magazine.com – Prompt injection onopgelost](https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/)
- [windowsforum.com – Cloud AI race 2026](https://windowsforum.com/threads/2026-ai-cloud-war-aws-vs-google-vs-microsoft-building-the-enterprise-nervous-system.416394/)
- [mindstudio.ai – Cloud AI infrastructure Q1 2026](https://www.mindstudio.ai/blog/google-cloud-vs-aws-vs-azure-q1-2026-ai-infrastructure)
- [felloai.com – Best AI Models August 2026](https://felloai.com/best-ai-models/)
