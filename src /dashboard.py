import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="ZeTheta Compliance Portal", layout="wide")

# This function ensures it looks in the same folder where the script is running
def load_audit_data():
    log_path = os.path.join(os.path.dirname(__file__), "audit_log.jsonl")
    
    if not os.path.exists(log_path):
        st.warning(f"File not found at: {log_path}. Please run main.py first.")
        return pd.DataFrame()
    
    data = []
    with open(log_path, "r") as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
    return pd.DataFrame(data)

st.title("🛡️ ZeTheta Compliance Analytics")
df = load_audit_data()

if not df.empty:
    st.success(f"Loaded {len(df)} records.")
    st.dataframe(df)
else:
    st.info("The log file is empty. Run main.py to generate transactions.")
