import redis
class RedisHelper():
    def __init__(self,host='192.168.1.107',port=6379):
        self._redis = redis.StrictRedis(host,port)
    def get(self,key):
        if self._redis.exists(key):
            return self._redis.get(key)
        else:
            return ""
    def set(self,key,value):
        self._redis.set(key,value)