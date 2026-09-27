'''
    1 
   22 
  333 
 4444 
55555 
'''

n = int(input("Enter a number :"))
for i in range(1,n+1) :
  for j in range(n,i,-1):
    print(" ",end="")
  for j in range(1,i+1):
    print(i,end="")
  print()