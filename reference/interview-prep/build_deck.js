// Protolabs TPM-AI Interview Cheat-Sheet PPTX Generator
// Run: node build_deck.js
const pptxgen = require("pptxgenjs");

const C = {
  navy:    "0B2447",
  navyDk:  "071838",
  teal:    "0891B2",
  tealLt:  "67E8F9",
  amber:   "D97706",
  amberLt: "FEF3C7",
  client:  "1E88E5",
  internal:"7E57C2",
  pricing: "FB8C00",
  mfg:     "43A047",
  bg:      "FFFFFF",
  bgLite:  "F8FAFC",
  ink:     "0F172A",
  ink2:    "334155",
  ink3:    "64748B",
  line:    "E2E8F0",
  muted:   "CBD5E1",
};

const F = {
  h: "Georgia",
  b: "Calibri",
};

// Always create fresh shadow objects — pptxgenjs mutates them
const shadow = () => ({ type: "outer", blur: 8, offset: 2, color: "000000", opacity: 0.08, angle: 135 });

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.3 × 7.5
pres.title = "Protolabs TPM-AI — Interview Cheat Sheet";
pres.author = "Dimos";

// ==========================================================
// SLIDE 1 — TITLE
// ==========================================================
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  // Top accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 13.3, h: 0.15,
    fill: { color: C.teal }, line: { type: "none" }
  });

  // Eyebrow
  s.addText("INTERVIEW CHEAT-SHEET  ·  ROUND 2 WITH TERESA", {
    x: 0.8, y: 1.0, w: 12, h: 0.4,
    fontSize: 12, fontFace: F.b, bold: true,
    color: C.tealLt, charSpacing: 8, margin: 0
  });

  // Title
  s.addText("AI Across Protolabs'\nProduction Manufacturing Flow", {
    x: 0.8, y: 1.6, w: 12, h: 2.0,
    fontSize: 48, fontFace: F.h, bold: true,
    color: "FFFFFF", margin: 0, valign: "top",
    paraSpaceAfter: 6
  });

  // Subtitle
  s.addText("Strategic frame for a 9-stage discussion — one high-value point per stage, framed for maximum impact", {
    x: 0.8, y: 3.9, w: 11, h: 0.8,
    fontSize: 18, fontFace: F.h, italic: true,
    color: C.muted, margin: 0
  });

  // Horizontal divider
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: 5.0, w: 1.5, h: 0.04,
    fill: { color: C.teal }, line: { type: "none" }
  });

  // Three-point promise
  s.addText([
    { text: "9 stages mapped  ·  ", options: { color: C.tealLt, bold: true } },
    { text: "4 strategic buckets  ·  ", options: { color: "FFFFFF" } },
    { text: "1 master frame", options: { color: C.tealLt, bold: true } }
  ], {
    x: 0.8, y: 5.2, w: 12, h: 0.5,
    fontSize: 16, fontFace: F.b, margin: 0
  });

  // Footer strip
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 7.2, w: 13.3, h: 0.3,
    fill: { color: C.navyDk }, line: { type: "none" }
  });
  s.addText("Source process: PL_Production_Manufacturing_EN.pdf   ·   Companion narrative: memoized-questing-sphinx.md", {
    x: 0.8, y: 7.2, w: 12, h: 0.3,
    fontSize: 10, fontFace: F.b,
    color: C.muted, valign: "middle", margin: 0
  });
}

