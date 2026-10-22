#  27. Group words that are anagrams of one another.
#     Example: ["eat", "tea", "bat", "ate"]
#     Expected groups: ["eat", "tea", "ate"] and ["bat"]

l = ["eat", "tea", "bat", "ate"]
d = {}

for ele in l:
  s = "".join(sorted(ele))

  if s not in d:
    d[s] = []
  
  d[s].append(ele)

print(d)
print(list(d.values()))


