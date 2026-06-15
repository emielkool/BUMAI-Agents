---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-29
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 29 april 2026

## 🔑 Highlights van de dag

- **OpenAI lanceert GPT-5.5** (23 april): het meest autonome model tot nu toe, sterk in agentic coding, computer use en wetenschappelijk onderzoek. API-beschikbaar tegen $5/1M input-tokens – significante stap richting een "AI super app".
- **Google sluit Pentagon-deal** (28 april): na Anthropic's weigering om z'n AI voor massasurveillance en autonome wapens beschikbaar te stellen, stapt Google in. Dit terwijl 950 eigen medewerkers een open brief tekenden tégen de deal zonder ethische grenzen.
- **EU AI Act-deadline nadert snel**: per 2 augustus 2026 is de wet volledig van kracht. Nationale AI-sandboxen moeten dan operationeel zijn; de Commissie investeert €63,2 miljoen in gezondheid en online veiligheid.
- **Prompt injection onoplosbaar verklaard door OpenAI**: het bedrijf erkent publiekelijk dat de aanvalsvector "net als scams op het web" structureel niet te elimineren is. Slechts 34,7% van organisaties heeft adequate verdediging ingezet.
- **DeepSeek-V4-Pro**: open-source MoE-model met 1,6T parameters en 1 miljoen token context, overbrugt het gat met toonaangevende closed-source modellen op redeneer- en agenttaken.

---

## 🧠 Technologie & Modellen

**GPT-5.5** is per 23 april beschikbaar voor Plus-, Pro-, Business- en Enterprise-gebruikers. OpenAI positioneert het als het "meest intuïtieve model ooit": geef het een rommelige meerstaps-taak en het plant, gebruikt tools, controleert zichzelf en gaat door totdat het klaar is. In de API kost het $5/1M inputtokens en $30/1M outputtokens – duurder dan GPT-5.4, maar met hogere tokenefficiëntie. Codex-gebruikers zien doorgaans minder tokens nodig per taak. Dat is hype + echte vooruitgang in één verpakking. [[bron]](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)

**DeepSeek-V4-Pro** (open-source) staat inmiddels op Hugging Face met 1,6T parameters (49B actief via MoE) en 1M-token context. Coding benchmarks zijn top-tier; reasoning sluit aan bij de top closed-source modellen. Relevant voor organisaties die on-premise of privé willen draaien. [[bron]](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

**Google** lanceerde bij Google Cloud Next '26 de *Agentic Data Cloud*, gericht op enterprise AI-agents die data-pipelines zelfstandig orkestreren. [[bron]](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)

---

## 🏛️ Governance & Ethiek

**EU AI Act – 100 dagen tot volledige werking.** Vanaf 2 augustus 2026 is de AI Act integraal van toepassing. Elke lidstaat moet dan een nationale AI-regulatory sandbox operationeel hebben. De Europese Commissie investeert €63,2 miljoen in AI voor gezondheid en online veiligheid, en werkt aan richtlijnen voor hoog-risico classificatie en transparantievereisten. [[bron]](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)

**Google vs. Anthropic – de Pentagon-splitsing.** Gisteren (28 april) maakte TechCrunch bekend dat Google een nieuw contract heeft getekend waarbij het Pentagon onbeperkte toegang krijgt tot Google AI op geclassificeerde netwerken. Anthropic weigerde eerder op ethische gronden (geen massasurveillance, geen autonome wapens) en kreeg de stempel "supply-chain risk" van het DoD. De rechtszaak loopt; een rechter gaf Anthropic voorlopig een injunctie. [[bron]](https://techcrunch.com/2026/04/28/google-expands-pentagons-access-to-its-ai-after-anthropics-refusal/) Dit is een precedent voor AI-leveranciers: welke klanten zijn you willing to serve?

---

## 🔐 Security & Risk

**Prompt injection: structureel onopgelost.** Drie AI coding agents lekten recent secrets via een enkele prompt injection in een GitHub Action – en Anthropic's eigen system card had het risico al gedocumenteerd. Microsoft patchte CVE-2026-21520 (CVSS 7.5, Copilot Studio), maar data was al geëxfiltreerd vóór de patch. OpenAI's formele conclusie: "prompt injection is hier om te blijven, net als scams op het web." [[bron]](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) [[bron]](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)

Slechts 34,7% van organisaties heeft dedicated prompt injection-verdediging ingezet. Voor elke klant die AI-agents deployt in productie is dit nu een concrete auditcategorie, geen theoretisch risico meer.

---

## 📈 Markt & Adoptie

Microsoft en Google domineren de enterprise AI-leveranciersmarkt. Bijna 75% van Google Cloud-klanten gebruikt AI-producten actief. Toch meldt twee derde van alle bedrijven dat ze vastzitten in de pilotfase: overgang naar productie blijft de bottleneck. Verwacht rendement op AI-investeringen: slechts 27% over de komende 1–2 jaar – verwachtingen worden bijgesteld. [[bron]](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

Google's $40 miljard investering in Anthropic (mede als reactie op competitie van OpenAI) verankert de driehoek Google–Anthropic–Microsoft–OpenAI verder. Consolidatie aan de top versnelt. [[bron]](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)

Multi-agent systemen zijn de dominante trend: meerdere gespecialiseerde agents die samenwerken vervangt het "één model doet alles"-paradigma.

---

## 💡 Ctac-relevantie

**AI Act – nu actie, niet afwachten.** Met 100 dagen tot de volledige inwerkingtreding is dit hét moment voor Ctac om klanten in de high-risk categorieën (overheid, zorg, finance) te benaderen met een concrete compliance-scan. De sandboxvereisten en transparantierichtlijnen zijn nu duidelijk genoeg om te adviseren.

**GPT-5.5 en agentic AI** zijn direct inzetbaar in Ctac-proposities. De stap van "model dat antwoorden geeft" naar "model dat meerstapstaken afrondt" maakt nieuwe use cases mogelijk in procesautomatisering voor klanten. Bespreek intern welke referentiecases je dit kwartaal wil bouwen.

**Prompt injection = klant-risicogesprek.** Elke klant die nu AI-agents in productie brengt, loopt reëel risico. Ctac kan hier waarde toevoegen als trusted advisor door een beveiligingsaudit-aanpak te ontwikkelen specifiek voor agentic AI-deployments.

**Google Pentagon-kwestie**: als Ctac klanten bedient in overheid of defensie-gerelateerde sectoren, vraag je bewust af welke AI-leverancier je adviseert. Antropics ethische grenzen zijn commercieel belastend geworden; Google's keuze heeft reputatie-implicaties voor partners. Zet dit op de agenda.

---

## 📚 Bronnen & verder lezen

- [OpenAI: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [TechCrunch: OpenAI releases GPT-5.5, bringing company one step closer to an AI 'super app'](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)
- [TechCrunch: Google expands Pentagon's access to its AI after Anthropic's refusal](https://techcrunch.com/2026/04/28/google-expands-pentagons-access-to-its-ai-after-anthropics-refusal/)
- [TechCrunch: Google to invest up to $40B in Anthropic](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)
- [EU AI Act – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC: Supporting the implementation of the AI Act with clear guidelines](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [VentureBeat: AI agent runtime security – system card audit](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat: Microsoft Copilot Studio prompt injection CVE](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [VentureBeat: Anthropic publishes prompt injection failure rates](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)
- [CIO Dive: Microsoft, Google rule AI vendor market for enterprises](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive: Google launches Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Hugging Face: DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [airia.com: AI Security in 2026 – Prompt Injection & the Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
