# 12.A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895 

number = int(input("Enter a number :"))

reverce = 0
while(number != 0):
  remender = number % 10
  reverce = reverce*10 + remender
  number = number // 10

print(f"reverce : {reverce}")


