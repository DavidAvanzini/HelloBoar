import json
from datetime import datetime
from detecto.core import Model
from detecto import utils
import io
import numpy as np
from PIL import Image
import predictions


from typing import Optional
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Request
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

predictions.init()
app = FastAPI()
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
@app.post("/detectimage/")
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




# if __name__ == '__main__':
# 	predictions.init()