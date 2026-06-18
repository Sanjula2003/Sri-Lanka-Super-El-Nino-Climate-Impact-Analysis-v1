import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="Super El Niño Analysis",
    page_icon="🌋",
    layout="wide"
)

# ----------------------------------
# Load Data
# ----------------------------------

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

df = pd.read_csv(
    BASE_DIR / "data" / "sri_lanka_climate_dataset.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

# ----------------------------------
# Recreate ENSO Categories
# ----------------------------------

def classify_enso(mei):

    if mei >= 1.5:
        return "Super El Nino"

    elif mei >= 0.5:
        return "El Nino"

    elif mei <= -0.5:
        return "La Nina"

    else:
        return "Neutral"


df["ENSO_Category"] = df["MEI"].apply(
    classify_enso
)

# ----------------------------------
# Rainfall Anomaly
# ----------------------------------

overall_rain = df["Rainfall"].mean()

df["Rainfall_Anomaly"] = (
    df["Rainfall"] - overall_rain
)

# ----------------------------------
# Temperature Anomaly
# ----------------------------------

overall_temp = df["Temperature"].mean()

df["Temperature_Anomaly"] = (
    df["Temperature"] - overall_temp
)

# ----------------------------------
# Super El Niño Dataset
# ----------------------------------

super_df = df[
    df["ENSO_Category"] == "Super El Nino"
]

# ----------------------------------
# Title
# ----------------------------------

st.title("🌋 Super El Niño Impact Analysis")

st.markdown(
    """
    This page evaluates how Sri Lanka's climate changed
    during Super El Niño events using rainfall,
    temperature, and ENSO indicators.
    """
)

# ----------------------------------
# KPI Cards
# ----------------------------------

st.subheader("Key Findings")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Super El Niño Months",
    len(super_df)
)

c2.metric(
    "Districts",
    df["District"].nunique()
)

c3.metric(
    "Avg Rainfall Anomaly",
    round(
        super_df["Rainfall_Anomaly"].mean(),
        2
    )
)

c4.metric(
    "Avg Temperature Anomaly",
    round(
        super_df["Temperature_Anomaly"].mean(),
        2
    )
)

# ----------------------------------
# Rainfall Ranking
# ----------------------------------

st.subheader(
    "🌧 Rainfall Impact Ranking"
)

rain_rank = (
    super_df
    .groupby("District")
    ["Rainfall_Anomaly"]
    .mean()
    .reset_index()
    .sort_values(
        "Rainfall_Anomaly",
        ascending=False
    )
)

fig_rain = px.bar(
    rain_rank,
    x="District",
    y="Rainfall_Anomaly",
    title="Average Rainfall Anomaly During Super El Niño"
)

st.plotly_chart(
    fig_rain,
    use_container_width=True
)

# ----------------------------------
# Temperature Ranking
# ----------------------------------

st.subheader(
    "🌡 Temperature Impact Ranking"
)

temp_rank = (
    super_df
    .groupby("District")
    ["Temperature_Anomaly"]
    .mean()
    .reset_index()
    .sort_values(
        "Temperature_Anomaly",
        ascending=False
    )
)

fig_temp = px.bar(
    temp_rank,
    x="District",
    y="Temperature_Anomaly",
    title="Average Temperature Anomaly During Super El Niño"
)

st.plotly_chart(
    fig_temp,
    use_container_width=True
)

# ----------------------------------
# SECII Index
# ----------------------------------

st.subheader(
    "🏆 SECII Ranking"
)

secii = (
    super_df
    .groupby("District")
    .agg({
        "Rainfall_Anomaly":"mean",
        "Temperature_Anomaly":"mean",
        "MEI":"mean"
    })
)

secii["SECII"] = (
    (
        secii["Rainfall_Anomaly"] /
        secii["Rainfall_Anomaly"].max()
    ) * 0.4
    +
    (
        secii["Temperature_Anomaly"] /
        secii["Temperature_Anomaly"].max()
    ) * 0.3
    +
    (
        secii["MEI"] /
        secii["MEI"].max()
    ) * 0.3
)

secii = secii.sort_values(
    "SECII",
    ascending=False
)

fig_secii = px.bar(
    secii.reset_index(),
    x="District",
    y="SECII",
    title="Super El Niño Climate Impact Index"
)

st.plotly_chart(
    fig_secii,
    use_container_width=True
)

# ----------------------------------
# Top Impacted District
# ----------------------------------

top_district = (
    secii.index[0]
)

top_score = (
    secii["SECII"].iloc[0]
)

st.success(
    f"""
    Most impacted district during Super El Niño:
    
    🏆 {top_district}
    
    SECII Score = {top_score:.3f}
    """
)

# ----------------------------------
# Super El Niño Records
# ----------------------------------

st.subheader(
    "📋 Super El Niño Observations"
)

st.dataframe(
    super_df.sort_values(
        "Date",
        ascending=False
    ),
    use_container_width=True
)