---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-05-27
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 27 mei 2026

## 🔑 Highlights van de dag

- **Anthropic op weg naar biljoen-valutatie:** Anthropic sluit een $30 miljard investeringsronde af op een waardering van $900+ miljard — voor het eerst hoger dan OpenAI — terwijl de Q2-omzet 130% steeg naar $10,9 miljard. Dit is geen hype meer; dit is infrastructuurschaal.
- **EU AI Act Omnibus aangenomen:** Op 7 mei bereikten Raad en Parlement akkoord over vereenvoudigde AI-regelgeving, met uitgebreide sandbox-toegang voor MKB en mid-caps. De formele bekrachtiging volgt vóór 2 augustus 2026 — de deadline voor hoog-risico-AI-systemen.
- **Andrej Karpathy naar Anthropic:** De meest invloedrijke AI-educator en voormalig Tesla Autopilot-lead vervoegt Anthropic om het pretraining-onderzoeksteam te herbouwen. Een sterk signaal over wie de volgende model-generatie gaat leiden.
- **Prompt injection: eerste grootschalige aanvallen in het wild gedocumenteerd:** Unit 42 rapporteerde in maart 2026 de eerste grootschalige indirecte prompt-injection-aanvallen op commerciële platforms. CVE-2025-53773 (CVSS 9.6) toont remote code execution via GitHub Copilot aan.
- **Enterprise AI-adoptie verdubbeld:** Organisatiebrede AI-adoptie steeg van 22% in 2025 naar 40% in 2026, gedreven door agentische workflows. De agentic AI-race is nu het hoofdslagveld voor Microsoft, Google en Anthropic.

---

## 🧠 Technologie & Modellen

**Claude Opus 4.7 algemeen beschikbaar**
Anthropic maakte Claude Opus 4.7 generiek beschikbaar, met name versterkt op geavanceerde software-engineering taken. Tegelijkertijd loopt de funding-ronde van $30 miljard op een valutatie die OpenAI's $852 miljard-waardering (maart 2026) overstijgt — wat de geloofwaardigheid van Anthropic als frontier-speler consolideert.
→ [Anthropic: Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)

**Google Gemini 3.5 Flash & Gemma 4**
Google lanceerde Gemini 3.5 Flash (frontier-kwaliteit voor de helft tot een derde van de prijs van vergelijkbare modellen) en de Gemma 4-familie: open-source modellen ontworpen voor redeneren en agentische workflows. Daarnaast introduceerde Google de achtste generatie TPU-chips, specifiek afgestemd op de lage latentie die agent-ecosystemen vereisen.
→ [TechCrunch: Google I/O Gemini updates](https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude-at-io-2026/)

**Agentische infrastructuur in opmars**
Dell lanceerde Dell Deskside Agentic AI (lokaal draaien van agents op workstations met Nvidia NemoClaw). Circle Internet Group introduceerde Circle Agent Stack met wallets en nanopayments voor autonome agents. SAP-consultant Resulting IT rapporteerde 59% kostenbesparing via twee agentische SAP-tools. De "agentic economy" krijgt snel concrete contouren.

---

## 🏛️ Governance & Ethiek

**EU AI Act Omnibus: vereenvoudiging én uitbreiding**
Het politiek akkoord van 7 mei versterkt de AI Office als centrale toezichthouder voor general-purpose AI-modellen, breidt sandbox-toegang uit voor innovators (inclusief EU-niveau), en verlengt MKB-vrijstellingen naar kleine mid-caps. Formele bekrachtiging wordt verwacht vóór 2 augustus 2026 — de datum waarop HRAIS-verplichtingen van kracht worden.
→ [Consilium EU](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)

