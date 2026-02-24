import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib

def train_climate_model():
    df = pd.read_csv("data/sample_climate.csv")

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)

    X, y = [], []
    for i in range(len(scaled)-1):
        X.append(scaled[i])
        y.append(scaled[i+1][0])  # Predict next temperature

    X = np.array(X).reshape(len(X), 1, df.shape[1])
    y = np.array(y)

    model = Sequential([
        LSTM(50, input_shape=(1, df.shape[1])),
        Dense(1)
    ])

    model.compile(optimizer="adam", loss="mse")
    model.fit(X, y, epochs=50, verbose=0)

    model.save("models/climate_model.h5")
    joblib.dump(scaler, "models/climate_scaler.pkl")

    print("Climate model trained successfully!")

if __name__ == "__main__":
    train_climate_model()
