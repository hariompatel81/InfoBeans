# 5) WAP to find out the factorial of a number.

number = int(input("Enter a number :"))

fact = 1
for i in range(2,number+1) :
  fact *= i

print(f"factorial of {number} is : {fact}")