#coding=UTF8
map_data = {1:"one", 2:"tow", 3:"three"}
list_data = ["a", "b",'c','d']

#遍历map
for k in map_data:
    print  k,map_data[k]

#遍历map
for k,v in map_data.items():
    print k,v

if not map_data.has_key("tt"):
        print "not exsit key tt"

print "-------------------------------------------------------------"

#遍历list
i = 0
for element in list_data:
    print  i, element, list_data[i]
    i += 1

#使用enumerate遍历list_data
for i, j in enumerate(list_data):
    print i, j

print "-----------------------操作map字典--------------------------------------"
print map_data.get(3)
print map_data.items()
print map_data.has_key("tt")
print "所有的keys", map_data.keys()
print "所有的values", map_data.values()
print map_data.viewvalues()
print map_data.__class__
print map_data.__sizeof__()
print map_data.__len__()
#del map_data[3]
#print map_data.clear()
#print map_data.items()