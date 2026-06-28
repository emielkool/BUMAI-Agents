---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-28
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 28 juni 2026

## 🔑 Highlights van de dag

- **OpenAI begrensd door Witte Huis:** GPT-5.6 (Sol, Terra, Luna) officieel aangekondigd maar bewust gelimiteerd tot ~20 vertrouwde partners na druk van de Trump-regering — een precedent dat de toegang tot frontier-modellen politiek maakt.
- **EU AI Act tikt naderbij:** Volledige toepasselijkheid op 2 augustus 2026; transparantieregels gaan dan gelden. Op 19 juni lanceerde de Commissie het AI Act Advisory Forum. Minder dan 6 weken te gaan.
- **Agentic AI = aantoonbaar beveiligingsrisico:** Drie AI-coderingsagenten lekten gevoelige secrets via één prompt-injection-aanval. CVE-2026-22708 in Cursor maakt remote code execution mogelijk via agentic IDE's.
- **Microsoft Agent 365 naar GA:** Governance-platform voor AI-agents verlaat preview — inclusief runtime-blokkering en shadow-AI-detectie. Prijskaartje: $99/maand.
- **Benelux loopt voor:** Adoptiepercentage van 49–52% tegenover 42% Europees gemiddelde — maar de digitale kloof met niet-gebruikers groeit mee.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6: Sol, Terra en Luna** zijn aangekondigd als volgende generatie modellen, maar een executive order van Trump (2 juni) verplicht federale instanties tot veiligheidsassessments voordat modellen breed uitgerold mogen worden. OpenAI distantieert zich openlijk van de beperking en belooft een algemene release "binnen enkele weken". Prijzen: Sol $5/$30, Terra $2,50/$15, Luna $1/$6 per miljoen tokens — vergelijkbaar met het Anthropic Fable 5-niveau. ([TechCrunch](https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/), [OpenAI](https://openai.com/index/previewing-gpt-5-6-sol/))

**Aziatische frontier-modellen:** Chinees beveiligingsbedrijf 360 lanceerde Tulongfeng en Japanse Sakana AI bracht Fugu uit — beide claimen Mythos/Fable 5-niveau te bereiken. De Anthropic-exportbeperking drijft Aziatische spelers naar zelfvoorzienende alternatieven, een trend die versnelt. ([TechCrunch](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/))

**Open source:** Qwen 3.6-27B (Alibaba) is beschikbaar op Hugging Face, gericht op stabiele productieomgevingen en codeertoepassingen. De open LLM-leaderboard toont een steeds dichtere benchmark-clustering — het gat tussen open en closed source verkleint. ([Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B))

---

## 🏛️ Governance & Ethiek

**EU AI Act: 35 dagen tot volledige toepasselijkheid.** Op 2 augustus 2026 treedt de volledige EU AI Act in werking, inclusief transparantieverplichtingen. Het inaugurele AI Act Advisory Forum vond op 19 juni plaats. Tegelijk won het Europese EUROPA-consortium (led door Italiaans Domyn) de Frontier AI Grand Challenge — bedoeld om een Europees open-source frontier-model te bouwen als strategisch alternatief. ([EU AI Act](https://artificialintelligenceact.eu/), [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

**VS versus open markt:** De Trump executive order van 2 juni creëert een nieuw precedent — frontier-modellen worden eerst geassesseerd voordat ze publiek gaan. OpenAI vindt dit uitzonderlijk en wil er geen norm van maken. De spanning tussen AI-veiligheid en vrije markt wordt steeds concreter. ([TechCrunch](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/))

**NL:** De rijksbrede chat-tool Vlam groeit uit tot soeverein AI-platform voor ministeries — een directe respons op afhankelijkheid van Amerikaanse hyperscalers. ([Computable](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/))

---

## 🔐 Security & Risk

**Agentic AI als aanvalsvlak:** Drie AI-coderingsagenten lekten productiesecrets via één kwaadaardig commentaar in code — prompt injection als supply chain-vector. VentureBeat meldt dat dit voorspeld werd in de system cards van de betrokken tools. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

**CVE-2026-22708 (Cursor):** Remote code execution via indirect prompt injection in de populaire AI IDE. Exploiteert hoe agentic IDE's shell-commando's verwerken. ([airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

**Cijfer om in je achterhoofd te houden:** 94,4% van state-of-the-art LLM-agents is kwetsbaar voor prompt injection volgens recent onderzoek. Dit is geen theoretisch risico meer.

---

## 📈 Markt & Adoptie

**Microsoft Agent 365 naar GA** met runtime-blokkering, shadow-AI-detectie en asset context mapping via Intune/Defender. $99/maand positioneert dit als enterprise-standaard. De framing van "ungoverned agents als corporate double agents" is bewust alarmerend — en effectief. ([VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat))

**SAP** consolideert data, AI en governance onder één SAP Business AI Platform, in samenwerking met AWS en Snowflake. Relevant voor Ctac's SAP-klanten. ([CIO Dive](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/))

**Benelux:** Adoptiepercentage 49–52% vs. 42% EU-gemiddelde. Vlaanderen signaleert groeiende digitale kloof: Gen AI is "bijna overal" maar creëert tweedeling. In Nederland ziet de tech-sector maatwerk AI verschuiven van experiment naar kritische bedrijfsfunctie. ([Computable](https://www.computable.nl/persberichten/maatwerk-ai-in-de-nederlandse-tech-sector-van-experiment-naar-onmisbare-sta/), [Data News](https://datanews.knack.be/nieuws/belgie/maatschappij-belgie/gen-ai-is-nu-bijna-overal-in-vlaanderen-maar-creeert-een-nieuwe-digitale-kloof/))

---

## 💡 Ctac-relevantie

**EU AI Act deadline (2 augustus):** Klanten die Ctac ingeschakeld hebben voor AI-implementaties moeten nú getoetst worden op de transparantieverplichtingen. Denk aan documentatieplicht voor high-risk toepassingen. Ctac kan de komende weken actief aanbieden om een AI Act readiness-check te doen — dit is een concreet haakje voor gesprekken in finance en overheid.

**Agent security als propositie:** De aaneenschakeling van incidents (Cursor CVE, prompt injection leaks) maakt AI security governance een verkoopbaar aanbod. Combineer dit met Microsoft Agent 365 als referentieplatform: Ctac kan klanten helpen hun agentic AI-landschap in kaart brengen en te beveiligen — direct gerelateerd aan de shadow AI-problematiek die Microsoft nu formeel adresseert.

**SAP-klanten:** De lancering van SAP Business AI Platform biedt kansen voor Ctac's SAP-praktijk om AI-governance en integratie als meerwaarde te positioneren bij bestaande klanten die al op SAP zitten.

**Geopolitieke fragmentatie van AI-toegang:** De US-exportbeperkingen op Anthropic-modellen en de Witte Huis-bemoeienis met GPT-5.6 zijn een signaal dat organisaties vendor-diversificatie moeten overwegen. Het Europese EUROPA-project en de Vlam-tool zijn eerste stappen. Ctac kan hier een onafhankelijk perspectief bieden: multi-cloud, multi-model architecturen.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI limits GPT-5.6 rollout after government request](https://techcrunch.com/2026/06/26/openai-limits-gpt-5-6-rollout-after-government-request-says-restrictions-shouldnt-be-the-norm/)
- [OpenAI – Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)
- [VentureBeat – OpenAI unveils GPT-5.6 Sol, Terra and Luna](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)
- [TechCrunch – White House asking OpenAI to slow roll new model](https://techcrunch.com/2026/06/25/the-white-house-is-asking-openai-to-slow-roll-the-release-of-its-new-model-over-safety-concerns/)
- [TechCrunch – Asian AI startups launch Mythos-like models](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/)
- [TechCrunch – It's not about Anthropic vs. OpenAI anymore](https://techcrunch.com/2026/06/26/its-not-about-anthropic-vs-openai-anymore/)
- [EU AI Act – Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Governance and enforcement of the AI Act](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [VentureBeat – Microsoft takes Agent 365 out of preview](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [VentureBeat – Three AI coding agents leaked secrets via prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [airia.com – AI Security in 2026: Prompt Injection](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Microsoft, Google rule AI vendor market for enterprises](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CIO Dive – SAP creates single platform for building, deploying AI](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [Computable – Vlam in de ai-pan bij rijksambtenaren](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/)
- [Computable – Maatwerk AI in de Nederlandse tech-sector](https://www.computable.nl/persberichten/maatwerk-ai-in-de-nederlandse-tech-sector-van-experiment-naar-onmisbare-sta/)
- [Data News – Gen AI in Vlaanderen creëert nieuwe digitale kloof](https://datanews.knack.be/nieuws/belgie/maatschappij-belgie/gen-ai-is-nu-bijna-overal-in-vlaanderen-maar-creeert-een-nieuwe-digitale-kloof/)
- [Hugging Face – Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)
