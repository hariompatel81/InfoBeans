# 3.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter salary :"))
year_of_service = int(input("Enter year of service :"))
net_bonus = 0

if year_of_service > 5:
  net_bonus = salary * 0.05

print(f"The net bonus amount is : {net_bonus}")
