# 6) WAP to find out the factors of a number.

number = int(input("Enter a number :"))

print(f"Factors of a {number} is :")
# a number divided by < n/2 only
for i in range(1,(number//2)+1) :
  if number % i == 0 :
    print(i,end=" ")

print(number)