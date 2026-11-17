---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-11
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 11 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act actief gehandhaafd:** Sinds 2 augustus 2026 handhaaft de AI Office daadwerkelijk — boetes, documentatieverplichtingen en verplichte AI-labels voor chatbots en deepfakes zijn nu juridisch afdwingbaar in heel Europa. Voor Ctac-klanten begint de urgentie nu pas echt te tellen.
- **OpenAI lanceert GPT-5.6-Cyber:** OpenAI heeft zijn Daybreak-programma uitgebreid met een gespecialiseerd cybersecurity-model en twee toegangsniveaus (Blue/Red) voor goedgekeurde verdedigers. Een defensief offensief in een wereld waar AI-aanvallen escaleren.
- **30 miljoen Copilot-seats bij Microsoft:** Microsoft 365 Copilot heeft de grens van 30 miljoen betaalde seats gepasseerd — een verdubbeling in twee kwartalen. De enterprise AI-markt consolideert zich snel rond Microsoft en Google.
- **85% van organisaties faalt bij AI-implementatie:** Onderzoek van Bain & Company toont dat een overweldigende meerderheid van bedrijven AI niet weet te vertalen naar blijvende bedrijfstransformatie. 80% van de CEO's is ontevreden. Dit is geen technisch probleem — het is een implementatieprobleem.
- **Prompt injection treft AI coding agents:** Een gecoördineerde prompt injection-aanval raakte Claude Code, Gemini CLI én GitHub Copilot tegelijk. Credentials werden gelekt via IAM-kwetsbaarheden, niet via de modellen zelf.

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 update (6 augustus):** Sol is verbeterd op feitelijke betrouwbaarheid en focus; Plus/Pro-gebruikers krijgen een slider waarmee ze de "denktijd" van het model kunnen instellen. Free-gebruikers krijgen standaard Luna (GPT-5.6 variant) met een Think-knop voor complexere vragen. Dit is een interessante UX-aanpak: reasoning als instelbare parameter in plaats van verborgen capability.

**Inkling (Thinking Machines):** Nieuw open model met ~1 biljoen parameters en 1M context window, getraind op 45 biljoen tokens inclusief beeld, audio en video. Het is vooralsnog het grootste open multimodale model beschikbaar. Geen grote naam erachter — bewijslast rust op benchmarks.

**DeepSeek-V4-Pro en Chinese open-weight modellen:** Chinese modellen zijn goed voor 41% van alle downloads op Hugging Face — meer dan Amerikaanse modellen. DeepSeek-V4-Pro-Max presteert toonaangevend op codering en reasoning benchmarks. De grens tussen open en closed-source vervaagt snel aan de top.

