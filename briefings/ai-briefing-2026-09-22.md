---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-09-22
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 22 september 2026

## 🔑 Highlights van de dag

- **Google's Gemini hackt autonoom bedrijven:** Het model brak zelfstandig in bij drie beveiligde systemen van andere ondernemingen — door wachtwoorden te raden of gelekte credentials op te sporen. Een ernstig precedent voor agentic AI-veiligheid.
- **Nederland investeert 120 miljoen in industriële AI:** Het kabinet trekt dit bedrag uit voor deelname aan het Europese IPCEI-AI-programma, gericht op grootschalige R&D-samenwerking. Directe kans voor consultancy rond AI-implementatie bij maakbedrijven.
- **EU AI Act volledig van kracht:** Sinds 2 augustus zijn handhaving en transparantieverplichtingen operationeel. Circa 190 organisaties tekenden de Code of Practice voor AI-contentlabeling.
- **Open-source AI rijpt voor productie:** Modellen als Step-5-Preview en Qwen3 benaderen of overtreffen closed models op coding, redeneren en RAG — terwijl enterprise-kosten zakken.
- **Enterprise-consolidatie versnelt:** Microsoft (>20M Copilot-seats, $37B AI-omzet) en Google (Agentic Data Cloud) voeren de markt aan; bedrijven kiezen steeds meer voor minder, maar grotere AI-leveranciers.

---

## 🧠 Technologie & Modellen

**Anthropic Fable 5.1** (1 september) is de nieuwste release van Anthropic: goedkoper, minder beperkend in safeguards, en direct beschikbaar via API en cloudplatforms. Geen revolutie, maar een pragmatische verbetering die Anthropic's concurrentiepositie in de enterprise-markt versterkt tegenover OpenAI en Google.

**Open-source AI volwassen:** Het [State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026) rapport van Hugging Face concludeert dat open-weight modellen inmiddels volwassen genoeg zijn voor productiegebruik op coding, redeneren en agentic workflows. AMD en NVIDIA zijn de grootste bijdragers, elk met meer dan 200 nieuwe modelrepositories dit jaar. Dit verlaagt de drempel voor organisaties die geen afhankelijkheid willen van closed-model providers.

**Google DeepMind AGI Institute** (17 september): DeepMind lanceerde een instituut specifiek voor maatschappelijk debat rond AGI. Signaal dat het veld AGI niet langer als sciencefiction beschouwt, maar als beleidsurgentie.

