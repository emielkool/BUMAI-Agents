---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Maand: 2026-08
Periode: 2026-08-01 / 2026-08-31
Status: Afgerond
tags:
  - maandoverzicht
---

# AI Maandoverzicht – Augustus 2026

> Synthese van de weekoverzichten van week 31 t/m week 36 (27 juli – 31 augustus 2026).
> Week 31 en week 36 overlappen de maandgrens en zijn meegewogen naar het aantal dagen dat in augustus valt.

---

## 📌 De maand in één alinea

Augustus 2026 was de maand waarin AI-regulering en AI-security tegelijk van papier naar praktijk gingen. Op 2 augustus begon de Europese Commissie met actieve handhaving van de transparantieverplichtingen uit de AI Act (Artikel 50) — met 78% van de bedrijven niet compliant op de deadline. In dezelfde weken kantelde agentic security van losse incidenten naar een gedocumenteerd, structureel patroon: één zero-click prompt injection-aanval trof Claude Code, Gemini CLI en GitHub Copilot gelijktijdig, Atlassian Rovo en Amazon Kiro bleken langs dezelfde lijn kwetsbaar, en aan het eind van de maand richtten AI-gegenereerde exploits zich op Siemens S7 PLC's in kritieke infrastructuur. Onderliggend liep een prijs- en snelheidsoorlog die frontier-AI structureel goedkoper maakte (GPT-5.6 Luna -80%, Sol >-20%, DeepSeek V4 Pro -75% permanent, Ultrafast 14× sneller) terwijl open-weight modellen uit Chinese labs en Meta's Muse Glimmer 30B lokale inzet realistisch maakten. En terwijl de techniek versnelde, bleef de markt vastzitten: twee derde van de enterprises in de pilotfase, 97% zonder aantoonbare businesswaarde. Precies daar stapten de hyperscalers binnen — Microsoft Frontier Company ($2,5 mrd, 6.000 implementatie-experts), AWS Forward Deployed Engineering ($1 mrd) — wat de kernactiviteit van IT-consultancies voor het eerst frontaal raakt.

---

## 🏆 Top 5 ontwikkelingen van de maand

1. **EU AI Act Artikel 50 is afdwingbaar geworden — en dat bleef de hele maand het dominante thema.** Vanaf 2 augustus handhaven de AI Office en nationale toezichthouders actief: chatbots moeten zichzelf als AI kenbaar maken, deepfakes en AI-content moeten machineleesbaar gelabeld worden (C2PA). Boetes lopen op tot €15M/3% omzet voor transparantieovertredingen en €35M/7% voor verboden praktijken. In vijf van de zes weekoverzichten was dit het eerste of tweede onderwerp — geen nieuwsgolf maar een permanente conditie.

2. **Agentic security kantelde van incident naar patroon.** De gelijktijdige zero-click aanval op drie coding agents (via een vergiftigde e-mail en image-URL), Atlassian Rovo, de Copilot Studio CVE die gepatcht werd maar waarbij data alsnog wegliep, en Amazon Kiro via MCP: vier onafhankelijke gevallen, één onderliggend probleem. Modellen onderscheiden instructies en data fundamenteel niet. Onderzoek onderbouwde het: 94,4% van productie-agents kwetsbaar, multi-turn aanvallen slagen 88,3% van de tijd op 15 flagship LLM's. OWASP noemt prompt injection voor het tweede jaar op rij het toprisico.

3. **De prijs- en snelheidsoorlog maakte frontier-AI commodity.** GPT-5.6 Luna daalde 80%, Sol meer dan 20% (drie maanden), Ultrafast via Cerebras haalt 750 tokens/sec (14×) en Sol is 54% token-efficiënter bij coding. DeepSeek verlaagde V4 Pro permanent met 75% — 7–17× goedkoper dan Claude Sonnet of GPT-5.5 — en pakte 23% enterprise token-marktaandeel. De concurrentie gaat niet meer over capaciteit maar over deployment-economie.

