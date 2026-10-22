# 3. Check whether the key "age" exists in a dictionary.

# employee = {
#   "name":"Hariom Patel",
#   "expiriance":10,
#   "salary":50000
# }

employee = {
  "name":"Hariom Patel",
  "age":10,
  "salary":50000
}

if "age" in employee:
  print("Age exist")
else :
  print("Age not exist") 

# another way or without a membership operation
keys = employee.keys()
for i in keys:
  if i == "age" :
    print("Age exist")
    break
else :
  print("Age not exist")