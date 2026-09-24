'''
ABCDE 
A  D 
A C
AB 
A
'''

for i in range(5,0,-1) :
  for j in range(i) :
    if (i==5) or (j==0) or (i==j+1) :
      print(chr(65+j),end="")
    else :
      print(" ",end="")

  print()