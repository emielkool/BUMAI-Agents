---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-22
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 22 november 2026

## 🔑 Highlights van de dag

- **Anthropic naar de beurs:** Anthropic noteert op de Nasdaq (ticker: ANT) tegen $83 per aandeel, marktwaarde circa $1,5 biljoen. Direct na de beursgang daalden AI-aandelen breed – de markt is verdeeld of dit het hoogtepunt markeert.
- **Model-race hoe dan ook door:** OpenAI (GPT-6.2 Astra/Sol), Google (Gemini 4 Neon) en Microsoft (zes Ignite-modellen) lanceerden allemaal nieuwe varianten deze week. Prijzen dalen fors – maar de first responses zijn kritisch: GPT-6.2 wordt omschreven als "essentially unusable" door power users.
- **AI supply chain onder druk:** Twee gekaapte Python-releases van Microsofts agent-framework op PyPI (17 november) en een kwaadaardige RubyGem die credentials steelt bevestigen dat de AI-toolstack een nieuw aanvalsoppervlak is.
- **Banken reguleren AI-agents proactief:** Citi, JPMorgan en BofA pasten hun gebruiksvoorwaarden aan: klanten die AI-agents toegang geven tot bankrekeningen, zijn zelf aansprakelijk. Signaal dat enterprise AI-agents de mainstreamfase ingaan.
- **EU AI Act: consultatie grondrechteneffectbeoordeling gestart.** De Commissie heeft op 16 november een conceptsjabloon gepubliceerd voor de verplichte grondrechtentoets bij hoog-risicosystemen.

---

## 🧠 Technologie & Modellen

De week stond in het teken van een opeenhoping van model-releases zonder duidelijke winnaar. **Google Gemini 4 Neon** (18 nov.) claimt coding-performance op Opus 5.5-niveau met 25% lagere API-prijzen en lijkt de sterkste kandidaat. **OpenAI's GPT-6.2 Astra en Sol** kregen overwegend negatieve reacties van vroege gebruikers, ondanks een prijsverlaging van 20% op het flagship. **Microsoft** presenteerde op Ignite zes nieuwe modellen die expliciet zijn gepositioneerd als goedkopere alternatieven voor OpenAI en Anthropic – opvallend strategisch signaal richting meer onafhankelijkheid van OpenAI.

Verder: **Kimi K3.1 Pro Prime** van het Chinese Moonshot AI (20 nov.) en **Claude Mythos 5.2** van Anthropic in beperkte toegang. De modelmarkt is steeds drukker, maar het onderscheid wordt moeilijker – prijsdruk en vendor lock-in zijn nu de belangrijkere variabelen dan ruwe benchmarkscores.

---

## 🏛️ Governance & Ethiek

De EU AI Act handhaaft al volledig vanaf 2 augustus jl. Op 16 november publiceerde de Europese Commissie een conceptsjabloon voor de verplichte **grondrechteneffectbeoordeling (FRIA)**, een kernverplichting voor aanbieders van hoog-risico AI-systemen. De consultatie loopt – dit is een concreet document om op te reageren. De **Digital Omnibus** (Verordening EU 2026/1744, in werking 27 juli) heeft de deadline voor Annex III hoog-risicosystemen verschoven naar 2 december 2027, wat enige lucht geeft.

In de VS klaagden acht staten OpenAI aan wegens misleidende communicatie over de risico's van ChatGPT. Meerdere non-profitorganisaties spanden een rechtszaak aan om AI-training en -deployment te laten stilleggen bij OpenAI, Google en Meta – juridisch kansloos, maar politiek signaalfunctie.

---

## 🔐 Security & Risk

November 2026 laat zien dat de AI-stack zelf nu een preferentieel aanvalsdoel is:

- **LiteLLM CVE-2026-40217:** CISA plaatste deze kwetsbaarheid op de KEV-lijst (Known Exploited Vulnerabilities). Deadline federale instanties: 2 december. Update naar ≥ 1.83.11.
- **Microsoft agent-framework (PyPI):** Twee gekaapte releases (1.26.1/1.26.2) op 17 november. Minder dan een uur live, maar dit benadrukt het risico van niet-gepinde dependencies in AI-agents.
- **Amazon Bedrock AgentCore:** Via één prompt kon een aanvaller AWS-metadata credentials ophalen en alle agents in een account overnemen. Privilege escalatie via agent chaining is een serieuze architectuurzorg.
- **Cloudflare Workers AI:** Tenant-isolatielek in GLM-5.3 liet antwoorden van andere sessies uitlekken. Inmiddels verholpen door Cloudflare.
- **Positief:** OpenAI reduceerde het succes van reasoning-extraction aanvallen van 54% naar 0,2% – een betekenisvolle verdedigingsverbetering.

