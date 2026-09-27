# check number is strong number or not

number = int(input("Enter a number :"))

temp = number 
strong = 0
fact = 1
while(number != 0):
  remainder = number % 10
 
  while remainder > 1 :
    fact *= remainder
    remainder -= 1

  number //= 10
  strong += fact
  fact = 1

if strong == temp :
  print(f"{temp} is strong number.")
else :
  print(f"{temp} is not strong number.")



