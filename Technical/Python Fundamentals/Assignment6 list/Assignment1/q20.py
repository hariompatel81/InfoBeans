'''
Q.19) Find Maximum product contigeous sub array 

Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.
Example 1:
Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is [6, -3, -10] which gives product as 180.
Example 2:
Input:
N = 6
Arr[] = {2, 3, 4, 5, -1, 0}
Output: 120
Explanation: Subarray with maximum product
is [2, 3, 4, 5] which gives product as 120.

'''
l = [2, 3, 4, 5, -1, 0]
max = float('-inf')
for i in range(len(l)-1) :
  cs = l[i]
  for j in range(i+1,len(l)) :
    cs = cs * l[j]
    if max < l[i] :
      max = l[i]
    if max < l[j] :
      max = l[j]
    if max < cs :
      max = cs

print("Sub array with maximum product :",max)
