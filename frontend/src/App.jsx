import { Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import Hero from "./components/Hero";
import About from "./components/About";
import Footer from "./components/Footer";
import Verify from "./pages/Verify";

const App = () => {
  return (
    <>
      <Header />

      <Routes>
        {/* HOME PAGE */}
        <Route
          path="/"
          element={
            <>
              <Hero />
              <About />
            </>
          }
        />

        {/* VERIFY PAGE */}
        <Route path="/verify" element={<Verify />} />
      </Routes>

      <Footer />
    </>
  );
};

export default App;
