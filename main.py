from fastapi import FastAPI, HTTPException
from app.schemas import ChurnInput
from app.model import predict_churn

app = FastAPI(title="Customer Churn Prediction API.")

@app.get('/home')
def home():
    return {"message": "Customer Churn Prediction API."}

@app.get('/health')
def health():
    return {"Status" : "Ok"}

@app.post("/predict")
def predict(data: ChurnInput):
    try:
        prob, pred = predict_churn(data.dict())

        response = {
            "churn_prediction": int(pred),
            "churn_probability": float(prob)
        }

        print("API RESPONSE:", response)  

        return response

    except Exception as e:
        print("API ERROR:", str(e)) 
        raise HTTPException(status_code=500, detail=str(e))

