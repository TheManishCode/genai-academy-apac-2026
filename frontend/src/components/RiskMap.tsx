import L from "leaflet";
import { CircleMarker, MapContainer, Popup, TileLayer } from "react-leaflet";
import { WardRisk } from "../data/mockData";
import { formatPercent } from "../lib/utils";

type RiskMapProps = {
  wards: WardRisk[];
};

const center: [number, number] = [28.62, 77.22];

function colorForRisk(risk: number) {
  if (risk >= 0.8) return "#e11d48";
  if (risk >= 0.6) return "#f59e0b";
  return "#0f766e";
}

export function RiskMap({ wards }: RiskMapProps) {
  return (
    <section className="glass rounded-lg p-4">
      <div className="mb-3 flex flex-wrap items-center justify-between gap-3">
        <div>
          <h2 className="text-lg font-bold text-ink dark:text-white">Live Risk Map</h2>
          <p className="text-sm text-slate-500 dark:text-slate-400">Flood, AQI, hospital, shelter and road intelligence layers</p>
        </div>
        <div className="flex flex-wrap gap-2 text-xs font-semibold">
          {["Flood", "AQI", "Rain", "Hospitals", "Shelters"].map((layer) => (
            <span key={layer} className="rounded-md bg-white px-2 py-1 text-slate-600 shadow-sm dark:bg-slate-900 dark:text-slate-300">
              {layer}
            </span>
          ))}
        </div>
      </div>
      <MapContainer center={center} zoom={11} scrollWheelZoom={false}>
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {wards.map((ward) => (
          <CircleMarker
            key={ward.id}
            center={[ward.lat, ward.lng]}
            radius={18 + ward.floodRisk * 18}
            pathOptions={{
              color: colorForRisk(ward.floodRisk),
              fillColor: colorForRisk(ward.floodRisk),
              fillOpacity: 0.42,
              weight: 2
            }}
            eventHandlers={{
              mouseover: (event) => event.target.openPopup(),
              click: (event) => event.target.openPopup()
            }}
          >
            <Popup>
              <div className="w-64">
                <strong>{ward.name}</strong>
                <p>Flood risk: {formatPercent(ward.floodRisk)} | AQI: {ward.aqi}</p>
                <p>{ward.reason}</p>
                <p><strong>Action:</strong> {ward.recommendation}</p>
              </div>
            </Popup>
          </CircleMarker>
        ))}
      </MapContainer>
    </section>
  );
}

L.Icon.Default.mergeOptions({
  iconRetinaUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon-2x.png",
  iconUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon.png",
  shadowUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png"
});
