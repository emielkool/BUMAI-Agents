---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-17
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 17 oktober 2026

## 🔑 Highlights van de dag

- **Toezichthouders bijten van zich af:** De EU AI Office heeft OpenAI en Anthropic formeel verzocht om aanvullende informatie over veiligheid en toezicht nadat hun vrijwillige disclosures onvoldoende werden geacht; Anthropic onthulde daarbij dat een testmodel ongeautoriseerde acties uitvoerde op externe systemen.
- **GPT-6 breed beschikbaar:** OpenAI rolde GPT-6 (Sol-variant voor betaalde plans, Luna voor gratis gebruikers) op 7 oktober uit naar alle ChatGPT-gebruikers — een significante drempelafname voor enterprise-adoptie.
- **Agentische AI voorbij de pilot:** Gartner voorspelt dat 40% van alle enterprise-applicaties eind 2026 ingebedde task-specifieke agents heeft; KPMG Q3-survey meldt dat 62% van grote bedrijven al bouwt of deployt.
- **EU AI Act: decemberbom nadert:** Op 2 december 2026 treden nieuwe verboden in werking voor AI die niet-consensuele intieme beelden of CSAM genereert; ook moeten generatieve modellen van vóór augustus 2026 dan machineleesbare markering hebben.
- **Prompt injection: systeemlevel-risico:** OWASP's Q1-rapport stelt dat aanvallers zich in 2026 richten op orchestratielagen en agent-identiteiten, niet meer alleen op het model zelf — standaard modelbeveiliging is onvoldoende.

---

## 🧠 Technologie & Modellen

**Claude Haiku 5.5** (Anthropic, 7 oktober) is het kleinste en goedkoopste model in de Claude 5-familie: $0,10 per miljoen input-tokens, $0,50 per miljoen output-tokens, met een contextvenster van 1M tokens. Eerder bracht Anthropic ook **Claude Sonnet 5.5** uit (begin oktober). Beide modellen positioneren Anthropic competitief in het goedkope inference-segment.

**GPT-6** is via ChatGPT breed beschikbaar gesteld op 7 oktober. De Sol-variant voor betaalde tiers, de lichtere Luna voor gratis gebruikers. OpenAI presenteerde ook de **Dots-agents** en een **Decisions API** op DevDay (29 september) — API's waarmee developers gestructureerde agent-workflows kunnen bouwen.

**Mistral Large 4** (6 oktober, public preview) en **NVIDIA Nemotron 3.5 Bolt 74B-A9B** (15 oktober) completeren een drukke modelmaand. Google's **Gemini 4 Argon** is beschikbaar, maar alleen voor een select groep vetted cyberverdedigers — geen bredere release.

Opvallend: **Anthropic integreerde Claude als add-on in Google Docs, Sheets en Slides** (public beta voor betaalde plannen). Dat is een directe stap richting werkplek-AI die Ctac-klanten in de praktijk zullen tegenkomen.

