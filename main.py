#Python
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

#py -m venv venv - entorno virtual
#venv\scripts\activate.bat

#uvicorn main:app --reload

app=FastAPI()

@app.get(
    path="/", 
    status_code=status.HTTP_200_OK,
    tags=["Home"]
    ) #path operation decorator

def home():    #path operation function
    return {"Hello":"World"}