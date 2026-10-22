# 14. Remove all digits from a string.

s = "My name is hariom343 patelrer em54y 464c4o5n5t5e5c4t3 356number is 8103401624"
print("Before remove digits...")
print(s)
l = list(s)
l1 = []

for ele in l:
  if ord(ele) >= 48 and ord(ele) <= 57 :
    continue
  else :
    l1.append(ele)

s = "".join(l1)
print("after removing digits...")
print(s)
