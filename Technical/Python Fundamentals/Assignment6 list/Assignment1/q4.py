# Q.4 Write a program to sort the array

l = [43,5,3,5,3,6,3,6,3,47,4,6,4,76,46]
print("Before sort :",l)
for i in range(len(l)-1) :
  for j in range(i+1, len(l)) :
    if l[i] > l[j] :
      l[i],l[j] = l[j],l[i]

print("After sort :",l)