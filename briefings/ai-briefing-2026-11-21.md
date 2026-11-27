---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-21
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 21 november 2026

## 🔑 Highlights van de dag

- **Model-sprint bij alle drie de grote labs:** OpenAI (GPT-6.2 Astra/Sol, 17 nov), Anthropic (Claude Fable 5.2, 9 nov) en Google (Gemini 4 Neon, 18 nov) brachten elk een nieuwe generatie modellen uit binnen twee weken. De prijsconcurrentie scherpt aan: Gemini 4 Neon zit op $3/$15 per miljoen tokens.
- **EU AI Act-deadline nadert snel:** Per 2 december 2026 geldt verplichte markering van AI-gegenereerde inhoud (Art. 50) en gelden nieuwe verboden op non-consensueel intiem materiaal. De sandbox-implementatieregels (VO 2026/2487) treden op 1 december in werking – wie dat nog niet heeft geregeld, loopt achter.
- **Kabinetsvisie NL "Kiezen voor AI voor iedereen":** Nederland trekt €120 miljoen voor een Europees AI-project, onderzoekt een eigen AI-veiligheidsinstituut en wil de afhankelijkheid van Big Tech verminderen. Interessant signaal voor Nederlandse IT-partners zoals Ctac.
- **Microsoft + IBM lanceren "Imagine Enterprise":** Een combinatie van 6.000+ AI-agents met IBM Consulting-ondersteuning, gericht op governed en veilige enterprise-AI-adoptie. Directe concurrentie voor de middensegment-markt.
- **52 prompt-injection-CVE's in 2026:** Het aantal officieel geregistreerde kwetsbaarheden in LLM-systemen groeit snel; coding assistants zijn het vaakst doelwit.

---

## 🧠 Technologie & Modellen

**Google Gemini 4 Neon** (18 november) is de meest recente release met een agressief prijspunt van $3/$15 per miljoen tokens. Google claime benchmark-superiority ten opzichte van concurrenten, maar het zijn self-reported cijfers – neem die met gepaste scepsis.

**OpenAI GPT-6.2 Astra** ($8/$40) en **Sol** ($2/$10) werden op 17 november uitgebracht. Sol is daarmee één van de goedkoopste frontier-opties; Astra zit in het premium segment. Naast deze releases lanceerde OpenAI ook een beperkte **GPT-6 Cyber**-variant, uitsluitend toegankelijk via "Daybreak Red"-goedkeuring – waarschijnlijk bedoeld voor security research.

**Anthropic Claude Fable 5.2** is vanaf 9 november algemeen beschikbaar. Er is ook een beperkte *Mythos 5.2*-variant, alleen voor geverifieerde organisaties. Dit volgt Anthropics patroon van stapsgewijze toegang voor gevoeliger toepassingen.

Op het gebied van **agentische systemen** zijn er twee opmerkelijke lanceringen:
- **Databricks Genie ZeroOps** (public beta, 19 nov): monitort data-jobs en tabellen, diagnosticeert fouten via Unity Catalog-metadata en stelt fixes voor als pull requests.
- **Microsoft Copilot Autopilot**: een autonome agent met een eigen Entra-identity en redeneerlaag – een verschuiving naar identity-aware agents die zelfstandig handelen.

