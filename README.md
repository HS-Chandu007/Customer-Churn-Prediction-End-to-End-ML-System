# Customer-Churn-Prediction-End-to-End-ML-System
This project is an end-to-end customer churn prediction system built using real-world business data. The goal is to identify customers who are likely to leave so that proactive retention strategies can be applied.

The work goes beyond model training and focuses on the full ML lifecycle — from problem framing and feature engineering to deployment and explainability.

Key highlights:

Framed churn prediction as a recall-focused classification problem to minimize missed churners

Performed detailed EDA on a highly imbalanced (9:1) dataset with skewed features and high-cardinality categories

Implemented custom target encoding with smoothing to handle categorical variables safely

Focused on high-impact feature engineering rather than feature quantity

Used RFE-CV for systematic feature selection

Trained and tuned XGBoost and LightGBM models using Optuna

Achieved 84%+ recall on churn class with 80%+ ROC-AUC

Added model explainability using SHAP and LIME

Validated generalization using learning curve analysis

Deployed the model using FastAPI, containerized with Docker, and exposed via an interactive Gradio UI

Adapted to real-world constraints by deploying on Hugging Face Spaces instead of paid cloud platforms

This project demonstrates practical decision-making, handling of real-world data challenges, and the ability to ship a usable ML system — not just train a model.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/88fd9354-3a81-4fac-ad47-213a36b49367" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/962a15d8-0af0-4ced-b151-2ac2073d1e86" />



