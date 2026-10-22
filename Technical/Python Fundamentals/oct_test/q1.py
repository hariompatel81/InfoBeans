'''
Q1. If-Else — Number Classification (5 Marks)

Write a program that accepts an integer and checks whether it is a Harshad number.

A number is a Harshad number if it is divisible by the sum of its digits.

Example:

Input: 18

Output: Harshad Number (18 is divisible by 1 + 8 = 9)
'''

def check_harshad(n):
  x = n
  sum = 0
  while x:
    remainder = x%10
    sum += remainder
    x = x//10

  if n%sum == 0:
    print(f"Harshad Number : ({n} is divisible by {sum})")
  else :
    print(f"{n} is not harshad Number.")

n = int(input("Enter number :"))
check_harshad(n)
