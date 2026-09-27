# 7. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# 8. Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

classes_held = int(input("Enter number of classes held :"))
classes_attended = int(input("Enter number of classes attended :"))
madical_cause = input("Are you have medical cause (y/n):")

class_attendence_percentage = (classes_attended / classes_held) * 100
print(f"Percentage of class attended : {class_attendence_percentage}")

if class_attendence_percentage < 75 :
  if madical_cause == "y" :
    print("Student is allow to sit in exam.")
  else : 
    print("Student is not allow to sit in exam.")
else :
  print("Student is allow to sit in exam.")