# 9. Find the key associated with the largest value in a dictionary.

d = {i:i*i for i in range(5)}

max = float('-inf')
for i in d.keys():
  if max < d[i] :
    max = d[i]
    key = i

print(f"{i} associated with {max}")