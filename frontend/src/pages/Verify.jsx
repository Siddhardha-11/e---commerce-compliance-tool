import { Box, Typography, TextField, Button, Paper } from "@mui/material";
import { useState } from "react";
import Lottie from "lottie-react";

import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";
import DownloadIcon from "@mui/icons-material/Download";

import RingMeter from "../components/RiskMeter";
import loadingAnimation from "../assets/loading.json";
import "../style/Verify.css";
import ArrowForwardIcon from "@mui/icons-material/ArrowForward";

const Verify = () => {
  const [loading, setLoading] = useState(false);
  const [showResult, setShowResult] = useState(false);

  const riskScore = 20;

  const obeying = [
    "Seller name provided",
    "Return policy available",
    "Clear pricing mentioned",
    "Contact details provided",
  ];

  const notObeying = [
    "Manufacturer address missing",
    "Warranty information not found",
    "No customer care number",
  ];

  const handleVerify = () => {
    setLoading(true);
    setShowResult(false);

    setTimeout(() => {
      setLoading(false);
      setShowResult(true);
    }, 2500);
  };

  return (
    <Box className="verify-bg">
      {/* HERO */}
      <Box className="verify-hero">
        <Typography variant="h2" className="hero-title" sx={{ mb: 1 }}>
          Verify Before You Buy
        </Typography>

        <Typography variant="body1" className="hero-subtitle">
          Analyze product URLs for compliance & risk instantly.
        </Typography>

        <Box className="hero-input-wrapper">
          <TextField
            fullWidth
            placeholder="https://www.example.com/product/..."
            InputProps={{ disableUnderline: true }}
          />
          <Button className="hero-verify-btn" endIcon={<ArrowForwardIcon />} sx={{
            "& .MuiButton-endIcon": {
              marginLeft: "3px",   // 🔥 reduce space here
            },
          }}
            onClick={handleVerify}>
            VERIFY
          </Button>
        </Box>
      </Box>

      {/* LOADING */}
      {loading && (
        <Box className="loading-box">
          <Lottie animationData={loadingAnimation} loop />
          <Typography>Analyzing product compliance…</Typography>
        </Box>
      )}

      {/* RESULTS */}
      {showResult && (
        <>
          <Box className="verify-dashboard">
            {/* PRODUCT DETAILS */}
            <Paper className="details-card">
              <Typography variant="h6" className="card-title">
                Product Details 📂
              </Typography>

              <Box className="card-scroll">
                <Typography>📦 Product: Wireless Earbuds</Typography>
                <Typography>🏪 Seller: ABC Electronics</Typography>
                <Typography>💰 Price: ₹1,499</Typography>
                <Typography>📂 Category: Electronics</Typography>
                <Typography>🚚 Delivery: Free</Typography>
                <Typography>🛒 Platform: Marketplace XYZ</Typography>
              </Box>
            </Paper>

            {/* RIGHT SIDE */}
            <Box className="right-panel">
              <Box className="risk-remain">
                <RingMeter score={riskScore} />
              </Box>

              <Box className="rules-row">
                <Paper className="rule-card obey">
                  <Typography variant="h6" className="card-title obey-title">
                    ✅ Obeying
                  </Typography>

                  <Box className="card-scroll">
                    {obeying.map((item, i) => (
                      <Box key={i} className="rule-item">
                        <CheckCircleIcon />
                        {item}
                      </Box>
                    ))}
                  </Box>
                </Paper>

                <Paper className="rule-card not-obey">
                  <Typography variant="h6" className="card-title not-obey-title">
                    ❌ Not Obeying
                  </Typography>

                  <Box className="card-scroll">
                    {notObeying.map((item, i) => (
                      <Box key={i} className="rule-item">
                        <CancelIcon />
                        {item}
                      </Box>
                    ))}
                  </Box>
                </Paper>
              </Box>

              <Button
                className="download-btn"
                startIcon={<DownloadIcon />}
              >
                DOWNLOAD COMPLIANCE REPORT
              </Button>
            </Box>
          </Box>

          {/* RECOMMENDATION */}
          <Box className="recommendation-box">
            <Typography variant="h5" className="recommendation-title">
              Recommendation
            </Typography>

            <Typography className="recommendation-text">
              Proceed with caution. Missing manufacturer and warranty
              information increases risk. Prefer verified sellers or
              official brand stores before completing your purchase.
            </Typography>
          </Box>
        </>
      )}
    </Box>
  );
};

export default Verify;
