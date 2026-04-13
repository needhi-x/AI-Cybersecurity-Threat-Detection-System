import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
def load_data():
    df = pd.read_csv("data/dataset.csv")
    print("✅ Dataset Loaded Successfully")
    print("Shape:", df.shape)
    return df

# Preprocess data
def preprocess_data(df):
    encoder = LabelEncoder()
    
    # Convert protocol_type (text → number)
    df["protocol_type"] = encoder.fit_transform(df["protocol_type"])
    
    print("✅ Data Preprocessed Successfully")
    return df