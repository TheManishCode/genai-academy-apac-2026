import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        ink: "#131820",
        mist: "#eef3f6",
        cloud: "#f8fbfc",
        ocean: "#0f766e",
        signal: "#e11d48",
        amber: "#f59e0b"
      },
      boxShadow: {
        soft: "0 20px 60px rgba(15, 23, 42, 0.12)"
      },
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"]
      }
    }
  },
  plugins: []
};

export default config;
