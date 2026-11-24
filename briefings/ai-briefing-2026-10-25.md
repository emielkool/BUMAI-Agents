---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-25
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 25 oktober 2026

## 🔑 Highlights van de dag

- **Block Dessa** (gisteren gepubliceerd): een full-duplex spraakmodel dat op consumerhardware draait. Het klinkt "griezelig menselijk" en is nu alleen beschikbaar voor veiligheidstesters. Een nieuwe drempel in realtime voice-AI.
- **Microsoft waarschuwt voor AI-gestuurde cyberaanvallen**: Nederlandse en internationale CISO's kregen afgelopen week te horen dat organisaties soms nog maar drie uur hebben om aanvallers te stoppen die met AI-agents werken. De dreiging is niet theoretisch meer.
- **SAP koopt Belgisch Techwolf**: SAP heeft de Belgische HR-tech speler Techwolf overgenomen om zijn agentische HR-functionaliteit te versterken. Relevant voor klanten in de Ctac-portfolio die met SAP SuccessFactors werken.
- **Meta Muse Spark Open** (816B parameters, open-weight): het grootste open model tot nu toe, maar let op: de licentie is geen OSI-approved open source. Het draait alleen op Apple silicon met ~1 TB RAM — indrukwekkend als graadmeter, minder als directe inzet.
- **Prompt injection blijft onopgelost**: OWASP noemt het "een onopgelost architectuurprobleem". Nieuwe CVE's tonen aan dat coding agents in productie kwetsbaar zijn via indirect geplaatste instructies in externe documenten of repositories.

---

## 🧠 Technologie & Modellen

De modelrace in oktober ging onverminderd door. **GPT-6 Sol en Luna** zijn nu breed uitgerold in ChatGPT; Sol voor betalende tiers, Luna gratis. OpenAI classificeert GPT-6 als "hoog capabel" in cybersecurity en bio/chemische domeinen — wat meteen vragen oproept over veiligheidsmaatregelen. De **OpenAI Decisions API** (beslismodel) is nu beschikbaar voor alle klanten, na aankondiging op Developer Day in september.

**Anthropic Claude Haiku 5.5** (gepubliceerd begin oktober) positioneert zich als de snelste, goedkoopste kleine model voor high-volume toepassingen. Relevante toevoeging voor Ctac als de focus op inference-kosten toeneemt.

**NVIDIA Nemotron 3.5 Super VL** (120B parameters, 19 oktober) richt zich specifiek op enterprise agents en multimodale taken, plus kleinere Bolt-modellen voor PC-inzet. NVIDIA versterkt zijn positie als AI-platform, niet alleen als chipaanbieder.

**Aleph Alpha Kolibri 1** (78B MoE, Apache 2.0, vroeg oktober): een Duits-Engels open model van de Europese AI-speler — interessant voor klanten in overheidssectoren die data-soevereiniteit hoog in het vaandel hebben.

*Kanttekening:* de benchmarkclaims van zowel Meta als Reflection (Beam-model) zijn op dit moment niet onafhankelijk geverifieerd. Voorzichtigheid is geboden bij het citeren ervan richting klanten.

Bronnen: [TechCrunch – Block Dessa](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/) · [TechCrunch – NVIDIA Nemotron](https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/) · [Anthropic – Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) · [Hugging Face – Muse Spark Open](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) · [TechCrunch – OpenAI Decisions API](https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/)

---

## 🏛️ Governance & Ethiek

In Nederland spraken **premier Jetten en staatssecretaris Aerdts met Nebius** over rekenkracht voor de geplande AI Gigafabriek in de Rotterdamse haven. Nebius, een van de eerste grote klanten, is opgericht door voormalige Yandex-medewerkers en opereert vanuit de Zuidas. Geopolitieke gevoeligheid is aanwezig, maar de gesprekken zijn gevoerd.

Opmerkelijk politiek: **68 Kamerleden** gebruikten het afgelopen jaar AI-tools om hun spreekteksten mee te schrijven, aldus onderzoek van De Groene Amsterdammer en Investico. Dit roept vragen op over authenticiteit in democratische deliberatie — en is een signaal dat AI-geletterdheid ook op beleidsniveau urgent is.

Op EU-niveau bereidt de Europese Commissie een voorstel voor om **Microsoft en Amazon als gatekeepers** aan te wijzen voor hun clouddiensten onder de Digital Markets Act. Dit raakt direct aan de vendor lock-in discussie die veel enterprise CIO's voeren.

