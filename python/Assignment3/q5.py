# 5.Take input of age of 3 people by user and determine oldest and youngest among them.

person1_age = input("Enter person1 age :")
person2_age = input("Enter person2 age :")
person3_age = input("Enter person3 age :")

if person1_age > person2_age and person1_age > person3_age :
  print("person1 is oldest")
  if person2_age > person3_age :
    print("person3 is youngest")
  else:
    print("person2 is youngest")
elif person2_age > person3_age  and person2_age > person1_age :
  print("person2 is oldest")
  if person3_age > person1_age :
    print("person1 is youngest")
  else:
    print("person3 is youngest")
else:
  print("person3 is oldest")
  if person1_age > person2_age :
    print("person2 is youngest")
  else:
    print("person1 is youngest")

  