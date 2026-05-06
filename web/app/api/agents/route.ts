import { NextResponse } from 'next/server';
import { loadAgents } from '@/lib/agents';

export async function GET() {
  const agents = loadAgents().map(a => ({
    id: a.id,
    name: a.name,
    purpose: a.purpose,
    keywords: a.keywords.slice(0, 8),
  }));

  return NextResponse.json({ agents });
}
