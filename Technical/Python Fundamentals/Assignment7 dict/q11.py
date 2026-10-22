# 11. Create a dictionary from two lists: one list contains keys and the other contains values. Do not use zip().

keys = [1,2,3,4,5,6,7,8,9]
values = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
d = {}
i = 0
j = 0

while i < len(keys) and j < len(values):
  d[keys[i]] = values[j]
  i += 1
  j += 1

while i < len(keys) :
  d[keys[i]] = None
  i += 1

while j < len(values) :
  d[None] = values[j]
  j += 1

print(d)

  

  

