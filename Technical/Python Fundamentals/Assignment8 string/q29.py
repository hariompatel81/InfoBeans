# 29. Remove a particular character from a string without using replace().

s = "Remove a particular character from a string withou"
ch = "r"
l = list(s)

for i in l:
  if i==ch:
    l.remove(i)

result = "".join(l)
print(result)