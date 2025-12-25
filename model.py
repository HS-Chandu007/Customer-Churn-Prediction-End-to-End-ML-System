import os
import joblib
import xgboost as xgb
import numpy as np

# Go from app/model.py → project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FEATURES_PATH = os.path.join(BASE_DIR, "artifacts", "selected_features.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "final_xgb.json")

selected_features = list(joblib.load(FEATURES_PATH))

booster = xgb.Booster()
booster.load_model(MODEL_PATH)


def build_feature_vector(input_dict: dict) -> np.ndarray:
    row = [input_dict[f] for f in selected_features]
    return np.array(row, dtype=float).reshape(1, -1)


def predict_churn(input_dict: dict, threshold: float = 0.5):
    X = build_feature_vector(input_dict)

    dmatrix = xgb.DMatrix(
        X,
        feature_names=selected_features
    )

    prob = float(booster.predict(dmatrix)[0])
    pred = int(prob >= threshold)
    return prob, pred
