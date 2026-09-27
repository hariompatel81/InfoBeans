# 2.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input("Enter quantity :"))
total_bill = quantity * 100
if quantity > 1000:
  total_bill = total_bill - (total_bill * 0.10)

print(f"Total cost for user : {total_bill}")