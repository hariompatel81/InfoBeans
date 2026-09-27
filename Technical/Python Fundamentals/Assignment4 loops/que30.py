# count digit of a number

number = int(input("Enter a number :"))

count = 0
while(number != 0):
  remainder = number % 10
  count += 1
  number //= 10

print(f"Number of digit in a number : {count}")