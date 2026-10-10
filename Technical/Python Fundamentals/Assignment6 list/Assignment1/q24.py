# 23. Write a Java program to find the sum and average of one dimensional integer array. 

l = [2,4,2,5,3,5,2,56,3]
sum = 0
average = 0

if len(l) == 0 :
  print("List is empty.")
else :
  for i in l :
    sum += i

  average = (sum / len(l))
  print("Sum is ",sum)
  print(f"Average is {average:.2f}")
  
