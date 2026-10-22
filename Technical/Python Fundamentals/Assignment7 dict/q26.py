# 26. Find the second-largest distinct value in a dictionary.

d = {
  "one": 1,
  "two": 2,
  "three": 2,
  "four": 1,
  "five": 5,
  "six": 5
}

values = list(d.values())

values.sort(reverse=True)

max = values[0]
for i in values:
  if max > i:
    print("Secound distinct value in dictionary",i)
    break
else :
  print("Secound distinct value not exist")



  
