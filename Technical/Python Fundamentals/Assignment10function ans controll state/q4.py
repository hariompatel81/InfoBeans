'''
4. Restaurant Billing System 
Beginner–Intermediate 
Concepts: Loops, conditions, functions 
Requirements 
Display a menu with item prices. 
Let customers select items and quantities. 
Calculate the running bill. 
Apply discounts based on the bill amount. 
Calculate the final bill, including tax. 
Bonus: Add coupon codes and repeat-order functionality.
'''
def add_to_card():
  pass

def display_manu():
  print()
  print("--------Manu--------")
  print("Item 1 Tomato Soup : 100")
  print("Item 2 Sweet Corn Soup : 120")
  print("Item 3 Paneer Tikka : 250")
  print("Item 4 Jeera Rice : 100")
  print("Item 5 Chilli Paneer : 230")
  print()

def select_item():
  pass

def calculate_bill(order):
  d = 

def add_coupon():
  pass

def take_order():
  while True:
    order = int(input("Enter item number :"))
    if order < 1 or order > 5 or order == "":
      print("\nInvalid input...\n")
    else :
      break

  while True:
    quantity = int(input("Enter Quantity :"))
    if quantity < 1:
      print("\nInvalide input...\n")
    else :
      break

  return order, quantity

add_order = {}

print("------ Welcome to our restourant ------")
display_manu()

print("What whoud you like to order :")
order, quantity = take_order()
add_order[order] = quantity

while True:
  ans = input("Do you want to add more item (y/n):")
  if ans == "y":
    order, quantity = take_order()
    if order in add_order:
      add_order[order] += quantity
    else :
      add_order[order] = quantity
  else :
    calculate_bill(add_order)
  
   






else :
  quantity = int(input(f"Enter quantity of item {item} : "))
  add_to_card[item] = quantity
  print(add_to_card) 
    

