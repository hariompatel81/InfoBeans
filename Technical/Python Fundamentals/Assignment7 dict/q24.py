# 24. Group a list of words according to their length.
# Example: ["cat", "apple", "dog", "mango"]
# Expected groups: 3 -> ["cat", "dog"], 5 -> ["apple", "mango"]

l = ["cat", "apple", "dog", "mango","djfjkdfvdfhbv"," dfjfjv",]
d = {}

for word in l:
  if len(word) not in d:
    d[len(word)] = [word]
  else :
    d[len(word)].append(word)

print(d)
  