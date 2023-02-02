from fastapi import FastAPI
import pickle
import pandas as pd
from mangum import Mangum
from schemas.schemas import Predictor


# Carregando Pickle file
with open("ML_models/randomforestclassifier.pkl","rb") as file:
  pickle_model = pickle.load(file)

app = FastAPI()

handler = Mangum(app)

# @app.get("/")
# def root():
#     return {"msg:":"working!"}

@app.post("/predictions")
async def predict_loan_status(prediction: Predictor):

    predictions = {"TotalIncome": int(prediction.TotalIncome),
                     "LoanAmount": int(prediction.LoanAmount),
                     "Credit_History": int(prediction.Credit_History),
                     "Property_Area": int(prediction.Property_Area)}

    df_predictions = pd.DataFrame([predictions])
    result = pickle_model.predict(df_predictions)[0]

    if result == 0:
        message = "Não aprovado!"
    else:
        message = 'Aprovado!'

    return {"O Estado do Empéstimo é " : message}