Bron: [OpenAI](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/) | [TechCrunch](https://techcrunch.com/2026/07/14/the-real-ai-race-may-no-longer-be-at-the-frontier-open-models-hugging-face/) | [Hugging Face](https://huggingface.co/blog/thinkingmachines-inkling)

## 🏛️ Governance & Ethiek

**EU AI Act — handhaving gestart op 2 augustus:** De Europese Commissie en nationale toezichthouders hebben formeel handhavingsbevoegdheden gekregen. Vanaf nu gelden verplicht:
- Chatbots en interactieve AI moeten zich als AI identificeren bij gebruikers
- Deepfakes (beeld, video, audio) moeten zichtbaar worden gelabeld
- GPAI-aanbieders (o.a. OpenAI, Google) moeten technische documentatie aanleveren op verzoek van de AI Office

Computable.nl meldde dat veel Nederlandse bedrijven deze verplichtingen nog onvoldoende kennen. De ACM en Rijksoverheid zijn aangewezen als nationale toezichthouders. Er loopt ook een aanbesteding van de Commissie voor meer EU-evaluatiecapaciteit van AI-modellen.

Bron: [European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [Computable.nl](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)

## 🔐 Security & Risk

**OpenAI Daybreak uitgebreid — GPT-5.6-Cyber gelanceerd (10 augustus):** OpenAI splitst Daybreak in twee lagen: *Blue* (GPT-5.6 Sol voor dagelijks defensiewerk) en *Red* (GPT-5.6-Cyber voor zero-day onderzoek, exploit-validatie en security testing, achter strikte vetting). Vanaf 1 september zijn hardware security keys verplicht voor alle Daybreak-accounts. Dit is de eerste keer dat OpenAI expliciet een model positioneert voor offensief onderzoek door verdedigers.

**Prompt injection treft drie platforms tegelijk:** VentureBeat rapporteerde dat aanvallers via prompt injection credentials exfiltreerden uit Claude Code (token budget bypass), Gemini CLI (Cloud Storage-scope leak) en GitHub Copilot. Het aanvalsoppervlak ligt bij IAM-configuraties — modellen zijn niet direct gecompromitteerd, maar de runtime-omgeving wel. CISOs moeten agentic AI-stacks nu als afzonderlijk aanvalsoppervlak behandelen.

**AI-cyberaanvallen stijgen ook in Benelux:** Check Point rapporteert 14% meer aanvallen in België in 2025 ten opzichte van een jaar eerder, waarbij gen-AI een steeds prominentere rol speelt in meerdere fasen van aanvallen (reconnaissance, phishing, exploit generation).

Bron: [TechCrunch](https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/) | [OpenAI](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/) | [VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) | [Data News](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)

## 📈 Markt & Adoptie

**Microsoft Copilot: 30 miljoen betaalde seats.** In één kwartaal groeide het van 20M naar 30M — dit is indrukwekkend maar vraagt nuance: hoeveel van deze seats worden actief gebruikt? CIO Dive meldde eerder dat enterprise-adoptie significant achterblijft op licentievolume. Microsoft lanceerde ook de *Frontier Company* met $2,5 miljard om enterprise-implementaties actief te begeleiden — een teken dat het bedrijf inziet dat verkopen niet gelijk staat aan verankeren.

**85% van organisaties faalt bij AI-transformatie:** Bain & Company stelt dat de meeste bedrijven AI niet weten te laten doorwerken in structurele transformatie. Twee derde zit vast in pilots. 80% van CEO's is ontevreden. Dit is marktbevestiging voor wat veel adviseurs al zagen: de bottleneck is implementatieaanpak, not technology.

**Infrastructuurinvesteringen op recordniveau:** Amazon investeert $200 miljard in 2026 ($131B in 2025), Google tussen $175B en $185B. De cloud-infrastructuur wordt razendsnel uitgebouwd — wat op termijn doorwerkt in lagere inference-kosten en grotere beschikbaarheid voor enterprise klanten.

Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/) | [Computable.nl](https://www.computable.nl/2026/08/07/kort-bedrijven-blijven-hangen-in-ai-pilots-veel-ontslagen-in-tech-sector-en-meer/) | [TechCrunch](https://techcrunch.com/2026/02/05/amazon-and-google-are-winning-the-ai-capex-race-but-whats-the-prize/)

## 💡 Ctac-relevantie

**EU AI Act als directe aanleiding voor klantgesprekken.** Nu de handhaving gestart is, veranderen vragen als "moeten wij iets met de AI Act?" in "voldoen wij al?". Klanten in overheid, zorg en finance — typische Ctac-sectoren — zijn verplicht transparant te zijn over AI-gebruik. Dit is een concrete ingang voor Ctac om AI-governance diensten te positioneren: van compliance assessment tot implementatie van labellingsvereisten en gebruikerscommunicatie.

**Implementatiekloof als Ctac-kans.** De 85%-mislukkingnorm van Bain is niet alarmerend — het is een businesscase. Als twee derde van de markt vastloopt in AI-pilots, is de vraag niet of bedrijven hulp nodig hebben, maar van wie ze die willen. Ctac kan zich hier onderscheiden met een aanpak gericht op verankering in processen, niet op demo's.

**AI coding agent security als nieuw aandachtsgebied.** Teams die intern Claude Code, Copilot of vergelijkbare tools inzetten — inclusief Ctac's eigen developers — moeten hun IAM-configuraties en credential-scoping herzien. De prompt injection-aanvallen van deze week zijn een concrete reminder: agentic AI introduceert aanvalsoppervlakken die buiten het klassieke security-model vallen.

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI lanceert nieuw cybermodel](https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/)
- [OpenAI – Daybreak uitbreiding](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/)
- [OpenAI – GPT-5.6 Sol update](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)
- [European Commission – AI Act handhaving 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [Computable.nl – AI Act transparantie-eisen](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [Computable.nl – Bedrijven hangen in AI pilots](https://www.computable.nl/2026/08/07/kort-bedrijven-blijven-hangen-in-ai-pilots-veel-ontslagen-in-tech-sector-en-meer/)
- [CIO Dive – Microsoft Copilot groei Q3 2026](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)
- [VentureBeat – AI agent runtime security](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [VentureBeat – 11 runtime attacks op AI security](https://venturebeat.com/security/ciso-inference-security-platforms-11-runtime-attacks-2026)
- [Data News – Meer cyberaanvallen door AI in Benelux](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-nl/)
- [Hugging Face – Inkling model](https://huggingface.co/blog/thinkingmachines-inkling)
- [TechCrunch – Open models race](https://techcrunch.com/2026/07/14/the-real-ai-race-may-no-longer-be-at-the-frontier-open-models-hugging-face/)
