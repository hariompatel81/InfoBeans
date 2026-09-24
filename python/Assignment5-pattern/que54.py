'''
ABCDE 
 A__D 
  A_C 
   AB 
    A 
'''
n = int(input("Enter a number :"))
for i in range(n,0,-1) :
  for j in range(n,i,-1) :
    print(" ",end="")
  for j in range(i) :
    if i==n or i <= 2 :
      print(chr(65+j),end="")
    else :
      if j==0 or i==j+1 :
        print(chr(65+j),end="")
      else :
        print(" ",end="")
  print()