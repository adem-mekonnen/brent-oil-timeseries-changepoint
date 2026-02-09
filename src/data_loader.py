import pandas as pd
import numpy as np
import os

def get_data_path(filename):
    """
    Dynamically finds the path to the data folder.
    Works whether called from notebooks/, src/, or dashboard/backend/
    """
    # Start from the current file's directory (src/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to the project root (brent-oil-analysis/)
    project_root = os.path.dirname(current_dir)
    return os.path.join(project_root, 'data', filename)

def load_oil_data():
    """
    Loads and cleans the Brent Oil Prices dataset.
    Standardizes columns and converts dates.
    """
    path = get_data_path('BrentOilPrices.csv')
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing dataset at {path}")

    # Load data
    df = pd.read_csv(path)

    # 1. Clean column names (Handle 'Date', 'Price' or 'date', 'price')
    df.columns = [c.strip().capitalize() for c in df.columns]

    # 2. Convert Date (Format: 20-May-87)
    # %d = day, %b = short month (May), %y = 2-digit year (87)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', errors='coerce')

    # 3. Sort by date (Critical for time series analysis)
    df = df.sort_values('Date').reset_index(drop=True)

    # 4. Handle Missing Values
    df = df.dropna(subset=['Price'])

    # 5. Feature Engineering: Log Returns
    # Essential for Task 2 (Change Point Analysis)
    df['Log_Return'] = np.log(df['Price'] / df['Price'].shift(1))

    return df

def load_events_data():
    """
    Loads the researched geopolitical/economic events dataset.
    """
    path = get_data_path('events_data.csv')
    
    if not os.path.exists(path):
        # Return an empty dataframe with correct columns if file doesn't exist yet
        return pd.DataFrame(columns=['Date', 'Event', 'Type', 'Description'])

    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def get_data_subset(df, start_date, end_date):
    """
    Utility to slice data for specific Task 2 windows (e.g., COVID Era).
    """
    mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    return df.loc[mask].copy()

if __name__ == "__main__":
    # Test script to verify loading works
    try:
        oil_df = load_oil_data()
        print("✅ Oil Data Loaded successfully!")
        print(oil_df.head())
        
        events_df = load_events_data()
        print("\n✅ Events Data Loaded successfully!")
        print(events_df.head())
    except Exception as e:
        print(f"❌ Error loading data: {e}")