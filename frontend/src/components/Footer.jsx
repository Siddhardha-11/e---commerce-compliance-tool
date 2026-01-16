import { Box, Typography } from "@mui/material";

const Footer = () => {
  return (
    <Box
      sx={{
        height: "70px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        borderTop: "1px solid #e5e7eb",
      }}
    >
      <Typography sx={{ fontSize: "14px", color: "#64748b" }}>
        © 2026 SafeBuy. All rights reserved. This is a demo project. Don't rely on us.
      </Typography>
    </Box>
  );
};

export default Footer;
