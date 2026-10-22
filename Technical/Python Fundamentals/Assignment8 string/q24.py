# 24. Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae"

s = "Python is easy"
result = ""
l = s.split(" ")
l2 = []
for ele in l:
  l2.append(ele[::-1])

result = " ".join(l2)
print(result)
