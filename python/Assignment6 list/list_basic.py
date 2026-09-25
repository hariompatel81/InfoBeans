import sys

# list 
x = [1,2,3,4,5]
print(f"List element :{x}")
print(f"Type of list :{type(x)}")
print(f"Length of the list :{len(x)}")

# index based access
for i in range(len(x)) :
  print(f"Index : {x[i]} Value : {x[i]}")

# value based access
for j in x :
  print(j,end='')
print()

# get size of a list
print(f"Data : {x}")
print(f"Length : {len(x)}")
print(f"Size : {sys.getsizeof(x)}")

# adding element into the list at last
print(f"List data before adding : {x}")
x.append(100)
print("After adding 100")
print(f"Data : {x}")
print(f"Length : {len(x)}")
print(f"Size : {sys.getsizeof(x)}")

print(f"List before.")
x.append(200)
print(f"Data : {x}")
print(f"Length : {len(x)}")
print(f"Size : {sys.getsizeof(x)}")

# add element according to index
x.insert(1,34) 
print(f"add element at index 1 : {x}")
x.insert(3,"hello")

# 








