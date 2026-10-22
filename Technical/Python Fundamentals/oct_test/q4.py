'''
Q4. Sets — Common and Unique Elements (5 Marks)

Given two lists, find:

Elements common to both lists.

Elements that appear in either list but not in both.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

Expected output:

Common elements: {30, 40}
Unique elements: {10, 20, 50, 60, 70}
'''

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

common = set()
unique = set()

i = 0
j = 0
while i < len(list1) and j < len(list2):
  if list1[i] ==  list2[j] :
    if list1[i] not in unique:
      common.add(list1[i])
      unique.add(list1[i])
      i += 1
      j += 1

  elif list1[i] < list2[j]:
    if list1[i] not in unique:
      unique.add(list1[i])
      i += 1

  else :
    if list2[j] not in unique:
      unique.add(list2[j])
      j += 1

while i < len(list1):
  if list1[i] not in unique:
    unique.add(list1[i])
    i += 1

while j < len(list2):
  if list2[j] not in unique:
    unique.add(list2[j])
    j += 1

print(f"Common : {common}")
print(f"Unique : {unique}")
