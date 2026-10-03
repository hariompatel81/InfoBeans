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

# list slicing [start:stop:step]
print(x[::-1])
print(x[-8:-4])
print(x[:6])
print(x[2:5])
print(x[1:100])
print(x[1:7:2])
print(x[7:3:-1])

# insert 
# 50 is index value which is not present in list
# so it will add element at the  last{append}

# if negative index is not available thanit will store element at start
x.insert(50,100)
print(x)
x.insert(-44,12)
print(x)

# append 
x.append(32)
print(len(x))
x.extend([24,54])
print(len(x))

# updating multiple elements
x[2:8:2] = ["A","B","C"]
print(x)
x[2] = "D"
print(x)

# deleting elements
del x[1:6:2]
print(x)

# del x # delet entirly
# print(x)

x.remove(100)
print(x)

print(x.pop(6))
print(x)

x.clear()
print(x)

# List comprehension 
# creation 
# create list having element from 1 to 1000
l1 = []
for i in range(1,1001) :
  l1.append(i)

print(l1)

# another way
l2 = [i for i in range(1,1001)]
print(l2)

# data transformation
# l3 = [1,2,3,4]
# result = [1,4,9,16]
l3 = [1,2,3,4]
result = [i*i for i in l3]

print(l3)
print(result)

# data filteration 
l4 = [1,2,3,4,5,6,7]
even_data = [i for i in l4 if i%2==0]
odd_data = [i for i in l4 if i%2]
print(f"{even_data}, {odd_data}")

# list comparison 
# ==, <, <=, >, >= work on data data
l5 = [1,2,3,4]
l6 = [1,2,3]

print(l5 == l6)
print(l5 is l6)
print(l5 is not l6)
print(id(l5))
print(id(l6))
l7 = l5
print(l5 == l7)
print(l5 is l7)
print(l5 is not l7)

# arithmetic opration 
l8 = [1,2,3,4]
l9 = [5,6,7,8]

print(l8 + l9)
l8 = l8 + l9
print(l8)
print(l8*3)
l9 = l8*3
print((l9))









