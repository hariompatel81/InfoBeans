'''
Q.7 Sub array with given sum
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

Example 1:
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

Example 2:
Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
1 <= N <= 105
1 <= Ai <= 109

'''
l = [1,2,3,4,5,6,7,8,9,10]
s = 15
left = 0
right = 0
cs = 0
while left <= right:
  cs = cs + l[right]

  while cs > s :
    cs = cs - l[left]
    left += 1

  if s == cs :
    print("Sub array position :",[left+1,right+1])
    break

  right += 1
  
else :
  print("Not any sub array exist...")

# another aproach
l = [1,2,3,4,5,6,7,8,9,10]
s = 15
left = 0
right = 0
cs = 0
while left <= right:
  cs = cs + l[right]

  if cs > s :
    cs = cs - l[left]
    left += 1
  elif cs < s :
    right += 1

  if s == cs :
    print("Sub array position :",[left+1,right+1])
    break
else :
  print("Not any sub array exist...")

    


  