// ==========================================================
// SLIDE 2 — MASTER FRAME
// ==========================================================
{
  const s = pres.addSlide();
  s.background = { color: C.bg };

  // Top accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 13.3, h: 0.15,
    fill: { color: C.navy }, line: { type: "none" }
  });

  // Eyebrow
  s.addText("THE MASTER FRAME", {
    x: 0.8, y: 0.6, w: 10, h: 0.35,
    fontSize: 11, fontFace: F.b, bold: true,
    color: C.teal, charSpacing: 6, margin: 0
  });

  // Title
  s.addText("Three things I want Teresa to remember about me", {
    x: 0.8, y: 1.0, w: 12, h: 0.9,
    fontSize: 32, fontFace: F.h, bold: true,
    color: C.ink, margin: 0
  });

  // Subtitle
  s.addText("Everything on the next nine slides flows from these three commitments. If the conversation gets chaotic, return to one of these.", {
    x: 0.8, y: 2.0, w: 12, h: 0.6,
    fontSize: 14, fontFace: F.b, italic: true,
    color: C.ink3, margin: 0
  });

  // Three cards
  const cards = [
    {
      n: "01",
      color: C.teal,
      title: "This isn't automation — it's the operating system of order-taking",
      body: "The CAD-order pipeline is where every commercial KPI is decided — conversion, margin, lead time, trust. Done right, AI becomes the reason Protolabs stays the fastest digital manufacturer. Done wrong, it's the fastest way to erode trust with both customers and engineers."
    },
    {
      n: "02",
      color: C.amber,
      title: "Engineers are amplified, not bypassed",
      body: "Under EU AI Act, human oversight is a regulatory requirement — not a preference. Engineers move from the routine 80% to the strategic 20%: novel geometry, exotic materials, customer consulting, edge-case judgment. Every override they make trains the next model. They become teachers."
    },
    {
      n: "03",
      color: C.mfg,
      title: "Sequence beats parallelism — one wedge, then compound",
      body: "With four engineers, spreading across five parallel projects is the fastest path to five half-built systems. The CAD order pipeline is the substrate — routing, copilot, CV inspection, learning loop all reuse it. Ship narrow, let it compound, then expand."
    }
  ];

  cards.forEach((card, i) => {
    const x = 0.8 + i * 4.15;
    const y = 2.9;
    const w = 3.85;
    const h = 3.9;

    // Card
    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w, h,
      fill: { color: C.bgLite }, line: { color: C.line, width: 1 },
      shadow: shadow()
    });
    // Top accent
    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w, h: 0.1,
      fill: { color: card.color }, line: { type: "none" }
    });
    // Number
    s.addText(card.n, {
      x: x + 0.3, y: y + 0.3, w: 1, h: 0.6,
      fontSize: 36, fontFace: F.h, bold: true,
      color: card.color, margin: 0
    });
    // Title
    s.addText(card.title, {
      x: x + 0.3, y: y + 1.1, w: w - 0.6, h: 1.4,
      fontSize: 17, fontFace: F.h, bold: true,
      color: C.ink, margin: 0, valign: "top"
    });
    // Body
    s.addText(card.body, {
      x: x + 0.3, y: y + 2.5, w: w - 0.6, h: 1.3,
      fontSize: 11.5, fontFace: F.b,
      color: C.ink2, margin: 0, valign: "top"
    });
  });

  // Bottom callout
  s.addText("Return to these three when the conversation drifts. They're the spine of the narrative.", {
    x: 0.8, y: 7.0, w: 12, h: 0.4,
    fontSize: 11, fontFace: F.b, italic: true,
    color: C.ink3, align: "center", margin: 0
  });
}

