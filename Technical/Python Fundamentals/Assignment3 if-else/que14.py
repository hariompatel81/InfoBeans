# 14.Write a program to accept percantage from the user and
# display grade according to the following criteria
#   Marks	  		Grade
#   > 90       		 A
#   >80 and <=90		 B
#   >=60 and <=80		 C
#   below 60		 D

percentage = int(input("Enter percentage :"))

if percentage > 90 :
  print("A")
elif percentage <= 90 and percentage > 80 :
  print("B")
elif percentage <= 80 and percentage >= 60 :
  print("C")
else :
  print("D")