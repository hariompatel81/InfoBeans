# 29. Suppose a one-dimensional array AR containing integers is arranged in ascending order. Write a java program to search for an integer from AR with the help of Binary search method, 

l = [1,3,4,5,6,7,8]
s = 7
i=0
j=len(l)-1

while i < j :
  mid = (i+j)//2
  if s == l[mid] :
    print("Element found")
    print(mid)
    break
  elif l[mid] < s :
    i = mid+1
  else :
    j = mid-1
   