# move 0,1,2
l1 = [0,0,1,2,2,1,2,1,2,2,0,1,2,0,1]
zc = 0
oc = 0
tc = 0

print("Before :",l1)
for ele in l1 :
  if ele == 0 :
    zc += 1
  elif ele == 1 :
    oc += 1
  else :
    tc += 1

for i in range(zc) :
  l1[i] = 0
for i in range(zc,zc+oc) :
  l1[i] = 1
for i in range(zc+oc,zc+oc+tc) :
  l1[i] = 2

print("After :",l1) 

## by using two pointer approach
l2 = [0,1,1,2,0,2,0,1]
low = 0
mid = 0
high = len(l2)-1

print("Before :",l2)
while mid <= high :
  if l2[mid] == 0 :
    l2[low],l2[mid] = l2[mid],l2[low]
    mid += 1
    low += 1
  elif l2[mid] == 1 :
    mid += 1
  else :
    l2[mid],l2[high] = l2[high],l2[mid]
    high -= 1    

print("After :",l2)