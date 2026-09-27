'''
    A 
   A B 
  A B C 
 A B C D 
A B C D E
'''
n = int(input("Enter a number :"))
for i in range(n,0,-1) :
  for j in range(i-1) :
    print(" ",end="")
  for j in range(n+1-i) :
    print(f"{chr(65+j)} ",end="")
  print()