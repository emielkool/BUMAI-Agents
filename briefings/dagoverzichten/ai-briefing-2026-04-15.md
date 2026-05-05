---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-15
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2026-04-15

## 🔑 Highlights van de dag

- **Anthropic lanceert Claude Mythos + Project Glasswing:** Een nieuw frontier-model detecteerde zelfstandig duizenden zero-day kwetsbaarheden in alle grote besturingssystemen en browsers. Toegang is uitsluitend voor 12 geselecteerde securitypartners – Anthropic plant geen publieke release vanwege het misbruikrisico.
- **Microsoft presenteert drie eigen foundational models:** MAI-Transcribe-1, MAI-Voice-1 en MAI-Image-2 zijn via Microsoft Foundry beschikbaar en markeren de eerste serieuze eigen modelontwikkeling door Microsoft, los van OpenAI.
- **GLM-5 uit China zet open-source benchmark neer:** Het Chinese model van Zhipu AI staat #1 onder open gewichtsmodellen op LMArena en LLM-benchmarks, volledig getraind op Huawei-chips zonder NVIDIA – een strategisch signaal.
- **EU AI Act nadert voltooiing:** Per 2 augustus 2026 geldt de verordening volledig. De Commissie publiceerde op 8 april nieuwe richtlijnen voor de definitie van een AI-systeem – een praktisch ankerpunt voor compliance-trajecten.
- **Agentic AI domineert enterprise 2026:** Spending op AI-software groeit bijna 60% YoY naar $452 miljard; meer dan 90% van beslissers verwacht agenten sneller te adopteren dan generatieve AI.

---

## 🧠 Technologie & Modellen

**Microsoft MAI-modellen** (2 april): Microsoft Foundry biedt nu MAI-Transcribe-1 (speech-to-text, laagste Word Error Rate op FLEURS-benchmark in top-25 talen), MAI-Voice-1 (TTS, $22/1M tekens) en MAI-Image-2. De modellen komen uit het MAI Superintelligence-team van Mustafa Suleyman. Microsoft claimt daarmee "top 3 lab" te zijn, direct onder OpenAI en Google. Dit is een directe concurrentiestelling richting eigen partner OpenAI. Bron: [TechCrunch](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)

**Meta Muse Spark** (8 april): Meta's nieuwe model werkt via meerdere AI-agenten parallel aan hetzelfde probleem. Het gaat expliciet om een "ground-up overhaul" van Meta's AI-aanpak, inclusief een aankomende "Contemplating"-modus voor complexere redenering. Interessant maar beperkte benchmarkdata beschikbaar – observatie vereist. Bron: [TechCrunch](https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/)

**GLM-5 open source** (april): Zhipu AI's GLM-5 scoort 77.8% op SWE-bench Verified en 92.7% op AIME 2026, beschikbaar onder MIT-licentie op Hugging Face. Getraind op Huawei Ascend-chips via MindSpore. De implicatie: geavanceerde open gewichtsmodellen zijn niet langer exclusief afhankelijk van de VS of NVIDIA-hardware. Bron: [Hugging Face blog](https://huggingface.co/blog/mlabonne/glm-5)

---

## 🏛️ Governance & Ethiek

**EU AI Act – volledige toepassing augustus 2026:** Op 8 april publiceerde de Europese Commissie nieuwe richtlijnen voor de definitie van een AI-systeem, ter ondersteuning van organisaties die voorbereidingen treffen. Komende maanden volgen nog richtlijnen over hoog-risico classificatie, transparantievereisten (Art. 50) en meldplicht voor ernstige incidenten. Elke lidstaat moet vóór 2 augustus een nationale regulatory sandbox hebben ingericht. Bron: [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines) / [artificialintelligenceact.eu](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/)

