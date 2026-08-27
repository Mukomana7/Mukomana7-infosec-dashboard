import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="InfoSec Awareness Dashboard", layout="wide")
st.title("🛡️ Bank Security Awareness & Risk Dashboard")

# 1. Sample Data
data = {
    "Department": [
        "Retail Banking",
        "Investment Banking",
        "Compliance",
        "IT & Ops",
        "HR",
    ],
    "Phishing Clicks": [12, 5, 2, 1, 8],
    "Phishing Reported": [34, 19, 28, 45, 12],
    "Training Completion %": [82, 91, 98, 95, 76],
}
df = pd.DataFrame(data)

# 2. Executive Metrics
c1, c2, c3 = st.columns(3)
c1.metric("Avg Training Completion", f"{df['Training Completion %'].mean():.1f}%")
c2.metric("Total Phishing Clicks", f"{df['Phishing Clicks'].sum()}")
c3.metric("Total Phishing Reports", f"{df['Phishing Reported'].sum()}")

st.markdown("---")

# 3. Charts
col1, col2 = st.columns(2)
with col1:
    st.subheader("Training Completion by Department")
    fig1 = px.bar(
        df,
        x="Department",
        y="Training Completion %",
        color="Training Completion %",
        color_continuous_scale="RdYlGn",
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Phishing Simulation Performance")
    fig2 = px.bar(
        df,
        x="Department",
        y=["Phishing Clicks", "Phishing Reported"],
        barmode="group",
    )
    st.plotly_chart(fig2, use_container_width=True)