from pydantic import BaseModel, Field

class ChurnInput(BaseModel):
    """
    Input schema for Customer Churn Prediction.
    All values must be NUMERIC and MUST match the model training features exactly.
    """

    age: int = Field(
        ge=0, le=100,
        description="Age of the customer in years."
    )

    tenure_months: int = Field(
        ge=0,
        description="Number of continuous months the customer has been using the service."
    )

    monthly_logins: int = Field(
        ge=0,
        description="Total number of login events recorded in the last month."
    )

    weekly_active_days: int = Field(
        ge=0, le=7,
        description="Number of distinct days per week the customer actively uses the platform."
    )

    avg_session_time: float = Field(
        ge=0,
        description="Average session duration per login (in minutes)."
    )

    last_login_days_ago: int = Field(
        ge=0,
        description="Number of days since the customer last logged into the platform."
    )

    monthly_fee: int = Field(
        ge=0,
        description="Monthly subscription or service fee charged to the customer."
    )

    total_revenue: int = Field(
        ge=0,
        description="Total lifetime revenue generated from the customer."
    )

    payment_failures: int = Field(
        ge=0,
        description="Number of failed payment attempts experienced by the customer."
    )

    avg_resolution_time: float = Field(
        ge=0,
        description="Average time (in hours) taken to resolve customer issues."
    )

    csat_score: int = Field(
        ge=0, le=5,
        description="Customer Satisfaction (CSAT) score on a scale of 0 to 5."
    )

    escalations: int = Field(
        ge=0,
        description="Number of times customer issues were escalated to higher support levels."
    )

    email_open_rate: int = Field(
        ge=0, le=100,
        description="Percentage of marketing emails opened by the customer."
    )

    marketing_click_rate: int = Field(
        ge=0, le=100,
        description="Percentage of marketing links clicked by the customer."
    )

    nps_score: int = Field(
        ge=-100, le=100,
        description="Net Promoter Score (NPS), ranging from -100 to 100."
    )

    # -------- Encoded categorical features (numeric) --------

    gender_enc: float = Field(
        description="Target-encoded numeric value representing the customer's gender."
    )

    country_enc: float = Field(
        description="Target-encoded numeric value representing the customer's country."
    )

    city_enc: float = Field(
        description="Target-encoded numeric value representing the customer's city."
    )

    customer_segment_enc: float = Field(
        description="Target-encoded numeric value for the customer segment (e.g., SME, Individual, Enterprise)."
    )

    signup_channel_enc: float = Field(
        description="Target-encoded numeric value representing the signup channel (e.g., Web, Mobile, Referral)."
    )

    contract_type_enc: float = Field(
        description="Target-encoded numeric value representing the type of contract."
    )

    payment_method_enc: float = Field(
        description="Target-encoded numeric value representing the primary payment method."
    )

    discount_applied_enc: float = Field(
        description="Target-encoded numeric value indicating whether a discount was applied."
    )

    complaint_type_enc: float = Field(
        description="Target-encoded numeric value representing the primary complaint category."
    )

    survey_response_enc: float = Field(
        description="Target-encoded numeric value representing customer survey sentiment."
    )

    # -------- Engineered numeric features --------

    engagement_score: int = Field(
        description="Composite engagement score derived from user activity metrics."
    )

    login_intensity: int = Field(
        description="Derived metric representing how frequently the customer logs in."
    )

    feature_adapotion_rate: int = Field(
        description="Rate at which the customer adopts new platform features."
    )

    usage_momentum: int = Field(
        description="Trend-based metric capturing recent changes in customer usage behavior."
    )

    revenue_per_feature: int = Field(
        description="Average revenue generated per feature used by the customer."
    )

    effective_cost_per_login: int = Field(
        description="Effective cost incurred by the platform per customer login."
    )

    value_gap: int = Field(
        description="Difference between customer lifetime value and cost incurred by the platform."
    )