// ==========================================================
// STAGE SLIDE HELPER
// ==========================================================
function stage(num, name, bucketColor, bucketLabel, today, lens, topPoint, frame, qText, aText) {
  const s = pres.addSlide();
  s.background = { color: C.bg };

  // Left color bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 0.25, h: 7.5,
    fill: { color: bucketColor }, line: { type: "none" }
  });

  // Stage number circle
  s.addShape(pres.shapes.OVAL, {
    x: 0.6, y: 0.35, w: 0.9, h: 0.9,
    fill: { color: bucketColor }, line: { type: "none" },
    shadow: shadow()
  });
  s.addText(String(num), {
    x: 0.6, y: 0.35, w: 0.9, h: 0.9,
    fontSize: 38, fontFace: F.h, bold: true,
    color: "FFFFFF", align: "center", valign: "middle", margin: 0
  });

  // Stage name
  s.addText(name, {
    x: 1.7, y: 0.35, w: 8.5, h: 0.9,
    fontSize: 28, fontFace: F.h, bold: true,
    color: C.ink, align: "left", valign: "middle", margin: 0
  });

  // Top-right bucket tag
  s.addShape(pres.shapes.RECTANGLE, {
    x: 10.4, y: 0.55, w: 2.5, h: 0.5,
    fill: { color: bucketColor }, line: { type: "none" }
  });
  s.addText(`STAGE ${num} / 9  ·  ${bucketLabel.toUpperCase()}`, {
    x: 10.4, y: 0.55, w: 2.5, h: 0.5,
    fontSize: 9, fontFace: F.b, bold: true,
    color: "FFFFFF", align: "center", valign: "middle",
    charSpacing: 2, margin: 0
  });

  // TODAY strip
  s.addText("TODAY", {
    x: 0.7, y: 1.5, w: 0.8, h: 0.3,
    fontSize: 10, fontFace: F.b, bold: true,
    color: C.ink3, charSpacing: 4, margin: 0
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 1.55, y: 1.65, w: 11.45, h: 0.015,
    fill: { color: C.line }, line: { type: "none" }
  });
  s.addText(today, {
    x: 0.7, y: 1.8, w: 12.3, h: 0.45,
    fontSize: 13, fontFace: F.b, italic: true,
    color: C.ink2, margin: 0, valign: "top"
  });

  // LEFT CONTENT — Strategic Lens
  s.addText("STRATEGIC LENS", {
    x: 0.7, y: 2.45, w: 3, h: 0.3,
    fontSize: 10, fontFace: F.b, bold: true,
    color: bucketColor, charSpacing: 4, margin: 0
  });
  s.addText(lens, {
    x: 0.7, y: 2.8, w: 7.7, h: 0.95,
    fontSize: 13, fontFace: F.b,
    color: C.ink2, margin: 0, valign: "top"
  });

  // TOP POINT — featured box
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.7, y: 3.85, w: 7.7, h: 1.85,
    fill: { color: C.bgLite }, line: { color: C.line, width: 1 },
    shadow: shadow()
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.7, y: 3.85, w: 0.14, h: 1.85,
    fill: { color: bucketColor }, line: { type: "none" }
  });
  s.addText("THE TOP POINT TO RAISE", {
    x: 1.0, y: 4.0, w: 5, h: 0.3,
    fontSize: 10, fontFace: F.b, bold: true,
    color: bucketColor, charSpacing: 4, margin: 0
  });
  s.addText(topPoint, {
    x: 1.0, y: 4.3, w: 7.3, h: 1.35,
    fontSize: 14.5, fontFace: F.b, bold: true,
    color: C.ink, margin: 0, valign: "top"
  });

  // FRAME FOR IMPACT — quote
  s.addText("FRAME FOR IMPACT", {
    x: 0.7, y: 5.85, w: 3, h: 0.3,
    fontSize: 10, fontFace: F.b, bold: true,
    color: C.amber, charSpacing: 4, margin: 0
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.7, y: 6.18, w: 0.1, h: 0.85,
    fill: { color: C.amber }, line: { type: "none" }
  });
  s.addText(`"${frame}"`, {
    x: 0.95, y: 6.15, w: 7.45, h: 0.9,
    fontSize: 13, fontFace: F.h, italic: true,
    color: C.ink2, margin: 0, valign: "top"
  });

  // RIGHT — Anticipated Q&A
  s.addShape(pres.shapes.RECTANGLE, {
    x: 8.7, y: 2.45, w: 4.3, h: 4.6,
    fill: { color: C.navy }, line: { type: "none" },
    shadow: shadow()
  });
  s.addText("IF TERESA ASKS", {
    x: 8.9, y: 2.6, w: 4, h: 0.3,
    fontSize: 10, fontFace: F.b, bold: true,
    color: C.tealLt, charSpacing: 4, margin: 0
  });
  s.addText(qText, {
    x: 8.9, y: 2.95, w: 4, h: 1.35,
    fontSize: 13, fontFace: F.b, italic: true,
    color: C.muted, margin: 0, valign: "top"
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 8.9, y: 4.5, w: 4, h: 0.015,
    fill: { color: C.teal }, line: { type: "none" }
  });
  s.addText("YOUR ANCHOR RESPONSE", {
    x: 8.9, y: 4.6, w: 4, h: 0.3,
    fontSize: 10, fontFace: F.b, bold: true,
    color: C.tealLt, charSpacing: 4, margin: 0
  });
  s.addText(aText, {
    x: 8.9, y: 4.95, w: 4, h: 2.0,
    fontSize: 12, fontFace: F.b,
    color: "FFFFFF", margin: 0, valign: "top"
  });

  // Footer
  s.addText(`${num} / 9`, {
    x: 0.7, y: 7.2, w: 1, h: 0.25,
    fontSize: 9, fontFace: F.b,
    color: C.ink3, align: "left", margin: 0
  });
  s.addText("Protolabs TPM-AI  ·  Interview Cheat Sheet", {
    x: 6, y: 7.2, w: 7, h: 0.25,
    fontSize: 9, fontFace: F.b,
    color: C.ink3, align: "right", margin: 0
  });
}

