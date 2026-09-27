# 17. Write a Python program to input basic salary of an employee and calculate its Gross salary according to following: Basic Salary <= 10000 : HRA = 20%, DA = 80% 
# Basic Salary <= 20000 : HRA = 25%, DA = 90% 
# Basic Salary > 20000 : HRA = 30%, DA = 95% 

salary = int(input("Enter basic salary :"))
gross_salary = 0

if salary <= 10000 :
  gross_salary = salary + (0.20*salary) + (0.80*salary)
elif salary <= 20000 :
  gross_salary = salary + (0.25*salary) + (0.90*salary)
else :
  gross_salary = salary + (0.30*salary) + (0.95*salary)