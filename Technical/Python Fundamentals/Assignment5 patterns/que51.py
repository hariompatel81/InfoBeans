'''
55555 
 4444 
  333 
   22 
    1 
'''
n = int(input("Enter a number :"))
for i in range(n,0,-1) :
  for j in range(n,i,-1) :
    print(" ",end="")
  for j in range(i):
    print(i,end="")
  print()