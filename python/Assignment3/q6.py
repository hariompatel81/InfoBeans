# 6. Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

value = int(input("Enter a value :"))
if value > 0 :
  print(value)
elif value < 0 :
  print(value*(-1))
else :
  print(value)