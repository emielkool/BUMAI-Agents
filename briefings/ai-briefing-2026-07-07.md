---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-07
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 7 juli 2026

## 🔑 Highlights van de dag

- **EU AI Act D-26:** Nog 26 dagen tot 2 augustus, wanneer de Europese Commissie handhavingsbevoegdheden krijgt voor GPAI-modellen – inclusief boetes tot €15 miljoen of 3% van de wereldwijde omzet. Urgentie voor compliance is nu maximaal.
- **GLM-5.2 dicht bij Opus 4.8 – voor een vijfde van de prijs:** Z.ai (Zhipu AI) bracht zijn open-source flagship uit onder MIT-licentie. Het model presteert op agentic benchmarks bijna gelijk aan Claude Opus 4.8 voor ~$1.40/$4.40 per miljoen tokens, versus $5/$25 voor Opus.
- **Microsoft zet 6.000 man in voor enterprise AI-adoptie:** Samen met de lancering van Frontier Company ($25 miljard) positioneert Microsoft zich als de uitvoerende arm voor AI-implementaties bij grote ondernemingen – model-agnostisch.
- **Prompt injection aanvallen stegen 340% YoY:** Unit 42 documenteerde dit jaar de eerste grootschalige indirecte prompt injection aanvallen in productieomgevingen. 88% van ondernemingen rapporteerde AI-beveiligingsincidenten.
- **Meta betreedt de cloud-markt:** Meta Compute Cloud is gepland voor lancering in juli 2026, met GPU-compute en Llama-modellen, 20–30% goedkoper dan AWS, Azure en Google Cloud – zij het nog onbevestigd.

## 🧠 Technologie & Modellen