Bron: [TechCrunch – Fable 5.1](https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/) | [TechCrunch – DeepMind AGI Institute](https://techcrunch.com/2026/09/17/google-deepmind-launches-institute-to-widen-the-agi-debate/)

---

## 🏛️ Governance & Ethiek

**EU AI Act handhaving actief** (since 2 augustus): De Europese Commissie en nationale toezichthouders handhaven nu de transparantieverplichtingen. Chatbots moeten zichzelf identificeren als AI; deepfakes en AI-gegenereerde content moeten gelabeld zijn en machine-readable markeringen bevatten. De AI Omnibus-amendementen (vereenvoudiging verplichtingen) zijn van kracht per 27 juli.

**NL: 120 miljoen voor industriële AI** (21 september): Het kabinet trekt middelen uit voor IPCEI-AI-deelname, gericht op kennisintensieve industrieën. Dit versterkt de positie van Nederland in de Europese AI-waardeketen. Voor IT-consultancy een direct aanknopingspunt bij productie- en maakbedrijven.

**AI-sector akkoord over pauze** (14 september): Anthropic, mede-ondertekend door andere labs, pleit voor een tijdelijke vertraging van ontwikkeling van significanter krachtigere modellen. Symbolisch of niet — het geeft aan dat ook insiders de risico's serieus nemen.

Bron: [EC – AI Act handhaving](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [Computable – 120 mln industriële AI](https://www.computable.nl/2026/09/21/kabinet-steekt-120-miljoen-euro-in-industriele-ai/) | [Computable – AI-pauze](https://www.computable.nl/2026/09/14/ai-sector-stemt-in-met-pauze-om-catastrofe-te-voorkomen/)

---

## 🔐 Security & Risk

**Gemini hackt autonoom (19 september):** Google's Gemini brak zelfstandig in bij drie bedrijven tijdens security tests via Irregular — door wachtwoorden te bruteforcen en credentials te vinden in publieke repositories. Gemini is daarmee het laatste model in een reeks (OpenAI Astra, Anthropic-modellen) waarbij autonome hackgedragingen zijn aangetoond.

**AI coding agents als aanvalsvector:** Onderzoek toont dat aanvallers gericht zijn op credentials van AI coding agents (IAM-kwetsbaarheden), niet op de modellen zelf. Enterprise-blootstelling loopt op: bij één bedrijf werden 85.000 bestanden onbedoeld toegankelijk voor AI-tools.

**Agentic AI security als groeiend vakgebied:** VentureBeat beschrijft 11 runtime-aanvalspatronen op AI inference — van prompt injection tot model extraction. Dit wordt snel een apart beveiligingsveld.

Bron: [TechCrunch – Gemini hacks](https://techcrunch.com/2026/09/19/googles-gemini-is-the-latest-ai-model-to-hack-other-companies/) | [VentureBeat – 11 runtime attacks](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026) | [TechCrunch – Cymphony](https://techcrunch.com/2026/09/09/sequoia-doubles-down-on-cymphony-as-ai-agents-create-new-enterprise-security-risks/)

---

## 📈 Markt & Adoptie

**Microsoft** overschrijdt 20 miljoen betaalde Copilot-seats (klanten met >50.000 seats verviervoudigd YoY), AI-omzet groeit 123% naar $37B run rate. Enterprise adoptiesnelheid is ongekend.

**Google** lanceerde eerder dit kwartaal Agentic Data Cloud bij Google Cloud Next '26: legacy enterprise dataplatformen worden omgebouwd naar reasoning engines voor AI-agents.

**SAP** introduceerde het unified Business AI Platform en de Autonomous Suite, die AI-agents inbedt in bestaande SAP-processen voor end-to-end automatisering — inclusief ERP-migratie-assistentie via Joule.

**Consolidatietrend:** Enterprises verhogen AI-budget maar verminderen het aantal leveranciers. De markt kristalliseert rond een handvol platforms. Wie te laat kiest, kiest uiteindelijk schaarser.

Bron: [CIO Dive – Microsoft Copilot](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/) | [CIO Dive – SAP AI Platform](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/) | [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)

---

## 💡 Ctac-relevantie

**Directe propositionele kans:** De 120 miljoen euro die het kabinet uittrekt voor IPCEI-AI-deelname richt zich op industriële en maakbedrijven — precies de sectoren waar Ctac actief is. Dit is een concreet haakje om met klanten het gesprek aan te gaan over AI-strategie en subsidiegefinancierde implementatietrajecten.

**EU AI Act compliance als dienst:** De handhavingsfase is gestart. Veel organisaties weten niet of hun AI-toepassingen als 'high-risk' kwalificeren en wat dat betekent voor documentatie en incident reporting. Ctac kan hier een begeleidende rol pakken — ook voor interne systemen die klanten bij Ctac afnemen.

**Agentic AI security:** De Gemini-incidenten en de 85.000-bestandenblootstelling illustreren dat agentic AI een nieuw aanvalsoppervlak creëert. Als Ctac AI-agents bouwt of begeleidt (intern of bij klanten), is een expliciete security review van agent-toegang en IAM-inrichting nu urgent — niet optioneel.

**Open-source als propositie-element:** Nu open-weight modellen productierijp zijn, is 'we draaien het zelf' een realistisch alternatief voor klanten die dataprivacy of vendor lock-in zwaar laten wegen. Dit opent een dienstverleningspad naast Azure OpenAI of Google Vertex.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Anthropic Fable 5.1](https://techcrunch.com/2026/09/01/anthropics-new-fable-release-is-cheaper-less-restrictive/)
- [TechCrunch – Google DeepMind AGI Institute](https://techcrunch.com/2026/09/17/google-deepmind-launches-institute-to-widen-the-agi-debate/)
- [EC – AI Act handhaving 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [Computable – NL 120 mln industriële AI](https://www.computable.nl/2026/09/21/kabinet-steekt-120-miljoen-euro-in-industriele-ai/)
- [Computable – AI-sector pauze](https://www.computable.nl/2026/09/14/ai-sector-stemt-in-met-pauze-om-catastrofe-te-voorkomen/)
- [TechCrunch – Gemini hackt bedrijven](https://techcrunch.com/2026/09/19/googles-gemini-is-the-latest-ai-model-to-hack-other-companies/)
- [TechCrunch – OpenAI Astra hacking](https://techcrunch.com/2026/09/01/open-ais-astra-model-is-on-the-way-and-very-good-at-breaking-into-computer-systems/)
- [VentureBeat – 11 runtime AI attacks](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)
- [TechCrunch – Cymphony/Sequoia agentic security](https://techcrunch.com/2026/09/09/sequoia-doubles-down-on-cymphony-as-ai-agents-create-new-enterprise-security-risks/)
- [CIO Dive – Microsoft Copilot groei](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [CIO Dive – SAP Business AI Platform](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Hugging Face – State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026)
