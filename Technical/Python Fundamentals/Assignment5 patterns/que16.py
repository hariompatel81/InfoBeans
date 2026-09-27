'''
a 
bc 
def 
ghij 
klmno 
'''
x = 0
for i in range(1,6) :
  for j in range(i) :
    print(chr(97 + x),end="")
    x += 1
  print()