# given an array of two integers l1 and an integer target, return the indices of the two numbers such that they add up to the target.
# l1 = [1,5,6,8,9]
# target = 12

# Brute force approach

l1 = [1,5,7,8,9]
target = 12
result = []

for i in range(len(l1)-1) :
  for j in range(i+1,len(l1)) :
    if l1[i] + l1[j] == target :
      result.extend([i,j])
      print(result)
      break
  if result :
    break
else :
  print("Not found any indices..")

# Two pointer approach
l2 = [2,7,11,15]
target = 9
i = 0
j = len(l2)-1
result = []
while i<j :
  sum = l2[i] + l2[j]
  if sum == target :
    result.extend([i,j])
    print(result)
    break
  elif sum > target :
    j -= 1
  else :
    i += 1
else :
  print("Not found any indices..")
