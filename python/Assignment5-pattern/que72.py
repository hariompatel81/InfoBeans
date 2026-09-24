'''
A B C D E 
 A B C D 
  A B C 
   A B 
    A 
'''
n = int(input("Enter a number :"))
for i in range(n,0,-1) :
  for j in range(n-i) :
    print(" ",end="")
  for j in range(i) :
    print(f"{chr(65+j)} ",end="")
  print()