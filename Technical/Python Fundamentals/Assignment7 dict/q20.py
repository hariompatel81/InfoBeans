# 20. Reverse a dictionary so that values become keys and keys become values. Assume all values are unique.

d = {i:i*i for i in range(1,6)}
d1 = {}
for key,value in d.items() :
  d1[value] = key

print(d)
print(d1)
  

