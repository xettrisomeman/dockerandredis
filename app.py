import redis 


def hello_redis():

    rediss = redis.Redis()

    rediss.set("name" , "hello")

    print(rediss.get("name"))



hello_redis()