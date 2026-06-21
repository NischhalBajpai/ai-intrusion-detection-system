import joblib
import pandas as pd
model = joblib.load("models/ids_model.pkl")
print("Model loaded successfully!")