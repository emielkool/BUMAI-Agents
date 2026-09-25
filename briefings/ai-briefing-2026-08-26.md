---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-26
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 26 augustus 2026

## 🔑 Highlights van de dag

- **OpenAI verlaagt GPT-5.6 Sol-prijzen met 20%+** – Drie maanden na de introductie gooit OpenAI de API-prijs van het Sol-vlaggenschip omlaag voor minstens drie maanden, wat de drempel voor productie-deployments verder verlaagt en de prijsdruk in de hele markt verhoogt.
- **EU AI Act handhaving actief** – Vanaf 2 augustus gelden de transparantieverplichtingen (Artikel 50): chatbots moeten zichzelf onthullen en AI-gegenereerde content moet machineleesbaar worden gemarkeerd. Nederlandse en Belgische bedrijven zijn nu direct vatbaar voor enforcement.
- **AI-gegenereerde exploits richten pijlen op kritische infrastructuur** – Gedocumenteerde aanvallen op Siemens S7 PLC's met AI-gegenereerde exploit-scripts zijn een voorteken van het dreigingslandschap voor industriële systemen, ook in Nederland.
- **Chinese labs domineren open-source AI** – HuggingFace rapporteert dat in vrijwel elke maand van 2026 het grootste open-weight model van een Chinees lab komt; Kimi K2.6 (~1,1 biljoen parameters, MIT-licentie) geldt momenteel als krachtigste open model voor developers.
- **Nederland tweede AI-exporteur van Europa** – Met ruim €80 miljard aan AI-gerelateerde goederenexport staat Nederland op plek 11 wereldwijd, maar het digitale talent blijft achter (18,6% technische studenten vs. 26,9% Europees gemiddeld).

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 prijsverlaging** – Op 21 augustus verlaagde OpenAI de API-prijs van GPT-5.6 Sol met meer dan 20% voor drie maanden. De GPT-5.6-familie bestaat uit Sol (flagship, state-of-the-art op coding en cybersecurity), Terra (balanced) en Luna (cost-efficient). Patroon: prijsdruk door concurrentie versnelt adoptie, maar raakt ook marge van resellers en dienstverleners.
Bron: [OpenAI](https://openai.com/index/gpt-5-6/) · [TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)

**Open-source: Chinese labs aan kop** – Volgens HuggingFaces 'State of Open Models Summer 2026' brengen Chinese labs consequent de grootste open-weight modellen uit. Kimi K2.6 (~1,1T parameters, Modified MIT-licentie) is het krachtigste open model voor developers en een serieus alternatief voor closed-source aanbieders.
Bron: [HuggingFace Blog](https://huggingface.co/blog/state-of-open-models-summer-2026)

## 🏛️ Governance & Ethiek

**EU AI Act handhaving gestart** – Per 2 augustus handhaaft de Europese Commissie de transparantieverplichtingen (Artikel 50). Chatbots moeten gebruikers direct informeren dat ze met AI praten; deepfakes en AI-gegenereerde content moeten machineleesbaar worden gelabeld. De deadline voor hoog-risico systemen is verschoven naar december 2027, maar de huidige verplichtingen gelden al volledig en zijn handhaafbaar.
Bron: [Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) · [Computable](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/) · [NOS](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)

**Adoptie NL/BE** – 61% van Nederlandse bedrijven heeft AI geïmplementeerd (was 49% een jaar geleden); in België 62% (was 52%). Benelux is koploper in Europa, al speelt het tekort aan digitaal talent parten.
Bron: [Computable](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/)

## 🔐 Security & Risk

**AI-exploits op industriële systemen** – AI-gegenereerde exploit-scripts zijn ingezet bij aanvallen op Siemens S7 PLC's in kritieke infrastructuur in de VS. Gecombineerd met het feit dat 28,3% van alle CVEs nu binnen 24 uur na bekendmaking wordt uitgebuit (in 2020 was dat de norm na 700+ dagen), wordt dit een urgent risico voor ook Nederlandse industriële omgevingen.
Bron: [The Hacker News](https://thehackernews.com/2026/08/ai-generated-exploit-scripts-target.html)

**Power users als zwakste schakel** – De top 5% van enterprise AI-gebruikers interacteert 12x zo veel met AI als de rest. Deze "super-adopters" vergroten het risico op shadow AI, datalekkage en ongegidste autonomous agents. Governance-beleid moet worden afgestemd op gebruik-profiel, niet op de gemiddelde gebruiker.
Bron: [The Hacker News](https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users.html)

**Hidden reasoning-lek** – Een kwetsbaarheid in de verwerking van hidden reasoning bij OpenAI, Anthropic en Google maakte het mogelijk om interne redeneerprocessen en secrets (zoals API-sleutels en wachtwoorden) te reconstrueren uit sessie-logs. Inmiddels gepubliceerd als security-disclosure; patching loopt.
Bron: [TechCrunch](https://techcrunch.com/2026/08/09/the-ai-safety-test-is-becoming-a-safety-risk/)

## 📈 Markt & Adoptie

**Hyperscalers verdubbelen AI-infrastructuurinvesteringen** – AI-geoptimaliseerde cloud-infrastructuur spending stijgt dit jaar naar ~$42 miljard; Microsoft, Google en AWS plannen gezamenlijk meer dan $500 miljard aan capex. Dat inference spending nu training overstijgt, is een teken van productie-rijpheid: de markt deployt, niet alleen experimenterend. Google lanceerde de "Agentic Data Cloud" specifiek voor enterprise AI-agents.
Bron: [CIO Dive](https://www.ciodive.com/news/AI-spending-soars-enterprise-maturity/827488/) · [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)

**OpenAI wint terrein bij zakelijke gebruikers** – Recente data toont dat OpenAI Anthropic begint bij te halen op de zakelijke markt. De race tussen closed-source labs verschuift van model-kwaliteit naar prijs, ecosysteem en enterprise-integratie.
Bron: [TechCrunch](https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/)

## 💡 Ctac-relevantie

Drie concrete aandachtspunten voor vandaag:

1. **EU AI Act compliance als propositie** – De handhaving per 2 augustus maakt AI-transparantie geen theoretisch risico meer. Ctac-klanten die chatbots of AI-tools inzetten richting eindgebruikers moeten aantoonbaar voldoen aan Artikel 50. Dit is een directe propositiekans: een "AI Act readiness"-scan of compliance-dienst, met name relevant voor klanten in overheid, zorg en finance.

2. **Shadow AI governance** – Het risicoprofiel van de 5% power users legt bloot dat generieke AI-beleidsdocumenten te grofmazig zijn. Voor Ctac-klanten in gereguleerde sectoren is een gebruiksgerichte AI-governance framework een logisch adviespakket naast technische implementaties.

3. **Open-source als differentiator** – Kimi K2.6 en vergelijkbare open-weight modellen met permissieve licenties verlagen de instapdrempel voor AI-oplossingen waarbij klanten niet afhankelijk willen zijn van hyperscalers. Voor Ctac's IP-strategie biedt dit een fundament: eigen oplossingen bouwen bovenop open modellen, en dat als voordeel positioneren richting klanten die data-soevereiniteit hoog in het vaandel hebben.

## 📚 Bronnen & verder lezen

- [GPT-5.6 – OpenAI](https://openai.com/index/gpt-5-6/)
- [GPT-5.6 lancering – TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [OpenAI wint zakelijke gebruikers – TechCrunch](https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/)
- [State of Open Models Summer 2026 – HuggingFace](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [EU AI Act handhaving gestart – Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [AI Act transparantie-eisen – Computable](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [AI-telefonist moet zichzelf prijsgeven – NOS](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)
- [AI-exploits op Siemens PLC's – The Hacker News](https://thehackernews.com/2026/08/ai-generated-exploit-scripts-target.html)
- [5% power users als security risico – The Hacker News](https://thehackernews.com/2026/08/the-outsized-shadow-why-5-of-ai-users.html)
- [AI safety test als security risico – TechCrunch](https://techcrunch.com/2026/08/09/the-ai-safety-test-is-becoming-a-safety-risk/)
- [AI infrastructuurspending – CIO Dive](https://www.ciodive.com/news/AI-spending-soars-enterprise-maturity/827488/)
- [Google Agentic Data Cloud – CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Nederland tweede AI-exporteur Europa – Computable](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/)
- [Meer cyberaanvallen door AI ook in België – Data News](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
