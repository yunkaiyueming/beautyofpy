
add = lambda x,y : x+y
print(add(1,2))

double = lambda x :x+x
numbers = [1,2,3,4,5]
print(list(map(double, numbers)))

file_func = lambda x:x%2==0

print(list( filter(file_func, numbers) ) )