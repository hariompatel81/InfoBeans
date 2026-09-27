'''
   * 
  *_*  
 *___*  
*_____* 
 *___*  
  *_* 
   * 
'''
n = int(input("Enter a number :"))
for i in range(1,n+1) :
  for _ in range(n-i) :
    print(" ",end="")
  for j in range(2*i-1) :
    if j==0 or j==2*i-2 :
      print("*",end="")
    else :
      print(" ",end="")
  print()

for i in range(1,n) :
  for _ in range(i) :
    print(" ",end="")
  for j in range(2*(n-i)-1) :
    if j==0 or j==2*(n-i)-2 :
      print("*",end="")
    else :
      print(" ",end="")
  print()