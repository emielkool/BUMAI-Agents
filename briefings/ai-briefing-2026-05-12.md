---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-12
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 12 mei 2026

## 🔑 Highlights van de dag

- **Anthropic lanceert "Mythos"** – het voorlopig krachtigste model van Anthropic, beperkt uitgerold via geselecteerde partners vanwege cybersecurity-risico's. De bewuste inperking signaleert dat de AI-frontier de 'gevaarlijkheidsdrempel' serieuzer neemt.
- **EU AI Act vereenvoudiging akkoord (7 mei)** – de Europese Commissie bereikte een politiek akkoord over vereenvoudigingen van de AI Act; op 8 mei volgde een publieke consultatie over transparantierichtlijnen. Volledige inwerkingtreding op 2 augustus 2026 nadert snel.
- **Microsoft publiceert Global AI Diffusion rapport** – 17,8% van de wereldwijde beroepsbevolking gebruikt nu AI actief; in 26 landen overstijgt dat al 30%. De kloof Noord-Zuid verdubbelt nog steeds.
- **Prompt injection blijft structureel onoplosbaar** – meerdere CVE's en een nieuw "promptware kill chain"-framework tonen dat agentic AI een fundamenteel aanvalsoppervlak toevoegt dat deterministisch niet te beveiligen is.
- **Anthropic Claude Code: 23.000 engineers bij Mercado Libre** – enterprise agentic coding is voorbij het pilot-stadium. Grote organisaties meten concreet: een 50.000-regelige Python→Go-migratie in 20 uur i.p.v. 2-3 maanden.

---

## 🧠 Technologie & Modellen

**Anthropic Mythos (gelimiteerde release)**
Anthropic heeft "Mythos" uitgerold aan een selecte groep partners. Het model is beschreven als het krachtigste tot nu toe, met significante cybersecurity-toepassingen. Vanwege het misbruikpotentieel houdt Anthropic de brede beschikbaarheid bewust beperkt terwijl veiligheids- en risicoevaluaties lopen. Dit is een bewuste afwijking van het race-to-release-patroon – positief signaal voor verantwoord AI-beleid, maar ook een bevestiging dat frontier-modellen nu serieus gevaarlijk geacht worden.
*Bron: Anthropic nieuws / TechCrunch*

