import { AgentDefinition, loadAgents } from './agents';

export interface RouteResult {
  agentIds: string[];
  mode: 'dfm-review' | 'qa' | 'unknown';
  vertical: string | null;
  confidence: number;
}

const PROCESS_KEYWORDS: Record<string, string[]> = {
  'cnc-machining': ['cnc', 'machining', 'machined', 'mill', 'milling', 'lathe', 'turning', 'drilled', 'tapped', 'threaded', 'aluminum 6061', 'steel 1018', 'titanium', '5-axis', 'end mill'],
  'injection-molding': ['injection', 'molded', 'mould', 'plastic', 'thermoplastic', 'polypropylene', 'pp', 'abs', 'polycarbonate', 'pc', 'nylon', 'draft angle', 'wall thickness', 'sink', 'warp', 'gate', 'runner', 'sprue', 'lsr', 'silicone'],
  'sheet-metal': ['sheet', 'metal', 'fabricated', 'fabrication', 'bend', 'flange', 'punch', 'laser cut', 'brake', 'aluminum sheet', 'steel sheet', 'gauge', 'formed'],
  '3d-printing': ['3d print', 'printed', 'additive', 'sla', 'sls', 'mjf', 'fdm', 'dmls', 'polyjet', 'layer height', 'support', 'orientation', 'resolution'],
  'materials-selection': ['material', 'select', 'choose', 'compare', 'alternative', 'properties', 'polymer'],
};

const MODE_KEYWORDS = {
  'dfm-review': ['dfm', 'design for manufacturing', 'review', 'evaluate', 'check', 'validate', 'can you make', 'manufacturable', 'issues', 'problems', 'concerns', 'analyze'],
  'qa': ['what', 'how', 'why', 'when', 'minimum', 'maximum', 'recommend', 'suggest', 'compare', 'difference between', 'explain', 'guide'],
};

const VERTICAL_KEYWORDS: Record<string, string[]> = {
  'vertical-aerospace': ['aerospace', 'aircraft', 'aviation', 'flight', 'as9100', 'space', 'satellite', 'structural', 'lightweight', 'defense'],
  'vertical-medical': ['medical', 'healthcare', 'biocompatible', 'iso 13485', 'fda', 'surgical', 'implant', 'device', 'biocompatibility'],
  'vertical-automotive-ev': ['automotive', 'car', 'vehicle', 'ev', 'electric vehicle', 'powertrain', 'battery', 'motor', 'transportation'],
};

const CHANGE_MGMT_KEYWORDS = ['change management', 'cobot', 'collaborative robot', 'resistant', 'adoption', 'knowledge transfer', 'workforce transformation', 'organizational change', 'engineer resistance', 'ai training', 'digital adoption', 'behavioral change'];

const FUNNEL_INTAKE_KEYWORDS = [
  'funnel intake', 'use case canvas', '6-box canvas', 'workshop prep', 'intake assessment',
  'pl-funnel-intake', 'onboard', 'new use case', 'evaluate use case', 'use case evaluation',
  'change readiness', 'data readiness', 'jtbd', 'jobs to be done', 'rice scoring',
  'moscow', 'cost of not doing', 'roi hypothesis', 'stakeholder journey', 'raci',
  'data engineering', 'compliance mapping', 'eu ai act risk class', 'nist ai rmf',
  'iso 42001', 'working with machines', 'autonomy level', 'discovery sprint',
  'rat first', 'riskiest assumption test', 'feasibility probe', 'solution architecture',
  'build vs buy', 'experiment plan', 'competitive analysis', 'proprietary model',
  'data flywheel', 'historical data', 'self-learning loop',
];

function scoreKeywords(text: string, keywordMap: Record<string, string[]>): Record<string, number> {
  const lower = text.toLowerCase();
  const scores: Record<string, number> = {};

  for (const [key, keywords] of Object.entries(keywordMap)) {
    scores[key] = keywords.reduce((sum, kw) => {
      const regex = new RegExp(kw.toLowerCase().replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
      const matches = lower.match(regex);
      return sum + (matches ? matches.length : 0);
    }, 0);
  }

  return scores;
}

export function routePrompt(prompt: string): RouteResult {
  const lower = prompt.toLowerCase();

  // 1. Check for change management (highest priority per CLAUDE.md)
  const hasChangeMgmt = CHANGE_MGMT_KEYWORDS.some(kw => lower.includes(kw.toLowerCase()));
  if (hasChangeMgmt) {
    return {
      agentIds: ['change-management-orchestrator'],
      mode: 'qa',
      vertical: null,
      confidence: 0.9,
    };
  }

  // 2. Check for funnel intake (high priority — product management workflow)
  const hasFunnelIntake = FUNNEL_INTAKE_KEYWORDS.some(kw => lower.includes(kw.toLowerCase()));
  if (hasFunnelIntake) {
    return {
      agentIds: ['funnel-intake'],
      mode: 'qa',
      vertical: null,
      confidence: 0.85,
    };
  }

  // 3. Check for CAD/copilot keywords
  const cadKeywords = ['text-to-cad', 'b-rep', 'generative design', 'topology', 'cad import', 'step', 'iges', 'stl', 'obj', 'mesh', 'feature recognition', 'cad analysis', 'geometry'];
  const hasCad = cadKeywords.some(kw => lower.includes(kw.toLowerCase()));

  // 4. Score processes
  const processScores = scoreKeywords(prompt, PROCESS_KEYWORDS);
  const sortedProcesses = Object.entries(processScores)
    .filter(([, score]) => score > 0)
    .sort((a, b) => b[1] - a[1]);

  // 5. Score mode
  const modeScores = scoreKeywords(prompt, MODE_KEYWORDS);
  const mode = (Object.entries(modeScores).sort((a, b) => b[1] - a[1])[0]?.[0] as RouteResult['mode']) || 'unknown';

  // 6. Score verticals
  const verticalScores = scoreKeywords(prompt, VERTICAL_KEYWORDS);
  const topVertical = Object.entries(verticalScores)
    .filter(([, score]) => score > 0)
    .sort((a, b) => b[1] - a[1])[0]?.[0] || null;

  // 7. Build agent list
  const agentIds: string[] = [];

  if (hasCad) {
    agentIds.push('cad-copilot');
  }

  if (sortedProcesses.length > 0) {
    if (sortedProcesses.length === 1 || sortedProcesses[0][1] > sortedProcesses[1][1] * 1.5) {
      agentIds.push(sortedProcesses[0][0]);
    } else {
      agentIds.push(sortedProcesses[0][0], sortedProcesses[1][0]);
    }
  }

  if (topVertical) {
    agentIds.push(topVertical);
  }

  // Fallback to dfm-router if nothing matched
  if (agentIds.length === 0) {
    agentIds.push('dfm-router');
  }

  const totalScore = sortedProcesses.reduce((sum, [, s]) => sum + s, 0);
  const confidence = Math.min(0.3 + totalScore * 0.15, 0.95);

  return { agentIds, mode, vertical: topVertical, confidence };
}
