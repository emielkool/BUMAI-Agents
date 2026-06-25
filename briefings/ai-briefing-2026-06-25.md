---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-25
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 25 juni 2026

## 🔑 Highlights van de dag

- **Alibaba Qwen-AgentWorld** (24 juni) traint modellen niet als agents maar als *world models* die tool-uitkomsten voorspellen — en verbetert zo agentische prestaties op zeven benchmarks zonder directe agentische training. Methodologisch interessant voor de hele sector.
- **CVE-2026-5027** is actief in het wild: aanvallen op LangFlow/LangChain-servers (7.000+ geraakt, eerste hits 8 juni). Onderzoek toont dat 94,4% van state-of-the-art LLM-agents kwetsbaar is voor prompt injection — geen theoretisch probleem meer.
- **EU AI Act**: op 2 augustus 2026 wordt de wet volledig van kracht, inclusief transparantieregels. De Europese Commissie hield op 19 juni de inaugurele sessie van het AI Act Advisory Forum.
- **Microsoft Copilot**: 20+ miljoen betaalde seats, 123% YoY AI-omzetgroei (>$37 mrd). De enterprise-markt consolideert razendsnel richting Microsoft en Google.
- **Vlam** (Veilige Lokale AI Modellen) van SSC-ICT en AIVD bereidt productie-uitrol voor in H2 2026 — het soevereine rijksbrede AI-platform voor de Nederlandse overheid.

## 🧠 Technologie & Modellen

