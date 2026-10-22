# 14. Copy a dictionary into another dictionary. Explain whether changing a nested object in the copy can affect the original.

import copy

d1 = {"name":"Hariom Patel"}
d2 = d1.copy()

print(d1)
print(d2)

d1["name"] = "Sujal"
print(d1)
print(d2)

d2.update(age=22)
print(d1)
print(d2)

d1 = {
  "name":"Hariom Patel",
  "address":{
    "housh no":123,
    "state":"MP"
  }
}

d2 = copy.deepcopy(d1)
print(d1)
print(d2)

d2["address"]["housh no"] = 170

print(d1)
print(d2)
print("Yes, changing changing a nested object in the copy can affect the orignal....")
