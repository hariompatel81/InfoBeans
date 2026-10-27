'''
1. Smart Calculator 
Beginner 
Concepts: if-elif-else, while, functions 
Requirements 
Display a menu for addition, subtraction, multiplication, division, and modulus. 
Take two numbers from the user. 
Use separate functions for each operation. 
Handle division by zero. 
Repeat until the user selects Exit. 
Bonus: Add power and floor division operations. 
'''

def decorator(ref):
  def wrapper(a,b):
    if b == 0:
      print("Divisor must be non-zero...")
    else :
      return ref(a,b)
  return wrapper

def addition(a,b):
  return a+b

def substraction(a,b):
  return a-b

def multiplication(a,b):
  return a*b

@decorator
def division(a,b):
  return a/b

def modulus(a,b):
  return a%b

@decorator
def floor_division(a,b):
  return a//b

def power(a,b):
  return a**b

while True:
  print()
  print("Enter 1 for 'Addition' operation :")
  print("Enter 2 for 'Substraction' operation :")
  print("Enter 3 for 'Multiplication' operation :")
  print("Enter 4 for 'Division' operation :")
  print("Enter 5 for 'Modulus' operation :")
  print("Enter 6 for 'Floor Division' operation :")
  print("Enter 7 for 'Power' operation :")
  print("Enter 8 for 'Exit' :")
  print()

  number = int(input("Select Option : "))
  if number == 8:
    break

  elif number < 1 or number > 8:
    print("\nInvalid Input...")

  else :
    print()
    a = int(input("Enter first number."))
    b = int(input("Enter secound number."))
    if number == 1:
      print(f"Addition is : {addition(a,b)}")
    elif number == 2:
      print(f"Substraction is : {substraction(a,b)}")
    elif number == 3:
      print(f"Multiplication is : {multiplication(a,b)}")
    elif number == 4:
      print(f"Division is : {division(a,b)}")
    elif number == 5:
      print(f"Modulus is : {modulus(a,b)}")
    elif number == 6:
      print(f"Floor Division is : {floor_division(a,b)}")
    else :
      print(f"{a} to the power {b} is : {power(a,b)}")



  
