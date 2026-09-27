'''
55555 
4  4 
3 3 
22 
1 
'''

for i in range(5,0,-1) :
  for j in range(i) :
    if (i==5) or (j==0) or (i==j+1) :
      print(i,end="")
    else :
      print(" ",end="")
  print()