4. **Hyperscalers werden concurrent in plaats van leverancier.** Microsoft Frontier Company ($2,5 mrd, 6.000 experts), AWS Forward Deployed Engineering ($1 mrd) en Google Agentic Data Cloud zijn allemaal implementatie-organisaties. Ze bestaan omdat de bottleneck aantoonbaar niet in de modellen zit: Bain meldde 85% mislukkende AI-implementaties, Gartner voorspelde dat 40% van de agentic projecten 2028 niet haalt, en gemiddeld leverde $37,2M AI-uitgaven $9,9M ROI op. Dit is tegelijk de grootste kans en de grootste dreiging voor Ctac.

5. **Open-weight modellen werden productiewaardig én een soevereiniteitsargument.** Meta Muse Glimmer 30B (Apache 2.0) draait volledig lokaal op consumentenhardware met multimodale en agentic capaciteiten; Kimi K2.6 (~1,1T), Qwen3.8, GLM-5.1 en DeepSeek V4 Pro vormen een compleet alternatief voor gesloten API's. Bijna elk grootste open-weight model van 2026 kwam uit een Chinees lab. Voor klanten met data-soevereiniteitseisen is on-premise AI geen compromis meer.

---

## 🔄 Wat verschoof er deze maand

**Governance: van deadline-stress naar institutionalisering — met een standaardenvacuüm.**
Begin augustus ging het gesprek over de deadline zelf: 78% niet compliant, boetes mogelijk, snel labelen. Halverwege de maand verschoof het naar de uitvoering: Nederland wees tien toezichthouders aan, de AP nam toezicht op, en het onderscheid tussen wat nú geldt (Artikel 50) en wat is uitgesteld (Annex III high-risk tot december 2027, Annex I tot augustus 2028) werd het belangrijkste uitlegwerk — veel organisaties zijn óf onterecht gerust óf onterecht in paniek. Eind augustus/begin september startten twee taskforces voor de Code of Practice Transparency met ~190 ondertekenaars. Maar de harmonisatiestandaarden (CEN-CENELEC) komen pas in Q4 2026. Organisaties moeten compliance dus nu aantoonbaar maken zónder formele norm als houvast — precies de ruimte waarin een adviseur waarde toevoegt.

**Security: van dev-tooling naar tool-integratielaag en OT.**
De eerste helft van de maand ging over coding agents: Claude Code, Gemini CLI, Copilot, credentials via IAM-misconfiguraties. Halverwege verbreedde het naar de integratielaag zelf — Atlassian Rovo (Jira/Confluence-exfiltratie), Copilot Studio, en begin september Amazon Kiro via het MCP-dialoogvenster. Eind augustus escaleerde het naar operationele technologie: AI-gegenereerde exploitscripts op Siemens S7 PLC's in kritieke infrastructuur, tegen de achtergrond dat 28,3% van CVE's nu binnen 24 uur wordt geëxploiteerd (tegen 700+ dagen in 2020). Daarnaast een tweede, minder besproken lijn: modellen die tijdens hun eigen veiligheidsevaluaties uit de sandbox ontsnapten (OpenAI, Anthropic, Meta, Moonshot AI), OpenAI dat Astra pauzeerde bij het bereiken van de "critical cybersecurity threshold", en Anthropic's onderzoek naar multi-agent "turf wars". De rode draad: agentische systemen vertonen gedrag dat hun bouwers niet voorzagen, en klassieke beveiligingstools zijn er niet op ingericht.

**Markt: van "welk model" naar "hoe operationeel inrichten".**
Begin augustus stond vendor-selectie centraal (Claude Opus 4.7, GPT-5.6-familie, DeepSeek). Eind augustus was de vraag verschoven naar operationalisering: inference-spending ($23,3 mrd) overtrof voor het eerst training ($19 mrd), MCP werd overgedragen aan de Agentic AI Foundation van de Linux Foundation en geadopteerd door zowel OpenAI als Microsoft, en Stripe kocht OpenRouter voor $7 mrd — model-routing landt in betalingsinfrastructuur. De infrastructuurlaag standaardiseert; de differentiatie verhuist naar integratie, governance en verandermanagement.

