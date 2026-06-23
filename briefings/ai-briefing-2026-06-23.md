---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-23
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 23 juni 2026

## 🔑 Highlights van de dag

- **Fable 5 wordt betaald model (vandaag)**: Anthropic's krachtigste publieke model Claude Fable 5 is per 23 juni niet langer inbegrepen in Pro/Team/Enterprise-abonnementen. Voortgezet gebruik vereist nu usage credits à $10/$50 per miljoen tokens (in/out). Tijdelijk of permanent — onduidelijk.
- **Exploit-snelheid explodeert**: De gemiddelde tijd tussen publicatie van een kwetsbaarheid en actieve exploitatie is gedaald van 53 dagen (2024) naar **24 uur** (2026). AI-tooling stelt aanvallers in staat exploits op machinesnelheid te bouwen.
- **EU AI Act-klok tikt**: Volledige toepasselijkheid per **2 augustus 2026** — nog zes weken. Elke lidstaat moet dan een AI regulatory sandbox hebben; nationale autoriteiten moeten aangewezen zijn. Nederland en België lopen achter schema.
- **Microsoft Agent 365 algemeen beschikbaar**: Shadow AI wordt officieel enterprise-risicomanagement. Context mapping, runtime-blocking en policy controls via Intune/Defender voor tot 18 agent-types (o.a. Claude Code en GitHub Copilot CLI).
- **Benelux AI-adoptie: koploper met talentprobleem**: NL 61%, BE 62% van bedrijven gebruikt AI (stijging ~10 pp in één jaar). Maar 58% ziet gebrek aan digitale vaardigheden als grootste belemmering voor verdere opschaling.

---

## 🧠 Technologie & Modellen