**Claude Sonnet 5 en Fable 5 (Anthropic)**
Anthropic lanceerde Claude Sonnet 5 op 30 juni – het meest agentische Sonnet-model tot nu toe, dat autonoom browsers en terminals kan bedienen. Het scoort 63,2% op SWE-bench Pro en overtreft Opus 4.8 op Terminal-Bench 2.1. Prijsstelling: $2/$10 per miljoen tokens t/m 31 augustus. Daarnaast is Claude Fable 5 per 1 juli wereldwijd herplaatst nadat het US Commerce Department het exportcontroleverbod ophief – 18 dagen na de blokkade.
*Bron: [Anthropic Newsroom](https://www.anthropic.com/news)*

**OpenAI GPT-5.6 en Jalapeño-chip**
OpenAI's GPT-5.6-familie (Sol, Terra, Luna) is op 26 juni gelanceerd via een door de overheid gecoördineerde toegangslijst, beperkt tot circa 20 vertrouwde partnerorganisaties. De brede beschikbaarheid is uitgesteld op verzoek van de Amerikaanse overheid. Op 1 juli kondigde OpenAI zijn eerste eigen inference-chip aan: de Jalapeño.
*Bron: [LLM Stats](https://llm-stats.com/llm-updates)*

**Z.ai GLM-5.2 – open source, MIT, frontier-klasse**
Z.ai's GLM-5.2 staat op Intelligence Index v4.1 op positie boven DeepSeek V4 Pro en Kimi K2.6. Het model heeft geen regionale beperkingen, werd uitgebracht precies een dag na de Amerikaanse exportblokkade op Anthropic-modellen voor buitenlandse gebruikers – een duidelijk geopolitiek statement.
*Bron: [CNBC](https://www.cnbc.com/2026/06/26/china-zhipu-z-ai-open-source-anthropic-openai.html) · [Euronews](https://www.euronews.com/next/2026/07/03/what-is-glm-52-the-new-chinese-ai-model-thats-rivalling-anthropic)*

**Open-source ecosysteem volwassen**
De 2026-benchmark-top bestaat uit Qwen 3 235B-A22B (beste overall), DeepSeek R1, Llama 4 Scout (10M-token context) en Kimi K2.6. Open-weight modellen zijn productie-rijp voor 90% van de enterprise use cases.
*Bron: [Hugging Face Blog](https://huggingface.co/blog/daya-shankar/open-source-llms)*

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving GPAI start 2 augustus**
De Europese Commissie krijgt over 26 dagen de bevoegdheid om GPAI-leveranciers te beboeten. Eerder dit jaar (7 mei) bereikten Raad, Parlement en Commissie een akkoord om de deadlines voor high-risk AI-systemen (Annex III) te verschuiven naar december 2027 – maar voor GPAI geldt die verlenging niet. Transparantieverplichtingen worden ook in augustus van kracht.
*Bron: [EU Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) · [Inside Global Tech](https://www.insideglobaltech.com/2026/05/28/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)*

**VN-dialoog over AI-governance gestart in Genève**
Op 6 juli begon in Genève het UN Global Dialogue on AI Governance. Het Independent International Scientific Panel on AI publiceerde een voorlopig rapport: het venster voor effectieve mondiale AI-governance staat open, maar niet voor lang.

**VS: vrijwillige standaarden frontier-modellen in de maak**
Het Witte Huis is in vergevorderd overleg met AI-bedrijven over vrijwillige standaarden voor releases van frontier-modellen; aankondiging wordt verwacht in de week van 7 juli.

## 🔐 Security & Risk

**Prompt injection: OWASP #1-bedreiging, 340% meer aanvallen**
In maart 2026 documenteerde Unit 42 de eerste grootschalige indirecte prompt injection aanvallen in productie, waaronder ad-review-ontwijking en systeempromptlekkage op commerciële platforms. Enterprise-survey: 88% van organisaties ervoer het afgelopen jaar een AI-agentbeveiligingsincident.
*Bron: [Help Net Security](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/) · [Securance](https://www.securance.com/blog/prompt-injection-the-owasp-1-ai-threat-in-2026/)*

**Anthropic versterkt veiligheidsprogramma**
Anthropic introduceerde een jailbreak-ernstsframework en een HackerOne-bug bounty programma specifiek voor AI-jailbreaks, naast verdiepte cybersafeguards in Claude Fable 5.
*Bron: [Anthropic Newsroom](https://www.anthropic.com/news)*

## 📈 Markt & Adoptie

**Microsoft:** 6.000 medewerkers ingezet bij enterprises, Frontier Company gelanceerd ($25 miljard), aanbod model-agnostisch inclusief third-party en open-source alternatieven.
*Bron: [American Bazaar Online](https://americanbazaaronline.com/2026/07/02/microsoft-mobilizes-workers-to-accelerate-enterprise-ai-adoption-483962/)*

**AWS:** $1 miljard Forward Deployed Engineering-organisatie; AI-engineers worden direct ingebed bij klanten om agentic AI-oplossingen te co-ontwikkelen en te deployen.

**Google:** Agentic Data Cloud gelanceerd op Google Cloud Next '26, met AI-native architectuur bovenop BigQuery/Vertex. CEO Pichai: inkomsten uit generatieve AI-producten groeide 800%.
*Bron: [CIO Dive](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)*

**Meta:** Compute Cloud in de maak (GPU-compute + Llama), gepland voor juli 2026, 20–30% goedkoper dan incumbents. Tegelijkertijd restructureert Meta met 8.000 ontslagen (10% personeelsbestand) en 7.000 herplaatste medewerkers naar AI-teams.
*Bron: [Windows News AI](https://windowsnews.ai/article/meta-targets-enterprise-ai-with-meta-compute-cloud-service-launch-set-for-july-2026.433272)*

**Blackstone & Qualcomm:** Blackstone investeert $30 miljard in AI-datacenters in Japan; Qualcomm neemt AI-startup Modular over voor $4 miljard.

## 💡 Ctac-relevantie

**EU AI Act compliance: nu of nooit.** Met de handhavingsklok die op 2 augustus afloopt, moeten Ctac-klanten in regulated sectors (zorg, finance, overheid) nú hun GPAI-toepassingen hebben gedocumenteerd en geaudit. Dit is een direct verkoopmoment voor Ctac's AI-compliancedienstverlening – niet als "misschien interessant", maar als urgente behoefte.

**GLM-5.2 en open-source volwassenheid herdefinieert de build-vs-buy-afweging.** Voor klanten die aarzelen vanwege kostenmodellen van gesloten frontier-modellen, opent het open-source aanbod van 2026 nieuwe mogelijkheden voor on-premise of private-cloud deployments met frontier-klasse kwaliteit. Ctac kan hierin onderscheid maken door een objectief modeladvies te leveren.

**Prompt injection is een acute risicofactor in agentic AI-projecten.** Elke Ctac-klant die nu AI-agents inzet of evalueert (RPA-vervanging, documentverwerking, klantenservice), loopt reëel risico. Security-by-design in agentic workflows moet een standaard deliverable worden, geen optionele module.

**Microsoft's model-agnostische aanpak** sluit aan bij wat Ctac zijn klanten kan aanbieden: implementatie-expertise die onafhankelijk is van één leverancier, waarbij de klant controle houdt over de eigen data en het ecosysteem.

## 📚 Bronnen & verder lezen

- [Anthropic Newsroom](https://www.anthropic.com/news)
- [LLM Stats – AI Model Updates July 2026](https://llm-stats.com/llm-updates)
- [CNBC – China's Zhipu AI closes in on US models](https://www.cnbc.com/2026/06/26/china-zhipu-z-ai-open-source-anthropic-openai.html)
- [Euronews – What is GLM-5.2](https://www.euronews.com/next/2026/07/03/what-is-glm-52-the-new-chinese-ai-model-thats-rivalling-anthropic)
- [EU Digital Strategy – AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Inside Global Tech – EU AI Act May 2026 amendments](https://www.insideglobaltech.com/2026/05/28/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)
- [Help Net Security – OWASP prompt injection](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)
- [CIO Dive – Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [American Bazaar – Microsoft 6,000 workers](https://americanbazaaronline.com/2026/07/02/microsoft-mobilizes-workers-to-accelerate-enterprise-ai-adoption-483962/)
- [Windows News AI – Meta Compute Cloud](https://windowsnews.ai/article/meta-targets-enterprise-ai-with-meta-compute-cloud-service-launch-set-for-july-2026.433272)
- [Hugging Face – Open Source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
