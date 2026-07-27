---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-26
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 26 juli 2026

## 🔑 Highlights van de dag

- **EU AI Act-deadline over zeven dagen:** Artikel 4 (AI-geletterdheid) wordt per 2 augustus 2026 gehandhaafd door de AP en RDI. Organisaties die hun medewerkers nog geen aantoonbare AI-basistraining hebben aangeboden, lopen direct handhavingsrisico.
- **Prijs-oorlog in de frontier-laag:** GPT-5.6, Grok 4.5 en Meta's Muse Spark 1.1 triggeren een historische kostencompressie; de tokenprijzen voor topcapaciteit dalen naar het $1-5/M-niveau. Dit democratiseert enterprise-AI maar ondermijnt de marges van puur door-model differentierte dienstverleners.
- **Agentic enterprise-oorlog:** Microsoft (€2,5 mrd + 6.000 experts), Google Cloud ($750 mln ecosysteeminvestering) en AWS ($1 mrd embedded engineers) strijden om de integrale enterprise AI-stack. De competitieve strijd is verschoven van modelkwaliteit naar operationeel beheer en integratie.
- **Prompt injection: systemisch risico voor agenten:** OWASP rapporteert een stijging van 340% in prompt injection-aanvallen; kritieke CVE's in Microsoft Copilot, GitHub Copilot en Cursor IDE (CVSS tot 9.8) tonen aan dat productie-agenten actief worden uitgebuit.
- **Kimi K3 van Moonshot AI** (2,8 biljoen parameters, open model) staat bovenaan de internationale coding-benchmark — een duidelijk signaal dat de Chinese open-source community het gat met de frontier lab's dicht.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6** verscheen deze maand in drie varianten (Luna, Terra, Sol) met elk 1 miljoen tokenscontext en een prijsrange van $1–5 per miljoen inputtokens. De initiële uitrol gaat via geselecteerde partners. Parallel lanceert OpenAI **GPT-Live**, een simultane spraakinteractie-modus die onderbrekingen en real-time vertaling ondersteunt — een stap voorbij het klassieke beurtsgespreksmodel.

**Anthropic Claude Sonnet 5** (30 juni) is volop beschikbaar. Fable 5 en Mythos 5 zijn per 1 juli wereldwijd toegankelijk na het vervallen van Amerikaanse exportbeperkingen; Anthropic voegde cybersecurity-classificatoren toe als aanvullende beveiliging.

**Google Gemini 3.6 Flash** (21 juli) richt zich op hoge snelheid en lage latentie. Google presenteerde ook twee nieuwe TPU-generaties — TPU 8i en TPU 8t — als dedicated infrastructuur voor grootschalige agentic workloads.

**Meta Muse Spark 1.1** introduceert Meta's eerste betaalde developer API (public preview, $20 gratis credits, VS-only). De 1M-tokencontext-agent ondersteunt computer use op desktop, browser en mobiel, plus parallelle sub-agent delegatie — een directe concurrent voor enterprise agentic platformen.

