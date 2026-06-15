---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-14
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 14 juni 2026

## 🔑 Highlights van de dag

- **Claude Fable 5 gelanceerd (9 juni):** Anthropic bracht het eerste publiek beschikbare Mythos-model uit. Het scoort het hoogst op FrontierBench en kan als agent meerdere dagen autonoom doorwerken. Prijsstelling is verdubbeld t.o.v. Opus 4.8: $10/$50 per miljoen tokens.
- **OpenAI Lockdown Mode live (6 juni):** Een opt-in beveiligingsmaatregel die prompt injection-aanvallen moet tegengaan bij gevoelige data — maar OpenAI erkent zelf dat het probleem nooit volledig opgelost zal worden.
- **Microsoft Build 2026:** Microsoft lanceerde MAI-Thinking-1, het eerste eigen reasoning-model (35B actieve parameters), en Microsoft IQ als enterprise-kennislaag bovenop Copilot, Foundry en Copilot Studio.
- **EU AI Act: nog 49 dagen:** Volledige toepasselijkheid op 2 augustus 2026. De Europese AI Office werkt aan richtlijnen voor hoog-risico classificatie en transparantievereisten.
- **Nederland & België koplopers:** 61% (NL) en 62% (BE) van de bedrijven gebruikt inmiddels AI — stijging van ~12 procentpunt in één jaar. Talent blijft de knelpost.

---

## 🧠 Technologie & Modellen

**Claude Fable 5 / Mythos 5 (Anthropic, 9 juni)**
Anthropic bracht Fable 5 uit als eerste publieke variant van het Mythos-model. Het model excelleert in software-engineering, kenniswerk en vision, en is het hoogst scorende model op Cognition's FrontierBench. Bijzonder: het model kan als agent meerdere dagen autonoom werken, plant over fases heen, delegeert aan sub-agents en controleert zijn eigen uitvoer. In risicogevoelige domeinen (cybersecurity, biologie, chemie) valt het terug op Opus 4.8. Prijs: $10/$50 per miljoen tokens — dubbel dat van Opus 4.8. Tot 22 juni nog gratis voor Pro/Max/Team/Enterprise-klanten.
- Bron: [TechCrunch](https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/) · [Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)

**Microsoft MAI-Thinking-1 & Microsoft IQ (Build 2026, begin juni)**
Microsoft lanceerde MAI-Thinking-1: een eigen reasoning-model van nul af opgebouwd (geen distillatie), 35B actieve parameters en 256K context. Daarnaast is Microsoft IQ beschikbaar — een contextlaag die enterprise-kennis en wereldkennis samenvoegt voor gebruik in Copilot, Foundry en Copilot Studio. Work IQ API's worden op 16 juni GA. Dit is een serieuze stap richting eigen modelonafhankelijkheid voor Microsoft.
- Bron: [Microsoft Blog](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/) · [VentureBeat](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)

