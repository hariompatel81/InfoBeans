# Q.2 Find minimum and maximum element in array

l = [45,4,5,3,5,3,55,4,6,5,4]

min = float('inf')
max = float('-inf')
for i in range(len(l)) :
  if l[i] > max :
    max = l[i]
  elif l[i] < min :
    min = l[i]

print(f"Min : {min}")
print(f"Max : {max}")
    

  

