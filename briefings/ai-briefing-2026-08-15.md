---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-15
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 15 augustus 2026

## 🔑 Highlights van de dag

- **OpenAI Ultrafast**: GPT-5.6 Sol draait nu 14× sneller via een Cerebras-partnerschap (750 tokens/sec in limited API preview) — relevant voor tijdkritische enterprise-workflows zoals incident response en klantenservice.
- **EU AI Act handhaving van kracht**: Seit 2 augustus 2026 handhaaft de Europese Commissie de transparantie-eisen van de AI Act; chatbots moeten zichzelf identificeren als AI, deepfakes moeten gelabeld zijn.
- **Atlassian Rovo prompt injection**: Beveiligingsonderzoekers tonen aan dat Rovo via verborgen instructies in geüploade bestanden Jira- en Confluence-data kan lekken naar aanvallers — een directe dreiging voor Ctac-klanten die Atlassian gebruiken.
- **Meta Muse Glimmer 30B** open-source uitgebracht onder Apache 2.0: lokaal draaibaar, multimodaal, gericht op autonome agentische taken — de open-source beweging dringt serieus door tot agent-use cases.
- **Microsoft Copilot >20 miljoen betaalde seats**, AI-omzet surpassing $37 mrd/jaar (+123% YoY): enterprise AI-adoptie is geen experimenteerfase meer.

## 🧠 Technologie & Modellen