**Alibaba Qwen-AgentWorld** (gepubliceerd 24 juni) introduceert world model pre-training als voorstap op agentisch fine-tunen: modellen leren eerst tool-uitkomsten te voorspellen, en generaliseren daarna beter als agent. Resultaat: verbeterde prestaties op zeven benchmarks, ook op drie datasets die het model nooit eerder zag. Strategisch relevant — minder trainingsdata, betere transfer naar nieuwe taken. [VentureBeat](https://venturebeat.com/technology/alibabas-model-never-trained-as-an-agent-and-improved-agent-performance-across-seven-benchmarks)

**Anthropic Sonnet 4.6** is de huidige standaard in claude.ai (Free en Pro). Opus 4.8 (mei) voegde een dynamic workflow-tool toe. Anthropic breidde haar partnerschap met Google en Broadcom uit voor gigawatt-schaal compute-capaciteit. [Anthropic](https://www.anthropic.com/news/claude-sonnet-4-6)

**Google Gemini 3.5 Flash** zet in op agents als primair paradigma, niet chatbots. 75% van Google Cloud-klanten zet AI-producten actief in. **Token-kosten** lopen op: de industrie worstelt met de rekening van 24/7 draaiende agent-workflows — niet elke use case is economisch rendabel. [TechCrunch – Gemini](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/) | [TechCrunch – token costs](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/)

## 🏛️ Governance & Ethiek

**EU AI Act Advisory Forum** hield op 19 juni zijn oprichtingsvergadering. **Datum om in de agenda te zetten: 2 augustus 2026** — dan treden alle verplichte bepalingen (inclusief transparantieregels artikel 50) volledig in werking. Lidstaten moeten vóór die datum ook minstens één AI regulatory sandbox operationeel hebben. [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support)

**Vlam** (Veilige Lokale AI Modellen) wordt door SSC-ICT en AIVD klaargestoomd voor rijksbrede uitrol in H2 2026: volledig soeverein, data en modellen onder Nederlandse controle — alternatief voor ChatGPT, Claude en Gemini bij ministeries. Tegelijkertijd bericht NOS dat de overheid volop AI gebruikt maar nauwelijks naar risico's kijkt. [Computable](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/) | [NOS](https://nos.nl/l/2540979)

## 🔐 Security & Risk

**CVE-2026-5027** is op 8 juni aan de exploited-vulnerabilities lijst van VulnCheck toegevoegd na in-the-wild aanvallen op LangFlow/LangChain-servers. Meer dan 7.000 servers getroffen. Onderzoek bevestigt dat 94,4% van LLM-agents kwetsbaar is voor prompt injection — security-experts voorspellen dat het erger wordt voor het beter wordt. [VentureBeat](https://venturebeat.com/security/7000-langflow-servers-under-attack-langgraph-langchain-same-holes)

**Microsoft Copilot Studio** (CVE-2026-21520, CVSS 7.5): indirecte prompt injection waarbij data ondanks de patch geëxfiltreerd kon worden. Tegelijk lanceerde Microsoft **MXC (Microsoft Execution Containers)**: een OS-niveau sandbox in Windows die IT-beheerders laat declareren wat een AI-agent kan en niet kan, enforced door de kernel. [VentureBeat – Copilot](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook) | [VentureBeat – MXC](https://venturebeat.com/security/microsoft-launches-mxc-an-os-level-sandbox-for-ai-agents-with-openai-and-nvidia-already-on-board)

**NewCore** verscheen uit stealth met $66 miljoen (15 juni) voor authenticeerbare identiteiten voor AI-agents — een cruciaal ontbrekend stuk in enterprise governance. Goldman Sachs en McKinsey (25.000 agents naast 60.000 medewerkers) bevestigen dat agents als digitale collega's worden ingezet. [TechCrunch](https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/)

## 📈 Markt & Adoptie

**Microsoft** overstijgt $37 mrd AI-omzet (+123% YoY) met 20+ miljoen Copilot paid seats. **Google**: KPMG behaalde 90% Gemini Enterprise-adoptie bij medewerkers met meer dan honderd agents in de eerste maand. Toch blijft twee derde van bedrijven vastzitten in de pilot-fase. [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)

**Benelux** is Europees koploper: Nederland 61% (+12 pp YoY), België 62% AI-adoptie onder bedrijven. Maar 58% noemt gebrek aan digitale vaardigheden de grootste hindernis. **Coralogix** haalde $200 mln op (3 juni) voor AI-agent monitoring — signaal dat 'wie bewaakt de agents?' een volwassen markt wordt. [Computable](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/) | [TechCrunch](https://techcrunch.com/2026/06/03/coralogix-raises-200m-in-race-to-build-the-monitoring-layer-for-ai-agents/)

## 💡 Ctac-relevantie

**Agent governance is de nieuwe compliance-uitdaging.** Prompt injection in het wild, de Copilot Studio CVE en NewCore's $66M-ronde voor agent-identiteiten maken één ding duidelijk: klanten die agentic AI inzetten hebben een *governance framework* nodig dat verder gaat dan modelkeuze. Ctac kan hier positie innemen door samen met klanten agent-beleid, rolscheiding en monitoring in te richten — vóór een incident hen dwingt.

**Vlam als kans in de publieke sector.** De rijksoverheid kiest voor soevereine AI-infrastructuur; dat vraagt om adviseurs die helpen integreren, beleid schrijven en compliancy borgen richting EU AI Act (deadline 2 augustus). Ctac's overheidsklanten zullen Vlam binnenkort op hun agenda hebben.

**Benelux AI-adoptie is bovengemiddeld, talent is de bottleneck.** Precies het gat dat Ctac als IT-consultancy kan vullen — mits de AI-unit snel schaalbare methodieken ontwikkelt voor adoptie-begeleiding en AI change management.

## 📚 Bronnen & verder lezen

- [Alibaba Qwen-AgentWorld – VentureBeat](https://venturebeat.com/technology/alibabas-model-never-trained-as-an-agent-and-improved-agent-performance-across-seven-benchmarks)
- [Anthropic Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)
- [Gemini 3.5 Flash: agents, not chatbots – TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/)
- [Token-kosten analyse – TechCrunch](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/)
- [EU AI Act Advisory Forum – Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/ai-act-enforcement-gets-independent-expert-support)
- [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [Vlam – Computable](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/)
- [Overheid en AI risico's – NOS](https://nos.nl/l/2540979)
- [CVE-2026-5027 / LangFlow aanvallen – VentureBeat](https://venturebeat.com/security/7000-langflow-servers-under-attack-langgraph-langchain-same-holes)
- [Copilot Studio prompt injection – VentureBeat](https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook)
- [Microsoft MXC OS-sandbox – VentureBeat](https://venturebeat.com/security/microsoft-launches-mxc-an-os-level-sandbox-for-ai-agents-with-openai-and-nvidia-already-on-board)
- [NewCore $66M voor agent-identiteiten – TechCrunch](https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/)
- [Microsoft vs Google enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Benelux AI-adoptie – Computable](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [Coralogix $200M agent monitoring – TechCrunch](https://techcrunch.com/2026/06/03/coralogix-raises-200m-in-race-to-build-the-monitoring-layer-for-ai-agents/)
