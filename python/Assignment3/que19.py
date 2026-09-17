# 19. Write a program to input choice from user. If user enter ‘+’ as choice then calculate addition of 2 number. If Choice ‘>’ then check which number is greaterst. If choice is ‘==’ then check both number is equal or not.

first_num = int(input("Enter first number :"))
sec_num = int(input("Enter secound number :"))
choice = input("Enter your choice from (+,>,==) :")

if choice == "==":
  print("Both number is equal.") if first_num == sec_num else print("Both number is not equal.")  
elif choice == ">" :
  print(f"{first_num} is greatest.") if first_num > sec_num else print(f"{sec_num} is greatest.")
else :
  print(f"Addittion is : {first_num + sec_num}")
