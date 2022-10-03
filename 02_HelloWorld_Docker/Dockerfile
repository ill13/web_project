# Chose a container; alpine is like a tiny linux distro VM
FROM python:3.8-alpine  

# Install our required python libraries
RUN pip3 install fastapi uvicorn  

# Copy our app folder and contents *into* the container
COPY ./app /app

# Execute the same command from HelloWorld FastAPI, but this time run it in the container on port 9000
CMD ["uvicorn", "app.main:app", "--host","0.0.0.0", "--port","9000"]

# Need for nginx later [probably delete for this section]
EXPOSE 9000

