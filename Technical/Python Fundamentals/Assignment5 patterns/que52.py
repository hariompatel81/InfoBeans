'''
12345 
 1__4 
  1_3 
   12 
    1 
'''
n = int(input("Enter a number :"))
for i in range(n,0,-1) :
  for j in range(n,i,-1) :
    print(" ",end="")
  for j in range(1,i+1) :
    if i==n or i <= 2 :
      print(j,end="")
    else :
      if j==1 or j==i :
        print(j,end="")
      else :    
        print(" ",end="")
  print()