# Brent Oil Price Analysis: Geopolitical & Economic Impact

## Overview
As a Data Scientist at **Birhan Energies**, I am tasked with analyzing how major political and economic events affect Brent oil prices. The oil market is notoriously volatile, making it difficult for investors, policymakers, and energy companies to manage risks. 

This project uses **Bayesian Change Point Analysis** (via PyMC) to identify structural breaks in oil prices and correlates them with historical events such as OPEC policy changes, regional conflicts, and global economic shocks.

## Folder Structure
The project is organized to support modularity (via the `src` folder), deep analysis (via `notebooks`), and insight delivery (via the `dashboard`).

```text
brent-oil-analysis/
├── .venv/                      # Python virtual environment
├── data/                       # Raw and processed datasets
│   ├── BrentOilPrices.csv      # Historical price data (1987-2022)
│   └── events_data.csv         # Researched geopolitical/economic events
├── notebooks/                  # Analysis and Modeling
│   ├── 01_eda_and_preprocessing.ipynb
│   └── 02_bayesian_change_point.ipynb
├── src/                        # Modular Python source code
│   ├── __init__.py
│   ├── data_loader.py          # Data cleaning and loading logic
│   ├── plotting.py             # Reusable visualization functions
│   └── stats_utils.py          # Statistical helper functions
├── dashboard/                  # Interactive Visualization
│   ├── backend/                # Flask API
│   └── frontend/               # React Application
├── tests/                      # Unit tests
├── .gitignore                  # Files to ignore in Git
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── setup.py                    # Package configuration
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd brent-oil-analysis
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows Git Bash
```

### 3. Install Dependencies
Due to potential network SSL restrictions, use the following command:
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
pip install -e .
```

## Tasks & Deliverables

### Task 1: Foundation for Analysis (Interim Report)
**Objective:** Define the workflow and understand data properties.
*   **Deliverables:**
    *   **Workflow:** Outline steps from data ingestion to insight generation.
    *   **Event Dataset:** A structured CSV containing 10-15 key geopolitical events.
    *   **EDA:** Analysis of trends, volatility (log returns), and stationarity (ADF test).
    *   **Assumptions:** Documentation of statistical assumptions and the difference between correlation and causation.

### Task 2: Change Point Modeling (Final Report)
**Objective:** Use Bayesian inference to identify and quantify price shifts.
*   **Methodology:** Implement a Switch Point model in **PyMC**.
*   **Quantification:** 
    *   Identify specific dates ($\tau$) of structural breaks.
    *   Calculate mean prices before and after ($\mu_1, \mu_2$).
    *   Quantify the percentage impact of events (e.g., COVID-19, Ukraine War).

### Task 3: Interactive Dashboard
**Objective:** Visualize results for stakeholders.
*   **Backend:** Flask API serving price data and model results.
*   **Frontend:** React dashboard using **Recharts** to display:
    *   Historical trends.
    *   Event-specific "highlights" on the price chart.
    *   Key indicators (volatility, average price shifts).

## Final Report Structure
The final submission includes a comprehensive report (Blog post or PDF) covering:
1.  **Executive Summary:** High-level findings for Birhan Energies' clients.
2.  **Methodology:** Explanation of Bayesian Change Point detection.
3.  **Insights:** Quantified impact of 5+ major events.
4.  **Dashboard screenshots:** Evidence of the functional visualization tool.
5.  **Conclusion:** Strategic advice for investors and policymakers based on the data.


## Data Fields
*   **Date:** The date of the recorded Brent oil price (May 20, 1987, to September 30, 2022).
*   **Price:** Price in USD per barrel.


## Team & Support
*   **Tutors:** Kerod, Filimon, Mahbubah
*   **Communication:** Slack `#all-week11`
*   **Consultancy:** Birhan Energies

---
*Developed as part of the 10 Academy Phase 11 Challenge.*
