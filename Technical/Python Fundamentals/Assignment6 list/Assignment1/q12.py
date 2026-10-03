'''
Q.11 Count pair with given sum.
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

Example 1:
Input:
N = 4, K = 6
arr[] = {1,5,7,1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.

Example 2:
Input:
N = 4, X = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation:
Each 1 will produce sum 2 with any 1.
'''
l = [1,3,4,5,3,53,3,24,4,3,4,3,2,43,3]
k = 6
count = 0
for i in range(len(l)-1) :
  for j in range(i+1,len(l)) :
    if k == l[i] + l[j] :
      count += 1

print("Pair count :",count)