// ==========================================================
// STAGE SLIDES 3–11
// ==========================================================

stage(1, "Start Your Project", C.client, "Client Edge",
  "Customer contacts production team or uploads 2D/3D CAD files to the platform.",
  "The first 30 seconds set the perception of Protolabs as AI-native. Most competitors still force customers to know exactly what they want before the platform will respond. That's a conversion leak.",
  "Multimodal RFQ ingest — accept CAD, sketch, PDF, email, or photo, and convert anything to a structured Order Object. Meet the customer with whatever they have.",
  "Lower the friction to 'yes.' A mechanical engineer with 10 minutes and a rough drawing should leave with a real answer — not another form to fill out.",
  "Isn't multimodal intake just a chatbot with extra steps?",
  "No — it's a structured extraction layer. LLM turns unstructured input into a validated Order Object that every downstream layer consumes. The difference between a nice demo and an actual pipeline."
);

stage(2, "Get Expert Assistance", C.internal, "Internal Ops",
  "Applications engineers work with customers to optimize projects for quality, batch scheduling, and pricing.",
  "This is the stage where engineer careers are decided. Also the highest-leverage trust-building moment — if engineers see hours of their week freed up here, they become advocates.",
  "Engineer copilot — LLM drafts customer responses grounded in the KB; engineer reviews and sends in seconds. Fastest visible win for the team you need on-side.",
  "The AI becomes their assistant, not their replacement. Hours back within a week of go-live. That's how you earn the right to ship anything bigger.",
  "Won't the engineers resent AI drafting their work?",
  "Not if they own the final word. Frame it as 'your draft got written while you were in the meeting.' That's time back — not oversight. I'd measure adoption as a voluntary metric, not mandated."
);

stage(3, "Assess Production Order", C.mfg, "Manufacturing",
  "Best production solution found across in-house factories and supplier network to meet budget, quantity, and compliance needs.",
  "This is the single most under-rated opportunity in the portfolio. Protolabs' biggest unmatched asset is the manufacturing network — and today it's routed by rules, not by ML learning from outcomes.",
  "ML factory and partner routing — learns from quality history, on-time rate, capability fit, capacity, geography, and certifications per partner per part-type. Impossible to replicate without the network.",
  "This is where I'd spend the strategic-bet budget. Competitors cannot copy it because they don't have the data. Every month it runs, the moat deepens.",
  "How do you train it when routing labels are weak?",
  "Use historical quote-to-actual outcomes as weak supervision — partners with better on-time rates and lower scrap get rewarded. Active learning tightens it over time. Don't need pristine labels to start compounding."
);

stage(4, "Finalize, Approve, Place Order", C.pricing, "Pricing & Quote",
  "Customer submits order; production is initiated either in-house or through a manufacturing partner.",
  "Pricing is where 1–3 percentage points of margin are typically left on the table. Every closed order funds the next version of the model; every lost order tells you how to reprice next time.",
  "Dynamic pricing with confidence-aware guardrails, a quote-optimization slider for customers, and an auto-learning loop from every quote outcome back into the pricing model.",
  "Every order is both revenue and training data. This is the one bucket that self-improves — accumulating compounding advantage without shipping new features.",
  "Isn't dynamic pricing risky for B2B relationships?",
  "Only if unguarded. Tier-aware caps, no personalized pricing for the same customer within a window, full transparency on what drives the price. The algorithm optimizes within boundaries humans set — not against the customer."
);

