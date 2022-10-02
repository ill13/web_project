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