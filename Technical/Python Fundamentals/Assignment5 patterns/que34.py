'''
EEEEE 
DDDD 
CCC 
BB 
A 
'''

for i in range(5,0,-1) :
  for j in range(i):
    print(chr(64+i),end="")
  print()