'''
    1 
   1 1 
  1 2 1 
 1 3 3 1 
1 4 6 4 1 
'''
n = int(input("Enter a number :"))
str = ""
for i in range(n) :
  # for space
  for j in range(n-i+1) :
    print(" ",end="")
  # first get last digit than store in string with space
  temp = 11**i
  while temp :
    r = temp % 10
    str += f"{r} "
    temp = temp//10
  # reverce a string data
  str2 = ""
  for i in range(len(str)-1,-1,-1) :
    str2 += str[i]
  # than print reverce string and make empty string
  print(str2)
  str = ""
  str2 = ""
