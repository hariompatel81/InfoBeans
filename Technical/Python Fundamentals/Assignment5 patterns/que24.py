'''
* 
** 
*@* 
*@@* 
***** 
'''

for i in range(1,6) :
  for j in range(i) :
    if (i == 3 and j == 1) or (i == 4 and j == 1) or (i == 4 and j == 2):
      print("@",end="")
    else :
      print("*",end="")
  print()