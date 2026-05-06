'use client';

import { useState, useCallback } from 'react';
import AgentSelector from './AgentSelector';
import MessageList, { Message } from './MessageList';
import MessageInput from './MessageInput';

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [selectedAgent, setSelectedAgent] = useState<string | null>(null);
  const [isStreaming, setIsStreaming] = useState(false);

  const sendMessage = useCallback(async (content: string) => {
    const userMsg: Message = {
      id: crypto.randomUUID(),
      role: 'user',
      content,
    };

    const assistantMsg: Message = {
      id: crypto.randomUUID(),
      role: 'assistant',
      content: '',
      isStreaming: true,
    };

    setMessages(prev => [...prev, userMsg, assistantMsg]);
    setIsStreaming(true);

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          messages: [...messages, userMsg].map(m => ({ role: m.role, content: m.content })),
          agentId: selectedAgent,
          provider: 'openai',
        }),
      });

      const reader = res.body?.getReader();
      if (!reader) throw new Error('No response body');

      const decoder = new TextDecoder();
      let buffer = '';
      let agentName = 'ProtoLabs Agent';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (!line.startsWith('data: ')) continue;
          const data = line.slice(6).trim();
          if (data === '[DONE]') continue;

          try {
            const parsed = JSON.parse(data);
            if (parsed.type === 'meta') {
              agentName = parsed.agentName;
            } else if (parsed.type === 'chunk') {
              setMessages(prev => {
                const last = prev[prev.length - 1];
                if (last.role !== 'assistant') return prev;
                const updated = [...prev];
                updated[updated.length - 1] = {
                  ...last,
                  content: last.content + parsed.content,
                  agentName,
                };
                return updated;
              });
            } else if (parsed.type === 'error') {
              setMessages(prev => {
                const updated = [...prev];
                updated[updated.length - 1] = {
                  ...updated[updated.length - 1],
                  content: `Error: ${parsed.message}`,
                  isStreaming: false,
                };
                return updated;
              });
            }
          } catch {
            // ignore parse errors
          }
        }
      }

      setMessages(prev => {
        const updated = [...prev];
        updated[updated.length - 1] = {
          ...updated[updated.length - 1],
          isStreaming: false,
        };
        return updated;
      });
    } catch (err) {
      setMessages(prev => {
        const updated = [...prev];
        updated[updated.length - 1] = {
          ...updated[updated.length - 1],
          content: `Error: ${(err as Error).message}`,
          isStreaming: false,
        };
        return updated;
      });
    } finally {
      setIsStreaming(false);
    }
  }, [messages, selectedAgent]);

  return (
    <div className="flex h-screen bg-protolabs-navy">
      <AgentSelector selectedId={selectedAgent} onSelect={setSelectedAgent} />
      <div className="flex-1 flex flex-col min-w-0">
        <header className="border-b border-protolabs-border px-6 py-4 flex items-center justify-between bg-protolabs-surface">
          <div>
            <h1 className="text-lg font-bold text-white">ProtoLabs Product Office</h1>
            <p className="text-xs text-gray-500">
              {selectedAgent ? `Locked to: ${selectedAgent}` : 'Auto-routing enabled'}
            </p>
          </div>
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-green-500" />
            <span className="text-xs text-gray-400">Online</span>
          </div>
        </header>
        <MessageList messages={messages} />
        <MessageInput onSend={sendMessage} disabled={isStreaming} />
      </div>
    </div>
  );
}
