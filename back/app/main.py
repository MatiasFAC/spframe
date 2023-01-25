import os
from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles

# get random image https://picsum.photos/1080/1920

app = FastAPI()

img_folder: str = "./static/files/"
main_url: str = "http://127.0.0.1/"

app.mount("/static", StaticFiles(directory="static"), name="static")


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
