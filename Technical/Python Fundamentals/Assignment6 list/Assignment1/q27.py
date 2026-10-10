# 26. Write a Java program to find the largest and smallest element of an array.

l = [3,5,5,3,5,3,5,3,6,3,5,5,4,56,445,544]
largest = float('-inf')
smallest = float('inf')

for i in l :
  if largest < i :
    largest = i
  if smallest > i :
    smallest = i

if not l :
  print("list is empty.")
else :
  print("Largest ",largest)
  print("Smallest ",smallest) 