**Claude Fable 5 – pricing shift per vandaag**
Anthropic's krachtigste publiek beschikbare model (gelanceerd 9 juni) verlaat vandaag de standaard abonnementen. Fable 5 was tot 22 juni gratis inbegrepen in Pro, Max, Team en seat-based Enterprise. Vanaf 23 juni vereist het gebruik credits op API-tarieven: **$10 per miljoen inputtokens en $50 per miljoen outputtokens** — het duurste algemeen beschikbare frontier-model, dubbel zo duur als Opus 4.8. Anthropic belooft restauratie in abonnementen "zodra capaciteit het toelaat", zonder concrete datum.
→ Bron: [Anthropic Fable 5 pricing](https://www.anthropic.com/news/claude-fable-5-mythos-5) | [Developers Digest deadline-analyse](https://www.developersdigest.tech/blog/claude-fable-5-june-22-deadline)

**GLM-5.2 – open-weights uitdager van GPT-5.5**
Z.ai heeft GLM-5.2 uitgebracht: een 753 miljard parameter open-weights model (MIT-licentie) met een 1-miljoen-token contextvenster. Volgens VentureBeat scoort het model op meerdere long-horizon coding benchmarks beter dan GPT-5.5, voor één zesde van de kosten. Dit is een significante stap voor de open-source frontier: enterprise-klasse codeerondersteuning zonder vendor lock-in.
→ Bron: [VentureBeat – GLM-5.2](https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost)

---

## 🏛️ Governance & Ethiek

**EU AI Act: nog zes weken tot volledige toepassing**
Per 2 augustus 2026 treedt de AI Act volledig in werking. Kernvereisten: verplichte conformiteitsbeoordeling voor hoog-risico AI, transparantie over GPAI-modellen, en operationele regulatory sandboxes per lidstaat. In mei 2026 werd een politiek akkoord bereikt over vereenvoudiging van de regels, maar de kern-verplichtingen staan. Voor bedrijven die nu nog in pilotfase zitten en hoog-risico toepassingen bouwen, is de tijdsdruk reëel.
→ Bron: [AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/) | [EC digitale strategie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

**Vlam: soevereine AI voor de Rijksoverheid**
Het Nederlandse rijksplatform Vlam (Veilige Lokale AI Modellen), door SSC-ICT en AIVD ontwikkeld als alternatief voor ChatGPT/Claude/Gemini, krijgt in H2 2026 een brede productie-uitrol. Data, modellen en infrastructuur blijven volledig onder Nederlandse controle. Dit is hét voorbeeld van soevereine AI in de publieke sector — en een potentieel referentie-architectuur voor overheidsklanten van Ctac.
→ Bron: [Computable – Vlam](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/)

---

## 🔐 Security & Risk

**Exploit-tijd gekelderd door AI-tooling**
Verizon's 2026 DBIR meldt dat de gemiddelde time-to-exploit gedaald is van ~53 dagen (2024) naar ~24 uur (2026). AI coding assistants stellen aanvallers in staat exploits te bouwen op machinesnelheid. Tegelijkertijd duurt het gemiddeld 74 dagen om een bekende high/critical CVE te patchen — een gevaarlijke tijdkloof van drie maanden.
→ Bron: [The Hacker News – AI broke vulnerability management](https://thehackernews.com/2026/06/ai-broke-vulnerability-management-thats.html) | [Schneier on Security](https://www.schneier.com/blog/archives/2026/06/vulnerability-disclosure-in-the-age-of-ai.html)

**Shadow AI als enterprise blinde vlek**
Medewerkers adopteren AI-tools buiten IT-zichtbaarheid om, waardoor security controls worden omzeild. Een relatief kleine groep "power users" drijft een disproportioneel groot deel van het enterprise AI-risico. Microsoft adresseert dit met runtime-blocking via Defender voor ontdekte lokale agents (Claude Code, GitHub Copilot CLI). Andere vendors volgen.
→ Bron: [The Hacker News – Shadow AI](https://thehackernews.com/2026/04/the-hidden-security-risks-of-shadow-ai.html)

---

## 📈 Markt & Adoptie

**Microsoft Agent 365: van preview naar GA**
Agent 365 is algemeen beschikbaar met context mapping (relatiemap van agents, MCP-servers, identiteiten en cloud resources), policy-based controls en runtime-blocking. Microsoft positioneert ungoverned AI agents als "corporate double agents" en vraagt $99/maand voor de governance-laag. Dit signaleert dat AI agent governance een volwassen product-categorie wordt.
→ Bron: [VentureBeat – Agent 365](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)

**AWS: $10 miljard datacenter-investering in North Carolina**
AWS investeert $10 miljard in North Carolina AI-datacenters als onderdeel van een totale capex van $100 miljard dit jaar. Google Cloud meldt dat bijna 75% van haar klanten AI-producten inzet. Ondertussen zit twee derde van de bedrijven wereldwijd nog vast in pilot-fase — de kloof tussen vroege adoptie en productie-implementatie is de strategische uitdaging van dit moment.
→ Bron: [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/) | [CIO Dive – Microsoft Google](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

---

## 💡 Ctac-relevantie

**Fable 5-prijswijziging raakt klanten direct.** Teams die Claude Fable 5 gebruiken in pilots of productie moeten hun kostenmodellen herzien. Ctac kan klanten nu ondersteunen bij een afweging: doorgaan met Fable 5 (credits), overstappen naar een goedkoper open-weights alternatief als GLM-5.2, of een hybride aanpak. Dit is een concrete adviesopening vandaag.

**EU AI Act: 6 weken.** Klanten in hoog-risico sectoren (overheid, zorg, finance) moeten conformiteitsbeoordelingen afronden. Ctac's AI-unit kan hier als sparring partner optreden. De Vlam-uitrol is een specifieke kans: overheidsklanten zoeken soevereine AI-implementaties — exact het segment waar Ctac actief is.

**Agent governance = nieuwe dienst.** De combinatie van shadow AI als risico en Microsoft Agent 365 als oplossing opent een nieuwe adviesmarkt: AI governance frameworks voor enterprise-klanten. Ctac kan hierin een regie-rol pakken, los van welke vendor de klant al gebruikt.

**Talentschaarste in Benelux.** Met 58% van bedrijven die digitaal talent als bottleneck noemen, is er ruimte voor Ctac om niet alleen technologie maar ook kennis en capaciteit te leveren. Opleidingstrajecten en embedded AI-engineers zijn product-kansen.

---

## 📚 Bronnen & verder lezen

- [Anthropic – Claude Fable 5 & Mythos 5 aankondiging](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Developers Digest – Fable 5 June 22 deadline](https://www.developersdigest.tech/blog/claude-fable-5-june-22-deadline)
- [VentureBeat – GLM-5.2 open-weights model](https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Europese Commissie – AI Act governance](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Computable – Vlam rijksoverheid AI-platform](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/)
- [The Hacker News – AI broke vulnerability management](https://thehackernews.com/2026/06/ai-broke-vulnerability-management-thats.html)
- [Schneier on Security – Vulnerability Disclosure in de AI-era](https://www.schneier.com/blog/archives/2026/06/vulnerability-disclosure-in-the-age-of-ai.html)
- [VentureBeat – Microsoft Agent 365 GA](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Computable – Benelux koploper AI adoptie](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
