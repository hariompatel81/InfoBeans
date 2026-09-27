# W.A.P to check armstrong number

number = int(input("Enter a number :"))

# calculate number digit length
temp = number
length = 0
while number != 0 :
  length += 1
  number //= 10

# check perfect
armstrong = 0
number = temp
while(temp != 0) :
  remainder = temp % 10
  armstrong += remainder**length
  temp //= 10

if armstrong == number :
  print(f"{number} is armstrong number.")
else :
  print(f"{number} is not armstrong number.") 
