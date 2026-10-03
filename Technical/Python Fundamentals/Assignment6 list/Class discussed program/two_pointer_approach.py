# add two non-decreasing list in non-decreasing order
# l1 = [2,3,3,4,5]
# l2 = [1,3,4,4,6,7,8]
# result = [1,2,3,3,3,4,4,4,5,6,7,8]

l1 = [2,3,3,4,5]
l2 = [1,3,4,4,6,7,8]
result = []
i = 0
j = 0

while i < len(l1) and j < len(l2) :
  if l1[i] < l2[j] :
    result.append(l1[i])
    i += 1
  else :
    result.append(l2[j])
    j += 1

while i < len(l1) :
  result.append(l1[i])
  i += 1
while j < len(l2) :
  result.append(l2[j])
  j += 1

print(l1)
print(l2)
print("Result :",result)
