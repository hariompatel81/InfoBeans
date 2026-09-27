# WAP to interchange first and last digit of a number 

n = int(input("Enter a number :"))
x = n
count = 0
while x :
  count += 1
  x //= 10

x = n
for i in range(1,count+1) :
  if i == 1 :
    last_digit = x % 10
    
  elif i == count :
    first_digit = x % 10
    
  x //= 10

x = n
n = n - first_digit*(10**(count-1))
n = n + last_digit*(10**(count-1))
n = n - last_digit
n = n + first_digit

print(f"After interchenging first-last of {x} is {n}")


