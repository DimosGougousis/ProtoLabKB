import { NextRequest } from 'next/server';
import { routePrompt } from '@/lib/router';
import { getAgentById } from '@/lib/agents';
import { streamCompletion, ChatMessage } from '@/lib/llm';

export const runtime = 'edge';
export const maxDuration = 60;

export async function POST(req: NextRequest) {
  try {
    const { messages, agentId, provider = 'openai' }: {
      messages: ChatMessage[];
      agentId?: string;
      provider?: 'openai' | 'anthropic';
    } = await req.json();

    const userMessage = messages[messages.length - 1];
    if (!userMessage || userMessage.role !== 'user') {
      return new Response('Last message must be from user', { status: 400 });
    }

    // Route or use explicit agent
    let targetAgentId = agentId;
    if (!targetAgentId) {
      const route = routePrompt(userMessage.content);
      targetAgentId = route.agentIds[0];
    }

    const agent = getAgentById(targetAgentId);
    if (!agent) {
      return new Response(`Agent not found: ${targetAgentId}`, { status: 404 });
    }

    // Build response stream
    const encoder = new TextEncoder();
    const stream = new ReadableStream({
      async start(controller) {
        // Send metadata first
        const meta = JSON.stringify({ type: 'meta', agentId: agent.id, agentName: agent.name });
        controller.enqueue(encoder.encode(`data: ${meta}\n\n`));

        try {
          for await (const chunk of streamCompletion(provider, agent, messages)) {
            const payload = JSON.stringify({ type: 'chunk', content: chunk });
            controller.enqueue(encoder.encode(`data: ${payload}\n\n`));
          }

          controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'done' })}\n\n`));
          controller.close();
        } catch (err) {
          const error = JSON.stringify({ type: 'error', message: (err as Error).message });
          controller.enqueue(encoder.encode(`data: ${error}\n\n`));
          controller.close();
        }
      },
    });

    return new Response(stream, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
      },
    });
  } catch (err) {
    return new Response(`Error: ${(err as Error).message}`, { status: 500 });
  }
}
