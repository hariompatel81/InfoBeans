'''
    1 
   212 
  32123 
 4321234 
543212345 
'''
n= int(input("Enter a number :"))
for i in range(1,n+1) :
  for j in range(n,i,-1) :
    print(" ",end="")
  for j in range(i,0,-1) :
    print(j,end="")
  for j in range(1,i) :
    print(j+1,end="")
  print()
  
