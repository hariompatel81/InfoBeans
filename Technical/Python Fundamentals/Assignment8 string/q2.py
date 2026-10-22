# 2. Check whether a string is a palindrome.

s = "nitan"
l = list(s)
left = 0
right = len(s)-1
while left < right:
  l[left],l[right] = l[right],l[left]
  left += 1
  right -= 1

revers = "".join(l)
if s == revers:
  print("String is pelindrom.")
else :
  print("String is not pelindrom.")