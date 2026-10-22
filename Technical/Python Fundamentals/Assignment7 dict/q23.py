# 23. Sort a dictionary by its values in ascending order.

d1 = {
  "one": 1,
  "three": 3,
  "two": 2,
  "four": 2
  }
d2 = {}
length = len(d1)

for _ in range(length):
  min = float('inf')  
  min_key = 0
  for key,value in d1.items():
    if min > value :
      min = value
      min_key = key

  d2[min_key] = d1.get(min_key, min)
  d1.pop(min_key)

print(d2)

  

