import { BrowserRouter, Routes, Route } from "react-router-dom";
import EcoAIFinder from "./components/EcoAIFinder";
import Home from "./components/HomePage/HeroSection";
import TextAi from "./components/TextAi";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/options" element={<EcoAIFinder />} />
        <Route path="/askAI" element={<TextAi />} />
        {/* Add other routes here */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
