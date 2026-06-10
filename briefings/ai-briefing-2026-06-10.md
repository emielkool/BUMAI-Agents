---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-06-10
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 10 juni 2026

## 🔑 Highlights van de dag

- **EU AI Act Omnibus definitief**: na het politieke akkoord van 7 mei zijn de hoge-risico deadlines verschoven naar december 2027 en augustus 2028 — de volledige toepasselijkheid per 2 augustus 2026 geldt wél, inclusief GPAI-verplichtingen.
- **MCP-kwetsbaarheden bereiken systeemniveau**: een architectuurfout in Anthropic's Model Context Protocol treft 7.000+ publieke servers en meer dan 150 miljoen downloads; de risico's voor agentic AI-deployments zijn acuut.
- **Microsoft verbreekt de modeldependentie**: met MAI-Code-1-Flash en een Foundry-catalogus van 11.000+ modellen mikt Microsoft bewust op minder afhankelijkheid van OpenAI, juist nu de codeermarkt ($9,3 mrd → $30 mrd tegen 2031) explodeert.
- **Google Cloud vaart een sterke koers**: 63% omzetgroei naar $20 mrd, Gemini Enterprise +40% betaalde MAU. Google en Microsoft delen de enterprise-markt, maar Google wint op agentic AI.
- **Prompt injection als structureel risico**: OWASP-#1 dreigingscategorie met 340% meer aanvallen j-o-j; de MCP-kwetsbaarheid versterkt dit verder voor organisaties die AI-agents inzetten.

---

## 🧠 Technologie & Modellen

**Microsoft MAI-Code-1-Flash** werd op Build aangekondigd als Microsoft's eerste eigen coderingsmodel — van beschrijving naar werkende code voor applicaties en websites. Tegelijk bevat het Foundry-platform nu meer dan 11.000 modellen, waaronder OpenAI GPT-5.5 en Anthropic Claude Opus 4.8. De strategische boodschap is helder: Microsoft wil multi-vendor zijn en de afhankelijkheid van één modelleverancier reduceren. ([CNBC, 2 juni](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html))

