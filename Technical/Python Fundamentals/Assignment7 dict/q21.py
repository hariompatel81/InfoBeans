# 21. Combine two dictionaries by adding the values of common keys.
#     Example: {'a': 10, 'b': 20} and {'b': 5, 'c': 7}
#     Expected: {'a': 10, 'b': 25, 'c': 7}

d1 = {'a': 10, 'b': 20}
d2 = {'b':5, 'c':7}

print("Input")
print(d1)
print(d2)
for key,value in d2.items():
  if key in d1:
    d1[key] = d1[key] + value
  else :
    d1[key] = value

print("Output")
print(d1)