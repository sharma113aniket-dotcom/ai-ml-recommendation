import React, { useState } from 'react';
import axios from 'axios';

export default function RecommendationPage() {
  const [prompt, setPrompt] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:8000/api/recommend', {
        prompt: prompt, k: 6
      });
      setResults(res.data.results || []);
    } catch (err) {
      alert("Error contacting backend: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Product Recommendation (Conversation Style)</h2>
      <form onSubmit={handleSubmit}>
        <input
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
          placeholder="Describe what you want (e.g., 'wooden study table for small room')"
          style={{ width: '60%' }}
        />
        <button type="submit">Ask</button>
      </form>

      {loading && <p>Loading...</p>}

      <div style={{ display: 'flex', flexWrap: 'wrap', marginTop: 20 }}>
        {results.map((r, idx) => (
          <div key={idx} style={{ border: '1px solid #ddd', padding: 10, margin: 8, width: 260 }}>
            <img
              src={r.images || "https://via.placeholder.com/240"}
              alt={r.title}
              style={{ width: '100%', height: 160, objectFit: 'cover' }}
            />
            <h4>{r.title}</h4>
            <p><b>Price:</b> {r.price}</p>
            <p style={{ fontSize: 13 }}>{r.description?.slice(0, 120)}...</p>
          </div>
        ))}
      </div>
    </div>
  );
}
