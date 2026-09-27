'''
    1 
    2 
    3 
    4 
123454321 
    4 
    3 
    2 
    1 
'''
n = int(input("Enter a number :"))

for i in range(1,2*n) :
  for j in range(1,2*n) :
    if i < n and j == n :
      print(i,end="")
    elif i == n :
      if j <= n :
        print(j,end="")
      else :
        print(2*n-j,end="")
    elif i > n and j == n :
      print(2*n-i,end="")
    else :
      print(" ",end="")
  print()

#another approach
n = int(input("Enter a number :"))
for i in range(1,2*n) :
  for j in range(1,n+1) :
    if i < n and j==n :
      print(i,end="")
    elif i==n :
      if j < n :
        print(j,end="")
      else :
        for k in range(n,0,-1) :
          print(k,end="")
    elif i>n and j==n :
      print(2*n-i,end="")
    else :
      print(" ",end="")
  print()      

