import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Climate Risk Map",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Sri Lanka Climate Risk Map")

df = pd.read_csv(
    "data/sri_lanka_climate_dataset.csv"
)

district_coords = {
    "Colombo":[6.9271,79.8612],
    "Kandy":[7.2906,80.6337],
    "Jaffna":[9.6615,80.0255],
    "Anuradhapura":[8.3114,80.4037],
    "Batticaloa":[7.7102,81.6924]
}

risk_df = (
    df.groupby("District")
    .agg({
        "Rainfall":"mean",
        "Temperature":"mean",
        "MEI":"mean"
    })
)

risk_df["Risk_Score"] = (
    risk_df["Rainfall"]*0.3 +
    risk_df["Temperature"]*0.4 +
    abs(risk_df["MEI"])*0.3
)

m = folium.Map(
    location=[7.8,80.7],
    zoom_start=7
)

for district,row in risk_df.iterrows():

    lat,lon = district_coords[district]

    score = row["Risk_Score"]

    if score > 12:
        color="red"

    elif score > 10:
        color="orange"

    else:
        color="green"

    folium.CircleMarker(
        location=[lat,lon],
        radius=12,
        popup=f"""
        {district}

        Risk Score: {score:.2f}
        """,
        color=color,
        fill=True
    ).add_to(m)

st_folium(
    m,
    width=1200,
    height=700
)