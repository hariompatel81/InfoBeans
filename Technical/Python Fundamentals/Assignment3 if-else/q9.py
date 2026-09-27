# 9. Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).

char = input("Enter a chatecter :")
if char >= "a" and char <= "z" :
  print("Charecter is lowercase.")
elif char >= "A" and char <= "Z" :
  print("Charecter is uppercase.")
else :
  print("invalid charecter")