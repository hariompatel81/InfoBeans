# inplace row reaverse
l = [
     [4,3,2,1],
     [9,8,6,5],
     [8,7,6,2]
    ]

for i in range(len(l)) :
  f = 0
  last = len(l[i])-1
  while f < last :
    l[i][f], l[i][last] = l[i][last], l[i][f]
    f += 1
    last -= 1

for i in range(len(l)) :
  for j in range(len(l[i])) :
    print(l[i][j],end=" ")
  print()
