# 4. Add a new key-value pair named "city" to an existing dictionary.

employee = {"name":"Hariom Patel", "age":22, "salary":6000}

# first way
# employee["city"] = "Indore"

# secound way
employee.update(city="Indore")

#third way
employee |= {"city":"Indore"}
print(employee)

