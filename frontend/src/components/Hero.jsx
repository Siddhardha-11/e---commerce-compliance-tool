import { Typography, Button } from "@mui/material";
import { motion } from "framer-motion";
import "../style/Hero.css";
import { useNavigate } from "react-router-dom";

const Hero = () => {
  const navigate = useNavigate();
  return (
    <div className="hero-container">
      {/* LEFT CONTENT */}
      <motion.div
        className="hero-content"
        initial={{ opacity: 0, x: -40 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
      >
        <motion.h2
          className="hero-title"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.6 }}
        >
          Shop Smart.
          <br />
          Shop Safe.
        </motion.h2>

        <motion.p
          className="hero-description"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4, duration: 0.6 }}
        >
          SafeBuy verifies e-commerce products and sellers against
          essential consumer-protection rules before you buy.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.6, duration: 0.4 }}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.97 }}
        >
          <Button
            variant="contained"
            size="large"
            className="hero-button"
            onClick={() => navigate("/verify")}
          >
            Verify Now
          </Button>
        </motion.div>
      </motion.div>

      {/* RIGHT IMAGE */}
      <motion.div
        className="hero-image"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3, duration: 0.8 }}
      />
    </div>
  );
};

export default Hero;
