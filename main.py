#Python
from copyreg import pickle
from typing import Optional
from enum import Enum
from pydantic import EmailStr

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI, Query, UploadFile
from fastapi import Body, Query, Path, Form, Header, Cookie,UploadFile,File
from fastapi import status
from fastapi import HTTPException

#ML model
import pickle
import numpy as np

#py -m venv venv - entorno virtual
#venv\scripts\activate.bat

#uvicorn main:app --reload

app=FastAPI()
pickle_in=open("kaggle_titanic_model.pkl","rb")
pred=pickle.load(pickle_in)

class Passenger(BaseModel):
    Pclass: Optional[int]
    Sex: Optional[int]
    Age: Optional[float]
    SibSp: Optional[int]
    eParch: Optional[int]
  


@app.get(
    path="/", 
    status_code=status.HTTP_200_OK,
    tags=["Home"]
    ) #path operation decorator

def home():    #path operation function
    return {"Hello":"World"}

@app.post(
    path="/predict",
)

def predict(data:Passenger):
    data=data.dict()
    Pclass=data["Pclass"] 
    Age= data["Age"] 
    Sex= data["Sex"] 
    SibSp= data["SibSp"] 
    eParch= data["eParch"]
    #x_test=[3,0,0.28947368,1,1]
    x_test=[Pclass,Age,Sex,SibSp,eParch]
    x_test=np.reshape(x_test,(1,5))
    prediction = pred.predict(x_test)
    print("Prediccion: ",prediction) 
    if(int(prediction[0])>0.5):
        prediction="Survived"
        print("Survived")
    else:
        prediction="Do not Survived"
        print("Do not Survived")

    return {
        'prediction': prediction
    }

    if __name__ == '__main__':
        uvicorn.run(app, host='127.0.0.1', port=8000)