Bronnen: [Computable – Jetten & Nebius](https://www.computable.nl/2026/10/19/premier-jetten-in-gesprek-met-zuidas-russen-van-nebius-over-ai/) · [NOS – AI in Tweede Kamer](https://nos.nl/artikel/2636031-ook-veel-van-wat-er-in-de-tweede-kamer-wordt-gezegd-komt-van-ai) · [CIO Dive – EU Digital Markets Act](https://www.ciodive.com/news/senior-execs-worry-ai-system-lock-in/823927/)

---

## 🔐 Security & Risk

**Prompt injection** blijft de dominante aanvalsvector op AI-agents. Een OWASP-onderzoeker noemde het deze week expliciet "een onopgelost architectuurprobleem". Recente CVE's bevestigen dit:

- **Roo Code CVE-2026-110202** (CVSS 7.7): een allowlist-bypass waarbij een denied commando via `>&`-redirect toch auto-approved werd — bereikbaar via indirect prompt injection vanuit een externe repo of document.
- **DB-GPT** (20 oktober): een lek waarbij een mock-user-lookup iedere aanroeper adminrechten gaf op een agent-endpoint, CVSS 9.3.

**Microsoft** sloeg deze week publiekelijk alarm over AI-gedreven cyberaanvallen. De melding is serieus te nemen: aanvallers gebruiken AI-agents om aanvallen sneller, gerichter en volautomatisch uit te voeren. De responstijd voor verdedigers slinkt.

**SAS** lanceerde eerder deze maand een platform voor toezicht op AI-toepassingen in enterprise-omgevingen. Een aanwijzing dat de markt voor AI-governance-tooling volwassen begint te worden.

Bronnen: [Computable – Microsoft AI-cyberaanvallen](https://www.computable.nl/2026/10/23/microsoft-slaat-alarm-over-ai-cyberaanvallen/) · [Help Net Security – OWASP prompt injection](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) · [Computable – AI-agents en kwetsbaarheden](https://www.computable.nl/2026/10/07/kort-ai-agents-vergroten-risico-van-oude-softwarekwetsbaarheden-sas-lanceert-platform-voor-toezicht-op-ai-toepassingen-en-meer/)

---

## 📈 Markt & Adoptie

**Microsoft** staat bovenaan in Gartner's enterprise-AI ranking, gevolgd door **Google** als koploper in agentic AI. Azure groeide 27% in Q4 (omzet $59,3 miljard). Microsoft investeert $2,5 miljard in een nieuw bedrijf (Microsoft Frontier Company) dat engineers inbedt bij grote klanten — een teken dat professionele dienstverlening rond AI-implementatie een serieus verdienmodel is.

**SAP koopt Techwolf** (Belgisch bedrijf): hiermee kunnen SAP HR-agents slimmer vaardigheidsinformatie gebruiken. Voor Ctac-klanten met SAP SuccessFactors is dit een te volgen ontwikkeling.

De vier hyperscalers (Amazon, Microsoft, Meta, Google) plannen gezamenlijk **$725 miljard aan CapEx in 2026** — het grootste investeringsjaar in AI-infrastructuur ooit. Amazon verhoogde zijn investering in Anthropic bovendien met $25 miljard voor extra rekenkracht.

Opvallend: een Rimini Street-rapport signaleert dat senior executives gemiddeld maar **27% rendement** verwachten op hun AI-investeringen binnen 1–2 jaar. De hype en de gerapporteerde ROI lopen uiteen.

Bronnen: [CIO Dive – Microsoft/Google enterprise](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) · [CIO Dive – SAP AI at scale](https://www.ciodive.com/news/SAP-build-ai-scale-enterprise/826284/) · [CIO Dive – AI spending maturity](https://www.ciodive.com/news/AI-spending-soars-enterprise-maturity/827488/) · [VentureBeat – Microsoft AI playbook](https://venturebeat.com/technology/microsoft-releases-new-ai-playbook-for-enterprises-based-on-its-own-learnings-and-it-reveals-a-surprising-moat-your-biz-may-already-have)

---

## 💡 Ctac-relevantie

**SAP-klanten:** De overname van Techwolf door SAP is direct relevant. Klanten die SAP SuccessFactors inzetten, zullen deze functionaliteit gefaseerd krijgen aangeboden. Ctac kan nu al het gesprek aangaan over skill-based HR-strategie als aanvulling op SAP-implementaties.

**Security-propositie:** De combinatie van prompt injection-kwetsbaarheden in coding agents (Roo Code, DB-GPT) en Microsoft's waarschuwing over AI-cyberaanvallen biedt een concrete haak voor een security-dienst rond AI-agents. Klanten die agents uitrollen — ook kleinschalig — hebben behoefte aan een risicoanalyse en mitigatieraamwerk. Dit past in de opbouw van de AI-unit.

**Microsoft Frontier Company:** Het feit dat Microsoft $2,5 miljard investeert in het inbedden van engineers bij klanten is een marktsignaal: implementatieondersteuning bij AI-uitrol is een schaars en betaald goed. Ctac heeft hier een positie als betrouwbare Nederlandse partner met sectorkennis — sterker dan internationale consultancybureaus voor middelgrote klanten.

**Open-source vs. vendor lock-in:** De Europese discussie over lock-in (Digital Markets Act) en het verschijnen van Aleph Alpha's Kolibri 1 (Apache 2.0, Europees model) wijzen op een groeiende markt voor data-soevereine AI-oplossingen — met name bij overheidsinstellingen en zorginstellingen. Dit is een propositiekans.

---

## 📚 Bronnen & verder lezen

- [TechCrunch AI – oktober 2026](https://techcrunch.com/category/artificial-intelligence/)
- [Block Dessa voice model (Oct 24)](https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human/)
- [Meta Muse Spark Open 816B – Hugging Face](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
- [NVIDIA Nemotron 3.5 Super VL (Oct 19)](https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/)
- [Anthropic Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)
- [OpenAI Decisions API (Oct 22)](https://techcrunch.com/2026/10/22/openai-makes-its-jev-competitor-widely-available-as-decision-model-competition-heats-up/)
- [Computable – Microsoft AI-cyberaanvallen (Oct 23)](https://www.computable.nl/2026/10/23/microsoft-slaat-alarm-over-ai-cyberaanvallen/)
- [Computable – Jetten & Nebius AI Gigafabriek (Oct 19)](https://www.computable.nl/2026/10/19/premier-jetten-in-gesprek-met-zuidas-russen-van-nebius-over-ai/)
- [NOS – AI in de Tweede Kamer](https://nos.nl/artikel/2636031-ook-veel-van-wat-er-in-de-tweede-kamer-wordt-gezegd-komt-van-ai)
- [CIO Dive – Microsoft/Google enterprise AI leadership](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – SAP AI at scale](https://www.ciodive.com/news/SAP-build-ai-scale-enterprise/826284/)
- [Aleph Alpha Kolibri 1 – Hugging Face](https://huggingface.co/Aleph-Alpha/Kolibri-1)
- [OWASP prompt injection onopgelost – Help Net Security](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
