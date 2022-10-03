from fastapi import FastAPI
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


my_date_string=f"Hello World using FastAPI, uvicorn, and Docker! It's {dt_string}!"

app = FastAPI()

@app.get("/")
def index():
    return {"title":my_date_string}