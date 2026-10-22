# 7. Convert lowercase characters to uppercase without using upper().
#  s = "inDor434e"  => "INDOR434E"

s = "inDor434e"
l = []
for i in s :
  if (ord(i) >= 97 and ord(i) <= 122) :
    l.append(chr(ord(i)-32))
  else :
    l.append(i)

s = "".join(l)  
print(s)
