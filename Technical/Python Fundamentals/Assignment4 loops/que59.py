# WAP to convert decimal number into binary number without using array 

n = int(input("Enter a number :"))
x = n
count = 0
while x :
  rem = x % 2
  binary = 10**count + rem
  x //= 2
  count += 1

print(f"Binary of {n} is {binary}")

