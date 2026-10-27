'''
3. ATM Banking Simulator 
Beginner–Intermediate 
Concepts: Nested conditions, loops, functions 
Requirements 
Verify a PIN. 
Display balance, deposit, withdrawal, and exit options. 
Prevent withdrawals exceeding the available balance. 
Reject invalid amounts. 
Use separate functions for deposit, withdrawal, and balance enquiry. 
Bonus: Allow only three PIN attempts. 
'''
def check_pin(pin):
  if pin == security_pin:
    return True
  else :
    return False

def deposit(amount):
  global balance
  balance += amount

def balance_enquiry():
  print(f"Balance is : {balance} \n")

def withdrawal(amount):
  global balance
  if balance < amount :
    print("Insufician balance")
    return False
  else :
    balance -= amount
    print("Withdraw Successfully")
    return True

security_pin = "1234"
balance = 10000.00
while True:
  print("Enter 1 for display balance :")
  print("Enter 2 for deposit :")
  print("Enter 3 for withdrawal :")
  print("Enter 4 for exit :")
  print()

  option = int(input("Select option :"))
  if option == 4:
    break
  elif option < 1 and option > 3:
    print("\nInvalid input...\n")
  else :
    if option == 1:
      i = 0
      while i < 3:
        pin = input("Enter PIN :")
        if check_pin(pin):
          balance_enquiry()
          break
        else :
          print("\nInvalid PIN...\n")
          i += 1

    elif option == 2:
      i = 0
      while i < 3:
        pin = input("Enter PIN :")
        if check_pin(pin):
          while True:
            amount = float(input("Enter amount : "))
            if amount < 0:
              print("\nInvalide amount...\n")
            else :
              deposit(amount)
              break
          break
        else :
          print("\nInvalid PIN...\n")
          i += 1

    else :
      amount = float(input("Enter amount :"))
      i = 0
      while i < 3:
        pin = input("Enter pin :")
        if check_pin(pin):
          withdrawal(amount)
          break
        else :
          print("Invalid pin")
          i += 1


      
      

