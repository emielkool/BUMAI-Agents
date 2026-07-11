---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-11
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 11 juli 2026

## 🔑 Highlights van de dag

- **Historische dag op 9 juli:** Voor het eerst in de AI-geschiedenis lanceerden drie frontier labs (OpenAI, Anthropic, Meta) op dezelfde dag elk een nieuw publiek toegankelijk frontier-model — een signaal dat het tempo van modeluitrol structureel is versneld.
- **Microsoft Frontier Company:** Microsoft investeert $2,5 miljard en zet 6.000 engineers in om direct bij enterprise-klanten embedded te gaan werken aan AI-implementaties — een directe concurrent van traditionele IT-consultants zoals Ctac.
- **EU AI Act: nog 3 weken:** Op 2 augustus 2026 treedt het merendeel van de AI Act-regels in werking (High-Risk + transparantievereisten). Organisaties die nog niet compliant zijn lopen actief risico.
- **Prompt injection domineert AI-security:** OWASP benoemt het als het #1 AI-beveiligingsrisico in 2026, met een groei van 340% jaar-op-jaar — waaronder een zero-click exploit in Microsoft 365 Copilot.
- **Nederlandse AI-Cloud live in oktober:** VOLT, Dell en NorthC Datacenters lanceren een GPU-platform als eerste stap naar een AI Gigafactory in Rotterdam (250.000 GPU's).

---

## 🧠 Technologie & Modellen

OpenAI lanceerde op 9 juli de **GPT-5.6-serie** in drie varianten: Sol (flagship), Terra (midrange) en Luna (snel en goedkoop) — beschikbaar voor alle ChatGPT-gebruikers en API-developers. Op dezelfde dag herintroduceerde Anthropic zijn **Mythos-klasse** flagship-model (na een exportcontrole-blokkade van drie weken) én lanceerde **Sonnet 5** met bijna-Opus 4.8-prestaties voor slechts $2/$10 per miljoen tokens (introductieprijs t/m 31 augustus). Meta voegde daar **Muse Spark 1.1** aan toe als eerste betaald model ($1,25/$4,25).

In het agentic domein lanceerde **AgentPrizm** op 9 juli een AgentMemory- en AgentSkills-platform via REST API + MCP-infrastructuur, waarmee agents persistent geheugen over sessies heen krijgen. Salesforce Headless 360 laat AI-agents nu rechtstreeks data opvragen, metadata deployen en Apex uitvoeren in de CRM-omgeving. Gartner voorspelt dat 40% van de enterprise-applicaties eind 2026 embedded agents bevat — in 2025 was dat nog minder dan 5%.

*Nuchter oordeel: de simultane lancering op 9 juli is symbolisch krachtig maar verandert de technische realiteit niet van de ene op de andere dag. De prijsverlaging bij Anthropic (Sonnet 5) is wél concreet relevant voor klantprojecten die API-kosten meewegen.*

---

## 🏛️ Governance & Ethiek

De **EU AI Act** nadert zijn meest kritische mijlpaal: per **2 augustus 2026** gelden de regels voor High-Risk AI-systemen (Annex III) en transparantieverplichtingen (art. 50). De Europese Commissie presenteerde op 7 juli een **Actieplan Cybersecurity & AI** dat lidstaten, bedrijven en overheden helpt bij aansluiting op de meest geavanceerde AI-modellen.

De Nederlandse overheid lanceerde op 3 juli een **internationale AI-strategie** gericht op veilige en verantwoorde AI-transitie in samenwerking met internationale partners. Het kabinet werkt ondertussen aan toezichtsinrichting voor EU AI Act-handhaving (RDI als aangewezen autoriteit).

*Wat telt: drie weken tot volledige AI Act-handhaving. Voor Ctac-klanten in gereguleerde sectoren (overheid, zorg, finance) is dit hét moment om compliance-gaps in kaart te brengen.*

---

## 🔐 Security & Risk

**Prompt injection** staat voor het tweede jaar op rij op #1 in de OWASP Top 10 voor LLM-applicaties. Aanvallen namen met 340% toe, en 88% van organisaties rapporteerde bevestigde of vermoedelijke AI-agent-security-incidenten in het afgelopen jaar.

Bijzonder zorgelijk is de **EchoLeak-kwetsbaarheid** (CVE-2025-32711) in Microsoft 365 Copilot: een zero-click aanval waarbij kwaadwillenden via een speciaal opgemaakt e-mailbericht gevoelige documenten konden exfiltreren zodra een gebruiker Copilot vroeg zijn inbox samen te vatten — zonder enige actie van het slachtoffer.

In het agentic domein wint **"Agent Zero Trust"** terrein: frameworks van Google DeepMind en Anthropic behandelen agents als potentiële insider threats met strenge guardrails. MCP-risico's (tool-poisoning via Model Context Protocol) zijn een nieuw aandachtspunt.

---

## 📈 Markt & Adoptie

**Microsoft Frontier Company** is de grootste enterprise-move van de week: $2,5 miljard en 6.000 forward deployed engineers die direct bij klanten worden ingebed om AI te implementeren. Partnerecosysteem (Accenture, Capgemini, EY, KPMG, PwC) blijft meegenomen, maar Microsoft claimt nu een groter deel van de implementatiewaardeketen zelf.

**Salesforce Agentforce** meldde $800 miljoen ARR (169% groei jaar-op-jaar) — agentic AI in CRM is geen concept meer maar een marktproduct met aantoonbare traction.

De **Dutch AI Cloud** (VOLT + Dell + NorthC) start in oktober 2026 met GPU-verhuur voor Nederlandse en Europese organisaties — een alternatief voor hyperscaler-afhankelijkheid dat relevant is voor Ctac-klanten met data-soevereiniteitsvereisten.

---

## 💡 Ctac-relevantie

De **Microsoft Frontier Company**-aankondiging is strategisch het meest urgent: Microsoft plaatst 6.000 engineers bij enterprise-klanten voor exact de implementatierol die Ctac ook bedient. Dit is geen aanvulling op het partnerkanaal — het is een directe concurrent in de advies- en implementatiefase. Ctac moet scherp nadenken over differentiatie: sector-specifieke kennis, klantrelaties en snelheid zijn het verdedigbare voordeel.

De **EU AI Act**-deadline van 2 augustus is een directe propositiekans. Klanten in high-risk categorieën (HR-systemen, kredietbeoordeling, essentiële infrastructuur) hebben nú behoefte aan gap-analyse en compliance-roadmaps. Dit is een concreet gespreksonderwerp voor komende klantcontacten.

De **Agent Zero Trust**-beweging bevestigt dat agentic AI-projecten niet zonder security-architectuur kunnen worden uitgerold. Dit raakt Ctac's AI-unit direct: bij elk agentisch systeem moet security by design onderdeel zijn van de deliverable, niet een afterthought.

---

## 📚 Bronnen & verder lezen

- [OpenAI GPT-5.6 lancering – TechXplore](https://techxplore.com/news/2026-07-openai.html)
- [ThursdAI – July 2026 releases overzicht](https://thursdai.news/releases/2026-07)
- [Microsoft Frontier Company – officieel blog](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)
- [Microsoft Frontier Company – HPCwire/BigDATAwire](https://www.hpcwire.com/bigdatawire/2026/07/06/microsoft-launches-new-2-5b-ai-initiative-with-6000-experts-to-help-enterprises-deploy-a/)
- [EU AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act 2026 updates – LegalNodes](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks/)
- [EC Actieplan Cybersecurity & AI – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Prompt injection OWASP #1 – Securance](https://www.securance.com/blog/prompt-injection-the-owasp-1-ai-threat-in-2026/)
- [EchoLeak CVE-2025-32711 – Security Boulevard](https://securityboulevard.com/2026/07/top-7-ai-security-risks-in-2026/)
- [Agent Zero Trust – Technology Radar July 2026](https://www.hectorpincheira.com/en/news/technological-radar-july-2026-ai-agents-go-into-production-and-governance-doesnt-keep-up/)
- [Dutch AI Cloud – Dutch IT Channel](https://www.dutchitchannel.nl/news/755382/nederlandse-ai-cloud-moet-eerste-stap-naar-nederlandse-ai-gigafactory-zijn)
- [Nederlandse internationale AI-strategie – Government.nl](https://www.government.nl/latest/news/2026/07/03/international-strategy-for-safe-and-responsible-ai-transition)
- [AgentPrizm lancering – AI Agents Directory](https://aiagentsdirectory.com/news/ai-agents-directory-daily-brief-july-5-2026)
- [Salesforce Agentforce $800M ARR – Agentic.ai](https://agentic.ai/news)
