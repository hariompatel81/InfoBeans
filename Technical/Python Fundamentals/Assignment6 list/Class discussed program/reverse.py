# reverse an array
l = [10,20,30,40,50]
left = 0
right = len(l)-1
while left < right :
  l[left],l[right] = l[right],l[left]
  left += 1
  right -= 1

print(l) 
