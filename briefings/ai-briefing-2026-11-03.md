---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-03
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 3 november 2026

## 🔑 Highlights van de dag

- **Google rolt Gemini 4 Argon breed uit** en houdt Gemini 4 Carbon voorlopig achter voor defensie en cybersecurity-partners — dit is de eerste keer dat Google een flagship model gefaseerd vrijgeeft op basis van veiligheidsoverwegingen.
- **Microsoft-OpenAI exclusiviteitsafspraak ontmanteld:** OpenAI mag nu op AWS en Google Cloud draaien. Agent 365 is live voor enterprise-klanten en kan ook agents op concurrerende clouds registreren — de hyperscaler-lock-in wordt minder hard.
- **AI vindt softwarebugs op industriële schaal:** Schneier meldt dat een groot deel van de kritieke CVE's van de afgelopen maand door AI werd ontdekt, met een projectie van ~100.000 extra kwetsbaarheden dit jaar. Geen hyperbool: LiteLLM is al gecompromitteerd via een supply chain-aanval gericht op cloud credentials.
- **Nederlands kabinet zet in op AI-bezuinigingen:** 25.000 rijksambtenaren minder via digitalisering en AI — een politiek ambitieus plan dat historisch vaker méér ICT-inhuur opleverde dan besparingen.
- **EU AI Act handhaving loopt:** de AI Office kan sinds augustus documentatie opvragen en boetes opleggen. December 2026 brengt nieuwe verboden rondom NCII-generatie.

## 🧠 Technologie & Modellen

**Google Gemini 4:** Gemini 4 Argon is breed beschikbaar via Google AI Studio en de Gemini API. Gemini 4 Carbon — de zwaarste variant, gericht op geavanceerde cyber-defensie — is vooralsnog beperkt tot overheidsdoeleinden en geselecteerde veiligheidspartners. Naast Gemini previewed Google ook Genie 4 (interactieve wereld-simulatie) en EmbeddingGemma 2 (offline multimodale search op edge-devices). Bron: [Google AI blog, oktober 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/)

