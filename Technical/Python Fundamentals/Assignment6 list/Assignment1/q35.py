# 35. Write a java program to implement selection sort algoritm

l = [2,5,3,6,4,8,5,3,23,5,76,8,5,3]
for i in range(len(l)-1) :
  min = l[i]
  ind = i
  for j in range(i+1,len(l)) :
    if min > l[j] :
      min = l[j]
      ind = j

  l[i],l[ind] = l[ind],l[i]

print(l)

