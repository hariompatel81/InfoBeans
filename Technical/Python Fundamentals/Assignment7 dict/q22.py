# 22. Find the common keys between two dictionaries.

d1 = {1:"one", 2:"two", 3:"three"}
d2 = {2:4, 5:25, 6:36, 3:9}

print("Input")
print(d1)
print(d2)

print("Comman keys :")
flag = True
for i in d2:
  if i in d1:
    print(i, end=" ")
    flag = False

print()
if flag:
  print("Both dictionary have unique keys...")





