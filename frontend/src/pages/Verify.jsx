import { Box, Typography, TextField, Button, Paper } from "@mui/material";
import { useState } from "react";
import axios from "axios"; // Import Axios for API calls
import Lottie from "lottie-react";

import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";
import DownloadIcon from "@mui/icons-material/Download";
import ArrowForwardIcon from "@mui/icons-material/ArrowForward";

import RingMeter from "../components/RiskMeter";
import loadingAnimation from "../assets/loading.json";
import "../style/Verify.css";

const Verify = () => {
  const [loading, setLoading] = useState(false);
  const [showResult, setShowResult] = useState(false);
  
  // 1. New State for URL and API Data
  const [url, setUrl] = useState("");
  const [result, setResult] = useState(null);

  const handleVerify = async () => {
    if (!url) return alert("Please enter a valid URL");

    setLoading(true);
    setShowResult(false);

    try {
      // 2. The Real Connection to your Stealth Backend
      const response = await axios.post("http://localhost:8000/scan", {
        url: url
      });

      setResult(response.data);
      setShowResult(true);
    } catch (error) {
      console.error("Scan failed:", error);
      alert("Could not analyze this product. Ensure backend is running.");
    } finally {
      setLoading(false);
    }
  };

  // 3. Helper to dynamically generate "Obeying" list based on data found
  const getObeyingList = (data) => {
    if (!data) return [];
    const list = [];
    if (data.product?.seller) list.push("Seller Identity Verified");
    if (data.product?.returns) list.push("Return Policy Detected");
    if (data.product?.price?.deal) list.push("Price Transparency");
    if (data.product?.technical_details) list.push("Technical Specs Available");
    return list.length > 0 ? list : ["Basic Metadata Found"];
  };

  // 4. Helper for "Not Obeying" (Violations from AI)
  const getNotObeyingList = (data) => {
    if (!data || !data.violations) return [];
    return data.violations.map(v => v.description); // Extract descriptions
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
            placeholder="https://www.flipkart.com/product/..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            InputProps={{ disableUnderline: true }}
          />
          <Button 
            className="hero-verify-btn" 
            endIcon={<ArrowForwardIcon />} 
            sx={{ "& .MuiButton-endIcon": { marginLeft: "3px" } }}
            onClick={handleVerify}
            disabled={loading}
          >
            {loading ? "SCANNING..." : "VERIFY"}
          </Button>
        </Box>
      </Box>

      {/* LOADING */}
      {loading && (
        <Box className="loading-box">
          <Lottie animationData={loadingAnimation} loop />
          <Typography>Connecting to Compliance Engine...</Typography>
        </Box>
      )}

      {/* RESULTS */}
      {showResult && result && (
        <>
          <Box className="verify-dashboard">
            {/* PRODUCT DETAILS */}
            <Paper className="details-card">
              <Typography variant="h6" className="card-title">
                Product Details 📂
              </Typography>

              <Box className="card-scroll">
                {/* Dynamic Data Injection */}
                <Typography>📦 Product: {result.product?.title?.substring(0, 40)}...</Typography>
                <Typography>🏪 Seller: {result.product?.seller || "Unknown"}</Typography>
                <Typography>💰 Price: ₹{result.product?.price?.deal || "N/A"}</Typography>
                <Typography>📂 Category: General</Typography>
                <Typography>📝 Returns: {result.product?.returns ? "Yes" : "No Info"}</Typography>
                <Typography>🔗 URL: {new URL(result.product?.url).hostname}</Typography>
              </Box>
            </Paper>

            {/* RIGHT SIDE */}
            <Box className="right-panel">
              <Box className="risk-remain">
                {/* Dynamic Risk Score */}
                <RingMeter score={result.risk_score} />
              </Box>

              <Box className="rules-row">
                <Paper className="rule-card obey">
                  <Typography variant="h6" className="card-title obey-title">
                    ✅ Obeying
                  </Typography>

                  <Box className="card-scroll">
                    {getObeyingList(result).map((item, i) => (
                      <Box key={i} className="rule-item">
                        <CheckCircleIcon />
                        {item}
                      </Box>
                    ))}
                  </Box>
                </Paper>

                <Paper className="rule-card not-obey">
                  <Typography variant="h6" className="card-title not-obey-title">
                    ❌ Violations
                  </Typography>

                  <Box className="card-scroll">
                    {getNotObeyingList(result).length > 0 ? (
                      getNotObeyingList(result).map((item, i) => (
                        <Box key={i} className="rule-item">
                          <CancelIcon />
                          {item}
                        </Box>
                      ))
                    ) : (
                      <Box className="rule-item">No Critical Violations Found</Box>
                    )}
                  </Box>
                </Paper>
              </Box>

              <Button
                className="download-btn"
                startIcon={<DownloadIcon />}
              >
                DOWNLOAD REPORT
              </Button>
            </Box>
          </Box>

          {/* RECOMMENDATION */}
          <Box className="recommendation-box">
            <Typography variant="h5" className="recommendation-title">
              {result.risk_score > 50 ? "⚠️ High Risk Detected" : "🛡️ Product Looks Safe"}
            </Typography>

            <Typography className="recommendation-text">
              {result.risk_score > 50 
                ? "Multiple compliance violations detected. The seller information or return policy is unclear. Proceed with extreme caution."
                : "This product passes most standard compliance checks. Seller and pricing details appear transparent."}
            </Typography>
          </Box>
        </>
      )}
    </Box>
  );
};

export default Verify;
