---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-21
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 21 mei 2026

## 🔑 Highlights van de dag

- **EU AI Act vereenvoudigd:** De EU bereikte op 7 mei een akkoord om de regels voor hoog-risico AI te vereenvoudigen en de implementatiedeadline te verschuiven naar 2027/28 — meer ruimte voor innovatie, maar ook minder druk voor compliance-teams op korte termijn.
- **Anthropic Mythos alarmeert securitywereld:** Het nieuwe Mythos-model vond zelfstandig duizenden kritieke kwetsbaarheden, waaronder een 17 jaar oude RCE-bug in FreeBSD. Toegang is bewust beperkt; Anthropic start Project Glasswing om kritieke software actief te beschermen.
- **Google lanceert Gemini 3.5 Flash en Spark:** Google versterkt zijn positie met een goedkoper frontier-model en een nieuw algemeen AI-agent-platform — directe concurrentie met OpenAI's agent-aanbod.
- **Microsoft Agent 365 nu beschikbaar:** Microsofts platform voor het beheren van AI-agents (GA per 1 mei) biedt governance over eigen én derde-partij agents voor €15/user/maand — governance wordt een product.
- **Prompt injection: tier-1-risico, nauwelijks voorbereiding:** Slechts 29% van de organisaties is voorbereid op agentic AI-security, terwijl indirecte prompt injection nu de dominante aanvalsvector is.

---

## 🧠 Technologie & Modellen

**Google Gemini 3.5 Flash & Spark** — Google lanceerde Gemini 3.5 Flash, een lichtgewicht frontier-model met vergelijkbare prestaties als zwaardere modellen maar tegen een derde van de kosten. Daarnaast introduceerde Google Gemini Spark, een algemeen AI-agent in de Gemini-app die redeneert over verbonden applicaties. Dit is een gerichte zet om zowel het kostenvoordeel als het agent-ecosysteem te versterken tegenover OpenAI.
*(Bron: [CNBC](https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html))*

