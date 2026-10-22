# 16. Count the frequency of each character in a string.
#    Example: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}

d = {}
s = "Hariom Patel"
for ch in s:
  d[ch] = d.get(ch,0)+1

print(d)

