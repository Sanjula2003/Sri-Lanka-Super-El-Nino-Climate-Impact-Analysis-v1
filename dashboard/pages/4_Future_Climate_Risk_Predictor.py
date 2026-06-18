import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Future Climate Risk Predictor",
    page_icon="🔮",
    layout="wide"
)

# -------------------------
# LOAD DATA
# -------------------------

df = pd.read_csv(
    "data/sri_lanka_climate_dataset.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

# -------------------------
# LOAD MODEL
# -------------------------

model = joblib.load(
    "../outputs/models/rainfall_predictor.pkl"
)

# -------------------------
# TITLE
# -------------------------

st.title("🔮 Future Climate Risk Predictor")

st.markdown("""
Simulate future Super El Niño conditions and estimate
their potential climate impacts across Sri Lanka.
""")

# -------------------------
# USER INPUTS
# -------------------------

districts = sorted(
    df["District"].unique()
)

col1, col2 = st.columns(2)

with col1:

    district = st.selectbox(
        "District",
        districts
    )

    month = st.slider(
        "Month",
        1,
        12,
        10
    )

with col2:

    future_mei = st.slider(
        "Future MEI Value",
        -3.0,
        3.0,
        2.0,
        0.1
    )

    future_year = st.slider(
        "Year",
        2026,
        2035,
        2030
    )

# -------------------------
# DISTRICT HISTORY
# -------------------------

district_df = df[
    df["District"] == district
]

latest = district_df.iloc[-1]

# -------------------------
# MODEL INPUT
# -------------------------

features = np.array([
    future_mei,
    latest["MEI"],
    latest["MEI"],
    latest["MEI"],
    latest["Rainfall"],
    latest["Temperature"],
    month,
    future_year
]).reshape(1, -1)

# -------------------------
# PREDICT
# -------------------------

predicted_rainfall = model.predict(
    features
)[0]

# -------------------------
# RISK SCORE
# -------------------------

risk_score = (
    abs(future_mei) * 0.4 +
    predicted_rainfall * 0.1
)

# -------------------------
# RISK CATEGORY
# -------------------------

if risk_score >= 2.5:
    risk_level = "HIGH"

elif risk_score >= 1.5:
    risk_level = "MODERATE"

else:
    risk_level = "LOW"

# -------------------------
# RESULTS
# -------------------------

st.header("Prediction Results")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Predicted Rainfall",
    f"{predicted_rainfall:.2f}"
)

c2.metric(
    "Future MEI",
    future_mei
)

c3.metric(
    "Risk Level",
    risk_level
)

# -------------------------
# IMPACT MESSAGE
# -------------------------

st.subheader(
    "Climate Impact Assessment"
)

if risk_level == "HIGH":

    st.error("""
    HIGH CLIMATE RISK

    • Significant climate disruption possible

    • Increased flood/drought risk

    • Agriculture may be affected

    • Water resource management required
    """)

elif risk_level == "MODERATE":

    st.warning("""
    MODERATE CLIMATE RISK

    • Noticeable climate variability

    • Monitor rainfall patterns

    • Localized impacts possible
    """)

else:

    st.success("""
    LOW CLIMATE RISK

    • Climate conditions near normal

    • Limited expected impacts
    """)

# -------------------------
# DISTRICT HISTORY CHART
# -------------------------

st.subheader(
    f"{district} Historical Rainfall"
)

chart_df = district_df.copy()

st.line_chart(
    chart_df.set_index("Date")["Rainfall"]
)

# -------------------------
# SCENARIO ANALYSIS
# -------------------------

st.subheader(
    "Super El Niño Scenarios"
)

scenario_df = pd.DataFrame({
    "MEI":[
        0.5,
        1.0,
        1.5,
        2.0,
        2.5
    ]
})

predictions = []

for mei in scenario_df["MEI"]:

    x = np.array([
        mei,
        latest["MEI"],
        latest["MEI"],
        latest["MEI"],
        latest["Rainfall"],
        latest["Temperature"],
        month,
        future_year
    ]).reshape(1,-1)

    predictions.append(
        model.predict(x)[0]
    )

scenario_df[
    "Predicted Rainfall"
] = predictions

st.dataframe(
    scenario_df,
    use_container_width=True
)

st.line_chart(
    scenario_df.set_index("MEI")
)