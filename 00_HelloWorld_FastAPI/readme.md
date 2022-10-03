# Hello World using FastAPI


Just a simple demo of FastAPI to display a webpage [Demonstrates a simple webpage using FastAPI and uvicorn]


This will eventually be moved to the WSL section, however, let's just speedrun it for now

#### Install Python if it's not already
```console
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
sudo apt install python3-venv

```
#### Set Python 3 as default Python
```sudo update-alternatives --install  /usr/bin/python python /usr/bin/python3 1```

#### Using *venv*

```python -m venv venv``` Once that completes ```source venv/bin/activate```

When you are done with *venv* and you'd like to exit the virtual environment, just type ```deactivate``` to exit. 

Note: Don't forget to create a *.gitignore* and add the *venv/* folder so Github doesn't get full of stuff

#### Install FastAPI and uvicorn

```pip install fastapi uvicorn[standard]```

This will install a bunch of stuff, however that should be all you need to start using FastAPI and uvicorn

#### Create the *Hello World*

Create a folder called ```app```
In the *app* folder create file called ```main.py```
In *main.py* paste

```python
from fastapi import FastAPI
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


my_date_string=f"Hello World! It's {dt_string}!"

app = FastAPI()

@app.get("/")
def index():
    return {"title":my_date_string}

```

#### Go live!

Go into your *app* folder and execute: ```uvicorn main:app --host 0.0.0.0 --port 8000```
Open a web browser and navigate to ```localhost:8000``` and you should see some text!

That's pretty much it!