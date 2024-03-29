# A tutorial on using Python with a newer style of webdev [versus LAMP ]

This 'newer style webdev / coding' tutorial will cover 
- Local code dev with **WSL2** and **Microsoft Visual Studio Code**
- *Remote code editing* with MSVSCode for *CI / CD* [continuous integration and development]
- Production ready web serving with **FastAPI**
- Modern web templating and design with **Jinja2** [using *Bootstrap* and CSS]
- Using containers with **docker** and **docker-compose**
- Using **NGINX** for *SSL* and as a *reverse proxy*


There is an assumption you are somewhat familiar with Linux and WSL, Scripting, Python, Webdev, VSCode, Docker, and Github. You should certainly already have accounts and know how to authenticate via the command line for Github and Docker.
***

### To work on this project locally
- ```wsl``` Fire up *WSL* from a command line
 - Setup *WSL* with ```wsl --install```, then follow the prompts
- ```cd ~``` Navigate to *home*. You can store this repo wherever you want, I use *~/code/*
- ```gh repo clone ill13/web_project``` Clone this repo to your home folder
- ```code .``` To open VS Code with this project loaded
- You may need to install *https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack* to get the ```venv``` to be recognized.


### *Github*: Quick Reference
- ```ptg "things you did"``` to push to github [ptg]: See the *Push to GitHub* in *01_Prereqs/Prereq_GitHub/readme.md*
- Github being pissy and you want to overwrite? : ```git push origin --force``` then do regular push like ```ptg "stuff"```
- ```git rm -r [filename or folder]``` then ```ptg "removed [fn or folder]"``` to get rid of things like *venv* or *__pycache__* 

### *venv*: Quick Reference
*venv* is a temporary and self-contained build environment so you don't screw up your main Python install, later *Docker* will replace *venv*
- ```python -m venv venv``` or ```py -3.9 -m venv venv``` (to force a specific version) Once that completes you can use
- ```source venv/bin/activate``` to start the virtual environment in Linux/WSL. 
- ```venv/scripts/activate``` to start the virtual environment in Windows
-  ```deactivate``` When you are done with *venv* and you'd like to exit the virtual environment, just type *deactivate* to exit. 
- Note: Don't forget to create a *.gitignore* and add the *venv/* folder so Github doesn't get full of stuff

### *docker-compose*: Quick Reference
- ```docker-compose up -d``` When in the directory of the container you want to build and start
- ```docker-compose build``` After making some changes to your container
- ```sudo docker-compose push``` Push the build to docker.io
- ```sudo docker stop [name]``` Stop a docker container
- ```sudo docker rm [name]``` Remove a docker container
- ```sudo docker ps``` Show active docker containers
 
