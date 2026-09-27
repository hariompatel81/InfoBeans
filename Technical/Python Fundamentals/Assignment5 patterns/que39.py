'''
123456 
54321 
1234 
321 
12 
1 
'''

for i in range(7) :
  if i % 2 == 0 :
    for j in range(1,7-i) :
      print(j,end="")
  else :
    for j in range(6-i,0,-1) :
      print(j,end="")
  print()