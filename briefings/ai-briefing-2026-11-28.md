---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-28
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 28 november 2026

## 🔑 Highlights van de dag

- **OpenAI GPT-6.2 rolt uit naar eindgebruikers:** Na de API-lancering op 17 november zijn Astra (geavanceerd redeneren) en Sol (snel en goedkoop) sinds 23 november beschikbaar voor Plus/Pro/Business/Enterprise. Dit zet nieuwe druk op concurrenten én op enterprise-beslissers die hun modelkeuze moeten heroverwegen.
- **Nederland: kabinet presenteert AI-visie "Kiezen voor AI voor iedereen":** Op 6 november keurde de ministerraad een nationale AI-visie goed met drie pijlers: verantwoord gebruik, toegang & veiligheid, en publieke waardensturing. Er komt een Nederlands AI Safety Institute; het compute-plan volgt begin 2027.
- **Europese open-source modellen botsen met publieke waarden:** Onderzoek van UTF.ai (26 november) toont aan dat Europese open-weight modellen regelmatig in strijd zijn met Nederlandse publieke normen — kritisch signaal voor overheids-AI-beleid en compliance.
- **Anthropic op weg naar beursgang:** Fable 5.2 en Mythos 5.2 gelanceerd (9 nov), IPO roadshow gestart (10 nov). Anthropic neemt inmiddels de lead over van OpenAI in enterprise AI-omzet.
- **EU AI Act GPAI-handhaving actief:** Sinds augustus 2026 heeft het AI Office afdwingingsbevoegdheden over General Purpose AI-aanbieders, inclusief boetes tot 3% van wereldwijde jaaromzet.

---

## 🧠 Technologie & Modellen

**OpenAI GPT-6.2 familie** is de dominante release van deze periode. Astra (frontier reasoning, complex professional work) en Sol (sneller en kostenefficiënt) zijn nu breed beschikbaar. ChatGPT wordt aangedreven door een geoptimaliseerde Sol-variant. Op 5 november introduceerde OpenAI ook GPT-6 Cyber, een gespecialiseerd security-model voor het vinden en fixen van exploiteerbare kwetsbaarheden — een opvallende strategische stap.

**Aleph Alpha Kolibri 1.1** (23 nov, Apache 2.0, 75B params/3,44B actief) is een relevante Europese open-source release gericht op Duits en Engels. Sterk verbeterde benchmark-scores ten opzichte van 1.0 bij lagere compute-kosten. Voor Ctac-klanten in de publieke sector die soevereine modellen willen, is dit een namen om bij te houden.

**Thinking Machines Inkling 2 Small** (20 nov) is een multimodaal open model (tekst + beeld, 594B totaal/17B actief) met een Mini-variant voor lokale setups. De "decision model"-categorie groeit snel: Amazon heeft ook al een eigen variant uitgebracht.

**Microsoft** heeft bij Build 2026 een eigen modelfamilie van zeven modellen gelanceerd — een signaal dat het bedrijf actief wil diversifiëren weg van volledige OpenAI-afhankelijkheid.

---

## 🏛️ Governance & Ethiek

**Nederland: "Kiezen voor AI voor iedereen"** (6 nov) is een brede kabinetsvisie — ambitieus geformuleerd, maar de NOS constateert dat de feitelijke investeringen beperkt zijn en datacenters nog altijd politiek gevoelig liggen. Staatssecretaris Aerdts wil een nationaal AI Safety Institute; details en tijdlijn nog onduidelijk.

**EU AI Act GPAI:** De handhavingsbevoegdheden van het AI Office zijn actief. Het GPAI Code of Practice (10 juli 2025) is het complianceframework. High-risk verplichtingen schuiven op naar december 2027 (Digital Omnibus), maar GPAI en transparantie-eisen (Art. 50) zijn al van kracht. Organisaties zijn ook indirect blootgesteld via de compliance-status van hun AI-leveranciers.

**AI-tokenkosten en WBSO:** De wetgeving om AI-tokenkosten aftrekbaar te maken via WBSO R&D-regeling wordt niet voor 2027 verwacht. Bedrijven die dit willen toepassen in 2027 moeten vóór 1 januari een aanvraag indienen.

**Tweede Kamer** dringt aan op een sterkere minister voor digitale zaken en een "Dutch Tech Force" voor overheids-ICT.

---

## 🔐 Security & Risk

