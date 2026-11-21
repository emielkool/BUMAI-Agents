---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-02
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 2 oktober 2026

## 🔑 Highlights van de dag

- **Google Gemini 4 Argon uitgebracht, maar met beperkte toegang**: Google bracht gisteren zijn topmodel Gemini 4 Argon uit, uitsluitend beschikbaar voor een geselecteerde groep cybersecurity-experts vanwege veiligheidszorgen. Een opmerkelijk conservatieve stap die aantoont dat ook Big Tech nu safety-gating serieus neemt.
- **OpenAI lanceert GPT-6 Sol en Luna**: Twee nieuwe mid-tier modellen die goedkoper en betrouwbaarder zijn dan de huidige topmodellen. GPT-6.1 Sol benadert de prestaties van GPT-6 Astra tegen significant lagere kosten — de prijzenoorlog in inference gaat onverminderd door.
- **Anthropic breidt Barclays-deal uit**: Barclays rolt Claude uit over zijn wereldwijde operaties, een van de grootste enterprise-bancaire AI-deployments tot nu toe. Dit signaleert dat het financiële domein volwassen genoeg is voor brede AI-adoptie.
- **EU AI Act enforcement actief**: Vanaf 2 augustus 2026 houden de AI Office en nationale toezichthouders toezicht op naleving. Boetes voor overtredingen kunnen oplopen tot 15 miljoen euro of 3% van de wereldwijde jaaromzet.
- **Agentic AI security wordt kritisch**: Prompt injection is uitgegroeid tot een volwassen aanvalscategorie; memory injection-aanvallen op AI-agents zijn nu gedemonstreerd in de praktijk.

---

## 🧠 Technologie & Modellen

