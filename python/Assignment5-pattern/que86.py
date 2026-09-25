'''
********** 
****  **** 
***    *** 
**      ** 
*        * 
'''
n = int(input("Enter a number :"))
for i in range(n) :
  for j in range(n,i,-1) :
    print("*",end="")
  for j in range(2*i) :
    print(" ",end="")
  for j in range(n,i,-1) :
    print("*",end="")
  print()

# another approach
for i in range(n) :
  for j in range(1,2*n) :
    if j <= n-i or j >= n+i :
      print("*",end="")
    else :
      print(" ",end="")
  print()
    