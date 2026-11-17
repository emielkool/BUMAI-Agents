---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-12
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 12 oktober 2026

## 🔑 Highlights van de dag

- **GPT-6 is live**: OpenAI lanceerde op 7 oktober GPT-6 in twee varianten (Sol en Luna), met een nieuw Intelligent UI dat tekst, visuals en interactieve elementen combineert in één interface — dit is een merkbare gebruikerservaring-sprong, geen incrementele verbetering.
- **Claude Haiku 5.5 maakt agentic pipelines goedkoper**: Anthropic's nieuwste kleine model heeft nu een instelbaar effort-niveau en is ontworpen als goedkope helper naast Opus 5.5 en Sonnet 5.5 in meerlagige agentische workflows.
- **EU AI Act transparantieverplichting handhaving nadert**: Artikel 50 is al van kracht (2 augustus 2026), maar de technische markering van AI-gegenereerde content krijgt een respijtperiode tot 2 december 2026 — organisaties die dit nog niet geregeld hebben lopen nu echt risico.
- **Agentic AI = prioriteit #1 securityrisico**: Uit meerdere rapporten blijkt dat prompt injection en tool misuse bij autonome AI-agents de snelst groeiende aanvalsvectoren zijn, met name bij agents die long-term credentials opslaan.
- **PwC zet 30.000 medewerkers op Claude**: De PwC-uitbreiding met Anthropic toont dat professionele dienstverleners agentic AI op industriële schaal inzetten — relevant model voor Ctac.

---

## 🧠 Technologie & Modellen

