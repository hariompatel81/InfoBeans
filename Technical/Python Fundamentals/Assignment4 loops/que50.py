# WAP to find out all the perfect numbers between two entered numbers 

a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))

sum = 0
for i in range(a+1,b) :
  for j in range(1,(i//2)+1) :
    if i % j == 0 :
      sum += j

  if sum == i :
    print(f"{i} is perfect number.")
  else :
    print(f"{i} is not perfect number.")

  sum = 0

