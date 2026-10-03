'''
Q.1 Peak an element

An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, find the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0.

Example 1:
Input:
N = 3
arr[] = {1,2,3}
Output: 1
Explanation: index 2 is 3.
It is the peak element as it is 
greater than its neighbour 2.
Example 2:
Input:
N = 2
arr[] = {3,4}
Output: 1
Explanation: 4 (at index 1) is the 
peak element as it is greater than 
its only neighbour element 3.
Constraints:
1 ≤ N ≤ 105
1 ≤ A[] ≤ 106
'''

arr = [1,3,2,4,3,5,3,5,3]

if len(arr)==1 or arr[0] > arr[1] or arr[len(arr)-2] < arr[len(arr)-1] :
   print(1)
else :
  for i in range(1,len(arr)) :
    if arr[i] > arr[i-1] or arr[i] > arr[i+1] :
      print(1)
      break
  else :
    print(0)
