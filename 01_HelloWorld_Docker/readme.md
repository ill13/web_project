# Hello World using FastAPI with Docker


Just a simple demo using *FastAPI* with *Docker* [Demonstrates using *Docker* and ```docker-compose``` to build complete python container]

We are going to copy the *app* folder from the *Hello World FastAPI* project and turn it into a alpine based python container. For you oldheads out there, a Docker container is basically a virtual machine. It's not really a VM, but for our purposes we can think of it as a VM and not worry about the differences.

We are going to install *docker* and *docker-compose* in WSL

## Install *docker* and *docker-compose* if it's not already

```bash
sudo apt update && sudo apt upgrade
sudo apt install docker
sudo apt install docker-compose

```
## Running *docker*

```
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
sudo usermod -aG docker $USER
```

Probably need to login to Docker.io with ```sudo docker login docker.io```

To start *docker* under WSL you'll need to fire up a new PowerShell terminal and run ```sudo dockerd```

In your main VSCode terminal window you can start your FastAPI app with ```docker-compose up -d```. The *-d* flag allows you to run it detached so you can free your current terminal window for more commands.

Open a web browser and navigate to ```localhost:8000``` and you should see some updated text!

## Using ```docker-compose```

When in the directory of the container you want to start, just do :```docker-compose up -d```

After making some changes to your container do ```docker-compose build```

Push the build to docker.io: ```sudo docker-compose push```

Stop a docker container: ```sudo docker stop [name]```

Remove a docker container: ```sudo docker rm [name]```




