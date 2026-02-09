import pandas as pd
import os

# Define the data
events_data = [
    {"Date": "1990-08-02", "Event": "Invasion of Kuwait", "Type": "Conflict", "Description": "Iraq invades Kuwait, triggering Gulf War oil spike."},
    {"Date": "1991-01-17", "Event": "Operation Desert Storm", "Type": "Conflict", "Description": "US-led coalition begins combat."},
    {"Date": "2001-09-11", "Event": "9/11 Attacks", "Type": "Geopolitical", "Description": "Terrorist attacks in US cause market uncertainty."},
    {"Date": "2003-03-20", "Event": "Iraq War", "Type": "Conflict", "Description": "US invasion of Iraq."},
    {"Date": "2008-07-11", "Event": "2008 Financial Crisis", "Type": "Economic", "Description": "Oil peaks at $147 before crashing due to global recession."},
    {"Date": "2011-02-15", "Event": "Libyan Civil War", "Type": "Conflict", "Description": "Uprising against Gaddafi disrupts supply."},
    {"Date": "2014-11-27", "Event": "OPEC Market Share Strategy", "Type": "Policy", "Description": "OPEC decides not to cut production despite glut."},
    {"Date": "2016-01-16", "Event": "Iran Sanctions Lifted", "Type": "Policy", "Description": "Nuclear deal implementation increases supply."},
    {"Date": "2016-11-30", "Event": "OPEC+ Cuts", "Type": "Policy", "Description": "OPEC and Russia agree to cut production."},
    {"Date": "2019-09-14", "Event": "Saudi Aramco Attack", "Type": "Conflict", "Description": "Drone attacks on Abqaiq processing facility."},
    {"Date": "2020-03-06", "Event": "OPEC+ Deal Collapse", "Type": "Policy", "Description": "Russia and Saudi Arabia start price war."},
    {"Date": "2020-03-11", "Event": "COVID-19 Pandemic", "Type": "Economic", "Description": "WHO declares pandemic; demand collapses."},
    {"Date": "2022-02-24", "Event": "Russia-Ukraine War", "Type": "Conflict", "Description": "Russia invades Ukraine; sanctions follow."}
]

# Create DataFrame
df = pd.DataFrame(events_data)

# Ensure the 'data' directory exists
os.makedirs('data', exist_ok=True)

# Save to CSV
df.to_csv('data/events_data.csv', index=False)
print("Success! 'data/events_data.csv' has been created.")