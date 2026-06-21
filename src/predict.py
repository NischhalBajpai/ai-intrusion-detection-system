import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "ids_model.pkl"
DATA_PATH = BASE_DIR / "data" / "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

model = joblib.load(MODEL_PATH)
print("Model loaded successfully!")

df = pd.read_csv(DATA_PATH)

# Remove leading/trailing spaces from all column names
df.columns = df.columns.str.strip()

print("Last column:", df.columns[-1])

sample = df.drop("Label", axis=1).iloc[[0]]

prediction = model.predict(sample)

print("Prediction:", prediction[0])