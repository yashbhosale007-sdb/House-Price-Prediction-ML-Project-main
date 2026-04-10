import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('house_model.pkl', 'rb'))

st.title("🏠 House Price Prediction App")

# Input fields
area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, step=100)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10)
stories = st.number_input("Number of Stories", min_value=1, max_value=5)
parking = st.selectbox("Parking Available?", [0, 1])
furnishing = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])

# Encode furnishing
furnishing_dict = {"Unfurnished": 2, "Semi-Furnished": 1, "Furnished": 0}
furnishing_value = furnishing_dict[furnishing]

# Prediction button
if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms, stories, parking, furnishing_value]])
    prediction = model.predict(features)
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
