# 28. P is one-dimensional array of integers. Write a Java program search for a data VAL from P. If VAL is present in the array then “element found ” otherwise “element not found” should be displayed. 

p = [2,54,5,55,34,4,45,2,35,78,89,42,12,3,32,3,2,22,126,7,8,7]
val = int(input("Enter value :"))

if not p :
  print("List is empty :")
else :
  for i in p :
    if i == val :
      print("Element found")
      break
  else :
    print("Element not found")
  
