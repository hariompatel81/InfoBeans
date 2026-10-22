# 25. Check whether a string contains only digits without using isdigit().

def check_only_digit(s):
  for ele in s:
    if not (ord(ele)>=48 and ord(ele)<=57):
      return False
  else :
    return True

s = input("Enter string :")
print(f"is string contain only digit : {check_only_digit(s)}")
