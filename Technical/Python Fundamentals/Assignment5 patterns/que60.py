'''
    X  
   X X  
  X___X 
 X_____X 
X X X X X 
'''
n = int(input("Enter a number :"))
for i in range(1,n+1) :
  for j in range(n-i) :
    print(" ",end="")
  for j in range(1,i+1) :
    if i <= 2 or i==n :
      print(f"X ",end="")
    else :
      if j==1 or j==i :
        print(f"X ",end="")
      else :
        print("  ",end="")
  print()