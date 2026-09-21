'''
1 
00 
111 
0000 
11111 
'''

for i in range(1,6) :
  for j in range(i) :
    if i % 2 == 0 :
      print(0,end="")
    else :
      print(1,end="")
  print()