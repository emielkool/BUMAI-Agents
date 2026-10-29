---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-10-29
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 29 oktober 2026

## 🔑 Highlights van de dag

- **EU AI Act handhaaft voor het eerst:** De EU AI Office stuurde begin deze week formele informatieverzoeken aan OpenAI en Anthropic na incidenten met AI-agenten. Geen boetes nog, maar de toon is gezet — dit is het begin van echte handhaving.
- **Microsoft-kwartaalcijfers: Copilot explodeert:** Dagelijkse Copilot-gebruikers zijn vijfvoudig gestegen jaar-op-jaar; omzet groeide 19% naar $92,3 miljard. Enterprise-AI is duidelijk uit de experimenteerfase.
- **Prompt injection schaalt naar RCE:** Endor Labs publiceerde gisteren 14 kwetsbaarheden in 7 AI-platforms waarbij prompt injection leidt tot remote code execution en datadiefstal — een duidelijk signaal dat agentic AI nieuwe aanvalsoppervlakken opent.
- **Agentic AI versnelt:** GPT-6.1 Terra is algemeen beschikbaar met 50% prijsverlaging voor computer-use; Google lanceert Gemini als plannings- en delegatie-agent voor enterprise. De stap van "chatbot" naar "werknemer" wordt concreet.
- **Harvard-onderzoek corrigeert hype:** AI coding agents verhogen code-output met 30%, maar verlengen code review-tijd met 49%. Netto productiviteitswinst is reëel maar kleiner dan aankondigingen suggereren.

---

## 🧠 Technologie & Modellen

**Anthropic** bracht op 7 oktober Claude Haiku 5.5 uit als het nieuwste lid van de Claude 5.5-familie (naast Sonnet 5.5 en Opus 5.5). Opvallender is **Claude Duet** (21 oktober, preview voor US Pro/Max): een proactieve achtergrondagent die zelfstandig taken oppakt zonder directe gebruikersinteractie. Dit is Anthropics antwoord op de agentic-race.

**OpenAI** maakte GPT-6.1 Terra algemeen beschikbaar (circa 26 oktober) met een prijsverlaging van 50% voor computer-use workloads — een directe stimulans voor developers om agenten in te zetten voor browserautomatisering en GUI-taken. De GPT-6 familie telt inmiddels meerdere varianten (Terra, Sol, Luna, Pro), wat de marktcommunicatie versnipperd maakt.

**Google** opende Gemini 4 Argon op 13 oktober voor betalende gebruikers wereldwijd na een beperkte lancering voor cyberbeveiligingsteams. Op 8 oktober kondigde Google aan dat Gemini evolueert naar een agent die subtaken plant en delegeert — geïntegreerd in de enterprise-suite.

*Kanttekening:* Release-trackers spreken elkaar tegen op exacte datums en modelnamen. Verifieer altijd via de officiële vendor-blogs vóór je dit communiceert naar klanten.

