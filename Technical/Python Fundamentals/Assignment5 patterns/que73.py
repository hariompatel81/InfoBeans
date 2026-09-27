'''
5 5 5 5 5 
 4 4 4 4 
  3 3 3 
   2 2 
    1 
'''
n = int(input("Enter a number :"))
for i in range(n,0,-1) :
  for j in range(n-i) :
    print(" ",end="")
  for j in range(i) :
    print(f"{i} ",end="")
  print()