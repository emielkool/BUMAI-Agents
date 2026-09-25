---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-08-05
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 5 augustus 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaving gestart**: Vanaf 2 augustus 2026 handhaaft de Europese Commissie actief de transparantieverplichtingen (Article 50) — chatbots, deepfakes en AI-gegenereerde content moeten nu verplicht gelabeld zijn. Dit is geen aankondiging meer maar afdwingbare realiteit.
- **OpenAI halveert prijzen**: GPT-5.6 Luna werd op 30 juli 80% goedkoper, Terra 20%. Agentic AI op frontier-niveau is nu draaibaar voor een fractie van de prijs van drie maanden geleden.
- **Microsoft AI-run rate doorbreekt $37 miljard**: 20+ miljoen Copilot-seats, 123% YoY-groei — enterprise AI is geen experiment meer maar bedrijfskritische infrastructuur.
- **Prompt injection treft drie grote coding agents tegelijk**: Claude Code, Gemini CLI én Copilot lekten secrets via één aanval. OWASP noemt prompt injection voor het tweede jaar op rij het grootste LLM-risico.
- **Enterprise agents verdubbeld, controle loopt achter**: Het gemiddeld aantal AI-agents per enterprise steeg in één kwartaal van 26-50 naar 76-100, maar slechts 52% is gemonitord.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 – massale prijsverlaging**
Op 30 juli verlaagde OpenAI de prijs van GPT-5.6 Luna met 80% en GPT-5.6 Terra met 20%. De GPT-5.6 familie (Sol = flagship, Terra = balanced, Luna = cost-efficient) is beschikbaar gesteld. Dit is strategisch: goedkopere inferentie maakt agentic use-cases economisch haalbaar die eerder financieel onhaalbaar waren.
*Bron: [TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)*

**Anthropic Claude voice mode update**
Eind juli breidde Anthropic de voice-modus van Claude uit met ondersteuning voor Opus, Sonnet én Haiku — gebruikers kiezen zelf hun kwaliteit/kostenverhouding. Sonnet 5 (gelanceerd 30 juni, $2/$10 per miljoen tokens) blijft de prijsleider voor agentic workloads.
*Bron: [TechCrunch](https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/)*

**Open-source: Poolside Laguna S 2.1 (NVFP4)**
Een nieuw open-weight model met FP8 KV-cache quantisatie en native reasoning-support. Kimi K2.6 en Qwen3 235B-A22B zijn de sterkste open modellen voor enterprise-gebruik. De Open LLM Leaderboard groeit door als referentiepunt.
*Bron: [Hugging Face](https://huggingface.co/poolside/Laguna-S-2.1-NVFP4)*

---

## 🏛️ Governance & Ethiek

**EU AI Act Article 50 – handhaving actief per 2 augustus**
Vier concrete verplichtingen zijn nu afdwingbaar: (1) chatbots moeten melden dat ze AI zijn, (2) deepfakes moeten worden gelabeld, (3) AI-gegenereerde content moet machine-leesbare markering dragen, (4) het AI Office en nationale autoriteiten mogen boetes opleggen. De deadline voor hoog-risico AI-systemen is verschoven naar december 2027, maar transparantieplicht geldt nú.

Computable.nl signaleert dat veel Nederlandse organisaties de eisen van Article 50 nog niet hebben geïmplementeerd, ondanks dat de wet al twee jaar bekendstaat.
*Bronnen: [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august) | [Computable.nl](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)*

---

## 🔐 Security & Risk

**Prompt injection treft Claude Code, Gemini CLI en Copilot tegelijk**
Een enkele prompt injection-aanval wist secrets te extraheren uit alle drie de dominante coding agents in één actie. Bijzonder: Anthropics eigen system card voor Claude Code had de kwetsbaarheid al beschreven als "not hardened against prompt injection." Dit illustreert een structureel probleem: agent-leveranciers documenteren bekende risico's maar bieden geen garanties.

Schaal van het probleem (onderzoeksdata):
- 94,4% van state-of-the-art LLM-agents is kwetsbaar voor prompt injection
- 100% kwetsbaar voor inter-agent trust exploits
- OWASP noemt prompt injection voor het tweede jaar op rij de #1 LLM-kwetsbaarheid
- De UK NCSC stelt dat de impact mogelijk groter is dan SQL-injection ooit was

*Bron: [VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)*

---

## 📈 Markt & Adoptie

**Microsoft FY26 – AI van experiment naar fundament**
Microsofts jaarverslag over FY26 toont: 20+ miljoen betaalde 365 Copilot-seats, 4x groei in klanten met >50.000 seats, AI-omzet groeit 123% YoY naar $37 miljard run rate. EY rolde Microsoft 365 Copilot uit bij 150.000 medewerkers (15% productiviteitswinst); NHS England bij 500.000 zorgprofessionals.
*Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-copilot-growth-boosts-spending-revenues-soar/819009/) | [Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)*

