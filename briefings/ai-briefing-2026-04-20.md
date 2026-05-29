---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-04-20
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 20 april 2026

## 🔑 Highlights van de dag

- **OpenAI breidt Codex sterk uit**: het platform kan nu zelfstandig op de desktop opereren, apps openen en via een ingebouwde browser taken uitvoeren — een directe aanval op Anthropic's agentische ambities.
- **Anthropic Mythos in preview**: Anthropic's nieuwe frontier-model is exclusief beschikbaar voor 40 partnerorganisaties in cybersecurity, waaronder Microsoft, Apple en CrowdStrike — een strategische keuze die inzet op vertrouwde ecosystemen vóór brede release.
- **Microsoft committeert aan Agent2Agent-standaard**: door in te stappen op Google's A2A-protocol kiest Microsoft voor interoperabiliteit tussen agenten — een stap die multi-agent enterprise-workflows gangbaar gaat maken.
- **EU AI Act nadert volledige handhaving**: de toezichts- en handhavingsbevoegdheden van de Europese Commissie over GPAI-modellen worden actief op 2 augustus 2026 — organisaties hebben nog vier maanden.
- **Prompt injection blijft structureel risico**: OpenAI erkende dat prompt injection in agentische systemen mogelijk nooit volledig te mitigeren is — een serieuze kanttekening bij elke agent-deployment.

## 🧠 Technologie & Modellen

**OpenAI Codex** kreeg afgelopen week een ingrijpende upgrade. Het kan nu als desktop-agent opereren: apps openen, cursor bedienen en via een ingebouwde browser taken uitvoeren op webapplicaties. Dit maakt Codex niet meer alleen een coding assistant, maar een volwaardige computer-use agent. Relevant, maar ook een stap waarbij de vraag naar veilige sandboxing en gebruikerscontrole urgent wordt.

**Anthropic Mythos** (preview, 7 april) is een krachtig nieuw model dat bewust beperkt vrijgegeven wordt aan 40 geselecteerde partners voor cybersecuritytoepassingen. Deelnemers zijn o.a. Amazon, Apple, Cisco, CrowdStrike en Microsoft. Anthropic claimt dat Mythos bestaande modellen ruimschoots overtreft op coding, reasoning en security-taken. De gesloten preview-aanpak is opmerkelijk — het suggereert dat Anthropic bewust snelheid opoffert voor controle en reputatie.

**OpenAI Agents SDK** (15 april) werd bijgewerkt om enterprise-teams in staat te stellen veiligere en capabelere agents te bouwen — timing die past bij de toenemende enterprise-vraag naar betrouwbare orchestratie.

**Microsoft** lanceerde drie eigen AI-modellen (MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2) via Microsoft Foundry, met een prijsstelling die concurrenten actief wil onderbieden. Dit is een signaal dat Microsoft zijn afhankelijkheid van OpenAI-modellen strategisch wil verminderen.

## 🏛️ Governance & Ethiek

De EU AI Act bevindt zich in april 2026 in een kritieke transitiefase. De meeste verplichtingen voor GPAI-modellen zijn al van kracht (augustus 2025), maar de handhavingsbevoegdheden van de Europese Commissie worden pas actief op **2 augustus 2026**. Lidstaten zijn verplicht vóór die datum nationale AI-sandboxes te hebben opgezet.

In Nederland speelt een actueel vraagstuk rond AI in defensie: het Ministerie van Defensie evalueert het Maven Smart System (MSS), een AI-systeem voor militaire besluitvorming. Experts wijzen op de noodzaak van menselijke controle bij potentieel letale beslissingen — een ethisch vraagstuk dat ook de bredere AI-governance raakt.

## 🔐 Security & Risk

Prompt injection is het thema van de maand. OpenAI stelt expliciet dat agentische AI-browsers mogelijk *altijd* kwetsbaar blijven voor prompt injection-aanvallen. Bruce Schneier publiceerde in april 2026 over "Cybersecurity in the Age of Instant Software" — AI verlaagt de drempel voor aanvallers die kwetsbaarheden zoeken én voor defenders die code snel kunnen patchen.

Het **promptware**-framework dat eerder dit jaar door Schneier werd geïntroduceerd, beschrijft een 7-staps kill chain voor aanvallen op LLM-gebaseerde systemen. Anthropic publiceerde als eerste vendor meetbare prompt injection failure rates — nuttig voor enterprise securityteams die vendors willen vergelijken.

