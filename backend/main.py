from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os.path
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/img/{img_id}")
async def get_img(img_id):
    img_path = './img/{0}.png'.format(img_id)
    print(img_path)
    try:
        os.path.isfile(img_path)
    finally:
        img_path = './img/no_img.png'
        
    return FileResponse(img_path)

class Product(BaseModel):
    id: str
@app.post("/product")
async def post_product(x: Product):
    print(x)
    return {"img_path":"http://127.0.0.1:8000/img/{0}".format(x.id)}
