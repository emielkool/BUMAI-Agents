---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-01
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 1 juli 2026

## 🔑 Highlights van de dag

- **Claude Sonnet 5** (Anthropic, 30 juni): bijna-Opus-prestaties voor een derde van de prijs, volledig gericht op agentic workflows. Dit verlaagt de instapkosten voor bedrijven die AI-agenten willen inzetten aanzienlijk.
- **OpenAI GPT-5.6 Sol/Terra/Luna** in beperkte preview voor geselecteerde overheidspartners – het meest agentische model van OpenAI tot nu toe, breed publiek moet nog wachten.
- **Microsoft verhoogt M365-prijzen per vandaag** met gemiddeld 16% vanwege ingebedde Copilot-functionaliteiten – een directe kostenverhoging voor enterprise-klanten en een gespreksopener over ROI.
- **EU AI Act deadline: 2 augustus 2026** – over minder dan 5 weken krijgt de Europese AI Office volledige handhavingsbevoegdheden over GPAI-modelleveranciers. Transparantieregels voor AI-content gaan dan ook in.
- **Agentic AI security escaleert**: een kritieke CVE in Cursor IDE maakt remote code execution via prompt injection mogelijk; vijf westerse inlichtingendiensten publiceerden gezamenlijke veiligheidsguidance voor agentic systemen.

## 🧠 Technologie & Modellen

