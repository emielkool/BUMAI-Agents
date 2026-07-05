---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-05
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 5 juli 2026

## 🔑 Highlights van de dag

- **Claude Fable 5 weer wereldwijd beschikbaar** na een turbulente drie weken: op 12 juni geblokkeerd door een Amerikaanse exportcontrolemaatregel (aanleiding: gevonden safeguard-bypass door Amazon-onderzoekers), per 1 juli volledig hersteld voor alle gebruikers en cloud-platforms.
- **Microsoft lanceert Frontier Company** – een aparte AI-engineeringdivisie met een investering van $2,5 miljard en 6.000 industrie-experts die direct bij klanten worden ingezet om AI-transformaties te realiseren. Dit verandert het speelveld voor IT-consultancies.
- **EU AI Act volledig van kracht per 2 augustus 2026** – over vier weken gaat de wet volledig gelden voor de meeste AI-systemen; bedrijven die nog niet compliant zijn lopen risico op boetes.
- **Prompt injection escaleert in enterprise-omgevingen** – agentic AI-systemen worden actief aangevallen via RAG-pipelines, multi-agent architecturen en MCP-servers; 90+ organisaties getroffen in 2025 volgens CrowdStrike.
- **Benelux koploper in Europa**, maar 58% van bedrijven noemt talent shortage als grootste blokkade voor verdere AI-uitrol.

---

## 🧠 Technologie & Modellen

**Claude Fable 5 & Mythos 5 – hersteld na export-controledrama**
Op 9 juni lanceerde Anthropic zijn krachtigste modellen ooit: Fable 5 (publiek) en Mythos 5 (enterprise). Drie dagen later legde de Amerikaanse overheid een exportcontroleplicht op nadat Amazon-onderzoekers een methode vonden om de veiligheidsmaatregelen te omzeilen. Per 30 juni werden de restricties opgeheven; per 1 juli zijn Fable 5 en Mythos 5 weer beschikbaar via Claude.ai, AWS, Google Cloud en Microsoft Foundry. Dit is géén routiniere release – het is het eerste publieke geval waarbij een AI-model tijdelijk door een westerse overheid werd geblokkeerd op veiligheidsgronden.

**Open-source: sterke modellen in opmars**
Op HuggingFace zijn twee modellen relevant: *Kimi K2.6* van Moonshot AI (1,1 biljoen parameters, MIT-licentie, sterk op agentic coding en multi-agent orchestration) en *DeepSeek-V4-Pro*, dat open-source modellen dichterbij het niveau van gesloten topmodellen brengt voor redeneren en agentic taken. Open-weight modellen zijn in 2026 productiewaardig voor serieuze toepassingen.

---

## 🏛️ Governance & Ethiek

**EU AI Act: deadline nadert**
Per 2 augustus 2026 is de EU AI Act volledig van kracht voor het grootste deel van de in-scope AI-systemen (hoog-risico categorieën als biometrie, kritieke infrastructuur en HR vallen pas per december 2027 onder de strengere regels). Belangrijk: alle EU-lidstaten moeten voor 2 augustus een nationaal AI-sandbox hebben ingericht. De Europese Commissie werkt aan praktische richtlijnen voor high-risk classificatie en transparantievereisten – die worden in de loop van 2026 gepubliceerd.

De politieke overeenkomst over het 'AI omnibus'-pakket (aangenomen november 2025) is bereikt op 7 mei 2026 en vergemakkelijkt compliance voor kleinere organisaties. Voor Ctac-klanten is dit het moment om AI governance-vraagstukken definitief te prioriteren.

---

## 🔐 Security & Risk

**AI in de cloud: onzichtbaar voor securityteams**
Computable (3 juli) bericht over onderzoek waaruit blijkt dat AI-agents en MCP-servers razendsnel worden uitgerold, maar dat 81% van de organisaties managed AI-services gebruikt terwijl securityteams geen zicht hebben op wat er in die omgevingen draait. Dit is een structureel probleem: shadow AI op cloud-niveau.

