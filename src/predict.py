import joblib
import pandas as pd
from preprocess import preprocess_data


MODEL_PATH = "models/pass_fail_model.pkl"


def load_model():
    """Load trained model"""
    return joblib.load(MODEL_PATH)


def predict_student(input_data):
    """
    Predict Pass/Fail for a student
    input_data = dictionary of student features
    """

    model = load_model()

    # Convert input dict to DataFrame
    df = pd.DataFrame([input_data])

    # Apply preprocessing
    df = preprocess_data(df)

    # Predict class & probability
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return prediction, probability