**Prompt injection blijft toprisico.** Cycode en RedFox Security markeren indirecte injectie (via documenten, e-mails en webpagina's die agenten ophalen) als het dominante aanvalsvector in 2026. Lakera-onderzoek (november 2026) bevestigt *memory poisoning*: vergiftigde data corrumpeert het langetermijngeheugen van agenten en is daardoor moeilijk te detecteren.

**GitHub Copilot CVE-2025-53773 (CVSS 9.6):** Een kritieke kwetsbaarheid in AI-codeerassistenten toont aan dat ontwikkeltools zelf aanvalsvectoren worden. De aanvalssuccesratio's voor coding assistants liggen tussen de 50–84% (Vectra AI-schattingen — niet onafhankelijk geverifieerd).

**Agenten met toolaccess** zijn bijzonder kwetsbaar: privilege escalation-chains waarbij agents worden gemanipuleerd om hoog-privileged tools aan te roepen zijn een opkomend patroon bij enterprise deployments.

---

## 📈 Markt & Adoptie

**OpenAI:** Kwartaalomzet doorbreekt $10 miljard voor het eerst. Enterprise vertegenwoordigt nu de meerderheid van de omzet (was ~30%). IPO-plan voor 2027 bevestigd door president Greg Brockman.

**Anthropic overtreft OpenAI in enterprise-omzet** (Bloomberg-bronnen). De Fable/Mythos 5.2-launch en de aankomende beursgang versterken de positie — Ctac-partners en klanten kunnen verwachten dat Anthropic actief enterprise-sales opbouwt.

**Microsoft 365 Copilot:** >20 miljoen betaalde seats, AI-business op $37B+ run rate (+123% YoY). Satya Nadella stelt dat AI-agenten de economie van het web gaan herstructureren — search, advertenties en workflow-software staan onder druk.

**Microsoft "vrij van OpenAI":** Microsoft AI-chief geeft aan dat het bedrijf nu de ruimte neemt om zelfstandig richting superintelligentie te werken. Dit is een strategisch kantelmoment voor het Microsoft-partner-ecosysteem, inclusief Ctac.

**Marktvoorzichtigheid:** Ramp-data laat zien dat token-spending in augustus–september slechts 1,5% groeide ondanks toenemend gebruik — prijsdruk dempt omzetgroei bij AI-providers.

---

## 💡 Ctac-relevantie

**Korte termijn (nu):** De GPT-6.2-uitrol en de opmars van Anthropic in enterprise maken het urgent om klantadvies over modelkeuze te actualiseren. Waar eerder GPT-4o de standaard was, zijn er nu serieuze alternatieven — dit is een adviesgesprek dat klanten al verwachten.

**WBSO-kans:** De mogelijke aftrekbaarheid van AI-tokenkosten via WBSO is concreet interessant voor Ctac-klanten met eigen model-experimentatie. Aanvraagdeadline is 1 januari 2027 — dit verdient een gerichte klantcommunicatie deze week.

**Security & agenten:** De risico's rond AI-agenten (memory poisoning, privilege escalation) zijn geen toekomstige zorg maar actueel. Klanten die agentic workflows bouwen of evalueren hebben concrete beveiligingsadviezen nodig — dit is een propositie-kans voor Ctac's AI- en security-teams gezamenlijk.

**EU AI Act compliance:** Nederlandse overheidsklanten worden direct geraakt door het onderzoek rond open-source modellen en publieke waarden. Ctac kan hier een beoordelingskader aanbieden.

---

## 📚 Bronnen & verder lezen

- [OpenAI Model Release Notes](https://help.openai.com/en/articles/9624314-model-release-notes)
- [Introducing GPT-6 Cyber – OpenAI](https://openai.com/index/introducing-gpt-6-cyber/)
- [Anthropic newsroom](https://www.anthropic.com/news)
- [Aleph Alpha Kolibri 1.1 – Hugging Face](https://huggingface.co/Aleph-Alpha/Kolibri-1.1)
- [Thinking Machines Inkling 2 – Hugging Face Blog](https://huggingface.co/blog/thinkingmachines-inkling)
- [OpenAI revenue crosses $10B – TechCrunch](https://techcrunch.com/2026/11/11/openais-quarterly-revenue-reportedly-crosses-10b-for-the-first-time/)
- [Ramp: AI spending stalling – TechCrunch](https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/)
- [Microsoft & Google rule enterprise AI – CIO Dive](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- [Satya Nadella: AI agents reshuffle the web – TechCrunch](https://techcrunch.com/2026/11/18/satya-nadella-predicts-ai-agents-will-reshuffle-the-economics-of-the-web/)
- [Microsoft AI chief: "set free" from OpenAI – VentureBeat](https://venturebeat.com/ai/microsoft-ai-chief-says-company-was-set-free-from-openai-to-pursue-superintelligence)
- [Kabinet AI-visie "Kiezen voor AI voor iedereen" – Computable](https://www.computable.nl/2026/11/06/kabinet-wil-ai-ontwikkeling-meer-sturen/)
- [NOS: Nederland afhankelijk van buitenlandse AI](https://nos.nl/artikel/2638296-kabinet-wil-meer-met-ai-maar-nederland-zal-afhankelijk-blijven)
- [Europese open-source modellen vs publieke waarden – Computable](https://www.computable.nl/2026/11/26/europese-ai-opensource-modellen-nog-vaak-strijdig-met-publieke-waarden/)
- [AI-tokenkosten en WBSO – Computable](https://www.computable.nl/2026/11/09/kosten-van-ai-tokens-mogelijk-aftrekbaar-via-wbso/)
- [Tweede Kamer: digitale autonomie – Computable](https://www.computable.nl/2026/11/12/tweede-kamer-wil-actie-en-daadkracht-bij-digitale-autonomie/)
- [EU AI Act GPAI Enforcement Goes Live – CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-gpai-enforcement-20260803-csa-st/)
- [Agentic AI Security Threats – Stellar Cyber](https://stellarcyber.ai/learn/agentic-ai-securiry-threats/)
- [AI Security Vulnerabilities 2026 – Cycode](https://cycode.com/blog/ai-security-vulnerabilities/)
- [Prompt injection – Vectra AI](https://www.vectra.ai/topics/prompt-injection)
