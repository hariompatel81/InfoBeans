# 12. Print all keys, all values, and all key-value pairs of a dictionary.

employee = {
  "name":"Hariom Patel",
  "age":22,
  "salary":50000
}

for key,value in employee.items():
  print(f"Key : {key}")
  print(f"value : {value}")
  print(f"key value pair : {key, value}")