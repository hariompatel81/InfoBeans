# 8. Remove all spaces from a string.

s = "my name is hariom patel"
l = list(s)

for i in l:
  if i == " ":
    l.remove(i)

s = "".join(l)
print(s)
