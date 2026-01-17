import { Box, Typography, Grid, Paper } from "@mui/material";
import { motion } from "framer-motion";
import VerifiedIcon from "@mui/icons-material/Verified";
import InsightsIcon from "@mui/icons-material/Insights";

const features = [
  {
    icon: <VerifiedIcon fontSize="large" />,
    title: "Compliance Check",
    desc: "Verify products against essential consumer-protection rules automatically.",
  },
  {
    icon: <InsightsIcon fontSize="large" />,
    title: "Risk Insights",
    desc: "Get a clear risk score and actionable insights in seconds.",
  },
];

const About = () => {
  return (
    <Box
      id="about"
      sx={{
        py: { xs: 10, md: 14 },
        px: { xs: 3, md: 10 },
        background:
          "linear-gradient(180deg, #ffffff 0%, #f8fafc 100%)",
      }}
    >
      {/* HEADING */}
      <Box sx={{ mt: -7, mb: 8 }}>
        <Typography
          variant="h3"
          sx={{ fontWeight: 800, color: "#0f172a", mb: 2 }}
        >
          Why SafeBuy?
        </Typography>

        <Typography
          sx={{
            fontSize: "18px",
            color: "#475569",
            maxWidth: "700px",
            lineHeight: 1.8,
            mb: -3, 
          }}
        >
          Online shopping shouldn’t feel risky. SafeBuy helps you
          verify products and sellers instantly, so you can shop with
          confidence and clarity.
        </Typography>
      </Box>

      {/* FEATURE CARDS */}
      <Grid container spacing={4}>
        {features.map((item, index) => (
          <Grid item xs={12} md={6} key={index}>
            <motion.div
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6, delay: index * 0.15 }}
              viewport={{ once: true }}
            >
              <Paper
                elevation={0}
                sx={{
                  p: 4,
                  height: "100%",
                  borderRadius: "16px",
                  border: "1px solid #e5e7eb",
                  transition: "all 0.3s ease",
                  "&:hover": {
                    transform: "translateY(-6px)",
                    boxShadow:
                      "0 20px 40px rgba(37, 99, 235, 0.15)",
                  },
                }}
              >
                <Box
                  sx={{
                    color: "#2563eb",
                    mb: 2,
                  }}
                >
                  {item.icon}
                </Box>

                <Typography
                  variant="h6"
                  sx={{ fontWeight: 700, mb: 1 }}
                >
                  {item.title}
                </Typography>

                <Typography
                  sx={{
                    color: "#475569",
                    lineHeight: 1.6,
                  }}
                >
                  {item.desc}
                </Typography>
              </Paper>
            </motion.div>
          </Grid>
        ))}
      </Grid>

      {/* MISSION STATEMENT */}
      <Box
        sx={{
          mt: 5,
          mb: -7,
          p: { xs: 4, md: 6 },
          borderRadius: "20px",
          background:
            "linear-gradient(135deg, #2563eb, #38bdf8)",
          color: "#ffffff",
        }}
      >
        <Typography
          variant="h4"
          sx={{ fontWeight: 700, mb: 2 }}
        >
          Our Mission
        </Typography>

        <Typography sx={{ fontSize: "18px", lineHeight: 1.7 }}>
          To make e-commerce safer by empowering users with transparent,
          automated compliance checks—before they click “Buy Now”.
        </Typography>
      </Box>
    </Box>
  );
};

export default About;
