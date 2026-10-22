# 28. Check whether one string is a rotation of another.
# Example: "abcd" and "cdab" → True

def check_rotation(s1,s2):
  if len(s1) != len(s2):
    return False
  else :
    if s1 == s2:
      return True
    else :
      for _ in range(len(s2)):
        last_char = s1[-1]
        l = list(s1)
        for i in range(len(l)-1,0,-1):
          l[i] = l[i-1]
        l[0] = last_char

        s1 = "".join(l)
        if s1 == s2:
          return True
      else :
        return False

s1 = input("Enter string :")
s2 = input("Enter string :")
print(f"{s1} is rotation of {s2} : {check_rotation(s1,s2)}")
        