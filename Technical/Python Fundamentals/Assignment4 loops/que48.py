# WAP to print tables of all the numbers between two entered numbers 
a = int(input("Enter fist number :"))
b = int(input("Enter secound number :"))

if a < b :
  for i in range(a+1,b) :
    for j in range(1,11) :
      print(i*j,end=" ")
    print()
else :
  for i in range(b+1,a) :
    for j in range(1,11) :
      print(i*j,end=" ")
    print()