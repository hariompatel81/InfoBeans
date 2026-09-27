'''
   * 
  *_* 
 *_*_* 
*_*_*_* 
 *_*_* 
  *_* 
   * 
'''
n = int(input("Enter a number :"))
for i in range(1,n+1) :
  for _ in range(n-i) :
    print(" ",end="")
  for j in range(1,i+1) :
    if j==i :
      print("*",end="")
    else :
      print("*_",end="")
  print()

for i in range(n-1,0,-1) :
  for _ in range(n-i) :
    print(" ",end="")
  for j in range(i) :
    if j==i-1 :
      print("*",end="")
    else :
      print("*_",end="")
  print()

