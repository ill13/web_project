# Hello World using FastAPI


Just a simple demo of FastAPI to display a webpage

Demonstrates a simple webpage with FastAPI


This will eventually be moved to the WSL section, however, let's just speedrun it for now

#### Install Python if it's not already
```bash
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
sudo apt install python3-venv

```
#### Set Python 3 as default Python
```sudo update-alternatives --install  /usr/bin/python python /usr/bin/python3 1```

#### Create a Python venv

```python -m venv venv```

Once that completes

```source venv/bin/activate```

Note: Don't forget to create a *.gitignore* and add the *venv/* folder 

#### Install FastAPI and uvicorn

```pip install fastapi uvicorn[standard]```

This will install a bunch of stuff, however that should be all you need to start hosting

#### Create the *Hello World*

Create a folder called ```app```
In the *app* folder create file called ```main.py```
In *main.py* paste

```python
from fastapi import FastAPI
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


my_date_string=f"Hello World! It's {dt_string} did you build this?"

app = FastAPI()

@app.get("/")
def index():
    return {"title":my_date_string}

```

#### Go live!

Go into your *app* folder and execute: ```uvicorn main:app --host 0.0.0.0 --port 8000```