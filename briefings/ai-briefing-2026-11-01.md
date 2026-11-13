---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-01
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 1 november 2026

## 🔑 Highlights van de dag

- **OpenAI DevDay 2026:** OpenAI kondigde GPT-5.6 aan in drie smaken (Sol, Terra, Luna) en introduceerde een Decisions API in beperkte preview. De Decisions API is potentieel een keerpunt: het stelt agenten in staat om gestructureerde beslissingspunten door te sturen naar menselijke operators.
- **Mistral Large 4 – open gewichten voor cybersecurity:** Mistral heeft de gewichten van zijn trillion-parameter model openbaar gemaakt via Hugging Face. Positionering op cybersecurity is opvallend en strategisch slim, gezien de groeiende markt voor AI-security tooling.
- **EU AI Act: decembertermijn nadert:** Per 2 december 2026 treden nieuwe verplichtingen in werking rondom generatieve AI-labelling en verboden op specifieke content. Organisaties die dit nog niet in orde hebben, lopen risico.
- **Nederland: kabinet verwacht 25.000 banen te schrappen via AI:** Een politiek en maatschappelijk geladen ontwikkeling die de publieke perceptie van AI-adoptie in de publieke sector beïnvloedt. Kans én risico voor IT-dienstverleners als Ctac.
- **Prompt injection: aanvalspercentage 50–84%:** Agentic AI-systemen blijven structureel kwetsbaar. Microsoft publiceerde eerder dit jaar RCE-kwetsbaarheden in Semantic Kernel; een volledig antwoord bestaat nog niet.

---

## 🧠 Technologie & Modellen

