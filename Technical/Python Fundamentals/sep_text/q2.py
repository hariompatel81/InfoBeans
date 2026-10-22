'''
Q2. Simple Calculator — match-case

Write a Python program that accepts:

Two numbers
An operator (+, -, *, /, %)

Use match-case to perform the selected operation.

The program should also handle division by zero.

Example:

Enter first number: 20
Enter second number: 5
Enter operator: /

Result: 4.0

For an invalid operator:

Invalid operator
'''

first = int(input("Enter first number :"))
secound = int(input("Enter secound number :"))
operator = input("Enter operator :")

match operator :
  case "+" :
    print(f"Result : {float(first+secound)}")
  case "-" :
    print(f"Result : {float(first-secound)}")
  case "*" :
    print(f"Result : {float(first*secound)}")
  case "/" :
    print(f"Result : {float(first/secound)}")
  case "%" :
    print(f"Result : {float(first%secound)}")
  case _ :
    print(f"Invalid operator")