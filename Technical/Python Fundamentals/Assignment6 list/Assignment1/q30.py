'''
30. Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. The numbers in array A appear in ascending order while the numbers in array B appear in descending order. Write a java progtam to produce third array C by merging arrays A and B in ascending order. . 
'''

A = [1,2,3,3,4,5,6]
B = [7,6,6,5,4,3,2,1]
C = []
M = len(A)
N = len(B)

i = 0
j = N-1
while i < M and j < N:
  if A[i] == B[j] :
    C.append(A[i])
    C.append(B[j])
    i += 1
    j -= 1
  elif A[i] < B[j] :
    C.append(A[i])
    i += 1
  else :
    C.append(B[j])
    j -= 1

while i < M :
  C.append(A[i])
  i += 1

while j > -1 :
  C.append(B[j])
  j -= 1

print(A)
print(B)
print(C)
   




