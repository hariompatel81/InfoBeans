# Q.3 Write a program to reverse the array.
l = [4,2,5,2,5,3,5,7,4,7]
left = 0
right = len(l)-1
print("Before :",l)
while left < right :
  l[left],l[right] = l[right],l[left]
  left += 1
  right -= 1

print("After : ",l)