---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-11
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 11 juni 2026

## 🔑 Highlights van de dag

- **Anthropic Project Glasswing**: Anthropic geeft een select groep strategische partners (AWS, Apple, Cisco, Google, JPMorgan Chase, Microsoft) vroegtijdig toegang tot *Claude Mythos Preview* — een nog niet gepubliceerd frontier model dat de huidige Claude-lijn overstijgt.
- **EU AI Act Code of Practice in aantocht**: De definitieve gedragscode voor labeling en markering van AI-gegenereerde content wordt deze maand gepubliceerd; per 2 augustus 2026 is de AI Act volledig van kracht.
- **Prompt injection CVSS 9.6 in GitHub Copilot**: CVE-2025-53773 maakt remote code execution mogelijk via verborgen instructies in pull request-beschrijvingen — een concrete dreiging voor iedere organisatie die Copilot inzet in CI/CD-workflows.
- **Agentic AI wordt mainstream**: Gartner voorspelt dat 40% van enterprise-applicaties eind 2026 AI-agents bevat; Google lanceerde zijn *Agentic Data Cloud* als tegenzet op Microsofts Copilot-ecosysteem.
- **Trump-executive order**: De Amerikaanse president verplicht AI-bedrijven frontier modellen 30 dagen vóór release aan de federale overheid aan te bieden voor cybersecurity-benchmarking — een precedent met mondiale nawerking.

---

## 🧠 Technologie & Modellen

**Anthropic Project Glasswing / Claude Mythos Preview**
Anthropic heeft een besloten preview gelanceerd van *Claude Mythos*, hun nieuwe frontier model. Toegang is beperkt tot een handvol strategische partners waaronder Microsoft, Google, AWS en Apple. Dit is een bewuste marktpositiestrategie: door deze spelers eerder toegang te geven, verankert Anthropic Claude dieper in de enterprise-cloudinfrastructuur voordat het model publiek gaat.

**Gemini 3.5 en Microsoft MAI-Code-1-Flash**
Gemini 3.5 Flash (gelanceerd op Google I/O, 19 mei) is beschikbaar via API tegen $1,50/$9,00 per miljoen tokens; Gemini 3.5 Pro wordt nog deze maand verwacht. Microsoft presenteerde op Build 2026 *MAI-Code-1-Flash*, een gespecialiseerd codemodel dat vanuit natuurlijke taalomschrijvingen volledige applicaties genereert. Juni 2026 is objectief de drukste modelreleasemaand van het jaar.

**Multi-agent architecturen als standaard**
De markt voor agentic AI groeit van $7,8 mrd nu naar verwacht $52 mrd in 2030 (CAGR >30%). Multi-agent systemen worden de standaard enterprise-architectuur voor complexe workflows — supply chain, klantenservice en financiële audit zijn de vroege adoptiepaden.

