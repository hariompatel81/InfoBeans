# 8. Remove all spaces from a string.

def remove_space(s) :
  l = []
  for ele in s :
    if ele != " " :
      l.append(ele)

  return "".join(l)

s = input("Enter string :")
print(f"String after removing spaces {remove_space(s)}")
