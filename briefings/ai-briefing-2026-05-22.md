---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-22
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 22 mei 2026

## 🔑 Highlights van de dag

- **Google I/O 2026 (19 mei):** Google lanceerde Gemini Omni, Gemini 3.5 Flash en de persoonlijke AI-agent Gemini Spark – de grootste upgrade van Google Search in 25 jaar. Het agentische tijdperk is nu ook voor consumenten werkelijkheid.
- **EU AI Act omnibus akkoord (7 mei):** Een politiek akkoord vereenvoudigt de implementatie van de AI Act. Volledige handhaving – inclusief GPAI-modellen – gaat in op 2 augustus 2026. De klok tikt voor bedrijven die nog niet compliant zijn.
- **Enterprise AI-agent security: systeemfalen.** 88% van grote bedrijven rapporteerde al een AI-agent-beveiligingsincident; 97% van security-leaders verwacht een materieel incident binnen 12 maanden. Toch gaat slechts 6% van security-budgetten naar dit risico.
- **Anthropic Mythos:** Anthropic bracht een nieuw topmodel uit ('Mythos') voor een selecte groep partners, met nadruk op cybersecurity-toepassingen – een verontrustende ontwikkeling voor aanvallers én een kans voor verdedigers.
- **Microsoft Agent 365 (GA):** Microsofts tool voor agentbeheer is algemeen beschikbaar; Copilot-gebruik groeide met 160% op jaarbasis.

---

## 🧠 Technologie & Modellen

**Google I/O 2026** was de dominante techniekaankondiging van de week. Drie releases vallen op:

- **Gemini Omni**: multimodaal vlaggenschipmodel dat video, tekst en beeld verwerkt vanuit elke input. Gericht op "wereldbegrip" en creatieve taken.
- **Gemini 3.5 Flash**: sneller dan Gemini 3.1 Pro op coding en agentic benchmarks, nu standaard in Google Search AI Mode wereldwijd.
- **Gemini Spark**: een persoonlijke AI-agent in de Gemini-app die langetermijntaken zelfstandig uitvoert met Gmail-integratie.

Google positioneert zijn **Antigravity-platform** als het agent-first ontwikkelplatform voor iedereen – van developer tot eindgebruiker. De stap is significant: Google combineert frontier-modellen met directe integratie in zijn hele ecosysteem (Search, Gmail, Android, Cloud).

**Anthropic** bracht Claude Opus 4.7 uit (zelfde prijs als 4.6: $5/M input, $25/M output) en "Mythos" – een krachtig model met cybersecurity-focus dat vooralsnog alleen voor geselecteerde partners beschikbaar is.

