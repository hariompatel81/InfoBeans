# WAP to find out all the Armstrong numbers between two entered numbers 

a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))

for i in range(a+1,b) :
  sum = 0
  count = 0
  x = i
  while x :
    count += 1
    x //= 10

  x = i
  while x :
    rem = x % 10
    sum += rem**count
    x //= 10

  if sum == i :
    print(f"{i} is a armstrong number.")

