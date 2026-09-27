'''
***** 
*  * 
* * 
** 
* 
'''

for i in range(1,6) :
  for j in range(5,i-1,-1) :
    if (i==1) or (j==5) or (i==j) :
      print("*",end="")
    else :
      print(" ",end="")
  print()