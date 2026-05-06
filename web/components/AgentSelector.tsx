'use client';

import { useState, useEffect } from 'react';

interface Agent {
  id: string;
  name: string;
  purpose: string;
  keywords: string[];
}

interface Props {
  selectedId: string | null;
  onSelect: (id: string | null) => void;
}

export default function AgentSelector({ selectedId, onSelect }: Props) {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/agents')
      .then(r => r.json())
      .then(data => {
        setAgents(data.agents);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div className="w-72 bg-protolabs-surface border-r border-protolabs-border flex flex-col h-full">
      <div className="p-4 border-b border-protolabs-border">
        <h2 className="text-sm font-semibold text-gray-400 uppercase tracking-wider">ProtoLabs Agents</h2>
        <p className="text-xs text-gray-500 mt-1">Select an agent or let the router decide</p>
      </div>

      <div className="flex-1 overflow-y-auto p-2 space-y-1">
        <button
          onClick={() => onSelect(null)}
          className={`w-full text-left px-3 py-2.5 rounded-lg text-sm transition-colors ${
            selectedId === null
              ? 'bg-protolabs-accent/10 text-protolabs-accent border border-protolabs-accent/20'
              : 'text-gray-300 hover:bg-gray-800'
          }`}
        >
          <div className="font-medium">Auto-Route</div>
          <div className="text-xs text-gray-500 mt-0.5">Let the router classify your prompt</div>
        </button>

        {loading ? (
          <div className="text-xs text-gray-500 px-3 py-4">Loading agents...</div>
        ) : (
          agents.map(agent => (
            <button
              key={agent.id}
              onClick={() => onSelect(agent.id)}
              className={`w-full text-left px-3 py-2.5 rounded-lg text-sm transition-colors ${
                selectedId === agent.id
                  ? 'bg-protolabs-accent/10 text-protolabs-accent border border-protolabs-accent/20'
                  : 'text-gray-300 hover:bg-gray-800'
              }`}
            >
              <div className="font-medium">{agent.name}</div>
              <div className="text-xs text-gray-500 mt-0.5 line-clamp-2">{agent.purpose}</div>
              <div className="flex flex-wrap gap-1 mt-1.5">
                {agent.keywords.slice(0, 3).map(kw => (
                  <span key={kw} className="text-[10px] px-1.5 py-0.5 bg-gray-800 rounded text-gray-400">
                    {kw}
                  </span>
                ))}
              </div>
            </button>
          ))
        )}
      </div>
    </div>
  );
}
