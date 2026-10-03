'''
Q.14. Find the first non-repeating elment in given array of integers
Find the first non-repeating element in a given array arr of N integers.
Note: Array consists of only positive and negative integers and not zero.
Example 1:
Input : arr[] = {-1, 2, -1, 3, 2}
Output : 3
Explanation:
-1 and 2 are repeating whereas 3 is 
the only number occuring once.
Hence, the output is 3.

Example 2:
Input : arr[] = {1, 1, 1}
Output : 0
 

'''
# l = [-1,2,-1,3,2]
# found = True
# for i in range(len(l)-1) :
#   temp = l[len(l)-1]
#   for j in range(len(l)-1,0,-1) : 
#     if temp ==  l[j-1] :
#       found = False
#     l[j] = l[j-1]
#   l[0] = temp

#   if found :
#     print("First non-repeating element :",temp)
  