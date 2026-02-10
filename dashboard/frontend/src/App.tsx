import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  ResponsiveContainer, ReferenceLine, Label, ComposedChart
} from 'recharts';
import { Calendar, ShieldAlert, Activity, Globe } from 'lucide-react';
import './App.css';

interface PriceData { Date: string; Price: number; }
interface EventData { Date: string; Event: string; Type: string; Description: string; }
interface AnalysisResult { event: string; detected_date: string; mu_before: number; mu_after: number; impact: string; }

function App() {
  const [prices, setPrices] = useState<PriceData[]>([]);
  const [events, setEvents] = useState<EventData[]>([]);
  const [analysis, setAnalysis] = useState<AnalysisResult[]>([]);
  const [startDate, setStartDate] = useState('2019-01-01');
  const [endDate, setEndDate] = useState('2022-09-30');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const [p, e, a] = await Promise.all([
          axios.get(`http://localhost:5000/api/prices?start=${startDate}&end=${endDate}`),
          axios.get('http://localhost:5000/api/events'),
          axios.get('http://localhost:5000/api/analysis')
        ]);
        setPrices(p.data);
        setEvents(e.data);
        setAnalysis(a.data);
      } catch (err) {
        console.error("Backend offline:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [startDate, endDate]);

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <div className="logo-section">
          <Globe size={32} color="#2563eb" />
          <div>
            <h1 style={{ margin: 0, fontSize: '1.5rem' }}>Birhan Energies</h1>
            <p style={{ margin: 0, color: '#64748b', fontSize: '0.875rem' }}>Brent Oil Strategic Intelligence</p>
          </div>
        </div>
        
        <div className="filter-group">
          <div className="input-box">
            <Calendar size={16} color="#64748b" />
            <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
          </div>
          <div className="input-box">
            <Calendar size={16} color="#64748b" />
            <input type="date" value={endDate} onChange={(e) => setEndDate(e.target.value)} />
          </div>
        </div>
      </header>

      <section className="kpi-grid">
        {analysis.map((item, i) => (
          <div key={i} className="kpi-card highlight">
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#64748b', fontSize: '0.875rem', marginBottom: '0.5rem' }}>
              <ShieldAlert size={18} color="#ef4444" />
              <span>{item.event}</span>
            </div>
            <div style={{ fontSize: '1.8rem', fontWeight: 700 }}>{item.impact}</div>
            <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '0.5rem' }}>Detected Break: {item.detected_date}</div>
          </div>
        ))}
        <div className="kpi-card">
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#64748b', fontSize: '0.875rem', marginBottom: '0.5rem' }}>
            <Activity size={18} color="#10b981" />
            <span>Market Status</span>
          </div>
          <div style={{ fontSize: '1.8rem', fontWeight: 700, color: '#10b981' }}>Volatile</div>
          <div style={{ fontSize: '0.75rem', color: '#94a3b8', marginTop: '0.5rem' }}>Analysis Mode: Switch-Point</div>
        </div>
      </section>

      <section className="chart-section">
        <div style={{ marginBottom: '1rem' }}>
          <h3 style={{ margin: 0 }}>Price Impact Visualization</h3>
          <p style={{ margin: 0, color: '#64748b', fontSize: '0.875rem' }}>Red: Events | Green: Model Detected Shifts</p>
        </div>
        <div className="chart-wrapper">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart data={prices}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
              <XAxis dataKey="Date" minTickGap={60} tick={{fontSize: 12}} />
              <YAxis domain={['auto', 'auto']} tick={{fontSize: 12}} />
              <Tooltip />
              <Legend />
              <Line name="Brent Price" type="monotone" dataKey="Price" stroke="#2563eb" strokeWidth={3} dot={false} />
              
              {events.map((ev, idx) => (
                <ReferenceLine key={`ev-${idx}`} x={ev.Date} stroke="#ef4444" strokeDasharray="4 4">
                  <Label value={ev.Event} position="top" fill="#ef4444" fontSize={10} fontWeight="bold" />
                </ReferenceLine>
              ))}

              {analysis.map((an, idx) => (
                <ReferenceLine key={`an-${idx}`} x={an.detected_date} stroke="#10b981" strokeWidth={3}>
                  <Label value="MODEL SHIFT" position="insideBottomLeft" fill="#059669" fontSize={10} fontWeight="bold" />
                </ReferenceLine>
              ))}
            </ComposedChart>
          </ResponsiveContainer>
        </div>
      </section>

      {loading && <div className="loading-overlay">Syncing Analysis...</div>}
    </div>
  );
}

export default App;