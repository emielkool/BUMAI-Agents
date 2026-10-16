---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-29
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 29 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act enforcement live (4 weken):** Sinds 2 augustus handhaaft de Europese Commissie actief de AI Act en nieuwe transparantie-eisen. AI-systemen die met gebruikers communiceren moeten zich nu identificeren als AI. Voor Ctac-klanten in gereguleerde sectoren is dit geen abstracte deadline meer.
- **GPT-5.6 Sol krijgt Ultrafast mode en prijsverlaging:** OpenAI introduceerde op 13 augustus een Ultrafast-preview van hun vlaggenschipmodel en verlaagde de prijs op 21 augustus. Google volgde met Gemini 3.7 Flash (13 aug); modellen worden sneller én goedkoper, wat enterprise-adoptie verder verlaagt.
- **Prompt injection escaleert naar productie-incidents:** Drie populaire AI-coding agents lekten API-keys en wachtwoorden via één injectie; AWS patchte een kritieke RCE-kwetsbaarheid in Kiro (CVE-2026-10591). De aanvalsvector is operationeel realiteit, niet meer theoretisch.
- **Microsoft Frontier Company: $2,5 miljard voor AI-deployment:** Microsoft lanceert een apart bedrijf met 6.000 experts om enterprise AI-trajecten te begeleiden. Met 20 miljoen Copilot-seats en een AI-omzetrun-rate van $37 miljard (+123% YoY) zet Microsoft de standaard voor wat "enterprise AI" betekent.
- **Nederland tweede AI-exporteur van Europa:** Nederland exporteert ruim €80 miljard aan AI-gerelateerde goederen, alleen Duitsland doet het beter. Tegelijk worstelt de Benelux met een acuut tekort aan digitaal talent (58% van bedrijven noemt dit een blokkade).

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6-familie** is begin juli uitgerold; augustus brengt verfijningen: een Ultrafast-modus voor Sol (13 aug), een prijsverlaging (21 aug) en beschikbaarheid van de Daybreak-modellen op AWS (11 aug). Sol claimt state-of-the-art prestaties op coding, kenniswerk en cybersecurity met minder tokens dan voorgaande versies.

**Anthropic Claude Opus 5** (uitgebracht 24 juli) kreeg op 12 augustus een update met verbeterde inferentiesnelheid en betere wetenschappelijke redeneervaardigheden. Het is nu de standaard voor Claude Max-abonnees. Prijsniveau: circa de helft van Claude Fable 5.

**Google Gemini 3.7 Flash** (13 aug) richt zich op efficiënte agentic workflows. Google introduceerde ook Gemini 3.5 Transcribe als dedicated speech-to-text endpoint.

**Open-source ecosysteem:** Qwen-modellen domineren de open-source wereld met 151.000+ afgeleide modellen op Hugging Face – 2,6× meer dan Meta. DeepSeek V4-Pro en Qwen3.8-Max zijn de meest recente releases in deze categorie. Wie open-source overweegt voor klantprojecten, kan voorbij Llama kijken.

