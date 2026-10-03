'''
Q.21 Max Sum in configuration

Given an array(0-based indexing), you have to find the max sum of i*A[i] where A[i] is the element at index i in the array.The only operation allowed is to rotate(clock-wise or counter clock-wise) the array any number of times.
Example 1:
Input:
N = 4
A[] = {8,3,1,2}
Output: 29
Explanation: Above the configuration
possible by rotating elements are
3 1 2 8 here sum is 3*0+1*1+2*2+8*3 = 29
1 2 8 3 here sum is 1*0+2*1+8*2+3*3 = 27
2 8 3 1 here sum is 2*0+8*1+3*2+1*3 = 17
8 3 1 2 here sum is 8*0+3*1+1*2+2*3 = 11
Here the max sum is 29
'''
l = [8,3,1,2]
sum = 0
max = float('-inf')
for i in range(len(l)) :
  # to find max
  for j in range(len(l)) :
    sum += j*(l[j])
  if max < sum :
      max = sum
  sum = 0

  # to rotate array
  temp = l[-1]
  for j in range(len(l)-1,0,-1) :
    l[j] = l[j-1]

  l[0] = temp

print("Max",max)


