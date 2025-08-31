
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import logging
app = FastAPI()
model = joblib.load("/content/drive/MyDrive/model_random_forest.pkl")
log_file = "api_activity.log"
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")
class PredictRequest(BaseModel):
    year: int
    month: int
