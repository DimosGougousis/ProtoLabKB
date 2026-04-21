---
type: skill
name: ProtoLabs Router
id: protolabs-router
purpose: Route user prompts to appropriate specialist agents based on process, mode, and vertical classification
version: 1.0
---

# ProtoLabs Router Skill

## Purpose

This skill provides the routing logic to classify user prompts and route them to the appropriate specialist agent in the ProtoLabs Product Office system.

## Classification Dimensions

### 1. Process Classification

| Process | Keywords | Agent |
|---------|----------|-------|
| CNC Machining | cnc, machining, machined, mill, milling, lathe, turning, drilled, tapped, threaded, aluminum, steel, titanium, milled, turned | cnc-machining |
| Injection Molding | injection, molded, mould, plastic, thermoplastic, polypropylene, pp, abs, polycarbonate, pc, nylon, draft, undercut, gate, runner, sprue, lsr, silicone | injection-molding |
| Sheet Metal | sheet, metal, fabricated, fabrication, bend, flange, punch, laser, cut, brake, gauge, formed | sheet-metal |
| 3D Printing | 3d print, printed, additive, sla, sls, mjf, fdm, dmls, polyjet, layer, orientation, support | 3d-printing |
| Materials | material, select, choose, compare, alternative, properties, aluminum, steel, titanium, plastic, polymer | materials-selection |

### 2. Mode Classification

| Mode | Keywords | Action |
|------|----------|--------|
| DFM Review | dfm, design for manufacturing, review, evaluate, check, validate, can you make, manufacturable, issues, problems, concerns, analyze | Evaluate design against rules |
| Q&A | what, how, why, when, minimum, maximum, recommend, suggest, compare, difference between, explain, guide | Answer knowledge-based question |

### 3. Vertical Classification (Optional)

| Vertical | Keywords | Agent |
|----------|----------|-------|
| Aerospace | aerospace, aircraft, aviation, flight, as9100, space, satellite, structural, lightweight, defense | vertical-aerospace |
| Medical | medical, healthcare, biocompatible, iso 13485, fda, surgical, implant, device, biocompatibility | vertical-medical |
| Automotive/EV | automotive, car, vehicle, ev, electric vehicle, powertrain, battery, motor, lightweight, transportation | vertical-automotive-ev |

## Routing Procedure

```
User Prompt
    ↓
1. EXTRACT KEYWORDS
   - Scan for process keywords
   - Scan for mode keywords  
   - Scan for vertical keywords
    ↓
2. CLASSIFY
   - Process: {cnc | injection | sheet-metal | 3d-printing | materials}
   - Mode: {dfm-review | qa}
   - Vertical: {aerospace | medical | automotive | none}
    ↓
3. RESOLVE AMBIGUITY
   - If multiple processes detected → ask clarifying question
   - If no process detected → default to router help message
   - If mode unclear → default to Q&A
    ↓
4. ROUTE
   - Load specialist agent for determined process
   - If vertical specified, also load vertical agent
   - Pass classification to agent
    ↓
5. EXECUTE
   - Agent loads its KB files
   - Performs DFM review or answers Q&A
   - Cites sources from KB files
```

## Ambiguity Resolution Examples

| Prompt | Detected | Resolution |
|--------|----------|------------|
| "Can you machine this aluminum bracket?" | Process: CNC, Mode: DFM | Route to cnc-machining |
| "What's the minimum wall thickness for PP?" | Process: Injection, Mode: Q&A | Route to injection-molding |
| "Should I 3D print or CNC this aerospace part?" | Process: 3D-print + CNC, Vertical: Aerospace | Load both + aerospace, provide comparison |
| "Is this part manufacturable?" | Mode: DFM, Process: unknown | Ask clarifying question about process |

## Output Format

After routing, the specialist agent will produce output using:
- `templates/dfm-eval-report.md` for DFM reviews
- `templates/qa-response.md` for Q&A responses

## Source Citation

Every claim must cite:
- The cached KB file path
- The original ProtoLabs URL from the file's `source_url` frontmatter

Format: `[knowledge/<folder>/<file>.md → <source_url>]`
