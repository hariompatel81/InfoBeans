# fine sum and swap min_sum with max_sum

l = [
     [1,2,3,4],
     [5,6,8,9],
     [2,6,7,8]
    ]
min = float('inf')
max = float('-inf')
minI = -1
maxI = -1
for i in range(len(l)) :
  sum = 0
  for j in range(len(l[i])) :
    sum += l[i][j]
  if sum > max :
    max = sum
    maxI = i
  if sum < min :
    min = sum
    minI = i

l[minI], l[maxI] = l[maxI], l[minI]
for i in range(len(l)) :
  for j in range(len(l[i])) :
    print(l[i][j],end=" ")
  print()

  

  

    
