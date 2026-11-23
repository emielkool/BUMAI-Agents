---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-11
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 11 oktober 2026

## 🔑 Highlights van de dag

- **GPT-6 nu standaard voor alle ChatGPT-gebruikers** – OpenAI heeft GPT-6 als standaardmodel uitgerold voor alle gebruikers, inclusief een nieuwe Intelligent UI die antwoorden mengt met grafieken, kaarten, formulieren en minitools. Foutpercentage van GPT-6.1 Sol daalde naar 7,7%.
- **Claude Haiku 5.5 live** – Anthropic lanceerde op 7 oktober een snel, goedkoop model voor high-volume workloads (classificatie, samenvatting, klantenservice). Sonnet 5.5 is al ~30% sneller én ~30% goedkoper dan zijn voorganger.
- **EU AI Act handhaving gestart, high-risk deadlines opnieuw uitgesteld** – De AI Office heeft per 2 augustus 2026 handhavingsbevoegdheden. Maar via het AI Omnibus (Reg. EU 2026/1744) zijn verplichtingen voor high-risk systemen verschoven naar 2027/2028. Nieuwe verboden gelden per 2 december 2026.
- **Prompt injection: onopgelost architectureel probleem** – OWASP en onderzoekers bevestigen dat de kern van het probleem niet is opgelost; AI coding tools zijn het zwaarst getroffen, met kritieke kwetsbaarheden in GitHub Copilot (CVSS 9.6) en Cursor IDE.
- **Hyperscalers verdubbelen AI-capex** – Microsoft, Google en Amazon investeren gezamenlijk $660–690 miljard in AI-infrastructuur in 2026. Toch verliest Microsoft Copilot actieve gebruikers zodra medewerkers ook toegang krijgen tot ChatGPT of Gemini.

---

## 🧠 Technologie & Modellen

**OpenAI – GPT-6 wordt standaard**
Op 7 oktober is GPT-6 de standaard voor alle ChatGPT-gebruikers. De nieuwste variant GPT-6.1 Sol is een goedkopere near-flagship met een foutpercentage van 7,7% (t.o.v. 11,4% eerder). De bijgeleverde Intelligent UI is meer dan een esthetische upgrade: antwoorden kunnen nu interactieve grafieken, kaarten en formulieren bevatten. Dit verschuift ChatGPT van chatinterface naar embedded applicatieschil.

**Anthropic – Haiku 5.5 en Sonnet 5.5**
Claude Haiku 5.5 (7 oktober) is ontworpen voor high-volume taken waar snelheid en kosten cruciale parameters zijn. Sonnet 5.5, uitgebracht eind september, combineert 30% hogere snelheid met 30% lagere kosten. Voor organisaties die Anthropic API inzetten, is dit een concrete kostenreductie zonder kwaliteitsverlies.

**Google – Gemini Nano Banana 2.1**
Google lanceerde op 6 oktober Gemini Nano Banana 2.1, een kleine on-device variant. Gemini 4 Argon is nog in beperkte toegang; Gemini 3.5 Pro blijft vertraagd. Google's focus ligt duidelijk bij enterprise-integratie: ~90% van de Fortune 100 gebruikt Gemini Enterprise.

**Agentic AI: van hype naar productie**
Gartner verwacht dat tegen 2028 33% van enterprise software agentic AI bevat (nu <1%). In productie blijkt het probleem zelden het model te zijn, maar de operationele omgeving: slechte toolintegratie, onduidelijke autorisatiescopes en falende terugkoppellussen.

