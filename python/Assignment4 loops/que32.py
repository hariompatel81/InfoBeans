# W.A.P to count number of even and odd in a digit

number = int(input("Enter a number :"))

even = 0
odd = 0

for i in range(number,0,-1) :
  remainder = number % 10
  if remainder % 2 == 0:
    even += 1
  else :
    odd += 1 
  number //= 10
  if number == 0 :
    break

print(f"Enven digit count is : {even}")
print(f"Odd digit count is : {odd}")