*Bronnen: [OpenAI GPT-5.6](https://openai.com/index/gpt-5-6/) · [TechCrunch GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/) · [HuggingFace State of Open Models](https://huggingface.co/blog/state-of-open-models-summer-2026) · [LLM Stats](https://llm-stats.com/ai-news)*

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhaving gestart op 2 augustus.** De Europese Commissie en nationale autoriteiten zijn nu actief. Het AI Office heeft bevoegdheden om technische documentatie op te vragen bij aanbieders van GPAI-modellen (zoals GPT-5.6 en Gemini), correctieve maatregelen te eisen en boetes op te leggen. De AI Omnibus – vereenvoudigde implementatieregels aangenomen november 2025 – trad 27 juli 2026 in werking.

**Transparantie-eis:** Chatbots en interactieve AI moeten zich direct bekendmaken als AI. NOS berichtte hierover specifiek voor AI-telefonisten: geen grijs gebied meer. Voor klanten van Ctac in klantcontact, zorg en dienstverlening is dit direct actueel.

**Tijdlijn hoogrisico-AI:** Aanvullende regels voor hoog-risico systemen (Annex III) gaan pas in per december 2027 en augustus 2028. Er is dus nog implementatietijd, maar de governance-infrastructuur staat nu.

*Bronnen: [EC: handhaving AI Act gestart](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) · [Computable AI Act transparantie](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/) · [NOS AI-telefonist](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)*

---

## 🔐 Security & Risk

**Prompt injection wordt productieschade.** Drie AI-coding agents lekten API-keys en wachtwoorden door één kwaadaardig geïnjecteerde prompt in een code-repository. VentureBeat meldt dat één vendor het risico al had voorspeld in zijn eigen system card, maar het toch niet voorkwam.

**CVE-2026-10591 (AWS Kiro):** Een simpele opdracht als "vat deze pagina samen" kon leiden tot remote code execution. AWS heeft gepatcht, maar dit illustreert hoe agentic AI-tools (die acties uitvoeren in plaats van alleen tekst genereren) een nieuw aanvalsoppervlak vormen.

**Cryptografische context injection op Grok:** Onderzoekers tonen aan dat versleutelde prompt injection naam, locatie, tier en chatprompts van gebruikers kan exfiltreren naar een externe server.

**OpenAI lanceert cyber-model (10 aug):** Specifiek getraind op cybersecurity-scenario's, defensief en offensief. Het suggereert dat AI-labs de security-dimensie serieus nemen als apart productdomein.

*Bronnen: [VentureBeat AI agent secrets](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026) · [Hacker News: Grok context injection](https://thehackernews.com/2026/08/new-cryptographic-context-injection.html) · [TechCrunch OpenAI cyber model](https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/) · [Airia: AI Security 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)*

---

## 📈 Markt & Adoptie

**Microsoft domineert enterprise AI:** 20 miljoen Copilot-seats, AI-omzetrun-rate $37 miljard (+123% YoY). Microsoft Frontier Company ($2,5 mrd, 6.000 experts) positioneert zich als de partner voor grootschalige AI-uitrol bij enterprises.

**Google Agentic Data Cloud:** Gepresenteerd op Google Cloud Next '26 – een AI-native architectuur die legacy dataplatformen omzet in redenerende engines voor AI-agents. Strategische concurrent voor Microsoft Fabric-positionering.

**OpenAI wint terrein bij zakelijke gebruikers** ten koste van Anthropic, volgens TechCrunch-analyse van 20 augustus. Twee derde van bedrijven zit echter nog vast in pilot-fase; de overgang naar productie blijft de bottleneck.

**Benelux:** AI-adoptie stijgt sterk (NL: 61%, BE: 62%), maar 58% noemt talenttekort als grootste blokkade. Nebius (Amsterdam Zuidas) rapporteert +454% omzetgroei tot €582 miljoen. Nederland is na Duitsland de grootste Europese exporteur van AI-hardware en -componenten (>€80 mrd).

*Bronnen: [Microsoft FY26 terugblik](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/) · [CIO Dive: Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/) · [TechCrunch: OpenAI vs Anthropic business](https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/) · [Computable: NL tweede exporteur](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/)*

---

## 💡 Ctac-relevantie

**EU AI Act compliance is nu werkelijkheid, niet voorbereiding.** Klanten van Ctac die AI-tools inzetten voor klantinteractie (chatbots, virtuele assistenten, geautomatiseerde telefonie) moeten nú voldoen aan de transparantie-eis. Ctac kan hier direct waarde leveren: een compacte compliance-scan voor bestaande AI-toepassingen bij klanten is een concrete propositie die nu op tafel ligt.

**Agentic AI security moet in standaard-projectaanpak.** De prompt-injection-incidenten bij Kiro en coding agents tonen dat agentic systemen een fundamenteel ander risicomodel hebben dan klassieke software. Ctac moet dit meenemen in de delivery-standaarden voor AI-agent-projecten: sandboxing, input-validatie en logging zijn geen optie maar basishygiëne.

**Microsoft Frontier Company als referentiepunt én concurrentiepositie:** Microsoft's expliciete beweging naar deployment-dienstverlening (naast licenties) raakt Ctac's kernmarkt. De kans: Ctac kent de klant beter, spreekt Nederlands, begrijpt de sector. Het risico: Microsoft schroeft de partner-propositie omhoog en verwacht dat partners mee-opschalen of wegtrekken.

**Talenttekort in Benelux = kans voor Ctac AI-unit.** 58% van Benelux-bedrijven ziet digitaal talent als blokkade. De Ctac AI-unit kan zich positioneren als de brug: externe AI-expertise plus begeleiding bij interne capaciteitsopbouw bij klanten.

---

## 📚 Bronnen & verder lezen

- [OpenAI GPT-5.6 aankondiging](https://openai.com/index/gpt-5-6/)
- [TechCrunch: GPT-5.6 lancering](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [HuggingFace: State of Open Models Summer 2026](https://huggingface.co/blog/state-of-open-models-summer-2026)
- [EC: EU AI Act handhaving gestart 2 augustus](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [NOS: AI-telefonist moet zich prijsgeven](https://nos.nl/artikel/2625224-geen-twijfel-ai-telefonist-moet-zich-voortaan-direct-prijsgeven)
- [Computable: Wat je moet weten van de AI Act](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [VentureBeat: AI agents lekken secrets via prompt injection](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [The Hacker News: Cryptografische context injection Grok](https://thehackernews.com/2026/08/new-cryptographic-context-injection.html)
- [TechCrunch: OpenAI lanceert cyber-model](https://techcrunch.com/2026/08/10/as-ai-led-attacks-multiply-openai-launches-a-new-cyber-model/)
- [Airia: AI Security 2026](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [Microsoft FY26 in retrospectief](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [CIO Dive: Google Agentic Data Cloud](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [TechCrunch: OpenAI wint terrein bij zakelijke gebruikers](https://techcrunch.com/2026/08/20/openai-is-gaining-on-anthropic-with-business-users-new-data-indicates/)
- [Computable: Nederland tweede AI-exporteur Europa](https://www.computable.nl/2026/08/19/kort-vercel-zet-miljoen-in-op-eigen-ai-sandbox-nederland-tweede-van-europa-met-export-ai-goederen-en-meer/)
- [Datanews: Meer cyberaanvallen door AI in België](https://datanews.knack.be/nieuws/security/cybercrime/meer-cyberaanvallen-door-ai-ook-in-ons-land/)
- [LLM Stats: AI model updates augustus 2026](https://llm-stats.com/ai-news)