**Nederland – Defensie en AI:** Het Nederlandse ministerie van Defensie evalueert het Maven Smart System voor gebruik bij doelselectie. Ethische en juridische vragen over menselijke controle bij AI-ondersteunde militaire beslissingen staan daarmee in het publieke debat. Bron: [NOS](https://nos.nl/nieuwsuur/artikel/2609142-zorgen-over-gebruik-van-ai-in-oorlogen-menselijke-afweging-blijft-nodig)

---

## 🔐 Security & Risk

**Anthropic Claude Mythos / Project Glasswing** (7 april): Het nieuwe Mythos-model identificeerde zelfstandig duizenden zero-day kwetsbaarheden – waaronder CVE-2026-4747, een 17 jaar oud remote code execution lek in FreeBSD. Deelnemers aan Project Glasswing: Amazon, Apple, Broadcom, Cisco, CrowdStrike, Linux Foundation, Microsoft en Palo Alto Networks. Anthropic investeert $100M in credits en $4M in open-source securityorganisaties. **Let op:** dit is een dual-use signaal – offensieve AI-capaciteiten voor kwetsbaarheidsdetectie zijn nu bewezen schaalbaar. Bron: [TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/) / [Hacker News](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)

**Prompt injection blijft structureel probleem:** OpenAI erkent dat prompt injection "waarschijnlijk nooit volledig wordt opgelost", vergelijkbaar met social engineering. Bruce Schneier beschreef eerder dit jaar de "promptware kill chain" – een gestructureerde aanvalsmethode op LLM-gebaseerde agents. Met de opkomst van autonome agenten wordt dit risico operationeel, niet langer theoretisch. Bron: [VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay) / [Schneier on Security](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)

---

## 📈 Markt & Adoptie

**Enterprise AI-spend explodeert:** Gartner schat de markt voor AI-applicaties, infrastructure software en services op meer dan $2 biljoen in 2026; AI-software specifiek groeit bijna 60% YoY naar $452 miljard. Banken kondigen plannen aan om agentic AI dit jaar op schaal uit te rollen. Bron: [CIO Dive](https://www.ciodive.com/news/what-to-expect-from-the-ai-boom-this-year/809783/)

**Agent2Agent interoperabiliteit (Microsoft + Google):** Microsoft committeert zich aan Google's A2A-protocol voor interoperabiliteit tussen AI-agenten. De public preview in Azure AI Foundry en Copilot Studio staat op de planning – klanten kunnen dan multi-agent workflows bouwen die platforms overspannen. Dit is een infrastructureel keerpunt voor enterprise agentic deployments. Bron: [CIO Dive](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)

**ROI-verwachtingen hoog maar realistisch nog ver weg:** Meer dan 60% van beslissers verwacht >100% ROI op AI-agenten (gemiddeld 171%). Tegelijk geven C-suite executives aan dat echte transformatie nog jaren vergt. Salesforce voegde ondertussen +6.000 enterprise klanten toe in drie maanden. Bron: [CIO Dive](https://www.ciodive.com/news/enterprise-agentic-AI-adoption-ROI-expectations-PagerDuty/744265/) / [VentureBeat](https://venturebeat.com/technology/while-everyone-talks-about-an-ai-bubble-salesforce-quietly-added-6-000)

---

## 💡 Ctac-relevantie

**EU AI Act compliance (urgent):** De deadline van 2 augustus is concreet. Klanten in hoog-risico sectoren (overheid, zorg, finance) die AI-systemen inzetten hebben nu een krappe vier maanden voor compliance. Ctac kan hier direct waarde toevoegen als begeleider van risicoklassificatie en documentatievereisten. De nieuwe Commissie-richtlijnen van 8 april zijn een goed startpunt voor klantgesprekken.

**Agentic AI als propositie:** De combinatie van Agent2Agent-interoperabiliteit (Microsoft + Google), hoge enterprise ROI-verwachtingen en groeiende adoptiesnelheid biedt een concreet moment om agentic AI als dienst te positioneren bij klanten op Azure. Ctac's positie als Microsoft-partner geeft toegang tot vroege Foundry-preview features.

**Security by design bij AI-projecten:** De Mythos/Glasswing-demonstratie en de erkenning dat prompt injection structureel onoplosbaar is, maken duidelijk dat elke agentic implementatie vanaf dag één securityarchitectuur nodig heeft. Dit is een differentiator voor Ctac als het meedenkt over veilige agent-deployments bij klanten – niet als afterthought maar als baseline.

**Open source kansen:** GLM-5 en de bredere open-source groei (>2M modellen op Hugging Face) maken het mogelijk om voor specifieke klantcasussen kostenefficiënt te experimenteren zonder afhankelijkheid van grote API-providers. Relevant voor klanten met data-soevereiniteitsvereisten.

---

## 📚 Bronnen & verder lezen

- [Microsoft lanceert drie MAI-foundational modellen – TechCrunch](https://techcrunch.com/2026/04/02/microsoft-takes-on-ai-rivals-with-three-new-foundational-models/)
- [Meta Muse Spark – TechCrunch](https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/)
- [GLM-5 open source frontier model – Hugging Face blog](https://huggingface.co/blog/mlabonne/glm-5)
- [Anthropic Mythos / Project Glasswing – TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [Claude Mythos vindt duizenden zero-days – The Hacker News](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
- [Project Glasswing – Anthropic](https://www.anthropic.com/glasswing)
- [Schneier: Promptware Kill Chain](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)
- [EU AI Act implementatie tijdlijn](https://artificialintelligenceact.eu/ai-act-implementation-next-steps/)
- [EC richtlijnen AI-definitie – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Microsoft commits to A2A interoperabiliteit – CIO Dive](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [Enterprise AI-spend 2026 – CIO Dive](https://www.ciodive.com/news/what-to-expect-from-the-ai-boom-this-year/809783/)
- [Agentic AI ROI-verwachtingen – CIO Dive](https://www.ciodive.com/news/enterprise-agentic-AI-adoption-ROI-expectations-PagerDuty/744265/)
- [NOS: AI in militaire beslissingen](https://nos.nl/nieuwsuur/artikel/2609142-zorgen-over-gebruik-van-ai-in-oorlogen-menselijke-afweging-blijft-nodig)
- [OpenAI: prompt injection niet oplosbaar – VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
