from urllib import response
from fastapi import FastAPI, File
from seg import get_custom_yolov5, get_image_from_bytes, get_pretrained_yolo
from starlette.responses import Response
import io
import cv2
import base64
from PIL import Image
import json
from fastapi.middleware.cors import CORSMiddleware
model = get_custom_yolov5()
model2 = get_pretrained_yolo()
app = FastAPI(
    title="Custom YOLOV5 API To Detect Drowsiness ",
    description=""" Get predicted class
    and return image and json result""",
    version="0.0.1",
)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]
app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
)

@app.get('/notify/v1/health')
def get_health():
    return dict(msg='OK')

@app.post("/obj-to-json")
async def detect_drowisness_return_json_result(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = model(input_image)
    detect_res = results.pandas().xyxy[0].to_json(orient="records")
    detect_res = json.loads(detect_res)
    return {"Detected_results": detect_res}

@app.post("/obj-to-img")
async def detect_drowisness_return_base64_img(file: bytes = File(...)):
    image = get_image_from_bytes(file)
    results = model(image)
    temp = results.render()  # updates results.imgs with boxes and labels
   
    bytes_io = io.BytesIO()
    imgbase64 = Image.fromarray(temp[0])
    imgbase64.save(bytes_io, format="jpeg")
    return Response(content=bytes_io.getvalue(),
media_type="image/jpeg")



@app.post("/withoutCustomeobj-to-img")
async def detect_drowisness_return_base64_img(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = model2(input_image)
    temp = results.render()  # updates results.imgs with boxes and labels
   
    bytesio = io.BytesIO()
    imgbase64 = Image.fromarray(temp[0])
    imgbase64.save(bytesio, format="jpeg")
    return Response(content=bytesio.getvalue(),
media_type="image/jpeg")