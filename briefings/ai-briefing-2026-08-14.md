---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-14
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 14 augustus 2026

## 🔑 Highlights van de dag

- **OpenAI lanceert "Ultrafast" modus voor GPT-5.6 Sol:** via een partnerschap met chipmaker Cerebras haalt het nieuwe servicetier tot 14× hogere snelheid (750 tokens/sec). Nog in preview, maar de directionele keuze richting inference-optimalisatie is duidelijk.
- **EU AI Act handhaving live:** per 2 augustus 2026 gelden de transparantievereisten in de hele EU — AI-systemen (chatbots, telefonisten, gegenereerde content) moeten zich direct kenbaar maken. Niet naleving kan nu gesanctioneerd worden.
- **DeepSeek stoot Google van AI-troon bij bedrijven:** Nederlandse enterprise-adoptiemetingen tonen DeepSeek als favoriet bij bedrijven, mede door een permanente prijsverlaging van 75% op V4-Pro. Goedkoper dan Claude Sonnet of GPT-5.5 met factor 7–17×.
- **Prompt injection treft Claude Code, Gemini CLI en Copilot tegelijk:** een gedocumenteerde aanval toonde aan dat dezelfde vector drie toonaangevende coding agents simultaan kon exploiteren. 94,4% van LLM-agents is kwetsbaar, aldus recent onderzoek.
- **Meta Muse Glimmer (30B) uit: lokale AI-agent met Apache 2.0-licentie:** gedistilleerd uit het grotere Muse-model, ontworpen voor privacy-bewuste toepassingen (coding, documentanalyse). Voegt serieuze open-source optie toe aan de agentic stack.

---

## 🧠 Technologie & Modellen

