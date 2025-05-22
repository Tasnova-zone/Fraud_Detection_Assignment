import streamlit as st
import joblib
import numpy as np

# Page settings
st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")
st.title("💳 Credit Card Fraud Detection App")
st.write("Fill in the transaction details to check if it's fraudulent.")

# Load the model
try:
    model = joblib.load("fraud_model.pkl")
except FileNotFoundError:
    st.error("❌ Model file 'fraud_model.pkl' not found. Please place it in the same folder as this script.")
    st.stop()

# Input fields
with st.form("prediction_form"):
    st.subheader("📝 Transaction Features")

    V_features = [st.number_input(f"V{i}", value=0.0, format="%.4f") for i in range(1, 29)]
    time = st.number_input("Transaction Time", value=0.0, format="%.2f")
    amount = st.number_input("Transaction Amount", value=0.0, format="%.2f")

    submit = st.form_submit_button("Predict")

# Predict on submission
if submit:
    input_data = np.array(V_features + [time, amount]).reshape(1, -1)

    try:
        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]  # Probability of fraud
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
        st.stop()

    st.subheader("🔍 Prediction Result")
    if prediction == 1:
        st.error(f"🚨 Fraud Detected! (Confidence: {prob*100:.2f}%)")
    else:
        st.success(f"✅ Legitimate Transaction (Confidence: {(1 - prob)*100:.2f}%)")
