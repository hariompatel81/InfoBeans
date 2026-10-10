# matrix multiplication
l1 = [[1,2,3],[4,5,6],[2,2,4]]
l2 = [[1,2,1],[3,4,1],[5,6,1]]

if len(l1[0]) == len(l2) :
  krange = max(len(l1),len(l2[0]))
  mul = [[0]*len(l2[0]) for _ in range(len(l1))] 
  print(mul)
  for i in range(len(l1)) :
    for j in range(len(l2[0])) :
      sum = 0
      for k in range(krange) :
        sum += l1[i][k] * l2[k][j]
      mul[i][j] = sum
      print(sum,end=" ")
    print() 
else :
  print("Matrix multiplication is not possible for this input...")



