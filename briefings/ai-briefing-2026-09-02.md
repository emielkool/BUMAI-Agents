---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-02
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2 september 2026

## 🔑 Highlights van de dag

- **Meta Muse Glimmer** is vandaag uitgebracht: een 30B multimodaal model voor lokaal agentisch gebruik, Apache 2.0 gelicentieerd – direct bruikbaar in enterprise-pilots zonder vendor lock-in.
- **EU AI Act transparantieregels** gelden nu al een maand (van kracht per 2 augustus): chatbots moeten zichzelf als AI identificeren en deepfakes moeten verplicht gelabeld worden. Conformiteitschecklists worden urgenter.
- **Big Tech slaat alarm**: meer dan honderd toonaangevende techbedrijven waarschuwden gisteren dat AI-gedreven cyberaanvallen kritieke infrastructuur de komende maanden zwaarder zullen treffen.
- **Microsoft Copilot** telt inmiddels meer dan 20 miljoen betaalde seats; de jaarlijkse AI-omzet van Microsoft oversteeg $37 miljard (+123% YoY) – AI is geen experiment meer maar kernproduct.
- **Open-source LLMs** domineren: Chinese labs brengen maand na maand grotere modellen uit dan Amerikaanse peers (tot 2,78 biljoen parameters); het gat tussen open en closed-source wordt kleiner.

## 🧠 Technologie & Modellen

**Meta Muse Glimmer** is vandaag gepubliceerd op Hugging Face. Het is een 30B-parametersmodel gedistilleerd uit Meta's grotere Muse, met ondersteuning voor tekst, beeld en audio, 1M context via het grotere Inkling-zustermodel, en een Apache 2.0-licentie. Uitgesproken gericht op lokale, agentische use cases – een praktische keuze voor teams die AI-agents on-premise willen draaien zonder API-kosten. ([Hugging Face blog](https://huggingface.co/blog/muse-glimmer))

