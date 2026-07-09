---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-07-09
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 9 juli 2026

## 🔑 Highlights van de dag

- **EU AI Act T-24 dagen**: Op 2 augustus 2026 krijgt de Europese Commissie formele handhavingsbevoegdheid over aanbieders van general-purpose AI-modellen. Bedrijven die GPAI-diensten leveren moeten nú hun documentatie op orde hebben.
- **Microsoft Frontier Company**: Microsoft investeert $2,5 miljard in een nieuwe business unit die 6.000 AI-engineers direct bij klanten inzet voor end-to-end implementaties. Signaal: de markt verschuift van tooling verkopen naar resultaatverantwoordelijkheid nemen.
- **Agentic AI security crisis**: Uit nieuw onderzoek blijkt dat 88% van enterprise-organisaties in het afgelopen jaar een AI agent security incident heeft gehad. JadePuffer, de eerste gedocumenteerde "agentic ransomware", bewijst dat dit geen theoretisch risico meer is.
- **Open source AI is productieklaar**: Kimi K2.6 (1,1T params) en Qwen3 235B-A22B (Apache 2.0) zijn in 2026 serieuze productie-alternatieven voor gesloten modellen, ook voor agentic toepassingen.
- **Nederland kiest digitale soevereiniteit**: Het kabinet scherpt het cloudbeleid aan en wil rijksdata zoveel mogelijk in eigen datacenters houden. VLAM (Veilige Lokale AI Modellen) moet het soevereine GenAI-platform voor de overheid worden.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-5.6 Sol** is uitgebracht als "meest agentische model tot nu toe" en stelt gebruikers in staat werk over subagents te verdelen voor langere autonome taken. De uitrol verloopt bewust traag: de Amerikaanse overheid keurt toegang "klant voor klant" goed vóór een brede release.

**Anthropic Claude Sonnet 5** (uitgebracht eind juni) positioneert zich als de goedkopere keuze voor agentische workflows op $2/M input tokens (tot 31 augustus), met sterke verbeteringen op redeneren, tool use en codering. Daarnaast zijn de exportbeperkingen op de Fable- en Mythos-modellen opgeheven door de Trump-administratie.

**Open-source landscape**: Kimi K2.6 scoort het hoogst voor development-taken, Qwen3 235B-A22B is de veiligste enterprise-keuze (Apache 2.0), en Gemma 4 26B is het meest praktisch voor lokale inzet met 256K context-window. Open source is niet meer de goedkope variant — het is een volwaardig alternatief.

