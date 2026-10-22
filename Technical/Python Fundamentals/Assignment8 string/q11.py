# 11. Count how many times a particular character occurs.

s = "my name is hariom patel"
d = {}

for i in s:
  d[i] = d.get(i,0)+1

print(d)