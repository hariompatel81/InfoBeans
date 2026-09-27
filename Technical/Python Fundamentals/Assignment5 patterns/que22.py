'''
A 
AB 
A C 
A  D 
ABCDE
'''

for i in range(1,6) :
  for j in range(i) :
    if (i==5) or (j==0) or (i==j+1) :
      print(chr(65+j),end="")
    else :
      print(" ",end="")
  print()