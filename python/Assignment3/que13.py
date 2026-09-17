# 13. Write a  program that keeps a number from the user and generates an integer between 1 and 7 and displays the name of the weekday.
# Test Data
# Input number: 3
# Expected Output :
# Wednesday

number = int(input("Enter a number between 1-7 :"))
match number:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednusday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")