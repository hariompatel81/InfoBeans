# 15) WAP to print alphabets in lowercase

str = input("Enter string data in uppercase(A-Z) only :")

lower = ""
i = 0
while len(str) > i :
  if ord(str[i]) != 32 :
    temp = ord(str[i]) + 32
  else :
    temp = ord(str[i])

  lower += chr(temp)
  i += 1
  
print(lower)