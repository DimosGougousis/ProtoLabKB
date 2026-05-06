import agentsJson from './agents.json';

export interface AgentDefinition {
  id: string;
  name: string;
  type: string;
  purpose: string;
  loads: string[];
  sourceUrls: string[];
  keywords: string[];
  content: string;
}

export function loadAgents(): AgentDefinition[] {
  return agentsJson as AgentDefinition[];
}

export function getAgentById(id: string): AgentDefinition | undefined {
  return loadAgents().find(a => a.id === id);
}

export function buildSystemPrompt(agent: AgentDefinition): string {
  const kbContext = agent.loads.length > 0
    ? `\n\n## Loaded Knowledge Base Files\n${agent.loads.map(l => `- ${l}`).join('\n')}`
    : '';

  const sourceContext = agent.sourceUrls.length > 0
    ? `\n\n## Source URLs\n${agent.sourceUrls.map(u => `- ${u}`).join('\n')}`
    : '';

  return `You are the ${agent.name} (${agent.id}) agent for the ProtoLabs Product Office.

## Purpose
${agent.purpose}

## Procedure
${agent.content.slice(0, 8000)}${agent.content.length > 8000 ? '\n\n[Content truncated for token efficiency]' : ''}
${kbContext}
${sourceContext}

## Rules
- Every claim must cite the cached KB file and original ProtoLabs URL.
- Use the format: "Claim [knowledge/<folder>/<article>.md → https://www.protolabs.com/...]"
- If you don't know, say so. Do not hallucinate manufacturing specifications.
- Be concise but thorough. Engineers value precision over verbosity.`;
}
