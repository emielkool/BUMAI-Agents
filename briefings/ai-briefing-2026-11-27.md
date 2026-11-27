---
Stakeholders:
  - Emiel Kool
  - Eloy Schultz
Datum: 2026-11-27
Status: Afgerond
tags:
  - overview
---

# AI Dagbriefing – 27 november 2026

## 🔑 Highlights van de dag

- **JP Morgan waarschuwt voor 24 miljoen banen:** Een nieuw rapport van JP Morgan schat dat AI-adoptie 24 miljoen knowledge-worker functies structureel raakt — de meest waarschijnlijke uitkomst is transformatie van werk, niet volledige verdringing. Dit versnelt de druk op HR-strategie bij enterprise-klanten.
- **EU AI Act: deadline 2 december 2026 nadert:** Systemen die vóór 2 augustus 2026 op de markt zijn gebracht, moeten vóór 2 december aan markeringsverplichtingen voldoen. Voor veel organisaties is dit een acute deadline die nog onderschat wordt.
- **AI-agents ontdekken autonoom zero-days:** Amazon Threat Intelligence beschrijft een Chinees-gelinkte actor die het Cairn-framework inzette om zonder menselijke sturing een zero-day te vinden. Dit markeert een kwalitatief nieuw dreigingsniveau.
- **Microsoft Ignite: MAI-modellen en 50 miljoen agents:** Microsoft introduceerde zijn eigen MAI-modelreeks met lagere prijzen dan OpenAI/Anthropic, en meldt meer dan 50 miljoen agents actief in Agent 365. Enterprise-adoptie versnelt zichtbaar.
- **Anthropic: Rust-migratie met Claude agents, 70% minder CPU:** Claude-agents migreerden de volledige Messages API van Python naar Rust. Een concreet bewijs dat agentic code-transformatie op productieniveau werkt.

---

## 🧠 Technologie & Modellen

November 2026 is een uitzonderlijk drukke maand voor modelreleases. Anthropic bracht op 9 november **Fable 5.2** uit als nieuw topmodel, een stap boven Opus 5.5. Google introduceerde **Gemini 4** in drie varianten (Carbon, Hydrogen en Neon), en OpenAI lanceerde **GPT-6.2 Astra en Sol** op 17 november. Alibaba (Qwen4-Max) en Moonshot AI (Kimi K3.1 Pro Prime) vullen de internationale lijn aan. In totaal werden er tot 24 november al meer dan 22 modellen van 13 labs uitgebracht.

Opvallend op het gebied van multimodale agenten: **GLM-5V-Turbo** (Tsinghua/Zhipu AI) scoort 62,3 op OSWorld en 75,7 op AndroidWorld, wat de lat hoger legt voor GUI-aansturing. **StudioBench** laat zien dat modellen audiovisuele productie end-to-end aankunnen, maar consistentie in kwaliteit is nog beperkt.

Praktisch relevant: Anthropic's inzet van Claude-agents voor de Rust-migratie van hun Messages API, met ~70% minder CPU-gebruik per request, is een helder enterprise-voorbeeld van ROI op agentic workflows.

