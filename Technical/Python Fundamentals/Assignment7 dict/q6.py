# 6. Remove a key from a dictionary using pop(). Handle the case where the key does not exist.

student = {"name":"Hariom Patel"}
key = "age"

if key in student:
  print(student.pop(key))
else :
  print("key not exist...")

# # another way
# keys = student.keys()
# if key in keys :
#   print(student.pop(key))
# else :
#   print("Key not exist...")