**Claude Sonnet 5 – Anthropic (30 juni 2026)**
Anthropic lanceerde Claude Sonnet 5, een middelgroot model met agentic capaciteiten die eerder voorbehouden waren aan grote, dure modellen. Het model kan plannen maken, tools (browser, terminal) gebruiken en autonoom taken uitvoeren op een niveau dat maanden geleden alleen Opus aankon. Introductieprijs: $2/$10 per miljoen tokens (input/output) t/m 31 augustus; daarna $3/$15. Ter vergelijking: Opus 4.8 kost $5/$25. Prestaties naderen Opus 4.8 – dit is een echte kosten-kwaliteitssprong voor enterprise agentic toepassingen.
([TechCrunch](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/) | [Anthropic](https://www.anthropic.com/news/claude-sonnet-5))

**OpenAI GPT-5.6 Sol, Terra en Luna**
OpenAI kondigde drie nieuwe GPT-5.6 varianten aan in beperkte preview voor overheidspartners. Sol is het topmodel voor complexe reasoning, langdurige agentic workflows en beveiligingskritische toepassingen. De gefaseerde uitrol volgt een executive order van president Trump (2 juni) die benchmarking en veiligheidsbeoordeling vereist vóór brede beschikbaarheid. Wanneer de bredere lancering volgt is nog onduidelijk.
([VentureBeat](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov))

## 🏛️ Governance & Ethiek

**EU AI Act: kritieke deadline op 2 augustus 2026**
Op 2 augustus 2026 wordt de AI Act volledig van kracht. Dan krijgt de Europese AI Office handhavingsbevoegdheden over GPAI-modellen (GPT, Claude, Gemini e.d.): recht op documentatie-opvraag, evaluaties, corrigerende maatregelen én boetes. Lidstaten moeten voor die datum minimaal één AI regulatory sandbox hebben ingericht. Transparantieregels voor AI-gegenereerde content treden ook dan in werking – aanbieders zijn verplicht AI-output merkbaar te maken. In juli worden de eerste ondertekenaars van de Code of Practice for AI Content Transparency gepubliceerd, wat publicitaire druk legt op niet-ondertekenaars.
([EU AI Act tracker](https://artificialintelligenceact.eu/implementation-timeline/) | [Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

## 🔐 Security & Risk

**CVE-2026-22708: prompt injection in Cursor IDE**
Een kritieke kwetsbaarheid in de populaire AI-coding omgeving Cursor maakt remote code execution mogelijk via indirect prompt injection in shell built-ins. Aanvallers kunnen via kwaadaardige code-input de AI-agent opdrachten laten uitvoeren buiten de intentie van de ontwikkelaar. Dit illustreert dat agentic AI-tools in de ontwikkelketen een nieuw en serieus aanvalsoppervlak vormen.
([arXiv](https://arxiv.org/pdf/2603.21642))

**Five Eyes + VS: gezamenlijke guidance agentic AI**
De cybersecuritydiensten van de VS (CISA), Australië, Canada, Nieuw-Zeeland en het VK publiceerden gezamenlijke veiligheidsguidance voor agentic AI-systemen. Vijf risicocategorieën: context poisoning, privilege escalation, excessive autonomy, supply chain risico's en onvoldoende logging/auditability. Aanbevolen maatregelen: least-privilege tooling, menselijke goedkeuring voor hoog-risico acties en adversarial testing.

## 📈 Markt & Adoptie

**Microsoft M365 prijsverhoging: +16% per vandaag**
Per 1 juli verhoogt Microsoft de commerciële M365-abonnementsprijzen met gemiddeld 16% vanwege de inbedding van Copilot in alle suites. Business Premium en Office 365 E1 zijn uitgezonderd. Microsoft heeft inmiddels >20 miljoen Copilot paid seats; het aantal klanten met >50.000 seats verviervoudigde jaar-op-jaar. De AI-omzet run-rate bedraagt >$37 miljard (+123% YoY).
([CIO Dive](https://www.ciodive.com/news/microsoft-365-ai-tools-higher-price/807189/) | [CIO Dive earnings](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/))

**Microsoft-OpenAI exclusiviteit opgeheven**
Microsoft en OpenAI hebben hun exclusieve cloud-distribitieovereenkomst herzien: OpenAI mag zijn modellen nu ook aanbieden via AWS en Google Cloud. Dit vergemakkelijkt multicloud-implementaties, maar verzwakt Microsofts unieke Azure-voordeel. Tegelijkertijd kondigde Microsoft Copilot Cowork aan – een agent die met Anthropic-technologie samenwerkt over M365-apps heen.
([VentureBeat](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud) | [VentureBeat Cowork](https://venturebeat.com/orchestration/microsoft-announces-copilot-cowork-with-help-from-anthropic-a-cloud-powered))

**Enterprise adoptie stagneert op de pilotgrens**
79% van enterprises ervaart uitdagingen bij AI-adoptie. Organisaties met sterk change management zijn 6× vaker succesvol in productie. De transitie van PoC naar schaalbare productie blijft de voornaamste bottleneck – niet de technologie, maar governance, integratie en change.
([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/))

## 💡 Ctac-relevantie

**Claude Sonnet 5 opent nieuwe propositie-mogelijkheden** – agentic AI is nu betaalbaar op Sonnet-niveau. Voor Ctac is dit het moment om klantproposities te verkennen voor multi-step workflows (documentanalyse, procesautomatisering, code-review pipelines) die eerder te kostbaar waren. De introductieprijs t/m augustus is een ideale periode voor een PoC.

**Microsoft prijsverhoging = gesprekskans bij klanten** – klanten met M365-licenties zien vandaag kosten stijgen. Ctac kan als trusted advisor positioneren: helpt de klant Copilot daadwerkelijk benutten zodat de meerprijs rendeert. Wie nog geen adoptieplan heeft, heeft dat gesprek nodig.

**EU AI Act augustusdeadline: concrete opportunity voor AI-unit** – klanten in gereguleerde sectoren (overheid, zorg, finance) moeten nu actie ondernemen rond GPAI-governance, sandboxverplichtingen en content-transparantie. Ctac kan helpen met compliance-assessments en implementatiebegeleiding. Dit is een korte-termijn window.

**Agentic AI security als nieuw aanbod** – bij klanten die Cursor, GitHub Copilot of vergelijkbare AI-coding tools gebruiken, is een security review van de AI-toolchain relevant en urgent. CVE-2026-22708 maakt duidelijk dat dit geen theoretisch risico is.

## 📚 Bronnen & verder lezen

- [Anthropic: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)
- [TechCrunch: Anthropic launches Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [VentureBeat: OpenAI unveils GPT-5.6 Sol, Terra and Luna](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)
- [EU AI Act: Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [Europese Commissie: AI Act governance & enforcement](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [CIO Dive: Microsoft 365 price increase](https://www.ciodive.com/news/microsoft-365-ai-tools-higher-price/807189/)
- [CIO Dive: Microsoft Copilot growth Q3 2026](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [VentureBeat: Microsoft-OpenAI exclusivity reworked](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)
- [VentureBeat: Microsoft Copilot Cowork](https://venturebeat.com/orchestration/microsoft-announces-copilot-cowork-with-help-from-anthropic-a-cloud-powered)
- [CIO Dive: Enterprise AI adoption challenges](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [arXiv: Prompt injection in AI coding editors](https://arxiv.org/pdf/2603.21642)
