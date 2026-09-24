'''
1 
10 
1 1 
1  0 
10101 
'''

for i in range(1,6) :
  for j in range(i) :
    if (i==5) or (j==0) or (i==j+1) :
      if j % 2 == 0 :
        print(1,end="")
      else :
        print(0,end="")
    else :
      print(" ",end="")
  print()