from src.data_preprocessing import load_data, preprocess_data
from src.model import train_model, evaluate_model, plot_confusion_matrix

# Step 1: Load data
df = load_data()

# Step 2: Preprocess
df = preprocess_data(df)

# Step 3: Split data
X = df.drop("label", axis=1)
y = df["label"]

# Step 4: Train model
model = train_model(X, y)

# Step 5: Evaluate model
predictions = evaluate_model(model, X, y)

print("\n🔍 Predictions:")
print(predictions)
plot_confusion_matrix(y, predictions)

print("\n🚨 Threat Detection Results:")

for i, pred in enumerate(predictions):
    if pred == 1:
        print(f"⚠️ ALERT: Attack detected at index {i}")
    else:
        print(f"✅ Normal traffic at index {i}")