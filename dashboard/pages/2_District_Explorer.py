import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="District Explorer",
    page_icon="📍",
    layout="wide"
)

# ----------------------------------
# Load Data
# ----------------------------------

df = pd.read_csv(
    "data/sri_lanka_climate_dataset.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

# ----------------------------------
# Title
# ----------------------------------

st.title("📍 District Climate Explorer")
st.markdown(
    """
    Explore rainfall, temperature, and ENSO patterns
    across Sri Lankan districts.
    """
)

# ----------------------------------
# Filters
# ----------------------------------

col1, col2 = st.columns(2)

years = sorted(
    df["Date"].dt.year.unique()
)

with col1:
    selected_year = st.selectbox(
        "Select Year",
        ["All"] + list(years)
    )

if selected_year != "All":
    df = df[
        df["Date"].dt.year == selected_year
    ]

with col2:
    district = st.selectbox(
        "Select District",
        sorted(df["District"].unique())
    )

district_df = df[
    df["District"] == district
]

# ----------------------------------
# KPI Section
# ----------------------------------

st.subheader("📊 Climate Summary")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "Avg Rainfall",
    f"{district_df['Rainfall'].mean():.2f}"
)

kpi2.metric(
    "Avg Temperature",
    f"{district_df['Temperature'].mean():.2f}°C"
)

kpi3.metric(
    "Max Rainfall",
    f"{district_df['Rainfall'].max():.2f}"
)

kpi4.metric(
    "Avg MEI",
    f"{district_df['MEI'].mean():.2f}"
)

# ----------------------------------
# Rainfall Trend
# ----------------------------------

st.subheader("🌧 Rainfall Trend")

fig_rain = px.line(
    district_df,
    x="Date",
    y="Rainfall",
    title=f"{district} Monthly Rainfall",
    markers=True
)

fig_rain.update_layout(
    height=500
)

st.plotly_chart(
    fig_rain,
    use_container_width=True
)

# ----------------------------------
# Temperature Trend
# ----------------------------------

st.subheader("🌡 Temperature Trend")

fig_temp = px.line(
    district_df,
    x="Date",
    y="Temperature",
    title=f"{district} Monthly Temperature",
    markers=True
)

fig_temp.update_layout(
    height=500
)

st.plotly_chart(
    fig_temp,
    use_container_width=True
)

# ----------------------------------
# Rainfall Distribution
# ----------------------------------

st.subheader("📈 Rainfall Distribution")

fig_hist = px.histogram(
    district_df,
    x="Rainfall",
    nbins=20,
    title=f"{district} Rainfall Distribution"
)

fig_hist.update_layout(
    height=500
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# ----------------------------------
# Temperature Distribution
# ----------------------------------

st.subheader("📉 Temperature Distribution")

fig_temp_hist = px.histogram(
    district_df,
    x="Temperature",
    nbins=20,
    title=f"{district} Temperature Distribution"
)

fig_temp_hist.update_layout(
    height=500
)

st.plotly_chart(
    fig_temp_hist,
    use_container_width=True
)

# ----------------------------------
# Monthly Averages
# ----------------------------------

st.subheader("📅 Monthly Climate Pattern")

monthly_avg = district_df.copy()

monthly_avg["Month"] = (
    monthly_avg["Date"]
    .dt.month
)

monthly_pattern = (
    monthly_avg
    .groupby("Month")
    [["Rainfall", "Temperature"]]
    .mean()
    .reset_index()
)

fig_month = px.line(
    monthly_pattern,
    x="Month",
    y=["Rainfall", "Temperature"],
    markers=True,
    title=f"{district} Average Monthly Climate Pattern"
)

fig_month.update_layout(
    height=600
)

st.plotly_chart(
    fig_month,
    use_container_width=True
)

# ----------------------------------
# Data Table
# ----------------------------------

st.subheader("📋 Raw Climate Data")

st.dataframe(
    district_df.sort_values(
        "Date",
        ascending=False
    ),
    use_container_width=True
)