# matrix transpose

l = [
      [1,2,3],
      [4,5,6]
    ]
# result = [[0]*len(l)]*len(l[0])
result = [[0]*len(l) for _ in range(len(l[0]))]
print(result)
for i in range(len(result)) :
  for j in range(len(result[i])) :
    result[i][j] = l[j][i]
    print(result[i][j],end=" ")
  print()

print(result)