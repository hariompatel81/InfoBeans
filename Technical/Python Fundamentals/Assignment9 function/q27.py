# 27. Find all duplicate characters and their frequencies.

def find_duplicates(s):
  d = {}
  d1 = {}
  for ele in s:
    d[ele] = d.get(ele, 0)+1

  for key,value in d.items():
    if value > 1:
      d1[key] = value

  return d1

s = input("Enter string :")
print(find_duplicates(s))