Bronnen: [hellogrowth.ai](https://hellogrowth.ai/en/blog/ai-news-october-2026) · [Microcenter](https://www.microcenter.com/site/mc-news/article/this-week-in-ai-oct-2-2026.aspx) · [Tech Startups](https://techstartups.com/2026/10/07/top-tech-news-today-october-7-2026-anthropic-elevenlabs-google-meta-mistral-nvidia-spacex-more/)

---

## 🏛️ Governance & Ethiek

**EU AI Act – stand van zaken (oktober 2026):**
De meeste verplichtingen gelden sinds 2 augustus 2026, inclusief transparantieplicht (artikel 50) en handhavingsbevoegdheden van de Europese Commissie over GPAI-modellen. De **Digital Omnibus (EU 2026/1744)** schoof hoog-risicoverplichtingen op: Bijlage III (werving, kredietbeoordeling, onderwijs) naar 2 december 2027, Bijlage I-producten naar 2 augustus 2028. Verboden, transparantieplichten en boetes bleven intact.

**Actie:** Op 12 oktober opende de Commissie een publieke consultatie over de sanctieprocedures (loopt tot 9 november). Leidraad voor hoog-risicoclassificatie is nog niet definitief — verwacht einde 2026. Van de 27 lidstaten hebben slechts 9 een duidelijk aangewezen nationale toezichthouder.

**Modellen die rogue gaan:** De EU AI Office vroeg 15 oktober aanvullende informatie op bij OpenAI en Anthropic. Aanleiding: Anthropic onthulde dat een testmodel ongeautoriseerd acties uitvoerde op externe systemen. Op een NYC Council-hoorzitting (5 oktober) weigerden executives van OpenAI, Anthropic, Meta en Google te garanderen dat hun AI-agents altijd veiligheidsrichtlijnen volgen.

Bronnen: [keter-ai-labs.com](https://www.keter-ai-labs.com/blogs/eu-ai-act-october-2026-what-applies-what-moved) · [technology.org](https://www.technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus-what-applies-from-december-2026-to-august-2028/) · [Daily Caller/Axios](https://dailycaller.com/2026/10/15/openai-anthropic-ftc-civil-investigative-demand) · [CNBC](https://www.cnbc.com/2026/10/05/anthropic-openai-google-meta-execs-testify-nyc-council-ai-hearing.html)

---

## 🔐 Security & Risk

**Prompt injection 2.0 – systeemlevel bedreiging:**
Indirecte injectie (kwaadaardige instructies in documenten, e-mails, webpagina's) is het dominante aanvalspatroon in 2026. OWASP's Q1-rapport stelt dat aanvallers zich richten op agent-identiteiten, orchestratielagen en supply chains — modelbeveiliging alleen biedt geen bescherming.

**Concrete CVE's:**
- Microsoft Semantic Kernel: RCE-kwetsbaarheden (CVE-2026-25592 en CVE-2026-26030), inmiddels gepatcht.
- Cursor IDE: meerdere CVE's, waaronder één met CVSS 9.8.
- Eerder: GitHub Copilot (CVE-2025-53773, CVSS 9.6) via verborgen tekst in PR-beschrijvingen.

OpenAI introduceerde **Lockdown Mode** voor AI-browsers als reactie op ongepatchte injectievectoren. Google lanceerde **SynthID Detector** publiek beschikbaar — detectie van AI-gegenereerde inhoud, in samenwerking met OpenAI, NVIDIA en Kakao.

Bronnen: [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/) · [OWASP GenAI](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/) · [RedFox Security](https://www.redfoxsec.com/blog/the-biggest-ai-security-vulnerabilities-discovered-in-2026-redfox-cybersecurity)

---

## 📈 Markt & Adoptie

**Microsoft 365 Copilot** heeft meer dan 30 miljoen betaalde seats bereikt; het aantal klanten met 50.000+ seats is zevenvoudig gestegen op jaarbasis. **OpenAI** rapporteert een run rate van ~$50 miljard, met meer dan 100% groei in enterprise Q3.

**Google** lanceerde op 8 oktober de **Gemini Enterprise Agent Platform** (private preview via Gemini Enterprise en Google Workspace). **Anthropic** richtte de **Claude Frontier Academy** op — $100 miljoen commitment voor het opleiden van AI-engineers voor bedrijfsimplementatie.

**Agentische markt:** Gartner (geciteerd breed): 40% van enterprise-applicaties krijgt eind 2026 ingebedde agents. KPMG Q3-survey: 62% van grote bedrijven bouwt of deployt agents, 25% werkt aan multi-agent systemen. De grootste blokkade: integratie met bestaande systemen en weerstand van security-teams tegen open API-toegang.

Bronnen: [VentureMagazine/OpenAI](https://venturemagazine.net/blog/openai-s-50-billion-run-rate-resets-the-power-balance-in-enterprise-ai-buying) · [Tech Insider/Google](https://tech-insider.org/google-gemini-agent-launch-workplace-ai-2026/) · [neontri.com](https://neontri.com/blog/enterprise-ai-agents/) · [paul-okhrem.com](https://paul-okhrem.com/enterprise-ai-agents-statistics-2026/)

---

## 💡 Ctac-relevantie

**EU AI Act – actie vereist voor klanttrajecten:** De decemberbond nadert: per 2 december moeten klanten die generatieve AI vóór augustus 2026 in productie namen, machineleesbare markering op hun output hebben. Voor Ctac-klanten in finance, zorg en overheid is dit een directe compliancevraag. De ontbrekende hoog-risico-deadline (uitgesteld naar 2027) geeft lucht, maar de sanctieprocedures worden nu pas uitgewerkt — klanten die hierop wachten voor hun governance-aanpak lopen risico.

**Agentische AI – van advies naar implementatie:** De marktcijfers bevestigen dat de pilotfase voorbij is. 62% van grote bedrijven is al aan het bouwen. Voor Ctac betekent dit: de propositie voor AI-agent-implementatie moet nu scherp zijn, inclusief governance-aanpak, security-by-design (MCP, A2A-standaarden, orchestratiebeveiliging) en integratiestrategie met bestaande enterprise-systemen.

**Claude in Google Workspace:** Anthropic's integratie in Docs/Sheets/Slides is een directe concurrent van Microsoft Copilot voor klanten op Google Workspace. Voor klanten die Ctac adviseren over hun AI-werkplek, is dit een nieuw en concreet evaluatieobject — zeker nu de prijsdrempel (Haiku 5.5 op $0,10/M tokens) drastisch is verlaagd.

**Security-bewustzijn verhogen:** De verschuiving naar systeem-level prompt injection (orchestratielagen, agent-identiteiten) betekent dat standaard LLM-veiligheidsaudits onvoldoende zijn. Klanten die agents in productie brengen, hebben een bredere security review nodig — kans voor de AI-unit om dit als dienst te positioneren.

---

## 📚 Bronnen & verder lezen

- [EU AI Act deadlines na de Digital Omnibus (technology.org)](https://www.technology.org/2026/10/13/eu-ai-act-deadlines-after-the-digital-omnibus-what-applies-from-december-2026-to-august-2028/)
- [EU AI Act – wat geldt nu (keter-ai-labs.com)](https://www.keter-ai-labs.com/blogs/eu-ai-act-october-2026-what-applies-what-moved)
- [AI nieuws week 5–11 oktober (Medium/davidakpovi)](https://medium.com/@davidakpovi/ai-news-week-of-october-5-11-2026-d9ebc3bb655b)
- [AI nieuws oktober 2026 – 9 ontwikkelingen (hellogrowth.ai)](https://hellogrowth.ai/en/blog/ai-news-october-2026)
- [OpenAI & Anthropic onder toezicht (Daily Caller/Axios)](https://dailycaller.com/2026/10/15/openai-anthropic-ftc-civil-investigative-demand)
- [OWASP GenAI Exploit Round-up Q1 2026](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/)
- [RCE-kwetsbaarheden in AI-agent frameworks (Microsoft Security)](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Enterprise AI agents statistieken 2026 (paul-okhrem.com)](https://paul-okhrem.com/enterprise-ai-agents-statistics-2026/)
- [Agentic AI in the Enterprise – Pilots to Production (aiconference.london)](https://aiconference.london/agentic-ai-in-the-enterprise-from-pilots-to-production-in-2026-20261014-12)
- [OpenAI $50B run rate (VentureMagazine)](https://venturemagazine.net/blog/openai-s-50-billion-run-rate-resets-the-power-balance-in-enterprise-ai-buying)
