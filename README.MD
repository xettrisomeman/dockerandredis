# Simple python app with docker and redis

## This app does set a redis value

## Use following commands to build the app

```docker
docker build -t <your_app_name> .
```

## After building the it will execute the code inside of Dockerfile

## Afer your app is built , run following commands

```docker
docker run -d --network=host redis
```

## You create a network host to host the redis on docker

## After the above code do the following to run the redis

```docker
docker run --network=host <your_app_name>
```
