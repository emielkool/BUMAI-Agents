---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-17
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 17 november 2026

## 🔑 Highlights van de dag

- **Modellenmarkt in volle gang:** Anthropic (Fable 5.2), Google (Gemini 4 Carbon GA + Hydrogen), OpenAI (GPT-Image-2.6) en Qwen4 Max — allemaal binnen de afgelopen week uitgebracht. De modelstrijd gaat onverminderd door, maar de differentiatie verschuift naar agentic capabilities en enterprise-integratie.
- **Microsoft Ignite start vandaag:** Microsoft onthult vandaag nieuwe Copilot-agentfuncties op Ignite (17–21 november). IBM en Microsoft lanceerden vorige week al "Imagine Enterprise", een platform met 6.000 voorgebouwde agents voor finance en retail.
- **EU AI Act: deadline 2 december nadert:** Generatieve AI-systemen die vóór 2 augustus 2026 al op de markt waren, moeten voor 2 december machine-leesbare markering toevoegen. Ook starten dan twee nieuwe verboden rondom non-consensuele intieme beelden en CSAM.
- **AgentCore-kwetsbaarheid blootgelegd:** Eén prompt naar een exposed Amazon Bedrock AgentCore-agent is voldoende om alle agents in hetzelfde AWS-account over te nemen. MCP-servers worden als nieuw aanvalsdoel beschreven.
- **Exploitatietijd halveert:** Het aantal CVEs in 2026 overtrof 100.000 en de mediane tijd van disclosure naar actieve exploitatie daalde van 120 naar 80 dagen. ENISA spreekt van "industrialisatie van vulnerability discovery" door AI.

---

## 🧠 Technologie & Modellen

**Anthropic** bracht op 9 november **Claude Fable 5.2** uit ($8/M tokens), met een beperkte variant genaamd Mythos 5.2 exclusief voor gescreende organisaties via Claude Security. Dat Anthropic een apart "enterprise-veiligheids"-tier bouwt is een signaal dat ze zich positioneren in gereguleerde sectoren.

**Google** maakte Gemini 4 Carbon op 10 november algemeen beschikbaar, gevolgd door Gemini 4 Hydrogen op 13 november via API. Vanaf 1 december sturen Gemini API-aanroepen naar gemini-2.5-pro en -flash automatisch door naar nieuwere versies — een subtiele maar relevante API-wijziging voor bestaande integraties.

**Meta** introduceerde **Muse Ember**, geoptimaliseerd voor herhaalde agenttaken (tool calls, codeertaken, documentparsing). **Runway** maakte Praxis-1, een world model, open source (Apache 2.0). **Qwen4 Max** (Alibaba) is vanaf 16 november beschikbaar via de Qwen API.

**OpenAI** lanceerde GPT-6-Cyber (beperkt, voor security-teams), twee nieuwe beeldmodellen (GPT-Image-2.6 Sunburst en Flare), en ChatGPT Wallet — waarmee agents kunnen betalen namens gebruikers zonder toegang tot een echte betaalkaart. ChatGPT Enterprise is nu ook beschikbaar in de AWS Marketplace.

---

## 🏛️ Governance & Ethiek

De **EU AI Act** nadert een volgende mijlpaal: op **2 december 2026** treden twee nieuwe verplichtingen in werking:
1. Generatieve AI-systemen op de markt vóór 2 augustus moeten machine-leesbare markering toevoegen (Art. 50(2)).
2. Verboden op AI die non-consensuele intieme beelden of CSAM genereert.

De **AI Omnibus** (Verordening EU 2026/1744) is per 27 juli 2026 van kracht. Op 16 november publiceerde de Commissie een concepttemplate voor *fundamental rights impact assessments* (Art. 27) — een instrument dat deployers van hoog-risico AI-systemen moeten invullen. De Europese Commissie presenteerde AI-soevereiniteit en rekencapaciteit ook op de EU-top in Dublin.

Praktijkadvies: hoog-risico AI-toepassingen binnen Ctac-klantomgevingen vallen mogelijk onder Art. 27 — de concepttemplate is nu beschikbaar om te reviewen.

---

## 🔐 Security & Risk

De combinatie van AI-versnelde kwetsbaarheidsontdekking en snellere exploitatie creëert een fundamenteel nieuwe risicoprofielen. Drie specifieke dreigingen verdienen directe aandacht:

