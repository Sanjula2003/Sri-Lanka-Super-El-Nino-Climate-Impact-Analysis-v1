import streamlit as st
import pandas as pd

df = pd.read_csv(
    "data/sri_lanka_climate_dataset.csv"
)

st.title("📊 Project Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Records",
    len(df)
)

col2.metric(
    "Districts",
    df["District"].nunique()
)

col3.metric(
    "Years",
    26
)

col4.metric(
    "Climate Variables",
    3
)

st.dataframe(
    df.head()
)