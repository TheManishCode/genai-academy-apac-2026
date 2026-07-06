import { Send, Sparkles } from "lucide-react";
import { useMemo, useState } from "react";

const examplePrompts = [
  "Which wards are likely to flood tomorrow?",
  "Which hospitals need preparation?",
  "What areas should be evacuated?",
  "Explain today's AQI."
];

export function AssistantPanel() {
  const [prompt, setPrompt] = useState(examplePrompts[0]);

  const answer = useMemo(() => {
    return {
      confidence: "87%",
      sql: "SELECT ward, flood_risk, population_at_risk FROM risk_forecasts WHERE horizon='24h' ORDER BY flood_risk DESC LIMIT 5;",
      text:
        "Yamuna Bank, Civil Lines, and two low-elevation river wards should be prioritized. The model cites rainfall forecast, river-level anomaly, clogged drains, and recent citizen reports as the dominant signals. Recommended actions: stage pumps, activate shelters, close underpasses, and notify hospitals inside the impact radius."
    };
  }, [prompt]);

  return (
    <section className="glass rounded-lg p-5">
      <div className="flex items-center gap-2">
        <Sparkles className="h-5 w-5 text-ocean" />
        <h2 className="text-lg font-bold text-ink dark:text-white">Gemini Decision Assistant</h2>
      </div>
      <div className="mt-4 grid gap-2 sm:grid-cols-2">
        {examplePrompts.map((item) => (
          <button
            key={item}
            onClick={() => setPrompt(item)}
            className="rounded-md border border-slate-200 bg-white px-3 py-2 text-left text-sm font-medium text-slate-700 transition hover:border-ocean hover:text-ocean dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200"
          >
            {item}
          </button>
        ))}
      </div>
      <div className="mt-4 rounded-lg bg-slate-950 p-4 text-white">
        <div className="flex items-center justify-between gap-3">
          <p className="text-sm font-semibold text-slate-200">{prompt}</p>
          <span className="rounded-md bg-emerald-400/15 px-2 py-1 text-xs font-bold text-emerald-300">
            {answer.confidence}
          </span>
        </div>
        <p className="mt-3 text-sm leading-6 text-slate-300">{answer.text}</p>
        <pre className="mt-3 overflow-auto rounded-md bg-black/35 p-3 text-xs text-cyan-200">{answer.sql}</pre>
      </div>
      <label className="mt-4 flex items-center gap-2 rounded-lg border border-slate-200 bg-white p-2 dark:border-slate-700 dark:bg-slate-900">
        <input
          value={prompt}
          onChange={(event) => setPrompt(event.target.value)}
          className="min-w-0 flex-1 bg-transparent px-2 text-sm outline-none dark:text-white"
          aria-label="Ask EcoMind AI"
        />
        <button className="rounded-md bg-ink p-2 text-white transition hover:bg-ocean dark:bg-ocean">
          <Send className="h-4 w-4" />
        </button>
      </label>
    </section>
  );
}
