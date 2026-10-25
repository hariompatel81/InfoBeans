# 35. Expand a compressed string.
# Example: "a3b2c4" → "aaabbcccc"

def expand_string(s):
  s1 = []
  result = ""
  for ele in s:
    if ele.isdigit():
      result += "".join(s1)*int(ele)
      s1 = []
    else :
      s1.append(ele)
  if not s1:
    return result
  else :
    result += "".join(s1)
    return result

s = input("Enter string : ")
print(f"Expanded string is : {expand_string(s)}")

