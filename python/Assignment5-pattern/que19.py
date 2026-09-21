'''
* 
* * 
*   *
*     * 
* * * * * 
'''

for i in range(1,6) :
  for j in range(i) :
    if (i == 5) or (j == 0) or (j == i-1) :
      print("*",end="")
    else :
      print(" ",end="")
  print()