**Moonshot AI Kimi K3** (2,8T parameters, open gewicht) veroverde de eerste plek op de CodeForce-benchmark, wat de discussie over de gelijkwaardigheid van Chinese AI aan Westerse frontier-modellen opnieuw aanwakkert. ([llm-stats.com](https://llm-stats.com/ai-news), [thursdai.news](https://thursdai.news/releases/2026-07))

---

## 🏛️ Governance & Ethiek

**Kritieke deadline: 2 augustus 2026.** Artikel 4 van de EU AI Act (verplichting tot AI-geletterdheid) treedt volgende week in werking. In Nederland zijn de **Autoriteit Persoonsgegevens (AP)** en de **Rijksinspectie Digitale Infrastructuur (RDI)** de bevoegde toezichthouders. Organisaties zonder aantoonbaar AI-literacy programma voor medewerkers riskeren handhavingsacties. Artikel 5 (verboden AI-praktijken, zoals sociale scoring en ondervragings-AI) geldt al.

Het **Digital Omnibus-pakket** (goedgekeurd 7 mei 2026) brengt de deadline voor hoog-risico AI-systemen naar 2 december 2027 en schort de sandbox-verplichting op tot augustus 2027 — enige ademruimte voor organisaties die zwaardere compliance-trajecten bouwen.

Op het **World AI Conference** in Shanghai (17–20 juli) kondigde Xi Jinping de oprichting aan van de World Artificial Intelligence Cooperation Organization (WAICO) met 29 oprichtende landen. Dit formationaliseert het geopolitieke AI-schaakbord en kan de governance-architectuur op de langere termijn compliceren voor Europese bedrijven. ([frankwatching.com](https://www.frankwatching.com/archive/2026/05/04/eu-ai-act-regelen-voor-2-augustus/), [digitaleoverheid.nl](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/artificiele-intelligentie-ai/ai-verordening/))

---

## 🔐 Security & Risk

OWASP's 2026 LLM Security Report meldt een stijging van **340% in prompt injection-aanvallen** ten opzichte van vorig jaar — de snelst groeiende aanvalscategorie wereldwijd. Succespercentages liggen op 50–84% afhankelijk van systeemconfiguratie. OWASP rankt prompt injection als LLM01, de primaire AI-dreiging.

Concreet: **CVE-2025-53773** (CVSS 9.6) toont aan dat verborgen prompt injection in pull request-beschrijvingen remote code execution mogelijk maakte via GitHub Copilot. Soortgelijke kritieke CVE's bestaan voor Microsoft Copilot (9.3) en Cursor IDE (9.8). Geen van de frontier-providers heeft een volledige fix; defense-in-depth is de enige werkbare strategie.

**Implicatie voor agentic deployments:** naarmate agenten meer autonomie krijgen en systemen aansturen, neemt de aanvalsoppervlakte exponentieel toe. Prompt injection in een agent met tool-gebruik is een significante andere dreiging dan injection in een chatbot. ([helpnetsecurity.com](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/), [microsoft.com/security](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/))

---

## 📈 Markt & Adoptie

De drie grote cloud-hyperscalers domineren het nieuws:

- **Microsoft** zet 6.000 medewerkers in en investeert $2,5 miljard in enterprise AI-adoptie. Klanten krijgen keuzevrijheid tussen Microsoft-modellen, commerciële modellen van derden en open-source alternatieven — een strategische opening voor adviseurs die model-agnostisch werken. ([hpcwire.com](https://www.hpcwire.com/bigdatawire/2026/07/06/microsoft-launches-new-2-5b-ai-initiative-with-6000-experts-to-help-enterprises-deploy-a/))
- **Google Cloud** lanceerde de **Agentic Data Cloud** en investeert $750 miljoen in ecosysteempartners. Focus ligt op agentic workloads met BigQuery en Vertex AI als fundament. ([ciodive.com](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))
- **AWS** stuurt AI-engineers direct in bij klantteams via een $1 miljard investering.

De industrie verschuift eenduidig van "welk model?" naar "hoe opereer je AI in productie?". MLOps, governance, observability en inferentiekosten zijn de nieuwe battleground. Dit is goed nieuws voor IT-consultants die waarde toevoegen ín de integratie en niet alleen in de modelselectie.

---

## 💡 Ctac-relevantie

**Onmiddellijke actie vereist (vóór 2 augustus):** De EU AI Act-deadline voor Artikel 4 is aanstaande zaterdag. Als Ctac nog geen formeel AI-geletterdheids-programma heeft voor medewerkers — ook intern voor niet-technische functies — is nu het moment om dit minimaal te documenteren. Een eenvoudige basistraining met aantoonbare deelname volstaat voor compliance; het RDI beoordeelt of er sprake is van "passende maatregelen".

**Propositiekans:** Microsoft's keuze om klanten model-agnostische flexibiliteit te bieden speelt rechtstreeks in op Ctac's positie als onafhankelijk integrator. De boodschap "wij helpen u uw AI-stack inrichten ongeacht het model" is nu mainstream en wordt gesteund door de hyperscalers zelf — een mooie opening in enterprise gesprekken.

**Agentische security als dienst:** De explosie van prompt injection in productie-agenten, gecombineerd met de snelle adoptie van copilots en agents bij enterprise-klanten, creëert een concrete behoefte aan agentic security reviews. Ctac kan dit als aanvullende dienst positioneren naast AI-implementaties: "wij bouwen het en wij toetsen het op de OWASP Top 10 voor LLMs."

**Open-source convergentie:** Open-gewicht modellen (Kimi K3, Llama-familie) naderen frontier-kwaliteit op specifieke taken. Voor Ctac-klanten met data-souvereiniteitsrestricties (overheid, zorg) worden on-premise deployments van open modellen steeds realistischer — dit verdient een update van de interne roadmap.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI nieuws juli 2026](https://llm-stats.com/ai-news)
- [ThursdAI – July 2026 releases](https://thursdai.news/releases/2026-07)
- [EU AI Act – Frankwatching (deadline 2 augustus)](https://www.frankwatching.com/archive/2026/05/04/eu-ai-act-regelen-voor-2-augustus/)
- [Digitale Overheid – AI-verordening NL](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/artificiele-intelligentie-ai/ai-verordening/)
- [OWASP prompt injection rapport – Help Net Security](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [Microsoft Security Blog – RCE via prompt injection in agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Microsoft $2,5 mrd enterprise AI initiatief – HPCwire](https://www.hpcwire.com/bigdatawire/2026/07/06/microsoft-launches-new-2-5b-ai-initiative-with-6000-experts-to-help-enterprises-deploy-a/)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Cloud Wars – Agentic AI investment vergelijking](https://cloudwars.com/innovation-leadership/agentic-ai-wars-will-microsoft-aws-match-google-clouds-750-million-ecosystem-investment/)
- [Airia – AI Security in 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
