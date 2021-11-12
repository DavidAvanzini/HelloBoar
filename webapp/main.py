import json
from datetime import datetime
from detecto.core import Model
from detecto import utils
import io
import numpy as np
from PIL import Image
import predictions
import persist


from typing import Optional
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Request
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#init ML model 
predictions.init()
description = "A Machine Learning Powered rest service to detect Boars"

tags_metadata = [
    {
        "name": "mainpage",
        "description": "main page",
    },
    {
        "name": "detections",
        "description": "Operations for boar detection from images",
    }   
]

app = FastAPI(title="HelloBoar",
    description=description,
    version="0.0.1",
    terms_of_service="",
    contact={
        "name": "David Avanzini",
        "url": "https://www.linkedin.com/in/davidavanzini//",
        "email": "",
    },openapi_tags=tags_metadata)
    


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


#@app.get("/")
#def read_root():
#    return {"Hello": "World"}

@app.get("/")
async def helloboarmainpage(request: Request):
    return templates.TemplateResponse("boarlogo.html", {"request": request})


@app.get("/map")
async def helloboarmap(request: Request):
    return templates.TemplateResponse("helloboar.html", {"request": request})

# @app.post("/files/")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     return {"filename": file.filename}


@app.post("/imageinfo/")
async def imageinfo(file: UploadFile = File(...)):
    contents = await file.read()
    print(type(contents))
    stream=io.BytesIO(contents)
    img = Image.open(stream)
    imgArray = np.array(img)
    print(imgArray.shape)
    print(type(img))
    now = datetime.now()
    resp={'date': now ,'size': [img.width, img.height]}
    return resp

"""Detect a boar from image"""
@app.post("/detectimage/",tags=["detections"])
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    print(type(contents))
    stream=io.BytesIO(contents)
    img = Image.open(stream)
    imgArray = np.array(img)
    threshold=0.95
    prediction= predictions.predict(imgArray,threshold)
    isamatch=predictions.ismatched(prediction)
    labels, boxes, scores=prediction
    scorestr=str(scores)
    now = datetime.now()
    resp={'date': now ,'size': [img.width, img.height],'threshold':threshold,'isamatch':isamatch,'scores':scorestr,'boxes': str(boxes)}
    return resp



"""Detect a boar from image and store it's position and result """
@app.post("/detectandstoreposition/",tags=["detections"])
async def detectandstoreposition(file: UploadFile = File(...),lat:float=44.41726492852156,lon:float=8.949127605715955):
    contents = await file.read()
    print(type(contents))
    stream=io.BytesIO(contents)
    img = Image.open(stream)
    imgArray = np.array(img)
    threshold=0.95
    prediction= predictions.predict(imgArray,threshold)
    isamatch=predictions.ismatched(prediction)
    labels, boxes, scores=prediction
    scorestr=str(scores)
    now = datetime.now()
    resp={'date': now ,'size': [img.width, img.height],'threshold':threshold,'isamatch':isamatch,'scores':scorestr,'boxes': str(boxes)}
    return resp





# if __name__ == '__main__':
# 	predictions.init()