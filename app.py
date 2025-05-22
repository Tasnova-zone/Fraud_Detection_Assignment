import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('fraud_model.pkl')

st.title("💳 Credit Card Fraud Detection")

# Input form for features
st.header("Enter Transaction Details")
time = st.number_input("Time", min_value=0.0)
amount = st.number_input("Amount", min_value=0.0)

# Input V1 to V28 features
v_features = []
for i in range(1, 29):
    val = st.number_input(f"V{i}", value=0.0)
    v_features.append(val)

if st.button("Predict"):
    # Prepare input for prediction
    input_data = np.array([[time] + v_features + [amount]])
    
    # Get prediction and probability
    prob = model.predict_proba(input_data)[0][1]
    prediction = model.predict(input_data)[0]

    # Show result
    st.subheader("Result")
    st.write(f"Fraud Probability: {prob:.4f}")
    st.success("✅ Not Fraud" if prediction == 0 else "⚠️ Fraud Detected!")
