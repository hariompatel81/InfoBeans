'''
Q.22) Java program to find nearest lesser and greater element in array
Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.
Example:
    Input:
    Enter the number of elements for the arrray : 3  
 
    Enter the elements for array_1.. 
    array_1[0] : 1   
    array_1[1] : 2   
    array_1[2] : 3   
 
    Enter the number : 2 
 
    Output:
    Element lesser than 2 is : 1 
    Element greater than 2 is : 3

'''
n = int(input("Enter length of an array :"))
l = []
for i in range(n) :
  ele = int(input("Enter element :"))
  l.append(ele)

target = int(input("Enter number witch nearest greater and lesser element you want to find :"))

print("List is",l)

for i in range(n-1) :
  for j in range(i+1, n) :
    if l[i] > l[j] :
      l[i],l[j] = l[j],l[i]

temp = None
for i in range(n) :
  if l[i] == target :
    temp = i
    break

if n == 1 or n == 0:
  print("nearest greater and lesser element are not present.")
elif temp == 0 and (len(l) > temp) :
  print("Lesser is not available and greater is ",l[temp+1])
elif temp == n-1 and (len(l) > temp):
  print("Greater is not available and lesser is ",l[temp-1])
else :
  while temp > 0 and l[temp] == l[temp-1] :
    temp -= 1
  while temp < n-1 and l[temp] == l[temp+1] :
    temp += 1
  if temp > 0 and temp < n-1 :
    print(f"Lesser is {l[temp-1]} and Greater is {l[temp+1]}")