**Anthropic "Dreaming" – zelflerende agents**
Anthropic introduceerde een systeem genaamd "dreaming" waarbij AI-agents kunnen leren van hun eigen fouten door simulatiecycli. Dit is een architecturele doorbraak richting continuous self-improvement en heeft implicaties voor langetermijnautonomie van agents.
*Bron: [VentureBeat](https://venturebeat.com/technology/anthropic-introduces-dreaming-a-system-that-lets-ai-agents-learn-from-their-own-mistakes)*

**Open source ecosysteem groeit door**
Hugging Face publiceerde de "State of Open Source AI – Spring 2026": het platform telt nu 13 miljoen gebruikers, meer dan 2 miljoen publieke modellen en 500.000 datasets. Open-source LLMs verkleinen het gat met closed modellen in benchmarks.
*Bron: [Hugging Face Blog](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)*

---

## 🏛️ Governance & Ethiek

**EU AI Act: vereenvoudiging en transparantieconsultatie**
Op 7 mei bereikten de EU-instellingen een akkoord over vereenvoudigingen in de AI Act om meer innovators toegang te geven tot regulatory sandboxes (beschikbaar vanaf 2028). Op 8 mei opende de Commissie een consultatie over conceptrichtlijnen voor AI-transparantieverplichtingen en de markering van AI-gegenereerde content. De volledige wet is van toepassing per 2 augustus 2026 – organisaties die nog niet compliant zijn, lopen dus op de deadline.
*Bron: [EU AI Act tracker](https://artificialintelligenceact.eu/) | [Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)*

**Protest tegen AI groeit in Nederland**
PauseAI en vergelijkbare bewegingen winnen langzaam terrein in Nederland, al is de kritische massa nog beperkt. Tegelijkertijd rapporteert NOS dat docenten AI gebruiken voor het nakijken van open vragen – het maatschappelijk debat over autonomie en toezicht versnelt.
*Bron: [NOS](https://nos.nl/nieuwsuur/artikel/2613730-protest-tegen-ai-groeit-bizarre-implicaties-als-het-slimmer-wordt-dan-wij)*

---

## 🔐 Security & Risk

**Prompt injection: structureel onoplosbaar verklaard**
OpenAI bevestigde nogmaals dat prompt injection "waarschijnlijk nooit volledig opgelost zal worden" – net als social engineering op het web. Ondertussen wees Microsoft CVE-2026-21520 (CVSS 7.5) toe aan Copilot Studio: een indirecte prompt injection die data exfiltreerde ondanks een patch. Anthropic publiceerde als eerste vendor kwantitatieve aanvalsuccesratio's over vier agent-oppervlakken, wat securityteams eindelijk meetbare inkoopcriteria geeft.

Het "promptware kill chain"-framework (zeven stappen, analoog aan de Cyber Kill Chain) consolideert dit aanvalspatroon in een bruikbaar model voor verdedigers. Drie AI-codeeragents lekten secrets via een enkele prompt injection – een concreet risico voor alle teams die agentic coding inzetten.
*Bron: [VentureBeat Security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [Schneier on Security](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)*

---

## 📈 Markt & Adoptie

**Microsoft: 17,8% van wereldbevolking gebruikt AI actief**
Het "State of Global AI Diffusion 2026"-rapport van Microsoft (gepubliceerd 7 mei) toont dat adoptie stijgt van 16,3% naar 17,8% van de wereldwijde beroepsbevolking in Q1 2026. De UAE leidt met 70,1%; in 26 economieën overstijgt adoptie al 30%. De kloof tussen Noord en Zuid verdubbelt echter – een geopolitiek risico voor mondiale AI-governance.
*Bron: [Microsoft On the Issues](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)*

**Google Cloud: eerste kwartaal boven $20 miljard**
Google Cloud overschreed voor het eerst de $20 miljard kwartaalomzet (+63% YoY), gedreven door AI-workloads. Microsoft en AWS plannen gezamenlijk meer dan $500 miljard capex voor AI-infrastructuur in FY2026. Consolidatie zet door: drie hyperscalers bezitten 71% van de cloudinfrastructuurmarkt.
*Bron: [CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)*

**Enterprise AI: consolidatie naar minder vendors**
Gartner-analyse bevestigt dat Microsoft en Google de enterprise AI-markt domineren; budgetten concentreren zich bij een kleine groep vendors die aantoonbaar ROI leveren. De verwachting is dat CIOs in 2026 minder maar grotere AI-investeringen doen.
*Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)*

---

## 💡 Ctac-relevantie

**1. EU AI Act-deadline is over 12 weken**
Vollledige toepasselijkheid op 2 augustus 2026 betekent dat klanten van Ctac – met name in overheid, finance en zorg – nu compliance-programma's moeten afronden. Dit is een direct acquisitie- en adviesmoment. Ctac kan concreet helpen met AI-inventarisatie, risicoklassificatie en implementatie van transparantielogging.

**2. Agentic coding als propositie voor enterprise klanten**
De cijfers van Anthropic (80x groei, 23K engineers bij Mercado Libre) maken het zakelijk argument voor agentic coding onweerlegbaar. Ctac's AI-unit kan pilots aanbieden gebaseerd op Claude Code of vergelijkbare tooling voor klanten met softwareteams van 20+ engineers – de ROI-case schrijft zichzelf.

**3. Prompt injection = aansprakelijkheidsrisico**
Klanten die bij Ctac AI-oplossingen afnemen verwachten dat security meeontworpen is. Het promptware kill chain-framework biedt Ctac een kader om bij elke agentic implementatie een security-assessment te koppelen. Dit differentieerde waarde t.o.v. vendors die security als afterthought behandelen.

---

## 📚 Bronnen & verder lezen

- [Anthropic nieuws – Mythos & enterprise agents](https://www.anthropic.com/news)
- [Anthropic "dreaming" – VentureBeat](https://venturebeat.com/technology/anthropic-introduces-dreaming-a-system-that-lets-ai-agents-learn-from-their-own-mistakes)
- [Anthropic 2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)
- [TechCrunch – Claude Code enterprise adoptie](https://techcrunch.com/2026/02/24/anthropic-launches-new-push-for-enterprise-agents-with-plugins-for-finance-engineering-and-design/)
- [Hugging Face – State of Open Source AI Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [EU AI Act tracker – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Europese Commissie – AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Microsoft – State of Global AI Diffusion 2026](https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/)
- [Microsoft – Securing global digital ecosystem (1 mei)](https://blogs.microsoft.com/on-the-issues/2026/05/01/from-capability-to-responsibility-securing-our-global-digital-ecosystem-with-next-generation-ai/)
- [Google Cloud tops $20B – CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/)
- [Microsoft & Google domineren enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [VentureBeat – Prompt injection & agent security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Schneier – Promptware Kill Chain](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)
- [NOS – Protest tegen AI](https://nos.nl/nieuwsuur/artikel/2613730-protest-tegen-ai-groeit-bizarre-implicaties-als-het-slimmer-wordt-dan-wij)
- [Computable – AI in ziekenhuizen](https://www.computable.nl/2026/03/17/ai-in-ziekenhuis-hoge-verwachtingen-beperkte-realisatie/)
