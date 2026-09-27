# 14) WAP to print alphabets in uppercase

char = input("Enter string data in lowercase(a-z) only :")
upper = ""
i = 0
while len(char) > i :
  if ord(char[i]) != 32 :
    temp = ord(char[i]) - 32
  else :
    temp = ord(char[i])

  upper += chr(temp)
  i += 1

print(upper)