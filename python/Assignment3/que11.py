# 11. Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# And any other input of age should print "ERROR".  

age = int(input("Enter age :"))
gender = input("Enter gender (m/f) :")
marital_status = input("Enter marital status (y/n) :")

if gender == 'f' :
  print("She will work only in urban areas.")
elif gender == 'm' and (age > 20 and age < 40) :
  print("He may work in anywhere.")
elif gender == 'm' and (age > 40 and age < 60 ) :
  print("He will work in urban areas only.")
else :
  print("Error")