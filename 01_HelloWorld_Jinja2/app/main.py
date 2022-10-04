from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from datetime import datetime


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


my_date_string=f"Hello World using FastAPI, uvicorn, and Jinja2! It's {dt_string}!"

app = FastAPI()
templates = Jinja2Templates("templates") # folder where your templates are stored
app.mount("/static", StaticFiles(directory="static"), name="static")



# @app.get("/")
# def index():
#     return {"title":my_date_string}


@app.get("/")

def index(request: Request):
    return templates.TemplateResponse("index.html",context={"request":request,'title':'Demo0'})
