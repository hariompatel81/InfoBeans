# 35. Expand a compressed string.
# Example: "a3b2c4" → "aaabbcccc"

s = "a3b2c4"
l = list(s)
l1 = []
for i in range(1,len(l)):
  if l[i].isdigit():
    l1.append(l[i-1]*int(l[i]))

result = "".join(l1)
print(result)

