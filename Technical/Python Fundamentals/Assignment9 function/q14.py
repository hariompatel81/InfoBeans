# 14. Remove all digits from a string.

def remove_digit(s):
  l = list(s)
  for ele in s:
    if ord(ele)>=48 and ord(ele)<=57 :
      l.remove(ele)

  return "".join(l)

s = input("Enter string:")
print(f"After removing digit: {remove_digit(s)}")   