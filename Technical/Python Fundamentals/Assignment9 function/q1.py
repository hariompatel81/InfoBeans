# 1. Write a program to reverse a string without using slicing ([::-1]).

def reverse(s):
  l = list(s)
  left = 0
  right = len(l)-1
  while left < right:
    l[left], l[right] = l[right], l[left]
    left += 1
    right -= 1
  return "".join(l)
  

s = input("Enter string :")
print(f"reverse : {reverse(s)}")

