# WAP to find out all the leap years between two entered years 

a = int(input("Enter first year :"))
b = int(input("Enter secound year :"))

for i in range(a+1,b) :
  if (i % 100 == 0 and i % 400 == 0) or (i % 100 != 0 and i % 4 == 0) :
    print(f"{i} is leap year.")
