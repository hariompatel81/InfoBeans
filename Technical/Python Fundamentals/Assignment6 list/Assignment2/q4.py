# print element of maximum sub array
l = [
     [1,2,3,4],
     [5,6,8,9],
     [2,6,7,8]
    ]

max = float('-inf')
ind = -1
for i in range(len(l)) :
  sum = 0
  for j in range(len(l[i])) :
    sum += l[i][j]
  if max < sum :
    max = sum
    ind = i

for i in range(len(l[ind])) :
  print(l[ind][i],end=" ")
print(" ===> ",max)
  
  
    