**GPT-6: Sol, Luna en Intelligent UI**
OpenAI rolde op 7 oktober GPT-6 uit voor alle ChatGPT-gebruikers. Plus/Pro/Business/Enterprise krijgen GPT-6 Sol; Free/Go-gebruikers GPT-6 Luna. De grootste vernieuwing is *Intelligent UI*: ChatGPT combineert nu dynamisch tekst, diagrammen, rekenmachines en mini-apps in één gesprek op basis van de vraag. Het model "antwoordt terwijl het nadenkt" — de wachttijd bij redenering wordt zo verborgen. Op 29 september lanceerde OpenAI ook al GPT-6.1 Sol voor developers (DevDay). Noot: hogere modellen (Astra) zijn nog achter een trusted-access programma geplaatst vanwege cyberveiligheidsgevoeligheid.
*Bron: [9to5Mac](https://9to5mac.com/2026/10/07/openai-brings-gpt-6-to-chatgpt-and-debuts-intelligent-ui/), [OpenAI](https://openai.com/index/introducing-gpt-6-sol-and-luna/)*

**Claude Haiku 5.5 — goedkope agent in een groter systeem**
Anthropic's Haiku 5.5 (7 oktober) is de eerste Haiku met een instelbaar effort-niveau. Het model is expliciet ontworpen voor high-volume taken als zijagent in meerlaagse pipelines naast Sonnet en Opus. Dit verlaagt de kosten voor agentic workflows substantieel.
*Bron: [LLM Gateway](https://llmgateway.io/blog/new-ai-models-this-week-2026-10-11)*

**Meer opvallende releases deze week**
- *Mistral Large 4* (preview, 6 oktober): Mistral's krachtigste instructiemodel tot nu toe.
- *Clef-omni* van Cloudflare (9 oktober): open-weight multimodaal model (audio, video, beeld, tekst) beschikbaar op Hugging Face. Interessant voor on-premise deployments.
- *Microsoft-Decision-1* (9 oktober): smal scoremodel voor routing en classificatietaken, beschikbaar via Microsoft Foundry.

---

## 🏛️ Governance & Ethiek

**EU AI Act Artikel 50 — handhavingsvenster sluit in december**
De transparantieverplichting is van kracht sinds 2 augustus 2026: aanbieders moeten gebruikers informeren dat ze met AI interageren, en synthetische content moet machine-leesbaar gemarkeerd worden. De respijtperiode voor de technische markering loopt af op **2 december 2026**. Boetes: tot €15 miljoen of 3% van de wereldwijde jaaromzet.

Onduidelijkheid blijft bestaan over de high-risk verplichtingen (Annex III): de Digital Omnibus zou die mogelijk vertragen tot december 2027, maar trilogonderhandelingen zijn nog gaande. Geen formele publicatie in het Publicatieblad van de EU — behandel huidige deadlines als leidend.
*Bron: [Cooley](https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026), [artificialintelligenceact.eu](https://artificialintelligenceact.eu/transparency-rules-article-50/), [Morgan Lewis](https://www.morganlewis.com/blogs/sourcingatmorganlewis/2026/08/eu-ai-acts-transparency-rules-what-went-into-effect-on-2-august)*

---

## 🔐 Security & Risk

**Agentic AI als aanvalsvlak — het groeit snel**
Uit meerdere 2026-rapportages (SentinelOne, HiddenLayer, Darktrace) blijkt een consistent beeld: autonome AI-agents zijn het snelst groeiende aanvalstarget. De meest genoemde dreigingen:

- *Prompt injection*: nog altijd de #1 op de OWASP LLM Top 10.
- *Excessive Agency*: sprong van positie 6 naar positie 3 in de 2026-ranking — agents met te brede rechten zijn een bewezen risico.
- *Credential theft*: agents die API-sleutels en chatbot-credentials opslaan zijn een primair doelwit voor infostealer malware (IBM X-Force).
- *Deepfake-fraude*: 73% van security professionals ervaart een significante impact van AI-gestuurde aanvallen op de eigen organisatie.

Kritische noot: de meeste statistieken komen van vendoren met een belang in alarmisme. Richtinggevend, niet absoluut.
*Bron: [Stellar Cyber](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/), [Darktrace](https://www.darktrace.com/blog/state-of-ai-cybersecurity-2026-87-of-security-professionals-are-seeing-more-ai-driven-threats-but-few-feel-ready-to-stop-them), [HiddenLayer](https://www.hiddenlayer.com/report-and-guide/threatreport2026)*

---

## 📈 Markt & Adoptie

**Microsoft en OpenAI: partnership losser, eigen routes**
Microsoft lanceerde in juli 2026 een eigen AI implementation unit met 2,5 miljard dollar en 6.000 medewerkers. Tegelijkertijd heeft Microsoft de exclusiviteitsrechten op distributie van OpenAI-modellen ingeleverd — beide partijen gaan nu deels eigen wegen. Enterprise maakt >40% van OpenAI's omzet uit. Azure OpenAI (56%) en Google Gemini (48%) lopen naast elkaar als meest gebruikte enterprise-platforms.
*Bron: [CNBC Microsoft](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html), [CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)*

**PwC + Anthropic: schaalontwikkeling als signaal**
PwC rolt Claude Code en Claude Cowork uit naar honderdduizenden medewerkers wereldwijd en certificeert 30.000 professionals op Claude. Dit is het meest concrete signaal tot nu toe dat grote professionele dienstverleners agentic AI structureel inbedden — niet als experiment maar als operationeel model.
*Bron: [PwC](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html)*

---

## 💡 Ctac-relevantie

**Drie directe aandachtspunten voor Ctac:**

1. **EU AI Act deadline 2 december**: Ctac zelf en klanten die AI-gegenereerde content publiceren (overheid, finance, zorg) moeten de machine-leesbare markering vóór 2 december regeld hebben. Dit is een concrete, hanteerbare compliance-opdracht die Ctac als quickwin kan aanbieden aan klanten die nog niet zover zijn.

2. **Agentic pipelines worden standaard**: De combinatie GPT-6 + Haiku 5.5 + Microsoft-Decision-1 laat zien dat de markt beweegt naar meerlaagse, gespecialiseerde agentarchitecturen in plaats van één groot model. Ctac's AI-propositie moet dit reflecteren: niet "een model kiezen" maar "een agent-architectuur ontwerpen".

3. **Het PwC-model als referentie**: 30.000 gecertificeerde professionals is een ander ordeningsprincipe dan individuele pilots. Als Ctac AI serieus wil inbedden, vraagt dat om een opleidingsprogramma en interne certificering — nu een goed moment om dat plan te scherpen voordat de markt dit als standaard verwacht.

---

## 📚 Bronnen & verder lezen

- [LLM Gateway – new models week 2026-10-11](https://llmgateway.io/blog/new-ai-models-this-week-2026-10-11)
- [9to5Mac – GPT-6 en Intelligent UI](https://9to5mac.com/2026/10/07/openai-brings-gpt-6-to-chatgpt-and-debuts-intelligent-ui/)
- [OpenAI – Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/)
- [artificialintelligenceact.eu – Article 50 transparantieregels](https://artificialintelligenceact.eu/transparency-rules-article-50/)
- [Cooley – EU AI Act transparantieverplichting 2 augustus 2026](https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026)
- [Morgan Lewis – Wat ging van kracht op 2 augustus?](https://www.morganlewis.com/blogs/sourcingatmorganlewis/2026/08/eu-ai-acts-transparency-rules-what-went-into-effect-on-2-august)
- [Darktrace – State of AI Cybersecurity 2026](https://www.darktrace.com/blog/state-of-ai-cybersecurity-2026-87-of-security-professionals-are-seeing-more-ai-driven-threats-but-few-feel-ready-to-stop-them)
- [HiddenLayer – 2026 AI Threat Landscape Report](https://www.hiddenlayer.com/report-and-guide/threatreport2026)
- [Stellar Cyber – Agentic AI Security Threats](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/)
- [CNBC – Microsoft AI implementation unit](https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html)
- [CIO Dive – Microsoft en Google domineren enterprise AI-markt](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [PwC – Uitbreiding alliantie met Anthropic](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html)
