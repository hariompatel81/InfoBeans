# 19. Find all duplicate elements in a list and their frequencies.

l = [1,3,5,3,5,7,7,5,6,8,6,5,3,2,6,5,6,5,6,4,6,6,4,3,5]
d = {}
for i in l:
  d[i] = d.get(i,0)+1

for key,value in d.items() :
  if value > 1:
    print(key,end=" ")

print()
