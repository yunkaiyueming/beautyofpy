#coding=utf8

from pymongo import MongoClient

uri = "mongodb://%s:%s@%s:%s" % ('root', '123456', '127.0.0.1','27017')
client = MongoClient(uri)
datas= client.yama_bi.url_view.find({'app_name':'bi'})
for data in datas:
    print data