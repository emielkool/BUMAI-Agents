---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-14
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 14 mei 2026

## 🔑 Highlights van de dag

- **Enterprise AI als georganiseerde industrie:** OpenAI en Anthropic lanceerden begin mei allebei een enterprise joint venture om AI-adoptie bij mid-market bedrijven te versnellen — de markt consolideert zich razendsnel rondom enkele dominante spelers.
- **MCP wordt open standaard:** Anthropic doneert het Model Context Protocol aan de Agentic AI Foundation (Linux Foundation), mede opgericht door OpenAI. Agentische interoperabiliteit wordt daarmee infrastructuur, niet meer een concurrentievoordeel.
- **EU AI Act over de drempel:** Op 7 mei bereikte de AI omnibus politiek akkoord; per 2 augustus 2026 gelden transparantieverplichtingen en GPAI-enforcement voor alle aanbieders in de EU.
- **AI-gestuurde aanvallen versnellen dramatisch:** 28,3% van nieuwe kwetsbaarheden wordt binnen 24 uur uitgebuit; onderzoekers ontdekten de eerste bekende AI-ontwikkelde zero-day voor 2FA-bypass. Shadow AI vergroot het aanvalsoppervlak verder.
- **Eerste AI-agent betaling in Nederland:** Mastercard en Rabobank voerden de eerste betaling via een AI-agent uit — een signaal dat financiële dienstverlening in NL actief experimenteert met autonome workflows.

---

## 🧠 Technologie & Modellen

