# 6. Find the length of a string without using len().

def length(s) :
  count = 0
  for _ in s :
    count += 1
  return count

s = input("Enter string :")
print(f"Length of a string {length(s)}")