**Anthropic Claude Haiku 5.5:** Uitgebracht in oktober als het snelste en zuinigste model in de Claude 5.5-lijn. Sonnet 5.5 en Opus 5.5 kwamen in september; de kleine modellen zijn nu bijgewerkt tot hetzelfde niveau. Bron: [Anthropic system cards](https://www.anthropic.com/system-cards)

**OpenAI GPT-6.1 Sol:** Op DevDay 2026 werd GPT-6.1 Sol aangekondigd als directe opvolger van GPT-6 Sol, met GPT-6.1 Sol Ultrafast in de pijplijn. De promotieprijs voor GPT-5.6 Sol loopt door tot 21 november. Bron: [OpenAI DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/)

**DeepSeek Super Agent:** DeepSeek lanceerde een AI-superagent gericht op coding en multi-agent-coördinatie — een directe uitdager voor OpenAI's Codex-ecosysteem, maar details over onderliggende architectuur ontbreken nog.

**Apple Intelligence × Alibaba Qwen:** Apple test Apple Intelligence in China met Qwen als lokaal model. Dit bevestigt dat geopolitieke fragmentatie ook het foundation-model-landschap bereikt.

## 🏛️ Governance & Ethiek

**EU AI Act – handhaving actief:** Sinds 2 augustus 2026 is de AI Office bevoegd om technische documentatie op te vragen, modellen te evalueren en fines op te leggen. Transparantie-eisen gelden: chatbots moeten zich als AI identificeren, deepfakes moeten worden gelabeld. OpenAI introduceert onzichtbare watermarks voor tekst in de EU; Anthropic, Google en Meta hebben soortgelijke toezeggingen gedaan. Bron: [Europese Commissie](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)

**Omnibus-uitstel:** De high-risk AI-regels (biometrie, arbeidsmarkt) zijn verschoven naar december 2027, inbedding in producten naar augustus 2028. Reden: de geharmoniseerde standaarden kwamen te laat. Praktische consequentie: organisaties hebben meer tijd, maar mogen niet afwachten. Bron: [AI Act tracker](https://artificialintelligenceact.eu/)

**December 2026:** Nieuw verbod op AI-systemen die non-consensuele intieme content of CSAM genereren (onderdeel van de AI Omnibus). Controleer of aanbieders van beeldgeneratie compliant zijn.

**Nederlandse overheid:** Het kabinet zet AI in als bezuinigingsinstrument: 25.000 fte minder, 3,5 miljard euro per jaar besparen. Historisch is dit patroon kwetsbaar — eerdere digitaliseringsprojecten leidden tot meer inhuur en taken. De 'Vlam'-chat (soevereine AI voor rijksambtenaren) wacht op de brede productie-uitrol na compliance-trajecten. Bron: [Computable, oktober 2026](https://www.computable.nl/2026/10/26/kabinet-rekent-op-ai-voor-forse-bezuiniging-op-personeel/)

## 🔐 Security & Risk

**AI-gedreven bug discovery op schaal:** Bruce Schneier rapporteert dat AI-tools een aanzienlijk deel van de recente kritieke CVE's hebben opgespoord. Projectie: ~100.000 nieuwe kwetsbaarheden in 2026. Dit is een structurele verschuiving: aanvallers en verdedigers gebruiken dezelfde tools. Bron: [Schneier on Security, 2 november 2026](https://www.schneier.com/blog/archives/2026/11/ai-vulnerability-finding-2.html)

**LiteLLM supply chain-aanval:** Malicieuze code in de populaire open-source LLM-proxy LiteLLM heeft cloud- en AI-servicecredentials buitgemaakt. Dit is een alarmerend patroon: AI-tooling zelf wordt aanvalsvector. Controleer afhankelijkheden in de AI-stack op supply chain-risico's. Bron: [TechCrunch, oktober 2026](https://techcrunch.com/2026/10/21/the-internet-is-having-a-very-bad-cybersecurity-day/)

**Agent prompt injection – "lethal trifecta":** Airia beschrijft het patroon: een agent met toegang tot privédata + blootstelling aan onbetrouwbare content + mogelijkheid tot datasturen naar buiten = structurele kwetsbaarheid. Relevant voor elk klantproject met AI-agents. Bron: [Airia blog](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)

**LLM-jacking bij Northflank:** Gerapporteerde inbreuk waarbij aanvallers LLM-API-toegang kaapten voor eigen gebruik — een nieuw type credential-misbruik dat specifiek AI-infrastructuur treft.

## 📈 Markt & Adoptie

**Microsoft:** AI-omzet bereikt een annualized run rate van $37 miljard. Agent 365 (governance voor AI-agents, ook cross-cloud) is uit preview. Capex 2026: $190 miljard. Bron: [VentureBeat](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat), [CIO Dive](https://www.ciodive.com/news/Microsoft-Google-booming-AI/873258/)

**Google Cloud:** Voor het eerst is enterprise AI de primaire groeimoteur. Omzet boven de $20 miljard per kwartaal. Maar negatieve vrije kasstroom van $9,1 miljard bij Alphabet wakkert vragen aan over terugverdientijd van AI-investeringen. Bron: [CIO Dive](https://www.ciodive.com/news/google-cloud-tops-20b-on-ai-boom/819018/), [TechCrunch](https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/)

**AWS:** Capex naar $220 miljard opgehoogd. Marktkandeel 28% (Synergy Research). Bron: [CIO Dive](https://www.ciodive.com/news/AWS-ai-investments-cloud/826883/)

**OpenAI × Multi-cloud:** Microsoft en OpenAI hebben hun exclusiviteitsafspraak opgeheven. OpenAI-producten draaien nu ook op AWS Bedrock en Google Cloud. Dit vergroot bereik maar vermindert Microsofts differentiatie. Bron: [VentureBeat](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)

**Antropic IPO:** Anthropic's IPO-filing reserveert aandelen voor Japanse investeerders — een signaal dat het bedrijf geopolitieke diversificatie zoekt vóór beursgang.

**Kanttekening:** TechCrunch signaleert dat de AI-spending-boom de eerste scheurtjes vertoont. Investeringen zijn geconcentreerd bij een klein aantal hyperscalers en grote enterprise-kopers; brede adoptie loopt achter.

## 💡 Ctac-relevantie

**Agent 365 en multi-cloud zijn nu actueel voor klantgesprekken.** Ctac kan klanten helpen bij het inrichten van AI-agent-governance nu Agent 365 productie-ready is en ook non-Microsoft agents ondersteunt. Dit is een directe opening voor zowel Microsoft- als AWS-trajecten.

**Supply chain security voor AI-tooling** is een blinde vlek bij veel organisaties. Als Ctac AI-oplossingen implementeert met open-source componenten (LiteLLM, LangChain, etc.), is een dependency-audit nu urgent — niet optioneel.

**De rijksoverheid als doelmarkt:** Het kabinet wil AI inzetten voor grote bezuinigingen. Ctac heeft publieke sector-ervaring en kan positioneren op implementatiebegeleiding, change management en risicobeheersing — precies de onderdelen die historisch mislopen bij overheidsdigi.

**EU AI Act compliance-diensten:** Met de AI Office actief en December 2026 als volgende deadline, is er vraag naar lichte compliance-scans en documentatieondersteuning. Dit past in een propositie die Ctac snel kan opbouwen.

## 📚 Bronnen & verder lezen

- [Google AI updates oktober 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/)
- [Anthropic system cards (Haiku 5.5)](https://www.anthropic.com/system-cards)
- [OpenAI DevDay 2026 Recap](https://openai.com/index/devday-2026-recap/)
- [EU AI Act – handhaving gestart](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [AI Act tracker (artificialintelligenceact.eu)](https://artificialintelligenceact.eu/)
- [Schneier: AI Vulnerability Finding, 2 nov 2026](https://www.schneier.com/blog/archives/2026/11/ai-vulnerability-finding-2.html)
- [Airia: AI Security in 2026 – Prompt Injection & Lethal Trifecta](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [TechCrunch: Cracks emerging in AI spending boom](https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/)
- [VentureBeat: Microsoft Agent 365 uit preview](https://venturebeat.com/technology/microsoft-takes-agent-365-out-of-preview-as-shadow-ai-becomes-an-enterprise-threat)
- [VentureBeat: Microsoft-OpenAI exclusiviteit voorbij](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud)
- [CIO Dive: Microsoft & Google booming AI revenue](https://www.ciodive.com/news/Microsoft-Google-booming-AI/873258/)
- [Computable: Kabinet bezuinigt via AI](https://www.computable.nl/2026/10/26/kabinet-rekent-op-ai-voor-forse-bezuiniging-op-personeel/)
- [TechCrunch: OpenAI watermarking ChatGPT in EU](https://techcrunch.com/2026/10/05/openai-will-start-watermarking-chatgpts-text-in-the-eu/)
