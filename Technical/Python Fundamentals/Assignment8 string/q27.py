# 27. Find all duplicate characters and their frequencies.

s = "aad dsd fffrr edv ccf r"
d = {}
import copy
for i in s:
  d[i] = d.get(i,0)+1

d2 = copy.deepcopy(d)
for i in d2:
  if d[i] == 1 or i==" ":
    d.pop(i)

print(d)