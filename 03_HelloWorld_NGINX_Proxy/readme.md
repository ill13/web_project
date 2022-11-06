# Hello World using Nginx with FastAPI, Docker, Jinja2


Just a demo to use Nginx as a reverse proxy with Docker. So we can host multiple [containers as] websites on a single server

Once you've got NGINX 

- Build your app so that it works in docker
- Push app to docker hub
- Pull the app to your server
- Edit your *docker-compose.yml*
    - Add as many docker images as you'd like and *nginx-proxy* should do all the heavy lifting for you

```yml
version: '3'

services:
  nginx-proxy:
    image: jwilder/nginx-proxy
    ports:
      - "80:80"
    volumes:
      - /var/run/docker.sock:/tmp/docker.sock:ro

  simple-fastapi:
    image: ill13/simple-fastapi:latest
    environment:
      - VIRTUAL_HOST=game.djstolar.com,djstolar.com

  nextcloud:
    image: nextcloud
    environment:
      - VIRTUAL_HOST=cloud.djstolar.com
```


