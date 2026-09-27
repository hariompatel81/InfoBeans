
# 16. Write a Java program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.          Calculate percentage and grade according to following: 
# 	Percentage >= 90% : Grade A 
# 	Percentage >= 80% : Grade B 
# 	Percentage >= 70% : Grade C 
# 	Percentage >= 60% : Grade D 
# 	Percentage >= 40% : Grade E 
# 	Percentage < 40% : Grade F

physics_marks = int(input("Enter physics marks :"))
chemistry_marks = int(input("Enter chemistry marks :"))
biology_marks = int(input("Enter biology marks :"))
mathematics_marks = int(input("Enter mathematics marks :"))
computer_marks = int(input("Enter computer marks :"))

percentage = (physics_marks + chemistry_marks + biology_marks + mathematics_marks + computer_marks) / 5

if percentage >= 90 :
  print("A")
elif percentage >= 80 :
  print("B")
elif percentage >= 70 :
  print("C")
elif percentage >= 60 :
  print("D")
elif percentage >= 40 :
  print("E")
else :
  print("F")