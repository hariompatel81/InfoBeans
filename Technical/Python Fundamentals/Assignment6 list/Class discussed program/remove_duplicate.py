# remove duplicate element from given array
l1 = [0,0,1,1,1,2,2,3,3,4]
i = 0
j = 1
print(f"Before : {l1}")
for i in range(0,len(l1)-1) :
  if l1[i] != l1[i+1] :
    l1[j] = l1[i+1]
    j += 1

print(f"After : {l1}")
