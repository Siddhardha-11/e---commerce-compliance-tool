import { AppBar, Toolbar, Typography, Button, Box } from "@mui/material";

const Header = () => {
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
        <Typography
          variant="h6"
          sx={{ fontWeight: 700, color: "#2563eb" }}
        >
          Safe
        </Typography>

         <Typography
          variant="h6"
          sx={{ fontWeight: 700, color: "#9C86D4" , ml:-153 }}
        >
          Buy
        </Typography>

        <Box>
          <Button sx={{  fontSize: "16px" , color: "#475569" }} onClick={() => handleScroll("about")}>
            About
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