**Google Gemini Enterprise Agent Platform wint terrein**
Google's geïntegreerde AI-agentplatform groeit snel in productie-deployments. Enterprise-clouduitgaven stegen naar $500 miljard per jaar, grotendeels gedreven door AI-infrastructuur. CIO Dive concludeert: Microsoft en Google domineren de enterprise AI-vendormarkt.
*Bron: [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)*

**Agentische AI verdubbeld, beheersing loopt achter**
Het gemiddeld aantal agents per enterprise sprong van 26-50 naar 76-100 per kwartaal. Tegelijk: 83% van IT-leiders zegt dat hun infrastructuur upgrades nodig heeft voor agentic AI, en slechts 52% van alle productie-agents wordt gemonitord. Helft van de enterprises rapporteerde een klantgerichte storing na intern geslaagde evaluatie.
*Bron: [VentureBeat](https://venturebeat.com/orchestration/enterprise-ai-is-entering-an-evaluation-gap-agents-are-gaining-autonomy-faster-than-companies-can-verify-them) | [CIO Dive](https://www.ciodive.com/news/agentic-ai-strains-legacy-it-systems/825003/)*

---

## 💡 Ctac-relevantie

**Directe compliance-actie vereist**: Article 50 van de EU AI Act is per 2 augustus afdwingbaar. Ctac moet bij lopende klantprojecten checken of AI-systemen (chatbots, content-tools, beslissingsondersteuning) voldoen aan de transparantieplicht. Dit is geen theoretisch risico — boetes zijn nu mogelijk. Maak dit een standaard deliverable in AI-projecten.

**Prijsverlaging opent nieuwe business cases**: De 80% prijsverlaging van GPT-5.6 Luna maakt use-cases haalbaar die drie maanden geleden nog niet rendabel waren (hoge-volume documentverwerking, autonome klantenservice-agents, real-time analyse). Dit is het moment om gestopte of afgewezen PoC-trajecten opnieuw te evalueren met klanten.

**Agent-monitoring is een concrete dienstverlening**: 83% van enterprises zit met een infrastructuur-gap en slechts 52% van hun agents wordt gemonitord. Dit is een herkenbaar pijnpunt dat Ctac kan adresseren als advies- of implementatiepropositie: agent-governance, observability-tooling en risico-assessment voor bestaande agent-deployments.

**Prompt injection = klantrisico dat uitleg behoeft**: De gelijktijdige aanval op Claude Code, Gemini CLI en Copilot is een wake-up call. Bij klanten die coding agents of autonome AI-workflows inzetten, is een beveiligingsscan op prompt injection-kwetsbaarheid nu een legitiem en urgent gespreksonderwerp.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – OpenAI GPT-5.6 lancering](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)
- [TechCrunch – Anthropic Claude voice mode update](https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/)
- [TechCrunch – Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [EC – EU AI Act enforcement starts 2 August](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)
- [Computable.nl – AI Act transparantie-eisen](https://www.computable.nl/2026/08/03/wat-je-moet-weten-van-de-ai-act-en-de-nieuwe-transparantie-eisen/)
- [VentureBeat – Prompt injection treft drie coding agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Microsoft Blog – FY26 terugblik](https://blogs.microsoft.com/blog/2026/07/28/looking-back-on-microsofts-fy26-from-ai-experimentation-to-frontier-transformation/)
- [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [VentureBeat – Enterprise evaluation gap](https://venturebeat.com/orchestration/enterprise-ai-is-entering-an-evaluation-gap-agents-are-gaining-autonomy-faster-than-companies-can-verify-them)
- [CIO Dive – Agentic AI strains legacy IT](https://www.ciodive.com/news/agentic-ai-strains-legacy-it-systems/825003/)
- [Hugging Face – Laguna S 2.1](https://huggingface.co/poolside/Laguna-S-2.1-NVFP4)
