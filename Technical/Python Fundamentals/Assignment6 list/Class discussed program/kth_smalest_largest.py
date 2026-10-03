# Kth smalest and largest
l = [1,3,5,2,5,3,6,3,6,23,3,7,3,6,3,7,36,]
k = int(input("give value of k :"))

for i in range(len(l)-1) :
  for j in range(i+1,len(l)) :
    if l[i] > l[j] :
      l[i],l[j] = l[j],l[i]

print(l)
print("Kth smallest : ",l[k-1])
print("Kth largest : ",l[len(l)-k]) 