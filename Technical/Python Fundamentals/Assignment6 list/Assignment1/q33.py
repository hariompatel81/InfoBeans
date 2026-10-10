# Impleament binary search

# binary array work only on sorted array
l = [1,2,3,4,5,6,7,8]
s = 7
i = 0
j = len(l)-1
mid = (i+j)//2

while i != j :
  mid = (i+j)//2
  if l[mid] == s :
    print("Element found at :",mid)
    break
  elif s < l[mid] :
    j = mid-1
  else :
    i = mid+1

   