**MCP naar Linux Foundation** — Anthropic en OpenAI richtten gezamenlijk de *Agentic AI Foundation* op onder de Linux Foundation. Anthropic doneert het Model Context Protocol als open standaard voor agent-naar-tool communicatie. Dit is strategisch belangrijk: MCP was de facto standaard, maar nu wordt het governance-neutraal. Voor iedereen die agentische systemen bouwt, verdwijnt het risico van vendor lock-in op protocol-niveau. ([Anthropic](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) / [OpenAI](https://openai.com/index/agentic-ai-foundation/))

**DeepSeek V4 preview** — DeepSeek toonde een preview van V4: 1,6 biljoen parameters (49 miljard actief via MoE), het grootste open-weight model dat beschikbaar is. Het model "dicht de kloof met frontier modellen" volgens TechCrunch. Interessant voor use cases waarbij open-source deployment gewenst is zonder Anthropic- of OpenAI-afhankelijkheid. ([TechCrunch](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/))

**Anthropic Agent Skills** — Anthropic maakte de enterprise *Agent Skills*-standaard open source, waarmee bedrijven herbruikbare, deelbare agent-capabilities kunnen definiëren. Dit zet druk op OpenAI's gesloten agentische ecosysteem. ([VentureBeat](https://venturebeat.com/technology/anthropic-launches-enterprise-agent-skills-and-opens-the-standard))

---

## 🏛️ Governance & Ethiek

**AI Act omnibus: politiek akkoord** — Op 7 mei 2026 bereikte de Europese AI omnibus politiek akkoord na stemming op 19 november 2025. Per **2 augustus 2026** zijn transparantieverplichtingen en GPAI-enforcement van kracht; organisaties moeten gebruikers informeren wanneer zij interacteren met AI-systemen. Hoog-risico toepassingen (o.a. biometrie, onderwijs, arbeidsmarkt) volgen pas per december 2027. Dit geeft implementatieteams nog enige ruimte, maar de basisverplichtingen komen eraan. ([EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines) / [AI Act tracker](https://artificialintelligenceact.eu/))

**Verbod op AI naaktmakings-apps** — Onderdeel van het omnibus-akkoord is een expliciet verbod op AI-systemen die niet-consensuele seksueel expliciete beelden genereren. België steunde dit voorstel actief.

---

## 🔐 Security & Risk

**Scan van 1 miljoen blootgestelde AI-diensten** — The Hacker News publiceerde bevindingen van een grootschalige scan: AI-infrastructuur blijkt vaker kwetsbaar en misconfigureerd dan welk ander software-type dan ook. Hardcoded credentials, onveilige Docker-setups en root-draaiende applicaties domineren het beeld. ([The Hacker News](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html))

**Eerste AI-ontwikkelde zero-day voor 2FA-bypass** — Hackers gebruikten AI om een zero-day te ontwikkelen die tweefactorauthenticatie omzeilt op een populair open-source beheertool. Exploitatie volgde snel na disclosure. ([The Hacker News](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known-zero-day-2fa-bypass-for-mass-exploitation.html))

**Shadow AI: 67% van CISOs heeft beperkt zicht** — Onderzoek toont dat twee derde van de Chief Information Security Officers weinig tot geen inzicht heeft in hoe AI binnen hun organisatie gebruikt wordt. In NL: KnowBe4 meldt dat 86% van phishingaanvallen inmiddels AI-aangestuurd is. ([The Hacker News](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai-in-enterprises.html) / [Computable](https://www.computable.nl/persberichten/knowbe4-86-van-phishingaanvallen-wordt-aangestuurd-door-ai/))

---

## 📈 Markt & Adoptie

**OpenAI & Anthropic enterprise JVs** — Begin mei lanceerden beide labs enterprise joint ventures. Anthropic gaat samen met Blackstone, Hellman & Friedman en Goldman Sachs een nieuwe AI-dienstverlener oprichten voor mid-market bedrijven. OpenAI's *The Development Company* haalde $4 miljard op tegen een waardering van $10 miljard. Het model: alternatieve vermogensbeheerders investeren én worden klant via preferred access. ([TechCrunch](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/))

**Pentagon-deals met Nvidia, Microsoft en AWS** — Het Amerikaanse Ministerie van Defensie sloot contracten met de drie partijen voor AI-deployment op geclassificeerde netwerken. 1,3 miljoen DoD-medewerkers hebben toegang tot het GenAI.mil-platform. ([TechCrunch](https://techcrunch.com/2026/05/01/pentagon-inks-deals-with-nvidia-microsoft-and-aws-to-deploy-ai-on-classified-networks/))

**Mastercard + Rabobank: AI-agent betaling in NL** — De twee partijen voerden de eerste betaling via een AI-agent uit in Nederland. Klein experiment, maar relevant signaal voor financiële dienstverlening in de Benelux. ([Computable](https://www.computable.nl/2026/05/05/kort-ai-ontslagen-betekenen-zelden-hoger-rendement-ai-moet-maakindustrie-verslimmen-en-meer/))

---

## 💡 Ctac-relevantie

**Enterprise AI JVs als kanaalstrategie** — De constructies van OpenAI en Anthropic laten zien hoe enterprise AI-adoptie bij mid-market bedrijven verloopt: via gestructureerde partnership-programma's met preferred access. Voor Ctac is dit relevant als IT-consultancybedrijf: positionering als preferred implementation partner binnen zulke ecosystemen (bijv. Anthropic's Claude Partner Network of OpenAI's enterprise kanaal) biedt structurele dealflow.

**MCP-standaardisatie versnelt agentische projecten** — Nu MCP governance-neutraal is, vermindert het technisch risico bij het bouwen van agentische systemen voor klanten. Ctac kan dit als argument inzetten richting klanten die aarzelen door vendor lock-in-zorg.

**Shadow AI en AI Act als gecombineerde propositie** — De combinatie van naderende AI Act-verplichtingen (augustus 2026) en breed zichtbare shadow AI-risico's biedt Ctac een concrete aanleiding voor klantgesprekken: AI-governance scans, beleidskaders en veilige adoptietrajecten zijn nu urgenter dan ooit — met een harde deadline.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI & Anthropic enterprise JVs](https://techcrunch.com/2026/05/04/anthropic-and-openai-are-both-launching-joint-ventures-for-enterprise-ai-services/)
- [Anthropic – Donating MCP & Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)
- [OpenAI – Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/)
- [TechCrunch – DeepSeek V4 preview](https://techcrunch.com/2026/04/24/deepseek-previews-new-ai-model-that-closes-the-gap-with-frontier-models/)
- [EC Digital Strategy – AI Act implementatie](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [The Hacker News – 1 miljoen blootgestelde AI-diensten](https://thehackernews.com/2026/05/we-scanned-1-million-exposed-ai.html)
- [The Hacker News – AI zero-day 2FA bypass](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known-zero-day-2fa-bypass-for-mass-exploitation.html)
- [The Hacker News – Shadow AI risico's](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai-in-enterprises.html)
- [TechCrunch – Pentagon deals Nvidia/Microsoft/AWS](https://techcrunch.com/2026/05/01/pentagon-inks-deals-with-nvidia-microsoft-and-aws-to-deploy-ai-on-classified-networks/)
- [VentureBeat – Anthropic Agent Skills open source](https://venturebeat.com/technology/anthropic-launches-enterprise-agent-skills-and-opens-the-standard)
- [Computable – KnowBe4 phishing 86% AI](https://www.computable.nl/persberichten/knowbe4-86-van-phishingaanvallen-wordt-aangestuurd-door-ai/)
- [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
