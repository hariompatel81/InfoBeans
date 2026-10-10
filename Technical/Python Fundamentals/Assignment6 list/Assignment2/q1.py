# lower tringle
l = [
     [1,2,3],
     [4,5,6],
     [7,8,9]
    ]

for i in range(len(l)) :
  for j in range(len(l[i])) :
    if i > j :
      print(l[i][j],end=" ")
    else :
      print(0,end=" ")
  print()

