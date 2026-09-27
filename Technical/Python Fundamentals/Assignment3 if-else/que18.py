# 18. Write a Python program to input electricity unit charges and calculate total electricity bill according to the given condition: For first 50 units Rs. 0.50/unit For next 100 units Rs. 0.75/unit For next 100 units Rs. 1.20/unit For unit above 250 Rs. 1.50/unit An additional surcharge of 20% is added to the bill. 

electricity_unit = int(input("Enter electricity unit :"))
if electricity_unit <= 50 :
  bill = electricity_unit*0.50
elif electricity_unit <= 150 :
  bill = 50*0.50 + ((electricity_unit-50)*0.75)
elif electricity_unit <= 250 :
  bill = 50*0.50 + 100*0.75 + ((electricity_unit-150)*1.20)
else :
  bill = 50*0.50 + 100*0.75 + 100*1.20 +((electricity_unit-250)*1.50)

bill = bill + 0.20*bill
print(f"electricity bill is :{bill:.2f}")


##brute force approach
# electricity_unit = int(input("Enter number of units to be consumed:"))
# electricity_bill = 0

# if electricity_unit <= 50 :
#   electricity_bill = electricity_unit * 0.50

# else :
#   if electricity_unit > 50 :
#     electricity_unit = electricity_unit - 50
#     electricity_bill = electricity_bill + (0.50*50)
#   if electricity_unit > 0 :
#     if electricity_unit > 100 :
#       electricity_unit = electricity_unit - 100
#       electricity_bill = electricity_bill + (0.75*100)
#     else :
#       electricity_bill = electricity_bill + (0.75*electricity_unit)
#       electricity_unit = 0
#   if electricity_unit > 0 :
#     if electricity_unit > 100 :
#       electricity_unit = electricity_unit - 100
#       electricity_bill = electricity_bill + (1.20*100)
#     else :
#       electricity_bill = electricity_bill + (1.20*electricity_unit)
#       electricity_unit = 0
#   if electricity_unit > 0 :
#     electricity_bill = electricity_bill + (1.50*electricity_unit)

# # 20% additional surcharge 
# electricity_bill = electricity_bill + (0.20*electricity_bill)

# print(f"Your total eletricity charge is: {electricity_bill}")
      
#better aproach
# units = int(input("Enter number of units: "))

# if units <= 50:
#     bill = units * 0.50

# elif units <= 150:
#     bill = (50 * 0.50) + ((units - 50) * 0.75)

# elif units <= 250:
#     bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)

# else:
#     bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

# # 20% surcharge
# bill = bill + (bill * 0.20)

# print(f"Your total electricity charge is: ₹{bill:.2f}")


