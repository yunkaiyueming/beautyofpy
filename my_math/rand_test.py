#coding=utf8
import random

list_data = ["aa","bb","cc","zz","ww","tt"]
tuple_data = ("aa","bb","cc","ww","tt")
print random.random()
print  random.choice(list_data)
print  random.choice(tuple_data)
print random.randint(1, 100)
print random.uniform(1.7,  8.5)
print random.sample(list_data,3)