**OpenAI GPT-5.4 "Thinking"** — OpenAI's meest recente model scoort 83% op de GDPVal-benchmark, wat neerkomt op of boven het niveau van menselijke experts op economisch waardevolle taken. Agentic samenwerking (meerdere agents die samenwerken) is de volgende wave die OpenAI aan het voorbereiden is.
*(Bron: [Fortune / MIT Tech Review](https://www.technologyreview.com/2026/04/21/1135643/10-ai-artificial-intelligence-trends-technologies-research-2026/))*

**Open-source ecosysteem groeit door:** Hugging Face telt inmiddels meer dan 1 miljoen modellen en 2 miljoen gebruikers. Sterkste open-weight opties voor productie: Qwen3, Gemma 4 (Apache 2.0) en Phi-4, DeepSeek R1 (MIT). Open-weight modellen zijn productie-rijp voor coding, reasoning en agentic workflows.
*(Bron: [Hugging Face Blog](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026))*

---

## 🏛️ Governance & Ethiek

**EU AI Act: akkoord over vereenvoudiging en uitstel** — Op 7 mei bereikten de EU Raad en het Europees Parlement een voorlopig akkoord over gerichte aanpassingen van de AI Act (onderdeel van het Digital Omnibus-pakket). De implementatie van regels voor hoog-risico AI wordt uitgesteld tot 2027/28. Meer innovatoren krijgen toegang tot regulatory sandboxes, inclusief een EU-level sandbox. De bevoegdheden van het AI Office worden versterkt en gecentraliseerd voor het toezicht op systemen gebaseerd op general-purpose AI-modellen.

**Strategische lezing:** Dit is positief voor Ctac en haar klanten — meer ruimte om te experimenteren zonder directe compliance-druk op hoog-risico toepassingen. Tegelijk: wie nu governance-processen opzet, heeft een voorsprong als de regels alsnog van kracht worden.
*(Bronnen: [EU Raad](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/), [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [artificialintelligenceact.eu](https://artificialintelligenceact.eu/))*

---

## 🔐 Security & Risk

**Anthropic Mythos: krachtig én riskant** — Het Mythos-model identificeerde en exploiteerde zelfstandig een 17-jaar oude RCE-kwetsbaarheid in FreeBSD (CVE-2026-4747) zonder menselijke tussenkomst. Ook meerdere Linux kernel-flaws werden gevonden en aaneengeschakeld voor volledige systeemovername. Anthropic beperkt toegang bewust tot Apple, Amazon, JPMorgan Chase en Palo Alto Networks. Via Project Glasswing wordt Mythos ingezet om kritieke software proactief te beschermen.

**Kritisch:** Dit is geen hype. Een model dat autonome exploit-chains kan genereren, verschuift het dreigingslandschap fundamenteel. De asymmetrie — aanvallers exploiteren in uren, verdedigers patchen in weken — maakt dit urgent voor enterprise security-teams.
*(Bronnen: [CNBC](https://www.cnbc.com/2026/05/08/anthropic-mythos-ai-cybersecurity-banks.html), [Dark Reading](https://www.darkreading.com/cybersecurity-operations/anthropic-mythos-cyber-what-comes-next), [Axios](https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks))*

**Prompt injection: tier-1-risico** — Slechts 29% van organisaties die agentic AI inzetten, rapporteert voorbereid te zijn op de bijbehorende securityrisico's. Indirecte prompt injection — waarbij kwaadaardige instructies verstopt zitten in documenten of websites die een AI-agent raadpleegt — is de meest impactvolle aanvalsvorm. Klassieke SQL-injection-verdedigingen zijn een nuttig analogie, maar AI-systemen lopen nog verder achter.
*(Bronnen: [Airia](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/), [TechRepublic](https://www.techrepublic.com/article/news-ai-agents-prompt-injection-data-security/))*

---

## 📈 Markt & Adoptie

**Enterprise AI-adoptie verdubbeld in één jaar:** Organisatiebrede AI-adoptie steeg van 22% (2025) naar 40% (2026), gedreven door agentic workflows en hyperautomatisering. Globale AI-investeringen overstijgen $650 miljard per jaar. Twee derde van de bedrijven zit echter nog vast in pilot-fase — de overgang naar productie blijft de bottleneck.
*(Bron: [GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/05/3288006/0/en/AI-Investment-Activity-to-Surpass-650-Billion-Annually-as-Enterprise-Adoption-Accelerates-Toward-2026.html))*

**Microsoft Agent 365 – GA:** Beschikbaar per 1 mei voor $15/user/maand, onderdeel van het nieuwe Microsoft 365 E7-pakket ($99/user/maand met Copilot + security). Agent 365 biedt centraal beheer, governance en beveiliging van AI-agents — inclusief derde-partij agents op AWS Bedrock en Google Cloud. Shadow AI-detectie via Defender en Intune is ingebakken.
*(Bron: [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/))*

**Google Cloud groeit 63% YoY** naar $20 miljard omzet; Microsoft verhoogt capex naar >$40 miljard. De hyperscalers verdubbelen hun inzet — het infrastructure-spel is bepalend voor welk AI-platform enterprise-dominant wordt.
*(Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))*

---

## 💡 Ctac-relevantie

**Agent governance wordt een must-have propositie.** Microsoft Agent 365 maakt AI-governance voor enterprise-afnemers tastbaar en geprijsd ($15/user/maand). Ctac kan hier direct op inhaken: klanten die Copilot of andere AI-agents uitrollen, hebben behoefte aan begeleiding bij het opzetten van governance-processen, policies en security-controles. Dit is een concrete implementatiepropositie die aansluit op bestaande Microsoft-partnerships.

**Prompt injection als adviesingang.** Het lage niveau van enterprise-voorbereiding (29%) is een opening voor Ctac's AI-unit: een security-quickscan voor agentic AI-omgevingen, inclusief prompt injection-risicoanalyse, is een laagdrempelige en urgente dienst die waarde toevoegt zonder grote implementatietrajecten te vereisen.

**EU AI Act uitstel: tijd benutten.** Het uitstel van hoog-risico AI-regels tot 2027/28 biedt klanten in gereguleerde sectoren (overheid, finance, zorg) extra tijd — maar Ctac kan nu juist het verschil maken door governance-frameworks proactief te implementeren terwijl de druk nog laag is.

---

## 📚 Bronnen & verder lezen

- [CNBC – Google debuts Gemini 3.5 Flash & Spark](https://www.cnbc.com/2026/05/19/google-ai-ultra-gemini-spark-omni.html)
- [EU Raad – AI Act vereenvoudiging akkoord (7 mei)](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [EC Digital Strategy – EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [artificialintelligenceact.eu – Implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [CNBC – Anthropic Mythos cybersecurity hysteria](https://www.cnbc.com/2026/05/08/anthropic-mythos-ai-cybersecurity-banks.html)
- [Axios – Anthropic withholds Mythos Preview](https://www.axios.com/2026/04/07/anthropic-mythos-preview-cybersecurity-risks)
- [Dark Reading – Anthropic Mythos: what comes next for cyber](https://www.darkreading.com/cybersecurity-operations/anthropic-mythos-cyber-what-comes-next)
- [Microsoft Security Blog – Agent 365 GA](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)
- [CIO Dive – Microsoft & Google rule AI vendor market](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Airia – Prompt Injection & the Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Hugging Face – State of Open Source Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [GlobeNewswire – AI Investment $650B annually](https://www.globenewswire.com/news-release/2026/05/05/3288006/0/en/AI-Investment-Activity-to-Surpass-650-Billion-Annually-as-Enterprise-Adoption-Accelerates-Toward-2026.html)
