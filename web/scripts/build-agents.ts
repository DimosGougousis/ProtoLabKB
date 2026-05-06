/**
 * Build script: reads ../agents/*.agent.md and generates lib/agents.json
 * Run before build: npx ts-node scripts/build-agents.ts
 */
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const ROOT = path.resolve(process.cwd(), '..');
const AGENTS_DIR = path.join(ROOT, 'agents');
const OUTPUT = path.join(process.cwd(), 'lib', 'agents.json');

function main() {
  if (!fs.existsSync(AGENTS_DIR)) {
    console.warn(`Agents directory not found: ${AGENTS_DIR}`);
    fs.writeFileSync(OUTPUT, '[]');
    return;
  }

  const files = fs.readdirSync(AGENTS_DIR).filter(f => f.endsWith('.agent.md'));

  const agents = files.map(file => {
    const raw = fs.readFileSync(path.join(AGENTS_DIR, file), 'utf-8');
    const { data, content } = matter(raw);

    return {
      id: data.id || file.replace('.agent.md', ''),
      name: data.name || data.id,
      type: data.type || 'agent',
      purpose: data.purpose || '',
      loads: data.loads || [],
      sourceUrls: data.source_urls || [],
      keywords: data.keywords || [],
      content,
    };
  });

  fs.writeFileSync(OUTPUT, JSON.stringify(agents, null, 2));
  console.log(`Generated ${OUTPUT} with ${agents.length} agents`);
}

main();
