'''
2. Student Result Management System 
Beginner 
Concepts: Conditions, loops, functions 
Requirements 
Input marks for five subjects. 
Calculate total, percentage, and grade. 
Check whether the student passed or failed. 
Validate that each mark is between 0 and 100. 
Create functions such as calculate_total(), calculate_percentage(), and calculate_grade(). 
Bonus: Accept results for multiple students and calculate the class average.
'''

def calculate_total(l):
  total = 0
  for i in l:
    total += i
  return total

def calculate_percentage(total_marks):
  return total_marks/5

def calculate_grade(percent):
  if percent >= 75:
    return "A"
  elif percent >= 60 and percent < 75:
    return "B"
  elif percent >= 45 and percent < 60:
    return "C"
  elif percent >= 33 and percent < 45:
    return "D" 
  else :
    return "E"

i = 1
class_result = 0
while True:
  print(f"Enter 1 to store student subject marks :")
  print(f"Enter 2 to exit :")

  option = int(input("Select your option :"))
  if option == 2:
    break
  elif option == 1:
    print(f"\nEnter student {i} subjects marks :")
    marks = []
    for j in range(1,6):
      mark = int(input(f"Enter student {i} subject {j} mark :"))
      while True:
        if mark >= 0 and mark <= 100:
          marks.append(mark)
          break
        else :
          print("\nMarks must be between 0-100\n")
          mark = int(input(f"Enter student {i} subject {j} mark :"))

    print(f"Student {i} subjects Total marks : {calculate_total(marks)}")
    print(f"Student {i} percentage : {calculate_percentage(calculate_total(marks)):.2f}%")
    print(f"Student {i} grad : {calculate_grade(calculate_percentage(calculate_total(marks)))}")
    if calculate_grade(calculate_percentage(calculate_total(marks))) == "E":
      print(f"Student {i} : Fail")
    else :
      print(f"Student {i} : Pass")

    print()
    class_result += calculate_percentage(calculate_total(marks))
    i += 1

  else :
    print("\nInvalid Input.\n")

if i-1 > 1:
  print(f"\nClass average is : {class_result/(i-1) :.2f}%")