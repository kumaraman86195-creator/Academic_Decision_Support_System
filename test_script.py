from src.data_loader import load_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model

# Load data
df = load_data()

# Train model
model, X_test, y_test = train_model(df)

# Evaluate model
acc, report, cm = evaluate_model(model, X_test, y_test)

print("Accuracy:", acc)
print("Report:\n", report)
print("Confusion Matrix:\n", cm)