**Bronnen:** [tecadmin.net – November 2026 AI Model Releases](https://tecadmin.net/november-2026-ai-model-releases/) · [theneuron.ai – AI Today 27 Nov](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-27-2026/) · [arxiv.org – StudioBench](https://arxiv.org/abs/2611.28902)

---

## 🏛️ Governance & Ethiek

De **EU AI Act** zit in een kritieke implementatiefase. Vanaf 2 augustus 2026 hebben de AI Office en nationale autoriteiten handhavingsbevoegdheden. Cruciaal voor nu: systemen die vóór die datum al op de markt waren, moeten **vóór 2 december 2026** voldoen aan markerings- en detectieverplichtingen.

De Digital Omnibus (Verordening EU 2026/1744, ingegaan op 27 juli 2026) heeft de Annex III high-risk deadline verlengd tot **2 december 2027** — wat sommige organisaties tijdelijk lucht geeft, maar het risico op compliancevertraging vergroot. Eerste geharmoniseerde norm (EN 18286, kwaliteitsmanagement) is geciteerd in het Official Journal op 14 oktober; richtlijnen voor high-risk classificatie zijn nog niet definitief.

Buiten de EU: Canada verhoogt zijn AI Compute Access Fund tot **1 miljard dollar**, en Rusland kondigde een update aan van zijn nationale AI-strategie t/m 2036.

**Bronnen:** [alicelabs.ai – EU AI Act Timeline 2026](https://alicelabs.ai/en/insights/eu-ai-act-timeline-2026) · [cubbbix.com – AI Regulation November 2026](https://cubbbix.com/blog/ai-regulation-november-2026-global-update)

---

## 🔐 Security & Risk

November 2026 laat een zorgwekkende verbreding zien van AI-specifieke dreigingen:

- **CVE-2026-103572:** Trailing-dot filename-trick leidt tot remote code execution via GitHub Copilot in Visual Studio en SSMS.
- **LiteLLM AI gateway (CVE-2026-40217):** Op 18 november toegevoegd aan CISA's Known Exploited Vulnerabilities-lijst; aanvallers met adminrechten kunnen code uitvoeren via de guardrail-testfunctie.
- **PyPI supply chain:** Twee gehijackte versies van Microsoft's Python agent-framework library (1.26.1 en 1.26.2) circuleerden op 17 november minder dan een uur op PyPI — genoeg voor schade.
- **Azure OpenAI CVE-2026-119990:** Privilege escalation met CVSS 9.8, gepatcht in Patch Tuesday november.
- **Autonome aanvallers:** De Cairn-casus (zie Highlights) toont dat de drempelverlagende werking van AI voor aanvallers tastbaar is geworden.

**Aanbeveling:** Controleer afhankelijkheden van Python agent-libraries en patching-status Azure OpenAI. Neem LiteLLM-deployments op in kwetsbaarhedenscans.

**Bronnen:** [adversa.ai – AI Coding Agent Security](https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/) · [mafurad.com – AI Agent Cyberattacks](https://www.mafurad.com/blog/ai-agent-cyberattacks-what-changed-in-november-2026-20261121) · [btigroup.com – Cybersecurity Update](https://www.btigroup.com/post/ai-cybersecurity-update-november-20-2026/)

---

## 📈 Markt & Adoptie

**Microsoft Ignite 2026** was het dominante enterprise-event van de maand. Kernpunten: introductie van de eigen **MAI-modelreeks** (goedkoper dan OpenAI/Anthropic, maar benchmark-caveats gelden), beschikbaarstelling van OpenAI-modellen via Foundry, en meldingen van 5x meer dagelijkse Copilot-gebruikers jaar-op-jaar. IBM en Microsoft lanceerden gezamenlijk **Imagine Enterprise** met 6.000 pre-built agents.

**OpenAI-modellen op Google Cloud** (private preview): de consolidatie van enterprise AI-toegang via grote cloud-hypers versnelt. Concurrentie speelt zich steeds minder af op modelkwaliteit en steeds meer op integratie, prijs en compliance.

**Nvidia pauzeert servershipments** naar Maleisië, Singapore, Thailand en Indonesië door exportcontroles die op 19 november van kracht gingen (drempel: ~750 Nvidia H100-equivalenten). Dit raakt cloud-infrastructuurplanning in Azië.

**JP Morgan-rapport** over 24 miljoen kwetsbare knowledge-worker banen is het meest geciteerde item van vandaag — niet alarmistisch, maar transformationeel van toon.

**Bronnen:** [storyboard18.com – Microsoft Ignite 2026](https://www.storyboard18.com/brand-makers/microsoft-unveils-new-enterprise-ai-agents-and-tools-at-ignite-2026-ws-l-114984.htm) · [business-standard.com – JP Morgan rapport](https://www.business-standard.com/technology/artificial-intelligence/ai-adoption-could-put-24-million-knowledge-worker-jobs-at-risk-jp-morgan-126112700267_1.html)

---

## 💡 Ctac-relevantie

**Drie directe aandachtspunten:**

1. **EU AI Act deadline 2 december:** Als Ctac-klanten systemen leveren of beheren die vóór augustus 2026 live gingen, lopen zij mogelijk risico op non-compliance. Dit is een concrete aanleiding voor een korte compliance-scan of klantadviesgesprek — en een propositiekans voor de AI-unit.

2. **Agentic workflows tonen meetbare ROI:** De Anthropic/Rust-casus en het 50M-agents-cijfer van Microsoft normaliseren het gesprek over agentic implementaties in enterprise. Ctac kan dit gebruiken als kapstok in klantgesprekken: niet "wat is een agent?", maar "waar vervangt agent-automatisering uw duurste handmatige stap?"

3. **Security is een verkoopargument geworden:** De toename van AI-specifieke CVE's (coding agents, inference engines, supply chain) maakt een AI-security-audit een reëel dienstverleningspakket. Met een AI engineer in het team kan Ctac hier sneller op reageren dan traditionele IT-auditors.

---

## 📚 Bronnen & verder lezen

- [The Neuron – AI Today 27 November 2026](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-27-2026/)
- [tecadmin.net – November 2026 AI Model Releases](https://tecadmin.net/november-2026-ai-model-releases/)
- [Alice Labs – EU AI Act Timeline 2026](https://alicelabs.ai/en/insights/eu-ai-act-timeline-2026)
- [Cubbbix – AI Regulation November 2026](https://cubbbix.com/blog/ai-regulation-november-2026-global-update)
- [Adversa AI – Copilot RCE CVE-2026-103572](https://adversa.ai/blog/top-ai-coding-agent-security-resources-november-2026/)
- [Mafurad – AI Agent Cyberattacks November 2026](https://www.mafurad.com/blog/ai-agent-cyberattacks-what-changed-in-november-2026-20261121)
- [Storyboard18 – Microsoft Ignite 2026](https://www.storyboard18.com/brand-makers/microsoft-unveils-new-enterprise-ai-agents-and-tools-at-ignite-2026-ws-l-114984.htm)
- [Business Standard – JP Morgan 24 miljoen banen](https://www.business-standard.com/technology/artificial-intelligence/ai-adoption-could-put-24-million-knowledge-worker-jobs-at-risk-jp-morgan-126112700267_1.html)
- [arXiv – StudioBench 2611.28902](https://arxiv.org/abs/2611.28902)
- [BTI Group – AI Cybersecurity Update November 2026](https://www.btigroup.com/post/ai-cybersecurity-update-november-20-2026/)
