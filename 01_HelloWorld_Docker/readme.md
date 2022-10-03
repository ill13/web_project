# Hello World using FastAPI with Docker


Just a simple demo using *FastAPI* with *Docker* [Demonstrates using *Docker* and ```docker-compose``` to build complete python container]

We are going to copy the *app* folder from the *Hello World FastAPI* project and turn it into a alpine based python container. For you oldheads out there, a Docker container is basically a virtual machine. It's not really a VM, but for our purposes we can think of it as a VM and not worry about the differences.

We are going to install docker and docker-compose in WSL

#### Install *docker* and *docker-compose* if it's not already
```bash
sudo apt update && sudo apt upgrade
sudo apt install docker
sudo apt install docker-compose

```



#### Using ```docker-compose```

Take a look at *docker-compose.yml*

```bash
version: '3'
services:
  simple-FastAPI:
    build: .
    container_name: "simple-FastAPI-container"
    ports:
      - "8001:15410" # 8001=external port and 15410=port where app is running
    volumes:  
      - ./app/:/app
    image: ill13/simple-fastapi:latest
```
```"8001:15410"``` First # is external port- as in what to append to the URL to get to work. Second # is internal port where the container is running. 

When in the directory of the container you want to start, just do :```docker-compose up -d```

After making some changes to your container do ```docker-compose build```

Push the build to docker.io: ```sudo docker-compose push```

Stop a docker container: ```sudo docker stop [name]```
Remove a docker container: ```sudo docker rm [name]```



