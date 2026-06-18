import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Extreme Event Detection",
    page_icon="⚠️",
    layout="wide"
)

st.title("⚠️ Extreme Climate Event Detection")

df = pd.read_csv(
    "data/sri_lanka_climate_dataset.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# Rainfall Thresholds
# -----------------------------

flood_threshold = (
    df["Rainfall"].quantile(0.95)
)

drought_threshold = (
    df["Rainfall"].quantile(0.05)
)

# -----------------------------
# Event Classification
# -----------------------------

def classify_event(rain):

    if rain >= flood_threshold:
        return "Flood Risk"

    elif rain <= drought_threshold:
        return "Drought Risk"

    else:
        return "Normal"


df["Extreme_Event"] = (
    df["Rainfall"]
    .apply(classify_event)
)

# -----------------------------
# KPI Cards
# -----------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Flood Events",
    len(
        df[
            df["Extreme_Event"]
            == "Flood Risk"
        ]
    )
)

col2.metric(
    "Drought Events",
    len(
        df[
            df["Extreme_Event"]
            == "Drought Risk"
        ]
    )
)

col3.metric(
    "Total Records",
    len(df)
)

# -----------------------------
# Event Distribution
# -----------------------------

event_counts = (
    df["Extreme_Event"]
    .value_counts()
    .reset_index()
)

event_counts.columns = [
    "Event",
    "Count"
]

fig = px.pie(
    event_counts,
    names="Event",
    values="Count",
    title="Climate Event Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# District Vulnerability
# -----------------------------

st.subheader(
    "District Vulnerability Ranking"
)

district_risk = (
    df[
        df["Extreme_Event"] != "Normal"
    ]
    .groupby("District")
    .size()
    .sort_values(
        ascending=False
    )
)

st.bar_chart(
    district_risk
)

# -----------------------------
# Super El Niño Event Analysis
# -----------------------------

st.subheader(
    "Extreme Events During Super El Niño"
)

super_df = df[
    df["MEI"] >= 1.5
]

super_df["Extreme_Event"] = (
    super_df["Rainfall"]
    .apply(classify_event)
)

event_summary = (
    super_df["Extreme_Event"]
    .value_counts()
)

st.dataframe(
    event_summary
)

# -----------------------------
# Event Table
# -----------------------------

st.subheader(
    "Detected Extreme Events"
)

st.dataframe(
    df[
        df["Extreme_Event"] != "Normal"
    ]
    .sort_values(
        "Date",
        ascending=False
    ),
    use_container_width=True
)