**Inkling by Thinking Machines** is eveneens recent beschikbaar: een groot multimodaal model (beeld, audio, tekst) met 1 miljoen tokens context en agentische capabilities. Interessant voor complexe, langlopende agentic workflows. ([Hugging Face](https://huggingface.co/blog/thinkingmachines-inkling))

**State of Open Models – Summer 2026**: het Hugging Face-rapport bevestigt dat Chinese labs (Qwen, Kimi, DeepSeek e.a.) consistent grotere en compétitieve modellen uitbrengen dan westerse labs. Kimi K2.6 (~1,1T parameters, Modified MIT) en Qwen3 235B-A22B (Apache 2.0) worden aangemerkt als de sterkste open-weight modellen voor enterprise-inzet. ([Hugging Face](https://huggingface.co/blog/state-of-open-models-summer-2026))

**OpenAI GPT-5.6** (Sol/Terra/Luna-familie, gelanceerd juli) heeft inmiddels prijsverlagingen ondergaan van 20–80% per variant. Sol wordt gepositioneerd als beste coding model, Luna als budgetoptie. ([TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/))

## 🏛️ Governance & Ethiek

De **EU AI Act** is per 2 augustus 2026 gedeeltelijk van kracht. Transparantieregels gelden nu: chatbots moeten aangeven dat ze AI zijn, deepfakes moeten expliciet gelabeld worden. De AI Omnibus-amendementen (digitaal vereenvoudigingspakket) zijn aangenomen in juni en van kracht per 27 juli – ze verlichten de nalevingslast voor een deel van de verplichtingen. Volgende mijlpalen: per 2 december 2026 gelden verboden op CSAM-gerelateerde AI-toepassingen; hoog-risico systemen (Annex III) volgen per december 2027. ([digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august))

In Nederland bevestigt NOS dat AI-gestuurde telefonisten en chatbots zich per direct moeten bekendmaken als AI – niet pas aan het einde van een gesprek. ([NOS](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven))

## 🔐 Security & Risk

**Big Tech noodklok kritieke infrastructuur**: meer dan honderd techbedrijven en grote afnemers roepen op tot betere digitale beveiliging. AI-gedreven cyberaanvallen worden wijdverbreider verwacht de komende maanden. ([Computable](https://www.computable.nl/2026/09/01/big-tech-luidt-noodklok-ai-bedreigt-kritieke-infrastructuur/))

**AI power users als risicovector**: de top 5% van enterprise AI-gebruikers interacteert 12× vaker met AI dan de onderste 50% en introduceert disproportioneel shadow AI, datalekrisico's en autonome agents buiten governance-kaders. 16,31% van AI-extensies bevat bekende CVE-kwetsbaarheden. ([The Hacker News](https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users-are-your-biggest-security-risk.html))

**Vulnerability management under pressure**: de gemiddelde hersteltijd voor kritieke kwetsbaarheden staat op 74 dagen; 45% van kwetsbaarheden bij grote bedrijven wordt nooit opgelost. AI versnelt aanvallen maar ook detectie – organisaties zonder AI-ondersteunde verdediging raken achterop. ([The Hacker News](https://thehackernews.com/2026/08/frontier-ai-vulnerability-managements.html))

## 📈 Markt & Adoptie

**Microsoft** domineert enterprise AI: 20+ miljoen Copilot-seats, jaarlijkse AI-omzet van $37 miljard (+123% YoY). Klanten met meer dan 50.000 seats verviervoudigden op jaarbasis. ([CIO Dive](https://www.ciodive.com/news/microsoft-touts-copilot-growth-boosts-spending-as-revenues-soar/819009/))

**Google** lanceerde de Agentic Data Cloud en positioneert zich als 'company to beat' in enterprise agentic AI. AWS en Google werken samen aan multicloud-verbindingen om enterprise AI-workloads te faciliteren. ([CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))

**Trapstuk van de markt**: tweederde van de bedrijven zit nog vast in de pilot-fase en verwacht slechts 27% ROI binnen 1–2 jaar. De kloof tussen koplopers en achterblijvers groeit – en dat is een strategische kans voor adviseurs die organisaties helpen opschalen. ([CIO Dive](https://www.ciodive.com/news/enterprise-software-spend-accelerates-amid-ai-adoption-blitz/760662/))

**Nederland**: na Duitsland is Nederland de grootste Europese exporteur van AI-gerelateerde goederen (>€80 miljard, #11 wereldwijd). Sterke positie, maar de AI-startup-index signaleert dat Nederland achterblijft in het creëren van nieuwe technologiebedrijven. ([Computable](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/))

## 💡 Ctac-relevantie

**EU AI Act compliance is nu concreet werk.** De transparantieregels gelden per 2 augustus – klanten die chatbots of andere interactieve AI inzetten moeten nu aantoonbaar voldoen. Ctac kan hier direct waarde leveren met compliance-scans en implementatiebegeleiding, met de deadline van 2 december 2026 (CSAM-verboden) als aanvullende stok achter de deur.

**Meta Muse Glimmer biedt een laagdrempelige ingang voor on-premise AI-pilots.** Apache 2.0, 30B parameters, multimodaal en agentisch – dit model is geschikt om klanten die vanwege datasoevereiniteit weerstand hebben tegen cloud-AI toch in beweging te krijgen. Interessant voor overheids- en zorgsectoren die Ctac bedient.

**De "pilot-trap" is een propositie-kans.** Tweederde van bedrijven zit vast in pilots. Ctac kan zich onderscheiden door niet nóg een proof-of-concept te verkopen, maar een traject van pilot naar productie – met focus op governance, schaalbaarheid en meetbare ROI. Dat sluit aan op de IP- en platform-transitie die intern gaande is.

**Security-awareness rondom AI-extensies verdient aandacht.** Meer dan 16% van populaire AI-extensies bevat CVE-kwetsbaarheden. Bij klanten met grote Copilot- of ChatGPT-uitrollingen is een extensie-audit een concrete en direct waardevolle dienst.

## 📚 Bronnen & verder lezen

- [Meta Muse Glimmer – Hugging Face](https://huggingface.co/blog/muse-glimmer)
- [Inkling by Thinking Machines – Hugging Face](https://huggingface.co/blog/thinkingmachines-inkling)
- [State of Open Models Summer 2026 – Hugging Face](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [OpenAI GPT-5.6 lancering – TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [EU AI Act transparantieregels van kracht – Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [AI-telefonist moet zich direct prijsgeven – NOS](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)
- [Big Tech noodklok kritieke infrastructuur – Computable](https://www.computable.nl/2026/09/01/big-tech-luidt-noodklok-ai-bedreigt-kritieke-infrastructuur/)
- [Top 5% AI-gebruikers als risicovector – The Hacker News](https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users-are-your-biggest-security-risk.html)
- [Frontier AI vulnerability management – The Hacker News](https://thehackernews.com/2026/08/frontier-ai-vulnerability-managements.html)
- [Microsoft Copilot Q3 2026 earnings – CIO Dive](https://www.ciodive.com/news/microsoft-touts-copilot-growth-boosts-spending-as-revenues-soar/819009/)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Nederland #2 Europa AI-export – Computable](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/)
