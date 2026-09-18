# armstrong number

number = int(input("Enter a number :"))

armstrong = 0
temp = number
while(temp != 0) :
  remainder = temp % 10
  armstrong += remainder**3
  temp //= 10

if armstrong == number :
  print(f"{number} is armstrong number.")
else :
  print(f"{number} is not armstrong number.") 
