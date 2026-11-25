---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-24
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 24 november 2026

## 🔑 Highlights van de dag

- **Anthropic op de beurs:** Anthropic ging op 19 november met succes naar de Nasdaq (ticker: ANT), bij een waardering van boven $1 biljoen. De IPO was 6x overgetekend — een signaal dat institutionele beleggers AI-frontier labs als serieuze long-term bets zien.
- **Modellenregen in november:** OpenAI (GPT-6.2 Sol & Astra, 17 nov), Google (Gemini 4 Neon, 18 nov) en Anthropic (Claude Fable 5.2 & Mythos 5.2, 9 nov) brachten allemaal nieuwe modellen uit. De releases volgen elkaar in hoog tempo op — dit is concurrentiedruk als strategie.
- **EU AI Act in volle uitvoering, maar high-risk uitgesteld:** Sinds 2 augustus 2026 zijn de meeste verplichtingen afdwingbaar, maar de Digital Omnibus heeft deadlines voor high-risk AI verschoven naar 2027–2028. Voor Nederlandse IT-dienstverleners is er dus nog ademruimte — maar niet voor altijd.
- **AI-agenten overnemen enterprise workflows:** Gartner verwacht dat 40% van enterprise software eind 2026 taakspecifieke AI-agenten bevat. De transitie van copilot naar autonome workflow-executie is in volle gang, maar Gartner voorspelt ook dat 40%+ van de agentic AI-projecten vóór 2027 zal falen.
- **AI supply chain: één op drie leveranciers heeft kritieke kwetsbaarheden ongepatch:** Black Kite onderzocht meer dan 18.000 AI-bedrijven en vond bij 34% kritieke beveiligingslekken. Dit is een directe risicofactor voor organisaties die AI-producten van derden inzetten.

---

## 🧠 Technologie & Modellen

**OpenAI – GPT-6.2 Sol en Astra (17 november)**
OpenAI bracht twee varianten uit: GPT-6.2 Sol als de alledaagse, goedkopere variant, en GPT-6.2 Astra (~20% goedkoper dan het vorige model). Sol lijkt bedoeld voor breedsprint gebruik en hoge volumes; Astra voor complexere taken. Ook GPT-6 Cyber werd uitgebracht, maar is slechts beperkt toegankelijk.

**Google – Gemini 4 reeks compleet (10–18 november)**
Google lanceerde in twee weken Carbon (10 nov), Hydrogen (12 nov) en Neon (18 nov). De drie varianten bestrijken de volledige bandbreedte van edge tot enterprise cloud. Opvallend: de Cloud-releasedatums liepen achter op de API-changelog — een hint dat Google zijn releases nog niet volledig gecoördineerd heeft.

**Anthropic – Claude Fable 5.2 en Mythos 5.2 (9 november)**
Fable 5.2 is algemeen beschikbaar; Mythos 5.2 is beperkt tot geverifieerde organisaties. Combineer dit met de beursgang: Anthropic positioneert zich bewust als "responsible frontier lab" richting institutionele afnemers.