**OpenAI Ultrafast mode (13 aug)** — OpenAI bracht een preview uit van Ultrafast, een nieuwe service-tier die GPT-5.6 Sol tot 14× sneller maakt dan standaardverwerking. Mogelijk gemaakt door een partnerschap met chipmaker Cerebras, haalt het systeem 750 output-tokens per seconde. De service is vooralsnog in beperkte preview beschikbaar via de API voor geselecteerde enterprise-klanten; OpenAI noemt toepassingen als incident response, klantenservice en financiële marktanalyse.
*Bron: [OpenAI](https://openai.com/index/previewing-ultrafast/) | [TechCrunch](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/)*

**Meta Muse Glimmer 30B (open-weight)** — Meta's Superintelligence Lab bracht Muse Glimmer uit: een 30B-parameter dense multimodal model onder Apache 2.0, gedestilleerd uit Muse Spark. Het is ontworpen voor lokale agentic tasks (codering, tool use, LLM-as-judge), met een 131K-context en ondersteuning voor 100+ talen — en draait op consumer hardware zonder cloudinfrastructuur.
*Bron: [Hugging Face](https://huggingface.co/meta-models/Muse-Glimmer-30B)*

**Google Gemini: 1 miljard MAU** — Gemini bereikte op 11 augustus 1 miljard maandelijkse actieve gebruikers, Google's snelst groeiende product ooit. ChatGPT bereikte dezelfde mijlpaal in juni 2026. De consumentenrace is duidelijk: twee echt grote spelers met vergelijkbaar bereik.

**GPT-5.6 updates** — OpenAI verbeterde GPT-5.6 Sol voor Plus/Pro-gebruikers en bood GPT-5.6 Luna als nieuwe standaard aan gratis gebruikers. Er werd ook een inspannings-slider geïntroduceerd waarmee gebruikers kunnen kiezen hoeveel "effort" het model inzet per vraag.
*Bron: [OpenAI](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)*

## 🏛️ Governance & Ethiek

**EU AI Act transparantie-handhaving actief (2 aug)** — De Europese Commissie is per 2 augustus begonnen met actieve handhaving van de transparantie-eisen uit de AI Act (Artikel 50). Concreet: interactieve AI-systemen (chatbots, voice-AI) moeten gebruikers informeren dat ze met AI praten; deepfakes en AI-gegenereerde content moeten machine-leesbaar gelabeld zijn. Bedrijven riskeren boetes bij niet-naleving. De deadline voor verplichtingen voor hoog-risico AI-systemen is verlengd tot december 2027 — dat geeft wat extra ruimte, maar transparantie geldt nú.
*Bron: [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [Computable.nl](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)*

## 🔐 Security & Risk

**Atlassian Rovo prompt injection (5 aug)** — PromptArmor publiceerde een kwetsbaarheid waarbij verborgen instructies in een geüpload bestand Rovo kunnen laten opdracht geven om Jira- en Confluence-data naar een aanvaller-gecontroleerde server te sturen — zonder extra goedkeuring van de gebruiker. Een tweede aanvalsvector via de `rovoChatPrompt` URL-parameter werd al op 8 juli door Atlassian gepatcht, maar de content-gebaseerde injectie was op 5 augustus nog werkzaam. Geen CVE-identifier toegewezen.
*Bron: [The Hacker News](https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html)*

**OpenAI/Anthropic/Google API-flaw** — Onderzoekers onthulden een API-kwetsbaarheid waarmee zwakkere AI-modellen de redenering van sterkere (frontier) modellen kunnen decoderen. Dit raakt de fundamenten van model-scheiding in multi-agent architecturen.
*Bron: [The Hacker News](https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html)*

**AI-gestuurde aanvallen versnellen** — CVE's worden gemiddeld binnen 24 uur na publicatie al geëxploiteerd (28,3% van de gevallen) doordat aanvallers AI gebruiken om exploits te versnellen. Dit comprimeerst het window voor patch-management drastisch.
*Bron: [The Hacker News](https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html)*

## 📈 Markt & Adoptie

**Microsoft AI: van experiment naar transformatie** — Microsoft presenteerde FY26 als het jaar van "Frontier Transformation". Copilot heeft nu >20 miljoen betaalde seats (klanten met >50K seats viervoudigden YoY); de AI-omzetrun rate overschreed $37 mrd/jaar (+123% YoY). Microsoft lanceerde tevens eigen in-house modellen (MAI-Image-2.5-Pro, MAI-Voice-2-Flash) die intern OpenAI-modellen vervangen en claimen 89% kostenreductie te bieden.
*Bron: [Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/) | [VentureBeat](https://venturebeat.com/infrastructure/microsoft-launches-new-in-house-ai-models-it-says-cut-costs-up-to-89-versus-openai)*

**Microsoft-OpenAI partnerschap geherstructureerd** — Het exclusiviteitsarrangement is losgelaten: OpenAI kan nu via alle cloudplatforms (AWS, Google Cloud) leveren. Azure blijft primaire partner voor first-launch, maar de race om AI-modellen te hosten is nu volledig open.
*Bron: [VentureBeat](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)*

**Meta Muse Code (5 aug)** — Meta lanceerde Muse Code, een terminal-gebaseerde coding agent voor grote codebases, direct concurrerend met GitHub Copilot en Cursor.
*Bron: [TechCrunch](https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/)*

## 💡 Ctac-relevantie

**EU AI Act — direct actie vereist**: Alle chatbots en AI-interfaces die Ctac bouwt of beheert voor klanten moeten per direct voldoen aan de transparantie-eisen (Artikel 50). Dit is geen toekomstige verplichting maar handhaving nu. Ctac kan hier een concrete compliance-dienst van maken: quickscan + remediatie voor klanten die AI-toepassingen draaien.

**Atlassian Rovo-risico voor Ctac-klanten**: Veel klanten in de Ctac-portfolio gebruiken Jira en Confluence intensief. De Rovo-kwetsbaarheid is een concrete dreiging die nog niet volledig gepatcht is. Dit is een moment om proactief klanten te informeren over het uitschakelen van de web-search optie in Rovo en uploads te beperken totdat Atlassian volledige mitigatie levert.

**Microsoft Copilot-adoptiegolf**: De groeicijfers van Microsoft tonen dat enterprise AI-adoptie in stroomversnelling is geraakt. Ctac's dienstverlening rond Copilot-implementatie, governance-vraagstukken en change management is nu acuter relevant dan ooit — er is een markt voor begeleiding bij opschaling van 50 naar 50.000+ seats.

**Dalende inferentiekosten openen nieuwe use cases**: OpenAI Ultrafast (Cerebras) en Microsoft's eigen modellen die 89% goedkoper zouden zijn dan OpenAI-modellen, signaleren dat de kostenbarrière voor AI in real-time toepassingen snel verdwijnt. Propositie-kans voor Ctac: klanten helpen herdenken welke processen nu wél AI-waardig worden bij lagere kosten.

## 📚 Bronnen & verder lezen

- [OpenAI: Previewing Ultrafast mode](https://openai.com/index/previewing-ultrafast/)
- [TechCrunch: OpenAI Ultrafast 14x speed](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/)
- [EC Digital Strategy: AI Act handhaving per 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [Computable.nl: Wat je moet weten van de AI Act](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [The Hacker News: Atlassian Rovo prompt injection](https://thehackernews.com/2026/08/atlassian-rovo-can-be-tricked-into.html)
- [The Hacker News: OpenAI/Anthropic/Google API flaw](https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html)
- [Microsoft Blog: FY26 AI Frontier Transformation](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [VentureBeat: Microsoft-OpenAI exclusiviteit opgeheven](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)
- [VentureBeat: Microsoft eigen modellen 89% goedkoper](https://venturebeat.com/infrastructure/microsoft-launches-new-in-house-ai-models-it-says-cut-costs-up-to-89-versus-openai)
- [Hugging Face: Meta Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B)
- [TechCrunch: Meta Muse Code coding agent](https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/)
- [AI Weekly: AI News August 13](https://aiweekly.co/ai-news-today)
