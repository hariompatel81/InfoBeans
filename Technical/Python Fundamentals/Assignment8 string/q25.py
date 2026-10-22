# 25. Check whether a string contains only digits without using isdigit().

s = "111111111111"
l = list(s)
for i in l:
   if not (ord(i) >= 48 and ord(i) <= 57):
    print("No string not contain only digit...")
    break
else :
  print("Yes string contain only digits...")
      