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
for i in range(1,n+n) :
  if i <= n :
    for j in range(1,i+1) :
      print("X",end="")
  else :
    for j in range((n+n)-i) :
      print("X",end="")
  print()