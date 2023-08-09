from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from datetime import datetime

# Create an f string
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
my_string=f"Hello World using FastAPI, uvicorn, and Jinja2! It's {dt_string}!"

# Open a local text file and add each line to a list as an item
with open('text.txt') as f:
    my_list = list(f)


app = FastAPI()
templates = Jinja2Templates("templates") # folder where your HTML templates are stored
app.mount("/static", StaticFiles(directory="static"), name="static") # folder containing styles.css


@app.get("/")

async def index(request: Request):
    return templates.TemplateResponse("index.html",context={'request':request,'title':"Demo0", 'content':my_string, 'my_list':my_list})


# @app.get("/butt")

# async def index(request: Request):
#     return templates.TemplateResponse("index.html",context={'request':request,'title':"Demo0", 'content':my_string, 'my_list':my_list})
