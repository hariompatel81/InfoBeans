# 11) WAP to print N odd numbers.

n = int(input("How much odd number do you want :"))

i = 1
while n :
  if i % 2 != 0 :
    print(i,end=" ")
    n -= 1
  i += 1