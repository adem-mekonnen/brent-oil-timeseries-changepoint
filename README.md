# Birhan Energies: Brent Oil Change Point Analysis
### **Strategic Intelligence on Geopolitical & Economic Shocks (1987-2022)**

## 1. Project Overview
As a Data Scientist at **Birhan Energies**, I conducted a comprehensive analysis to understand how major political decisions, conflicts, and economic sanctions influence Brent oil prices. The oil market is characterized by high instability; this project provides a data-driven framework to quantify that instability.

Using **Bayesian Change Point Analysis** (via PyMC), we identified "Structural Breaks" in the market—moments where the fundamental price floor shifted permanently rather than temporarily.

## 2. Folder Structure
The project is organized into a modular full-stack application to ensure reproducibility and clean separation of concerns.

```text
brent-oil-analysis/
├── data/                       # Data storage
│   ├── BrentOilPrices.csv      # Raw daily price data
│   └── events_data.csv         # Curated geopolitical events (13 events)
├── notebooks/                  # Statistical Analysis
│   ├── 01_eda_and_preprocessing.ipynb  # Stationarity & Trend analysis
│   └── 02_bayesian_change_point.ipynb  # PyMC Bayesian Modeling
├── src/                        # Modular Python Package (Core Logic)
│   ├── data_loader.py          # Centralized CSV processing
│   ├── plotting.py             # Matplotlib/Seaborn wrappers
│   └── stats_utils.py          # Statistical tests (ADF, etc.)
├── dashboard/                  # Deployment
│   ├── backend/                # Flask API
│   │   ├── api/routes.py       # JSON Endpoints
│   │   ├── data/               # Model output (analysis_results.json)
│   │   └── app.py              # Server entry point
│   └── frontend/               # React Dashboard (Vite + TypeScript)
│       ├── src/App.tsx         # Dashboard UI with Recharts
│       └── src/App.css         # Professional Styling
├── requirements.txt            # Project dependencies
├── setup.py                    # Package configuration for 'src'
└── README.md                   # Project documentation
```

---

## 3. Installation & Setup

### Environment Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate  # On Windows Git Bash

# Install dependencies (with SSL certificate bypass)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Install the internal 'src' package in editable mode
pip install -e .
```
## 4. Implementation Details

### **Task 1: The Foundation**
*   **EDA:** Conducted Augmented Dickey-Fuller (ADF) tests proving price non-stationarity ($p > 0.05$).
*   **Event Research:** Compiled a dataset of 13 major events including the Gulf War, 2014 OPEC market share war, and the 2022 Ukraine invasion.
*   **Volatility:** Identified volatility clustering through log-return analysis.

### **Task 2: Bayesian Modeling (PyMC)**
*   **Model:** Implemented a Switch-Point model using MCMC sampling.
*   **Quantification:** Identified a structural break on **March 9, 2020**, where the mean price floor collapsed by **61.6%** (from ~$54 to ~$21) due to the COVID-19 pandemic and OPEC+ negotiations.

### **Task 3: Interactive Dashboard**
*   **Backend:** Flask server providing endpoints for historical prices, geopolitical events, and Bayesian model results.
*   **Frontend:** A modern React/Vite dashboard using **Recharts** to visualize event overlays and model-detected shifts.

---

## 5. How to Run the Project

### 1. Generate Analysis
Run all cells in `notebooks/02_bayesian_change_point.ipynb` to generate the `analysis_results.json` file.

### 2. Start Backend (Flask)
```bash
cd dashboard/backend
python app.py
```
*The API will be available at `http://localhost:5000`*

### 3. Start Frontend (React/Vite)
```bash
cd dashboard/frontend
npm install
npm run dev
```
*The Dashboard will be available at `http://localhost:5173`*

## 6. Key Business Insights
*   **Regime Shifts:** Unlike temporary spikes, events like COVID-19 cause "regime shifts" that invalidate previous 200-day moving averages.
*   **Actionable Advice:** Birhan Energies recommends that stakeholders use Bayesian change point detection to trigger "immediate hedging" when a structural break is confirmed by the model, as price floors take months or years to recover.
## 7. Submission Details
*   **Interim Report:** Submitted Feb 8, 2026.
*   **Final Submission:** Feb 10, 2026.
*   **Tutors:** Kerod, Filimon, Mahbubah.

---
*Developed for the Birhan Energies Consultancy Intern Program.*
