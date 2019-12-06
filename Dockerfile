FROM python:3-alpine 

ADD . /app

RUN pip install redis 

WORKDIR /app 


CMD ["python" , "app.py"]

