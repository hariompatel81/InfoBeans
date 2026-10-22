# 28. Check whether one string is a rotation of another.
# Example: "abcd" and "cdab" → True

s1 = "abcd"
s2 = "cdab"
l = list(s1)
rotate = set()

for i in range(len(s1)-1,-1,-1):
  last_digit = s1[i]
  for j in range(len(s1)-1,0,-1):
    l[j] = l[j-1]

  l[0] = last_digit
  s3 = "".join(l)
  rotate.add(s3)

  if s2 in rotate:
    print(True)
    break
  




