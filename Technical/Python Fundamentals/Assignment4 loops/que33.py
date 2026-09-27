# check perfect number

number = int(input("Enter a number :"))

i = 1
sum = 0
while(i <= number//2) :
  if number % i == 0 :
    sum += i
  i += 1

if number == sum :
  print(f"{number} is perfect number.")
else :
  print(f"{number} is not a prime number.")