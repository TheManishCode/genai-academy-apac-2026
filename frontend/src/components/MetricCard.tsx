import { LucideIcon } from "lucide-react";

type MetricCardProps = {
  label: string;
  value: string;
  delta: string;
  icon: LucideIcon;
  tone: string;
};

export function MetricCard({ label, value, delta, icon: Icon, tone }: MetricCardProps) {
  return (
    <section className="glass rounded-lg p-4">
      <div className="flex items-center justify-between gap-3">
        <span className="text-sm font-medium text-slate-500 dark:text-slate-400">{label}</span>
        <Icon className={`h-5 w-5 ${tone}`} />
      </div>
      <div className="mt-3 flex items-end justify-between gap-3">
        <strong className="text-2xl font-bold tracking-normal text-ink dark:text-white">{value}</strong>
        <span className="rounded-md bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-600 dark:bg-slate-800 dark:text-slate-300">
          {delta}
        </span>
      </div>
    </section>
  );
}
