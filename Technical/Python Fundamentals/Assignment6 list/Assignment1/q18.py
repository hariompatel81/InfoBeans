'''
Q.17 Find it there is any subarray with sum equals to zero
Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.
Example 1:
Input:
5
4 2 -3 1 6

Output: 
Yes

Explanation: 
2, -3, 1 is the subarray 
with sum 0.
Example 2:
Input:
5
4 2 0 1 6

Output: 
Yes

Explanation: 
0 is one of the element 
in the array so there exist a 
subarray with sum 0.

'''
l = [4, 2, 0, 1, 6]
 
flag = False
for i in range(len(l)-1) :
  cs = l[i]
  for j in range(i+1,len(l)) :
    cs = cs + l[j]
    if l[j] == 0 or l[i] == 0 or cs == 0:
      print("Yes")
      flag = True
      break
    
  if flag :
    break
  