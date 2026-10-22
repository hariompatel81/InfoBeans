# 1. Write a program to reverse a string without using slicing ([::-1])

s = "hariom"
l = list(s)
left = 0
right = len(s)-1
while left < right:
  l[left],l[right] = l[right],l[left]
  left += 1
  right -= 1

s = "".join(l)
print(s)
