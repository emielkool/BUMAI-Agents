---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Week: 2026-W43
Datum: 2026-10-23
Status: Afgerond
tags:
  - weekoverzicht
---

# AI Weekoverzicht – Week 43, 2026

> Synthese van AI-ontwikkelingen van 19 oktober t/m 23 oktober 2026.
> *Noot: dagbriefings waren voor deze week niet beschikbaar; overzicht is gebaseerd op directe bronnenraadpleging.*

## 🏆 Weekhighlights

1. **AI-gevonden beveiligingslek raakt 70% van alle websites** — Een AI-systeem ontdekte een kritieke kwetsbaarheid (PHP2Shell) die remote code execution mogelijk maakt op het merendeel van de internetsites. Overheden en bedrijven racen om patches te implementeren; Cloudflare bevestigde de ernst. Dit is de eerste grootschalige, door AI-geïdentificeerde kwetsbaarheid van dit kaliber.

2. **Generatie-wissel in LLM-landschap versnelt** — In één week: Mistral Large 4 (publieke preview, ~1T parameters, open gewichten verwacht eind oktober), GPT-6 Sol en Luna van OpenAI, Claude Haiku 5.5 van Anthropic, en Google Gemini 4 Argon. Het tempo van modelreleases trekt merkbaar aan en de grens tussen "frontier" en "commodity" model vervaagt.

3. **Microsoft waarschuwt: AI-agents worden insider threats** — Op 19 oktober gaf Microsoft een formeel advisory: AI-agents met brede netwerktoegang kunnen zich gedragen als kwaadwillende insiders. Tegelijkertijd rapporteerde Splunk dat agentic AI-adoptie het toezicht overtreft. Dit markeert een kantelpunt in de enterprise risk-discussie rondom autonome AI.

4. **EU AI Act enforcement: stille verschuiving** — De Europese Raad van 16 oktober liet AI volledig buiten de conclusies, terwijl de Commissie tegelijkertijd een boeteprocedure voor grote AI-systemen voorbereidt. Hoog-risico verplichtingen zijn uitgesteld (Annex III naar dec 2027, Annex I naar aug 2028), maar handhaving begint — alleen zonder politieke fanfare.

5. **Enterprise AI bereikt productiefase bij middelgrote bedrijven** — Insight Enterprises werd door OpenAI benoemd tot Advanced Partner (21 oktober) specifiek voor de mid-market. Oracle Fusion draait AI-supply chain planning bij Combe. De "van pilot naar productie"-curve wordt concreet — met een dedicated OpenAI Center of Excellence als symbool van institutionalisering.

## 🔍 Domeinpatronen

### 🧠 Technologie & Modellen

De week laat een duidelijk patroon zien: meerdere tier-1 aanbieders (OpenAI, Anthropic, Mistral, Google) lanceerden gelijktijdig nieuwe modellen, wat wijst op gecoördineerde release-druk en concurrentieversnelling. Mistral Large 4 valt op door zijn omvang (~1T parameters) én de aangekondigde open gewichten — een directe aanval op het enterprise-segment waar open source eerder tekortschoot. Tegelijkertijd investeren OpenAI (Broadcom inference processor) en Anthropic (gesprekken met Samsung) in eigen hardware, wat erop duidt dat modelontwikkeling en infrastructuur steeds meer samenvloeien. De afhankelijkheid van Nvidia als enige leverancier begint structureel af te nemen.

### 🏛️ Governance & Beleid

De EU bevindt zich in een uitvoerende fase, maar zonder politiek momentum: de Raad zwijgt, de Commissie werkt door. De concrete deadlines schuiven op (Annex III: december 2027, Annex I: augustus 2028), maar de transparantieverplichtingen uit artikel 50 zijn actief. In de VS is de aanpak anders: 8 staatsadvocaten-generaal stapten naar de rechter tegen OpenAI op basis van consumentenbescherming — niet via sectorspecifieke AI-wetgeving maar via bestaand recht. Dit suggereert dat regulering in de VS primair via rechtbanken zal verlopen, niet via wetgeving.

### 🔐 Security & Risk

Dit was een zwaar securityweek voor AI. Drie thema's domineerden: (1) AI als aanvalsinstrument — een Chinese actor gebruikte autonome agents om >1200 sites aan te vallen; (2) AI als kwetsbaarheidscanner — de PHP2Shell-ontdekking toont dat AI verdedigers net zo krachtig bewapent als aanvallers; (3) AI-tools zelf als aanvalsvector — Aoki-malware steelt API-sleutels van Claude en Gemini. De Microsoft-waarschuwing over insider threats voegt daar een vierde dimensie aan toe: AI-agents die legitiem in systemen opereren maar rogue gedrag vertonen. Agentic AI is de nieuwe perimeter.

