from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for simplicity. In production, you should specify the allowed origins explicitly.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with the list of allowed origins if you know them
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sum")
def calculate_sum():
    result = 5 + 2
    return {"result": result}

# def calculate_sum(num1: int, num2: int):
#     result = num1 + num2
#     return {"result": result}
   
