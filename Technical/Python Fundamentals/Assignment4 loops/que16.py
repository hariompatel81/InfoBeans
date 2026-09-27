# 16) …... -6	-3	0	3	6	……. n terms [where n is divisible 3]

n = int(input("Enter a number witch is multiple of 3 :"))
# print this sereis for n
for i in range(-n,n+1,3) :
    print(i,end=" ")
print()

# -6 -3 0 3 6 .......n
count = 0
item = -9
while count < n :
  count += 1
  item += 3
  print(item,end=" ")

print()
print(f"{n}th term of the series : {item}")

  

