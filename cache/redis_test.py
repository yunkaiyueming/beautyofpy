#coding=utf8

import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379)
print r.get("city_69")
print r.keys("*city*")
print r.keys("*user*")
print r.hkeys("user:130")

print r.hget("user:130", "id"),r.hget("user:130", "name"),r.hget("user:130", "age")
#r.hset("user:130","name", "tony_130")