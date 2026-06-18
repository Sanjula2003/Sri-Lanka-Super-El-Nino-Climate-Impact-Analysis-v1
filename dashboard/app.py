import streamlit as st

st.set_page_config(
    page_title="Super El Niño Sri Lanka",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Super El Niño Climate Impact Analysis")

st.markdown("""
### Multi-District Climate Analysis for Sri Lanka (2000–2025)

Using:

- NOAA MEI v2
- NASA POWER Climate Data

Developed by:
**Sanjula Bandara**
""")

st.info(
    "Use the navigation menu on the left to explore climate impacts across Sri Lanka."
)