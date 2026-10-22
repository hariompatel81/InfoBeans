# 17. Count the frequency of each number in a list.
#    Example: [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}

d = {}
l = [1, 2, 2, 3, 1, 2]
for i in l:
  d[i] = d.get(i,0)+1

print(d)