**Nederland: toezichtwetsvoorstel open voor consultatie**
Het kabinet heeft het wetsvoorstel voor nationaal AI-toezicht opengesteld voor consultatie tot 1 juni 2026. In NL/BE zullen HR, onderwijs, overheid en finance de eersten zijn die de AI Act als operationele realiteit voelen.
→ [Rijksoverheid.nl](https://www.rijksoverheid.nl/actueel/nieuws/2026/04/20/kabinet-zet-stap-met-toezicht-op-europese-ai-regels)

**Vaticaan kiest Anthropic als AI-veiligheidspartner**
Paus Leo XIV presenteerde zijn eerste encycliek *Magnifica Humanitas* samen met Anthropic-medeoprichter Christopher Olah. De bewuste keuze voor Anthropic — niet Google, niet OpenAI — is een reputatiesignaal over veiligheidscredentials in het maatschappelijk debat.

---

## 🔐 Security & Risk

**Prompt injection: van curiositeit naar tier-1 risico**
Prompt injection staat op #1 in OWASP Top 10 voor LLM-applicaties 2026. Circa 40% van agent-protocollen vertoont exploiteerbare kwetsbaarheden. Kritisch: CVE-2025-53773 (CVSS 9.6) demonstreert remote code execution via verborgen prompt injection in GitHub Copilot pull request-beschrijvingen.
→ [Securance: OWASP #1 AI threat](https://www.securance.com/blog/prompt-injection-the-owasp-1-ai-threat-in-2026/)
→ [CrowdStrike: Indirect Prompt Injection](https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/)

**Cisco State of AI Security 2026**
Cisco publiceerde zijn jaarlijkse AI-security rapport met een sterk uitgebreid dreigingslandschap: aanvallen verschuiven van chatbot-misbruik naar multi-agent en toolchain-exploitatie. Defensieve gelaagde aanpak kan aanvalssucces terugbrengen van 73% naar minder dan 9%.
→ [Cisco AI Security 2026 Report](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)

**Anthropic Mythos: te krachtig voor publieke release?**
Anthropic's Mythos-model — beschreven als "ver vooruit" op het gebied van cybersecurity — wekt bezorgdheid bij overheden, banken en energiebedrijven. OpenAI verleende de EU wél toegang tot GPT-5.5-Cyber; Anthropic houdt Mythos nog achter. Een terechte voorzichtigheid of marktstrategie?

---

## 📈 Markt & Adoptie

**Enterprise AI-adoptie: kantelpunt bereikt**
Organisatiebrede AI-adoptie steeg naar 40% (2025: 22%), aangedreven door agentische automatisering. Wereldwijde AI-investeringen overstijgen $650 miljard per jaar. Microsoft en Google domineren de enterprise AI-markt, waarbij Google Cloud 63% YoY-omzetgroei rapporteerde ($20 miljard).
→ [CIO Dive: Microsoft/Google enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
→ [GlobeNewswire: $650B AI investment](https://www.globenewswire.com/news-release/2026/05/05/3288006/0/en/AI-Investment-Activity-to-Surpass-650-Billion-Annually-as-Enterprise-Adoption-Accelerates-Toward-2026.html)

**OpenAI bereidt beursgang voor**
OpenAI werkt aan een vertrouwelijke S-1-aanvraag bij de SEC — de eerste stap richting IPO. Gecombineerd met de Anthropic-ronde op $900 miljard valutatie staat de AI-markt structureel te veranderen qua governance en aandeelhoudersverwachtingen.

**Benelux IT: AI breed aanwezig, AI-driven nog zeldzaam**
Bijna iedere IT-dienstverlener in NL/BE gebruikt AI in enige vorm, maar slechts 19% is volledig "AI-driven". Kans én risico voor Ctac: klanten hebben behoefte aan begeleiding van AI-gebruik naar structurele AI-waardecreatie.
→ [ICTMagazine: Benelux AI-adoptie](https://www.ictmagazine.nl/nieuws/benelux-it-sector-omarmt-ai-grotendeels/)

---

## 💡 Ctac-relevantie

**2 augustus 2026 nadert snel voor klanten in HR, overheid en finance.** De EU AI Act Omnibus biedt vereenvoudiging voor MKB en mid-caps — precies Ctac's klantenbasis. Nu is het moment om compliance-quickscans en GPAI-risicobeoordelingen als concrete dienstverlening te positioneren, vóór de zomerstop.

**Agentische AI is de volgende groeifase.** De SAP-agentic-tools die 59% kostenbesparing leveren, het ServiceNow/Accenture-partnership voor enterprise agent-scaling, en Dells lokale agentic infrastructuur laten zien dat het niet meer gaat over "AI gebruiken" maar over "AI die werk doet." Ctac's custom software-competentie is hier direct inzetbaar — niet als AI-tool leverancier, maar als integrator van agentische workflows in bestaande klantprocessen.

**Security is nu een vereiste in elk AI-voorstel.** Prompt injection op OWASP #1, kritische CVE's in Copilot-workflows en Cisco's dreigingsrapport geven Ctac concrete argumenten om AI-security standaard mee te nemen in elke implementatie — geen optie, maar hygiëne.

---

## 📚 Bronnen & verder lezen

- [Anthropic: Claude Opus 4.7 introductie](https://www.anthropic.com/news/claude-opus-4-7)
- [TechCrunch: Google I/O Gemini updates](https://techcrunch.com/2026/05/19/google-updates-its-gemini-app-to-take-on-chatgpt-and-claude-at-io-2026/)
- [Consilium EU: AI Act Omnibus akkoord](https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/)
- [LegalNodes: EU AI Act 2026 compliance updates](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [Rijksoverheid: toezicht op AI-regels](https://www.rijksoverheid.nl/actueel/nieuws/2026/04/20/kabinet-zet-stap-met-toezicht-op-europese-ai-regels)
- [Securance: OWASP prompt injection #1 threat](https://www.securance.com/blog/prompt-injection-the-owasp-1-ai-threat-in-2026/)
- [CrowdStrike: Indirect Prompt Injection Attacks](https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/)
- [Cisco: State of AI Security 2026](https://blogs.cisco.com/ai/cisco-state-of-ai-security-2026-report)
- [CIO Dive: Microsoft & Google enterprise AI dominantie](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [GlobeNewswire: $650B AI investeringen](https://www.globenewswire.com/news-release/2026/05/05/3288006/0/en/AI-Investment-Activity-to-Surpass-650-Billion-Annually-as-Enterprise-Adoption-Accelerates-Toward-2026.html)
- [ICTMagazine: Benelux IT-sector omarmt AI](https://www.ictmagazine.nl/nieuws/benelux-it-sector-omarmt-ai-grotendeels/)
- [VentureBeat: Claude's agent control plane](https://venturebeat.com/orchestration/claudes-next-enterprise-battle-is-not-models-its-the-agent-control-plane)
- [LLM Stats: AI model releases mei 2026](https://llm-stats.com/ai-news)
