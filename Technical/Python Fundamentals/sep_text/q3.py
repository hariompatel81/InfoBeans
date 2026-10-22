'''
Q3. Number Analysis — Loop + if-else

Write a Python program that accepts a positive integer N and prints:

Sum of all digits
Number of digits
Largest digit
Smallest digit
Whether the number is a palindrome

Example:

Enter number: 12321

Sum of digits: 9
Number of digits: 5
Largest digit: 3
Smallest digit: 1
Palindrome: Yes

Restriction: Do not convert the number into a string.
'''

n = int(input("Enter a number :"))
if n < 0 :
  print("Invalid input")
else :
  min = 10
  max = 0
  reverse = 0
  sum = 0
  count = 0
  x = n
  while x :
    count += 1
    print(count)
    x //= 10

  x = n
  while x :
    rem = x%10
    sum += rem
    reverse  = reverse*10 + rem
    x //= 10

    if rem > max :
      max = rem
    elif rem < min :
      min = rem

  if n == reverse :
    pelindrome = "Yes"
  else :
    pelindrome = "No"

  print(f"Sum of digit : {sum}")
  print(f"Number of digit : {count}")
  print(f"Largest digit : {max}")
  print(f"Smallest digit : {min}")
  print(f"Palindrome : {pelindrome}")






