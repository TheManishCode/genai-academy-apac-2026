import { motion } from "framer-motion";
import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from "recharts";
import { Moon, Sun, UploadCloud, Users } from "lucide-react";
import { useState } from "react";
import { AssistantPanel } from "./components/AssistantPanel";
import { MetricCard } from "./components/MetricCard";
import { RiskMap } from "./components/RiskMap";
import { alerts, gpuBenchmarks, incidents, kpis, roles, shapFactors, trendData, wards, type Role } from "./data/mockData";

export function App() {
  const [dark, setDark] = useState(false);
  const [role, setRole] = useState<Role>("Government");

  return (
    <main className={dark ? "dark" : ""}>
      <div className="min-h-screen bg-[linear-gradient(135deg,#f8fbfc_0%,#eef3f6_45%,#f7f5ff_100%)] text-ink dark:bg-[linear-gradient(135deg,#0b1120_0%,#111827_58%,#172554_100%)]">
        <header className="sticky top-0 z-20 border-b border-slate-200/70 bg-white/80 backdrop-blur-xl dark:border-slate-800 dark:bg-slate-950/70">
          <div className="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-3">
            <div className="flex min-w-0 items-center gap-3">
              <div className="grid h-10 w-10 place-items-center rounded-lg bg-ink text-white dark:bg-ocean">
                <span className="text-lg font-black">E</span>
              </div>
              <div className="min-w-0">
                <h1 className="truncate text-lg font-extrabold tracking-normal text-ink dark:text-white">EcoMind AI</h1>
                <p className="truncate text-xs font-medium text-slate-500 dark:text-slate-400">
                  AI Decision Intelligence for Climate Resilience
                </p>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <select
                value={role}
                onChange={(event) => setRole(event.target.value as Role)}
                className="rounded-md border border-slate-200 bg-white px-3 py-2 text-sm font-semibold dark:border-slate-700 dark:bg-slate-900 dark:text-white"
                aria-label="Role"
              >
                {roles.map((item) => (
                  <option key={item}>{item}</option>
                ))}
              </select>
              <button
                onClick={() => setDark((value) => !value)}
                className="rounded-md border border-slate-200 bg-white p-2 text-slate-700 dark:border-slate-700 dark:bg-slate-900 dark:text-white"
                aria-label="Toggle theme"
              >
                {dark ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
              </button>
            </div>
          </div>
        </header>

        <div className="mx-auto max-w-7xl px-4 py-6">
          <motion.section
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            className="grid gap-4 lg:grid-cols-[1.2fr_0.8fr]"
          >
            <div className="glass rounded-lg p-6">
              <div className="flex flex-wrap items-center gap-2 text-xs font-bold uppercase tracking-normal">
                <span className="rounded-md bg-emerald-100 px-2 py-1 text-emerald-700">Vertex AI + Gemini</span>
                <span className="rounded-md bg-cyan-100 px-2 py-1 text-cyan-700">BigQuery Live Twin</span>
                <span className="rounded-md bg-violet-100 px-2 py-1 text-violet-700">NVIDIA RAPIDS</span>
              </div>
              <h2 className="mt-4 max-w-4xl text-4xl font-extrabold tracking-normal text-ink dark:text-white md:text-5xl">
                Decide faster before climate risk becomes disaster.
              </h2>
              <p className="mt-4 max-w-3xl text-base leading-7 text-slate-600 dark:text-slate-300">
                EcoMind AI fuses weather, flood, AQI, hospital, road, satellite and citizen signals into explainable predictions and action plans for {role.toLowerCase()} teams.
              </p>
            </div>
            <div className="glass rounded-lg p-5">
              <div className="flex items-center gap-2">
                <Users className="h-5 w-5 text-ocean" />
                <h2 className="text-lg font-bold dark:text-white">Decision Brief</h2>
              </div>
              <p className="mt-3 text-sm leading-6 text-slate-600 dark:text-slate-300">
                Severe flood risk is concentrated across 7 wards. Activating pumps, shelters, diversions and hospital surge staffing is estimated to reduce impact by 31%.
              </p>
              <div className="mt-4 grid grid-cols-3 gap-2 text-center">
                {["7 wards", "124k people", "31% reduction"].map((item) => (
                  <span key={item} className="rounded-md bg-white px-2 py-3 text-sm font-bold shadow-sm dark:bg-slate-900 dark:text-white">
                    {item}
                  </span>
                ))}
              </div>
            </div>
          </motion.section>

          <section className="mt-5 grid gap-4 sm:grid-cols-2 xl:grid-cols-6">
            {kpis.map((kpi) => (
              <MetricCard key={kpi.label} {...kpi} />
            ))}
          </section>

          <section className="mt-5 grid gap-5 xl:grid-cols-[1.25fr_0.75fr]">
            <RiskMap wards={wards} />
            <AssistantPanel />
          </section>

          <section className="mt-5 grid gap-5 lg:grid-cols-3">
            <div className="glass rounded-lg p-5 lg:col-span-2">
              <h2 className="text-lg font-bold dark:text-white">Prediction Trends</h2>
              <div className="mt-4 h-72">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={trendData}>
                    <defs>
                      <linearGradient id="flood" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="5%" stopColor="#e11d48" stopOpacity={0.45} />
                        <stop offset="95%" stopColor="#e11d48" stopOpacity={0.02} />
                      </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" stroke="#dbe3ea" />
                    <XAxis dataKey="day" />
                    <YAxis />
                    <Tooltip />
                    <Area type="monotone" dataKey="flood" stroke="#e11d48" fill="url(#flood)" />
                    <Area type="monotone" dataKey="demand" stroke="#0f766e" fill="#0f766e22" />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>
            <div className="glass rounded-lg p-5">
              <h2 className="text-lg font-bold dark:text-white">SHAP Explanation</h2>
              <div className="mt-4 h-72">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={shapFactors} layout="vertical">
                    <XAxis type="number" hide />
                    <YAxis dataKey="factor" type="category" width={105} tick={{ fontSize: 12 }} />
                    <Tooltip />
                    <Bar dataKey="impact" radius={[0, 6, 6, 0]}>
                      {shapFactors.map((_, index) => (
                        <Cell key={index} fill={["#e11d48", "#f59e0b", "#0f766e", "#2563eb", "#7c3aed"][index]} />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </section>

          <section className="mt-5 grid gap-5 lg:grid-cols-3">
            <div className="glass rounded-lg p-5">
              <h2 className="text-lg font-bold dark:text-white">Live Alerts</h2>
              <div className="mt-4 space-y-3">
                {alerts.map(({ title, body, icon: Icon }) => (
                  <article key={title} className="rounded-lg border border-slate-200 bg-white p-3 dark:border-slate-700 dark:bg-slate-900">
                    <div className="flex items-center gap-2">
                      <Icon className="h-4 w-4 text-signal" />
                      <h3 className="text-sm font-bold dark:text-white">{title}</h3>
                    </div>
                    <p className="mt-2 text-sm text-slate-600 dark:text-slate-300">{body}</p>
                  </article>
                ))}
              </div>
            </div>
            <div className="glass rounded-lg p-5">
              <h2 className="text-lg font-bold dark:text-white">Citizen Reports</h2>
              <label className="mt-4 flex cursor-pointer flex-col items-center justify-center rounded-lg border border-dashed border-slate-300 bg-white p-6 text-center dark:border-slate-700 dark:bg-slate-900">
                <UploadCloud className="h-8 w-8 text-ocean" />
                <span className="mt-2 text-sm font-bold dark:text-white">Upload image, video, audio or text</span>
                <span className="mt-1 text-xs text-slate-500 dark:text-slate-400">Gemini extracts type, severity, urgency and location</span>
                <input className="sr-only" type="file" />
              </label>
              <div className="mt-4 space-y-2">
                {incidents.slice(0, 3).map((incident) => (
                  <div key={incident.id} className="flex items-center justify-between gap-3 rounded-md bg-slate-50 p-2 text-sm dark:bg-slate-900">
                    <span className="font-semibold dark:text-white">{incident.type}</span>
                    <span className="text-slate-500">{incident.time}</span>
                  </div>
                ))}
              </div>
            </div>
            <div className="glass rounded-lg p-5">
              <h2 className="text-lg font-bold dark:text-white">RAPIDS Benchmark</h2>
              <div className="mt-4 space-y-3">
                {gpuBenchmarks.map((item) => (
                  <div key={item.task}>
                    <div className="flex justify-between text-sm">
                      <span className="font-semibold dark:text-white">{item.task}</span>
                      <span className="text-emerald-600">{Math.round(item.cpu / item.gpu)}x faster</span>
                    </div>
                    <div className="mt-2 grid grid-cols-[1fr_1fr] gap-2 text-xs">
                      <span className="rounded-md bg-rose-100 px-2 py-1 text-rose-700">CPU {item.cpu}s</span>
                      <span className="rounded-md bg-emerald-100 px-2 py-1 text-emerald-700">GPU {item.gpu}s</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </section>
        </div>
      </div>
    </main>
  );
}
