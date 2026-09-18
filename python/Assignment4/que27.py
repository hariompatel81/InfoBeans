# W.A.P x**y in loop

base = int(input("Enter base :"))
power = int(input("Enter power :"))
result = 1

for i in range(power):
  result *= base

print(f"Result : {result}")