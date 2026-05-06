'use client';

import { useEffect, useRef } from 'react';
import { remark } from 'remark';
import remarkGfm from 'remark-gfm';
import remarkHtml from 'remark-html';

export interface Message {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  agentName?: string;
  isStreaming?: boolean;
}

interface Props {
  messages: Message[];
}

function renderMarkdown(content: string): string {
  try {
    const result = remark().use(remarkGfm).use(remarkHtml).processSync(content);
    return String(result);
  } catch {
    return content;
  }
}

export default function MessageList({ messages }: Props) {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="flex-1 overflow-y-auto px-6 py-6 space-y-4">
      {messages.length === 0 && (
        <div className="flex flex-col items-center justify-center h-full text-gray-500">
          <div className="text-4xl mb-4">ProtoLabs</div>
          <p className="text-sm">Ask about CNC machining, injection molding, DFM review, or manufacturing strategy.</p>
          <div className="flex gap-2 mt-6">
            {['What is the minimum wall thickness for ABS?', 'Review my CNC bracket design', 'Compare SLA vs SLS for aerospace'].map(q => (
              <span key={q} className="text-xs px-3 py-1.5 bg-gray-800 rounded-full border border-gray-700">
                {q}
              </span>
            ))}
          </div>
        </div>
      )}
      {messages.map(msg => (
        <div key={msg.id} className={msg.role === 'user' ? 'flex justify-end' : 'flex justify-start'}>
          <div className={msg.role === 'user' ? 'chat-message-user' : 'chat-message-agent'}>
            {msg.role === 'assistant' && msg.agentName && (
              <div className="text-xs font-medium text-protolabs-accent mb-1.5 flex items-center gap-1.5">
                <span className="w-1.5 h-1.5 rounded-full bg-protolabs-accent" />
                {msg.agentName}
              </div>
            )}
            <div
              className="prose-custom text-sm"
              dangerouslySetInnerHTML={{ __html: renderMarkdown(msg.content) }}
            />
            {msg.isStreaming && (
              <span className="inline-block w-2 h-4 bg-protolabs-accent ml-1 animate-pulse" />
            )}
          </div>
        </div>
      ))}
      <div ref={bottomRef} />
    </div>
  );
}
