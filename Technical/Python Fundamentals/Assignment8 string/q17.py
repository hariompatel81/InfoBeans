# 17. Find the first non-repeating character in a string.
# Example: "aabbcddee" → c

s = "aabbcddee"
d = {}

for ele in s:
  d[ele] = d.get(ele,0)+1

for key in d:
  if d[key] == 1 :
    print(f"First non-repeating element is {key}")
    break
else :
   print(f"There is no non-repeating element present in this string...")
