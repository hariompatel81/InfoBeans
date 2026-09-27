# sum of digit of a number

number = int(input("Enter a number :"))
sum = 0

while (number != 0 ):
  remainder = number % 10
  sum += remainder
  number //= 10

print(f"Sum of digit of a number is : {sum}")