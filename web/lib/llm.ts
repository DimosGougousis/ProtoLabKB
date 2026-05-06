import OpenAI from 'openai';
import Anthropic from '@anthropic-ai/sdk';
import { AgentDefinition, buildSystemPrompt } from './agents';

let openaiClient: OpenAI | null = null;
let anthropicClient: Anthropic | null = null;

function getOpenAI(): OpenAI {
  if (!openaiClient) {
    openaiClient = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
  }
  return openaiClient;
}

function getAnthropic(): Anthropic {
  if (!anthropicClient) {
    anthropicClient = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
  }
  return anthropicClient;
}

export interface ChatMessage {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

export async function* streamCompletion(
  provider: 'openai' | 'anthropic',
  agent: AgentDefinition,
  messages: ChatMessage[],
  model?: string
): AsyncGenerator<string, void, unknown> {
  const systemPrompt = buildSystemPrompt(agent);
  const fullMessages: ChatMessage[] = [{ role: 'system', content: systemPrompt }, ...messages];

  if (provider === 'openai') {
    const stream = await getOpenAI().chat.completions.create({
      model: model || process.env.OPENAI_MODEL || 'gpt-4o',
      messages: fullMessages as any,
      stream: true,
      temperature: 0.3,
      max_tokens: 4000,
    });

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) yield content;
    }
  } else {
    const stream = await getAnthropic().messages.create({
      model: model || process.env.ANTHROPIC_MODEL || 'claude-3-5-sonnet-20241022',
      max_tokens: 4000,
      system: systemPrompt,
      messages: messages.filter(m => m.role !== 'system').map(m => ({
        role: m.role as 'user' | 'assistant',
        content: m.content,
      })),
      stream: true,
    });

    for await (const chunk of stream) {
      if (chunk.type === 'content_block_delta' && 'text' in chunk.delta) {
        yield chunk.delta.text;
      }
    }
  }
}
