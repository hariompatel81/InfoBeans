# sliding window
l = [2,4,24,2,5,2,5,2,5,2,4,1]
target = 6
cs = 0
left = 0
right = 0
while left <= right :
  cs = cs + l[right]
  while cs > target and left < right:
    cs = cs - l[left]
    left += 1
    break
  if cs == target :
    print(f"{left}, {right}")
    break
  right += 1


