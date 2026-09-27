# WAP to reverse a number
n = int(input("Enter a number :"))
x = n
rev = 0
while n :
  r = n%10
  rev = rev*10 + r
  n //= 10

print(f"Reverce of a number is {rev}")
