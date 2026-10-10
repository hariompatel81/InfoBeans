# 36. Write a java program to implement bubble sort algorithm

l = [3,4,567,4,6,4,2,4]
for i in range(len(l)) :
  isSwap = False
  for j in range(len(l)-i-1) :
    if l[j] > l[j+1] :
      l[j+1],l[j] = l[j],l[j+1]
      isSwap = True

  if not isSwap :
    break

print(l)

