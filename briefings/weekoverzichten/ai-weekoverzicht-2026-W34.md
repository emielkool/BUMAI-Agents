---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W34
Periode: 2026-08-17 / 2026-08-23
Status: In uitvoering
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 34 (17–23 augustus 2026)

### Maandag 17 augustus
→ Dagbriefing: [ai-briefing-2026-08-17.md](../ai-briefing-2026-08-17.md)

**Highlights:**
- **EU AI Act handhaving actief:** Transparantievereisten zijn per 2 augustus afdwingbaar — chatbots moeten zich als AI kenbaar maken, deepfakes verplicht gelabeld. De AI Omnibus verlengt de deadline voor hoog-risico systemen naar december 2027, maar compliance is nu al verplicht voor Artikel 50-toepassingen.
- **DeepSeek V4 Pro + Harness gelanceerd:** DeepSeek introduceert een open-source coding agent als alternatief voor Claude Code en stapt over op piek/dalprijs-model (per 16 aug). Met 7–17× kostenvoordeel t.o.v. Claude Sonnet en GPT-5.5 en 23% enterprise token-marktaandeel verstoort DeepSeek de vendor-verhoudingen structureel.
- **Prompt injection treft Claude Code, Gemini CLI en Copilot tegelijk:** Één aanval lekte secrets via drie coding agents. Het onderliggende probleem — modellen kunnen instructies en data niet onderscheiden — is architectureel, niet eenvoudig te patchen.

**Ctac-relevantie van de dag:** De combinatie van EU AI Act-handhaving (Artikel 50 direct afdwingbaar), DeepSeek als prijsverstoorder en agentic AI-beveiligingsincidenten maakt dit een cruciale week voor klantadvies op drie fronten: compliance-assessment, vendor-herafweging en security-architectuur voor agentic pipelines.

---

### Dinsdag 18 augustus
→ Dagbriefing: [ai-briefing-2026-08-18.md](../ai-briefing-2026-08-18.md)

**Highlights:**
- **EU AI Act handhaving: AI-telefonisten moeten zich direct identificeren** — NOS en Computable berichten dat de transparantieverplichting breed wordt opgepikt; consumenten én bedrijven krijgen nu rechtsbescherming bij AI-interacties.
- **Meta Muse Glimmer 30B gelanceerd (Apache 2.0):** Een lokaal draaiend open-source model met agentische capaciteiten en multimodaliteit — direct concurrent voor cloud-gebaseerde AI, met grote gevolgen voor on-premise deployment bij overheid en finance.
- **Atlassian Rovo kwetsbaar voor prompt injection:** Aanvallers kunnen Jira/Confluence-data exfiltreren via één aanval. OWASP bevestigt: prompt injection blijft de #1 LLM-kwetsbaarheid — enterprise AI-integraties creëren nieuwe aanvalsvectoren.

**Ctac-relevantie van de dag:** De EU AI Act-handhaving maakt compliance-assessments urgent voor klanten met AI-klantcontact. Tegelijkertijd opent Muse Glimmer kansen voor Ctac bij privacy-bewuste klanten die cloud-AI mijden. De Atlassian-kwetsbaarheid vraagt om proactieve klantcommunicatie als security-partner.

---

### Woensdag 19 augustus
→ Dagbriefing: [ai-briefing-2026-08-19.md](../ai-briefing-2026-08-19.md)

**Highlights:**
- **EU AI Act transparantievereisten van kracht:** Handhaving gestart 2 augustus — chatbots moeten zich identificeren als AI, deepfakes verplicht gelabeld. De AI Office én nationale autoriteiten hebben nu afdwingbevoegdheden; hoog-risico systemen (Annex I) krijgen uitstel tot augustus 2028 via de AI Omnibus.
- **Google Gemini 3.7 Flash en OpenAI Ultrafast mode:** Google's coding benchmark steeg in drie weken van 34% naar 44%; OpenAI's GPT-5.6 Sol draait nu op 750 tokens/seconde (14× sneller) via Cerebras. De modelrace en infrastructuursnelheid versnellen tegelijkertijd.
- **Stripe koopt OpenRouter voor $7 miljard:** Model-routing voor 400+ LLMs landt in betalingsinfrastructuur — betalingen en AI-orkestratie convergeren, met grote implicaties voor developer-tooling en enterprise AI-stacks.

