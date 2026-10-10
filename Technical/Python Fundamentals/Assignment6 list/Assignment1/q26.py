# 25. Write a Java program to reverse the element of an integer 1-D array. 

l = [1,2,5,4,5,6,7]
print("List",l)
i = 0
j = len(l)-1
while i < (len(l)//2) :
  temp = l[i]
  l[i] = l[j]
  l[j] = temp

  # another way
  # l[i] = l[i] + l[j]
  # l[j] = l[i] - l[j]
  # l[i] = l[i] - l[j]

  # pythonic way
  # l[i],l[j] = l[j],l[i]
  i+=1
  j-=1

print("Reversed list :",l)
