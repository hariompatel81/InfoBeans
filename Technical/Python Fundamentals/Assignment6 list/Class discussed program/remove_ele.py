# remove element
l1 = [1,5,3,2,5]
pos = 0
val = 5
print("Before :",l1)
for i in range(len(l1)) :
  if l1[i] != val :
    l1[pos] = l1[i]
    pos += 1

print("After :",l1)