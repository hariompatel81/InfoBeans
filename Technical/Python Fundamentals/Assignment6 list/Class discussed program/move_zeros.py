# move zeros
l1 = [0,1,0,3,12]
pos = 0
val = 0

print("Before :",l1)
for i in range(len(l1)) :
  if l1[i] != val :
    l1[pos] = l1[i]
    pos += 1

print("After :",l1)

