from fastapi import FastAPI
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


my_date_string=f"Hello World! It's {dt_string} did you build this?"

app = FastAPI()

@app.get("/")
def index():
    return {"title":my_date_string}