# Hello World using FastAPI with Docker


Just a simple demo using *FastAPI* with *Docker*

Demonstrates using *Docker* and ```docker-compose``` to build complete python container

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



