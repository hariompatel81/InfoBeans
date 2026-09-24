'''
    1 
   11 
  1*1 
 1**1 
11111 
'''

n = int(input("Enter a number :"))
for i in range(1,n+1) :
  for j in range(n-i) :
    print(" ",end="")
  for j in range(i) :
    if i <= 2 or n==i :
      print(1,end="")
    else :
      if j==0 or i==j+1 :
        print(1,end="")
      else :
        print("*",end="")
  print()