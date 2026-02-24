import streamlit as st
import requests

st.title("🌍 EcoMind Dashboard")

st.header("Climate Prediction")
temp = st.number_input("Temperature")
humidity = st.number_input("Humidity")
co2 = st.number_input("CO2 Level")
sea = st.number_input("Sea Level")

if st.button("Predict Climate"):
    response = requests.post(
        "http://127.0.0.1:8000/predict-climate/",
        json={
            "temperature": temp,
            "humidity": humidity,
            "co2": co2,
            "sea_level": sea
        }
    )
    st.success(response.json())

st.header("Energy Optimization")
cpu = st.number_input("CPU Usage")
t = st.number_input("Data Center Temp")

if st.button("Predict Energy"):
    response = requests.post(
        "http://127.0.0.1:8000/predict-energy/",
        json={
            "cpu_usage": cpu,
            "temperature": t
        }
    )
    st.success(response.json())
