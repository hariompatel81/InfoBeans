# 29. Given two dictionaries, return the keys whose values are equal in both.

d1 = {1:2, 2:2, 3:5, 4:4, 5:6}
d2 = {2:2, 3:5, 7:7, 4:3, 1:4}

result = []
for key,value in d1.items():
  if value in d2.values():
    result.append(key)

for key,value in d2.items():
  if value in d1.values():
    result.append(key)

print(result)