*Bronnen: [TechCrunch – Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/) | [TechCrunch – open source](https://techcrunch.com/2026/07/07/why-the-rise-of-open-source-ai-isnt-hurting-anthropic-yet/) | [Hugging Face – open source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)*

---

## 🏛️ Governance & Ethiek

**EU AI Act – kritieke deadline**: Op **2 augustus 2026** gaan de handhavingsbevoegdheden van de EC over GPAI-providers van kracht. Tegelijkertijd worden de transparantieregels (Art. 50) van toepassing. De deadline om de vrijwillige Code of Practice inzake AI-gegenereerde content te ondertekenen is **22 juli 2026** — minder dan twee weken weg.

**Nederland – digitale soevereiniteit**: Het kabinet scherpt het cloudbeleid aan met als doel minder afhankelijkheid van Amerikaanse aanbieders. Staatssecretaris Aerdts werkt aan een overheidsbreed cloudkader. Google Cloud heeft de privacytoets van het Rijk wél doorstaan. VLAM — het rijksbrede platform voor lokale AI-modellen — is in ontwikkeling als soeverein alternatief voor commerciële GenAI-diensten.

*Bronnen: [EU AI Act implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/) | [Computable – cloudbeleid](https://www.computable.nl/2026/07/07/rijk-scherpt-cloudbeleid-aan-minder-afhankelijk-van-vs-en-strengere-eisen-maar-lange-overgangstermijn/) | [Computable – soevereiniteit](https://www.computable.nl/2026/07/03/kabinet-kiest-voor-maximale-digitale-soevereiniteit/)*

---

## 🔐 Security & Risk

Dit is de meest zorgwekkende sectie van de week. Drie grote bevindingen:

1. **JadePuffer – eerste agentic ransomware**: Gedocumenteerd door Sysdig. Een AI-agent voerde een volledige aanvalsketen uit: inbraak, credential-diefstal, laterale beweging, versleuteling én het schrijven van het losgeldbriefje. Een mens initieerde het, maar de uitvoering was autonoom. ([TechCrunch](https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/))

2. **Secrets-lekkage via AI coding agents**: GitGuardian meldt dat AI-assisted commits (zoals Claude Code) secrets lekken op een tarief van 3,2% — ruim twee keer het normale baseline van 1,5%. AI service credential-leaks stegen 81% jaar-op-jaar naar 1,275 miljoen blootgestelde credentials. ([VentureBeat](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026))

3. **88% incident rate**: Bijna alle grote organisaties die AI-agents inzetten rapporteerden het afgelopen jaar een beveiligingsincident. Prompt injection blijft het #1 OWASP-risico voor LLM-toepassingen.

Conclusie: wie AI-agents in productie draait zonder gelaagd privilege-beheer en secrets management, speelt Russisch roulette.

---

## 📈 Markt & Adoptie

**Microsoft Frontier Company** ($2,5B, 6.000 experts) is de grootste strategische move van de week. Het gaat niet om meer licenties verkopen, maar om resultaatverantwoordelijkheid: Microsoft co-ontwerpt, co-implementeert en verbetert AI-systemen continu bij de klant. Tegelijkertijd legde Microsoft 5.000 medewerkers af in Xbox en commerciële sales — kapitaal stroomt van traditionele business naar AI-delivery. ([Microsoft Blog](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/))

**SAP Business AI Platform + Autonomous Suite**: SAP bundelt zijn gehele technologie, data en AI in één platform met agents die end-to-end bedrijfsprocessen automatiseren. Voor SAP-klanten (ook Ctac-klanten) wordt dit de komende kwartalen de meest tastbare AI-verandering.

**Microsoft Copilot**: 20+ miljoen betaalde seats, AI annual run rate van $37 miljard (+123% YoY). Enterprise AI is geen experiment meer.

*Bronnen: [TechCrunch – Microsoft Frontier](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) | [CIO Dive – SAP](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/) | [CIO Dive – Microsoft Copilot](https://www.ciodive.com/news/microsoft-earnings-Q3-2026/819009/)*

---

## 💡 Ctac-relevantie

**EU AI Act deadline (2 augustus)** is direct handelingsplichtig: als Ctac GPAI-diensten afneemt of doorlevert aan klanten, moeten de due diligence-documenten nú in orde zijn. De Code of Practice ondertekenen voor 22 juli geeft positieve signaalwerking richting overheidsklanten.

**Microsoft Frontier Company** is een directe concurrent voor Ctac's advies- en implementatiewerk. Het model waarbij vendor-engineers bij klanten zitten is precies het terrein waar Ctac opereert. Kans: positioneer Ctac als de onafhankelijke, multi-vendor tegenhanger die niet vastzit aan één model of cloud.

**Agentic AI security** moet een concrete propositie worden, niet alleen een risicowaarschuwing. Klanten in overheid en finance bouwen agents en weten niet wat ze beveiligen moeten. Ctac's AI engineer kan hier een security-by-design framework voor agentic architecturen uitwerken.

**VLAM en digitale soevereiniteit** sluiten direct aan op de overheidsmarkt van Ctac. Open-source modellen zoals Qwen3 of Gemma 4 lokaal draaien is nu technisch volwassen — een sovereign AI stack voor publieke sector is een reëel voorstel geworden.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Claude Sonnet 5 (30 juni)](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)
- [TechCrunch – Open source vs Anthropic (7 juli)](https://techcrunch.com/2026/07/07/why-the-rise-of-open-source-ai-isnt-hurting-anthropic-yet/)
- [EU AI Act – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [EC – Code of Practice AI-gegenereerde content](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content)
- [Computable – Cloudbeleid Rijk (7 juli)](https://www.computable.nl/2026/07/07/rijk-scherpt-cloudbeleid-aan-minder-afhankelijk-van-vs-en-strengere-eisen-maar-lange-overgangstermijn/)
- [Computable – Digitale soevereiniteit (3 juli)](https://www.computable.nl/2026/07/03/kabinet-kiest-voor-maximale-digitale-soevereiniteit/)
- [Microsoft Blog – Frontier Company (2 juli)](https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/)
- [TechCrunch – Microsoft Frontier Company](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/)
- [TechCrunch – JadePuffer ransomware (6 juli)](https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/)
- [VentureBeat – AI agent security incidents](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds)
- [VentureBeat – Secrets lekkage via AI agents](https://venturebeat.com/security/ai-agent-runtime-security-system-card-audit-comment-and-control-2026)
- [Hugging Face – Open source LLMs 2026](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [CIO Dive – SAP Business AI Platform](https://www.ciodive.com/news/sap-creates-single-platform-enterprise-ai/820015/)
- [CIO Dive – Microsoft vs Google enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
