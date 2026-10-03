# WAP to search element at index
item = int(input("Enter a element :"))
l = [2,3,4,4,5,54,6,4,6,4,6]
for i in range(len(l)) :
  if l[i] == item :
    print(f"Element found at index : {i}")
    break
else :
  print(f"Element not found")

# for all elements
result = []
for i in range(len(l)) :
  if item == l[i] :
    result.append(i)
print(result)

if result :
  s = "Element found at :"
  for i in result :
    s += " " + str(i) 
  print(s)
else :
  print("Element not found.")  