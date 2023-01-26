import os
import shutil
from typing import List
from dotenv import load_dotenv
from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# get random image https://picsum.photos/1080/1920

# Load Var
load_dotenv()
img_folder: str = os.getenv("img_folder")
static_folder: str = os.getenv("static_folder")
main_url: str = os.getenv("main_url")
print(f"img_folder: {img_folder}")
print(f"static_folder: {static_folder}")
print(f"main_url: {main_url}")

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=static_folder, html=True), name="static")


def get_list_img() -> list:
    return os.listdir(img_folder)


@app.get("/")
async def root():
    return {"status": "up"}


@app.get("/list_img")
async def list_img():
    list_url: list = []
    count = 0
    for i in get_list_img():
        count += 1
        temp_dict = {"name": i, "sort": count, "url": f"{main_url}static/files/{i}", "time": 10}
        list_url.append(temp_dict)
    return {"list_img": list_url}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     with open("destination.png", "wb") as buffer:
#         shutil.copyfileobj(image.file, buffer)
#     return {"filename": file.filename}


@app.post("/uploadfiles/")
async def image(images: List[UploadFile] = File(...)):
    for image in images:
        with open(f"./static/files/{image.filename}", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