*Bronnen: [llm-stats.com](https://llm-stats.com/ai-news), [nhimg.org/llm-release-tracker](https://nhimg.org/llm-release-tracker), [aiagentsdirectory.com](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-18-2026)*

---

## 🏛️ Governance & Ethiek

**EU AI Act – 2 december nadert:** Per 2 december 2026 gelden twee nieuwe verplichtingen:
1. Generatieve AI-systemen die al op de markt zijn, moeten voldoen aan **Art. 50(2)**: markering van AI-gegenereerde inhoud (deepfake-labeling e.d.).
2. Nieuwe verboden op non-consensueel intiem beeldmateriaal en CSAM gegenereerd door AI treden in werking.

De **sandbox-implementatieregels** (Uitvoeringsverordening 2026/2487, in werking 1 dec) zijn op 11 november gepubliceerd in het Publicatieblad. Ook zijn op 12 november de **Art. 50-transparantierichtlijnen** (C/2026/6005) gepubliceerd – dit zijn de beleidshandvatten die organisaties moeten implementeren.

Opvallend: de deadline voor *high-risk* AI-systemen (Annex III) is door het Digital Omnibus-pakket uitgesteld van augustus 2026 naar **2 december 2027** – één jaar uitstel, maar bedrijven die dat als reden gebruiken om niets te doen aan transparantieverplichtingen zitten er naast.

**Nederland:** De kabinetsvisie "Kiezen voor AI voor iedereen" (6 november) zet in op: soevereiniteit (minder Big Tech-afhankelijkheid), €120 mln voor een Europees AI-project onder Duits leiderschap, onderzoek naar een nationaal AI-veiligheidsinstituut, en een Mediapact voor journalistieke content. MKB-ruimte voor AI-toepassing staat expliciet op de agenda; begin 2027 volgt uitwerking van AI-infrastructuur.

*Bronnen: [casrai.org](https://casrai.org/news/eu-ai-act-2-december-2026-obligations-article-50), [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [rijksoverheid.nl](https://www.rijksoverheid.nl/actueel/nieuws/2026/11/06/kabinet-kiest-voor-ai-die-nederland-vooruithelpt), [computable.nl](https://www.computable.nl/2026/11/06/kabinet-wil-ai-ontwikkeling-meer-sturen/)*

---

## 🔐 Security & Risk

**52 prompt-injection-CVE's in 2026** zijn officieel geregistreerd in de NVD (stand: 6 november). Dit is een structurele trend: het aantal exploits in LLM- en agent-software stijgt snel, met coding assistants als meest aangevallen categorie. Vectra noemt een Cursor CVE-keten als recent voorbeeld.

**Memory poisoning** (Lakera AI-onderzoek, november 2026): vergiftigde databronnen kunnen de langetermijngeheugens van agents besmetten. Dit is bijzonder zorgwekkend nu productiepipelines met agents-met-geheugen uitgerold worden.

**Palo Alto Unit 42** (oktober 2026): agents met lange gesprekshistorie zijn significant kwetsbaarder voor manipulatie en persistent injection. De praktische implicatie: hoe langer een agent "leeft", hoe groter het aanvalsoppervlak.

*Bronnen: [airia.com](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/), [stellarcyber.ai](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/), [dev.to/koeseo](https://dev.to/koeseo/52-prompt-injection-cves-in-2026-so-far-what-the-numbers-say-3apj)*

---

## 📈 Markt & Adoptie

**Microsoft + IBM "Imagine Enterprise"** (18 november): de twee bedrijven bundelen 6.000+ AI-agents met Microsoft-cloud en IBM Consulting-implementatiecapaciteit. Dit is een directe aanval op de mid-market en positioneert IBM weer als relevante enterprise-AI-speler naast de pure-play cloudpartijen.

**Google Cloud groeit explosief:** Revenue +103% tot $30,7 mrd in Q3 2026 (bron: aggregator, verifieer via Alphabet-cijfers). De Gemini Enterprise-interface – één universele agent over alle Google Workspace-apps – is in oktober gelanceerd en wordt nu breed uitgerold.

**AT&T** rapporteert bijna 500 autonome workflows in productie, een indicatie dat agent-deployment bij grote ondernemingen echt op gang komt. Flexera 2026-survey: 87% van enterprises heeft een multi-cloud strategie, Azure + Google Cloud meest voorkomende combinatie.

*Bronnen: [cloudwars.com](https://cloudwars.com/cloud-wars-minute/microsoft-and-ibm-unite-to-accelerate-enterprise-ai-adoption/), [aiagentstore.ai](https://aiagentstore.ai/ai-agent-news/this-week), [fatjoe.com](https://fatjoe.com/blog/ai-stats/)*

---

## 💡 Ctac-relevantie

**EU AI Act-compliance is nu urgent werk.** De 2-december-deadline voor Art. 50 (markering van AI-gegenereerde content) is over 11 dagen. Als Ctac klanten heeft die generatieve AI op de EU-markt aanbieden – denk aan chatbots, automatisch gegenereerde documenten, deepfake-detectiesystemen – dan is dit nu actief gesprekspunt richting die klanten. De sandbox-regels en transparantierichtlijnen zijn gepubliceerd en direct toepasbaar.

**Het kabinetsbeleid creëert kansen.** De Nederlandse overheid wil AI-toepassing in het MKB stimuleren en minder afhankelijk worden van Big Tech. Ctac kan zich hier als "trusted local AI partner" positioneren – een bedrijf dat helpt met veilige, compliant AI-implementaties zonder volledige afhankelijkheid van één hyperscaler.

**De agent-security-discussie is een propositie-kans.** Met 52 CVE's en groeiende agent-deployments wordt veilige agent-architectuur een boardroom-onderwerp. Ctac's AI-unit kan zich onderscheiden door security-by-design in agent-trajecten als standaard te zetten – in plaats van het als optionele module te positioneren.

**Microsoft + IBM-alliantie vraagt herpositionering.** Als Ctac Microsoft-partner is, is de Imagine Enterprise-bundeling een kans (implementatiewerk), maar ook een druk op onderscheidend vermogen. Eigen IP, sector-specifieke agents of verticale oplossingen (overheid, zorg, finance) zijn het antwoord op commoditisering van generieke AI-implementaties.

---

## 📚 Bronnen & verder lezen

- [LLM Release Tracker – nhimg.org](https://nhimg.org/llm-release-tracker)
- [LLM News Today – llm-stats.com](https://llm-stats.com/ai-news)
- [AI Agents News Week of Nov 20 – aiagentstore.ai](https://aiagentstore.ai/ai-agent-news/this-week)
- [EU AI Act – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Art. 50 deadline uitleg – casrai.org](https://casrai.org/news/eu-ai-act-2-december-2026-obligations-article-50)
- [Sandbox implementing regulation – praxikon.com](https://www.praxikon.com/en/posts/ai-regulatory-sandbox-rules-article-58-ai-act-implementing-regulation-2026-2487)
- [Kabinetsvisie AI – rijksoverheid.nl](https://www.rijksoverheid.nl/actueel/nieuws/2026/11/06/kabinet-kiest-voor-ai-die-nederland-vooruithelpt)
- [Kabinet wil AI sturen – computable.nl](https://www.computable.nl/2026/11/06/kabinet-wil-ai-ontwikkeling-meer-sturen/)
- [AI security 2026 – airia.com](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [52 prompt injection CVEs – dev.to](https://dev.to/koeseo/52-prompt-injection-cves-in-2026-so-far-what-the-numbers-say-3apj)
- [Agentic AI threats – stellarcyber.ai](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/)
- [Microsoft + IBM Imagine Enterprise – cloudwars.com](https://cloudwars.com/cloud-wars-minute/microsoft-and-ibm-unite-to-accelerate-enterprise-ai-adoption/)
- [AI Usage Statistics Nov 2026 – fatjoe.com](https://fatjoe.com/blog/ai-stats/)
