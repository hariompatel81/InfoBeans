# 18. Find the first non-repeating character in a string using a dictionary.

d = {}
s = "Hariom patel is good boy"
s1 = s.lower()
for ch in s1:
  d[ch] = d.get(ch,0) + 1

for key,value in d.items() :
  if value == 1 :
    print(f"First non-repeating chatecter is {key}.")
    break
else :
  print("There is no any repeating element...")



