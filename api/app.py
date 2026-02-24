from fastapi import FastAPI
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = FastAPI()

climate_model = load_model("models/climate_model.h5")
climate_scaler = joblib.load("models/climate_scaler.pkl")
energy_model = joblib.load("models/energy_model.pkl")

@app.post("/predict-climate/")
def predict_climate(data: dict):
    values = np.array(list(data.values())).reshape(1, -1)
    scaled = climate_scaler.transform(values)
    scaled = scaled.reshape(1,1,-1)

    prediction = climate_model.predict(scaled)
    return {"predicted_temperature": float(prediction[0][0])}

@app.post("/predict-energy/")
def predict_energy(data: dict):
    values = [[data["cpu_usage"], data["temperature"]]]
    prediction = energy_model.predict(values)
    return {"predicted_energy_consumption": float(prediction[0])}
