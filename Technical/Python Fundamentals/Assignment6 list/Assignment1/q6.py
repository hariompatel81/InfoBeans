# Q.5 Find occurance of an integer number in array.

l = [564,6,4,7,6,8,4,23,6,7,7,6,5,4,3,2]
n = int(input("Enter integer :"))
count = 0
for i in range(len(l)) :
  if n == l[i] :
    count += 1

print("Occurence of integer is :",count)