---

## 📈 Markt & Adoptie

**Anthropic's Nasdaq-beursgang** is de markante kapstok van de week. De IPO markeert volwassenheid van het AI-segment, maar ook kwetsbaarheid: AI-aandelen daalden breed na de notering. **Microsoft** rapporteerde $92,3 miljard omzet (+19%) met Copilot-groei van >75% qoq bij enterprise; **Google Cloud** boekte $30,7 miljard in Q3 (+103%). De aantallen zijn indrukwekkend, maar een separate analyse berekent dat van $307 miljard enterprise-spend slechts een minderheid concrete ROI oplevert – het verwachtingsmanagement-probleem blijft.

**Nvidia** meldde $115,8 miljard kwartaalomzet, maar stopte H200-verkopen aan China. Berichten over het vertrek van CEO Jensen Huang (12 nov.) circuleren maar zijn nog niet door primaire bronnen bevestigd – behandel als onzeker.

---

## 💡 Ctac-relevantie

**Drie directe aandachtspunten:**

1. **EU AI Act FRIA-sjabloon:** Het conceptdocument van 16 november is nu beschikbaar. Klanten met hoog-risicosystemen (overheid, zorg, HR-selectie) hebben deze beoordeling nodig voor 2027. Ctac kan dit als gestructureerd adviestraject positioneren – begin met een shortlist van klanten die in scope vallen.

2. **AI-agent security:** De reeks beveiligingsincidenten (PyPI, AgentCore, Workers AI) maakt duidelijk dat agent-architecturen zonder expliciete security-review riskant zijn. Dit versterkt de propositie voor een veiligheidsaudit als onderdeel van AI-implementatietrajecten.

3. **Prijsdruk door modelconcurrentie:** Microsoft's eigen modellen gaan direct concurreren met OpenAI en Anthropic. Voor klanten die Azure-first zijn, wordt de keuze voor Copilot vs. eigen LLM-inzet opnieuw een open vraag. Anticipeer hierop in lopende adviesgesprekken.

---

## 📚 Bronnen & verder lezen

- [AI News Today: 22 November 2026 Roundup](https://aitoolsrecap.com/Blog/ai-news-november-22-2026)
- [Microsoft aims to challenge OpenAI, Anthropic with cheaper AI models (Axios)](https://www.axios.com/2026/11/17/microsoft-ai-models-openai-anthropic-ignite)
- [GenAI security November 2026: Workers AI leak, three vLLM flaws (Adversa AI)](https://adversa.ai/blog/top-genai-security-resources-november-2026/)
- [AI agent security November 2026: AgentCore takeover, rogue agents (Adversa AI)](https://adversa.ai/blog/top-ai-agent-security-resources-november-2026/)
- [How the EU Digital Omnibus Reshapes AI Act Timelines (OneTrust)](https://www.onetrust.com/blog/how-the-eu-digital-omnibus-reshapes-ai-act-timelines-and-governance-in-2026/)
- [AI Act standardisation (EC)](https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation)
- [Latest in AI News: GPT-6.2 Astra, Gemini 4 Neon, Anthropic IPO (Rupak Ganguly)](https://rupakganguly.com/posts/latest-in-ai-news-gpt-62-astra-gemini-4-neon-anthropic-ipo/)
- [AI News Roundup November 2026 (JoinAIWeek)](https://joinaiweek.com/blog/ai-news-roundup-november-2026)
- [Enterprise AI Adoption: Microsoft Copilot Usage Grows (PYMNTS)](https://www.pymnts.com/earnings/2026/microsoft-sees-enterprise-ai-adoption-accelerate-as-copilot-usage-grows/)
- [Generative AI Market 2027 (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/11/16/3403809/0/en/generative-ai-market-companies-2027-openai-anthropic-microsoft-google-and-nvidia-scale-revenue-and-raise-record-capital-in-a-market-headed-for-usd-1-206-24-billion-by-2035.html)