**OpenAI DevDay 2026** resulteerde in meerdere aankondigingen. GPT-5.6 "Sol" is de nieuwste flagship, naast "Terra" (balanced) en "Luna" (low-cost). GPT-6.1 Sol richt zich specifiek op agentic coding en computer use. De Decisions API is het meest opmerkelijke: het voegt een gestructureerde menselijke goedkeuringsstap toe aan agentische workflows — wat voor enterprise-adoptie cruciaal is. ([openai.com](https://openai.com/index/devday-2026-recap/))

**Mistral Large 4** is het eerste trillion-parameter open-weight model dat gericht is op cybersecurity use cases. De keuze om de gewichten volledig te openen via Hugging Face positioneert Mistral als alternatief voor gesloten modellen, met name voor organisaties met data-residency-eisen. ([techcrunch.com](https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/))

**Meta Muse Wonder** (gelanceerd 12 oktober) is Meta's eerste echte frontier model. Wonder Full, de krachtigste variant, is exclusief voor Muse Code-abonnees en niet via de API beschikbaar — een duidelijke keuze voor een closed-ecosystem-strategie. ([techcrunch.com](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/))

---

## 🏛️ Governance & Ethiek

**EU AI Act – decembertermijn:** Per 2 december 2026 gelden nieuwe regels:
- Verbod op non-consensuele intieme afbeeldingen (CSAM en "nudificatie-apps")
- Verplichte labelling van AI-gegenereerde content (Art. 50(2)) voor systemen die vóór augustus 2026 op de markt waren

De eerste geharmoniseerde standaard (kwaliteitsmanagementsysteem) werd op 19 oktober gepubliceerd in het EU Official Journal. Dit is de eerste concrete technische standaard onder de Act — meer volgen. ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [artificialintelligenceact.eu](https://artificialintelligenceact.eu/))

**Nederland – kabinetsplan:** Staatssecretaris Van den Burg (BZK) wil met AI 25.000 ambtenarenbanen schrappen (van 160.000), goed voor €3,5 miljard bezuiniging in acht jaar. De staatssecretaris erkent zelf dat AI "geen wondermiddel" is — wat de uitvoeringsrisico's onderstreept. Voor IT-dienstverleners biedt dit werk; voor draagvlak bij eindgebruikers vraagt het zorgvuldige communicatie. ([computable.nl](https://www.computable.nl/2026/10/26/kabinet-rekent-op-ai-voor-forse-bezuiniging-op-personeel/))

**Benelux-parlement** riep de drie regeringen op tot harmonisatie van nationale AI-strategieën en wil de regio tot AI-testzone maken. ([datanews.knack.be](https://datanews.knack.be/))

---

## 🔐 Security & Risk

**Prompt injection blijft een open wond.** OWASP rankt het als LLM01; succesvol aanvalspercentage ligt op 50–84%. Microsoft openbaarde eerder dit jaar twee kritieke RCE-kwetsbaarheden in Semantic Kernel (CVE-2026-25592, CVE-2026-26030) waarbij geïnjecteerde prompts konden escaleren naar code-executie. Het UK NCSC stelt dat prompt injection mogelijk nooit volledig te mitigeren valt zoals SQL-injectie dat wel is. ([microsoft.com](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/), [cycode.com](https://cycode.com/blog/ai-security-vulnerabilities/))

**AI-gestuurde cyberaanvallen in Benelux** nemen toe. Check Point signaleert Nederland en Luxemburg als uitschieters. ([datanews.knack.be](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/))

---

## 📈 Markt & Adoptie

**Microsoft en Google domineren enterprise AI**, zo blijkt uit Gartner-rapportage. Microsoft leidt op ecosysteem en partnernetwerk; Google wordt als sterkste speler in enterprise agentic AI gezien. Azure en Google Cloud groeien beide sterk — Google Cloud passeerde $20 miljard per kwartaal in Q1 2026. ([ciodive.com](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

**Microsoft Frontier Company** is een nieuwe interne AI-implementatie-eenheid met $2,5 miljard en 6.000 medewerkers — gericht op het sluiten van de kloof tussen AI-experiment en operationele uitrol. ([techcrunch.com](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/))

**SAP Business AI Platform** bundelt bouw en deployment van AI in één enterprise-platform, met agent-interoperabiliteit tussen Joule en externe agents (via Google Cloud en Microsoft-partnerships). ([ciodive.com](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/))

**Adoptie stagneert.** Tweederde van de bedrijven zit nog in pilotfase; executives verwachten slechts 27% rendement op AI-investeringen in de komende één à twee jaar. De proof-of-concept-val is realiteit, niet uitzondering.

**Nederland:** Kabinet investeert €120 miljoen in industriële AI via het EU-programma IPCEI-AI. ([computable.nl](https://www.computable.nl/2026/09/21/kabinet-steekt-120-miljoen-euro-in-industriele-ai/))

---

## 💡 Ctac-relevantie

**Decembertermijn EU AI Act** vraagt directe actie bij klanten die generatieve AI-toepassingen ingezet hebben zonder labelling of met verboden content-functies. Ctac kan hier adviseren én implementeren — dit is concreet advieswerk voor de korte termijn.

**Decisions API van OpenAI** sluit direct aan op de enterprise-eis van "human-in-the-loop." Voor klanten in gereguleerde sectoren (overheid, zorg, finance) is dit een enabler die agentic AI-projecten uit de risicozone haalt. Ctac kan dit als onderscheidend argument inzetten bij klanten die aarzelen vanwege autonomie van AI-systemen.

**Prompt injection en agentic security** zijn de komende maanden een toenemend aandachtspunt, zeker voor klanten die Copilot, Semantic Kernel of MCP-gebaseerde agents implementeren. Ctac's AI engineer kan hier een praktische security-checklist voor ontwikkelen.

**Kabinetsplan 25.000 banen:** Overheidsklanten van Ctac zullen intern druk voelen om AI-pilots naar productie te brengen. Dit is een kans, mits de verwachtingen reëel worden geset. Juist hier kan Ctac onderscheiden op implementatiekwaliteit, niet op belofte.

**Subsidieronde zorgsimulaties (Stichting Dutch, opent 10 november):** Maximaal €600.000 per project voor AI-ondersteunde zorgsimulaties. Vermeldenswaard voor klanten in de zorgsector of Ctac's eigen innovatieprogramma's.

---

## 📚 Bronnen & verder lezen

- [OpenAI DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/)
- [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)
- [TechCrunch: Mistral Large 4 open weights](https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/)
- [TechCrunch: Meta Muse Wonder](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/)
- [EU Digital Strategy: AI Act enforcement framework](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [EU AI Act Explorer: Digital Omnibus](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/)
- [Computable: Kabinet rekent op AI voor bezuiniging](https://www.computable.nl/2026/10/26/kabinet-rekent-op-ai-voor-forse-bezuiniging-op-personeel/)
- [Computable: Kabinet 120 miljoen voor industriële AI](https://www.computable.nl/2026/09/21/kabinet-steekt-120-miljoen-euro-in-industriele-ai/)
- [CIO Dive: Microsoft en Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive: SAP AI-platform](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [TechCrunch: Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [Microsoft Security Blog: RCE in AI agent frameworks](https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/)
- [Data News: Meer cyberaanvallen door AI in Benelux](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
- [Cycode: AI Security Vulnerabilities 2026](https://cycode.com/blog/ai-security-vulnerabilities/)
