# find min and max element from list
l1 = [12,3,4,34,5,34,4,5,3,5,3,45,3,43]
min = l1[0]
max = l1[0]

for i in l1 :
  if i > max :
    max = i
  elif i < min :
    min = i

print("Min : ",min)
print("Max : ",max)