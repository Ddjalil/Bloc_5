import uvicorn
import pandas as pd 
import json
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile
from joblib import dump, load



description = """
### Bienvenue dans notre API Getaround.
"""


# initialise API object
app = FastAPI(
    title="GetAround API",
    description=description,
    version="1.0",
    openapi_tags= [
    {
        "name": "Home",
        "description": "Voici la page d'Acceuil de L'API GetAround."
    },
    {
        "name": "Predicts",
        "description": "GetAround API with POST or GET method."
    }
]
)


tags_metadata = [
    {
        "name": "Introduction Endpoints",
        "description": "Simple endpoints to try out!",
    },
    {
        "name": "Prediction",
        "description": "Prediction of the rental price based on a machine learning model"
    }
]


	


class PredictionFeatures(BaseModel):
    model_key: str = "Citroën"
    mileage: int = 97097
    engine_power: int = 160
    fuel: str = "diesel"
    paint_color: str = "silver"
    car_type: str = "convertible"
    private_parking_available: bool = True
    has_gps: bool = True
    has_air_conditioning: bool = False
    automatic_car: bool = False
    has_getaround_connect: bool = False
    has_speed_regulator: bool = True
    winter_tires: bool = True
    
    
@app.get("/", tags = ["Introduction Endpoint"])
async def index():
    message = "Hello! Voici le point de depart de l'API de Getaround`"
    return message


@app.get("/preview", tags=["Preview"])
async def preview(rows: int):
    """ Un petit apercu du Dataset """
    data = pd.read_csv("get_around_pricing_project.csv")
    preview = data.head(rows)
    return preview.to_dict()


@app.post("/predict", tags = ["Price prediction"])
async def predict(predictionFeatures: PredictionFeatures):
    # Read data 
    data = pd.DataFrame(dict(predictionFeatures), index=[0])
    # Load model
    loaded_model = load("modele2.joblib")
    # Prediction
    prediction = loaded_model.predict(data)
    # Format response
    response ={"predictions": prediction.tolist()[0]}
    return response

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000, debug=True, reload=True)