**Anthropic: agent-autonomie verdubbeld**
Uit Anthropic's eigen onderzoek blijkt dat de p99.9 sessieduur van Claude-agents tussen oktober 2025 en januari 2026 bijna verdubbeld is: van <25 minuten naar >45 minuten. Dit illustreert hoe snel de praktische inzetbaarheid van agentic systemen toeneemt.
- Bron: [Anthropic Research](https://www.anthropic.com/research/measuring-agent-autonomy)

---

## 🏛️ Governance & Ethiek

**EU AI Act: T-minus 49 dagen**
Per 2 augustus 2026 is de EU AI Act volledig van toepassing (m.u.v. hoog-risico AI in gereguleerde producten, die tot 2028 uitstel hebben). De Europese AI Office is bezig met richtlijnen voor hoog-risico classificatie, transparantievereisten en incident-reporting. Voor veel enterprise-klanten in NL/BE geldt: de implementatieklok tikt. De AI Office centraliseert ook het toezicht op general-purpose AI-modellen, wat de handhaving eenduidiger moet maken.
- Bron: [EU AI Act Tracker](https://artificialintelligenceact.eu/implementation-timeline/) · [EC Digital Strategy](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)

**Nederland: kabinet blokkeert AI-overnames door niet-bevriende landen**
Het kabinet krijgt binnenkort de bevoegdheid om overnames van Nederlandse AI-bedrijven door niet-bevriende landen (zoals China) te verbieden. Per 1 januari aanstaande kan dit al worden toegepast. Dit past in een bredere trend van technologische soevereiniteit in Europa.
- Bron: [Computable](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/)

**Vlam: soeverein AI-platform voor de rijksoverheid**
De Nederlandse overheids-chattool Vlam wordt uitgebreid tot een rijksbreed AI-platform en soeverein alternatief voor commerciële generatieve AI-diensten. Brede productie-uitrol verwacht in H2 2026. Rijksambtenaren adopteren AI in hoog tempo.
- Bron: [Computable](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/)

---

## 🔐 Security & Risk

**OpenAI Lockdown Mode (6 juni)**
OpenAI introduceerde Lockdown Mode voor ChatGPT — een opt-in instelling die live webaccess, Agent Mode, connectors en bestandsdownloads uitschakelt om prompt injection-aanvallen te beperken. Het is uitgerold naar persoonlijke en Business-accounts. Kanttekening: OpenAI erkent expliciet dat Lockdown Mode geen volledige bescherming biedt; aanvallen via cached webcontent of geüploade bestanden blijven mogelijk. De bredere boodschap: prompt injection is "the XSS of the AI era" en zal nooit volledig worden opgelost.
- Bron: [TechCrunch](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/) · [OpenAI](https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/)

**Cyberaanvallen met AI nemen toe in België**
In 2025 nam het aantal cyberaanvallen in België met 14% toe, waarbij AI een significante rol speelt. Dit sluit aan bij het bredere beeld dat AI-gestuurde aanvallen sneller schalen en personaliseerbaarder worden.
- Bron: [DataNews](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)

---

## 📈 Markt & Adoptie

**Microsoft & Google domineren enterprise AI**
Microsoft en Google bezetten de leidende posities in de enterprise AI-markt. Microsoft versterkt dit met de lancering van eigen modellen en IQ-lagen; Google met het Agentic Data Cloud-platform dat legacy datapijplijnen omzet in reasoning-engines. Beide bedrijven integreren hun oplossingen diep in bestaande enterprise-toolstacks — waardoor switching costs snel oplopen voor klanten die nu instappen.
- Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) · [Google Cloud](https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up)

**AI-adoptie in NL & BE schiet omhoog**
Nederland: 61% van de bedrijven gebruikt AI (was 49% in 2025). België: 62% (was 52%). De Benelux is daarmee Europees koploper. Grootste rem: tekort aan digitaal talent. Dit zal de druk op externe AI-partners en consultants verder verhogen.
- Bron: [Computable](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)

---

## 💡 Ctac-relevantie

**Agentic AI als nieuwe propositie:** Fable 5's vermogen om meerdere dagen autonoom te werken als multi-agent systeem is geen hype meer — het is productieklaar. Voor Ctac is dit het moment om concrete use cases te definiëren waarbij langlopende agentic workflows klantwaarde leveren: denk aan geautomatiseerde code-review pipelines, documentgeneratie of complexe data-extractie. De AI-engineer in het team kan hier direct mee experimenteren; Emiel kan dit richting klanten positioneren als onderscheidend aanbod.

**EU AI Act compliance = acute kans:** Met twee maanden tot volledige toepasselijkheid zijn veel klanten in NL/BE nog niet klaar. Ctac kan hier een gerichte compliance-quickscan of readiness-assessment aanbieden — zeker richting overheid, zorg en finance, waar hoog-risico classificaties het meest pregnant zijn. De vluchtigheid van dit raam sluit snel.

**Vlam-platform overheid:** De uitbreiding van Vlam naar een rijksbreed AI-platform biedt kansen voor Ctac richting overheidsklanten — zowel in integratie- als in migratie-trajecten voor ministeries die van commerciële diensten af willen. Dit verdient actieve prospectie.

**Talent schaars, vraag hoog:** De adoptiecijfers bevestigen dat de vraag naar AI-expertise in NL/BE flink uitloopt op het aanbod. Ctac's AI-unit kan zich positioneren als preferred partner voor organisaties die intern capaciteit missen. Prioriteer zichtbaarheid (events, publicaties) om die positie te verzilveren.

---

## 📚 Bronnen & verder lezen

- [Anthropic – Claude Fable 5 & Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [TechCrunch – Claude Fable 5 lancering](https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/)
- [VentureBeat – Fable 5 voor enterprise](https://venturebeat.com/technology/anthropic-brings-mythos-to-the-masses-with-claude-fable-5-its-most-powerful-generally-available-model-ever)
- [OpenAI – Lockdown Mode introductie](https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/)
- [TechCrunch – OpenAI Lockdown Mode](https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/)
- [Microsoft Blog – Build 2026](https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/)
- [VentureBeat – Microsoft eigen AI-modellen](https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google)
- [EU AI Act – Implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – AI Act richtlijnen](https://digital-strategy.ec.europa.eu/en/news/supporting-implementation-ai-act-clear-guidelines)
- [Computable – NL kabinet blokkeert AI-overnames](https://www.computable.nl/2026/06/09/kabinet-kan-spoedig-ai-overnames-uit-niet-bevriende-landen-blokkeren/)
- [Computable – Vlam rijksbreed platform](https://www.computable.nl/2026/06/10/vlam-in-de-ai-pan-bij-rijksambtenaren/)
- [Computable – Benelux koploper AI-adoptie](https://www.computable.nl/2026/05/29/benelux-koploper-in-ai-maar-tekort-aan-digitaal-talent-speelt-parten/)
- [DataNews – Cyberaanvallen met AI in België](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
- [Anthropic Research – Agent autonomy](https://www.anthropic.com/research/measuring-agent-autonomy)
- [CIO Dive – Microsoft & Google enterprise dominantie](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Airia – AI Security in 2026](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
