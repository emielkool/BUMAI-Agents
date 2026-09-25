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

- **Prijsoorlog aan de top:** Anthropic lanceerde Claude Opus 5.5 ($4/$20 per miljoen tokens input/output), en OpenAI reageerde binnen een uur met GPT-6 Sol ($2/$10) en GPT-6 Luna ($0,10/$0,50). Frontier-modellen worden met tientallen procenten goedkoper in één dag.
- **Alibaba Apsara Conference opent:** In Hangzhou presenteerde Alibaba zijn volledige agentic AI-stack: Qwen Book agentic computer, AI-wearables, en de nieuwe Zhenwu V900-chip — drie keer krachtiger dan zijn voorganger, en het sterkste AI-chipplatform van China.
- **Salesforce AIforce:** Op Dreamforce 2026 kondigde Salesforce 'AIforce' aan: een laag die CRM-functionaliteit naar externe interfaces (Claude, Slack, Lightning) brengt. De eigen Koa-reasoning-model is in pilot. Salesforce positioneert AI expliciet als vervanger van de traditionele UI.
- **Agentic AI neem het over van traditionele applicatielagen:** Zowel Salesforce als Alibaba framen hun aankondigingen als "headless" interfaces waarbij AI autonoom toegang krijgt tot bedrijfssystemen — een structurele verschuiving in enterprise software-architectuur.

## 🧠 Technologie & Modellen

**Claude Opus 5.5 (Anthropic):** Flagship-model met focus op coding, autonome werkstromen en professionele taken. Input $4 / output $20 per miljoen tokens — 20% goedkoper dan Opus 5, 30% sneller. Anthropic positioneert Opus 5.5 als het meest capabele model voor complexe agentic taken.

**GPT-6 Sol & Luna (OpenAI):** Sol ($2/$10) is een betaalbaar alternatief voor intensief codeer- en analysewerk; Luna ($0,10/$0,50) richt zich op bulk-taken als samenvatting en extractie. Door Sol en Luna onmiddellijk na de Anthropic-aankondiging uit te brengen, stuurt OpenAI een duidelijk signaal: prijs is het nieuwe battleground.

**Qwen Book (Alibaba):** Een agentic computer met het Qwen Desktop OS als AI-native besturingssysteem. De integratie van foundation models, OS, applicaties en cloudservices in één stack is een directe aanval op de dominantie van Windows/macOS als AI-platform.

**Zhenwu V900 (Alibaba Cloud):** China's krachtigste AI-chip, 3x de prestaties van de M890-voorganger. Strategisch belang: vermindert afhankelijkheid van Nvidia bij Chinese cloudinfrastructuur.

## 🏛️ Governance & Ethiek

**AIforce en headless CRM – governance-implicaties:** Als AI-agents rechtstreeks bedrijfssystemen benaderen zonder traditionele gebruikersinterface, verdwijnt de gebruiker als controlepunt. Dit vergroot de druk op organisaties om machine-identiteitsbeheer en agent-toegangscontrole in te richten — een blinde vlek in de meeste huidige frameworks.

**EU AI Act – GPAI handhaving lopend:** Het European AI Office is de eerste ronde van systeemrisico-evaluaties (van frontier-modelleveranciers boven 10²⁵ FLOP's) aan het verwerken. De publicatie van bevindingen wordt verwacht voor eind Q4 2026. De evaluaties omvatten red-teaming methodologieën, energieverbruik en auteursrecht-conformiteit.

## 🔐 Security & Risk

**Prompt injection via agentic systemen — acuut risico:** Nu agents als Agentforce Coworker (Salesforce) en Qwen Book directe toegang krijgen tot productiesystemen, neemt het aanvalsoppervlak voor indirecte prompt injection sterk toe. De combinatie van brede systeemtoegang en onvoldoende identiteitsbeheer is het meest genoemde kwetsbaarheidspatroon in 2026-rapporten.

**Prijsdruk verhoogt adoptie en dus risico:** Goedkopere modellen verlagen de drempel voor brede enterprise-inzet — maar ook voor misbruik en onbeheerde inzet. De daling van token-kosten compenseert niet de governance-lasten die bij grootschalig gebruik horen.

## 📈 Markt & Adoptie

**Headless enterprise AI als markttrend:** Salesforce AIforce en Alibaba Qwen Book vertegenwoordigen dezelfde trend: applicatielagen worden ontkoppeld van UI en aangestuurd door AI-agents. Dit heeft grote implicaties voor systeemintegratie en de positie van SI-partners.

**Prijscompressie frontier-modellen:** Luna op $0,10/$0,50 maakt GPT-6-kwaliteit binnen bereik van vrijwel iedere onderneming voor bulk-verwerking. Dat verandert de ROI-berekening voor veel use cases die eerder economisch niet haalbaar waren (documentverwerking, grootschalige samenvatting, klantenserviceautomatisering).

**Google mental-market share leider:** Bij zakelijke beslissers scoort Google 16,1% mentale marktaandeel, gevolgd door OpenAI (12,6%) en Microsoft (8,7%). Geen partij heeft dominantie vergrendeld — de markt blijft volatiel.

## 💡 Ctac-relevantie

De Salesforce AIforce-aankondiging is direct relevant voor Ctac-klanten die Salesforce gebruiken: Agentforce Coworker is nu beschikbaar. Ctac kan hier een implementatie- en governance-propositie op bouwen — juist omdat headless AI-toegang nieuwe beveiligings- en integratievraagstukken meebrengt die klanten zelf niet kunnen oplossen.

De prijsoorlog (Opus 5.5 vs. Sol/Luna) maakt het economisch realiseren van AI-use cases eenvoudiger. Ctac kan dit inzetten in businesscases voor klanten: token-kosten zijn niet langer de drempel — de bottleneck is nu implementatie, governance en integratie. Dat is precies waar Ctac waarde levert.

Alibaba's Qwen Book en Zhenwu V900 zijn relevant als signaal voor de opkomst van Chinese AI-platforms in enterprise-context. Dit heeft geopolitieke implicaties voor klanten met leveranciersrisicobeheer. Ctac kan hier een advisory-rol spelen.

## 📚 Bronnen & verder lezen

- [Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war – Simon Willison](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/)
- [Anthropic releases Claude Opus 5.5 and OpenAI counters with two cheaper GPT-6 models – SiliconANGLE](https://siliconangle.com/2026/09/22/anthropic-releases-claude-opus-5-5-and-openai-counters-with-two-cheaper-gpt-6-models/)
- [OpenAI Launches GPT-6 Sol and Luna Minutes After Anthropic Drops Claude Opus 5.5 – Decrypt](https://decrypt.co/378986/openai-launches-gpt-6-sol-luna-anthropic-claude-opus-5-5)
- [Salesforce Launches AIforce at Dreamforce '26 – Salesforce Ben](https://www.salesforceben.com/salesforce-launches-aiforce-at-dreamforce-26-ai-replaces-the-ui/)
- [Alibaba Unveils Agentic Computer, AI Wearables and More at 2026 Apsara Conference – Alizila](https://www.alizila.com/alibaba-unveils-agentic-computer-ai-wearables-and-more-at-2026-apsara-conference/)
- [Dreamforce 2026: The Top Announcements – CX Foundation](https://cxfoundation.com/news/dreamforce-announcements-2026)
