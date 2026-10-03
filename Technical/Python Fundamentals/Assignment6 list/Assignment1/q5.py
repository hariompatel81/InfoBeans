# Q.5 Find the kth largest and kth smallest element in array.

k = int(input("Enter k:"))
l = [42,5,3,5,3,6]
for i in range(len(l)-1) :
  for j in range(i+1,len(l)) :
    if l[i] > l[j] :
      l[i],l[j] = l[j],l[i]

print("sorted list :",l)
print("kth largest element :",l[len(l)-k+1])
print("kth smalest element :",l[k-1])