# 1, 4, 9, 16, 25 ….. 

n = int(input("Enter a number :"))
i = 1
odd = 0
x = n
while n > 0 :
  if i%2 != 0 :
    odd += i
    print(odd,end=", ")
    n -= 1
  i += 1

print()
print(f"{x}th term is {odd}")

