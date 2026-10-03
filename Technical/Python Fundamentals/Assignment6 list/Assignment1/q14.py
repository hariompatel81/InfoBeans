# Find the first repeating element in array of integers
l = [1,5,3,5,7,3,6,9]
found = None
for i in range(len(l)-1) :
  for j in range(i+1,len(l)) :
    if l[i] == l[j] :
      print("First repeating element :",l[i])
      found = l[i]
      break
  if found is not None :
    break

else :
  print("All element are unique.")

# optimised way
l = [1,5,3,5,7,3,6,9]
result = None
s = set()
for i in range(len(l)-1,-1,-1) :
  if l[i] in s :
    result = l[i] 
  s.add(l[i])

print("First repeating element is.",result)