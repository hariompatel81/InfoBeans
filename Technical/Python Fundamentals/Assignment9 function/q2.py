# 2. Check whether a string is a palindrome.

def ispalindrom(s):
  l = list(s)
  left = 0
  right = len(l)-1
  while left < right:
    l[left], l[right] = l[right], l[left]
    left += 1
    right -= 1
  sr = "".join(l)
  return True if sr == s else False

s = input("Enter string :")
print(f"pelindrom : {ispalindrom(s)}")