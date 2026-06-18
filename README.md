# 🌍 Super El Niño Climate Impact Analysis for Sri Lanka

## Overview

Super El Niño events are among the most influential climate phenomena affecting global weather systems. Sri Lanka frequently experiences changes in rainfall patterns, temperature variability, drought conditions, and flood risks during strong ENSO phases.

This project investigates the relationship between the **Multivariate ENSO Index (MEI v2)** and Sri Lanka's climate using historical rainfall and temperature data from **2000–2025**.

The project combines climate data analytics, statistical analysis, machine learning, and geospatial visualization to evaluate climate impacts across multiple Sri Lankan districts.

---

## Objectives

* Analyze historical ENSO patterns using NOAA MEI v2 data.
* Investigate rainfall anomalies during El Niño and La Niña events.
* Examine temperature variations associated with ENSO phases.
* Compare climate impacts across multiple Sri Lankan districts.
* Build a machine learning model to predict future rainfall.
* Develop a climate risk assessment framework.
* Identify extreme climate events such as floods and droughts.
* Create an interactive dashboard for climate exploration.

---

## Study Area

The analysis covers five major districts in Sri Lanka:

* Colombo
* Kandy
* Jaffna
* Anuradhapura
* Batticaloa

---

## Data Sources

### NOAA MEI v2 Dataset

Source:
https://psl.noaa.gov/enso/mei/

Used for:

* ENSO monitoring
* El Niño classification
* La Niña classification
* Super El Niño detection

---

### NASA POWER Climate Dataset

Source:
https://power.larc.nasa.gov/

Variables:

* Monthly Rainfall (PRECTOTCORR)
* Monthly Temperature (T2M)

Period:

* January 2000 – December 2025

---

## Project Structure

```text
project/
│
├── data/
│   ├── raw/
│   │   └── meiv2.data
│   │
│   └── processed/
│       ├── mei.csv
│       ├── colombo_rainfall.csv
│       ├── colombo_temperature.csv
│       └── sri_lanka_climate_dataset.csv
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_enso_rainfall_analysis.ipynb
│   ├── 03_temperature_collection.ipynb
│   ├── 04_climate_dataset.ipynb
│   ├── 05_feature_engineering.ipynb
│   ├── 06_eda.ipynb
│   ├── 06_multi_district_data_collection.ipynb
│   └── 07_ml_model.ipynb
│
├── outputs/
│   ├── figures/
│   └── models/
│       └── rainfall_predictor.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Methodology

### Phase 1 – Data Collection

Climate data were collected using NASA POWER APIs for each district.

Variables:

* Rainfall
* Temperature

ENSO data were obtained from NOAA MEI v2.

---

### Phase 2 – Data Preprocessing

Steps:

* Data cleaning
* Date standardization
* Dataset merging
* Missing value handling
* Feature engineering

---

### Phase 3 – Climate Analysis

Performed analyses:

* Rainfall anomaly analysis
* Temperature anomaly analysis
* ENSO categorization
* Lag analysis
* Correlation analysis

ENSO Categories:

* La Niña
* Neutral
* El Niño
* Super El Niño

---

### Phase 4 – Multi-District Impact Assessment

Districts were compared using:

* Average rainfall anomaly
* Average temperature anomaly
* Climate sensitivity indicators

A custom metric was developed:

### SECII

**Super El Niño Climate Impact Index**

Used to rank districts according to climate vulnerability during Super El Niño periods.

---

### Phase 5 – Machine Learning

Target Variable:

* Monthly Rainfall

Features:

* MEI
* MEI Lag 1
* MEI Lag 3
* MEI Lag 6
* Rainfall Lag 1
* Temperature Lag 1
* Month
* Year

Models Evaluated:

* Random Forest Regressor
* XGBoost Regressor

---

## Model Performance

### Random Forest

* R² Score: 0.757
* MAE: 1.52

### XGBoost

* R² Score: 0.754
* MAE: 1.48

Best Model:

✅ Random Forest Regressor

---

## Dashboard Features

### 📊 Overview

* Project summary
* Dataset statistics
* Climate indicators

### 📍 District Explorer

* District selection
* Rainfall trends
* Temperature trends
* ENSO exploration

### 🌋 Super El Niño Analysis

* Rainfall anomaly ranking
* Temperature anomaly ranking
* District comparisons

### 🔮 Future Climate Risk Predictor

Predict future rainfall under hypothetical ENSO conditions.

Inputs:

* District
* Future MEI
* Month
* Year

Outputs:

* Predicted Rainfall
* Climate Risk Level

### 🗺 Climate Risk Map

Interactive Sri Lanka climate risk visualization using Folium.

### ⚠ Extreme Event Detection

Automatically identifies:

* Flood-risk periods
* Drought-risk periods

---

## Key Findings

### Rainfall

* Super El Niño periods generally increase rainfall anomalies across all selected districts.
* Anuradhapura exhibited the highest rainfall anomaly response.

### Temperature

* Northern and Eastern districts experienced higher temperatures during Super El Niño periods.

### ENSO Relationship

* Direct monthly correlation between rainfall and MEI was weak.
* Lagged climate effects showed stronger influence.

### Climate Risk

* Jaffna and Batticaloa demonstrated higher climate sensitivity according to SECII.

---

## Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* XGBoost

### Visualization

* Plotly
* Matplotlib
* Seaborn
* Folium

### Dashboard

* Streamlit

### Data Sources

* NOAA MEI v2
* NASA POWER

---

## Installation

```bash
git clone https://github.com/Sanjula2003/Sri-Lanka-Super-El-Nino-Climate-Impact-Analysis-v1.git

cd super-el-nino-climate-analysis

pip install -r requirements.txt

streamlit run app.py
```

---

## Future Improvements

* Add all 25 districts of Sri Lanka
* Integrate real-time climate APIs
* Forecast temperature alongside rainfall
* Incorporate SPI drought indices
* Develop deep learning forecasting models
* Deploy cloud-based climate monitoring system

---

## Author

**Sanjula Bandara**

BSc (Hons) Data Science
NSBM Green University

GitHub:
https://github.com/Sanjula2003

LinkedIn:
https://www.linkedin.com/in/danushasanjula/

---

## License

This project is developed for educational, research, and climate analytics purposes.
