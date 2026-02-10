from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json
import os
import sys

# Ensure src is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.data_loader import load_oil_data, load_events_data

app = Flask(__name__)
CORS(app)

@app.route('/api/prices')
def get_prices():
    df = load_oil_data()
    # Filter for the last 10 years to improve frontend performance
    df = df[df['Date'].dt.year >= 2012]
    return jsonify(df.assign(Date=df['Date'].dt.strftime('%Y-%m-%d')).to_dict(orient='records'))

@app.route('/api/events')
def get_events():
    events = load_events_data()
    return jsonify(events.to_dict(orient='records'))

@app.route('/api/analysis')
def get_analysis():
    path = os.path.join(os.path.dirname(__file__), 'data', 'analysis_results.json')
    with open(path, 'r') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    app.run(port=5000, debug=True)