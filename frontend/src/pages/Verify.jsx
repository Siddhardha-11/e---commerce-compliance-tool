import { Box, Typography, TextField, Button, Paper } from "@mui/material";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";
import CancelIcon from "@mui/icons-material/Cancel";
import DownloadIcon from "@mui/icons-material/Download";
import RingMeter from "../components/RiskMeter";
import "../style/Verify.css";

const Verify = () => {
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

  return (
    <Box className="verify-page">
      {/* TOP */}
      <Box className="verify-top">
        <Typography variant="h3">Verify Before You Buy</Typography>
        <Typography className="subtitle">
          Paste a product URL to analyze compliance and risk.
        </Typography>

        <Box className="verify-input">
          <TextField
            fullWidth
            placeholder="https://www.example.com/product/..."
          />
          <Button variant="contained">Verify</Button>
        </Box>
      </Box>

      {/* MAIN DASHBOARD */}
      <Box className="verify-dashboard">
        {/* LEFT : DETAILS (1 PART) */}
        <Paper className="details-card">
          <Typography variant="h6">Product Details</Typography>
          <Box className="card-scroll">
            <Typography>Product: Wireless Earbuds</Typography>
            <Typography>Seller: ABC Electronics</Typography>
            <Typography>Price: ₹1,499</Typography>
            <Typography>Category: Electronics</Typography>
            <Typography>Delivery: Free</Typography>
            <Typography>Platform: Marketplace XYZ</Typography>
          </Box>
        </Paper>

        {/* RIGHT : RISK + RULES (2 PARTS) */}
        <Box className="right-panel">
          {/* RISK */}
          <Box className="risk-remain">
            <RingMeter score={riskScore} />
          </Box>

          {/* RULES */}
          <Box className="rules-row">
            <Paper className="rule-card obey">
              <Typography>✅ Obeying</Typography>
              <Box className="card-scroll">
                {obeying.map((i, idx) => (
                  <Box key={idx} className="rule-item">
                    <CheckCircleIcon /> {i}
                  </Box>
                ))}
              </Box>
            </Paper>

            <Paper className="rule-card not-obey">
              <Typography>❌ Not Obeying</Typography>
              <Box className="card-scroll">
                {notObeying.map((i, idx) => (
                  <Box key={idx} className="rule-item">
                    <CancelIcon /> {i}
                  </Box>
                ))}
              </Box>
            </Paper>
          </Box>

          <Button startIcon={<DownloadIcon />} className="download-btn">
            Download Compliance Report
          </Button>
        </Box>
      </Box>

      {/* RECOMMENDATION */}
      <Box className="recommendation-box">
        <Typography variant="h4">Recommendation</Typography>
        <Typography>
          Proceed with caution. Missing manufacturer and warranty
          information increases risk. Prefer verified sellers or official
          brand stores.
        </Typography>
      </Box>
    </Box>
  );
};

export default Verify;
