# 34. Compress a string by counting consecutive repeated characters.
# Example: "aaabbccccd" → "a3b2c4d1"

s = "aaabbccccd"
d = {}
for ele in s:
  d[ele] = d.get(ele,0)+1

l = []
for key, value in d.items():
  l.append(str(key))
  l.append(str(value))

result = "".join(l)
print(result)
  

  