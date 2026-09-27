'''
A 
BCD 
EFGHI 
JKLMNOP 
'''

x = 1
for i in range(1,5) :
  for j in range(1,2*i) :
    print(chr(64+x),end="")
    x += 1
  print()