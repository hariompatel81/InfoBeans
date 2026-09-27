# WAP to convert binary number into decimal number 

n = int(input("Enter a number :"))
rev = 0
binary = 0
x = n
while n :
  rem = n % 2
  rev = 10*rev + rem
  n //= 2

while rev :
  rem = rev % 10
  binary = 10*binary + rem
  rev //= 10

print(f"Binary of {x} is {binary}")

