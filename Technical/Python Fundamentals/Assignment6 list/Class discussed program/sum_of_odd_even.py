# WAP to calculate the sum of even and odd element in list.
l = [2,3,4,3,4,3,53,5,3,3,43]
esum = 0
osum = 0
for i in l :
  if i%2 == 0 :
    esum += 1
  else :
    osum += 1

print(f"Sum of even elements of list : {esum}")
print(f"Sum of odd elements of list : {osum}")

