# 9. Find the first and last character of a string.

def findflch(s) :
  if not s :
    print("String is empty.")
    return None
  else :
    return s[0],s[-1]

s = "unrvy489tr8"
print(f"First and last charecter is : {findflch(s)}")