Bronnen: [LLM Stats](https://llm-stats.com/ai-news) · [LarWell AI News](https://larwell.com/blog/ai-news-this-week-november-22-2026) · [LLM Gateway Timeline](https://llmgateway.io/timeline)

---

## 🏛️ Governance & Ethiek

**EU AI Act: afdwingbaar, maar high-risk in de wacht**
Sinds 2 augustus 2026 zijn de verboden, AI-geletterdheidsplicht, transparantieregels en GPAI-verplichtingen van kracht. De Digital Omnibus (Verordening EU 2026/1744) heeft echter de deadlines voor high-risk AI — denk aan AI in werving, kredietverlening, onderwijs — verschoven naar december 2027 en augustus 2028. Reden: geharmoniseerde normen zijn niet op tijd klaar, en veel EU-lidstaten hebben hun toezichthouders nog niet volledig ingericht.

**Nederland:** Tien bestaande toezichthouders delen de handhavingstaken; de AP en de Rijksinspectie Digitale Infrastructuur (RDI) coördineren. Voor Nederlandse IT-bedrijven is duidelijkheid over wie wat handhaaft nog beperkt.

Bronnen: [i-scoop EU AI Act Digital Omnibus](https://i-scoop.eu/eu-ai-act-timeline-digital-omnibus) · [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [FPF AI Act Timeline](https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/)

---

## 🔐 Security & Risk

**34% van AI-leveranciers heeft ongepatchte kritieke kwetsbaarheden**
Black Kite onderzocht 18.160 AI-bedrijven en vond bij 34,2% kritieke, niet-gepatchte lekken (september–oktober 2026). Dit is geen abstracte statistiek: organisaties die AI-producten van derden inzetten, nemen indirect risico als die leverancier een zwak patchbeleid heeft.

**Prompt injection en datalekkage in productiesystemen**
Het IPA Japan-overzicht (oktober–november 2026) meldt een bug waarbij redeneergegevens uit de OpenAI API lekten. Ook werd een gemanipuleerde Claude Code-extensie verspreid via Cursor. Dit zijn concrete voorbeelden van kwetsbaarheden in de AI-ontwikkelketen.

**OWASP Top 10 LLM 2026: "unbounded consumption" stijgt**
Eén prompt die een keten van resource-intensieve toolaanroepen triggert is een groeiend risico — relevant voor organisaties die agentic AI inzetten zonder rate-limiting of kostenbeheer.

Bronnen: [Black Kite AI Supply Chain Report](https://www.unite.ai/nl/black-kite-2026-ai-supply-chain-report/) · [OWASP Top 10 LLM 2026](https://www.unite.ai/nl/2026-owasp-top-10-llm-security-agentic-ai-risks/) · [IPA November 2026](https://www.ipa.go.jp/digital/ai/security/rcu1hd0000007gji-att/2026-5_1113.pdf)

---

## 📈 Markt & Adoptie

**Anthropic IPO: $1 biljoen waardering, 6x overgetekend**
Anthropic noteerde op 19 november op de Nasdaq (ANT) bij een prijs van $70–$78 per aandeel (825 miljoen aandelen). De vraag was zes keer het aanbod. Dit is een marktsignaal: frontier AI wordt niet meer als speculatief beschouwd, maar als infrastructure-tier investering.

**Microsoft Copilot domineert enterprise adoption**
Morning Consult (augustus 2026): 73% van de grootste ondernemingen heeft Microsoft Copilot goedgekeurd of in gebruik. Google Gemini zit op 55% goedkeuring breed. Microsoft investeert $2,5 miljard en 6.000 mensen in het Frontier-programma waarbij medewerkers direct bij klanten zitten.

**Van copilot naar autonome agents**
Enterprises migreren van assistive AI naar autonome workflow-executie. IBM lanceerde Enterprise Advantage voor CIOs die willen opschalen, Salesforce Agentforce breidt uit richting SMB, Workday richt zich op governed access voor HR/finance-agenten.

Bronnen: [Morning Consult Enterprise AI](https://morningconsult.com/articles/state-of-enterprise-ai) · [CIO Dive – Microsoft/Google](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) · [Al Jazeera Anthropic IPO](https://www.aljazeera.com/economy/2026/11/19/anthropic-starts-trading-in-the-us-after-blockbuster-ipo) · [eWeek Enterprise AI](https://www.eweek.com/news/enterprise-ai-arms-race/)

---

## 💡 Ctac-relevantie

**Anthropic's beursgang als strategisch ijkpunt**
De IPO van Anthropic maakt Claude-modellen onderdeel van een beursgenoteerde investering — dit vergroot de verwachtingen rond enterprise-features, SLA's en compliance. Voor Ctac betekent dit dat klanten steeds vaker vragen om concrete roadmap-commitment van AI-leveranciers. Zorg dat proposities niet afhangen van één model-aanbieder.

**EU AI Act: nu handelen op transparantie, niet wachten op high-risk**
De transparantie- en GPAI-verplichtingen gelden nu al. Ctac kan klanten in zorg, overheid en finance helpen met AI-registers, impact assessments en documentatieplichten — ook al zijn high-risk deadlines uitgesteld. Dit is een reëel salesargument richting compliance-bewuste sectoren.

**Agentic AI: kans en governance-risico tegelijk**
De markt beweegt snel richting autonomous agents. Ctac's AI-unit kan zich onderscheiden door niet alleen te implementeren, maar ook governance-kaders mee te leveren: cost controls, audit trails, rol-gebaseerde autorisatie. Gartners voorspelling dat 40% van agentic projecten zal falen, is een opening: Ctac als "de partij die het wél laat werken."

**Supply chain security als propositiepijler**
Met 34% van AI-leveranciers met kritieke kwetsbaarheden is vendor risk assessment een reëel vraagstuk. Ctac kan dit integreren in TPRM-dienstverlening of als onderdeel van een AI-adoptietraject.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI News November 2026](https://llm-stats.com/ai-news)
- [LarWell – AI News Week 22 november 2026](https://larwell.com/blog/ai-news-this-week-november-22-2026)
- [Al Jazeera – Anthropic starts trading after blockbuster IPO](https://www.aljazeera.com/economy/2026/11/19/anthropic-starts-trading-in-the-us-after-blockbuster-ipo)
- [i-scoop – EU AI Act Digital Omnibus timeline](https://i-scoop.eu/eu-ai-act-timeline-digital-omnibus)
- [FPF – AI Act Implementation Timeline](https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/)
- [EC Digital Strategy – Regulatory Framework AI](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Black Kite – 2026 AI Supply Chain Report](https://www.unite.ai/nl/black-kite-2026-ai-supply-chain-report/)
- [OWASP Top 10 LLM 2026 – Agentic AI Risks](https://www.unite.ai/nl/2026-owasp-top-10-llm-security-agentic-ai-risks/)
- [Morning Consult – State of Enterprise AI](https://morningconsult.com/articles/state-of-enterprise-ai)
- [CIO Dive – Microsoft/Google rule AI market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [eWeek – Enterprise AI Arms Race](https://www.eweek.com/news/enterprise-ai-arms-race/)
- [Cryptobriefing – Anthropic IPO November 19](https://cryptobriefing.com/anthropic-ipo-november-19-trillion-valuation/)
