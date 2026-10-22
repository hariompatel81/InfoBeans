# 15. Create a dictionary in which numbers from 1 to 5 are keys and their squares are values.

# d = {i:i*i for i in range(1,6)}
# print(d)


d = {}
for i in range(1,6) :
  d[i] = i*i

print(d)
