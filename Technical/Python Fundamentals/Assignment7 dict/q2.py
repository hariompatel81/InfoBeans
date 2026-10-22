# 2. Given a dictionary of student details, print each key and value on a separate line.
l = [("name","Hariom Patel"),("age",22),("marks",70)]
student = dict(l)
for key,value in student.items() :
  print(key,value)

# for key in student:
#   print(key, student[key])