# 16) …... -6	-3	0	3	6	9	……. n terms [where n is divisible 3]

n = int(input("Enter a number :"))

for i in range(-n, n+1) :
  if i % 3 == 0 :
    print(i,end=" ")
  

