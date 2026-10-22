# 12. Check whether two strings are equal without using == for the complete strings.

def check_equal(s1,s2):
  if len(s1) == len(s2):
    for i in range(len(s1)):
      if ord(s1[i]) - ord(s2[i]):
        return "Not equal"
    else :
      return "Equal"
  else :
    return "Not equal"

s1 = input("Enter string :")
s2 = input("Enter string :")
print(check_equal(s1,s2))