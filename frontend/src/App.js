import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import RecommendationPage from './components/RecommendationPage';
import AnalyticsPage from './components/AnalyticsPage';

function App() {
  return (
    <BrowserRouter>
      <div style={{ padding: 20 }}>
        <nav>
          <Link to="/">Recommend</Link> |{" "}
          <Link to="/analytics">Analytics</Link>
        </nav>
        <hr />
        <Routes>
          <Route path="/" element={<RecommendationPage />} />
          <Route path="/analytics" element={<AnalyticsPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
