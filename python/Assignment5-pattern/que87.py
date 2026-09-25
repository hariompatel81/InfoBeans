'''
********** 
****  **** 
***    *** 
**      ** 
*        * 
*        * 
**      ** 
***    *** 
****  **** 
********** 
'''
n = int(input("Enter a number :"))
x = 10
for i in range(1,2*n+1) :
  if i <= n :
    for j in range(1,2*n+1) :
      if j <= n+1-i or j >= n+i :
        print("*",end="")
      else :
        print(" ",end="")
    print()
  else :
    for j in range(1,2*n+1) :
      if j <= i-n or j >= x :
        print("*",end="")
      else :
        print(" ",end="")
    print()
    x -= 1 

print("\n\n")

# another aproach
for i in range(n,0,-1) :
  for j in range(1,2*n+1) :
    if j <= i or j > 2*n - i :
      print("*",end="")
    else :
      print(" ",end="")
  print()

for i in range(1,n+1) :
  for j in range(1,2*n+1) :
    if j <= i or j > 2*n - i :
      print("*",end="")
    else :
      print(" ",end="")
  print()