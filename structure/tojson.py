#coding=UTF8
import json,urllib2

map_data = {"name":"张三", "age":12, "pwd":"qsxxx"}
json_str = json.dumps(map_data)
print json_str, type(json_str)

json_str2 = json.dumps(map_data,sort_keys=True,indent =4,separators=(',', ': '),encoding="utf8",ensure_ascii=False )
print json_str2,type(json_str2)

print '---------------------json转python内置数据结构----------------------------------'
decode_data = json.loads(json_str2); print decode_data,type(decode_data)
decode_data2 = json.loads(json_str2, encoding="utf8"); print decode_data2,type(decode_data2)
print decode_data['name'], type(decode_data['name']) #获取到的是中文
print decode_data2["name"]