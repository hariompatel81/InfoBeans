'''
    A 
   AB 
  A_C 
 A__D 
ABCDE 
'''
n = int(input("Enter a number:"))
for i in range(1,n+1) :
  for j in range(n-i) :
    print(" ",end="")
  for j in range(i) :
    if i <= 2 or i==j+1 :
      print(chr(65+j),end="")
    else :
      if j==0 or i==n :
        print(chr(65+j),end="")
      else :
        print(" ",end="")
  print()