# 30. Safely retrieve a value from a deeply nested dictionary. If any key is missing, return a default value such as "Unknown".

students = {
  "s1" : {
    "name": "hariom patel",
    "age":22,
    "address":{
      "housh no": 170,
      "street": "raj mohalla",
      "city": "indore"
    }
  },
  "s2" : {
    "name": "hariom patel",
    "age":22,
    "address":{
      "housh no": 170,
      "street": "raj mohalla",
      "city": "indore"
    }
  },
  "s3" : {
    "name": "hariom patel",
    "age":22,
    "address":{
      "housh no": 170,
      "street": "raj mohalla",
      "city": "indore"
    }
  }
}

print(students.get("s1","Unknown"))
print(students.get("s1").get("name","Unknown"))
print(students.get("s1").get("address").get("houshno","Unknown"))
  
