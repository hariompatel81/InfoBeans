# Write a program to cyclically rotate array by one.

l = [10,20,30,40,50]
print("List :",l)
if len(l) :
  temp = l[len(l)-1]

  for i in range(len(l)-1,0,-1) :
    l[i] = l[i-1]

  l[0] = temp

print(f"List after one rotation ",l)

# rotate by k

l = [10,20,30,40,50]
k = int(input("Enter k :"))
for i in range(k) :
  if len(l) :
    temp = l[len(l)-1]
    for i in range(len(l)-1,0,-1) :
      l[i] = l[i-1]

    l[0] = temp

print(f"List after {k} rotation :",l)