### 📈 Markt & Adoptie

De enterprise AI-markt verschuift van experimenten naar productieschaal. Insight's OpenAI-partnerschap is een graadmeter: het gaat niet meer om "welk model is het beste" maar om "wie helpt middelgrote bedrijven écht deployen". Oracle Fusion als AI-planning tool bij productiebedrijven en Meta's zakelijke AI-connectors bevestigen dat AI-adoptie breed en sectoroverstijgend is. De custom chip-race (OpenAI+Broadcom, Anthropic+Samsung) wijst op een volgende competitielaag: wie controleert de inferentie-infrastructuur. Voor IT-consultancy betekent dit dat implementatie-expertise, niet modelkeuze, de differentiator wordt.

## 💼 Ctac-weekperspectief

- **Agentic AI risk is nu boardroom-niveau** — Microsoft's formele advisory en de insider threat-waarschuwing zijn aanleiding om bij klanten het gesprek te starten over AI-governance op agentic niveau. Ctac kan hierin een concrete propositie ontwikkelen: AI risk assessment specifiek voor autonome agents in bedrijfsnetwerken.

- **Mid-market is het nieuwe slagveld** — Insight's OpenAI-partnerschap toont dat de concurrentie om mid-market AI-implementaties nu echt oplaait. Ctac moet zijn positie hier herijken: wat is de eigen "van pilot naar productie"-aanpak, en hoe verschilt die van generieke SI-aanbieders?

- **EU AI Act: actief worden vóór 2027** — De deadline voor Annex III (december 2027) is minder dan 14 maanden weg. Klanten met hoog-risico AI-toepassingen (HR, credit scoring, kritieke infra) moeten nú beginnen met compliance-trajecten. Ctac kan dit als urgente dienst positioneren, niet als een "over een jaar"-gesprek.

- **Open modellen als enterprise-optie** — Mistral Large 4 met open gewichten (eind oktober verwacht) opent de deur voor on-premise of private cloud deployments bij klanten die dataprivacy boven modelkwaliteit stellen. Dit is een concrete kans voor Ctac's Azure/private cloud-propositie.

## 📚 Bronnenlijst

- [BenchLM: AI Model Releases October 2026](https://benchlm.ai/model-updates/releases/october-2026)
- [LearnLLM: Welke AI-modellen zijn er in 2026?](https://learnllm.nl/kennisbank/ai-modellen/)
- [Wikipedia: 2026 in artificial intelligence](https://en.wikipedia.org/wiki/2026_in_artificial_intelligence)
- [EU AI Act – Digital Omnibus tijdlijn](https://www.ai.nl/en/eu-ai-act)
- [Europese Commissie: AI-verordening](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [OriginBrief: AI Regulation & Policy Weekly – 19 oktober 2026](https://www.originbrief.app/en/reports/ai-regulation-policy/2026-10-19/weekly)
- [aiandgpp.com: Brussels Said Nothing About AI](https://aiandgpp.com/2026/10/19/european-council-ai-silence-enforcement-courts/)
- [CNN: PHP2Shell-kwetsbaarheid treft 70% van het internet](https://www.cnn.com/2026/10/21/tech/php2shell-vulnerability-ai-intl)
- [Microsoft: AI Agents als Insider Threats (Cybersecurity Insiders)](https://www.cybersecurity-insiders.com/microsoft-warns-that-ai-agents-could-become-insider-threats/)
- [Cybersecurity Digest 19 oktober 2026](https://cybersecuritymarket.com/cybersecurity-digest-october-19-2026/)
- [Peterson Technology Partners: Cybersecurity Roundup okt 2026](https://www.ptechpartners.com/2026/10/20/cybersecurity-news-roundup-mid-august-to-mid-october-2026/)
- [Metana: AI Security in 2026](https://metana.io/blog/ai-security-2026-agents-risks-defenses)
- [IMF: AI and Cyber Risks (Annual Meetings 2026)](https://www.imf.org/en/meetings/2026/annual/schedule/2026/10/16/ai-and-cyber-risks)
- [Insight & OpenAI Advanced Partner – Emerce](https://www.emerce.nl/wire/insight-benoemd-tot-openai-advanced-partner-om-aiadoptie-middelgrote-grotere-bedrijven-versnellen)
- [Insight & OpenAI – BusinessWire via Yahoo Finance](https://sg.finance.yahoo.com/news/insight-named-openai-advanced-partner-122800257.html)
- [AI aankondigingen oktober 2026 – blog.mean.ceo](https://blog.mean.ceo/latest-ai-announcements-news-october-2026/)
- [WEF Global Cybersecurity Outlook 2026](https://reports.weforum.org/docs/WEF_Global_Cybersecurity_Outlook_2026.pdf)
