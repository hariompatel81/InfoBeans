'''
55555 
 4__4 
  3_3 
   22 
    1 
'''

n = int(input("Enter a number :"))
for i in range(n,0,-1) :
  for j in range(n,i,-1) :
    print(" ",end="")
  for j in range(i) :
    if i==n or i <= 2 :
      print(i,end="")
    else :
      if j==0 or i==j+1 :
        print(i,end="")
      else :
        print(" ",end="")
  print()