**OpenAI – Ultrafast mode (13 aug)**
OpenAI kondigde gisteren "Ultrafast" aan voor GPT-5.6 Sol, aangedreven door Cerebras-hardware. Het systeem genereert tot 750 output tokens per seconde — tot 14× sneller dan de standaard API. De preview is initieel beperkt tot een kleine groep API-klanten. GPT-5.6 Sol is ook 54% efficiënter bij codingtaken vergeleken met de voorganger. De modellfamilie bestaat nu uit Sol (flagship), Terra (balans/kosten) en Luna (snel en goedkoop). ([OpenAI](https://openai.com/index/previewing-ultrafast/), [TechCrunch](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/))

**Meta Muse Glimmer – open-source lokale agent (10 aug)**
Meta lanceerde Muse Glimmer, een 30B-parametersmodel gedestilleerd van hun grotere Muse-model. Apache 2.0-licentie, ontworpen voor lokale inzet bij privacy-gevoelige workloads: coding, documentanalyse, persoonlijke assistenten. Relevante toevoeging voor Ctac-scenario's waarbij data het pand niet mag verlaten. ([Hugging Face Blog](https://huggingface.co/blog/muse-glimmer))

**DeepSeek Harness + V4-Pro permanente prijsverlaging**
DeepSeek lanceerde een open-source agent harness als directe concurrent voor Claude Code en GitHub Copilot, gecombineerd met een permanente 75% prijsverlaging op V4-Pro. Inputs zijn 7× goedkoper dan Claude Sonnet. Dit verhoogt de druk op westerse aanbieders om hun pricing te herzien. ([VentureBeat](https://venturebeat.com/infrastructure/how-deepseeks-radical-architecture-is-shattering-silicon-valleys-token-moat))

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving en transparantie per 2 augustus actief**
Vanaf 2 augustus 2026 handhaaft de Europese Commissie (via het AI Office) en de nationale autoriteiten de AI Act-regels. Concreet geldt nu: elke interactie met een AI-chatbot, AI-telefonist of AI-gegenereerde content moet transparant worden gemaakt. Bedrijven die dit niet doen, riskeren boetes. Elke lidstaat moest vóór 2 augustus ook minimaal één nationale AI-sandbox operationeel hebben. ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august), [NOS](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven))

De regels voor hoog-risico AI-systemen volgen pas op 2 december 2027 (embedded in fysieke producten: augustus 2028). Dit geeft bedrijven nog enige aanlooptijd, maar de transparantieplicht is nu al geldend recht. ([Computable](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/))

---

## 🔐 Security & Risk

**Simultane prompt injection aanval op Claude Code, Gemini CLI en Copilot**
Beveiligingsonderzoekers documenteerden een aanval waarbij drie grote coding agents tegelijk werden gecompromitteerd via één prompt injection vector, waarbij API-credentials werden buitgemaakt. Dit past in een bredere trend: in 2025 werden AI-tools bij meer dan 90 organisaties misbruikt voor credential-diefstal. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**Kwetsbaarheidscijfers alarmerend:**
Onderzoek toont aan dat 94,4% van state-of-the-art LLM-agents kwetsbaar is voor prompt injection, en 100% voor inter-agent trust exploits. De kern van het probleem: modellen kunnen instructies en data structureel niet onderscheiden. Voor agentic AI-implementaties is dit een architectureel risico dat niet met patches weggewerkt kan worden. ([Airia](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/), [VentureBeat](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers))

---

## 📈 Markt & Adoptie

**Microsoft Copilot: >20 miljoen betaalde seats, AI-omzet $37B+ (+123% YoY)**
Microsoft toont indrukwekkende groei bij Copilot: het aantal klanten met >50.000 seats verviervoudigde jaar-op-jaar. De AI run rate overschreed $37 miljard. Tegelijk investeren AWS, Google Cloud en Azure gezamenlijk meer dan $500 miljard in AI-infrastructuur dit jaar. ([CIO Dive](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/))

**AI IaaS groeit 96%; inference overtreft training**
Per augustus 2026 overstijgt inferentiebudget voor het eerst het trainingsbudget bij enterprise AI-afnemers. AI-geoptimaliseerde IaaS groeit naar verwachting naar $42 miljard eind 2026. ([Computable](https://www.computable.nl/2026/08/10/kort-openai-pauzeert-astra-ai-iaas-groeit-96-nieuwe-cra-quick-scan-en-gesimuleerde-vishing/))

**DeepSeek stoot Google van AI-troon bij bedrijven**
Mede gedreven door drastisch lagere tokenkosten wint DeepSeek terrein op Google bij enterprise-klanten. Nebius (AI-cloudbedrijf, hoofdkantoor Amsterdamse Zuidas) zag zijn inkomsten met 454% stijgen naar €582M, wat de groeiende vraag naar AI-cloud in de Benelux bevestigt. ([Computable](https://www.computable.nl/2026/08/13/deepseek-stoot-google-van-ai-troon-bij-bedrijven/))

---

## 💡 Ctac-relevantie

**1. EU AI Act: nu actie vereist voor klanten**
De transparantieverplichting is per 2 augustus van kracht. Ctac kan direct waarde leveren door klanten te helpen hun AI-toepassingen te inventariseren en de juiste disclosuremechanismen in te richten. Dit is een concrete propositie richting sectoren met veel klantcontact (finance, overheid, zorg).

**2. Goedkope alternatieven zetten vendor-keuze op scherp**
DeepSeek V4-Pro is bij bepaalde workloads 7–17× goedkoper dan westerse alternatieven. Voor klanten met hoge tokenvolumes (documenten verwerken, klantenservice AI) is een eerlijk kostenmodel nodig. Ctac kan hier als onafhankelijk adviseur onderscheidend zijn — mits we zelf de juiste vergelijkingskaders hebben.

**3. Agentic AI-security: verplicht onderwerp bij elke implementatie**
De simultaneïteit van de prompt injection aanvallen op coding agents maakt duidelijk: agentic AI zonder expliciete security-architectuur is een aansprakelijkheidsrisico voor klanten én voor Ctac. Zorg dat elke AI-agent-propositie een security-review bevat (tool-permissions, sandbox-isolatie, input-validatie).

**4. Meta Muse Glimmer = on-premises optie voor gevoelige sectoren**
Voor overheids- en zorginstellingen die data niet naar de cloud willen sturen, biedt een 30B open-source model nu serieuze functionaliteit lokaal. Dit opent een nieuw marktsegment voor Ctac: begeleiding bij lokale AI-deployments.

---

## 📚 Bronnen & verder lezen

- [OpenAI – Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed](https://openai.com/index/previewing-ultrafast/)
- [TechCrunch – OpenAI introduces Ultrafast (13 aug 2026)](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/)
- [OpenAI – GPT-5.6 family overview](https://openai.com/index/gpt-5-6/)
- [Hugging Face – Meta Muse Glimmer (10 aug 2026)](https://huggingface.co/blog/muse-glimmer)
- [VentureBeat – DeepSeek Harness & V4-Pro pricing](https://venturebeat.com/infrastructure/how-deepseeks-radical-architecture-is-shattering-silicon-valleys-token-moat)
- [EC – Commission starts enforcing AI Act (2 aug 2026)](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [NOS – AI-telefonist moet zich voortaan direct prijsgeven](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)
- [Computable – Wat je moet weten van de AI Act (3 aug 2026)](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [VentureBeat – Prompt injection treft Claude Code, Gemini CLI en Copilot](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Airia – AI Security in 2026: Prompt Injection, the Lethal Trifecta](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Microsoft earnings & Copilot growth](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [Computable – DeepSeek stoot Google van AI-troon (13 aug 2026)](https://www.computable.nl/2026/08/13/deepseek-stoot-google-van-ai-troon-bij-bedrijven/)
- [Computable – AI IaaS groeit 96% (10 aug 2026)](https://www.computable.nl/2026/08/10/kort-openai-pauzeert-astra-ai-iaas-groeit-96-nieuwe-cra-quick-scan-en-gesimuleerde-vishing/)
