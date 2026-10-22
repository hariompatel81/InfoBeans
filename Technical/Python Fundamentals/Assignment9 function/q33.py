# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False

# def check_balanced_par(s):
#   bucket = {'{':'}','[':']','(':')'}
#   l = []
#   for ele in s:
#     if ele in bucket:
      


# s = input("Enter string :")
# print(f"{s} is balenced : {check_balanced_par(s)}")

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
  

s = "([)]"
d = {"{":"}","[":"]","(":")"}
l1 = []

for ele in s:
  if ele in d:
    if ele == "{":
      l1.append(d["{"])
    elif ele == "[":
      l1.append(d["["])
    else :
      l1.append(d["("])
  else :
    if ele != l1.pop():
      print(False)
      break
else :
  print(True)



