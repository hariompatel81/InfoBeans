# strong number

number = int(input("Enter a number :"))

fact = 1
def factorial(n):
  for i in range(2,n+1):
    fact *= i
    return fact

strong = 0
remainder = 0
while(number != 0):
  remainder = number % 10
  strong += factorial(remainder) 
  number //= 10

print(f"Strong number is : {strong}")


