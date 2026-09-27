#  3) WAP to find out the sum of N natural number.

number = int(input("Enter natural number: "))

sum = 0
for i in range(1,number+1) :
  sum += i

print(f"Sum of natural number : {sum}")