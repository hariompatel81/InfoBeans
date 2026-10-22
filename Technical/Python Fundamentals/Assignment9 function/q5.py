# 5. Count the number of words in a sentence.

# def cword1(s) :
#   count = 1
#   s = s.strip()
#   for ch in s:
#     if ch == " ":
#       count += 1
#   return count

def cword(s) :
  count = 0
  s = s.strip()
  l = s.split(' ')
  for word in l:
    if word != "":
      count += 1
  return count

s = input("Enter string :")
# print(f"Word count : {cword1(s)}")
print(f"Word count : {cword(s)}")