**Google Gemini 4 Argon – safety-gated release**
Google heeft Gemini 4 Argon officieel gelanceerd, maar de toegang is beperkt tot een selecte groep cybersecurity-experts. Dit vertraging-en-beperking-patroon zorgt er voor dat Google voorlopig achterloopt op Anthropic en OpenAI, die de frontlinie actief blijven verleggen. ([Dawn.com](https://dawn.com/news/2033975))

**OpenAI GPT-6 Sol en Luna – inference democratisering**
OpenAI lanceerde twee nieuwe modellen: Sol en Luna. GPT-6.1 Sol benadert de prestaties van het topmodel GPT-6 Astra en kost aanzienlijk minder. De trend is duidelijk: frontier performance daalt structureel in prijs. ([llm-stats.com](https://llm-stats.com/llm-updates))

**Anthropic Claude Opus 5.5 en Sonnet 5.5**
Opus 5.5 heeft striktere safeguards voor cybersecurity-toepassingen; Sonnet 5.5 positioneert Anthropic als kostenefficiënte enterprise-partner. Barclays' globale uitrol onderstreept de enterprise-geloofwaardigheid. ([llm-stats.com](https://llm-stats.com/ai-news))

**Open-weight: Qwen 3.6 Plus als reëel alternatief**
Alibaba's Qwen 3.6 Plus presteert op SWE-Bench Verified vergelijkbaar met Claude Opus en GPT-5.4, ondersteunt 1 miljoen tokens context en handelt tool-use betrouwbaar af. Dit is geen speelgoed meer — open-weight modellen naderen frontier-niveau op agentic coding. ([mindstudio.ai](https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026))

---

## 🏛️ Governance & Ethiek

**EU AI Act: handhavingsfase is begonnen**
Vanaf 2 augustus 2026 zijn de AI Office en nationale autoriteiten operationeel bevoegd om de AI Act te handhaven. De lopende tijdlijn:
- **Nu actief**: Article 50 transparantieverplichtingen (deepfake-labeling, AI-interactie-disclosure)
- **December 2026**: Verboden praktijken worden van kracht
- **December 2027**: High-risk systemen (Annex III)
- **Augustus 2028**: Productgekoppelde AI-systemen (Annex I)

Boetes: tot €15 mln of 3% wereldwijde omzet. Organisaties die nog geen risicoklassificatie hebben gemaakt, lopen nu daadwerkelijk risico. ([legalnodes.com](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks), [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai))

---

## 🔐 Security & Risk

**Agentic AI is de nieuwe aanvalsoppervlakte**
Twee concrete dreigingen domineren de security-agenda deze week:

1. **Memory injection op AI-agents**: Aanvallers injecteren kwaadaardige data in de geheugen-databronnen van agents, waardoor agents persistente valse overtuigingen ontwikkelen over beveiligingsbeleid. Dit is geen theoretische aanval meer. ([stellarcyber.ai](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/))

2. **AI-ontdekte kwetsbaarheden worden direct geëxploiteerd**: Google's AI-agenten vinden kwetsbaarheden die leiden tot remote code execution; aanvallers reproduceerden een exploit binnen vier dagen na publieke disclosure. Het volume van CVE-disclosures verdubbelde in 2026 van ~5k naar ~10k per maand. ([helpnetsecurity.com](https://www.helpnetsecurity.com/2026/10/01/google-ai-discovered-vulnerabilities-remote-code-execution/))

Indirect prompt injection via web pages, documenten en e-mails is nu de dominante aanvalsvector. Dit is direct relevant voor organisaties die AI-agents op productiedata loslaten.

---

## 📈 Markt & Adoptie

**Hyperscaler capex: $660-690 miljard in 2026**
Microsoft, Google, Amazon, Meta en Oracle investeren samen $660-690 miljard in AI-infrastructuur dit jaar. Amazon leidt met $200 mrd, Alphabet met $175-185 mrd. De schaal van deze investeringen maakt het steeds moeilijker voor Europese spelers om zelfstandige AI-infrastructuur op te bouwen. ([futurumgroup.com](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/))

**Google Agentic Data Cloud**
Google Cloud lanceerde Agentic Data Cloud: een AI-native architectuur die legacy enterprise-dataplatformen omzet in reasoning engines. Directe concurrent voor databricks/Snowflake-posities. ([ciodive.com](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/))

**Microsoft Copilot: adoptieprobleem blijft**
Bij organisaties waar medewerkers naast Copilot ook ChatGPT en Gemini beschikbaar hebben, daalt actief Copilot-gebruik naar 8%. Alleen als Copilot het enige beschikbare AI-hulpmiddel is, stijgt gebruik naar ~68%. Dit raakt direct de business case van Microsoft 365 Copilot-implementaties. ([geekwire.com](https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/))

---

## 💡 Ctac-relevantie

**EU AI Act compliance is nu een concrete salesopening.** De handhaving is operationeel; veel klanten van Ctac in finance, overheid en zorg vallen onder Article 50 of Annex III. Een AI-risicoclassificatie-scan als instapproduct is nu urgent en verkoopbaar — niet als nice-to-have maar als compliance-verplichting.

**Het Copilot-adoptieprobleem is een kans voor Ctac.** Het dalende actieve gebruik van Copilot in multi-AI omgevingen bevestigt dat technologie alleen onvoldoende is. Ctac kan hier een rol spelen in het begeleiding van change management en AI-governance rondom Microsoft-deployments — een dienst die de implementatie-business verdiept.

**Agentic AI security wordt een nieuw adviesdomein.** Naarmate klanten AI-agents op productiedata inzetten, neemt het risico op memory injection en prompt injection exponentieel toe. Ctac's AI-unit kan nu proactief security-kaders rondom agentic systemen ontwikkelen als onderscheidend aanbod.

**Intern**: Ctac heeft in H1 2026 tegenwind gehad maar richt zich strategisch op AI en sovereign cloud. De huidige model-prijsdaling (GPT-6.1 Sol, Sonnet 5.5) maakt AI-integraties voor klanten goedkoper — gebruik dit als commercieel argument om projecten die vastgelopen waren op businesscases opnieuw op te pakken.

---

## 📚 Bronnen & verder lezen

- [Google Gemini 4 Argon aankondiging – Dawn.com](https://dawn.com/news/2033975)
- [New AI Model Releases October 2026 – blog.mean.ceo](https://blog.mean.ceo/new-ai-model-releases-news-october-2026/)
- [LLM Updates – llm-stats.com](https://llm-stats.com/llm-updates)
- [LLM AI News – llm-stats.com](https://llm-stats.com/ai-news)
- [Last Week in AI #345](https://lastweekin.ai/p/last-week-in-ai-345-5-new-models)
- [EU AI Act 2026 updates – legalnodes.com](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)
- [EU AI Act – digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [AI Security: remote code execution via AI-discovered vulns – helpnetsecurity.com](https://www.helpnetsecurity.com/2026/10/01/google-ai-discovered-vulnerabilities-remote-code-execution/)
- [Top Agentic AI Security Threats 2026 – stellarcyber.ai](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/)
- [Google Agentic Data Cloud – ciodive.com](https://www.ciodive.com/news/google-launches-agentic-data-cloud/818235/)
- [Microsoft Copilot adoptie-probleem – geekwire.com](https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/)
- [AI Capex 2026: $690B – futurumgroup.com](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/)
- [Best Open-Source LLMs agentic coding 2026 – mindstudio.ai](https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026)
- [Ctac H1 2026 resultaten – dutchitchannel.nl](https://www.dutchitchannel.nl/news/756237/tegenwind-dwingt-ctac-tot-koerswijziging)
