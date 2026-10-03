# WAP to print Square, Cube and Square Root of all numbers from 1 to N 

import math
n = int(input("Enter a number :"))
for i in range(1,n+1) :
  print(f"Square : {i*i} Cube : {i*i*i} Square root : {math.sqrt(i)}")