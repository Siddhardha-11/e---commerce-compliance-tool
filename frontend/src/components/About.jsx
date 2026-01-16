import { Box, Typography } from "@mui/material";

const About = () => {
  return (
    <Box
      id="about"
      sx={{
        minHeight: "100vh",
        px: { xs: 3, md: 10 },
        py: { xs: 8, md: 12 },
        backgroundColor: "#f8fafc",
      }}
    >
      <Typography
        variant="h3"
        sx={{ fontWeight: 700, mb: 3, color: "#0f172a" }}
      >
        About SafeBuy
      </Typography>

      <Typography
        sx={{
          fontSize: "18px",
          maxWidth: "800px",
          lineHeight: 1.7,
          color: "#475569",
        }}
      >
        SafeBuy is an AI-powered compliance screening platform designed
        to help consumers shop confidently online. We analyze e-commerce
        product listings and seller information to verify compliance
        with essential consumer-protection rules.
        <br /><br />
        Our goal is to reduce fraud, improve transparency, and empower
        users to make informed purchasing decisions—before they click
        “Buy Now”.
      </Typography>
    </Box>
  );
};

export default About;
