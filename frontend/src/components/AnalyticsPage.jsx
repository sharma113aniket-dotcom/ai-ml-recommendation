import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function AnalyticsPage() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/analytics')
      .then(res => setStats(res.data))
      .catch(err => console.error('Error fetching analytics:', err));
  }, []);

  if (!stats) return <div>Loading analytics...</div>;

  return (
    <div>
      <h2>Dataset Analytics</h2>
      <ul>
        <li><b>Number of products:</b> {stats.num_products}</li>
        <li><b>Unique brands:</b> {stats.unique_brands}</li>
        <li><b>Unique categories:</b> {stats.categories_count}</li>
      </ul>
      <p>You can add charts here later (e.g. Chart.js, Recharts).</p>
    </div>
  );
}
