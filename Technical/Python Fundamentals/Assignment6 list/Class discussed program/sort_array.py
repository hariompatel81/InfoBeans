# sort array
print("Before :")
l = [2,4,2,3,3,5,3,6,3,56,2,6,3]
for i in range(len(l)-1) :
  for j in range(i+1,len(l)) :
    if l[i] > l[j] :
      l[i],l[j] = l[j],l[i]

print("After :",l)