1. **AgentCore account-takeover (AWS Bedrock):** Eén prompt naar een exposed agent volstaat om metadata-service-credentials te stelen en álle agents in het account over te nemen. Partijen die Amazon Bedrock AgentCore inzetten moeten de blootstelling van endpoints direct controleren.
2. **MCP-servers als aanvalsdoel:** Trellix benoemt AI-orchestratietools en MCP-servers als nieuw aanvalstarget — relevant voor iedereen die multi-agent architecturen bouwt.
3. **Cross-tenant lek Cloudflare Workers AI:** Veroorzaakt door een upstream SGLang-bug, inmiddels gepatcht. Laat zien dat AI-infrastructure-stack risico's draagt die buiten de traditionele applicatielaag liggen.

---

## 📈 Markt & Adoptie

Forrester stelt dat drie kwart van de enterprises agentic AI *adopteert*, maar weinig bedrijven schalen het daadwerkelijk. Bij bedrijven boven de $1 miljard omzet schaalt nu 40% agents (was 27% vorig jaar). Governance en security zijn de voornaamste remmers — niet de technologie zelf.

**Microsoft Ignite** (17–21 november) is de grote marktgebeurtenis van deze week. Verwacht aankondigingen rond Copilot-agents, Azure AI Foundry en enterprise governance-tooling. Vorige week lanceerden IBM en Microsoft al "Imagine Enterprise" met 6.000 voorgebouwde enterprise-agents voor finance en retail.

**Anthropic** bevestigde dat Claude Managed Agents nu binnen de eigen security-perimeter van klanten kunnen draaien — een directe respons op data-soevereiniteitszorgen in Europa.

---

## 💡 Ctac-relevantie

**Drie directe aandachtspunten:**

1. **Microsoft Ignite (vandaag):** Volg de Copilot-aankondigingen actief. Ctac werkt met Microsoft-stack en klanten verwachten advies over wat de nieuwe agentfuncties betekenen voor hun workflows. Dit is een kans voor een snelle klantupdate of webinar.

2. **EU AI Act deadline 2 december:** Voor klanten die generatieve AI inzetten die vóór augustus live was, is de clock naar 2 december gaande. Ctac kan hier als adviseur optreden — zeker met de nieuwe Art. 27-template die nu beschikbaar is. Dit is concreet leverbaar consultancywerk.

3. **Agent security als propositie:** De AgentCore-kwetsbaarheid en MCP-aanvallen laten zien dat agentic architecturen specifieke security-expertise vereisen die de meeste klanten niet in huis hebben. Ctac kan dit adresseren in de AI-unit propositie: niet alleen bouwen, maar ook security-review van agent-architecturen.

---

## 📚 Bronnen & verder lezen

- [New AI Models — November 2026 LLM Releases (llmgateway.io)](https://llmgateway.io/timeline)
- [New AI Models in November 2026: Every Major Release (BeevR)](https://beevr.ai/blog/ai-model-releases-november-2026)
- [EU AI Act Timeline: Every Deadline 2026 Update](https://aiethicsassessor.com/blog/eu-ai-act-timeline-every-deadline-2026)
- [EU AI Act News November 2026](https://blog.mean.ceo/eu-ai-act-news-november-2026/)
- [EU leaders put AI sovereignty on Dublin agenda (FINCHANNEL)](https://finchannel.com/eu-leaders-put-ai-sovereignty-computing-capacity-and-safeguards-on-dublin-agenda/141447/world-2/europe/2026/11/)
- [GenAI security November 2026: Workers AI leak, three vLLM flaws (Adversa)](https://adversa.ai/blog/top-genai-security-resources-november-2026/)
- [AI agent security November 2026: AgentCore takeover (Adversa)](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/)
- [The CyberThreat Report: November 2026 (Trellix)](https://www.trellix.com/advanced-research-center/threat-reports/november-2026/)
- [AI Agents News Brief: November 11, 2026 (aiagentsdirectory.com)](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-11-2026)
- [The State Of Agentic AI In 2026 (Forrester)](https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/)
- [AI Trends November 2026: Agentic AI Takes Center Stage](https://tashios.com/blog/ai-trends-november-2026-agentic-ai)
- [Building AI that can work across the enterprise (MIT Technology Review)](https://www.technologyreview.com/2026/11/16/1146070/building-ai-that-can-work-across-the-enterprise/)
- [AI Regulation News November 2026: EU Dec 2 and US Midterms (Cubbbix)](https://cubbbix.com/blog/ai-regulation-november-2026-global-update)
- [CISO Daily Briefing – 16 november 2026 (Cloud Security Alliance)](https://labs.cloudsecurityalliance.org/research/ciso-daily-briefing-20261116/)
