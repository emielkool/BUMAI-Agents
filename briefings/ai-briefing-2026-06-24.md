---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-24
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 24 juni 2026

## 🔑 Highlights van de dag

- **Anthropic lanceert Claude Fable 5 & Mythos 5** – State-of-the-art op vrijwel alle benchmarks, en voor minder dan de helft van de prijs van de vorige topmodellen. Dit is een directe strategische aanval op OpenAI's marktpositie én een kans voor enterprise-adoptieversnelling.
- **EU AI Act: volle toepasselijkheid over zes weken** – Per 2 augustus 2026 is de AI Act volledig van kracht. De stakeholderconsultatie over hoog-risico richtlijnen sloot gisteren (23 juni); organizations die nog niet compliant zijn, hebben amper tijd.
- **Exploit-window ingekort tot 24 uur** – AI-tools versnellen aanvallen zo drastisch dat gemiddeld 28% van CVE's binnen een dag na openbaarmaking al wordt misbruikt. Klassiek vulnerability management werkt niet meer.
- **Microsoft 365 Copilot: 20 miljoen betaalde seats** – Jaaromzet AI-business 123% gegroeid naar $37 miljard ARR. De enterprise-race is niet meer theoretisch; Microsoft loopt weg.
- **Agent Control Specification (ACS)** – Microsoft publiceert open-source standaard voor het controleren van AI-agentgedrag; cruciaal voor enterprise governance van autonome agenten.

---

## 🧠 Technologie & Modellen