**Prompt injection als productiebedreiging**
Prompt injection blijft #1 op de OWASP Top 10 voor LLM-applicaties. In 2025 zijn meer dan 90 organisaties getroffen via geïnjecteerde prompts in legitieme AI-tools (CrowdStrike 2026 Global Threat Report). In 2026 neemt het aanvalsoppervlak toe door agentic systemen met meer autonomie, tool-toegang en integratie in kritieke workflows. Drie AI coding agents lekten recent geheimen via één enkele prompt injection – en het betreffende system card had het risico al voorspeld.

---

## 📈 Markt & Adoptie

**Microsoft Frontier Company – de consultancy-markt wordt opnieuw gedefinieerd**
Op 2 juli lanceerde Microsoft de *Microsoft Frontier Company*: een zelfstandige divisie die 6.000 AI-engineers direct bij klanten inzet voor co-design en doorlopende verbetering van AI-systemen. Investering: $2,5 miljard. Eerste klanten: London Stock Exchange Group, Unilever, Land O'Lakes. Dit is geen partnership-model maar een direct concurrerende positionering ten opzichte van IT-consultancies.

**Marktcijfers: enterprise AI versnelt maar strandt vaak in pilotfase**
Microsoft heeft meer dan 20 miljoen betaalde M365 Copilot-seats; de AI-omzet loopt op een jaarlijks tempo van $37 miljard (+123% YoY). Google Cloud passeerde voor het eerst $20 miljard per kwartaal, mede gedreven door Gemini Enterprise (+40% QoQ in paid MAU's). Toch rapporteert twee derde van de enterprises dat ze vastzitten in de pilotfase en moeite hebben om AI-initiatieven naar productie te brengen.

**Benelux koploper, maar talent is de bottleneck**
61% van de Nederlandse bedrijven heeft AI ingevoerd (was 49% vorig jaar); de Benelux scoort boven het Europese gemiddelde van 54%. De grootste belemmering voor verdere uitrol: 58% noemt gebrek aan AI- en digitale vaardigheden.

---

## 💡 Ctac-relevantie

Microsoft Frontier Company is het meest directe signaal van deze week: de grootste softwareleverancier trekt de implementatierol naar zich toe met een eigen consulting-arm. Voor Ctac betekent dit dat de differentiatie verschuift van *technische implementatie* naar *diepgaande domeinkennis en maatwerk-AI* die Microsoft niet kan leveren vanuit een generiek engagementmodel. De focus op maatwerk-AI (van experiment naar productie) die ook in de Nederlandse markt zichtbaar is, sluit hier direct op aan.

De naderende deadline van de EU AI Act (2 augustus) is een commercieel moment: klanten die nu nog geen governance-aanpak hebben, hebben urgentie. Ctac kan hier als trusted advisor optreden, mits dat aanbod intern scherp is gepositioneerd.

Op securitygebied is de combinatie van MCP-servers, cloud-gebaseerde AI-agents en onzichtbaarheid voor securityteams een concreet vraagstuk dat bij enterprise-klanten speelt. Dit raakt zowel de AI-unit als bestaande security- en cloudpraktijken.

---

## 📚 Bronnen & verder lezen

- [Anthropic: Redeploying Claude Fable 5](https://www.anthropic.com/news/redeploying-fable-5)
- [VentureBeat: Anthropic brengt Fable 5 terug na opheffing exportcontrole](https://venturebeat.com/technology/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it)
- [TechCrunch: Trump drops restrictions on Anthropic's Mythos and Fable models](https://techcrunch.com/2026/06/30/trump-drops-restrictions-on-anthropics-mythos-and-fable-models/)
- [Microsoft Blog: Frontier Company – AI engineering](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)
- [TechCrunch: Microsoft launches AI deployment company with $2.5B](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [EU AI Act: Shaping Europe's digital future](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [VentureBeat: Prompt injection exploiting enterprise AI](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [Computable: AI in cloudomgevingen versnipperd en onzichtbaar](https://www.computable.nl/2026/07/03/ai-in-cloudomgevingen-versnipperd-en-onzichtbaar-voor-securityteams/)
- [CIO Dive: Microsoft, Google rule AI vendor market for enterprises](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Computable: Benelux koploper in AI, maar tekort aan talent](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [HuggingFace: Kimi K2.6](https://huggingface.co/moonshotai/Kimi-K2.6)
- [HuggingFace: DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- [Airia: AI Security in 2026 – Prompt Injection](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
