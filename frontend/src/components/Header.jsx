import { AppBar, Toolbar, Typography, Button, Box } from "@mui/material";
import { useLocation } from "react-router-dom";

const Header = () => {
  const location = useLocation();
  const isVerifyPage = location.pathname === "/verify";

  const handleScroll = (id) => {
    const section = document.getElementById(id);
    section?.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <AppBar
      position="static"
      elevation={0}
      sx={{
        backgroundColor: "#ffffff",
        borderBottom: "1px solid #e5e7eb",
      }}
    >
      <Toolbar sx={{ justifyContent: "space-between" }}>
        {/* LOGO */}
        <Box sx={{ display: "flex", alignItems: "center" }}>
          <Typography variant="h6" sx={{ fontWeight: 700, color: "#2563eb" }}>
            Safe
          </Typography>
          <Typography variant="h6" sx={{ fontWeight: 700, color: "#9C86D4" }}>
            Buy
          </Typography>
        </Box>

        {/* NAV */}
        {!isVerifyPage && (
          <Button
            sx={{ fontSize: "16px", color: "#475569" }}
            onClick={() => handleScroll("about")}
          >
            About
          </Button>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Header;
