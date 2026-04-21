# ProtoLabs Product Office — CLAUDE.md

> Entry point for the ProtoLabs knowledge-base system. This file defines the agent registry, routing keywords, and progressive-loading rules.

## Agent Registry

| Agent ID | File | Purpose | Keywords |
|----------|------|---------|----------|
| `dfm-router` | `agents/dfm-router.agent.md` | Intent classification & routing | route, classify, parse |
| `cnc-machining` | `agents/cnc-machining.agent.md` | CNC DFM evaluation | cnc, machining, milled, turned, drill, tap, mill, lathe, aluminum, steel, titanium |
| `injection-molding` | `agents/injection-molding.agent.md` | Injection molding DFM | injection, molding, mould, plastic, thermoplastic, pp, abs, pc, nylon, draft, undercut, gate, runner |
| `sheet-metal` | `agents/sheet-metal.agent.md` | Sheet metal DFM | sheet, metal, fab, fabrication, bend, flange, punch, laser, cut, aluminum sheet, steel sheet |
| `3d-printing` | `agents/3d-printing.agent.md` | 3D printing DFM | 3d print, additive, sla, sls, mjf, fdm, dmls, polyjet, stereolithography, layer |
| `materials-selection` | `agents/materials-selection.agent.md` | Material recommendations | material, select, choose, aluminum, steel, titanium, plastic, polymer, compare, alternative |
| `vertical-aerospace` | `agents/vertical-aerospace.agent.md` | Aerospace-specific guidance | aerospace, aircraft, aviation, flight, as9100, lightweight, structural |
| `vertical-medical` | `agents/vertical-medical.agent.md` | Medical device guidance | medical, healthcare, biocompatible, iso 13485, fda, device, implant |
| `vertical-automotive-ev` | `agents/vertical-automotive-ev.agent.md` | Automotive/EV guidance | automotive, car, vehicle, ev, electric, lightweight, powertrain, battery |
| `trends-strategy` | `agents/trends-strategy.agent.md` | Strategic trend analysis | trend, strategy, industry 4.0, innovation, future, market, forecast |

## Routing Keywords

### Process Detection
- **CNC**: cnc, machining, machined, mill, milling, lathe, turning, drilled, tapped, threaded, aluminum 6061, steel 1018, titanium
- **Injection Molding**: injection, molded, mould, plastic, thermoplastic, polypropylene, abs, polycarbonate, nylon, draft angle, wall thickness, sink, warp, gate, runner, sprue
- **Sheet Metal**: sheet, metal, fabricated, bend, flange, punch, laser cut, brake, aluminum sheet, steel sheet, gauge
- **3D Printing**: 3d print, printed, additive, sla, sls, mjf, fdm, dmls, polyjet, layer height, support, orientation, resolution

### Mode Detection
- **Design Evaluation**: dfm, design for manufacturing, review, evaluate, check, validate, can you make, manufacturable, issues, problems, concerns
- **Q&A**: what, how, why, when, minimum, maximum, recommend, suggest, compare, difference between

### Vertical Detection
- **Aerospace**: aerospace, aircraft, aviation, flight, as9100, space, satellite, structural, lightweight
- **Medical**: medical, healthcare, biocompatible, iso 13485, fda, surgical, implant, device
- **Automotive/EV**: automotive, car, vehicle, ev, electric vehicle, powertrain, battery, motor, lightweight

### Compliance & Export Control Keywords (Sets regulated=true)
- **ITAR**: itar, defense, military, munitions, usml, export control, deemed export, technical data
- **EAR**: ear, export administration, eccn, dual-use, commerce control list, restricted party
- **Aerospace Certifications**: as9100, as9102, faa, far 25, nadcap, flight critical, aircraft certification
- **Medical Certifications**: iso 13485, fda, 510k, pma, biocompatible, usp class vi, iso 10993, mdr, udi
- **Automotive Certifications**: iatf 16949, ppap, apqp, fmea, spc, msa, control plan, ts 16949
- **Cybersecurity**: nist, cmmc, 800-171, cybersecurity, cyber, security framework, cui, fci
- **Environmental**: rohs, reach, conflict minerals, 3tg, hazardous substance, environmental compliance
- **AI Governance**: eu ai act, ai act, ai governance, algorithmic, high-risk ai, ai conformity, ce marking ai
- **Data Protection**: gdpr, data protection, privacy, personal data, data subject rights, breach notification

## Progressive Loading Rule

When a user prompt is received:

1. **Parse** the prompt for keywords (process, mode, vertical)
2. **Load** `agents/dfm-router.agent.md` to classify intent
3. **Route** to the appropriate specialist agent based on classification
4. **Load** only the required KB files specified in the agent's `loads:` frontmatter
5. **Execute** the agent's procedure (design eval or Q&A)
6. **Emit** output using the appropriate template with source citations

## Source Citation Format

Every claim must cite:
- The cached KB file: `knowledge/<folder>/<article>.md`
- The original ProtoLabs URL from the file's `source_url` frontmatter

Example: "Minimum hole diameter for CNC drilling is 0.5mm [knowledge/cnc-machining/mastering-complex-features.md → https://www.protolabs.com/resources/design-tips/mastering-complex-features-on-machined-parts/]"

## Commands Available

| Command | Description |
|---------|-------------|
| `/pl-dfm-review <path\|description>` | Evaluate a part design against ProtoLabs DFM rules |
| `/pl-ask <question>` | Ask a manufacturing question grounded in ProtoLabs guidance |
| `/pl-refresh-kb [folder]` | Refresh cached knowledge base articles |

## See Also

- `PLAN.md` — Full implementation architecture
- `TODO.md` — Delivery checklist
- `agents/` — Specialist agent definitions
- `knowledge/` — Cached ProtoLabs articles
- `templates/` — Output templates
