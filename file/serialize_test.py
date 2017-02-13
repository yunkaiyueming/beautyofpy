#coding=utf8
import pickle
import pprint

list_data = ["nihao","我们的","tsfd",1231]
pprint.pprint(list_data)

serialize_data = pickle.dumps(list_data)
pprint.pprint(serialize_data)

un_serialize_data = pickle.loads(serialize_data)
pprint.pprint(un_serialize_data)