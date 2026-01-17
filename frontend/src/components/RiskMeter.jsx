import { useEffect, useState } from "react";
import "../style/RiskMeter.css";

const RiskMeter = ({ score }) => {
  const [progress, setProgress] = useState(0);
  const radius = 60;
  const circumference = 2 * Math.PI * radius;

  useEffect(() => {
    let current = 0;
    const timer = setInterval(() => {
      current += 1;
      setProgress(current);
      if (current >= score) clearInterval(timer);
    }, 14);
    return () => clearInterval(timer);
  }, [score]);

  const offset = circumference - (progress / 100) * circumference;

  const label =
    score < 40 ? "Low Risk" : score < 70 ? "Medium Risk" : "High Risk";

  return (
    <div className="ring-meter">
      <svg width="160" height="160">
        <circle
          cx="80"
          cy="80"
          r={radius}
          stroke="#e5e7eb"
          strokeWidth="12"
          fill="none"
        />
        <circle
          cx="80"
          cy="80"
          r={radius}
          stroke="url(#riskGrad)"
          strokeWidth="12"
          fill="none"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          strokeLinecap="round"
        />
        <defs>
          <linearGradient id="riskGrad">
            <stop offset="0%" stopColor="#22c55e" />
            <stop offset="50%" stopColor="#f59e0b" />
            <stop offset="100%" stopColor="#ef4444" />
          </linearGradient>
        </defs>
      </svg>

      <div className="ring-text">
        <h2>{progress} / 100</h2>
        <span>{label}</span>
      </div>
    </div>
  );
};

export default RiskMeter;