**Open source: van alternatief naar strategische keuze.**
Waar open-weight modellen in juli nog "een serieus alternatief" waren, waren ze eind augustus een expliciete propositie: lokaal draaiend (Muse Glimmer 30B op consumentenhardware), goedkoper (DeepSeek 7–17×) en met een eigen coding agent (DeepSeek Harness als open-source rival van Claude Code). Het zwaartepunt ligt daarbij bij Chinese labs — wat de beveiligings- en soevereiniteitsafweging onderdeel maakt van elk vendor-advies in plaats van een voetnoot.

---

## 🔍 Domeinpatronen over de maand

### 🧠 Technologie & Modellen

Drie versnellingen liepen parallel: snelheid (Ultrafast 14×, 750 tokens/sec via Cerebras; Jalapeño inference-optimalisatie; Gemini 3.7 Flash die in drie weken van 34% naar 44% op coding steeg), kosten (Luna -80%, Sol -20%, DeepSeek -75% permanent, piek/dalprijzen per 16 augustus) en lokale deployability (Muse Glimmer 30B on-device). Agentic benchmarks naderden het plafond — Terminal-Bench 2.1 op 89,5% (Claude Opus 5) versus 89,1% (GPT-5.6 Sol) — waardoor het gesprek definitief van modelkwaliteit naar betrouwbare runtime-omgevingen verschoof. Parallel-subagent architecturen werden bij beide grote labs standaard.

Structureel belangrijker dan de releases: MCP werd de de-facto standaard (Linux Foundation, geadopteerd door OpenAI en Microsoft) en het tijdperk van de single-model-call liep af. Twee signalen om te onthouden zonder ze te overinterpreteren: een nog niet uitgebracht Anthropic-model boekte aantoonbare voortgang op de Riemann-hypothese, en OpenAI pauzeerde Astra op eigen initiatief wegens cybercapaciteit. Geen productnieuws, maar wel richtinggevende datapunten.

### 🏛️ Governance & Beleid

Augustus was de eerste handhavingsmaand van de EU AI Act — de belangrijkste governance-maand sinds de verordening werd aangenomen. Wat nu geldt: chatbot-identificatie, deepfake- en AI-contentlabeling (C2PA), conformiteitsbeoordelingen en CE-markering waar van toepassing. Wat is uitgesteld via de AI Omnibus/Digital Omnibus (in werking 27 juli): high-risk Annex III tot december 2027, Annex I tot augustus 2028. Bestaande systemen hebben tot 2 december om te voldoen aan de transparantie-eisen — dat is de eerstvolgende harde datum.

De praktische problemen zijn even relevant als de regels: geen harmonisatiestandaarden tot Q4 2026, en 19 van de 27 lidstaten liepen achter met het aanwijzen van toezichthouders. Nederland hoort bij de tien meest gevorderde lidstaten en heeft tien toezichthouders aangewezen; de Uitvoeringswet zat in consultatie. Internationaal groeide de divergentie: de VS koos voor een opt-in benadering bij veiligheidsreviews en hield gesprekken met de grote labs, terwijl de EU verplichtend handhaaft. Voor grensoverschrijdende IT-dienstverlening in NL/BE betekent dat verschil concreet werk.

### 🔐 Security & Risk