stage(5, "Get Sample Parts (Optional)", C.mfg, "Manufacturing",
  "Before production begins, sample parts can be sent to the customer for final approval.",
  "This is the highest-stakes trust moment before signing a multi-hundred-thousand or million-part production contract. Failed sample runs kill deals quietly — and the PM never hears why.",
  "Predictive yield model that pre-tunes process parameters to pass first-time, combined with AI-generated First Article Inspection reports using vision-based dimensional measurement.",
  "First-pass yield on samples is effectively your close rate on production. Instrumenting it compounds trust at the most fragile moment in the entire funnel — right before the signature.",
  "Is predictive yield actually achievable with current data?",
  "Yes. Per-process physics plus historical run data gives you a process-window map. The model predicts where this specific part sits inside that window and pre-tunes machine parameters. Not speculative — applied statistics with ML on top."
);

stage(6, "Proceed with Production", C.mfg, "Manufacturing",
  "Once parts are approved, batch or full production begins.",
  "Most AI PMs stop at the software stack and treat the factory floor as a black box. Real industrial AI extends onto the machines themselves. Going deep here is a credibility signal — I know where cents-per-part are actually won or lost.",
  "Adaptive process control — RL-based micro-adjustment of machine parameters in real time — plus predictive maintenance for tool wear and smart scheduling across the network.",
  "The factory floor is where the economics actually happen. I'm not treating manufacturing as a black box. Compounding margin lives on the machine, not in the model.",
  "Can we really retrofit RL onto existing production machines?",
  "Don't start with RL. Start with statistical process control — use it to build the sensor and data infrastructure, prove value on anomaly detection, then layer RL onto machines where payback justifies it. Sequenced, not speculative."
);

stage(7, "Assure Batch Quality", C.mfg, "Manufacturing",
  "Parts are tested within each batch for strict quality-control adherence during production.",
  "Quality control delivers the clearest cents-per-part savings AND the clearest regulatory defensibility under EU AI Act. Start with the process that has the worst current scrap rate — the ROI case writes itself.",
  "Computer-vision inline inspection with in-process anomaly detection on sensor streams, plus auto-generated Certificates of Conformity and traceability records for every batch.",
  "Pick the process with the worst current scrap rate. Measurable per-part savings in two quarters. Clean case for scaling. And a clean regulatory story — human oversight kept in the loop by design.",
  "What if computer vision misses a defect a human would catch?",
  "Hybrid deployment — CV flags and grades; human QC confirms. Model learns from human corrections every week. We never remove the human in year one. It's augmentation, and under EU AI Act for safety-critical parts, it stays that way by regulation."
);

stage(8, "Warehouse Your Batches (Optional)", C.client, "Client Edge",
  "If additional batches are not immediately needed, parts can be warehoused at one of Protolabs' facilities.",
  "Inventory optimization is a hidden expansion lever. Every existing customer is a demand-forecast dataset we're currently wasting — expansion revenue at near-zero customer acquisition cost.",
  "Reorder prediction with opt-in customer visibility, just-in-time batch release for warehoused parts, and demand forecasting to inform warehouse-placement optimization across the network.",
  "Expansion revenue without new logos. Every existing customer is a demand-forecast dataset. Predict their reorders before they ask — and every relationship gets stickier.",
  "What about customers who don't want us predicting their demand?",
  "Opt-in only, and framed customer-facing as a service: 'based on your order history, here's when you'd likely need a reorder.' It's a dashboard, not surveillance. Transparency is the entire design principle."
);

