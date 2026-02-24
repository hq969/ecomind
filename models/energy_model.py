import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

def train_energy_model():
    data = {
        "cpu_usage": [50, 60, 70, 80, 90],
        "temperature": [25, 27, 29, 30, 32],
        "energy_consumption": [200, 230, 260, 290, 330]
    }

    df = pd.DataFrame(data)

    X = df[["cpu_usage", "temperature"]]
    y = df["energy_consumption"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "models/energy_model.pkl")
    print("Energy model trained successfully!")

if __name__ == "__main__":
    train_energy_model()
