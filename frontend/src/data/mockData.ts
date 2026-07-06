import {
  Activity,
  Ambulance,
  BellRing,
  CloudRain,
  Flame,
  HeartPulse,
  MapPin,
  ShieldAlert,
  Wind
} from "lucide-react";

export type Role = "Citizen" | "Government" | "Admin" | "NGO";

export type WardRisk = {
  id: string;
  name: string;
  lat: number;
  lng: number;
  floodRisk: number;
  aqi: number;
  heatRisk: number;
  rainfallMm: number;
  populationAtRisk: number;
  confidence: number;
  reason: string;
  recommendation: string;
};

export const roles: Role[] = ["Government", "Citizen", "NGO", "Admin"];

export const kpis = [
  { label: "Current AQI", value: "168", delta: "+18 vs 24h", icon: Wind, tone: "text-rose-600" },
  { label: "Rainfall", value: "112 mm", delta: "next 24h", icon: CloudRain, tone: "text-cyan-600" },
  { label: "Flood Risk", value: "High", delta: "7 wards", icon: ShieldAlert, tone: "text-amber-600" },
  { label: "Heatwave Risk", value: "41 C", delta: "2 zones", icon: Flame, tone: "text-orange-600" },
  { label: "Disaster Score", value: "82/100", delta: "+11 today", icon: Activity, tone: "text-violet-600" },
  { label: "Hospital Load", value: "74%", delta: "rising", icon: HeartPulse, tone: "text-emerald-600" }
];

export const wards: WardRisk[] = [
  {
    id: "W-14",
    name: "Yamuna Bank",
    lat: 28.621,
    lng: 77.256,
    floodRisk: 0.91,
    aqi: 181,
    heatRisk: 0.42,
    rainfallMm: 138,
    populationAtRisk: 42000,
    confidence: 0.87,
    reason: "River level anomaly, saturated soil index, blocked drains, and high 24h rainfall forecast.",
    recommendation: "Pre-stage 18 pumps, open 5 shelters, close two underpasses, and notify hospitals within 6 km."
  },
  {
    id: "W-22",
    name: "Civil Lines",
    lat: 28.681,
    lng: 77.225,
    floodRisk: 0.74,
    aqi: 154,
    heatRisk: 0.51,
    rainfallMm: 102,
    populationAtRisk: 28000,
    confidence: 0.82,
    reason: "Drainage complaints increased 2.4x, low road elevation, and delayed pump availability.",
    recommendation: "Divert traffic from Ring Road, dispatch drain clearance crews, and prepare two relief schools."
  },
  {
    id: "W-09",
    name: "Okhla Industrial",
    lat: 28.535,
    lng: 77.283,
    floodRisk: 0.58,
    aqi: 211,
    heatRisk: 0.68,
    rainfallMm: 81,
    populationAtRisk: 19000,
    confidence: 0.79,
    reason: "Industrial PM2.5 spike, stagnant wind, and high night-time heat retention.",
    recommendation: "Issue AQI advisory, reduce outdoor shifts, and deploy mobile health vans near factories."
  },
  {
    id: "W-31",
    name: "Rohini Sector 18",
    lat: 28.738,
    lng: 77.118,
    floodRisk: 0.33,
    aqi: 142,
    heatRisk: 0.78,
    rainfallMm: 43,
    populationAtRisk: 12000,
    confidence: 0.75,
    reason: "High surface temperature, low tree-cover index, and energy demand surge.",
    recommendation: "Open cooling centers, prioritize power-grid monitoring, and send heat alerts to elderly residents."
  }
];

export const incidents = [
  { id: "CR-9031", type: "Waterlogging", area: "Yamuna Bank", severity: "Critical", source: "Citizen image", time: "8 min" },
  { id: "CR-9027", type: "AQI spike", area: "Okhla Industrial", severity: "High", source: "OpenAQ", time: "16 min" },
  { id: "CR-9019", type: "Road closure", area: "Civil Lines", severity: "Medium", source: "Responder", time: "31 min" },
  { id: "CR-9004", type: "Hospital surge", area: "LNJP cluster", severity: "High", source: "FHIR feed", time: "42 min" }
];

export const alerts = [
  { title: "Heavy rainfall threshold breached", body: "3 river-adjacent wards need pump staging before 02:00.", icon: BellRing },
  { title: "Hospital demand rising", body: "Expected emergency demand +22% for respiratory and trauma cases.", icon: Ambulance },
  { title: "Shelter activation recommended", body: "6 shelters cover 82% of high-risk population within 1.5 km.", icon: MapPin }
];

export const trendData = [
  { day: "Mon", flood: 48, aqi: 138, demand: 52 },
  { day: "Tue", flood: 54, aqi: 151, demand: 56 },
  { day: "Wed", flood: 61, aqi: 149, demand: 59 },
  { day: "Thu", flood: 72, aqi: 163, demand: 66 },
  { day: "Fri", flood: 78, aqi: 171, demand: 71 },
  { day: "Sat", flood: 82, aqi: 168, demand: 74 },
  { day: "Sun", flood: 87, aqi: 181, demand: 79 }
];

export const shapFactors = [
  { factor: "Rain forecast", impact: 32 },
  { factor: "Drain complaints", impact: 24 },
  { factor: "River level", impact: 18 },
  { factor: "Road elevation", impact: 14 },
  { factor: "Pump availability", impact: 12 }
];

export const gpuBenchmarks = [
  { task: "Feature engineering", cpu: 42.1, gpu: 6.8 },
  { task: "XGBoost training", cpu: 118.4, gpu: 18.9 },
  { task: "Isolation Forest", cpu: 31.6, gpu: 5.4 },
  { task: "Batch inference", cpu: 12.2, gpu: 2.1 }
];
