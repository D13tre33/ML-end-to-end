from fastapi import FastAPI
import pandas as pd
import numpy as np
from sklearn.externals import joblib

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model
try:
    model = joblib.load('credit_card_fraud_model.pkl')
    print('Model loaded successfully')
except FileNotFoundError:
    print('Model file not found')

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "API is running"}

# Predict endpoint
@app.post("/predict/")
async def predict(data: dict):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Return prediction result
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