stage(9, "Ship Your Parts", C.internal, "Internal Ops",
  "Advanced logistics requirements accommodated — freight forwarding and delivery with specific carriers.",
  "Last-mile is where customer experience is actually decided. Most B2B under-invests because it feels like 'just logistics' — but a delayed shipment costs more than its freight. It costs the next reorder.",
  "Carrier and route ML based on cost, time, reliability, and carbon footprint — plus proactive delay prediction and customs auto-classification that fires paperwork before humans notice.",
  "A delayed shipment costs more than its freight — it costs the next order. AI here converts 'we're sorry' calls into 'here's what we're already doing about it' calls.",
  "Isn't this just better logistics software, not really AI?",
  "Both — and the distinction matters. The AI is in the prediction: which shipments will slip, which need intervention, which customs filings are at risk. The rest is orchestration. You need both; pretending one is the whole answer is the common mistake."
);

// ==========================================================
// SLIDE 12 — STRATEGIC SEQUENCING
// ==========================================================
{
  const s = pres.addSlide();
  s.background = { color: C.bgLite };

  // Top accent bar
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 13.3, h: 0.15,
    fill: { color: C.navy }, line: { type: "none" }
  });

  // Eyebrow
  s.addText("WHERE I WOULD START — AND WHY", {
    x: 0.8, y: 0.6, w: 10, h: 0.35,
    fontSize: 11, fontFace: F.b, bold: true,
    color: C.teal, charSpacing: 6, margin: 0
  });

  // Title
  s.addText("Strategic Sequencing: One Wedge, Then Compound", {
    x: 0.8, y: 1.0, w: 12, h: 0.9,
    fontSize: 30, fontFace: F.h, bold: true,
    color: C.ink, margin: 0
  });

  s.addText("Spreading four engineers across five parallel projects is the fastest path to five half-built systems. Each of these unlocks the next.", {
    x: 0.8, y: 2.0, w: 12, h: 0.6,
    fontSize: 14, fontFace: F.b, italic: true,
    color: C.ink3, margin: 0
  });

  // 5 numbered steps
  const steps = [
    { n: "1", t: "CAD Order Pipeline", s: "The substrate — every downstream use case reuses its data flywheel, override UX, routing, and audit trail.", c: C.navy, star: false },
    { n: "2", t: "ML Partner Routing", s: "Protolabs' unmatched asset. Competitors can't copy without the network. Moat deepens monthly.", c: C.mfg, star: true },
    { n: "3", t: "Engineer Copilot", s: "Fastest visible win for the team whose trust you need. Turns skeptics into advocates in weeks.", c: C.internal, star: false },
    { n: "4", t: "CV Inline Inspection", s: "Pick the process with the worst scrap rate. Measurable cost-per-part savings in 2 quarters.", c: C.mfg, star: false },
    { n: "5", t: "Quote→Actual Loop", s: "Closes the learning cycle. Pricing model self-improves every month without new features.", c: C.pricing, star: false },
  ];

  steps.forEach((step, i) => {
    const x = 0.7 + i * 2.5;
    const y = 3.0;
    const w = 2.35;
    const h = 3.7;

    // Card
    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w, h,
      fill: { color: "FFFFFF" }, line: { color: C.line, width: 1 },
      shadow: shadow()
    });
    // Top color bar
    s.addShape(pres.shapes.RECTANGLE, {
      x, y, w, h: 0.12,
      fill: { color: step.c }, line: { type: "none" }
    });
    // Number
    s.addShape(pres.shapes.OVAL, {
      x: x + (w - 0.9) / 2, y: y + 0.4, w: 0.9, h: 0.9,
      fill: { color: step.c }, line: { type: "none" }
    });
    s.addText(step.n, {
      x: x + (w - 0.9) / 2, y: y + 0.4, w: 0.9, h: 0.9,
      fontSize: 34, fontFace: F.h, bold: true,
      color: "FFFFFF", align: "center", valign: "middle", margin: 0
    });
    // Title
    s.addText(step.t + (step.star ? "  ★" : ""), {
      x: x + 0.15, y: y + 1.5, w: w - 0.3, h: 0.9,
      fontSize: 16, fontFace: F.h, bold: true,
      color: C.ink, align: "center", valign: "top", margin: 0
    });
    // Description
    s.addText(step.s, {
      x: x + 0.2, y: y + 2.45, w: w - 0.4, h: 1.2,
      fontSize: 10.5, fontFace: F.b,
      color: C.ink2, align: "left", valign: "top", margin: 0
    });

    // Arrow to next (except last)
    if (i < steps.length - 1) {
      s.addText("→", {
        x: x + w - 0.05, y: y + 1.55, w: 0.3, h: 0.5,
        fontSize: 24, fontFace: F.b, bold: true,
        color: C.ink3, align: "center", valign: "middle", margin: 0
      });
    }
  });

  // Bottom callout strip
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.7, y: 6.85, w: 11.9, h: 0.5,
    fill: { color: C.amberLt }, line: { color: C.amber, width: 1 }
  });
  s.addText([
    { text: "Sequence beats parallelism. ", options: { bold: true, color: "78350F" } },
    { text: "Each unlocks the next — and the foundation compounds long after I'm shipped on something else.", options: { color: "78350F" } }
  ], {
    x: 0.7, y: 6.85, w: 11.9, h: 0.5,
    fontSize: 13, fontFace: F.h, italic: true,
    align: "center", valign: "middle", margin: 0
  });
}

