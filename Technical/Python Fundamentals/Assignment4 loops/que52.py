# WAP to reverse all the numbers between two entered numbers 

a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))

for i in range(a+1,b) :
  x = i
  rev = 0
  while i :
    rem = i % 10
    rev = 10*rev + rem
    i //= 10
  print(f"Reverse of {x} is {rev}")