*Bronnen: [LLM Stats](https://llm-stats.com/ai-news) · [WaveSpeed Blog](https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/) · [CNBC](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html) · [Anthropic Newsroom](https://www.anthropic.com/news)*

---

## 🏛️ Governance & Ethiek

**EU AI Act: code of practice en deadlines**
De definitieve *Code of Practice* voor transparantie-verplichtingen (Article 50 — markering van AI-gegenereerde content) wordt in juni 2026 gepubliceerd. Per **2 augustus 2026** is de AI Act volledig van toepassing — al zijn high-risk systemen in sectoren als biometrie, onderwijs en grenscontrole pas per december 2027 aan strengere regels onderworpen. De Europese Commissie heeft ondertussen een wetenschappelijk panel van 60 onafhankelijke AI-experts aangesteld ter ondersteuning van de handhaving.

**Trump executive order: pre-release disclosure**
President Trump ondertekende een executive order ("Promoting Advanced Artificial Intelligence Innovation and Security") die AI-bedrijven verzoekt frontier modellen 30 dagen vóór publieke release aan federale instanties beschikbaar te stellen voor cybersecurity-benchmarking. Hoewel dit vooralsnog een Amerikaans beleidsinstrument is, creëert het een precedent dat het internationale debat over AI-governance zal beïnvloeden.

*Bronnen: [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/) · [White House](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)*

---

## 🔐 Security & Risk

**Kritieke kwetsbaarheid in GitHub Copilot (CVSS 9.6)**
CVE-2025-53773 toont aan dat verborgen prompt injection-instructies in pull request-beschrijvingen remote code execution mogelijk maken via GitHub Copilot. Dit is geen theoretische aanval: het raakt direct de dagelijkse ontwikkelworkflow van teams die AI-assistentie gebruiken in code review.

**Semantic Kernel-kwetsbaarheden**
Twee nieuwe CVE's in Microsoft Semantic Kernel (CVE-2026-25592 en CVE-2026-26030) stellen aanvallers in staat unauthorized code execution te bereiken via injection-aanvallen gericht op agents die in het framework gebouwd zijn. Relevant voor elke organisatie die Semantic Kernel inzet als AI-orchestratie-laag.

**Prompt injection blijft structureel probleem**
OWASP heeft prompt injection opnieuw als #1 AI-beveiligingsdreiging benoemd. Unit 42 documenteerde in maart 2026 de eerste grootschalige *indirecte* prompt injection-aanvallen in het wild (ad review-evasion, systeemprompten lekkend op live platforms). Het fundamentele probleem — modellen kunnen instructies en data niet betrouwbaar onderscheiden — is nog niet opgelost.

*Bronnen: [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/) · [CrowdStrike](https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/) · [Airia](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)*

---

## 📈 Markt & Adoptie

**Azure groeit 39% — AI als groeikatalysator**
Microsoft Azure groeit met 39% aanzienlijk harder dan AWS (19%) en Google Cloud (30%). De AI-integratie in Microsoft 365 Copilot is hierbij de bepalende factor. Opvallend: Microsoft 365 Copilot combineert nu GPT (voor drafting) met Claude (voor fact-checking en citaatkwaliteit) in één workflow — het einde van het single-model tijdperk in enterprise AI.

**Google Agentic Data Cloud**
Google lanceerde op Google Cloud Next '26 de *Agentic Data Cloud*, een AI-native architectuur die legacy enterprise data-platformen transformeert tot "reasoning engines". Dit is Google's antwoord op Microsofts Copilot-ecosysteem en positioneert BigQuery als de centrale laag voor enterprise AI-agents.

**Adoptiedrempels bij MKB**
Uit onderzoek van Morning Consult blijkt dat enterprise AI voor het MKB niet vraag-beperkt maar fricties-beperkt is. Grootste blokkades: prijstransparantie (27%), commitment-angst (28%) en integratie-onzekerheid (21%). Google en OpenAI functioneren als de twee "mentale frontdeuren" bij MKB-oriëntatie.

*Bronnen: [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/) · [GeekWire](https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/) · [Tech Insider](https://tech-insider.org/microsoft-ai-spending-azure-copilot-2026/) · [Morning Consult](https://morningconsult.com/articles/enterprise-ai-smb-brand-perception-2026)*

---

## 💡 Ctac-relevantie

**Directe actiepunten:**

1. **Security-baseline voor AI-tooling**: De GitHub Copilot-kwetsbaarheid (CVSS 9.6) vereist aandacht als Ctac Copilot inzet in klantprojecten. Controleer of pull request-beschrijvingen van extern worden ingelezen door AI-tooling en implementeer input-sanitisatie als extra laag. Dit is ook een dienst die Ctac aan klanten kan aanbieden: AI security review als onderdeel van DevSecOps-trajecten.

2. **EU AI Act Augustus-deadline**: Per 2 augustus 2026 geldt de volledige AI Act. De Code of Practice voor content-labeling wordt nu gepubliceerd. Ctac-klanten die generatieve AI inzetten in publieke communicatie (overheid, zorg, finance) moeten vóór die datum compliant zijn. Dit is een concreet advies- en implementatietraject voor de komende 7 weken.

3. **Multi-agent architectuur als propositie**: De verschuiving naar agentic AI (40% van enterprise-apps met agents eind 2026, $52 mrd markt in 2030) sluit aan op de IP- en platformstrategie van Ctac. Het bouwen van herbruikbare agent-templates voor specifieke sectoren (bijv. gemeentelijke processen, zorgdossiers) is een realistisch propositie-pad voor de AI-unit. Google's Agentic Data Cloud en Microsoft's multi-model Copilot zijn de ecosystemen waarbinnen Ctac kan positioneren.

4. **Claude Mythos als signaal**: Dat Anthropic de grootste tech-spelers selecteert voor vroegtijdige toegang bevestigt dat Claude serieuze enterprise-positie inneemt naast GPT. Voor Ctac-klanten die model-diversificatie willen (minder OpenAI-afhankelijkheid) is Claude een geloofwaardig alternatief om nu al te verkennen.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI model releases juni 2026](https://llm-stats.com/ai-news)
- [WaveSpeed – June 2026 AI Launch Wave](https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/)
- [Anthropic Newsroom](https://www.anthropic.com/news)
- [CNBC – Microsoft MAI-Code-1-Flash](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)
- [EU AI Act Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act enforcement expert support](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support)
- [White House – AI Innovation and Security EO](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)
- [Microsoft Security Blog – RCE in AI agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [CrowdStrike – Indirect Prompt Injection](https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/)
- [Airia – AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [GeekWire – Microsoft Copilot multi-model era](https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/)
- [LegalNodes – EU AI Act 2026 Updates](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [Firecrawl – Agentic AI Trends 2026](https://www.firecrawl.dev/blog/agentic-ai-trends)
