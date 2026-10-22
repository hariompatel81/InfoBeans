# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"

s = "programming"
print("Before")
print(s)
d = {}
l = []
for ch in s :
  d[ch] = d.get(ch,0)+1
  if d[ch] == 1:
    l.append(ch)

s = "".join(l)
print("After")
print(s)
