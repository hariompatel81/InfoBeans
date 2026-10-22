# 18. Find the first repeating character.
# Example: "programming" → r

s = "programming"
if s:
  d = {}
  for ele in s:
    d[ele] = d.get(ele,0)+1

    if d[ele] > 1:
      print(f"First repeating element is -->{ele}")
      break
  else :
    print(f"string contains all the unique values...")
else :
  print("String is empty...")