Praktische implicatie: elke agent-deployment moet als potentieel aanvalsvlak worden behandeld. Sandboxing, minimale rechten en human-in-the-loop voor kritieke acties zijn geen luxe maar noodzaak.

## 📈 Markt & Adoptie

De enterprise AI-markt polariseert: **Microsoft** domineert in brede enterprise-adoptie dankzij zijn ecosysteem, terwijl **Google** sterker staat in agentische AI-stacks. De stap van Microsoft om in te stappen op Google's Agent2Agent-protocol is pragmatisch — het maakt multi-vendor agent-workflows mogelijk en verlaagt lock-in-druk voor enterprise-klanten.

**Salesforce Agentforce 2dx** is live: autonome agents die proactief achter de schermen enterprise-systemen monitoren en acties uitvoeren zonder menselijke trigger. Dit is de volgende generatie CRM-automatisering.

In België rapporteert 63% van de organisaties dat digitale soevereiniteit "zeer" of "eerder" belangrijk is, terwijl gemiddeld 24% van cloudcapaciteit verspild wordt — een rem op AI-investeringen die ook voor Nederlandse klanten herkenbaar is.

## 💡 Ctac-relevantie

Drie directe aandachtspunten voor deze week:

1. **Agent-interoperabiliteit als propositie**: de A2A-standaard die Microsoft en Google nu adopteren wordt het raamwerk voor multi-agent enterprise-architecturen. Ctac kan hier vroeg waarde leveren door klanten te begeleiden in het ontwerpen van veilige, interoperabele agent-workflows — vóórdat vendors dit als commodity gaan verkopen.

2. **EU AI Act-deadline nadert**: met vier maanden tot volledige handhaving (2 augustus 2026) hebben klanten in gereguleerde sectoren (overheid, finance, zorg) nu dringend behoefte aan een compliance-gap-analyse. Dit is een concrete kans voor de AI-unit.

3. **Security-first bij agent-uitrol**: de erkende kwetsbaarheid van agentische systemen voor prompt injection maakt security-architectuur een vereiste, geen afterthought. Bij elke klant-engagement waarbij agents worden geïntroduceerd, moet Ctac standaard een security-review inbouwen.

## 📚 Bronnen & verder lezen

- [OpenAI Codex desktop-agent update – TechCrunch](https://techcrunch.com/2026/04/16/openai-takes-aim-at-anthropic-with-beefed-up-codex-that-gives-it-more-power-over-your-desktop/)
- [Anthropic Mythos preview (cybersecurity) – TechCrunch](https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/)
- [OpenAI Agents SDK update – TechCrunch](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/)
- [Microsoft lanceert MAI-modellen – VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [Microsoft committeert aan Agent2Agent – CIO Dive](https://www.ciodive.com/news/-Microsoft-AI-agent-standard-Google-a2a-interoperability/747593/)
- [EU AI Act implementatietijdlijn – artificialintelligenceact.eu](https://artificialintelligenceact.eu/implementation-timeline/)
- [EU AI Act governance & handhaving – EC](https://digital-strategy.ec.europa.eu/en/policies/ai-act-governance-and-enforcement)
- [Prompt injection blijft risico – VentureBeat](https://venturebeat.com/security/openai-admits-that-prompt-injection-is-here-to-stay)
- [Cybersecurity in het tijdperk van instant software – Schneier](https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html)
- [Salesforce Agentforce 2dx – VentureBeat](https://venturebeat.com/ai/salesforce-launches-agentforce-2dx-pushing-autonomous-ai-deep-into-enterprise-workflows)
- [Microsoft vs. Google in enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [AI in defensie NL – NOS](https://nos.nl/nieuwsuur/artikel/2609142-zorgen-over-gebruik-van-ai-in-oorlogen-menselijke-afweging-blijft-nodig)
- [Cyberbeleid en AI-security NL – Computable](https://www.computable.nl/2026/04/17/cyberbeleid-gaat-veel-verder-dan-techniek/)
- [Cloudverspilling en Europese AI-ambities – Computable](https://www.computable.nl/persberichten/waarom-miljoenen-aan-cloudverspilling-europese-ai-ambities-vertragen/)
