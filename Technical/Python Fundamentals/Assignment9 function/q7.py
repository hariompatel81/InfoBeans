# 7. Convert lowercase characters to uppercase without using upper().
#   s = "inDor434e"  => "INDOR434E"

def uppercase(s) :
  l = []
  for ele in s :
    if ord(ele)>=97 and ord(ele)<=122 :
      l.append(chr(ord(ele)-32))
    else :
      l.append(ele)

  return "".join(l)

s = input("Enter string :")
print(f"Upper case string {uppercase(s)}")