*Bronnen: [llm-stats.com](https://llm-stats.com/ai-news) · [slash-digital.io](https://slash-digital.io/en/insights/ai-models-2026/) · [computerworld.com](https://www.computerworld.com/article/3843138/agentic-ai-ongoing-coverage-of-its-impact-on-the-enterprise.html)*

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving actief, high-risk uitgesteld**
Sinds 2 augustus 2026 heeft de Europese AI Office handhavingsbevoegdheden voor general-purpose AI-modellen (GPAI). Ze kunnen documentatie opvragen, modellen evalueren en boetes opleggen. Nationale autoriteiten handhaven de overige AI-systemen — al zijn sommige lidstaten nog bezig hun implementatiewetgeving af te ronden.

Via het AI Omnibus (Reg. EU 2026/1744, in werking 27 juli 2026) zijn de meest belastende verplichtingen voor high-risk AI verschoven: standalone systemen hoeven pas per 2 december 2027 compliant te zijn, embedded systemen pas per 2 augustus 2028. Systemen die vóór 2 augustus 2026 op de markt zijn gebracht, genieten een overgangsperiode tot 2 december 2026.

**Kritische noot:** Het uitstel ontlast bedrijven op korte termijn, maar creëert ook onduidelijkheid over prioritering. Organisaties die nu compliance uitstellen, riskeren dat de kosten voor aanpassing later hoger uitvallen.

**Evenementen deze week in NL/BE**
World Summit AI Amsterdam vond 7–8 oktober plaats. Flanders AI Forum is op 20 oktober in Mechelen; BNAIC/BeNeLearn 2026 is 21–23 oktober in Maastricht.

*Bronnen: [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act) · [insideglobaltech.com](https://www.insideglobaltech.com/2026/05/28/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)*

---

## 🔐 Security & Risk

**Prompt injection: architectureel onopgelost**
Een OWASP-onderzoeker bevestigde op Infosec Europe 2026 dat het probleem fundamenteel onopgelost is: LLMs kunnen instructies van data niet betrouwbaar onderscheiden. Elk stuk externe tekst dat een agent ophaalt, kan als instructie werken.

Google registreerde een stijging van 32% in kwaadaardige indirect prompt injection content (november 2025–februari 2026). Unit 42 documenteert al 22 actieve payload-leveringstechnieken.

**AI coding tools: voornaamste aanvalsvector**
- **CVE-2025-53773** (GitHub Copilot): remote code execution, CVSS-score 9.6
- **CVE-2026-22708** (Cursor IDE): onderdeel van een exploitketen
- **EchoLeak** (Microsoft 365 Copilot): datalekrisico via indirect prompt injection

Voor agentic systemen geldt Simon Willison's "lethal trifecta": een agent met toegang tot privédata + blootstelling aan onbetrouwbare content + externe communicatiemogelijkheden is een kant-en-klaar exfiltratietool.

**Aanbeveling:** Ga uit van het principe dat initiële injectie *altijd* uiteindelijk slaagt. Defense-in-depth, granulaire autorisaties en audit logging zijn geen nice-to-haves.

*Bronnen: [helpnetsecurity.com](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) · [labs.cloudsecurityalliance.org](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/) · [futurumgroup.com](https://futurumgroup.com/insights/indirect-prompt-injection-exposes-a-universal-ai-security-flaw-no-deployment-model-is-immune/)*

---

## 📈 Markt & Adoptie

**Hyperscalers verdubbelen investering**
Microsoft, Alphabet en Amazon investeren gezamenlijk $660–690 miljard in AI-capex in 2026, bijna een verdubbeling ten opzichte van 2025. De race richt zich op inference-capaciteit dicht bij de data.

**Google vs. Microsoft: strijd om enterprise-standaard**
Google Cloud meldt dat 80% van zijn klanten AI-producten gebruikt en dat ~90% van de Fortune 100 Gemini Enterprise inzet. Microsoft Copilot Studio heeft 160.000 organisaties en 400.000+ custom agents — maar: actief Copilot-gebruik daalt naar 8% wanneer medewerkers ook toegang hebben tot ChatGPT of Gemini (vs. ~68% wanneer Copilot de enige optie is). Dit suggereert dat Copilot-adoptie deels gebonden is aan vendor lock-in, niet aan voorkeur.

**Enterprise AI-spend (schatting):**
OpenAI 42% · Anthropic 24% · Google 17% · AWS/Azure samen 11% · overig 6%

*Bronnen: [cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026) · [futurumgroup.com (capex)](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/) · [af.net](https://af.net/realtime/enterprise-ai-adoption-surges-as-microsoft-salesforce-and-google-drive-innovation/)*

---

## 💡 Ctac-relevantie

**1. Model-economie: goedkoper bouwen met Haiku 5.5 en Sonnet 5.5**
De nieuwe Anthropic-modellen bieden een concreet kostenvoordeel voor klantoplossingen die hoge volumes verwerken (classificatie, extractie, samenvatting). Ctac's AI-unit kan dit direct meenemen bij het ontwerp van propositie-offerings: de ROI-berekening wordt aantrekkelijker.

**2. EU AI Act: nu actie nemen loont**
De AI Office is actief, maar high-risk deadlines zijn uitgesteld. Dat biedt ruimte voor een gefaseerde aanpak — maar klanten die nu adviseren "het kan nog wachten" maken een strategische fout. De omschakelkosten zijn later hoger. Ctac kan zich positioneren als pragmatisch compliance-gids: niet alleen "wat moet", maar "wat loont nu al".

**3. Agentic AI security: onmisbaar in elke propositie**
De groeiende inzet van AI-agents in enterprise (Copilot Studio, Gemini-agents) maakt prompt injection-risico's urgent. Elke Ctac-klant die overweegt agentic workflows te bouwen, moet dit weten. Ctac kan hier waarde leveren met een security-assessment van geplande agentic implementaties — dit onderscheidt serieuze partijen van cowboys.

**4. Microsoft Copilot-paradox: kans voor onafhankelijk advies**
De lage actieve Copilot-gebruikscijfers bij multivendor-omgevingen zijn een strategische opening. Ctac kan onafhankelijk adviseren over de juiste toolkeuze per usecase, in plaats van kritiekloos Copilot te pushen. Dat vergroot vertrouwen bij klanten die al meerdere AI-licenties betalen zonder resultaat.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI News oktober 2026](https://llm-stats.com/ai-news)
- [Slash Digital – Best AI models October 2026](https://slash-digital.io/en/insights/ai-models-2026/)
- [EC – Enforcement AI Act](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [Inside Global Tech – AI Omnibus update mei 2026](https://www.insideglobaltech.com/2026/05/28/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)
- [Help Net Security – OWASP prompt injection](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [Cloud Security Alliance – Indirect Prompt Injection in the Wild 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-indirect-prompt-injection-in-the-wild-2026/)
- [Futurum – Indirect Prompt Injection universeel probleem](https://futurumgroup.com/insights/indirect-prompt-injection-exposes-a-universal-ai-security-flaw-no-deployment-model-is-immune/)
- [Google Cloud – Gemini at Work 2026](https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026)
- [Futurum – AI Capex 2026: $690B sprint](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/)
- [Computerworld – Agentic AI enterprise coverage](https://www.computerworld.com/article/3843138/agentic-ai-ongoing-coverage-of-its-impact-on-the-enterprise.html)
- [BNAIC 2026 – Maastricht University](https://www.maastrichtuniversity.nl/bnaic2026)
