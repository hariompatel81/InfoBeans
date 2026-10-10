'''
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
'''
l1 = [1, 5, 6, 10, 20, 40, 80]
l2 = [6, 7, 20, 80, 100]
l3 = [3, 4, 6, 15, 20, 30, 70, 80, 120]
i=0
j=0
k=0
intersection = []

while i<len(l1) and j<len(l2) and k<len(l3) :
  if l1[i] == l2[j] == l3[k] :
    intersection.append(l1[i]) 
    i += 1
    j += 1
    k += 1
  elif l1[i] < l2[j] : #and l1[i] < l3[k] :
    i += 1
  elif l2[j] < l3[k] : #and l2[j] < l1[i] :
    j += 1
  else :
    k += 1

print("Commaon elements :",intersection)

