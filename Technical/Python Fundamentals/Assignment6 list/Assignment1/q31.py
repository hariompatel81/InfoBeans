'''
31. Suppose X. Y, Z are arrays of integers of size M, N, and M + N respectively. The numbers in array X and Y appear in descending order. Write a java program to produce third array Z by merging arrays X and Y in descending order. 
'''
X = [9,8,7,6,5,4,3,2]
Y = [8,7,6,5,4,3,2,1]
C = []
i = 0
j = 0

while i < len(X) and j < len(Y) :
  if X[i] == Y[j] :
    C.append(X[i])
    C.append(Y[j])
    i += 1
    j += 1

  elif X[i] > Y[j] :
    C.append(X[i])
    i += 1

  else :
    C.append(Y[j])
    j += 1

while i < len(X) :
  C.append(X[i])
  i+=1

while j < len(Y) :
  C.append(Y[j])
  j +=1

print(C)