**Ctac-relevantie van de dag:** De EU AI Act-handhaving is nu volledig actief: compliance-trajecten voor klanten met chatbots en generatieve AI zijn urgent. Twee derde van bedrijven zit nog vast in de pilot-fase — dit is de openingsmarkt voor Ctac als productie-enabler. Meta Muse Glimmer (Apache 2.0, lokaal) biedt kansen bij privacy-bewuste klanten in overheid, zorg en finance.

---

### Donderdag 20 augustus
→ Dagbriefing: [ai-briefing-2026-08-20.md](../ai-briefing-2026-08-20.md)

**Highlights:**
- **EU AI Act handhaving volledig actief (2 augustus):** Transparantie-eisen zijn nu juridisch afdwingbaar — chatbots moeten zich identificeren als AI, deepfakes moeten gelabeld zijn. Het AI Office en nationale toezichthouders kunnen nu boetes opleggen. Voor Ctac-klanten met klantcontact-AI is compliance geen optie meer.
- **Prompt injection raak bij drie grote coding tools tegelijk:** Claude Code, Gemini CLI en GitHub Copilot werden gelijktijdig getroffen; credentials gelekt via besmette repositories. AI-coding agents in productie vereisen minimale IAM-permissies en onbetrouwbare input-behandeling — nu een aangetoond risico, geen theorie.
- **Microsoft Frontier Company ($2,5 miljard):** Microsoft bouwt een eigen AI-implementatiebedrijf met 6.000 experts — directe concurrent voor IT-consultancies. Enterprise AI verschuift van experiment naar productie; hyperscalers investeren gezamenlijk >$500 miljard in capex voor 2026.

**Ctac-relevantie van de dag:** Microsoft Frontier Company is de meest urgente strategische dreiging voor Ctac's implementatiediensten — maar biedt ook kansen in segmenten waar Microsoft niet direct actief is. EU AI Act-compliance assessments zijn nu tijdgevoelig. De prompt injection-incidenten creëren een onderscheidende propositieruimte rondom veilige AI-integratie.

---

### Vrijdag 21 augustus
→ Dagbriefing: [ai-briefing-2026-08-21.md](../ai-briefing-2026-08-21.md)

**Highlights:**
- **EU AI Act handhaving actief per 2 augustus:** Chatbots moeten zich als AI identificeren, deepfakes verplicht gelabeld; het AI Office en nationale autoriteiten handhaven nu actief met boetebevoegdheid. De AI Omnibus verlengt de deadline voor hoog-risico systemen tot december 2027, maar Artikel 50 is direct afdwingbaar.
- **OpenAI GPT-5.6 Ultrafast + Meta Muse Glimmer 30B lokaal:** OpenAI's Sol-model draait nu 14× sneller en is 54% token-efficiënter in codeertaken; Meta's Muse Glimmer 30B brengt volledig lokale agentic AI op consumenten-hardware — zonder cloud-afhankelijkheid, interessant voor privacy-gevoelige sectoren.
- **Prompt injection: 94% van LLM-agents kwetsbaar:** Drie AI-codeeragenten lekten secrets via één aanval; Microsoft patchte een CVE in Copilot Studio maar data werd alsnog geëxfiltreerd. Inference-spending ($23,3 mrd) overtreft nu training ($19 mrd) — enterprises operationaliseren in hoog tempo, terwijl de beveiligingsachterstand groeit.

**Ctac-relevantie van de dag:** De combinatie van actieve EU AI Act-handhaving (Artikel 50 nu afdwingbaar) en snel stijgende Benelux-adoptie (NL: 61%, BE: 62%) bevestigt dat compliance-assessments en productie-implementaties de centrale klantbehoefte zijn. Prompt injection als #1 kwetsbaarheid vraagt om security-by-design als vast onderdeel van elk agentic AI-traject dat Ctac begeleidt.

---

## 🏆 Weekhighlights

*(wordt bijgewerkt aan het einde van de week)*

---

## 🔍 Domeinpatronen

*(wordt bijgewerkt aan het einde van de week)*

---

## 💼 Ctac-weekperspectief

*(wordt bijgewerkt aan het einde van de week)*

---

## 📚 Bronnenlijst

*(wordt bijgewerkt aan het einde van de week)*
