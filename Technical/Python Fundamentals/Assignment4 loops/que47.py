# WAP to find out the sum of first and last digit of a user entered number  

n = int(input("Enter a number :"))
count = 0
x = n
while x > 0 :
  count += 1
  x //= 10

x = n
for i in range(1,count+1) :
  if i == 1 :
    last_digit = x % 10
  elif i == count :
    first_digit = x % 10
  x //= 10

print(f"Sum of first and last digit of a {n} is {first_digit+last_digit}")
