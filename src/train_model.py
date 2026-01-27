import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import os
from src.preprocess import preprocess_data


def train_model(df):
    """
    Train XGBoost model for Pass/Fail prediction
    """

    # Apply preprocessing
    df = preprocess_data(df)

    # Split features and target
    features = [
    "study_hours_per_day",
    "attendance_percentage",
    "absences",
    "sleep_hours",
    "stress_level",
    "motivation_level",
    "family_support",
    "school_support",
    "activity_level",
    "avg_grade"]

    X = df[features]
    y = df["pass_fail"]

    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initialize XGBoost model
    model = XGBClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        subsample=0.9,
        colsample_bytree=0.9,
        random_state=42
    )

    # Train model
    model.fit(X_train, y_train)
    os.makedirs("models", exist_ok=True)
    # Save model
    joblib.dump(model, "models/pass_fail_model.pkl")

    return model, X_test, y_test