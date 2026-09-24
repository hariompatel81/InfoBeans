'''
   1 
  12
 123 
1234 
 123 
  12 
   1 
'''
n = int(input("Enter a number :"))
for i in range(1,n+1) :
  for _ in range(n-i) :
    print(" ",end="")
  for j in range(1,i+1) :
    print(j,end="")
  print()
for i in range(1,n) :
  for _ in range(i) :
    print(" ",end="")
  for j in range(1,n+1-i) :
    print(j,end="")
  print()
