# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{9[6()]}(){}" → True, "([)]" → False

def check_balanced_par(s):
  if not s:
    return False
  elif len(s) == 1:
    return False
  else :
    bucket = {'{':'}','[':']','(':')'}
    bucket2 = {'}',']',')'}
    l = []
    for ele in s:
      if ele in bucket:
        l.append(bucket[ele])
      else :
        if ele in bucket2:
          if ele != l.pop():
            return False
    else :
      if l:
        return False
      else :
        return True
      
s = input("Enter string :")
print(f"{s} is balenced : {check_balanced_par(s)}")


# without function

# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False

# s = "  {1[3(123)4]5}  "
# l = list(s)

# l1 = []
# for ele in l:
#   if ele == "{":
#     l1.append("}")
#   elif ele == "}":
#     l1.append("{")
#   elif ele == "(":
#     l1.append(")")
#   elif ele == ")":
#     l1.append("(")
#   elif ele == "[":
#     l1.append("]")
#   elif ele == "]":
#     l1.append("[")

# sat = {'[',']','{','}','(',')'}
# for ele in l:
#   if ele in sat:
#     if ele != l1.pop():
#       print(False)
#       break

# else :
#   print(True)