**Google Gemini 3.5 Flash** is GA sinds 19 mei (Google I/O). Gemini 3.5 Pro is in juni verwacht en moet de redeneer-regressie van Flash herstellen; dit is het model voor reasoning-zware enterprise-toepassingen. ([LLM Stats](https://llm-stats.com/ai-news))

**Anthropic** breidde op 2 juni Project Glasswing uit — het programma dat Claude Mythos Preview (gelanceerd april 2026) naar enterprise schaalt. De recente $65 mrd Series H-ronde (waardering: $965 mrd) geeft Anthropic de middelen voor infra-uitbreiding op grote schaal. ([Anthropic Newsroom](https://www.anthropic.com/news))

*Beoordeling:* De "11.000 modellen in Foundry"-claim is marketingretoriek; de werkelijk bruikbare modellen zijn een handvol. MAI-Code-1-Flash is interessant als kostenbesparend alternatief, maar mist nog het track record van GPT of Claude.

---

## 🏛️ Governance & Ethiek

**EU AI Act Omnibus** (politiek akkoord: 7 mei 2026) verschuift de meest belastende deadlines:
- Annex III (hoog-risico use cases: recruitment, kredietscoring, handhaving) → compliance per **2 december 2027**
- Annex I (AI ingebed in gereguleerde producten) → **2 augustus 2028**

De volledige werking van de AI Act per **2 augustus 2026** verandert echter niet. GPAI-verplichtingen gelden al sinds augustus 2025. De **GPAI Code of Practice** is afgerond en ondertekend door ~24 aanbieders (waaronder Anthropic, Google, IBM, Microsoft, Mistral en OpenAI) — Meta ontbreekt, xAI tekende uitsluitend het veiligheidshoofdstuk. ([artificialintelligenceact.eu](https://artificialintelligenceact.eu/) | [verifywise.ai Omnibus analyse](https://verifywise.ai/blog/eu-ai-act-omnibus-what-changed))

Lidstaten moeten per 2 augustus 2026 minimaal één nationaal AI-sandbox hebben ingericht. Nederland loopt hierbij voor; voor klanten in gereguleerde sectoren (overheid, finance, zorg) begint actieve handhavingspraktijk zichtbaar te worden.

---

## 🔐 Security & Risk

**MCP-systeemkwetsbaarheid** is de dominante AI-security-dreiging van dit moment. Een architectuurfout in Anthropic's officiële MCP SDK's (Python, TypeScript, Java, Rust) maakt remote code execution mogelijk via poisoned config files en tool poisoning. Cijfers: 7.000+ publiek toegankelijke servers, 150M+ downloads, 492 MCP-servers zonder enige authenticatie online aangetroffen. Het Pentagon bestempelde Anthropic voor het eerst als "supply chain risk". ([SecurityWeek](https://www.securityweek.com/by-design-flaw-in-mcp-could-enable-widespread-ai-supply-chain-attacks/) | [The Hacker News](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html))

**CVE-2025-53773** (CVSS 9.6): verborgen prompt injection in pull request-omschrijvingen leidt tot remote code execution via GitHub Copilot. Relevant voor elke organisatie die Copilot in CI/CD-pipelines gebruikt.

**Prompt injection +340% j-o-j**: OWASP heeft het als dreigingsnummer 1 geclassificeerd voor 2026. Gecombineerd met MCP-blootstelling is dit een acuut risico voor teams die agentic AI-workflows bouwen. ([airia.com](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/))

*Aanbeveling:* Tool allowlisting, identity binding, runtime monitoring en human-in-the-loop checkpoints zijn nu de minimumvereisten voor verantwoorde agent-deployments.

---

## 📈 Markt & Adoptie

**Microsoft** domineert enterprise-AI breed via ecosysteem en platform-reach ($150 mrd capex/jaar). **Google** wint specifiek op agentic AI: betaalde Gemini Enterprise-gebruikers groeiden 40% in het afgelopen kwartaal, met Bosch, Mars en Merck als referentieklanten. Google Cloud groeide 63% j-o-j naar $20 mrd. ([CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/) | [CNBC](https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html))

De **AI-codeermarkt** groeit naar verwachting 26% per jaar, van $9,3 mrd nu naar ~$30 mrd in 2031 (Mordor Intelligence). Microsoft en Google voeren hier nu actief een strijd om marktaandeel met eigen modellen naast die van OpenAI en Anthropic.

---

## 💡 Ctac-relevantie

**Directe actie op security:** Elke Ctac-delivery die MCP-servers of agentic workflows gebruikt (intern of bij klanten), dient nu te worden geauditeerd op blootstelling. CVE-2025-53773 en het MCP-architectuurprobleem zijn geen theoretische risico's — ze zijn documenteerbaar misbruikt in productieomgevingen. Maak van tool allowlisting en runtime monitoring een standaardonderdeel van elk AI-agent-project.

**EU AI Act Omnibus — timing herschikken:** De uitstel van Annex III naar december 2027 geeft klanten in recruitment, finance en handhaving meer lucht. Maar de augustus 2026 deadline nadert snel, en GPAI-compliance geldt al. Ctac kan nu specifiek waarde leveren door klanten in gereguleerde sectoren te helpen hun GPAI-blootstelling in kaart te brengen (welke modellen zijn in gebruik? welke van de ondertekende Code of Practice-aanbieders worden gebruikt?).

**Multimodel-strategie:** De Foundry-aanpak van Microsoft (11.000 modellen, vendor-agnostisch) sluit aan op wat Ctac zou moeten adviseren aan klanten: geen lock-in op één model, maar een evaluatiemethodologie die kosten, prestaties en compliance afweegt. De opbouw van die methodologie is nu strategisch relevant.

---

## 📚 Bronnen & verder lezen

- [LLM Stats – AI updates juni 2026](https://llm-stats.com/ai-news)
- [CNBC – Microsoft MAI-Code-1-Flash, 2 juni 2026](https://www.cnbc.com/2026/06/02/microsoft-unveils-new-ai-models-lessen-reliance-on-openai-lower-costs.html)
- [CNBC – Microsoft & Google vs Anthropic & OpenAI in coding, 1 juni 2026](https://www.cnbc.com/2026/06/01/microsoft-and-google-take-on-anthropic-and-openai-in-ai-coding-models.html)
- [Anthropic Newsroom](https://www.anthropic.com/news)
- [EU AI Act Omnibus analyse – verifywise.ai](https://verifywise.ai/blog/eu-ai-act-omnibus-what-changed)
- [artificialintelligenceact.eu – implementatietijdlijn](https://artificialintelligenceact.eu/implementation-timeline/)
- [GPAI Code of Practice introductie](https://artificialintelligenceact.eu/introduction-to-code-of-practice/)
- [SecurityWeek – MCP by-design flaw](https://www.securityweek.com/by-design-flaw-in-mcp-could-enable-widespread-ai-supply-chain-attacks/)
- [The Hacker News – Anthropic MCP RCE vulnerability](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html)
- [airia.com – AI Security 2026: Prompt Injection en de Lethal Trifecta](https://airia.com/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [CIO Dive – Microsoft & Google domineren enterprise AI](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [CSA Research Note – MCP Security Crisis (4 mei 2026)](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-security-crisis-20260504-csa-styled/)
