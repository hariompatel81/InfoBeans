# 7) WAP to check whether entered number is prime or not.

# my logic
number = int(input("Enter a number :"))

i = 2
if number < 2 :
  print(f"{number} is not prime.")
else :
  for i in range(2,(number // 2)+1) :
    if number % i == 0 :
      break

  if i > (number//2) :
    print(f"{number} is prime.")
  else :
    print(f"{number} is not prime.")


## using while loop

# number = int(input("Enter a number :"))
# i = 2

# while i <= (number//2) :
#   if number % i == 0 :
#     break
#   i += 1

# if (i > (number//2)) and (number > 1) :
#   print(f"{number} is prime.")
# else :
#   print(f"{number} is not prime.")