*Bron: [TechCrunch – Google I/O 2026](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/), [Anthropic](https://www.anthropic.com/news/claude-opus-4-7)*

---

## 🏛️ Governance & Ethiek

Op **7 mei 2026** bereikten EU-lidstaten een politiek akkoord over het **AI Omnibus-voorstel** – een vereenvoudiging van de AI Act-implementatie, zonder de kernverplichtingen te verzwakken. Tijdlijn:

- **2 augustus 2025**: GPAI-modelverplichtingen al van kracht.
- **2 augustus 2026**: Volledige handhaving, inclusief Commissie-sanctiebevoegdheden voor GPAI-aanbieders (documentatieopvraag, evaluaties, boetes).

Organisaties in NL/BE die general-purpose AI-modellen aanbieden of inzetten in high-risk contexten hebben nog **10 weken**. Transparantieregels voor AI-gegenereerde content worden ook in augustus afdwingbaar.

In Nederland investeert het **Rijk 70 miljoen euro in de AI-fabriek in Groningen** (NOS), gericht op rekencapaciteit voor Nederlandse AI-ontwikkeling – een signaal dat soevereine AI-infrastructuur serieus op de agenda staat.

*Bron: [EU AI Act tracker](https://artificialintelligenceact.eu/), [NOS – AI-fabriek Groningen](https://nos.nl/artikel/2572670-rijk-steekt-nu-ook-70-miljoen-in-ai-fabriek-groningen)*

---

## 🔐 Security & Risk

De **enterprise AI-agent securitycrisis** is niet langer theoretisch:

- **88%** van enterprises rapporteerde al een AI-agent-beveiligingsincident (VentureBeat-onderzoek).
- **85%** draait al AI-agent pilots; slechts **5%** durft ze in productie te brengen.
- Drie populaire coding agents lekten gevoelige data via één gerichte **prompt injection-aanval** – waarbij een vendor's eigen system card het risico al voorspeld had.
- **AI Tool Poisoning**: aanvallers manipuleren gedeelde tool-registries die agents gebruiken voor taakuitvoering. Authenticatie slaagt, autorisatie faalt.

Kern van het probleem: enterprise identity-systemen (SOC 2, ISO 27001) zijn gebouwd voor mensen, niet voor agents. Agents hebben geen plek in bestaande controlecatalogi.

*Bron: [VentureBeat – 88% incidents](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds), [VentureBeat – tool poisoning](https://venturebeat.com/security/ai-tool-poisoning-exposes-a-major-flaw-in-enterprise-agent-security), [VentureBeat – coding agents prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)*

---

## 📈 Markt & Adoptie

**Microsoft** boekte zijn sterkste Copilot-kwartaal ooit: betaalde seats +160% YoY, dagelijks gebruik ×10. **Microsoft 365 E7** bundelt nu M365 E5, Copilot én de nieuwe **Agent 365** ($15/gebruiker/maand) – één dashboard voor het observeren, beveiligen en besturen van alle AI-agents binnen een organisatie.

**Google** introduceerde een **$100/maand AI Ultra-abonnement** voor developers en kenniswerkers – een signaal dat Big Tech de AI-markt segmenteert richting premium enterprise-tiers.

**OpenAI** lanceerde **Workspace Agents** als opvolger van custom GPTs: directe integraties met Slack, Salesforce en andere enterprise-tools. Dit maakt het makkelijker om agents in te zetten zonder custom API-werk.

In Nederland signaleert **Computable** dat generatieve AI recruitment fundamenteel verstoort: werkzoekenden optimaliseren cv's en sollicitaties met AI, waardoor werkgevers echte competenties moeilijker kunnen beoordelen.

*Bron: [Microsoft Blog – Frontier Suite](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/), [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/), [VentureBeat – OpenAI Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more), [Computable – AI en recruitment](https://www.computable.nl/2026/05/20/generatieve-ai-maakt-rekrutering-steeds-complexer/)*

---

## 💡 Ctac-relevantie

**Agent security als nieuwe propositie:** De kloof tussen "agents draaien" en "agents vertrouwen" is de grootste groeirem voor enterprise AI-adoptie. 85% van bedrijven heeft pilots, maar slechts 5% zet ze productie-ready in. Ctac kan hier een concrete adviespropositie op bouwen: **agent governance & security-assessments** voor klanten die stagneren in de pilotfase. Denk aan risicoframeworks, identity-mapping voor agents en compliancetoetsing tegen ISO/SOC-normen.

**EU AI Act deadline nadert:** 10 weken tot volledige handhaving op 2 augustus 2026. Klanten in high-risk sectoren (overheid, zorg, finance) die Ctac als IT-partner hebben zijn mogelijk nog niet klaar. Een gerichte **AI Act readiness scan** is nu commercieel opportuun én maatschappelijk verantwoord.

**Microsoft 365 E7 en Agent 365** zijn aankomend gesprekspunt in elke Microsoft-klantrelatie. De bundeling vereenvoudigt de aankoopbeslissing maar vraagt ook om governance-begeleiding – precies waar Ctac waarde kan toevoegen.

**Gemeenten als nieuwe markt:** De Computable-berichtgeving over AI-anonimisering bij gemeenten en de Rijksinvestering in AI-infrastructuur wijzen op een groeiende behoefte aan praktische, veilige AI-implementaties bij overheidsklanten in NL.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Google I/O 2026: AI design tools](https://techcrunch.com/2026/05/19/ai-design-tools-are-the-next-big-battleground-and-google-is-going-all-in-at-io-2026/)
- [TechCrunch – Gemini Spark](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/)
- [Google Blog – 100 aankondigingen I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/)
- [Anthropic – Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [EU AI Act – implementatietimeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act governance & handhaving](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [VentureBeat – 88% enterprise incidents](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds)
- [VentureBeat – AI tool poisoning](https://venturebeat.com/security/ai-tool-poisoning-exposes-a-major-flaw-in-enterprise-agent-security)
- [VentureBeat – 85% agents, 5% production](https://venturebeat.com/security/85-of-enterprises-are-running-ai-agents-only-5-trust-them-enough-to-ship)
- [Microsoft Blog – Frontier Suite](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)
- [CIO Dive – Microsoft & Google enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [VentureBeat – OpenAI Workspace Agents](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more)
- [NOS – AI-fabriek Groningen](https://nos.nl/artikel/2572670-rijk-steekt-nu-ook-70-miljoen-in-ai-fabriek-groningen)
- [Computable – AI en recruitment](https://www.computable.nl/2026/05/20/generatieve-ai-maakt-rekrutering-steeds-complexer/)
- [Computable – AI-anonimisering gemeenten](https://www.computable.nl/2026/05/19/gemeenten-lanceren-ai-tool-voor-bron-anonimisering/)
