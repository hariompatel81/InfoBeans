'''
Q.9 Find the Union and Intersaction of two sorted array.
Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays. 
Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.
Example 1:
Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
Example 2:
Input:
6 2 
85 25 1 32 54 6
85 2 
Output: 
7
Explanation: 
85, 25, 1, 32, 54, 6, and
2 are the elements which comes in the
union set of both arrays. So count is 7.
'''
l1 = [1,2,2,2,3,4,5]
l2 = [1,2,2,3,4]
i=0
j=0
uniun = []
intersection = []

while i<len(l1) and j<len(l2) :
  
  if l1[i] == l2[j] :
    if not uniun or uniun[-1] != l1[i] :
      uniun.append(l1[i]) 
      intersection.append(l1[i])
    i += 1
    j += 1
    
    # if not intersection or intersection[-1] != l1[i] :
    #   intersection.append(l1[i])
    #   i += 1
    #   j += 1

  elif l2[j] < l1[i] :
    if not uniun or uniun[-1] != l2[j] :
      uniun.append(l2[j])
    j+=1

  else :
    if not uniun or uniun[-1] != l1[i] :
      uniun.append(l1[i])
    i+=1

while i < len(l1) :
  if not uniun or uniun[-1] != l1[i] :
    uniun.append(l1[i])
  i+=1

while j < len(l2) :
  if not uniun or uniun[-1] != l2[j] :
    uniun.append(l2[j])
  j+=1

print("Uniun :",uniun)
print("Intersection :",intersection)




