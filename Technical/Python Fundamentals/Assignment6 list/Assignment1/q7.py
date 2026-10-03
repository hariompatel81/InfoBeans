# Q.6 Sort the array of 0s , 1s and 2s.

l = [0,1,1,2,1,2,1,2,1,2,1,2,0,0,0,2]
zc = 0
oc = 0
tc = 0
for i in range(len(l)) :
  if l[i] == 0 :
    zc += 1
  elif l[i] == 1 :
    oc += 1 
  else :
    tc += 1

for i in range(zc) :
  l[i] = 0
for j in range(zc,zc+oc) :
  l[j] = 1
for k in range(zc+oc,zc+oc+tc) :
  l[k] = 2

print(l)


# another solution
l1 = [1,0,1,2,1,2,0,0,1,2,0,1]
left = 0
mid = 0
right = len(l1)-1
print("list : ",l1)
while mid <= right :
  if l1[mid] == 0 :
    l1[left],l1[mid]=l1[mid],l1[left]
    left += 1
    mid += 1
  elif l1[mid] == 1 :
    mid += 1
  else:
    l1[mid],l1[right] = l1[right],l1[mid]
    right -= 1

print("After shifting 0`s,1`s,2`s : ",l)