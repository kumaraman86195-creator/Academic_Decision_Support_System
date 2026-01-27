import pandas as pd
import os


def load_data(path=None):
    """
    Load dataset safely using absolute project path
    """

    if path is None:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(base_dir, "data", "raw", "student_performance_balanced.csv")

    return pd.read_csv(path)