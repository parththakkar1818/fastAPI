from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests as req
from bs4 import BeautifulSoup as bs

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

@app.get("/addtwonumber") 
def add_two_numbers(number1: float, number2: float):
    """Add two numbers together"""
    result = number1+number2
    return {"result": result}

@app.get("/getprice")
def getFlipkartPrice(productUrl: str):
    head={"User Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
    page=req.get(productUrl)
    soup= bs(page.content, "html.parser")
    data = soup.find("div", class_="_30jeq3")
    price=data.text.split()[0].replace('₹','').replace(',','')
    return {"price":price}
