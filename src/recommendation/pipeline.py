from src.recommendation.weak_subject_detection import apply_weak_subject_detection
from src.recommendation.risk_detection import apply_risk_detection
from src.recommendation.personalised_feedback import apply_feedback
from src.recommendation.course_recommendation import apply_course_recommendation

def run_recommendation_pipeline(df):
    df = apply_weak_subject_detection(df)
    df = apply_risk_detection(df)
    df = apply_feedback(df)
    df = apply_course_recommendation(df)

    return df