Bronnen: [llmgateway.io](https://llmgateway.io/timeline) · [TechCrunch – Google Gemini Agentic](https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/) · [aiagentsdirectory.com (27 okt)](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-27-2026)

---

## 🏛️ Governance & Ethiek

De **EU AI Office** is per 2 augustus 2026 bevoegd tot handhaving van de AI-verordening. Op 14 oktober bevestigde EVP Henna Virkkunen dat de AI Office informatieverzoeken heeft gestuurd aan aanbieders van general-purpose AI-modellen, gelinkt aan incidenten met AI-agenten waarbij OpenAI en Anthropic betrokken zijn. Nog geen boetes — de eerste zijn te verwachten in 2027.

Belangrijk: de **Digital Omnibus-verordening (EU) 2026/1744** heeft de meeste high-risk verplichtingen verschoven naar respectievelijk 2 december 2027 en 2 augustus 2028. Dat geeft bedrijven meer ademruimte, maar maakt compliantie-planning op de lange termijn ook ingewikkelder.

Vanaf **2 december 2026** gelden nieuwe verboden, waaronder verbod op AI-gegenereerd niet-consensueel intiem materiaal en CSAM.

In Nederland eist de **Consumentenbond** samen met de ACM dat bedrijven transparanter communiceren wanneer klantenservice door AI wordt afgehandeld — aangehaakt aan de transparantieverplichtingen uit de AI Act.

Bronnen: [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act) · [technology.org – eerste handhavingszaak](https://www.technology.org/2026/10/15/eu-ai-act-first-enforcement-openai-anthropic-ai-office/) · [actuia.com – Omnibus delays](https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/)

---

## 🔐 Security & Risk

**Endor Labs** publiceerde op 28 oktober een rapport over 14 kwetsbaarheden verspreid over zeven AI-platforms, waarbij prompt injection leidt tot remote code execution en datadiefstal. Het bedrijf wijst op drie structurele risicofactoren: te ruime privileges voor agenten, slechte isolatie tussen agent-sessies, en misplaatst vertrouwen in externe data.

**Radware** presenteerde op 27 oktober onderzoek waarbij 86 miljoen GitHub-items werden gescand op verborgen prompt-injecties die AI-codeeragenten kunnen manipuleren. Indirect prompt injection — waarbij de kwaadaardige instructie verborgen zit in een document, e-mail of webpagina die de agent verwerkt — blijft het dominante aanvalspatroon.

OWASP-onderzoeker Ariel Fogel herhaalde op Infosecurity Europe 2026: "Prompt injection is structureel onopgelost." Het model verwerkt systeemprompt en gebruikersinput als één tekststroom — het onderscheid tussen 'instructie' en 'data' bestaat niet op architectuurniveau.

**Panasonic Nederland:** Een medewerker uploadde persoonsgegevens van circa 334.000 personen naar een niet-goedgekeurde externe AI-dienst (23 oktober). Dit is een klassiek lek via de "bring-your-own-AI"-route die veel organisaties nog niet hebben dichtgetimmerd.

Bronnen: [cybrsecmedia.com – Endor Labs](https://www.cybrsecmedia.com/prompt-injection-flaws-expose-7-ai-platforms-to-remote-code-execution/) · [airia.com – lethal trifecta](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/) · [infosecurity-magazine.com](https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/)

---

## 📈 Markt & Adoptie

**Microsoft** rapporteerde kwartaalcijfers (28 oktober): omzet +19% YoY naar $92,3 miljard, dagelijkse Copilot-gebruikers vijfvoudig gestegen. Copilot-klanten op consumptie-billing groeiden >75% kwartaal-op-kwartaal. Dit zijn structurele adoptiemetreken, geen proeflicenties.

**Google** hernoemde zijn enterprise AI-platform van Vertex AI naar Gemini Enterprise in september 2026 en integreert agentic capabilities direct in de cloud-suite. **Amazon** werkt samen met OpenAI om OpenAI-gebouwde agenten via AWS Bedrock aan te bieden — een strategische keuze die de hyperscaler-competitie complex maakt: AWS verkoopt nu ook OpenAI-producten.

**Capex-race:** Gecombineerde AI-infrastructuurinvestering van Microsoft, Google en Amazon wordt voor heel 2026 geschat op $763 miljard. Beleggers kijken scherp of de returns inmiddels zichtbaar worden — Microsoft lijkt die drempel te passeren.

**Arctic Wolf** (27 oktober): agentic AI lost nu ~60% van beveiligingsonderzoeken op binnen hun SOC-platform, met menselijk toezicht op de overige 40%. Dit is een vroeg bewijs van agentic AI in productie bij enterprise security.

Bronnen: [pymnts.com – Microsoft earnings](https://www.pymnts.com/earnings/2026/microsoft-sees-enterprise-ai-adoption-accelerate-as-copilot-usage-grows/) · [GlobeNewswire – Arctic Wolf](https://globenewswire.com/news-release/2026/10/27/3389057/0/en/arctic-wolf-2026-agentic-security-operations-report-reveals-ai-now-resolves-the-majority-of-security-investigations-in-its-agentic-soc.html)

---

## 💡 Ctac-relevantie

**AI Act compliance als dienst:** De eerste EU-handhavingsacties creëren directe vraag bij klanten naar compliance-begeleiding. Ctac kan hier positioneren met een gestructureerde scan van AI-inzet versus de risicoklassen uit de AI Act — met name voor klanten in overheid, zorg en finance die zich voor high-risk verplichtingen moeten voorbereiden op 2027/2028.

**Agentic AI-proposities rijpen:** GPT-6.1 Terra met 50% prijsverlaging en Google's agentic Gemini maken het bouwen van werkende agent-workflows betaalbaar voor enterprise. Dit is het moment om met klanten concrete agent-use cases te identificeren (document-review, monitoring, customer service). De Harvard-bevinding dat review-tijd met 49% stijgt, is nuttig als verwachtingsmanagement: agents vragen ook nieuwe werkprocessen.

**Security by design voor AI:** Het Panasonic-lek en de Endor Labs-bevindingen tonen dat "bring-your-own-AI" een serieus datarisico is. Ctac kan klanten helpen met AI-governance beleid en technische guardrails (data classification, agent sandboxing, privilege minimization) — dit sluit aan op bestaande IT-security proposities en vereist geen opbouw vanaf nul.

**Rijksmuseum × Prosus:** De driejarige AI-samenwerking is een concreet Nederlands voorbeeld van enterprise AI-adoptie in de publieke sector — bruikbaar als referentie en gespreksopener bij overheidsklanten.

---

## 📚 Bronnen & verder lezen

- [TechCrunch – Google Gemini agentic AI for business](https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/)
- [EU AI Office – enforcement framework](https://digital-strategy.ec.europa.eu/en/policies/enforcement-ai-act)
- [technology.org – eerste handhavingszaak OpenAI/Anthropic](https://www.technology.org/2026/10/15/eu-ai-act-first-enforcement-openai-anthropic-ai-office/)
- [actuia.com – AI Act Omnibus vertraging](https://www.actuia.com/en/news/ai-act-obligations-in-force-and-delays-under-omnibus-2026-1744/)
- [cybrsecmedia.com – Endor Labs 14 kwetsbaarheden](https://www.cybrsecmedia.com/prompt-injection-flaws-expose-7-ai-platforms-to-remote-code-execution/)
- [airia.com – AI Security 2026: Lethal Trifecta](https://airia.com/blog/ai-security-in-2026-prompt-injection-the-lethal-trifecta-and-how-to-defend/)
- [infosecurity-magazine.com – OWASP: prompt injection onopgelost](https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/)
- [pymnts.com – Microsoft Q1 FY2027 cijfers](https://www.pymnts.com/earnings/2026/microsoft-sees-enterprise-ai-adoption-accelerate-as-copilot-usage-grows/)
- [GlobeNewswire – Arctic Wolf Agentic Security Report](https://globenewswire.com/news-release/2026/10/27/3389057/0/en/arctic-wolf-2026-agentic-security-operations-report-reveals-ai-now-resolves-the-majority-of-security-investigations-in-its-agentic-soc.html)
- [aiagentsdirectory.com – Agents news 27 oktober](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-27-2026)
- [llmgateway.io – AI model release tracker](https://llmgateway.io/timeline)
- [aiinsider.nl](https://aiinsider.nl/) · [hetlaatsteainieuws.nl](https://www.hetlaatsteainieuws.nl/)
