'''
Q4. Prime Numbers in a Range — Nested Loops

Write a Python program that accepts two numbers start and end and prints all prime numbers between them.

Also display the total number of prime numbers found.

Example:

Enter start: 10
Enter end: 30

Prime numbers:
11 13 17 19 23 29

Total prime numbers: 6

Restriction: Do not use any built-in function/library for checking whether a number is prime.
'''
start = int(input("Enter start :"))
end = int(input("Enter end :"))
print(f"Prime numbers : ",end=" ")
count = 0
for i in range(start,(end+1)) :
  prime = True
  for j in range(2,(i//2)+1) :
    if i%j == 0 :
      prime = False
      break

  if prime :
    print(i,end=" ")
    count += 1

print(f"\nTotal prime numbers : {count}")

