import gradio as gr
import requests

API_URL = "http://localhost:8000/predict"


def predict_churn_ui(
    age,
    tenure_months,
    monthly_logins,
    weekly_active_days,
    avg_session_time,
    last_login_days_ago,
    monthly_fee,
    total_revenue,
    payment_failures,
    avg_resolution_time,
    csat_score,
    escalations,
    email_open_rate,
    marketing_click_rate,
    nps_score,
    gender_enc,
    country_enc,
    city_enc,
    customer_segment_enc,
    signup_channel_enc,
    contract_type_enc,
    payment_method_enc,
    discount_applied_enc,
    complaint_type_enc,
    survey_response_enc,
    engagement_score,
    login_intensity,
    feature_adapotion_rate,
    usage_momentum,
    revenue_per_feature,
    effective_cost_per_login,
    value_gap
):
    payload = {
        "age": age,
        "tenure_months": tenure_months,
        "monthly_logins": monthly_logins,
        "weekly_active_days": weekly_active_days,
        "avg_session_time": avg_session_time,
        "last_login_days_ago": last_login_days_ago,
        "monthly_fee": monthly_fee,
        "total_revenue": total_revenue,
        "payment_failures": payment_failures,
        "avg_resolution_time": avg_resolution_time,
        "csat_score": csat_score,
        "escalations": escalations,
        "email_open_rate": email_open_rate,
        "marketing_click_rate": marketing_click_rate,
        "nps_score": nps_score,
        "gender_enc": gender_enc,
        "country_enc": country_enc,
        "city_enc": city_enc,
        "customer_segment_enc": customer_segment_enc,
        "signup_channel_enc": signup_channel_enc,
        "contract_type_enc": contract_type_enc,
        "payment_method_enc": payment_method_enc,
        "discount_applied_enc": discount_applied_enc,
        "complaint_type_enc": complaint_type_enc,
        "survey_response_enc": survey_response_enc,
        "engagement_score": engagement_score,
        "login_intensity": login_intensity,
        "feature_adapotion_rate": feature_adapotion_rate,
        "usage_momentum": usage_momentum,
        "revenue_per_feature": revenue_per_feature,
        "effective_cost_per_login": effective_cost_per_login,
        "value_gap": value_gap
    }

    resp = requests.post(API_URL, json=payload)
    response = resp.json()

    print("RAW API RESPONSE:", response)

    if "churn_probability" not in response or "churn_prediction" not in response:
        return "Error", 0.0, f"❌ API Error:\n```json\n{response}\n```"

   
    pred = int(response["churn_prediction"])
    prob = float(response["churn_probability"])


    if pred == 1:
        label = "Churn"
        explanation = (
            f"⚠️ The model predicts the customer is **likely to churn** "
            f"with a confidence level of **{prob * 100:.2f}%**."
            )
    else:
        label = "No Churn"
        explanation = (
            f"✅ The model predicts the customer is **unlikely to churn** "
            f"with a confidence level of **{(1 - prob) * 100:.2f}%**."
            )

    return label, round(prob, 4), explanation


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # 📉 Customer Churn Prediction  
        **FastAPI · XGBoost · Docker · Gradio**

        ⚠️ This model expects **target-encoded numeric values** for categorical features.
        """
    )

    age = gr.Number(0, 100, label="Age")
    tenure_months = gr.Number(0, label="Tenure (Months)")
    monthly_logins = gr.Number(0, 31, label="Monthly Logins")
    weekly_active_days = gr.Number(0, 7, label="Weekly Active Days")
    avg_session_time = gr.Number(0, label="Avg Session Time")
    last_login_days_ago = gr.Number(0, label="Days Since Last Login")

    monthly_fee = gr.Number(0, label="Monthly Fee")
    total_revenue = gr.Number(0, label="Total Revenue")
    payment_failures = gr.Number(0, label="Payment Failures")
    avg_resolution_time = gr.Number(0, label="Avg Resolution Time")
    csat_score = gr.Number(0, 5, label="CSAT Score")
    escalations = gr.Number(0, label="Escalations")

    email_open_rate = gr.Number(0, 100, label="Email Open Rate")
    marketing_click_rate = gr.Number(0, 100, label="Marketing Click Rate")
    nps_score = gr.Number(-100, 100, label="NPS Score")

    gender_enc = gr.Number(0, 1, label="Gender (target encoded)")
    country_enc = gr.Number(0, 1, label="Country (target encoded)")
    city_enc = gr.Number(0, 1, label="City (target encoded)")
    customer_segment_enc = gr.Number(0, 1, label="Customer Segment (target encoded)")
    signup_channel_enc = gr.Number(0, 1, label="Signup Channel (target encoded)")
    contract_type_enc = gr.Number(0, 1, label="Contract Type (target encoded)")
    payment_method_enc = gr.Number(0, 1, label="Payment Method (target encoded)")
    discount_applied_enc = gr.Number(0, 1, label="Discount Applied (target encoded)")
    complaint_type_enc = gr.Number(0, 1, label="Complaint Type (target encoded)")
    survey_response_enc = gr.Number(0, 1, label="Survey Response (target encoded)")

    engagement_score = gr.Number(0, label="Engagement Score")
    login_intensity = gr.Number(0, label="Login Intensity")
    feature_adapotion_rate = gr.Number(0, label="Feature Adoption Rate")
    usage_momentum = gr.Number(0, label="Usage Momentum")
    revenue_per_feature = gr.Number(0, label="Revenue per Feature")
    effective_cost_per_login = gr.Number(0, label="Effective Cost per Login")
    value_gap = gr.Number(0, label="Value Gap")

    predict_btn = gr.Button("🔮 Predict Churn", variant="primary")

    churn_label = gr.Label(label="Prediction")
    churn_prob = gr.Number(label="Churn Probability")
    explanation = gr.Markdown()

    predict_btn.click(
        predict_churn_ui,
        inputs=[
            age, tenure_months, monthly_logins, weekly_active_days,
            avg_session_time, last_login_days_ago, monthly_fee, total_revenue,
            payment_failures, avg_resolution_time, csat_score, escalations,
            email_open_rate, marketing_click_rate, nps_score,
            gender_enc, country_enc, city_enc, customer_segment_enc,
            signup_channel_enc, contract_type_enc, payment_method_enc,
            discount_applied_enc, complaint_type_enc, survey_response_enc,
            engagement_score, login_intensity, feature_adapotion_rate,
            usage_momentum, revenue_per_feature, effective_cost_per_login,
            value_gap
        ],
        outputs=[churn_label, churn_prob, explanation]
    )

demo.launch(share=True)

    