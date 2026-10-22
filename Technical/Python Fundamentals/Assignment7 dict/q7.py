# 7. Find the number of key-value pairs in a dictionary without using len().

d = {i:i*i for i in range(6)}
count = 0
for i in d :
  count += 1

print(f"{count} key-value pair exist in dictionary...")