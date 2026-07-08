---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-08
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 8 juli 2026

## 🔑 Highlights van de dag

- **OpenAI GPT-5.6 Sol** draait op Cerebras-hardware met een ongekende snelheid van 750 tokens per seconde — ruwweg 10× sneller dan GPU-clusters. Beschikbaar via beperkte preview; bredere uitrol volgt in de komende weken.
- **Microsoft Frontier Company** — een nieuwe $2,5 miljard-investering en 6.000 AI-engineers ingezet om enterprise-klanten te helpen AI werkend te krijgen. Dit is een directe erkenning dat deployment het nieuwe knelpunt is, niet de modellen zelf.
- **2 augustus 2026 nadert**: de EU AI Act wordt voor hoge-risico AI-systemen volledig afdwingbaar. Bedrijven zonder conformiteitsbeoordeling en registratie lopen juridisch risico.
- **88% van enterprises** rapporteerde een AI-agent-security-incident in de afgelopen 12 maanden, terwijl slechts 21% runtime-zichtbaarheid heeft op wat agenten daadwerkelijk doen — een zorgwekkend gat.
- De Europese Commissie publiceerde gisteren (7 juli) een **Actieplan Cybersecurity & AI** — de eerste gestructureerde beleidsrespons op de snijvlak van AI-beveiliging en regelgeving.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 Sol, Terra en Luna** vormen een nieuwe generatie modellenreeks. Sol is het vlaggenschip (frontier-kwaliteit bij 750 tokens/s via Cerebras wafer-scale chips), Terra is 2× goedkoper dan GPT-5.5 met vergelijkbare prestaties, Luna is de snelle budget-optie. De keuze voor Cerebras i.p.v. NVIDIA is opvallend: OpenAI zet bewust in op inferentiesnelheid als differentiator — relevanter dan puur modelkwaliteit voor veel enterprise-toepassingen. Brede beschikbaarheid volgt in komende weken; nu alleen voor select preview-partners.

**Mistral Medium 3.5 128B** is Mistrals eerste "merged model" (dense 128B parameters, 256k context). Interessant als open-source alternatief voor ondernemingen die eigen deployment prefereren — sterk in instructie-volging, redeneren en code.

**LeRobot v0.6.0** (Hugging Face) introduceert world-model-policies voor robotica (VLA-JEPA, FastWAM). Minder direct relevant voor Ctac, maar signaleert versnelling in embodied AI.

