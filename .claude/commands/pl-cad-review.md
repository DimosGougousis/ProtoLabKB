---
type: command
name: pl-cad-review
description: Parse CAD file and generate DFM evaluation with 2D/3D visualizations
usage: /pl-cad-review <path-to-cad-file> [options]
---

# /pl-cad-review

Parse CAD files (STEP, STL, OBJ, 3MF) and generate comprehensive DFM evaluation with 2D/3D visualizations.

## Usage

```
/pl-cad-review part.step                           # Basic CAD review
/pl-cad-review part.stl --process cnc               # Force CNC process analysis
/pl-cad-review part.step --vertical aerospace       # Aerospace compliance
/pl-cad-review part.step --material aluminum-6061    # Specify material
/pl-cad-review part.step --output ./reports/       # Custom output directory
/pl-cad-review part.step --no-3d                    # Skip 3D viewer (faster)
```

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--process` | Force specific process (cnc, injection, 3d-printing, sheet-metal) | Auto-detect |
| `--vertical` | Industry vertical (aerospace, medical, automotive) | None |
| `--material` | Material specification | Auto-detect |
| `--output` | Output directory for reports and images | `./cad-output/` |
| `--no-3d` | Skip 3D interactive viewer generation | False |
| `--no-2d` | Skip 2D view generation | False |
| `--quality` | Render quality (low, medium, high) | medium |

## Workflow

```
User CAD File
     │
     ▼
┌─────────────────────────┐
│ 1. CAD Parser Agent      │
│    • Validate format     │
│    • Extract geometry    │
│    • Detect features     │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ 2. Visualization Gen     │
│    • 2D orthographic     │
│    • 3D interactive      │
│    • Feature highlighting  │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ 3. DFM Router            │
│    • Classify process    │
│    • Detect vertical     │
│    • Set regulated flag  │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ 4. Specialist Agent      │
│    • Apply DFM rules     │
│    • Evaluate features   │
│    • Generate score      │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ 5. Report Generator      │
│    • Combine all data    │
│    • Insert images       │
│    • Output PDF/HTML     │
└─────────────────────────┘
```

## Output Structure

```
cad-output/
├── report.html              # Main report with embedded images
├── report.pdf               # PDF version
├── geometry.json            # Structured geometry data
├── features.json            # Detected features
├── dfm-analysis.json        # DFM evaluation results
├── images/
│   ├── front.png            # Front orthographic view
│   ├── top.png              # Top orthographic view
│   ├── side.png             # Side orthographic view
│   ├── iso.png              # Isometric view
│   ├── section-front.png    # Section view (if requested)
│   └── detail-a.png         # Detail view (if requested)
└── viewer/
    └── index.html           # Interactive 3D viewer
```

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `UNSUPPORTED_FORMAT` | File extension not recognized | Convert to STEP, STL, or OBJ |
| `CORRUPT_FILE` | File data is invalid | Check source file, re-export |
| `EMPTY_GEOMETRY` | No valid geometry found | Verify file contains solid |
| `PARSE_ERROR` | Parser failed on specific entity | Try different STEP schema |
| `MEMORY_ERROR` | File too large | Simplify geometry or use streaming |

## Integration with Existing Commands

The `/pl-cad-review` command integrates with existing commands:

```
/pl-cad-review part.step
    ↓
[Generates geometry.json, images, viewer]
    ↓
/pl-dfm-review part.step  # Can now use parsed data
    ↓
[Uses geometry.json instead of re-parsing]
```

## Source Citation

When providing CAD review results, cite:
- CAD Parser Agent — `agents/cad-parser.agent.md`
- Feature Recognition — `knowledge/cad/feature-recognition.md`
- Visualization Standards — `knowledge/cad/visualization-best-practices.md`

---
*CAD Review Command for ProtoLabs Product Office*
