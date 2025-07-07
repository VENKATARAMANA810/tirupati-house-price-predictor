import streamlit as st
import pickle
import numpy as np
import requests

# Load model and columns
model = pickle.load(open('model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

st.title("🏠 Tirupati House Price Predictor")

# Input fields
area = st.number_input("Area (sqft)", 500, 10000, 1000)
bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])
location = st.selectbox("Location", [col.replace("location_", "") for col in columns if "location_" in col])
type_ = st.selectbox("Type", [col.replace("type_", "") for col in columns if "type_" in col])

# Build input vector
input_data = np.zeros(len(columns))

input_data[columns.index('area')] = area
input_data[columns.index('bhk')] = bhk

loc_col = f"location_{location}"
typ_col = f"type_{type_}"

if loc_col in columns:
    input_data[columns.index(loc_col)] = 1
if typ_col in columns:
    input_data[columns.index(typ_col)] = 1

# Prediction
if st.button("Predict Price"):
    prediction = model.predict([input_data])[0]
    st.success(f"Estimated House Price: ₹{round(prediction):,}")