**Anthropic – Claude Fable 5 & Claude Mythos 5**
Anthropic heeft vandaag Claude Fable 5 en Mythos 5 aangekondigd. Fable 5 presteert state-of-the-art op vrijwel alle gangbare benchmarks en excelleert in software engineering, kenniswerk, vision en wetenschappelijk redeneren. Opvallend: de prijs daalt met meer dan 50% ten opzichte van Mythos Preview – $10/M input, $50/M output tokens. Anthropic heeft tegelijkertijd confidentieel een IPO-aanvraag ingediend na een Series H van $65 miljard (waardering $965 miljard).
Bron: [Anthropic – Claude Fable 5 & Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

**Google – Gemini Omni Flash & DiffusionGemma**
Google rolde Gemini Omni Flash uit naar alle AI-abonnementen. Daarnaast lanceerde het op 10 juni DiffusionGemma: een experimenteel open model dat tot 4× snellere tekstgeneratie biedt op GPU's. DiffusionGemma is veelbelovend voor inference-optimalisatie en on-premise toepassingen.
Bronnen: [Gemini Omni](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/) | [DiffusionGemma](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)

**Microsoft – eigen modellen & Agent Control Specification**
Op Microsoft Build (2 juni) onthulde Microsoft eigen AI-modellen om afhankelijkheid van OpenAI te verminderen. Bovendien publiceerde het de open-source **Agent Control Specification (ACS)**: een standaard waarmee ontwikkelaars granulaire controle krijgen over wat AI-agenten mogen doen. Work IQ APIs kwamen op 16 juni GA – een intelligentielaag die agenten organisatiecontext geeft.
Bronnen: [Microsoft Build 2026 blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/) | [TechCrunch ACS](https://techcrunch.com/2026/06/02/microsoft-offers-devs-a-better-way-to-control-ai-agent-behavior/)

---

## 🏛️ Governance & Ethiek

**EU AI Act: T-minus 6 weken**
Volledige toepasselijkheid van de AI Act is op 2 augustus 2026. De Europese Commissie sloot gisteren (23 juni) de publieke consultatie over hoog-risico classificatierichtlijnen. In de loop van 2026 komen ook richtlijnen voor transparantievereisten (art. 50), incident-reporting en verplichtingen voor deployers van hoog-risico systemen. Iedere EU-lidstaat moet vóór 2 augustus minimaal één regulatory sandbox hebben ingericht.

De eerder aangekondigde **AI Omnibus** – een vereenvoudigingspakket voor het MKB – bereikte op 7 mei 2026 een politiek akkoord. Dit verlicht de nalevingslasten voor kleinere aanbieders.
Bronnen: [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/) | [EC richtlijnen](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)

---

## 🔐 Security & Risk

**Exploit-window ingekort tot 24 uur**
Volgens recent onderzoek is de gemiddelde tijd tussen CVE-openbaarmaking en eerste actieve exploitatie gedaald naar ~24 uur (2024: ~53 dagen). AI-tools stellen aanvallers in staat exploits razendsnel te bouwen en in te zetten. 28,3% van CVE's wordt al binnen een dag uitgebuit. De gemiddelde remediatietijd blijft 74 dagen – een gevaarlijk gat.

**CISOs verlaten klassiek vulnerability management**
AI heeft het vulnerability management als discipline fundamenteel gebroken, aldus Hacker News. CISOs verschuiven budgetten richting Breach & Attack Simulation (BAS), dat continu geautomatiseerd test of aanvalspaden werken. Klassieke patchmanagement-cycli zijn te traag voor het nieuwe dreigingslandschap.
Bronnen: [Schneier on Security – Vulnerability Disclosure in the Age of AI](https://www.schneier.com/blog/archives/2026/06/vulnerability-disclosure-in-the-age-of-ai.html) | [THN – AI broke vulnerability management](https://thehackernews.com/2026/06/ai-broke-vulnerability-management-thats.html)

---

## 📈 Markt & Adoptie

**Microsoft domineert enterprise-AI**
Microsoft 365 Copilot telt inmiddels meer dan 20 miljoen betaalde seats; het aantal klanten met 50.000+ seats verviervoudigde jaar-op-jaar. De jaarlijkse AI-omzet oversteeg $37 miljard ARR (+123% YoY). Agent 365 verliet preview en is nu GA voor enterprise. Twee derde van bedrijven zit echter nog vast in pilot-fase en slaagt er niet in AI naar productie te brengen.
Bronnen: [CIO Dive – Microsoft Google markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [VentureBeat – Agent 365](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)

**AWS Bedrock AgentCore**
Amazon lanceerde op de AWS Summit New York 2026 AgentCore: een managed platform voor het bouwen, deployen en beveiligen van autonome AI-agenten op schaal. Werkt met elk framework en foundation model.
Bron: [AWS Summit NY 2026](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/)

**OpenAI IPO in de maak**
OpenAI werkt aan een vertrouwelijke IPO-aanvraag via Goldman Sachs en Morgan Stanley, mogelijk al in september 2026. Samen met Anthropic's gelijktijdige filing markeert dit een consolidatiemoment voor de sector: de hyperscaler-fase begint.

---

## 💡 Ctac-relevantie

**Onmiddellijk:**
- **EU AI Act deadline nadert razendsnel.** Klanten die nog in pilot-fase zitten met hoog-risico toepassingen (HR, kredietbeoordeling, veiligheidssystemen) moeten nú in actie komen. Ctac kan hier direct mee helpen met compliance-assessments en implementatie van AI governance frameworks. De consultatie die gisteren sloot maakt ook duidelijk dat de definitieve richtlijnen van de EC nog uitkomen – er is ruimte om klanten nu alvast te positioneren als early adopters van compliance.

**Strategisch:**
- **Anthropic's prijsdaling op Fable 5** maakt het aantrekkelijker om Claude-modellen in te zetten naast of in plaats van GPT-4-klasse modellen. Voor Ctac's AI-unit is het waardevol om de prestaties en prijspunten te evalueren als basis voor klantproposities.
- **Microsoft ACS & Agent 365 GA:** Ctac's klanten in de Microsoft-stack kunnen nu serieus agentische workflows implementeren. ACS biedt de governance-laag die enterprise-klanten vragen. Dit is een concreet haakje voor Ctac-proposities rond Microsoft 365 Copilot en Azure AI Foundry.
- **Security is het nieuwe compliance-gesprek.** De drastische verkorting van exploit-windows maakt AI-security tot een boardroom-onderwerp. Ctac kan de combinatie van AI-adoptie en AI-security als integrale dienst positioneren – niet als afzonderlijke trajecten.

---

## 📚 Bronnen & verder lezen

- [Anthropic – Claude Fable 5 & Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [EU AI Act – Implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Richtlijnen voor hoog-risico AI-systemen](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems)
- [Microsoft Build 2026 – Officieel blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [TechCrunch – Microsoft Agent Control Specification](https://techcrunch.com/2026/06/02/microsoft-offers-devs-a-better-way-to-control-ai-agent-behavior/)
- [VentureBeat – Microsoft Agent 365 GA](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [CIO Dive – Microsoft/Google enterprise AI markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [The Hacker News – AI broke vulnerability management](https://thehackernews.com/2026/06/ai-broke-vulnerability-management-thats.html)
- [Schneier on Security – Vulnerability disclosure in the age of AI](https://www.schneier.com/blog/archives/2026/06/vulnerability-disclosure-in-the-age-of-ai.html)
- [AWS Summit NY 2026 – AgentCore](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/)
- [Google – Gemini Omni Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/)
- [Google – DiffusionGemma](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)