// ==========================================================
// SLIDE 13 — CLOSING FRAME
// ==========================================================
{
  const s = pres.addSlide();
  s.background = { color: C.navy };

  // Top accent
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 13.3, h: 0.15,
    fill: { color: C.teal }, line: { type: "none" }
  });

  // Eyebrow
  s.addText("IF TERESA REMEMBERS ONLY ONE THING", {
    x: 0.8, y: 1.2, w: 12, h: 0.4,
    fontSize: 12, fontFace: F.b, bold: true,
    color: C.tealLt, charSpacing: 8, align: "center", margin: 0
  });

  // Big quote opening mark
  s.addText("\u201C", {
    x: 0.8, y: 1.6, w: 2, h: 1.5,
    fontSize: 120, fontFace: F.h, bold: true,
    color: C.teal, align: "left", valign: "top", margin: 0
  });

  // Main quote
  s.addText("My job isn't to ship AI.\nMy job is to make Protolabs measurably faster\nand more trusted than anyone else in digital manufacturing —\nand to do it in a way engineers want to use,\ncustomers trust, and regulators can audit.", {
    x: 1.4, y: 2.1, w: 10.5, h: 3.4,
    fontSize: 24, fontFace: F.h, italic: true,
    color: "FFFFFF", align: "center", valign: "middle", margin: 0,
    paraSpaceAfter: 4
  });

  // Signature line
  s.addShape(pres.shapes.RECTANGLE, {
    x: 5.9, y: 5.7, w: 1.5, h: 0.03,
    fill: { color: C.teal }, line: { type: "none" }
  });

  // The anchor line
  s.addText("You're not being bypassed. You're being amplified —", {
    x: 0.8, y: 5.95, w: 12, h: 0.45,
    fontSize: 16, fontFace: F.h, bold: true,
    color: C.tealLt, align: "center", margin: 0
  });
  s.addText("and you're becoming the people who decide what good looks like.", {
    x: 0.8, y: 6.35, w: 12, h: 0.45,
    fontSize: 16, fontFace: F.h, bold: true,
    color: C.tealLt, align: "center", margin: 0
  });

  // Footer strip
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 7.2, w: 13.3, h: 0.3,
    fill: { color: C.navyDk }, line: { type: "none" }
  });
  s.addText("Protolabs TPM-AI  ·  Round 2 with Teresa  ·  Interview cheat-sheet", {
    x: 0.8, y: 7.2, w: 12, h: 0.3,
    fontSize: 10, fontFace: F.b,
    color: C.muted, align: "center", valign: "middle", margin: 0
  });
}

// ==========================================================
// WRITE FILE
// ==========================================================
pres.writeFile({ fileName: "C:\\Users\\dimos\\ProtoLab\\interview_presentation.pptx" })
  .then(fn => console.log("Wrote:", fn))
  .catch(e => { console.error(e); process.exit(1); });