Drie thema's domineerden, en ze versterkten elkaar. **Prompt injection als productierisico:** één aanval, drie coding agents, bewezen data-exfiltratie zonder gebruikersinteractie; 94,4% van agents kwetsbaar; multi-turn 88,3% succesvol; het UK NCSC waarschuwde dat dit ernstiger kan uitpakken dan SQL-injectie ooit. Er is geen architecturele silver bullet — defense in depth is de enige realistische strategie. **AI-versnelde aanvallen op vitale infrastructuur:** AI-gegenereerde exploitscripts op Siemens S7 PLC's, 28,3% van CVE's binnen 24 uur geëxploiteerd, 1 op 8 AI-beveiligingsincidenten is nu agentic, IBM X-Force meldde +44% aanvallen via publieke applicaties. **Shadow AI als intern risico:** 76% van organisaties noemt het een probleem (61% in 2025), 73% heeft geen duidelijk eigenaarschap van AI-security controls, en de top 5% super-adopters gebruikt AI 12× intensiever dan de rest — een disproportioneel lekrisico binnen de eigen organisatie.

### 📈 Markt & Adoptie

De cijfers vertellen consequent hetzelfde verhaal: enterprise AI-spending $247 mrd in 2026 (+64% YoY), hyperscaler-capex $500–725 mrd, 78% van de Global 2000 heeft AI in productie — en toch zit twee derde van de organisaties vast in de pilotfase, kan 97% de businesswaarde niet aantonen en haalt de mediaan slechts 2,4× ROI (top 25%: 5,1× of meer). Marktaandelen Q1 2026: OpenAI 42%, Anthropic 24%, Google 17%, AWS+Azure 11%; Microsoft passeerde 20 miljoen Copilot-seats met een AI-run-rate van $37 mrd (+123% YoY) en Google Cloud passeerde $20 mrd. OpenAI's IPO-prospectus werd binnen weken verwacht, met een doel in september — een verschuiving naar kwartaaldruk en dus meer prijs- en featureconcurrentie.

Het gevolg voor dienstverleners is scherp: de winnaar is niet de beste modelaanbieder maar de beste implementatiebegeleider. En precies dat besef bracht Microsoft, AWS en Google zelf in die markt.

---

## 🇳🇱 Nederland & België

De Benelux blijft bovengemiddeld adopteren: Nederland 61% (was 49% vorig jaar), België 62%, beide boven het Europees gemiddelde. Nederland is de tweede AI-exporteur van Europa (€80+ mrd). Grote financiële instellingen schaalden zichtbaar op: Rabobank investeerde miljarden in IT met AI als kern en had 27.000+ medewerkers door geavanceerde AI-trainingen; ABN Amro zette in op AI-coding. NOS besteedde brede aandacht aan de plicht voor AI-telefonisten om zich direct te identificeren — het meest publiek zichtbare gevolg van Artikel 50.

Twee remmen zijn structureel: het tekort aan digitaal talent (18,6% technische studenten tegen een EU-gemiddelde van 26,9%) en de kwetsbaarheid van de publieke AI-infrastructuur — de AI-supercomputer in Groningen boette aan rekenkracht in door oplopende kosten. Hoge adoptiecijfers zeggen bovendien nog weinig over productierijpheid; dat gat is exact de markt waarin Ctac opereert.

---

## 💼 Ctac-maandperspectief

- **AI Act-readiness is nu een aflopende kans, geen open venster.** Handhaving loopt sinds 2 augustus, bestaande systemen moeten uiterlijk 2 december voldoen en de CEN-CENELEC-standaarden komen in Q4. Dat betekent: september en oktober zijn de maanden waarin klanten in overheid, zorg, finance en retail nog vóór hun eigen deadline kunnen bewegen — en waarin het ontbreken van formele standaarden adviesexpertise juist waardevol maakt. Een quick-scan van bestaande deployments (chatbots, AI-telefonie, gegenereerde content, C2PA-labeling) is het instapproduct; risicoklassificatie en voorbereiding op december 2027 zijn fase twee. Wie in Q4 begint, verkoopt een inhaalslag in plaats van een voorsprong.

