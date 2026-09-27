# WAP to print factorial of all the numbers between two entered numbers 
a = int(input("Enter first number : "))
b = int(input("Enter secound number : "))

print("Factorial ")
for i in range(a+1,b) :
  fact = 1
  for j in range(2,i+1) :
    fact = fact * j
  print(fact,end=" ")

