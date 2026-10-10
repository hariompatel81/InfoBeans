# 37. Write a java progrtam to implement insertion sort algorithm

l = [3,4,6,3,6,3,6,7,8,5,75]
for i in range(1,len(l)) :
  key = l[i]
  j = i-1
  while j >= 0 and l[j] > key :
    l[j+1] = l[j]
    j -= 1
  l[j+1] = key

print(l)
  


