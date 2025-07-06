# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('house_price_model.pkl')

st.title("🏡 House Price Prediction App")

# Sidebar inputs
st.sidebar.header("Input House Features")

def user_input():
    MSZoning = st.sidebar.selectbox("MS Zoning", ['RL', 'RM', 'FV', 'RH', 'C (all)'])
    LotArea = st.sidebar.number_input("Lot Area (sq ft)", min_value=1000, max_value=100000, value=7500)
    Neighborhood = st.sidebar.selectbox("Neighborhood", ['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel'])
    OverallQual = st.sidebar.slider("Overall Quality (1-10)", 1, 10, 5)
    YearBuilt = st.sidebar.number_input("Year Built", min_value=1800, max_value=2025, value=2005)
    YearRemodAdd = st.sidebar.number_input("Year Remodeled", min_value=1800, max_value=2025, value=2005)
    ExterQual = st.sidebar.selectbox("Exterior Quality", ['Ex', 'Gd', 'TA', 'Fa'])
    Foundation = st.sidebar.selectbox("Foundation", ['PConc', 'CBlock', 'BrkTil', 'Wood', 'Slab'])
    BsmtQual = st.sidebar.selectbox("Basement Quality", ['Ex', 'Gd', 'TA', 'Fa', 'NA'])
    TotalBsmtSF = st.sidebar.number_input("Total Basement SF", 0, 3000, 800)
    HeatingQC = st.sidebar.selectbox("Heating Quality", ['Ex', 'Gd', 'TA', 'Fa', 'Po'])
    GrLivArea = st.sidebar.number_input("Above Ground Living Area", 500, 4000, 1500)
    FullBath = st.sidebar.slider("Full Bathrooms", 0, 3, 1)
    TotRmsAbvGrd = st.sidebar.slider("Total Rooms Above Ground", 2, 14, 6)
    KitchenQual = st.sidebar.selectbox("Kitchen Quality", ['Ex', 'Gd', 'TA', 'Fa'])
    Fireplaces = st.sidebar.slider("Number of Fireplaces", 0, 3, 1)
    GarageFinish = st.sidebar.selectbox("Garage Finish", ['Fin', 'RFn', 'Unf', 'NA'])
    GarageCars = st.sidebar.slider("Garage Capacity (cars)", 0, 4, 2)
    GarageArea = st.sidebar.number_input("Garage Area", 0, 1500, 500)
    SaleCondition = st.sidebar.selectbox("Sale Condition", ['Normal', 'Abnorml', 'Partial', 'AdjLand'])

    # Create a dataframe for model input
    data = {
        'MSZoning': [MSZoning],
        'LotArea': [LotArea],
        'Neighborhood': [Neighborhood],
        'OverallQual': [OverallQual],
        'YearBuilt': [YearBuilt],
        'YearRemodAdd': [YearRemodAdd],
        'ExterQual': [ExterQual],
        'Foundation': [Foundation],
        'BsmtQual': [BsmtQual],
        'TotalBsmtSF': [TotalBsmtSF],
        'HeatingQC': [HeatingQC],
        'GrLivArea': [GrLivArea],
        'FullBath': [FullBath],
        'TotRmsAbvGrd': [TotRmsAbvGrd],
        'KitchenQual': [KitchenQual],
        'Fireplaces': [Fireplaces],
        'GarageFinish': [GarageFinish],
        'GarageCars': [GarageCars],
        'GarageArea': [GarageArea],
        'SaleCondition': [SaleCondition]
    }

    return pd.DataFrame(data)

# Collect user input
input_df = user_input()

# Prediction
if st.button("Predict House Price"):
    prediction = model.predict(input_df)
    st.success(f"🏠 Estimated Sale Price: ${int(prediction[0]):,}")