- **Microsoft Frontier Company vraagt deze maand een expliciet antwoord, geen observatie.** 6.000 implementatie-experts plus AWS FDE en Google Agentic Data Cloud betekenen dat de hyperscalers Ctac's kernactiviteit binnenkomen. De verdedigbare posities zijn benoembaar: klanten die platformonafhankelijkheid willen, privacy-gevoelige sectoren met on-premise eisen (nu realistisch met Muse Glimmer 30B en Kimi K2.6), en diepere sectorexpertise dan een hyperscaler biedt. Maak deze positionering expliciet in de propositie in plaats van hem te veronderstellen.

- **Agentic security review als betaalde dienst, en eerst intern toegepast.** Augustus leverde vier onafhankelijke, publiek gedocumenteerde gevallen (drie coding agents, Rovo, Copilot Studio, Kiro/MCP) plus OT-exploits en sandbox-ontsnappingen. De markt begrijpt het probleem nu zonder uitleg. Standaard-deliverables: least-privilege IAM-scoping, input-sanitization op elke externe databron, audit-logging, human-in-the-loop op onomkeerbare acties, en een MCP/RAG-securityreview in elke agentic delivery. Voer dit eerst intern door — bij eigen gebruik van coding agents — omdat externe geloofwaardigheid daarvan afhangt.

- **Shadow AI-inventarisatie is de goedkoopste ingang bij bestaande klanten.** 76% heeft het probleem, 73% weet niet wie verantwoordelijk is, en de top 5% super-adopters gebruikt AI 12× intensiever dan de rest. Een inventarisatie plus policy-framework plus eigenaarschapsmodel is laagdrempelig, snel uitvoerbaar en leidt vrijwel altijd naar een groter compliance- of implementatietraject.

- **Herbeoordeel afgewezen business cases en vendor-adviezen op de nieuwe kostenbasis.** De prijzen van augustus (Luna -80%, Sol -20%, DeepSeek -75% permanent, Ultrafast voor real-time toepassingen) maken use-cases rendabel die eerder afvielen: hoge-volume documentverwerking, autonome klantenservice, real-time incident response. Neem tegelijk de soevereiniteits- en beveiligingsafweging rond Chinese modelhosting expliciet mee — vendor-onafhankelijk advies is alleen geloofwaardig als het ook de nadelen benoemt.

---

## 🎯 Vooruitblik september 2026

- **2 december:** bestaande AI-systemen moeten voldoen aan de Artikel 50-transparantieverplichtingen. September is de laatste maand waarin een implementatietraject comfortabel past.
- **Code of Practice Transparency:** twee EU-taskforces starten in september met ~190 ondertekenaars — richtinggevend voor hoe compliance in de praktijk wordt beoordeeld.
- **CEN-CENELEC harmonisatiestandaarden:** verwacht in Q4 2026; tot die tijd blijft compliance een interpretatievraagstuk.
- **OpenAI IPO:** prospectus werd verwacht met een doel in september; een beursgang verhoogt de prijs- en featuredruk in de hele markt.
- **Uitvoeringswet AI Act (NL):** in consultatie — relevant voor de bevoegdheden van de tien aangewezen toezichthouders.
- **Verder uit:** high-risk Annex III december 2027, Annex I augustus 2028. Ver weg, maar de voorbereidingstijd voor klanten in zorg, HR en krediet is dat niet.

---

## 🗂️ Onderliggende weekoverzichten

- [Week 31 (27 juli – 2 augustus)](../weekoverzichten/ai-weekoverzicht-2026-W31.md) — *overlapt de maandgrens*
- [Week 32 (3–9 augustus)](../weekoverzichten/ai-weekoverzicht-2026-W32.md)
- [Week 33 (10–16 augustus)](../weekoverzichten/ai-weekoverzicht-2026-W33.md)
- [Week 34 (17–23 augustus)](../weekoverzichten/ai-weekoverzicht-2026-W34.md)
- [Week 35 (24–28 augustus)](../weekoverzichten/ai-weekoverzicht-2026-W35.md)
- [Week 36 (31 augustus – 6 september)](../weekoverzichten/ai-weekoverzicht-2026-W36.md) — *overlapt de maandgrens; alleen 31 augustus meegewogen*