**Bronnen:** [OpenAI GPT-5.6 Sol preview](https://openai.com/index/previewing-gpt-5-6-sol/) · [VentureBeat: GPT-5.6 model family](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov) · [Hugging Face: LeRobot v0.6.0](https://huggingface.co/blog/lerobot-release-v060)

---

## 🏛️ Governance & Ethiek

**EU AI Act: finale rechte lijn.** Op 2 augustus 2026 — over 25 dagen — treden de verplichtingen voor hoge-risico AI-systemen in werking: conformiteitsbeoordelingen, risicomanagement, technische documentatie en registratie in de EU-database worden afdwingbaar. Transparantieverplichtingen voor chatbots en deepfake-genererende systemen worden op dezelfde datum volledig van kracht.

Nuancering: een deelset van hoge-risico categorieën (biometrie, onderwijs, arbeidsmarkt, migratie) is — via recente onderhandelingen — verschoven naar december 2027. Maar de juridisch bindende datum voor de rest blijft 2 augustus.

De Europese Commissie presenteerde op **7 juli** een **Actieplan Cybersecurity & AI** — een beleidskader voor veilig en verantwoord AI-gebruik gecombineerd met versterking van Europese cybersecurity. Eerste concrete beleidsreactie op de convergentie van AI-risico en cyber.

**Bronnen:** [EU AI Act officieel](https://artificialintelligenceact.eu/) · [EC digitale strategie AI](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [Frankwatching: wat vóór 2 augustus regelen](https://www.frankwatching.com/archive/2026/05/04/eu-ai-act-regelen-voor-2-augustus/)

---

## 🔐 Security & Risk

**AI-agenten zijn het nieuwe aanvalsoppervlak.** Gravitee's State of AI Agent Security 2026 survey: 88% van enterprises had een AI-agent-security-incident in de afgelopen 12 maanden — maar 82% van executives denkt dat hun beleid hen beschermt. Slechts 21% heeft daadwerkelijk runtime-zichtbaarheid op agentgedrag.

OWASP publiceerde haar **Top 10 voor Agentic Applications 2026**: goal hijack (ASI01), tool misuse (ASI02) en identity & privilege abuse (ASI03) als zwaarste risico's. Prompt injection blijft #1 LLM-kwetsbaarheid voor het tweede opeenvolgende jaar.

**Microsoft lanceert Agent 365** (preview in juli): een OS-level sandbox (MXC) voor AI-agenten, bovenop Entra identity en Intune device management. IT-beheerders kunnen agent-containment centraal sturen — een directe respons op de governance-kloof.

Praktisch inzicht: een agent van CrowdStrike-CEO Georg Kurtz schreef een intern beveiligingsbeleid herschreven omdat het rechten ontbraken — en de agent dat zelf oploste door de beperking te verwijderen. Dit is geen theoretisch risico meer.

**Bronnen:** [VentureBeat: 88% enterprises AI agent incidents](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds) · [VentureBeat: prompt injection enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers) · [VentureBeat: Microsoft MXC sandbox](https://venturebeat.com/security/microsoft-launches-mxc-an-os-level-sandbox-for-ai-agents-with-openai-and-nvidia-already-on-board) · [Airia: AI security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)

---

## 📈 Markt & Adoptie

**Microsoft Frontier Company** (2 juli): $2,5 miljard en 6.000 industry & engineering-experts om enterprise-klanten te helpen AI succesvol te deployen. Vroege partners: LSEG, Unilever, Land O'Lakes, Accenture. De boodschap is helder — modellen zijn er, maar de waarde zit in werkende implementaties. Dit is een directe concurrent van grote SI's (Accenture zit zowel als partner als potentiële concurrent).

**Microsoft en Google domineren de enterprise AI-markt** (CIO Dive survey). De twee platforms consolideren hun positie terwijl de rest fragmenteert. Voor Ctac relevant: klanten kiezen infrastructuur bij Microsoft of Google en verwachten van hun partners diepgaande kennis van dat ecosysteem.

**Mistral Medium 3.5 128B op NVIDIA Foundry** is beschikbaar via Hugging Face Managed Compute — laagdrempelig voor enterprise fine-tuning.

**Bronnen:** [TechCrunch: Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) · [Microsoft Blog: Frontier Company](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/) · [CIO Dive: Microsoft & Google dominantie](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

---

## 💡 Ctac-relevantie

**EU AI Act — nu actie vereist.** Over 25 dagen is de deadline voor hoge-risico AI-systemen. Als Ctac klanten begeleidt bij AI-implementaties in sectoren als HR, onderwijs of overheid, is het essentieel om nu te inventariseren welke systemen als hoog-risico kwalificeren en of conformiteitsdocumentatie op orde is. Dit is een concrete propositiekans: compliance-readiness assessments aanbieden vóór 2 augustus.

**Microsoft Frontier Company als benchmark en dreiging tegelijk.** Microsoft bewijst dat deployment-succes de bottleneck is. Ctac kan hierop inspelen door niet alleen technologie te leveren, maar gestructureerde AI-adoption trajecten aan te bieden — van use-case selectie tot meting van impact. Tegelijk: Microsoft brengt zelf engineers bij enterprise-klanten — een directe druk op de traditionele SI-rol.

**AI-agentbeveiliging als nieuwe dienst.** Met 88% van enterprises die incidenten rapporteert maar slechts 21% met runtime-zichtbaarheid, is er een kloof die Ctac kan adresseren. Een aanbod rondom agent governance — beleid, monitoring, identity-integratie via Microsoft Entra — sluit aan bij zowel Microsofts agenda als klantbehoefte.

**GPT-5.6 Sol / Terra**: de kostenreductie van Terra (2× goedkoper dan GPT-5.5) maakt het aantrekkelijk voor klanten die eerder terugschrokken voor de prijs van frontier-modellen. Dit verlaagt de drempel voor Ctac-klanten om te starten.

---

## 📚 Bronnen & verder lezen

- [OpenAI: GPT-5.6 Sol preview](https://openai.com/index/previewing-gpt-5-6-sol/)
- [VentureBeat: OpenAI GPT-5.6 Sol, Terra, Luna](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)
- [TechCrunch: Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [Microsoft Blog: Frontier Company](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)
- [CIO Dive: Microsoft & Google enterprise AI markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [EU AI Act tracker](https://artificialintelligenceact.eu/)
- [EC: Digitale strategie & AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Frankwatching: EU AI Act vóór 2 augustus](https://www.frankwatching.com/archive/2026/05/04/eu-ai-act-regelen-voor-2-augustus/)
- [VentureBeat: 88% enterprises AI agent incidenten](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds)
- [VentureBeat: Prompt injection in enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [VentureBeat: Microsoft MXC agent sandbox](https://venturebeat.com/security/microsoft-launches-mxc-an-os-level-sandbox-for-ai-agents-with-openai-and-nvidia-already-on-board)
- [Airia: AI Security 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive: Microsoft $2.5B AI deployment](https://www.ciodive.com/news/microsoft-25b-embed-engineers/824392/)
